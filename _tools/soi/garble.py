"""Garble finder: zero-token check of a dictation line against the SOP section 8 table.

Usage:
    python _tools/soi/garble.py "<dictation>"

Parses the table under "## 8 ·" in SOP.md at run time (never hardcoded) and adds a
small seed list. Prints one line per hit as `proword · matched text · score`, or
`no hit`. A hit is a substring match (score 1.00) or a difflib ratio >= 0.8 over
word windows of the same length. Stdlib only.
"""
import difflib
import re
import sys
from pathlib import Path

SOP = Path(__file__).resolve().parents[2] / "SOP.md"
THRESHOLD = 0.8
SEEDS = {
    "go for launch": ["go for log", "go for lunch"],
    "DARKROOM": ["black room"],
    "LEECHSEED": ["Leach Seed"],
    "how copy": ["tell copy", "hell copy"],
    "take recs": ["Take R.X."],
}


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s.lower())).strip()


def clean_cell(s):
    s = re.sub(r"\([^)]*\)", "", s)
    return s.replace('"', "").replace("“", "").replace("”", "").strip()


def load_table():
    """Return {proword: [variants]} parsed from the section 8 table in SOP.md."""
    out = {}
    in8 = False
    for line in SOP.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in8 = line.startswith("## 8 ")
            continue
        if not in8 or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Heard",) or set(cells[0]) <= set("-"):
            continue
        proword = re.sub(r"\s+", " ", clean_cell(cells[1]).replace("*", "")).split(" — ")[0].strip()
        variants = [clean_cell(v) for v in cells[0].split(" · ")]
        out.setdefault(proword, []).extend(v for v in variants if norm(v))
    return out


def find_hits(text, table):
    nt = norm(text)
    words = nt.split()
    hits = []
    for proword, variants in table.items():
        for v in variants:
            nv = norm(v)
            if not nv:
                continue
            if re.search(r"(?<![a-z0-9])" + re.escape(nv) + r"(?![a-z0-9])", nt):
                hits.append((proword, v, 1.0))
                continue
            if len(nv) < 5:
                continue
            n = len(nv.split())
            best = (0.0, "")
            for i in range(len(words) - n + 1):
                chunk = " ".join(words[i:i + n])
                r = difflib.SequenceMatcher(None, nv, chunk).ratio()
                if r > best[0]:
                    best = (r, chunk)
            if best[0] >= THRESHOLD:
                hits.append((proword, best[1], best[0]))
    return hits


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    table = load_table()
    for proword, variants in SEEDS.items():
        table.setdefault(proword, []).extend(variants)
    hits = sorted(set(find_hits(" ".join(sys.argv[1:]), table)))
    if not hits:
        print("no hit")
        return 0
    for proword, matched, score in sorted(hits, key=lambda h: -h[2]):
        print(f"{proword} · {matched} · {score:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# designed from the Steering Claude Code article + Chief's ask · BOLO 140 · 2026-10-12
