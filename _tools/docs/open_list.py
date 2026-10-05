"""Gather every OPEN gap in the core docs (BOLO 102). Usage: python _tools/docs/open_list.py  → _tools/docs/out/open_gaps.json + a count."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(ROOT, "ShroomsQ", "_CANON", "_DOCS")
gaps = []
for dp, _, fns in sorted(os.walk(DOCS)):
    for f in sorted(fns):
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        for i, line in enumerate(io.open(p, encoding="utf-8").read().splitlines(), 1):
            m = re.search(r"\*\*OPEN:\*\*\s*(.+)", line)
            if m:
                rel = os.path.relpath(p, DOCS).replace(os.sep, "/")
                sysd, doc, page = rel.split("/")
                gaps.append({"n": len(gaps) + 1, "system": sysd, "doc": doc, "page": page, "line": i, "gap": m.group(1).strip()})
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
io.open(os.path.join(HERE, "out", "open_gaps.json"), "w", encoding="utf-8").write(json.dumps(gaps, ensure_ascii=False, indent=1))
print(f"{len(gaps)} OPEN gaps → _tools/docs/out/open_gaps.json")
