"""
codebook.py — SOP §8 is the dictionary.

BOLO 26, BUILD route (ruled 2026-09-16). The whole point of BUILD over INSTALL was
that the codebook stays in sync because it *is* the SOP. So nothing here is a copy
of §8; this parses §8 live, every run.

Two products come out of the table:

  lexicon()      the Command vocabulary, fed to Whisper as `initial_prompt` so the
                 recognizer biases toward our spellings BEFORE it guesses.
  rules()        the post-transcription find/replace table.

The honest part is what this REFUSES to replace. §8 is a read-through table written
for a human, and a good third of its rows are context-conditional — "SLP (in a
process context)", "sweep (spoken by habit)", "standing (in a canning context)".
Blind-replacing those would eat ordinary speech: every "standing" becomes "canning".
So rows carrying a context qualifier are parsed, kept, and left OFF by default.
`--aggressive` turns them on for a session; they are never silently applied.
"""

import io
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SOP = os.path.join(ROOT, "SOP.md")

# A parenthetical that names a situation is a context gate, not part of the phrase.
CONTEXT_RE = re.compile(r"\((?:[^)]*\b(?:context|spoken|as heard|after a code|repeated|by habit|×\d)\b[^)]*)\)", re.I)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def _section(text, num):
    """Slice one numbered SOP section out of the file."""
    lines = text.splitlines()
    start = None
    for i, l in enumerate(lines):
        if re.match(rf"^##\s*{num}\s*·", l):
            start = i
            break
    if start is None:
        raise SystemExit(f"SOP.md: section {num} not found — has the file been reorganized?")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    return lines[start:end]


def _variants(cell):
    """Split a Heard cell into phrases, noting which carry a context gate."""
    out = []
    for raw in cell.split("·"):
        v = raw.strip()
        if not v:
            continue
        gated = bool(CONTEXT_RE.search(v))
        v = CONTEXT_RE.sub("", v).strip()
        v = v.strip().strip('"').strip("'").strip()
        # a variant that is only a description, not something you could say, is not a rule
        if not v or v.startswith("year ranges"):
            continue
        out.append((v, gated))
    return out


def _targets(cell):
    """The bold terms in a Read-as cell, in order."""
    return [t.strip() for t in BOLD_RE.findall(cell)]


def _read_as(cell, tg):
    """
    What to actually type. Usually the bold term, but some cells carry meaning in the
    unbolded words too — "preserved **foods**" means the whole phrase, not "foods".
    Commentary after an em-dash is never part of the replacement.
    """
    # Parentheticals go FIRST. A gloss may itself contain an em-dash — "(coded 9/16 —
    # first catch from the tool)" — and splitting on the dash first would cut the
    # parenthetical in half, leaving an unbalanced "(coded 9/16" glued to the term.
    head = re.sub(r"\s*\([^)]*\)", " ", cell)
    head = re.split(r"\s+—\s+", head)[0].strip()
    if "·" not in head:
        plain = BOLD_RE.sub(r"\1", head).strip()
        if plain and len(plain) <= 40:
            return plain
    return tg[0]


def parse(path=SOP):
    """Return (rules, notes, terms). A rule is (heard, read_as, gated)."""
    text = io.open(path, encoding="utf-8").read()
    lines = _section(text, 8)

    rules, notes, terms = [], [], []
    for l in lines:
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        heard, read = cells
        if heard.lower() == "heard" or set(heard) <= set("-: "):
            continue

        tg = _targets(read)
        terms.extend(tg)
        vs = _variants(heard)

        if not tg:
            # prose guidance, not a substitution — e.g. "check against the doc"
            notes.append((heard, read))
            continue

        # "College shelf · he and" → "**CUL shelf** · **S8**" pairs positionally
        if len(tg) > 1 and len(vs) == len(tg):
            pairs = [(v, t, g) for (v, g), t in zip(vs, tg)]
        else:
            read = _read_as(read, tg)
            pairs = [(v, read, g) for v, g in vs]

        PLACEHOLDER = re.compile(r"(?<![\w-])N(?![\w-])")
        for v, t, g in pairs:
            # "the dope on N" / "goes to ex … N" are templates for a human reader,
            # not literal strings anyone says. A find/replace cannot honour them.
            if PLACEHOLDER.search(v) or "…" in v:
                notes.append((v, t))
                continue
            # "bolo polo" → "**BOLO N**": the heard phrase carries no number, so the
            # placeholder has nothing to bind to. Drop it and keep the real correction.
            if PLACEHOLDER.search(t):
                t = PLACEHOLDER.sub("", t).strip()
                if not t:
                    notes.append((v, "(placeholder only)"))
                    continue
            # A row that maps a phrase to itself is a spelling note, not a rule — but
            # compare case-sensitively: "darkroom" -> "DARKROOM" IS the correction.
            if v == t:
                continue
            rules.append((v, t, g))

    # longest first so "sit rep" wins before "rep"
    rules.sort(key=lambda r: -len(r[0]))
    return rules, notes, terms


