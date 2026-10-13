"""langextract trial (BOLO 140, pick lx-02 · ruled 10/13 "GO" on qwen2.5:14b).

Runs the fabula-event schema over one note on local Ollama and writes a review file.
Nothing here touches canon: the output is a review file under _tools/extract/out/.

Usage (from the repo root, the .venv python):
  .venv/Scripts/python _tools/extract/trial.py <note.md> [--model qwen2.5:14b] [--passes 2]

Rows the model cannot ground in the source text (no char_interval) are dropped and counted.
The worked examples below are built from the ruled fabula (_tools/worldview/fabula.json).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import langextract as lx
from langextract import data

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_tools/extract/out"

ERAS = "1 Skeeter Creek · 2 DCUS · 3 LAKAD · 4 ASTRO7EX · 5 beyond"

PROMPT = f"""Extract every story EVENT from the text, in order of appearance.
An event is something that happens or happened in the story world: a founding, a crash, a rename, a rise, a birth, a departure.
Use the exact words of the text for extraction_text; never paraphrase and never invent.
Attributes: who (the actor), what (one short phrase), when (a year or 'unknown'), where (a place or 'unknown'),
era (one of: {ERAS}, or 'unknown').
Ideas, theory, questions, and notes about writing are NOT events; skip them."""


def _ex(text: str, rows: list[tuple[str, dict]]) -> data.ExampleData:
    for span, _ in rows:
        assert span in text, f"example span not in text: {span!r}"
    return data.ExampleData(
        text=text,
        extractions=[
            data.Extraction(extraction_class="event", extraction_text=span, attributes=attrs)
            for span, attrs in rows
        ],
    )


EXAMPLES = [
    _ex(
        "In 2099 the Moon nukes orbit into a Kessler cascade. The Moon Severance cuts Earth off from space, "
        "and the Narco Republic rises in the Americas.",
        [
            ("the Moon nukes orbit into a Kessler cascade",
             {"who": "the Moon", "what": "Kessler cascade", "when": "2099", "where": "orbit", "era": "1 Skeeter Creek"}),
            ("the Narco Republic rises in the Americas",
             {"who": "the Narco Republic", "what": "rises", "when": "unknown", "where": "the Americas", "era": "1 Skeeter Creek"}),
        ],
    ),
    _ex(
        "The Bishops buy Red Hills Academy from the founder's son and rebrand it as DCUS. "
        "In 2199 Tori overrides the pace notes on the Delta Coast run and Jebb dies in the crash.",
        [
            ("The Bishops buy Red Hills Academy from the founder's son and rebrand it as DCUS",
             {"who": "the Bishops", "what": "rebrand Red Hills Academy as DCUS", "when": "unknown", "where": "Red Hills Academy", "era": "2 DCUS"}),
            ("Jebb dies in the crash",
             {"who": "Jebb Midnight", "what": "dies in the crash", "when": "2199", "where": "Delta Coast", "era": "2 DCUS"}),
        ],
    ),
    _ex(
        "The characters take a rocket up and the story leaves Earth for cislunar space. "
        "Vivian is born in Aldrin Sector on the Moon on 2091-10-10. "
        "Plot is the order the audience sees events; fabula is the order they happened.",
        [
            ("The characters take a rocket up",
             {"who": "the characters", "what": "leave Earth", "when": "unknown", "where": "cislunar space", "era": "3 LAKAD"}),
            ("Vivian is born in Aldrin Sector on the Moon",
             {"who": "Vivian", "what": "born", "when": "2091-10-10", "where": "Aldrin Sector, the Moon", "era": "4 ASTRO7EX"}),
        ],
    ),
]


def run(note: Path, model_id: str, passes: int, model_url: str) -> Path:
    text = note.read_text(encoding="utf-8", errors="replace")
    t0 = time.time()
    result = lx.extract(
        text_or_documents=text,
        prompt_description=PROMPT,
        examples=EXAMPLES,
        model_id=model_id,
        model_url=model_url,
        extraction_passes=passes,
        max_char_buffer=1000,
        show_progress=False,
    )
    secs = time.time() - t0
    OUT.mkdir(parents=True, exist_ok=True)
    stem = note.stem.replace(" ", "_")
    rows, dropped = [], 0
    for e in result.extractions:
        ci = e.char_interval
        if ci is None or ci.start_pos is None:
            dropped += 1
            continue
        rows.append({
            "class": e.extraction_class,
            "text": e.extraction_text,
            "start": ci.start_pos, "end": ci.end_pos,
            "align": str(e.alignment_status).split(".")[-1] if e.alignment_status else "",
            **{k: (e.attributes or {}).get(k, "") for k in ("who", "what", "when", "where", "era")},
        })
    jl = OUT / f"{stem}.jsonl"
    with jl.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    rev = OUT / f"{stem}.review.md"
    lines = [
        f"# langextract trial · {note.name}",
        "",
        f"model `{model_id}` · passes {passes} · {len(text):,} chars · {secs:.0f} s · "
        f"grounded rows {len(rows)} · dropped (ungrounded) {dropped}",
        "",
        "Score each row by hand: right · wrong · ungrounded. The 70% line decides the wrap (BOLO 140 lx-01).",
        "",
        "| # | score | who | what | when | where | era | quote | pos |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        q = r["text"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {i} |  | {r['who']} | {r['what']} | {r['when']} | {r['where']} | {r['era']} | {q} | {r['start']}-{r['end']} |")
    rev.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{note.name}: {len(rows)} grounded · {dropped} dropped · {secs:.0f} s · {rev}")
    return rev


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("note", nargs="*")
    ap.add_argument("--queue", help="a file with one note path per line (CRLF tolerated)")
    ap.add_argument("--model", default="qwen2.5:14b")
    ap.add_argument("--passes", type=int, default=2)
    ap.add_argument("--url", default="http://localhost:11434")
    a = ap.parse_args()
    notes = list(a.note)
    if a.queue:
        notes += [ln.strip() for ln in Path(a.queue).read_text(encoding="utf-8").splitlines() if ln.strip()]
    for n in notes:
        try:
            run(Path(n), a.model, a.passes, a.url)
        except Exception as e:          # one bad note never stops the queue; the log says which
            print(f"{n}: FAILED · {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
