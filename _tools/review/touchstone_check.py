"""Touchstone id check (BOLO 100 TS-B9).

Greps every `TS <book>:<n>` under ShroomsQ/_CANON/_SSOT/ and confirms each id
has an entry in the Touchstones register. Exit 0 = pass, 1 = unknown ids.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SSOT = ROOT / "ShroomsQ" / "_CANON" / "_SSOT"
REGISTER = next(SSOT.glob("01_NARRATIVE_FRAMEWORKS/*ssot_01_touchstones_register.md"))
# Format examples, not entries: the naming rule cites "TS 1:3" to show book:number.
EXAMPLES = {("ssot_06_2_documents_style.md", "1:3")}
ID = re.compile(r"\bTS (\d+:\d+)\b")

registered = set(re.findall(r"\*\*TS (\d+:\d+) —", REGISTER.read_text(encoding="utf-8")))
bad = []
total = 0
for p in sorted(SSOT.rglob("*.md")):
    if "_history" in p.parts or "_ARCHIVE" in p.parts:
        continue
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        for m in ID.finditer(line):
            total += 1
            if m.group(1) not in registered and (p.name.split(" ")[-1], m.group(1)) not in EXAMPLES:
                bad.append((p.relative_to(ROOT).as_posix(), n, "TS " + m.group(1)))

print(f"register ids: {len(registered)} | citations checked: {total}")
for f, n, i in bad:
    print(f"MISSING {i}  {f}:{n}")
print("PASS" if not bad else f"FAIL ({len(bad)} unregistered)")
sys.exit(1 if bad else 0)
