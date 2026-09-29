"""BOLO 89 · build the cross-domain trope register (zero tokens).
Joins the domain index (names + one-line defs), the keys (work/89/keys.batch*.json),
and the plot trope graph's keyed tropes, then writes:
  _tools/tropes/data/domains/register.json   every trope: slug · name · def · domains · keys · conf · links
  _tools/tropes/data/domains/LAYERS.md        every layer with every trope keyed to it (the pull list)
and prints the counts table the SSOT doc carries.
"""
import glob, json
from collections import defaultdict
from pathlib import Path
R = Path(__file__).parent
D = R / "data" / "domains"
idx = json.loads((D / "index.json").read_text(encoding="utf-8"))
defs = json.loads((D / "defs.json").read_text(encoding="utf-8")) if (D / "defs.json").exists() else {}  # first sentences for index lines with no def
links = {}
for l in (D / "tropes.jsonl").read_text(encoding="utf-8").splitlines():
    if l.strip():
        j = json.loads(l); links[j["slug"]] = j["links"]
keys = {}
for f in sorted(glob.glob(str(R.parent / "bolostatus/work/89/keys.batch*.json"))):
    for r in json.loads(Path(f).read_text(encoding="utf-8")):
        k = keys.setdefault(r["slug"], {"keys": {}, "conf": r.get("conf")})
        k["keys"].update(r.get("keys", {}))  # theme batches (batchT*) add a key, never replace
        if k["conf"] != "low" and r.get("conf") == "low": k["conf"] = "low"
reg = {}
for s, v in idx.items():
    if not v.get("domains"): continue
    k = keys.get(s, {})
    reg[s] = {"name": v["name"], "def": v["def"] or defs.get(s, ""), "domains": v["domains"], "keys": k.get("keys", {}),
              "conf": k.get("conf"), "links": links.get(s, [])}
(D / "register.json").write_text(json.dumps(reg, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
ORDER = {"character": [f"L{i}" for i in range(1, 13)], "sexuality": [f"L{i}" for i in range(1, 13)],
         "setting": [f"S{i}" for i in range(1, 13)], "genre": [f"G{i}" for i in range(1, 13)], "theme": ["R1", "R2", "R3", "R4"]}
by = defaultdict(list)
for s, r in reg.items():
    for d, k in r["keys"].items():
        by[(d, k)].append(r["name"])
out = ["# The trope register · the pull list (BOLO 89, built by build_register.py)", "",
       "Every layer, every trope keyed to it. Names only; the one-line defs live in register.json.", ""]
table = []
for d, ks in ORDER.items():
    out.append(f"## {d}")
    row = []
    for k in ks + [None]:
        names = sorted(by.get((d, k), []), key=str.lower)
        if not names: continue
        out.append(f"### {d} · {k or 'null'} · {len(names)}")
        out.append(", ".join(names)); out.append("")
        row.append(f"{k or 'null'} {len(names)}")
    table.append(f"| {d} | {' · '.join(row)} |")
(D / "LAYERS.md").write_text("\n".join(out), encoding="utf-8")
print(f"register: {len(reg)} tropes · keyed {len(keys)}")
print("\n".join(table))