def lexicon(path=SOP, extra=None):
    """The initial_prompt handed to Whisper. Bias, not a dictionary — Whisper has none."""
    _, _, terms = parse(path)
    seen, out = set(), []
    # the seed from the 9/3 card, kept because these are spoken constantly
    seed = [
        "Ultrasin", "Bold Venture", "BVX", "DARKROOM", "BOLO", "boresight", "Oscar Mike",
        "Charlie Mike", "RTB", "buttonhook", "break-break", "sit rep", "how copy",
        "Dramatica", "Blender", "MCDP", "DCUS", "Tori", "Anna Colson Conway", "Papi",
        "main effort", "PMCS", "Ready Rack", "Magazine", "SOP", "DOCTRINE 0",
        "DOPE SHEET", "FRAGO", "HOTLINE", "ABORT", "the Command", "Papi",
    ]
    for t in seed + terms + list(extra or []):
        t = re.sub(r"\s+", " ", t).strip()
        # drop parenthetical glosses that ride along in a bold cell
        t = re.sub(r"\s*\(.*?\)\s*", " ", t).strip()
        if not t or len(t) > 40:
            continue
        k = t.lower()
        if k in seen:
            continue
        seen.add(k)
        out.append(t)
    return ", ".join(out) + "."


def rules(path=SOP, aggressive=False):
    """The replacement table actually applied. Gated rows only on --aggressive."""
    rs, _, _ = parse(path)
    return [(h, r) for h, r, g in rs if aggressive or not g]


def apply(text, path=SOP, aggressive=False):
    """Run the codebook over a transcript. Case-insensitive, whole-phrase."""
    hits = []
    for heard, read in rules(path, aggressive):
        # \b fails on phrases ending in punctuation-ish chars; guard with lookarounds
        pat = re.compile(r"(?<![\w-])" + re.escape(heard) + r"(?![\w-])", re.I)
        text, n = pat.subn(read, text)
        if n:
            hits.append((heard, read, n))
    return text, hits


def main():
    aggressive = "--aggressive" in sys.argv
    rs, notes, _ = parse()
    active = rules(aggressive=aggressive)
    gated = [r for r in rs if r[2]]

    if "--lexicon" in sys.argv:
        print(lexicon())
        return
    if "--test" in sys.argv:
        i = sys.argv.index("--test")
        sample = " ".join(sys.argv[i + 1:]) or sys.stdin.read()
        out, hits = apply(sample, aggressive=aggressive)
        print("in  :", sample)
        print("out :", out)
        for h, r, n in hits:
            print(f"       {h!r} -> {r!r} ×{n}")
        return

    print(f"SOP §8 codebook · {len(rs)} rules parsed")
    print(f"  active   {len(active)}")
    print(f"  gated    {len(gated)}  (context-conditional, off unless --aggressive)")
    print(f"  notes    {len(notes)}  (prose guidance, never substituted)")
    print(f"  lexicon  {len(lexicon().split(', '))} terms")
    print()
    print("gated rows — these would eat ordinary speech if applied blind:")
    for h, r, _g in gated:
        print(f"    {h!r} -> {r!r}")


if __name__ == "__main__":
    main()
