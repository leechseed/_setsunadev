# -*- coding: utf-8 -*-
"""CREATOR CASE fetch — the script half of the research formation (BOLO 51 phase 5). Public record only.

Usage:  python _tools/creator-cases/fetch.py <slug> [--fansly h] [--x h] [--ph model-slug] [--url URL ...]

Writes  _tools/creator-cases/work/<slug>/raw/fansly.json · x.json · wayback.cdx.json · wayback.<stamp>.html · url_<n>.html
        _tools/creator-cases/work/<slug>/manifest.json   what was fetched, status, bytes, the hard dates found
        _tools/creator-cases/work/<slug>/brief.EXTRACT.md  the haiku brief: raw → facts.json (dated facts with source URLs)
        _tools/creator-cases/work/<slug>/brief.WRITE.md    the sonnet brief: facts.json → the case file per case-brief.md
Endpoints per the creator-research-endpoints memory: Fansly public API (prices in thousandths of a dollar; createdAt in seconds),
fxtwitter, Wayback via curl (id_ raw flag, --compressed). Blocked hosts are not attempted.
"""
import io, json, os, sys, subprocess, datetime, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research-fetch/1.0"

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")
def write(p, s, mode="w"):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, mode, encoding="utf-8", newline="\n") as f: f.write(s)

def curl(url, timeout=40):
    """curl, not urllib: this box's python cert store is stale (CERTIFICATE_VERIFY_FAILED on every host, 9/12)."""
    try:
        r = subprocess.run(["curl", "-sL", "--compressed", "-A", UA, "--max-time", str(timeout), "-w", "\n__STATUS__%{http_code}", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        body, _, code = r.stdout.rpartition("\n__STATUS__")
        return (int(code) if code.strip().isdigit() else 0), (body if code else (r.stdout or r.stderr))
    except Exception as e:
        return 0, str(e)

get = curl

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    slug = a[0]; opts = {}; urls = []
    i = 1
    while i < len(a):
        if a[i] == "--url": urls.append(a[i + 1]); i += 2
        elif a[i].startswith("--"): opts[a[i][2:]] = a[i + 1]; i += 2
        else: i += 1
    wd = os.path.join(HERE, "work", slug); raw = os.path.join(wd, "raw")
    man = {"slug": slug, "when": datetime.datetime.now().isoformat(timespec="minutes"), "fetched": [], "dates": {}}
    def rec(name, url, status, body):
        p = os.path.join(raw, name); write(p, body)
        man["fetched"].append({"name": name, "url": url, "status": status, "bytes": len(body.encode("utf-8"))})
    if "fansly" in opts:
        u = f"https://apiv3.fansly.com/api/v1/account?usernames={opts['fansly']}"
        s, b = get(u); rec("fansly.json", u, s, b)
        try:
            acc = json.loads(b)["response"][0]
            for k in ("avatar", "banner"):
                ts = (acc.get(k) or {}).get("createdAt")
                if ts: man["dates"][f"fansly.{k}.createdAt"] = datetime.datetime.utcfromtimestamp(int(ts)).date().isoformat()
            man["dates"]["fansly.prices_usd"] = {str(t.get("name")): round((t.get("price") or 0) / 1000, 2) for t in acc.get("subscriptionTiers", [])}
        except Exception: pass
    if "x" in opts:
        u = f"https://api.fxtwitter.com/{opts['x']}"
        s, b = get(u); rec("x.json", u, s, b)
        try:
            usr = json.loads(b)["user"]; man["dates"]["x.joined"] = usr.get("joined"); man["dates"]["x.followers"] = usr.get("followers")
        except Exception: pass
    if "ph" in opts:
        for kind in ("model", "pornstar", "channels", "users"):
            u = f"https://web.archive.org/cdx/search/cdx?url=pornhub.com/{kind}/{opts['ph']}&output=json&limit=40"
            s, b = curl(u); rec(f"wayback.cdx.{kind}.json", u, s, b)
            try:
                rows = json.loads(b)
                if len(rows) > 1:
                    man["dates"][f"wayback.{kind}.first"] = rows[1][1][:8]; man["dates"][f"wayback.{kind}.last"] = rows[-1][1][:8]
                    stamp, orig = rows[-1][1], rows[-1][2]
                    s2, b2 = curl(f"https://web.archive.org/web/{stamp}id_/{orig}"); rec(f"wayback.{kind}.{stamp}.html", orig, s2, b2[:400_000])
                    break
            except Exception: pass
    for k, u in enumerate(urls, 1):
        s, b = get(u)
        if s == 0: s, b = curl(u)
        rec(f"url_{k}.html", u, s, b[:400_000])
    write(os.path.join(wd, "manifest.json"), json.dumps(man, ensure_ascii=False, indent=1))
    ex = f"""You are EXTRACT, the facts specialist for creator case "{slug}". Model: haiku.
READ: every file in {rel(raw)}/ and {rel(os.path.join(wd, 'manifest.json'))}. Nothing else.
WRITE: {rel(os.path.join(wd, 'facts.json'))} — a JSON list of facts, each {{"fact": "…", "date": "YYYY-MM-DD or null", "source": "<the URL from the manifest>", "confidence": "HIGH|MEDIUM|LOW", "kind": "identity|timeline|model|price|growth|quote|interview"}}.
RULES: business facts only (handles, dates, prices, counts, platforms, quotes about the business); never describe sexual content; no legal names unless the page itself uses one as the public professional name; prices in dollars (Fansly values are thousandths); every fact carries the URL it came from. Reply with the path and the fact count, nothing else.
"""
    wr = f"""You are WRITE, the case-file specialist for creator case "{slug}". Model: sonnet.
READ: {rel(os.path.join(wd, 'facts.json'))} · _tools/creator-cases/case-brief.md (the format and the hard rules) · _CANON_NODES/creator-case-alexbreecooper.md (the newest complete file, for shape).
WRITE: _CANON_NODES/creator-case-{slug}.md — the ten sections exactly as the brief lays them out; section 10 header is `## 10 · TTP`; every claim carries a source URL from facts.json; a thin record makes a thin, honest file (§8 says what is not known).
RULES: nothing not in facts.json; the brief's rules on pronouns, privacy, and content stand; do not edit the performer register; end your reply with the REGISTER NOTE: and X HANDLE: lines the brief describes, and nothing else.
"""
    write(os.path.join(wd, "brief.EXTRACT.md"), ex); write(os.path.join(wd, "brief.WRITE.md"), wr)
    ok = sum(1 for f in man["fetched"] if f["status"] == 200)
    print(f"FETCH · {slug} · {ok}/{len(man['fetched'])} ok · dates: {json.dumps(man['dates'], ensure_ascii=False)[:300]}")
    print(f"next: EXTRACT (haiku) → WRITE (sonnet) → python _tools/creator-cases/check.py {slug}")

if __name__ == "__main__":
    main()
