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
import urllib.parse
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


TEXT_EXT = (".md", ".json", ".py", ".js", ".ts", ".mjs", ".cjs", ".sh", ".ps1", ".yml", ".yaml", ".toml", ".txt", ".cfg",
            ".ini", ".bat", ".cmd", ".html", ".tsx", ".jsx", ".rb", ".go", ".rs", ".mdc")
CODE_EXT = (".py", ".js", ".ts", ".mjs", ".cjs", ".sh", ".ps1", ".tsx", ".jsx", ".rb", ".go", ".rs", ".bat", ".cmd")
MAX_FETCH = 400
RISK_RX = {
    "hooks": re.compile(r'"hooks"\s*:|\b(PreToolUse|PostToolUse|SessionStart|UserPromptSubmit)\b'),
    "installers": re.compile(r"\bnpm\s+i(nstall)?\b|\bnpx\b|\bpip3?\s+install\b|\buv\s+(pip|tool|run|add|sync)\b|curl[^\n|]*\|\s*(ba)?sh|"
                             r"irm[^\n|]*\|\s*iex|Invoke-WebRequest|\bsetup\.sh\b|\binstall\.ps1\b", re.I),
    "network": re.compile(r"\brequests\.(get|post|put|delete|request|Session)|\burllib\b|\bfetch\(|\baxios\b|\bhttp\.client\b|"
                          r"https?://(?!(?:[\w.-]*\.)?github\.com|raw\.githubusercontent\.com)[\w.-]+\.[a-z]{2,}"),
    "blobs": re.compile(r"[A-Za-z0-9+/=]{200,}"),
    "telemetry": re.compile(r"posthog|sentry|telemetry|analytics|mixpanel", re.I),
    "autotrigger": re.compile(r"always use|proactively|automatically run|MUST use this", re.I),
    "injection": re.compile(r"ignore (all )?previous|disregard your instructions|you are now", re.I),
}


def risk_pass(owner, repo, branch, tree_items):
    """Fetch text files up to 200 KB (cap MAX_FETCH) and count risk patterns. Returns the risk dict."""
    res = {k: {"files": 0, "hits": 0, "examples": []} for k in RISK_RX}
    cand = [t for t in tree_items if t["type"] == "blob" and t["path"].lower().endswith(TEXT_EXT)
            and 0 < t.get("size", 0) <= 200_000][:MAX_FETCH]
    scanned = 0
    for t in cand:
        p = t["path"]
        low = p.lower()
        try:
            req = urllib.request.Request(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{urllib.parse.quote(p)}",
                                         headers={"User-Agent": "command-intake/0.1"})
            raw = urllib.request.urlopen(req, timeout=30).read()
        except Exception:
            continue
        if b"\x00" in raw[:2000]:
            continue
        txt = raw.decode("utf-8", "replace")
        scanned += 1
        is_md = low.endswith(".md") or low.endswith(".mdc")
        is_agent = is_md and bool(re.search(r"(^|/)(agents|skills|commands)/|claude\.md$", low))
        for k, rx in RISK_RX.items():
            if k == "network" and low.endswith(CODE_EXT) is False:
                continue
            if k == "autotrigger" and not is_agent:
                continue
            if k == "injection" and not is_md:
                continue
            n = len(rx.findall(txt))
            if n:
                r = res[k]
                r["files"] += 1
                r["hits"] += n
                if len(r["examples"]) < 5:
                    r["examples"].append(p)
    flags = {k: v["hits"] > 0 for k, v in res.items()}
    verdict = "STOP" if (flags["blobs"] or flags["telemetry"] or flags["injection"]) else \
        "WATCH" if (flags["hooks"] or flags["installers"] or flags["network"] or flags["autotrigger"]) else "CLEAN"
    return {"verdict": verdict, "files_scanned": scanned, "files_skipped": max(0, len(cand) - scanned), "checks": res}


def risk_line(rk):
    c = rk["checks"]
    return ("RISK " + rk["verdict"] + " · hooks {hooks} · installers {installers} · network {network} · blobs {blobs} · "
            "telemetry {telemetry} · auto-trigger {autotrigger} · injection {injection}".format(
                **{k: v["hits"] for k, v in c.items()}) + f" · {rk['files_scanned']} files read")


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
    try:
        out["risk"] = risk_pass(owner, repo, meta["default_branch"], tree.get("tree", []))
        rl = risk_line(out["risk"])
    except Exception as e:
        out["risk"] = {"verdict": "UNKNOWN", "error": str(e)}
        rl = f"RISK UNKNOWN · {e}"
    json.dump(out, open(os.path.join(d, "scan.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(rl + "\n\n" + readme)
    p = out["parts"]
    print(rl)
    return (f"{owner}/{repo} · ★{out['stars']} · {out['license']} · pushed {str(out['pushed'])[:10]} · {out['files']} files · "
            f"agents {p['agents']} · skills {p['skills']} · commands {p['commands']} · hooks {p['hooks']} · mcp {p['mcp']} · "
            f"installers {p['installers']} · py {p['python']} / js {p['node']} -> {os.path.relpath(d, ROOT)}")


if __name__ == "__main__":
    for u in sys.argv[1:]:
        try:
            print(scan(u))
        except Exception as e:
            print(f"fail: {u}: {e}")
