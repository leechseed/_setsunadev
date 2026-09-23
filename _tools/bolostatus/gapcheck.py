# -*- coding: utf-8 -*-
"""BORESIGHT gap-table check — RANGE at the fan-in (script, zero tokens).
Usage: python _tools/bolostatus/gapcheck.py <N>
Reads work/<N>/boresight/{docs.md,command.md,gaps.json}. Every doc id once · statuses legal · cites real · counts add up."""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
n = sys.argv[1]
W = os.path.join(HERE, "work", n, "boresight")
rd = lambda f: io.open(os.path.join(W, f), encoding="utf-8").read()
doc_ids = re.findall(r"^\|\s*([A-F]\d+)\s*\|", rd("docs.md"), re.M)
c_ids = set(re.findall(r"^\|\s*(C\d+)\s*\|", rd("command.md"), re.M))
g = json.loads(rd("gaps.json"))
rows = g.get("rows", [])
F, A = [], []
LEGAL = {"DONE", "PARTIAL", "GAP", "N/A", "ORGANIC"}
seen = {}
for r in rows:
    seen[r.get("id")] = seen.get(r.get("id"), 0) + 1
    if r.get("status") not in LEGAL: F.append(f"{r.get('id')}: status {r.get('status')!r} not legal")
    for c in r.get("cites", []):
        if c not in c_ids: F.append(f"{r.get('id')}: cites {c}, not in command.md")
    if r.get("status") in ("GAP", "PARTIAL") and not r.get("fix"): A.append(f"{r.get('id')}: {r['status']} with no fix")
    if r.get("status") == "DONE" and r.get("enforced") in ("none", "SOP rule", ""): A.append(f"{r.get('id')}: DONE but enforced by {r.get('enforced')!r}")
missing = [d for d in doc_ids if d not in seen]; extra = [d for d in seen if d not in doc_ids]; dup = [d for d, k in seen.items() if k > 1]
if missing: F.append(f"doc ids missing from the table: {missing}")
if extra: F.append(f"ids not in docs.md: {extra}")
if dup: F.append(f"ids placed twice: {dup}")
cnt = {}
for r in rows: cnt[r.get("status")] = cnt.get(r.get("status"), 0) + 1
sc = g.get("summary", {}).get("counts", {})
for k in LEGAL:
    if sc.get(k, 0) != cnt.get(k, 0): F.append(f"summary.counts.{k} = {sc.get(k)} but rows say {cnt.get(k, 0)}")
fs = g.get("summary", {}).get("four_steps", [])
if [x.get("doc") for x in fs] != ["D1", "D2", "D3", "D4"]: F.append("summary.four_steps must be D1..D4 in order")
print(f"GAPCHECK · BORESIGHT {n} · {len(rows)} rows against {len(doc_ids)} doc ids · {len(c_ids)} C-ids")
print("  counts: " + " · ".join(f"{k} {cnt.get(k, 0)}" for k in ("DONE", "PARTIAL", "GAP", "ORGANIC", "N/A")))
for x in fs: print(f"  {x.get('step'):<10} {x.get('verdict'):<8} {x.get('line', '')[:140]}")
for t in g.get("summary", {}).get("top_gaps", []): print("  top: " + t[:160])
for f in F: print("BLOCKING: " + f)
for a in A: print("advisory: " + a)
sys.exit(1 if F else 0)
