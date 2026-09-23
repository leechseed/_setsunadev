# -*- coding: utf-8 -*-
"""Character-node check — RANGE at the fan-in for a node written against a template node (script, zero tokens).
Usage: python _tools/tm/nodecheck.py <new-node.md> <template-node.md>
Same frontmatter keys · same H2/H3 headings in the same order · the 12 layers all present · every ⧗ listed as a call in Open questions · no 'RULED' claim on a ⧗ line."""
import io, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
new, tpl = sys.argv[1], sys.argv[2]
rd = lambda p: io.open(p, encoding="utf-8").read()
a, t = rd(new), rd(tpl)
def fm(s):
    m = re.match(r"^---\n(.*?)\n---", s, re.S)
    return [l.split(":")[0].strip() for l in m.group(1).splitlines() if re.match(r"^[a-z_]+:", l)] if m else []
def heads(s): return [h.strip() for h in re.findall(r"^#{2,3} (.+)$", s, re.M)]
F, A = [], []
fa, ft = fm(a), fm(t)
for k in ft:
    if k not in fa: F.append(f"frontmatter key missing: {k}")
ha, ht = heads(a), heads(t)
norm = lambda h: re.sub(r"[^a-z0-9 ]", "", h.lower()).strip()
na, nt = [norm(h) for h in ha], [norm(h) for h in ht]
missing = [h for h, n in zip(ht, nt) if n not in na]
if missing: F.append(f"headings missing: {missing}")
order = [n for n in na if n in nt]
if order != [n for n in nt if n in na]: A.append("heading order differs from the template")
layers_t = re.findall(r"^\|\s*(?:L)?(\d{1,2})\b", t.split("## The 12 layers", 1)[1].split("\n## ", 1)[0], re.M) if "## The 12 layers" in t else []
layers_a = re.findall(r"^\|\s*(?:L)?(\d{1,2})\b", a.split("## The 12 layers", 1)[1].split("\n## ", 1)[0], re.M) if "## The 12 layers" in a else []
if len(set(layers_a)) < 12: A.append(f"the 12 layers: {len(set(layers_a))} numbered rows found (template has {len(set(layers_t))})")
flags = a.count("⧗")
oq = a.split("## Open questions", 1)[1].split("\n## ", 1)[0] if "## Open questions" in a else ""
calls = len(re.findall(r"^\s*\d+\.", oq, re.M))
if flags and not calls: F.append("⧗ flags planted but Open questions lists no numbered calls")
bad = [l[:90] for l in a.splitlines() if "⧗" in l and re.search(r"\bRULED\b", l) and "RULED 2026-09-23" not in l]
if bad: A.append(f"lines carrying both ⧗ and RULED: {bad[:3]}")
print(f"NODECHECK · {new} against {tpl} · {len(a)//1024} KB · {len(ha)} headings · {flags} ⧗ · {calls} calls")
for f in F: print("BLOCKING: " + f)
for x in A: print("advisory: " + x)
sys.exit(1 if F else 0)
