"""BOLO 89 · the low-confidence second pass, step 1 (zero tokens).
For every register trope whose index line carried no definition, fetch its page and keep
the FIRST SENTENCE of the article only (the public-repo rule: one line, never page text).
Polite: one request a second; resumable.
out: _tools/tropes/data/domains/defs.json  {slug: first sentence}
"""
import json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import fetch
D = Path(__file__).parent / "data" / "domains"
idx = json.loads((D / "index.json").read_text(encoding="utf-8"))
out_p = D / "defs.json"
defs = json.loads(out_p.read_text(encoding="utf-8")) if out_p.exists() else {}
todo = [s for s, v in idx.items() if v.get("domains") and not v["def"].strip() and s not in defs]
print(f"empty defs: {len(todo)} to fetch")
for n, s in enumerate(todo, 1):
    try:
        _, page = fetch.get(s)
    except Exception as e:
        print(f"  {s}: {e}"); time.sleep(2); continue
    art = fetch.article(page)
    m = re.search(r"<p>(.*?)</p>", art, re.S)
    t = fetch.text(m.group(1)) if m else ""
    first = re.split(r"(?<=[.!?])\s", t, 1)[0][:300]
    defs[s] = first
    if n % 25 == 0:
        out_p.write_text(json.dumps(defs, ensure_ascii=False), encoding="utf-8"); print(f"  {n}/{len(todo)}")
    time.sleep(1)
out_p.write_text(json.dumps(defs, ensure_ascii=False), encoding="utf-8")
print("done")
