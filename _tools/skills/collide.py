#!/usr/bin/env python3
"""Find skill and agent descriptions that overlap (stdlib only, zero tokens).

Reads .claude/skills/*/SKILL.md and .claude/agents/*.md, scores every pair on shared
trigger words (Jaccard over content words) and near-duplicate sentences, prints pairs
at or above the threshold, highest first.

Usage: python _tools/skills/collide.py [--min 0.4] [repo_root]
Output: score | a | b | shared words. Exit 0 always (a triage list, not a gate).
"""
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

STOP = set("""a an and are as at be by for from has have if in into is it its of on or that the their then
this to use used uses when with without you your fires never only each every one any all not no can will
run runs new per via than also so do does done s command bolo skill agent agents skills reads read writes
write returns report reports changes change file files""".split())


def desc_of(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\r?\n(.*?)\r?\n---", t, re.S)
    if not m:
        return ""
    d = re.search(r"^description:\s*(.*(?:\n[ \t]+.*)*)", m.group(1), re.M)
    return re.sub(r"\s+", " ", d.group(1)).strip().strip("\"'") if d else ""


def words(text):
    return {w for w in re.findall(r"[a-z][a-z0-9-]{2,}", text.lower()) if w not in STOP}


def sentences(text):
    return [s.strip().lower() for s in re.split(r"(?<=[.;:])\s+", text) if len(s.strip()) > 60]


def main():
    args = sys.argv[1:]
    thr = 0.4
    if "--min" in args:
        i = args.index("--min")
        thr = float(args[i + 1])
        del args[i:i + 2]
    root = Path(args[0]) if args else Path(__file__).resolve().parents[2]
    items = []
    for f in sorted((root / ".claude" / "skills").glob("*/SKILL.md")):
        items.append(("skill:" + f.parent.name, desc_of(f)))
    for f in sorted((root / ".claude" / "agents").glob("*.md")):
        if f.name.lower() != "readme.md":
            items.append(("agent:" + f.stem, desc_of(f)))
    data = [(n, d, words(d), sentences(d)) for n, d in items if d]
    rows = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            a, b = data[i], data[j]
            shared = a[2] & b[2]
            union = a[2] | b[2]
            jac = len(shared) / len(union) if union else 0.0
            dup = max((SequenceMatcher(None, x, y).ratio() for x in a[3] for y in b[3]), default=0.0)
            dup = dup if dup >= 0.9 else 0.0
            score = max(jac, dup)
            if score >= thr:
                rows.append((score, a[0], b[0], sorted(shared)[:8], dup > 0))
    rows.sort(reverse=True)
    for s, a, b, sh, dup in rows:
        print(f"{s:.2f} | {a} | {b} | {', '.join(sh)}{' | near-duplicate sentence' if dup else ''}")
    print(f"SUMMARY · {len(data)} descriptions · {len(rows)} pairs at or above {thr}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()

# idea from mishanefedov/skill-issue (MIT, via sickn33/agentic-awesome-skills skills/skill-issue) · own code · BOLO 140 · 2026-10-13
