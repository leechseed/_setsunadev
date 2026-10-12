"""split_template.py — THE CUT (BOLO 136): one starting sheet per editing style (Chief, 10/12: "split the template").

The pmv:ref set holds two styles that an average hides: the RAPID cut (a new shot every second or less) and the
LONG HOLD (split-screen or crossfade edits whose changes are soft, so the cut detector sees few). A video goes to
a style by its cuts per minute: RAPID at RAPID_MIN and up, HOLD at HOLD_MAX and under, MIDDLE between.
Writes TEMPLATE-rapid.md · TEMPLATE-middle.md · TEMPLATE-hold.md next to the per-video JSONs, each built by the
same template() as TEMPLATE.md, plus STYLES.md (who went where). Rerun after deconstruct.py; it reads the JSONs.

Usage: python _tools/thecut/split_template.py _PRIVATE/thecut/deconstruct
"""

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from deconstruct import template  # noqa: E402

RAPID_MIN = 30.0    # cuts per minute (provisional: the set splits cleanly around here)
HOLD_MAX = 6.0


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "_PRIVATE/thecut/deconstruct"
    rows = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(d, "stash*.json")))]
    groups = {"rapid": [], "middle": [], "hold": []}
    for r in rows:
        c = r["cuts_per_min"]
        groups["rapid" if c >= RAPID_MIN else "hold" if c <= HOLD_MAX else "middle"].append(r)
    names = {"rapid": "the RAPID cut", "middle": "the MIDDLE pace", "hold": "the LONG HOLD"}
    for k, rs in groups.items():
        if not rs:
            continue
        t = template(rs).replace("# THE CUT · the reference format", f"# THE CUT · {names[k]} ({len(rs)} videos)")
        if k == "hold":
            t += ("\n> The cut detector sees hard cuts only. Long-hold edits change by split screens, overlays and crossfades, "
                  "so their cut counts read low. Trust their tempo, length and look; read their pacing by eye.\n")
        open(os.path.join(d, f"TEMPLATE-{k}.md"), "w", encoding="utf-8").write(t)
    with open(os.path.join(d, "STYLES.md"), "w", encoding="utf-8") as f:
        f.write(f"# Styles · RAPID ≥ {RAPID_MIN} cuts/min · HOLD ≤ {HOLD_MAX} · MIDDLE between\n\n")
        for k, rs in groups.items():
            f.write(f"## {names[k]} · {len(rs)}\n\n")
            for r in sorted(rs, key=lambda r: -r["cuts_per_min"]):
                f.write(f"- {r['cuts_per_min']:>6} cuts/min · {r['shot_s']['median']}s shots · {r['bpm']} BPM · {r['title'][:70]}\n")
            f.write("\n")
    print(" · ".join(f"{k} {len(v)}" for k, v in groups.items()), f"· of {len(rows)}")


if __name__ == "__main__":
    main()
