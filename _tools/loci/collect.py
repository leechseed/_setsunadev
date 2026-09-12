# -*- coding: utf-8 -*-
"""LOCI collect — the script half of a link-harvest research run (BOLO 51 phase 7, the formation).

Usage:  python _tools/loci/collect.py <locus.md or links.txt> [--limit N] [--batch 12]

Reads   every http(s) URL in the file (order kept)
Writes  _tools/loci/work/<name>/<nnn>.txt      the page as text (tags stripped, scripts dropped), capped 120 KB
        _tools/loci/work/<name>/manifest.json  url · status · bytes · title per link
        _tools/loci/work/<name>/brief.EXTRACT.<k>.md   one haiku brief per batch of links: text → extract.<k>.json
        _tools/loci/work/<name>/brief.WRITE.md          the sonnet brief: every extract.*.json → the register file
Then:   python _tools/loci/check.py <name> <register.md>  proves every fetched link is covered.
"""
import io, os, re, sys, json, html, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) loci-collect/1.0"

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

def to_text(h):
    h = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", " ", h)
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    t = html.unescape(h)
    t = re.sub(r"[ \t\r\f\v]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return (html.unescape(title.group(1)).strip() if title else ""), t.strip()

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    src = a[0]; limit = int(a[a.index("--limit") + 1]) if "--limit" in a else 0; batch = int(a[a.index("--batch") + 1]) if "--batch" in a else 12
    text = io.open(src, encoding="utf-8").read()
    urls = []
    for u in re.findall(r"https?://[^\s)>\]]+", text):
        u = u.rstrip(".,;")
        if u not in urls: urls.append(u)
    if limit: urls = urls[:limit]
    name = os.path.splitext(os.path.basename(src))[0].replace(".locus", "")
    wd = os.path.join(HERE, "work", name)
    man = []
    for i, u in enumerate(urls, 1):
        # curl, not urllib: this box's python cert store is stale (CERTIFICATE_VERIFY_FAILED on every host, 9/12)
        try:
            r = subprocess.run(["curl", "-sL", "--compressed", "-A", UA, "--max-time", "30", "-w", "\n__STATUS__%{http_code}", u],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            body, _, code = r.stdout.rpartition("\n__STATUS__")
            status = int(code) if code.strip().isdigit() else 0
            body = body[:1_500_000] if code else (r.stdout or r.stderr)
        except Exception as e:
            status, body = 0, str(e)
        title, t = to_text(body) if status == 200 else ("", body)
        t = t[:120_000]
        write(os.path.join(wd, f"{i:03d}.txt"), f"URL: {u}\nTITLE: {title}\nSTATUS: {status}\n\n{t}")
        man.append({"n": i, "url": u, "status": status, "bytes": len(t.encode("utf-8")), "title": title[:120]})
        print(f"{i:03d} {status:>3} {len(t)//1024:>4} KB  {title[:60] or u[:60]}")
    write(os.path.join(wd, "manifest.json"), json.dumps(man, ensure_ascii=False, indent=1))
    ok = [m for m in man if m["status"] == 200]
    k = 0
    for start in range(0, len(ok), batch):
        k += 1; chunk = ok[start:start + batch]
        files = " · ".join(rel(os.path.join(wd, f"{m['n']:03d}.txt")) for m in chunk)
        write(os.path.join(wd, f"brief.EXTRACT.{k}.md"), f"""You are EXTRACT-{k}, a collect specialist for the "{name}" locus. Model: haiku.
READ: {files}. Nothing else.
WRITE: {rel(os.path.join(wd, f'extract.{k}.json'))} — a JSON list, one object per file: {{"url": "…", "body": "<the standards body or publisher>", "items": [{{"id": "<standard number or title>", "title": "…", "domain": "<quality|software|systems|AI|risk|PM|HF|design|print|other>", "tier": "<policy|standard|handbook|procedure|list>", "free": true|false, "note": "one line"}}], "gaps": "what the page promised but did not carry"}}.
RULES: extract what the page actually lists; a page that is a list of standards yields many items, a single standard yields one; never invent an id; keep notes under 20 words. Reply with the path and the item count, nothing else.
""")
    write(os.path.join(wd, "brief.WRITE.md"), f"""You are WRITE, the register specialist for the "{name}" locus. Model: sonnet.
READ: every {rel(wd)}/extract.*.json and the locus file {rel(src)} (for the house areas it names). Nothing else.
WRITE: the register file the locus names (or {rel(os.path.join(wd, name + '.register.draft.md'))} if it does not): one table by domain (id · title · body · tier · free · maps to house area · note), then a gaps section (what no link carried), then a free-sources section. Every fetched URL appears at least once.
RULES: nothing not in the extracts; ids verbatim; under 900 lines. Reply with the path and nothing else.
""")
    print(f"COLLECT · {name} · {len(ok)}/{len(urls)} fetched · {k} extract batch(es) of {batch} · {rel(wd)}")
    print(f"next: launch EXTRACT-1..{k} (haiku, one message, gear permitting) → WRITE (sonnet) → python _tools/loci/check.py {name} <register.md>")

if __name__ == "__main__":
    main()
