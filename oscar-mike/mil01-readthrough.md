---
parked: 2026-09-06
title: The MIL.01 Read-Through
handle: mil01 readthrough
tags: reading, BVX-LEARN, vocabulary, BLACK, BOLO-31, BOLO-32, BOLO-33
status: parked on "Oscar Mike" — Core Thesis + Invariants marked and harvested; resumes at HEURISTICS
open-decision: "the dropped Invariant-1 clause (restore / keep gone) · 'ask for my confidence' — spoken at park, read provisionally as a study-loop step, unruled"
---

# THE MIL.01 READ-THROUGH

Papi is reading `KNOWLEDGE_AREAS/🧬 MIL.01 — MCDP 1 Warfighting — USMC (1997).md` and marking the load-bearing terms. The marking standard and the harvest were built around this read on 9/6.

## Where it stopped

- **Marked + harvested:** CORE THESIS and INVARIANTS. 63 marks, 62 terms after case merge, every term with its sense in MCDP 1 and the sentence it sat in.
- **Unmarked:** HEURISTICS · CORE CONCEPTS (10) · KEY VOCABULARY · NOTABLE QUOTES · WHAT DOESN'T WORK · QUICK SELF-CHECK · APPLICATION.
- **Outputs:** `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/_vocab/MIL.01.vocab.md` · `_0.1_BVX_LEARN/_meta/VOCABULARY.md` (register, 62 rows) · the senses file lives in the session scratchpad; regenerate senses at the next harvest.

## Resume

1. Papi reads on in VS Code, wrapping load-bearing terms as `==term==`. Bold is never used for marks (SOP: `📐 ssot_05_operations_markdown_marking`).
2. Papi says the section is marked. Claude writes the senses JSON for the new terms and runs:
   `python _tools/vocab_harvest.py "<MIL.01 path>" --senses <senses.json>`
   The VOCAB page regenerates; the register gains only the new rows.
3. Same loop for MIL.02 through MIL.11. Each sheet gets its own `_vocab/<ID>.vocab.md`.
4. When a term shows up across three sheets, promote it: its own note, `[[term]]` replaces the highlight.

## Open

- ~~The dropped clause~~ — **RESTORED 9/6** on Papi's call ("add the original"): Invariant 1 again ends "…continuous mutual adaptation, not of one side's execution."
- **"Ask for my confidence."** Spoken at park, before "Oscar Mike." Read provisionally as: after each study block, Claude asks Papi for a confidence rating on the material (calibration, the learning-science move). Not yet ruled or worded. If ruled, it goes into SOP §1 as a step of the reading loop.

## Related

[[project-flow]] · BOLO 33 (the MCDP browser, CK3-derived information architecture, seed) · [[verb-transitivity]] (the learning-tools lesson: minimal first)
