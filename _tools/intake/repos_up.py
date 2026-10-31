"""repos_up.py - REPOS ARE UP (BOLO 165). Zero tokens, stdlib only.

Chief 10/19: "when I say repos are up, I want you to look at the Firefox tabs that are open and just grab all those".
Reads Firefox's open tabs from a COPY of the session file, keeps every github.com/<owner>/<repo> link, and prints the
repo list plus the intake hand-off line (the intake skill takes "intake <links>"; step 1 is repo_scan.py).

Runs on the proword only: reading the live profile is named by Chief's "repos are up", never on its own.

The session file: <profile>/sessionstore-backups/recovery.jsonlz4 while Firefox runs, <profile>/sessionstore.jsonlz4
after it closes. Format mozlz4: 8-byte magic b"mozLz40\\0", a 4-byte little-endian size, then one LZ4 block. The file
is copied to a temp folder first and only the copy is read; nothing in the profile is touched. Nothing is written.

Usage:
  python _tools/intake/repos_up.py                 # newest Firefox profile's session file
  python _tools/intake/repos_up.py --file F        # any mozlz4 (or plain JSON) session file, e.g. a test fixture
  python _tools/intake/repos_up.py --json          # the data as JSON

Kept: github.com/<owner>/<repo>, cut back to the repo (/tree, /blob, /issues, query and fragment dropped), deduped
case-blind, in tab order. Skipped: github.com/<owner> alone, gists, settings, notifications and GitHub's own pages.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import struct
import sys
import tempfile
import urllib.parse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

MAGIC = b"mozLz40\0"

# First path parts on github.com that are GitHub's own pages, never an owner.
RESERVED = {
    "settings", "notifications", "orgs", "organizations", "marketplace", "explore", "topics", "trending",
    "collections", "sponsors", "login", "logout", "signup", "join", "session", "sessions", "password_reset",
    "features", "pricing", "about", "enterprise", "search", "pulls", "issues", "new", "codespaces", "apps",
    "users", "stars", "watching", "dashboard", "account", "customer-stories", "security", "readme", "team",
    "site", "contact", "git-guides", "events", "copilot", "github-copilot", "mobile", "nonprofit", "education",
    "resources", "solutions", "discussions", "home", "dashboard-feed", "watchlist", "repositories", "downloads",
    "gist", "raw", "assets", "blog", "changelog", "premium-support", "sitemap", "terms", "privacy",
}
OWNER_RX = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
REPO_RX = re.compile(r"^[A-Za-z0-9._-]{1,100}$")


def lz4_block_decode(src: bytes, size: int) -> bytes:
    """Decode one raw LZ4 block (no frame header) of known decompressed size."""
    out = bytearray()
    i, n = 0, len(src)
    while i < n:
        token = src[i]
        i += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[i]
                i += 1
                lit += b
                if b != 255:
                    break
        out += src[i:i + lit]
        i += lit
        if i >= n:  # the last sequence carries literals only
            break
        off = src[i] | (src[i + 1] << 8)
        i += 2
        if off == 0 or off > len(out):
            raise ValueError("bad LZ4 offset")
        mlen = token & 15
        if mlen == 15:
            while True:
                b = src[i]
                i += 1
                mlen += b
                if b != 255:
                    break
        mlen += 4
        start = len(out) - off
        if off >= mlen:
            out += out[start:start + mlen]
        else:  # overlapping copy, byte by byte
            for k in range(mlen):
                out.append(out[start + k])
    if size and len(out) != size:
        raise ValueError(f"LZ4 size mismatch: got {len(out)}, header says {size}")
    return bytes(out)


def read_session(path: str) -> dict:
    """Copy the session file to a temp folder, decode the copy, return the session JSON."""
    with tempfile.TemporaryDirectory(prefix="repos_up_") as tmp:
        copy = os.path.join(tmp, "session.copy")
        shutil.copyfile(path, copy)
        with open(copy, "rb") as f:
            raw = f.read()
    if raw[:8] == MAGIC:
        (size,) = struct.unpack("<I", raw[8:12])
        raw = lz4_block_decode(raw[12:], size)
    return json.loads(raw.decode("utf-8"))


def find_session() -> str | None:
    """The newest session file across the Firefox profiles (the proword names the box)."""
    base = os.path.join(os.environ.get("APPDATA", ""), "Mozilla", "Firefox", "Profiles")
    cands = glob.glob(os.path.join(base, "*", "sessionstore-backups", "recovery.jsonlz4"))
    if not cands:
        cands = glob.glob(os.path.join(base, "*", "sessionstore.jsonlz4"))
    return max(cands, key=os.path.getmtime) if cands else None


def open_tab_urls(session: dict) -> tuple[list[str], int, int]:
    """The current URL of every open tab, in window and tab order. Returns (urls, windows, tabs)."""
    urls, nwin, ntab = [], 0, 0
    for win in session.get("windows") or []:
        nwin += 1
        for tab in win.get("tabs") or []:
            entries = tab.get("entries") or []
            if not entries:
                continue
            ntab += 1
            idx = tab.get("index") or len(entries)  # 1-based
            idx = min(max(int(idx), 1), len(entries))
            url = entries[idx - 1].get("url")
            if url:
                urls.append(url)
    return urls, nwin, ntab


def repo_of(url: str) -> tuple[str, str] | None:
    """(owner, repo) when the URL is a github.com repo page, else None."""
    try:
        u = urllib.parse.urlsplit(url)
    except ValueError:
        return None
    if u.scheme not in ("http", "https") or (u.hostname or "").lower() not in ("github.com", "www.github.com"):
        return None
    parts = [p for p in u.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    if repo.lower().endswith(".git"):
        repo = repo[:-4]
    if owner.lower() in RESERVED or not OWNER_RX.match(owner) or not REPO_RX.match(repo) or repo in (".", ".."):
        return None
    return owner, repo


def collect(urls: list[str]) -> tuple[list[dict], int]:
    repos, seen, other_gh = [], set(), 0
    for url in urls:
        hit = repo_of(url)
        if not hit:
            host = (urllib.parse.urlsplit(url).hostname or "").lower() if "://" in url else ""
            if host.endswith("github.com"):
                other_gh += 1
            continue
        key = (hit[0].lower(), hit[1].lower())
        if key in seen:
            continue
        seen.add(key)
        repos.append({"owner": hit[0], "repo": hit[1], "url": f"https://github.com/{hit[0]}/{hit[1]}"})
    return repos, other_gh


def main() -> int:
    ap = argparse.ArgumentParser(description="REPOS ARE UP: the GitHub repos in Firefox's open tabs (BOLO 165)")
    ap.add_argument("--file", help="a session file to read instead of the newest Firefox profile's")
    ap.add_argument("--json", action="store_true", help="print the data as JSON")
    a = ap.parse_args()

    path = a.file or find_session()
    if not path or not os.path.isfile(path):
        msg = "no Firefox session file found" if not a.file else f"no such file: {a.file}"
        print(json.dumps({"error": msg}) if a.json else "repos are up · " + msg)
        return 1
    try:
        urls, nwin, ntab = open_tab_urls(read_session(path))
    except (ValueError, OSError, UnicodeDecodeError, IndexError) as e:
        print(json.dumps({"error": f"could not read the session file: {e}"}) if a.json
              else f"repos are up · could not read the session file: {e}")
        return 1
    repos, other_gh = collect(urls)
    links = " ".join(r["url"] for r in repos)
    data = {
        "source": "file" if a.file else "firefox",
        "windows": nwin,
        "tabs": ntab,
        "repos": repos,
        "github_not_repo": other_gh,
        "handoff": f"intake {links}" if repos else "",
        "scan": f"python _tools/intake/repo_scan.py {links}" if repos else "",
    }
    if a.json:
        print(json.dumps(data, indent=1))
        return 0
    print(f"repos are up · {len(repos)} repo(s) from {ntab} tab(s) in {nwin} window(s)"
          + (f" · {other_gh} other GitHub tab(s) skipped" if other_gh else ""))
    w = max((len(r["owner"]) + len(r["repo"]) + 1 for r in repos), default=0)
    for n, r in enumerate(repos, 1):
        print(f"  {n:>2}  {(r['owner'] + '/' + r['repo']).ljust(w)}  {r['url']}")
    if repos:
        print("hand-off: " + data["handoff"])
        print("scan:     " + data["scan"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
