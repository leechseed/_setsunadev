"""THE CORE COMPONENT COUNT (BOLO 102 stage 1, ruled 10/4 "core first").

Usage:  python _tools/docs/components.py

Core = each system's top-level docs in ShroomsQ/_CANON/_SSOT/0*/ (shelves in subfolders are
not core: they get reference only, later). A component is a named H2 section of a core doc;
its H3 sections are its parts. Boilerplate sections (contents, purpose, history, open) are skipped.

Output: _tools/docs/out/components.json  (system -> doc -> components -> parts) + a count table.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")
OUT = os.path.join(HERE, "out", "components.json")

SKIP = re.compile(r"^(table of contents|contents|purpose|overview|version history|changelog|change log|"
                  r"open( \(provisional\))?|open questions|references|sources|see also|related|notes|"
                  r"citations|bibliography|summary)\b", re.I)


def headings(text):
    """H2 → [H3] outside fenced code and front matter."""
    text = re.sub(r"\A\s*---\n.*?\n---\s*\n", "", text.lstrip("﻿"), flags=re.S)
    comps, cur, fence = [], None, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(##|###)\s+(.+?)\s*#*\s*$", line)
        if not m:
            continue
        name = re.sub(r"[*_`]", "", m.group(2)).strip()
        if m.group(1) == "##":
            cur = None if SKIP.match(name) else {"name": name, "parts": []}
            if cur:
                comps.append(cur)
        elif cur is not None:
            cur["parts"].append(name)
    return comps


def main():
    inv, rows = {}, []
    for sysdir in sorted(d for d in os.listdir(SSOT) if re.match(r"0\d_", d)):
        full = os.path.join(SSOT, sysdir)
        docs = {}
        for f in sorted(os.listdir(full)):
            if f.endswith(".md"):
                docs[f] = headings(io.open(os.path.join(full, f), encoding="utf-8", errors="replace").read())
        inv[sysdir] = docs
        c = sum(len(v) for v in docs.values())
        p = sum(len(x["parts"]) for v in docs.values() for x in v)
        rows.append((sysdir, len(docs), c, p))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(inv, io.open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{'system':28} docs  components  parts")
    for r in rows:
        print(f"{r[0]:28} {r[1]:4}  {r[2]:10}  {r[3]:5}")
    t = [sum(r[i] for r in rows) for i in (1, 2, 3)]
    print(f"{'TOTAL':28} {t[0]:4}  {t[1]:10}  {t[2]:5}")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
