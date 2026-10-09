"""The packet digest: every judged intake note flattened to one line per nugget, grouped by bin and system (BOLO 107).

Usage: python _tools/intake/digest.py
Zero tokens. Reads _PRIVATE/intake/pilot/batch_A,B.json and _PRIVATE/intake/joplin/batch_*.json; writes
_PRIVATE/intake/packet/digest.md (what the packet writer reads, instead of the raw batches) and prints the counts.
"""
import glob, io, json, os, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from inventory import ROOT  # noqa: E402

INTAKE = os.path.join(ROOT, "_PRIVATE", "intake")
OUT = os.path.join(INTAKE, "packet", "digest.md")
SYSTEMS = {"00": "EPISTEMOLOGY", "01": "NARRATIVE FRAMEWORKS", "02": "CHARACTER", "03": "SETTING", "04": "PLOT",
           "05": "WORLDBUILDING", "06": "THEME", "07": "STYLE", "08": "TRACKING", "09": "OPERATIONS"}


def main():
    files = sorted(glob.glob(os.path.join(INTAKE, "pilot", "batch_*.json"))) + sorted(glob.glob(os.path.join(INTAKE, "joplin", "batch_*.json")))
    notes = []
    for f in files:
        notes += json.load(io.open(f, encoding="utf-8"))
    bins, conf, eras, authors = Counter(), Counter(), Counter(), Counter()
    by = defaultdict(list)
    titles = []
    for n in notes:
        bins[n.get("bin")] += 1
        eras[str(n.get("era", "-"))] += 1
        authors[n.get("author", "-")] += 1
        if n.get("bin") == "dead" or n.get("dupe_of"):
            continue
        lin = ",".join(n.get("lineage") or [])
        titles.append("%s · %s · %s · era %s · %s%s" % (n["id"], n.get("bin"), n.get("author", "-"), n.get("era", "-"),
                                                       (n.get("title") or "")[:70], " · lineage " + lin if lin else ""))
        for g in n.get("nuggets", []):
            conf[g.get("conf")] += 1
            tag = "%s, %s%s%s" % (n["id"], g.get("conf"), ", " + n.get("author") if n.get("author") == "report" else "",
                                  ", lineage " + lin if lin else "")
            line = "- %s (%s)" % (g.get("t", "").strip(), tag)
            if g.get("verbatim"):
                line += '\n  > "%s"' % g["verbatim"].strip()
            by[(n.get("bin"), str(g.get("system", "??")))].append(line)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    w = io.open(OUT, "w", encoding="utf-8")
    w.write("# Intake digest (BOLO 107) · %d notes · %d nuggets\n\n" % (len(notes), sum(conf.values())))
    w.write("bins: %s\n\nconf: %s\n\nera: %s\n\nauthor: %s\n\n" % (dict(bins), dict(conf), dict(eras), dict(authors)))
    for b in ("canon", "method", "inspiration"):
        w.write("\n# %s\n" % b.upper())
        for s in sorted(SYSTEMS):
            rows = by.get((b, s), [])
            if rows:
                w.write("\n## %s %s (%d)\n\n%s\n" % (s, SYSTEMS[s], len(rows), "\n".join(rows)))
    w.write("\n# NOTE INDEX (live notes)\n\n" + "\n".join(titles) + "\n")
    w.close()
    print("DIGEST: %d notes · %d nuggets · %s · %d KB -> %s" % (len(notes), sum(conf.values()), dict(bins),
                                                            os.path.getsize(OUT) // 1024, OUT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
