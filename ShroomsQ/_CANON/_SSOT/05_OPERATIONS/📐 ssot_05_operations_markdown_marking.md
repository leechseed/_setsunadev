---
type: ssot_05_operations
category: operations
version: 1.0.0
last_updated: 2026-09-06
applies_to: [BVX-LEARN, OVEREXITOUT, ASTRO7EX, SSOT]
status: canonical — RULED 2026-09-06 on the BOLO 32 boresight
purpose: "Assigns one meaning to each inline mark in house Markdown so that writer-side structure and reader-side capture never share ink."
dependencies: ["[[📐 ssot_writing_guide]]", "[[📐ssot_SSOT_CREATION]]", "[[📐 ssot_template_prompt_for_summarizing_novels_and_books]]"]
trunk: BLACK
bolo: 32
tool: _tools/vocab_harvest.py
---

# 📐 ssot_05_operations_markdown_marking

## TABLE OF CONTENTS

- [Purpose](#purpose)
- [Core Methodology — the four marks](#core-methodology--the-four-marks)
- [Implementation](#implementation)
- [Examples](#examples)
- [Version History](#version-history)

## PURPOSE

Two people mark the same document. The writer marks structure and first-instance terms. The reader marks the terms the argument rests on. Before this standard both used bold, and a one-sheet carrying 26 template bolds and 63 reader bolds could not be told apart by eye or by script. This document gives each party its own ink, keeps every mark safe under a format-on-save editor, and makes reader marks harvestable by one command.

## CORE METHODOLOGY — the four marks

| Mark | Syntax | Owner | Meaning |
|---|---|---|---|
| **Bold** | `**term**` | writer | Structure (lead-in sentences, labels such as **Key Idea**) and the first instance of a technical term, defined immediately, per [[📐 ssot_writing_guide]] Technical Precision. |
| ==Highlight== | `==term==` | reader | A load-bearing term captured while reading. Input to the harvest. The only mark a reader makes. |
| _Italic_ | `_text_` | writer | Captions, source lines, asides. Never a term. |
| [[Wikilink]] | `[[term]]` | promoter | A term that has earned its own note. Replaces the highlight on promotion. |

Rules:

1. A reader never bolds. A writer never highlights. Ink identifies the hand.
2. A highlight names a **load-bearing term**: a word or phrase the argument cannot stand without in this source. It does not name an unknown word; unknown words go to the dictation lexicon or the spell dictionary.
3. A highlight carries no definition inline. The sense is written at harvest, into the VOCAB page, in the meaning the term has **in that source**.
4. Every mark in this table survives the house editors. Prettier rewrites `*x*` to `_x_` and pads tables; it leaves `**`, `==`, and `[[ ]]` alone. Italic is therefore written with underscores from the start.
5. A highlight is removed in exactly two cases: the term is promoted to a wikilink, or review finds it is not load-bearing.
6. Highlight renders in Obsidian and in VS Code with a preview extension; in the VS Code source view it is read as the two equals signs. The end-state renderer is the MCDP browser (BOLO 33).

## IMPLEMENTATION

### Reader protocol

1. Read the one-sheet in the editor. On a load-bearing term, wrap it: `==term==`. Multi-word terms are wrapped whole (`==commander's intent==`).
2. Do not stop to define. Do not bold. Do not annotate inline.
3. At the end of a reading block, run the harvest.

### Harvest

```
python _tools/vocab_harvest.py "<path to the one-sheet>" --senses <senses.json>
```

The script reads every `==term==` with its section heading and the sentence it sits in, dedupes by term, and writes:

- **The per-source VOCAB page** at `KNOWLEDGE_AREAS/_vocab/<ID>.vocab.md`, in the 2023 Logseq VOCAB shape: the source's section outline, one `**term** — sense` line per mark, the sentence it came from beneath it.
- **The house register** at `_0.1_BVX_LEARN/_meta/VOCABULARY.md`: one row per (term, source), appended, never hand-typed.

`--senses` supplies the sense per term as JSON. A term without a sense is written with its sentence only and is listed on the console so the sense can be supplied on the next run.

### Writer protocol

The writer follows [[📐 ssot_writing_guide]] as written. Bold is spent on structure and on the first instance of a technical term, defined immediately. Italic is written with underscores. The writer does not pre-highlight terms for the reader.

### Retro-conversion

Marks already made in bold are converted by listing the exact bold spans and passing them to the harvest: `--convert-bold terms.txt`. Only listed spans convert, so template bolds stay bold. The list is produced from the git diff between the generated sheet and the marked sheet. MIL.01 was converted this way on 2026-09-06 (63 spans, 62 terms after case merge).

## EXAMPLES

**Example 1 — a reader mark in an invariant.**

Before, writer-side only:

```
1. **Friction is permanent.** Friction resists all action and saps energy.
```

After the reader's pass:

```
1. **Friction is permanent.** Friction resists all action and saps ==energy==.
```

Harvest writes to `MIL.01.vocab.md`:

```
- **energy** — the capacity to act, which friction drains
  - ↳ "Friction resists all action and saps energy."
```

**Example 2 — promotion.** The term `==commander's intent==` appears in MIL.01, MIL.08, and MIL.09 and receives its own note. In all three sheets the highlight becomes `[[commander's intent]]`; the register rows remain, now pointing at a note.

## VERSION HISTORY

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-06 | Ruled on the BOLO 32 boresight: four marks, reader/writer split, harvest tool, retro-conversion of MIL.01. |
