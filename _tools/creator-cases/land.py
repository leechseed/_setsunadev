"""land.py <slug> <register name> <note> <xhandle> [sex]  — rename GOUGE→TTP in the file, apply the register row."""
import io, sys, re
slug, name, note, handle = sys.argv[1:5]
sex = sys.argv[5] if len(sys.argv) > 5 else None
f = f"_CANON_NODES/creator-case-{slug}.md"
s = io.open(f, encoding="utf-8").read()
s2 = re.sub(r"^## (\d+) · GOUGE$", r"## \1 · TTP", s, flags=re.M).replace("§10 GOUGE added", "§10 TTP added")
if s2 != s: io.open(f, "w", encoding="utf-8", newline="\n").write(s2); print("header → TTP")
p = "_CANON_NODES/performer-register.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
hit = [i for i, l in enumerate(lines) if l.startswith(f"| {name} |") or l.startswith(f"| **{name}** ")]
assert len(hit) == 1, (name, hit)
i = hit[0]; cells = lines[i].split(" | ")
# columns: | Name | Lane | Sex | Listed | Sources | First | Stash | 5★ | note | X |
cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
assert len(cells) == 10, cells
if sex and cells[2] == "—": cells[2] = sex
cells[8] = (cells[8] + ("; " if cells[8] else "") + "9/10 study → " + note).strip()
if handle and handle != "—": cells[9] = handle
lines[i] = "| " + " | ".join(cells) + " |"
io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("register row applied:", name)
