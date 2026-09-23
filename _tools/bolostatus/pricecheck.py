# -*- coding: utf-8 -*-
"""BORESIGHT pricing check — RANGE at the fan-in (script, zero tokens).
Usage: python _tools/bolostatus/pricecheck.py <N>
Reads work/<N>/boresight/{facts.md,pricing.json}. Every path priced in three values · every value cites real F-ids · risk and effort present."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); n = sys.argv[1]
W = os.path.join(HERE, "work", n, "boresight")
fids = set(re.findall(r"^\|\s*(F\d+)\s*\|", io.open(os.path.join(W, "facts.md"), encoding="utf-8").read(), re.M))
p = json.load(io.open(os.path.join(W, "pricing.json"), encoding="utf-8"))
F, A = [], []
paths = p.get("paths", [])
if len(paths) != 4: F.append(f"{len(paths)} paths, must be 4")
for x in paths:
    k = x.get("key", "?")
    for v in ("conservative", "on_target", "ideal"):
        val = x.get("ninety_day", {}).get(v)
        if not val or not re.search(r"\$\s?\d", str(val.get("usd", ""))): F.append(f"{k}: {v} has no dollar figure")
        cites = (val or {}).get("cites", [])
        if not cites: F.append(f"{k}: {v} cites nothing")
        for c in cites:
            if c not in fids: F.append(f"{k}: {v} cites {c}, not in facts.md")
    for fld in ("risk", "effort", "ramp", "ceiling", "verdict"):
        if not x.get(fld): A.append(f"{k}: {fld} empty")
    if x.get("confidence") not in ("HIGH", "MEDIUM", "LOW"): F.append(f"{k}: confidence must be HIGH/MEDIUM/LOW")
if not p.get("ranking") or len(p["ranking"]) != 4: A.append("ranking of the four paths missing or not four long")
if not p.get("bottom_line"): A.append("bottom_line empty")
print(f"PRICECHECK · BORESIGHT {n} · {len(paths)} paths · {len(fids)} facts")
for x in paths:
    nd = x.get("ninety_day", {})
    print(f"  {x.get('key','?'):<12} {x.get('confidence','?'):<7} cons {nd.get('conservative',{}).get('usd','?'):<14} target {nd.get('on_target',{}).get('usd','?'):<14} ideal {nd.get('ideal',{}).get('usd','?'):<14} | {x.get('verdict','')[:70]}")
print("  ranking:", " > ".join(p.get("ranking", [])))
print("  bottom line:", p.get("bottom_line", "")[:200])
for f in F: print("BLOCKING: " + f)
for a in A: print("advisory: " + a)
sys.exit(1 if F else 0)
