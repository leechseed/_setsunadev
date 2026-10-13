"""RANGE for the BOLO check context (10/13): the script reviewer at the fan-in.

Checks work/out*.json against rows.json: every open BOLO covered once, three non-empty fields each,
no [[links]] or markdown left, sentences at 20 words or fewer (advisory). Exit 1 on a blocking finding.
Usage: python _tools/bolocheck/range.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = {r["n"] for r in json.loads((HERE / "rows.json").read_text(encoding="utf-8"))}
seen, block, adv = {}, [], []
for f in sorted((HERE / "work").glob("out*.json")):
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        block.append(f"{f.name}: does not parse ({e})")
        continue
    for k, v in d.items():
        n = int(k)
        if n in seen:
            block.append(f"BOLO {n} in both {seen[n]} and {f.name}")
        seen[n] = f.name
        for fld in ("mission", "progress", "next"):
            t = (v or {}).get(fld, "")
            if not t.strip():
                block.append(f"BOLO {n}: empty {fld}")
            if "[[" in t or "**" in t:
                block.append(f"BOLO {n}: markup left in {fld}")
            for s in re.split(r"(?<=[.!?])\s+", t):
                if len(s.split()) > 20:
                    adv.append(f"BOLO {n} {fld}: {len(s.split())} words")
missing = sorted(rows - set(seen))
extra = sorted(set(seen) - rows)
if missing:
    block.append(f"no context for BOLO {missing}")
if extra:
    adv.append(f"not open, ignored: {extra}")
print(f"RANGE · {len(seen)}/{len(rows)} covered · {len(block)} blocking · {len(adv)} advisory")
for x in block:
    print("  BLOCK", x)
for x in adv[:15]:
    print("  adv  ", x)
sys.exit(1 if block else 0)
