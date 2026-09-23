# -*- coding: utf-8 -*-
"""BOLO 51's standing audit — the rows it re-reads every pass (script, zero tokens).
Usage:  python _tools/audit/audit.py            # open rows, GAP first, cheapest first
        python _tools/audit/audit.py close A7 "allowlist expanded 9/23"
        python _tools/audit/audit.py all"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rows.json")
d = json.load(io.open(P, encoding="utf-8")); rows = d["rows"]
if len(sys.argv) > 2 and sys.argv[1] == "close":
    for r in rows:
        if r["id"] == sys.argv[2]: r["closed"] = " ".join(sys.argv[3:]) or "closed"
    io.open(P, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1)); print("closed", sys.argv[2]); sys.exit(0)
show = rows if "all" in sys.argv else [r for r in rows if not r["closed"]]
order = {"GAP": 0, "PARTIAL": 1}; cost = {"S": 0, "M": 1, "L": 2, "-": 3}
show.sort(key=lambda r: (order.get(r["status"], 9), cost.get(r["cost"], 9), r["id"]))
op = sum(1 for r in rows if not r["closed"])
print(f"AUDIT · {len(rows)} rows · {op} open · {len(rows)-op} closed · source BORESIGHT 64")
for r in show:
    tag = "closed " + r["closed"][:10] if r["closed"] else r["status"]
    print(f"  {r['id']:<5} {tag:<17} {r['cost']:<2} {r['practice'][:46]:<46} | {(r['fix'] or r['gap'])[:88]}")
