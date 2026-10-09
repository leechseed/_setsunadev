"""The near-duplicate pass: which unread notes repeat what the intake already read (BOLO 107, 10/9).

Usage: python _tools/intake/dedupe.py [--threshold 0.8]

Zero tokens. The inventory caught copies by title; this catches them by text. Every note is cut into 8-word
shingles. A note whose shingles sit mostly (threshold, default 80%) inside notes already read, or inside an
unread note kept earlier in this pass, is a copy. Notes in the pasted-research folder go to Lane A (the books lane)
instead of the readers. Writes _PRIVATE/intake/dedupe.json ({path: reason}); batch.py make skips those paths.
The script judges nothing about what is good.
"""
import io, json, os, re, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from inventory import ROOT, body_of  # noqa: E402

INTAKE = os.path.join(ROOT, "_PRIVATE", "intake")
OUT = os.path.join(INTAKE, "dedupe.json")
LANE_A = ("_devlog/LEECHSEED STUDIES/SETTING & GENRE & FUZZ/",)   # pasted research, ruled to Lane A 10/9 ("go dedupe")
K = 8


def shingles(text):
    w = re.findall(r"\w+", text.lower())
    return {hash(" ".join(w[i:i + K])) for i in range(max(0, len(w) - K + 1))}


def body(r):
    raw = io.open(os.path.join(ROOT, r["path"]), encoding="utf-8", errors="replace").read()
    return body_of(r["vault"], raw)[0]


def main():
    th = float(sys.argv[sys.argv.index("--threshold") + 1]) if "--threshold" in sys.argv else 0.8
    inv = json.load(io.open(os.path.join(INTAKE, "inventory.json"), encoding="utf-8"))["notes"]
    read = json.load(io.open(os.path.join(INTAKE, "read.json"), encoding="utf-8"))
    live = [r for r in inv if not r["empty"] and not r.get("dupe_of") and not r["book"]]
    seen = set()
    for r in live:
        if r["path"] in read:
            seen |= shingles(body(r))
    todo = sorted((r for r in live if r["path"] not in read), key=lambda r: (r["vault"] != "logseq", r["path"]))
    out, why = {}, Counter()
    for r in todo:
        if r["path"].startswith(LANE_A):
            out[r["path"]] = "lane A: pasted research"
            why["lane A"] += 1
            continue
        s = shingles(body(r))
        if s and len(s & seen) / len(s) >= th:
            out[r["path"]] = "copy: %d%% already read" % round(100 * len(s & seen) / len(s))
            why["copy " + r["vault"]] += 1
            continue
        seen |= s
        why["new " + r["vault"]] += 1
    io.open(OUT, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=0))
    print("DEDUPE (threshold %d%%): %d unread notes · %s -> %s" % (th * 100, len(todo), dict(sorted(why.items())), OUT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
