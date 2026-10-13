"""repo_scan.py — BOLO 140, the repo intake (Chief 10/12: "I have a whole bunch of GitHub repos ... adding them to our
process ... tools so you have to think less"). Zero tokens: one GitHub repo becomes a scan file the specialists read.

For each repo URL: metadata (stars, license, last push, size), the file tree (paths only), the README, and counts of the
Claude Code parts it ships (agents, skills, commands, hooks, MCP configs, install scripts). Writes
_PRIVATE/intake-repos/<owner>__<repo>/scan.json + README.md, and prints one line per repo.

Usage: python _tools/intake/repo_scan.py <github url> [<github url> ...]
       (set GITHUB_TOKEN in the environment to lift the 60-requests-an-hour limit; never commit a token)
"""
import base64
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "intake-repos")
API = "https://api.github.com/repos/"


def get(url):
    h = {"User-Agent": "command-intake/0.1", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        h["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60))


def parts(paths):
    low = [p.lower() for p in paths]
    count = lambda rx: sum(1 for p in low if re.search(rx, p))
    return {
        "agents": count(r"(^|/)agents/[^/]+\.md$"),
        "skills": count(r"(^|/)skills/[^/]+/skill\.md$"),
        "commands": count(r"(^|/)commands/[^/]+\.md$"),
        "hooks": count(r"(^|/)hooks?/|hooks\.json$"),
        "mcp": count(r"mcp[^/]*\.json$|(^|/)mcp/"),
        "installers": count(r"(^|/)(install|setup)\.(sh|ps1|py|js)$|package\.json$"),
        "python": count(r"\.py$"),
        "node": count(r"\.(js|ts|mjs)$"),
    }


def scan(url):
    m = re.search(r"github\.com/([^/\s]+)/([^/\s?#]+)", url)
    if not m:
        return f"skip: not a GitHub repo URL: {url}"
    owner, repo = m.group(1), m.group(2).removesuffix(".git")
    meta = get(API + f"{owner}/{repo}")
    tree = get(API + f"{owner}/{repo}/git/trees/{meta['default_branch']}?recursive=1")
    paths = [t["path"] for t in tree.get("tree", []) if t["type"] == "blob"]
    try:
        rd = get(API + f"{owner}/{repo}/readme")
        readme = base64.b64decode(rd["content"]).decode("utf-8", "replace")
    except Exception:
        readme = ""
    d = os.path.join(OUT, f"{owner}__{repo}")
    os.makedirs(d, exist_ok=True)
    out = {"url": meta["html_url"], "description": meta.get("description"), "stars": meta.get("stargazers_count"),
           "license": (meta.get("license") or {}).get("spdx_id"), "pushed": meta.get("pushed_at"), "archived": meta.get("archived"),
           "size_kb": meta.get("size"), "default_branch": meta["default_branch"], "files": len(paths),
           "truncated_tree": tree.get("truncated", False), "parts": parts(paths), "paths": paths[:4000]}
    json.dump(out, open(os.path.join(d, "scan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(readme)
    p = out["parts"]
    return (f"{owner}/{repo} · ★{out['stars']} · {out['license']} · pushed {str(out['pushed'])[:10]} · {out['files']} files · "
            f"agents {p['agents']} · skills {p['skills']} · commands {p['commands']} · hooks {p['hooks']} · mcp {p['mcp']} · "
            f"installers {p['installers']} · py {p['python']} / js {p['node']} -> {os.path.relpath(d, ROOT)}")


if __name__ == "__main__":
    for u in sys.argv[1:]:
        try:
            print(scan(u))
        except Exception as e:
            print(f"fail: {u}: {e}")
