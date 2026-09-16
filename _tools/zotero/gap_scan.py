# -*- coding: utf-8 -*-
"""BOLO 18 stage 2, step 5: rank THE GAP (z-lib favourites not in the library) by story-spine shelf, so the acquisition queue is ranked.
Reads _0.1_BVX_LEARN/_meta/zlib_gap.json ('gap' list), applies the full-pass title rules, writes GAP-BY-SHELF.md.

Usage: python _tools/zotero/gap_scan.py
"""
import io, os, re, sys, json, collections, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
META = os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta")
sys.path.insert(0, HERE)
from fullpass import COMPILED  # the same rules as the library pass


def main():
    g = json.load(io.open(os.path.join(META, "zlib_gap.json"), encoding="utf-8"))
    gap = g["gap"]
    rows = []
    for e in gap:
        s = e if isinstance(e, str) else " — ".join(str(e.get(k, "")) for k in ("author", "title") if e.get(k)) or json.dumps(e, ensure_ascii=False)
        hits = [k for k, rx in COMPILED if rx.search(s)]
        rows.append((s, hits))
    lvc = collections.Counter(k for _, h in rows for k in h)
    keyed = [r for r in rows if r[1]]
    L = ["---", "id: BVX-LEARN.gap-by-shelf", "title: \"THE GAP ranked by story-spine shelf\"", "type: report",
         f"generated: {datetime.date.today()}", "status: BOLO 18 stage 2 - step 5 (acquisition queue)", "---", "",
         "# THE GAP by shelf", "",
         f"{len(gap)} z-lib favourites not in the library, title rules only (no PDF to read). {len(keyed)} hit a story shelf; the rest are off-spine or unreadable by title.", "",
         "| Shelf | Titles in the gap |", "|---|---|"] + [f"| {k} | {v} |" for k, v in lvc.most_common()]
    for lvl in ["L0", "L4", "L5", "L6", "L7", "SETTING", "TEXTURE", "CRAFT-PROCESS"]:
        rs = [s for s, h in rows if lvl in h]
        L += ["", f"## {lvl} ({len(rs)})", ""] + [f"- {s[:140]}" for s in sorted(rs)]
    io.open(os.path.join(META, "GAP-BY-SHELF.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print(f"gap {len(gap)} · on a shelf {len(keyed)} ·", dict(lvc.most_common()))


if __name__ == "__main__":
    main()
