# -*- coding: utf-8 -*-
"""RTB prep — the zero-token half of the card-clearing pass (BOLO 51 phase 6, the formation).

Usage:  python _tools/oscarmike/rtb_prep.py

Reads   oscar-mike/INDEX.md + every card file
Writes  _tools/oscarmike/work/rtb/cards.md       every open card: handle · title · parked · tags · status · the card's own resume/decision lines
        _tools/oscarmike/work/rtb/brief.DISPO.md the haiku brief: one disposition line per card
The main line then reads dispositions.md (~22 lines), rules each (PROMOTE → where · DELETE · KEEP), and executes.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CARDS = os.path.join(ROOT, "oscar-mike")

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")

def main():
    idx = io.open(os.path.join(CARDS, "INDEX.md"), encoding="utf-8").read()
    rows = re.findall(r"^\| `([^`]+)` \| (.+?) \| (\d{4}-\d{2}-\d{2}) \| (.+?) \| (.+?) \|$", idx, re.M)
    open_rows = [r for r in rows if "RTB" not in r[4] and "deleted" not in r[4].lower()]
    files = {f[:-3].lower(): f for f in os.listdir(CARDS) if f.endswith(".md") and f not in ("INDEX.md", "README.md")}
    out = [f"# OPEN CARDS · {len(open_rows)} of {len(rows)}\n"]
    for h, t, d, tags, st in open_rows:
        key = h.lower().replace(" ", "-")
        fn = files.get(key) or next((v for k, v in files.items() if key.split("-")[0] in k), None)
        body = io.open(os.path.join(CARDS, fn), encoding="utf-8").read() if fn else ""
        keep = [l for l in body.splitlines() if re.search(r"resume|decision|open|ruling|next|promote|pointer", l, re.I)][:8]
        out.append(f"## `{h}` — {t}\nparked {d} · tags: {tags} · status: {st}\nfile: {('oscar-mike/' + fn) if fn else 'NOT FOUND'}\n" + "\n".join("  " + l.strip()[:200] for l in keep) + "\n")
    wd = os.path.join(HERE, "work", "rtb")
    os.makedirs(wd, exist_ok=True)
    cards_p = os.path.join(wd, "cards.md")
    io.open(cards_p, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    brief = f"""You are DISPO, the RTB specialist. Model: haiku.
READ: {rel(cards_p)} only.
WRITE: {rel(os.path.join(wd, 'dispositions.md'))} — one line per card, in the same order:
  `handle` · PROPOSE: PROMOTE → <the real file it should go home to, guessed from its tags and pointers> | DELETE (nothing in it that is not already elsewhere) | KEEP (mid-flight, resumes on a named event) · one clause of why.
RULES: propose only; never edit a card; never read another file; one line per card, under 40 words. Reply with the path and nothing else.
"""
    io.open(os.path.join(wd, "brief.DISPO.md"), "w", encoding="utf-8", newline="\n").write(brief)
    print(f"RTB prep · {len(open_rows)} open card(s) of {len(rows)} · {rel(cards_p)} ({os.path.getsize(cards_p)//1024} KB)")
    print(f"brief: {rel(os.path.join(wd, 'brief.DISPO.md'))} → launch DISPO (haiku) → read dispositions.md → rule each line → execute")

if __name__ == "__main__":
    main()
