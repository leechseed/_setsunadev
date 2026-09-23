# -*- coding: utf-8 -*-
"""BREVITY — the proword selection loop's disk side (BOLO 37, ruled 9/23).

The panel lives on the sit rep page; Chief's picks land in the page's store (collection `picks`,
one document per slot: {ranks: [w1, w2, w3], when, by, sealed}). The main line pulls them with the
ArtifactData tool (list picks) and hands the JSON to this script, which rules the slots on disk.

Usage:  python _tools/soi/brevity.py                       # the open slots, front five each
        python _tools/soi/brevity.py apply picks.json      # rule slots from the store's documents
        python _tools/soi/brevity.py add <id> "<thing>" W1 W2 ... W10   # a new slot (first five surface)
picks.json: either {"docs":[{"id":..,"data":{..}}]} as ArtifactData prints it, or {"<slot>": {"ranks": [...]}}."""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "benches.json")
d = json.load(io.open(P, encoding="utf-8")); slots = d["slots"]
save = lambda: io.open(P, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1))

if len(sys.argv) > 2 and sys.argv[1] == "apply":
    raw = json.load(io.open(sys.argv[2], encoding="utf-8"))
    picks = {x["id"]: x.get("data", x) for x in raw["docs"]} if "docs" in raw else raw
    today = time.strftime("%Y-%m-%d"); n = 0
    for s in slots:
        p = picks.get(s["id"])
        if not p or not p.get("ranks"): continue
        s["status"] = "ruled"; s["ruling"] = {"ranks": p["ranks"], "when": p.get("when", today), "sealed": s["sealed"]}; n += 1
        print(f"RULED {s['id']:<14} {p['ranks'][0]}  (2: {p['ranks'][1]} · 3: {p['ranks'][2]}) · sealed was {s['sealed'][0]}")
        print(f"  SOP §5 line: - **{p['ranks'][0]} — RULED {today}** on BREVITY (the loop): {s['thing'][:90]}… Bench shown: {' · '.join(s['bench'][:5])}. Sealed: {' · '.join(s['sealed'])}.")
    save(); print(f"{n} slot(s) ruled · benches.json written · add the SOI entries and the SOP §5 lines by hand (the loop names, the SOP records)")
    sys.exit(0)
if len(sys.argv) > 4 and sys.argv[1] == "add":
    words = sys.argv[4:]
    slots.append({"id": sys.argv[2], "thing": sys.argv[3], "since": time.strftime("%-m/%-d") if os.name != "nt" else time.strftime("%m/%d").lstrip("0").replace("/0", "/"), "bench": words, "sealed": words[:3], "status": "open"})
    save(); print("added", sys.argv[2], "·", len(words), "candidates, five surface"); sys.exit(0)
op = [s for s in slots if s["status"] == "open"]
print(f"BREVITY · {len(slots)} slots · {len(op)} open · {len(slots)-len(op)} ruled")
for s in slots:
    tag = "RULED " + s["ruling"]["ranks"][0] if s["status"] == "ruled" else "open"
    print(f"  {s['id']:<14} {tag:<22} {' · '.join(s['bench'][:5])}")
