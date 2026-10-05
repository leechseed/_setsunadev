"""THE REGISTER FLIP + the rung stamp (BOLO 102 stage 2, after the apply batch).

Usage:  python _tools/docs/ifc_apply.py

1. Reads every _tools/docs/work/ifc/done.<sys>.json (a list of IF ids the writer landed) and flips those
   rows in _tools/docs/out/ifc_candidates.json from `proposed` to `built` (a one-sided row stays as it is;
   its id in a done file only records that the silent side now names it). Prints the counts, then rebuilds
   the catalog (ifc_build.py).
2. Reads _tools/docs/work/ifc/rungs.json ({doc stem: rung}) and stamps `rung: <value>` into the front matter
   of every core doc that lacks it (call 9: every doc tagged from birth). Prints how many it stamped.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
WORK = os.path.join(HERE, "work", "ifc")
SRC = os.path.join(HERE, "out", "ifc_candidates.json")
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")


def flip():
    done = set()
    for f in glob.glob(os.path.join(WORK, "done.*.json")):
        try:
            done |= set(json.load(io.open(f, encoding="utf-8")))
        except Exception as e:
            print("  BAD", os.path.basename(f), e)
    E = json.load(io.open(SRC, encoding="utf-8"))
    flipped, named = 0, 0
    for e in E:
        if e.get("id") in done:
            if e["status"] == "proposed":
                e["status"] = "built"
                e["note"] = (e["note"] + " · " if e["note"] else "") + "landed 2026-10-05 (stage 2 apply batch)"
                flipped += 1
            else:
                e["note"] = (e["note"] + " · " if e["note"] else "") + "silent side named it 2026-10-05"
                named += 1
    io.open(SRC, "w", encoding="utf-8").write(json.dumps(E, ensure_ascii=False, indent=1))
    print(f"flip · {len(done)} ids reported · {flipped} proposed → built · {named} one-sided rows named by the silent side · "
          f"{sum(1 for e in E if e['status'] == 'proposed')} still proposed")
    subprocess.run([sys.executable, os.path.join(HERE, "ifc_build.py")], check=False)


def stamp():
    p = os.path.join(WORK, "rungs.json")
    if not os.path.exists(p):
        print("rung stamp · no rungs.json yet")
        return
    rungs = json.load(io.open(p, encoding="utf-8"))
    n, missing = 0, []
    for d in sorted(os.listdir(SSOT)):
        if not re.match(r"\d\d_", d):
            continue
        for f in sorted(os.listdir(os.path.join(SSOT, d))):
            if not f.endswith(".md"):
                continue
            stem = re.sub(r"^[^\w]+", "", f)[:-3].strip()
            rung = rungs.get(stem) or rungs.get(f) or rungs.get(f[:-3])
            if not rung:
                missing.append(stem)
                continue
            path = os.path.join(SSOT, d, f)
            t = io.open(path, encoding="utf-8", newline="").read()
            m = re.match(r"(﻿?---\r?\n)(.*?)(\r?\n---)", t, re.S)
            if not m or re.search(r"(?m)^rung:", m.group(2)):
                continue
            nl = "\r\n" if "\r\n" in m.group(1) else "\n"
            t = t[:m.end(2)] + f"{nl}rung: {rung}" + t[m.end(2):]
            io.open(path, "w", encoding="utf-8", newline="").write(t)
            n += 1
    print(f"rung stamp · {n} doc(s) stamped · {len(missing)} with no rung in rungs.json: {', '.join(missing[:8])}")


if __name__ == "__main__":
    flip()
    stamp()
