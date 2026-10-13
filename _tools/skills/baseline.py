#!/usr/bin/env python3
"""Baseline test helper for a skill (sp-02, BOLO 140). Stdlib only, read-only.

usage: python -X utf8 _tools/skills/baseline.py <skill-name>

Prints two test prompts for the skill (from its "Test prompts" section if it has
one, else built from the description's quoted triggers) and the checklist the CDR
runs: each prompt WITHOUT the skill, then WITH it, and compares.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    if len(sys.argv) != 2:
        print(__doc__); return 2
    name = sys.argv[1]
    path = os.path.join(ROOT, ".claude", "skills", name, "SKILL.md")
    if not os.path.isfile(path):
        print("no such skill: " + name); return 2
    text = io.open(path, encoding="utf-8").read()
    prompts = []
    m = re.search(r"^#+\s*Test prompts\s*$(.*?)(?=^#+\s|\Z)", text, re.M | re.S | re.I)
    if m:
        prompts = [re.sub(r"^\s*(?:[-*]|\d+[.)])\s*", "", l).strip()
                   for l in m.group(1).splitlines() if re.match(r"^\s*(?:[-*]|\d+[.)])\s", l)]
    if len(prompts) < 2:
        d = re.search(r"^description:\s*(.+)$", text, re.M)
        desc = d.group(1) if d else ""
        trig = re.findall(r'"([^"]{3,80})"', desc)
        trig = [t for t in trig if "<" not in t] or trig
        prompts = prompts + ["(from description) " + t for t in trig]
    prompts = (prompts + ["(none found: write one by hand)"] * 2)[:2]
    print("SKILL: %s  (%s)" % (name, os.path.relpath(path, ROOT)))
    print("\nTEST PROMPTS")
    for i, p in enumerate(prompts, 1):
        print("  %d. %s" % (i, p))
    print("""
CHECKLIST (the CDR runs this; costs a few agent runs)
  [ ] 1. WITHOUT the skill: run prompt 1 and prompt 2 in a fresh specialist with the skill folder unreadable. Record how each fails or drifts (steps skipped, wrong format, wrong files).
  [ ] 2. Write or trim the skill against those recorded failures only.
  [ ] 3. WITH the skill: re-run both prompts in a fresh specialist. Record the result.
  [ ] 4. Compare: did each recorded failure go away? Did a new one appear?
  [ ] 5. If a failure remains, edit the skill, repeat from step 3 (cap: 3 rounds).
  [ ] 6. Run python -X utf8 _tools/skills/lint.py and confirm 0 errors.
  [ ] 7. Note the before and after in the skill's references/ if it keeps one.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
