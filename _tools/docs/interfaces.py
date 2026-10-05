"""THE N² SCAN (BOLO 102 stage 2, the interface layer — RECON, zero tokens).

Usage:  python _tools/docs/interfaces.py

Reads every core source doc (ShroomsQ/_CANON/_SSOT/0N_*/*.md, top level) and finds where it names
another system: a link or wiki link to another system's doc (by ssot stem), or that system's folder.
Writes:
  _tools/docs/out/interfaces.json   every edge: from doc → to doc, with the line it sits on
  _tools/docs/out/N2.md             the N² grid (system × system, edge counts; NASA SE Handbook
                                    interface management) + the doc pairs, busiest first
The grid says WHERE the systems touch. What flows across each touch is stage 2's design work.
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")
OUT = os.path.join(HERE, "out")
NAMES = {"00": "Base", "01": "Narrative", "02": "Character", "03": "Setting", "04": "Plot",
         "05": "Worldbuilding", "06": "Theme", "07": "Style", "08": "Tracking", "09": "Operations"}


def stem(f):
    return re.sub(r"^[^\w]+", "", f)[:-3].strip().lower()


def main():
    docs = {}   # stem -> (system, path)
    folders = {}
    for d in sorted(os.listdir(SSOT)):
        m = re.match(r"(\d\d)_", d)
        if not m:
            continue
        folders[d.lower()] = m.group(1)
        for f in os.listdir(os.path.join(SSOT, d)):
            if f.endswith(".md"):
                docs[stem(f)] = (m.group(1), os.path.join(SSOT, d, f))
    stems = sorted(docs, key=len, reverse=True)
    pat = re.compile("|".join(re.escape(s) for s in stems) + "|" + "|".join(re.escape(f) for f in folders), re.I)

    edges, grid, pairs = [], Counter(), Counter()
    for s, (nn, p) in sorted(docs.items()):
        seen = set()
        for i, line in enumerate(io.open(p, encoding="utf-8", errors="replace").read().splitlines(), 1):
            for m in pat.finditer(line):
                hit = m.group(0).lower()
                if hit in docs:
                    to_nn, to_doc = docs[hit][0], hit
                else:
                    to_nn, to_doc = folders[hit], hit
                if to_nn == nn or (s, to_doc, i) in seen:
                    continue
                seen.add((s, to_doc, i))
                edges.append({"from_sys": nn, "from": s, "to_sys": to_nn, "to": to_doc, "line": i,
                              "text": line.strip()[:240]})
                grid[(nn, to_nn)] += 1
                pairs[(s, to_doc)] += 1

    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, "interfaces.json"), "w", encoding="utf-8").write(json.dumps(edges, ensure_ascii=False, indent=1))
    keys = sorted(NAMES)
    md = ["# The N² grid · BOLO 102 stage 2 RECON", "",
          "Row = the system that names another; column = the system it names. Each cell counts the lines.",
          "The diagonal is each system itself. A cell says the two systems touch; stage 2 says what crosses.", "",
          "| from \\ to | " + " | ".join(f"{k} {NAMES[k]}" for k in keys) + " |",
          "|---|" + "---|" * len(keys)]
    for r in keys:
        md.append(f"| **{r} {NAMES[r]}** | " + " | ".join("■" if r == c else (str(grid[(r, c)]) if grid[(r, c)] else "·") for c in keys) + " |")
    md += ["", f"**{len(edges)} references · {len(pairs)} doc pairs · "
           f"{sum(1 for r in keys for c in keys if r != c and grid[(r, c)])} of 90 system pairs touch.**", "",
           "## The busiest doc pairs", "", "| from | to | lines |", "|---|---|---|"]
    md += [f"| {a} | {b} | {n} |" for (a, b), n in pairs.most_common(40)]
    silent = [f"{NAMES[r]} → {NAMES[c]}" for r in keys for c in keys if r != c and not grid[(r, c)]
              and r not in ("09",) and c not in ("09",)]
    md += ["", "## Story-system pairs that never name each other", "", ", ".join(silent) or "none"]
    io.open(os.path.join(OUT, "N2.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"N² scan · {len(docs)} core docs · {len(edges)} references · {len(pairs)} doc pairs → _tools/docs/out/N2.md")


if __name__ == "__main__":
    main()
