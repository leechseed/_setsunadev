# -*- coding: utf-8 -*-
"""RANGE for BVX-LEARN distills: checks a KNOWLEDGE_AREAS entry against the v4 template gates (TEMPLATE.distill.v4.md §D).
Blocking: frontmatter missing id/spine/feeds · fewer than 2 or more than 5 mermaid blocks · a required section missing ·
a mermaid block with no caption line adjacent · Core Thesis over 60 words. Advisory: em-dash count, word count outside 1,500-3,000.

Usage: python _tools/zotero/check_distill.py BVX.0175 [BVX.0236 ...]   (ids or paths)
"""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
KA = os.path.join(ROOT, "_0.1_BVX_LEARN", "KNOWLEDGE_AREAS")
REQUIRED = ["CORE THESIS", "MIND MODELS", "FRAMEWORK", "KEY CONCEPTS", "HEURISTICS", "INVARIANTS", "PITFALLS", "APPLICATION", "CROSS-REFERENCES", "PROVENANCE", "META"]
TYPES = r"^\s*(mindmap|flowchart|graph|stateDiagram-v2|timeline|sequenceDiagram|quadrantChart|classDiagram|erDiagram|journey|gantt|pie)\b"


def check(path):
    t = io.open(path, encoding="utf-8").read(); name = os.path.basename(path)
    blocking, advisory = [], []
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = m.group(1) if m else ""
    if not m: blocking.append("no frontmatter")
    for k in ("id:", "spine:", "feeds:", "title:"):
        if k not in fm: blocking.append(f"frontmatter missing {k}")
    heads = [h.upper() for h in re.findall(r"^##+\s+(.*)$", t, re.M)]
    for r in REQUIRED:
        if not any(r in h for h in heads): blocking.append(f"section missing: {r}")
    blocks = re.findall(r"```mermaid\n(.*?)```", t, re.S)
    if len(blocks) < 2: blocking.append(f"only {len(blocks)} mermaid block(s), minimum 2")
    if len(blocks) > 5: blocking.append(f"{len(blocks)} mermaid blocks, maximum 5")
    kinds = []
    for b in blocks:
        first = next((ln for ln in b.splitlines() if ln.strip() and not ln.strip().startswith("%%")), "")
        mt = re.match(TYPES, first)
        kinds.append(mt.group(1) if mt else "?")
        if not mt: blocking.append(f"mermaid block starts with an unknown type: {first.strip()[:40]}")
        nodes = len(re.findall(r"^\s{2,}\S", b, re.M)) if kinds[-1] == "mindmap" else len(re.findall(r"\[|\(|-->|--\s", b))
        if nodes > 40: advisory.append(f"{kinds[-1]} block has ~{nodes} node marks (rule: ~25 max)")
    if blocks and kinds and kinds[0] != "mindmap": blocking.append(f"diagram 1 must be a mindmap, found {kinds[0]}")
    for mm in re.finditer(r"```mermaid\n", t):
        before = t[max(0, mm.start() - 400): mm.start()]; after = t[mm.end():]
        end = after.find("```"); after = after[end + 3: end + 400] if end >= 0 else ""
        if not re.search(r"caption|\*[^*\n]{10,}\*", before + after, re.I): blocking.append("a mermaid block has no caption line near it")
    ct = re.search(r"^##+\s+.*CORE THESIS.*\n(.*?)(?=^##+ )", t, re.S | re.M)
    if ct:
        words = len(re.sub(r"[*_>`]", "", ct.group(1)).split())
        if words > 60: advisory.append(f"Core Thesis is {words} words (gate: 60)")
    wc = len(t.split())
    if not 1500 <= wc <= 3200: advisory.append(f"word count {wc} (target 1,800-2,600 plus diagrams)")
    em = t.count("—")
    if em > 40: advisory.append(f"{em} em-dashes")
    ok = not blocking
    print(f"{'PASS' if ok else 'FAIL'} {name} · {wc} words · diagrams {len(blocks)} {kinds}")
    for b in blocking: print("   BLOCK", b)
    for a in advisory: print("   adv  ", a)
    return ok


def main():
    args = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(KA) if re.match(r"BVX\.\d{4}\.md$", f))
    res = [check(a if os.path.exists(a) else os.path.join(KA, a + ".md")) for a in args]
    print(f"{sum(res)}/{len(res)} pass")
    sys.exit(0 if all(res) else 1)


if __name__ == "__main__":
    main()
