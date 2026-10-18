---
name: sitrep
description: 'Use when Chief asks where things stand: "sit rep", "the board", "where did we leave off", "what are we working on", or the countersign.'
---

# The sit rep

The procedure lives in the driver script (BOLO 155 M7, 10/18). Run each phase and do exactly what its `NEXT` lines say.

```
python _tools/sitrep/run.py          # H0 prep, then the H1 order
python _tools/sitrep/run.py fanin    # H2 RANGE, reruns, then your two files
python _tools/sitrep/run.py close    # H3 build, flush, then the publish
```

## The doctrine (BOLO 54, never bent)

- The main line never opens STATE, BOLO, SOP, PROJECTS or the cache notes. It reads the digest and writes only Block VI and the meta patch.
- Three specialists, launched in one message **by name** (`drafting-rack-block` · `drafting-index-blocks` · `drafting-watch-block`), each with its brief verbatim. No agent reads another's input or output. A gear shift never adds a fourth.
- RANGE is a script (`assemble.py`), never a checker agent. A role reruns once per board; what survives goes in the caveat.
- `stats` in the meta patch is a list of "label: value" strings, never a dict.

## The reply (ruled 10/6)

Left off (one sentence) · **Start next: BOLO N** (a five-word why) · the link · Block 0 in three bullets · the leverage line · one caveat line only if RANGE left advisory findings. No preamble, no questions.

The pre-M7 skill text (the full step-by-step) is in `references/SKILL.pre-M7.md`; history and costs in `references/history.md`.
