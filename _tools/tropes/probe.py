# BOLO 89 · probe candidate TV Tropes index pages: does the page exist, how many trope entries does it list,
# how many of those are new to the register + plot index. Read-only; 1 request/second.
import json, re, sys, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, "_tools/tropes")
from fetch import get, article, ENTRY, LINK
have = set(json.load(open("_tools/tropes/data/domains/index.json", encoding="utf-8"))) | set(json.load(open("_tools/tropes/data/index.json", encoding="utf-8")))
cands = sys.argv[1:]
for slug in cands:
    try:
        url, page = get(slug)
    except Exception as e:
        print(f"{slug:28} ERR {str(e)[:40]}"); time.sleep(1); continue
    art = article(page)
    ents = set(m[0] for m in ENTRY.findall(art)) or set(m[0] for m in LINK.findall(art))
    real = url.rsplit("/", 1)[-1]
    print(f"{slug:28} -> {real:28} entries {len(ents):4}  new {len(ents - have):4}")
    time.sleep(1)
