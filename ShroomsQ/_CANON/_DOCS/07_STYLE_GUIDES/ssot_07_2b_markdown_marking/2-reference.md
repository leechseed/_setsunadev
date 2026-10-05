---
title: "Markdown marking: reference"
type: reference
for: "A writer or reader looking up one mark, protocol or command"
does: "Lists every component and part of markdown marking 07.2b"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_2b_markdown_marking.md"
source_version: "1.0.3"
---

**Who it's for:** a writer or reader looking up one mark or command · **What it does:** lists every component and part of 07.2b · **Type:** reference

# Markdown marking: reference

One entry per component and part, in source order. The tool is `_tools/vocab_harvest.py`. The standard is BOLO 32, ruled 2026-09-06. See the [concept](1-concept.md) for the why.

## CORE METHODOLOGY — the four marks

| Mark | Syntax | Owner | Meaning |
|---|---|---|---|
| Bold | `**term**` | writer | Structure (lead-ins, labels such as **Key Idea**) and the first instance of a technical term, defined at once. |
| Highlight | `==term==` | reader | A load-bearing term captured while reading. Input to the harvest. The only mark a reader makes. |
| Italic | `_text_` | writer | Captions, source lines, asides. Never a term. |
| Wikilink | `[[term]]` | promoter | A term that has earned its own note. Replaces the highlight on promotion. |

**Rules**

1. A reader never bolds. A writer never highlights. Ink identifies the hand.
2. A highlight names a load-bearing term: a word or phrase the argument cannot stand without in this source. Unknown words go to the dictation lexicon or the spell dictionary.
3. A highlight carries no definition inline. The sense is written at harvest, in the meaning the term has in that source.
4. Every mark survives the Command editors. Prettier rewrites `*x*` to `_x_` and pads tables, and leaves `**`, `==` and `[[ ]]` alone. So write italic with underscores.
5. A highlight is removed in two cases: the term is promoted to a wikilink, or review finds it not load-bearing.
6. Highlight renders in Obsidian, and in VS Code with a preview extension. VS Code's source view shows two equals signs. The end-state renderer is the MCDP browser (BOLO 33).

Connects to: the writer's bold rule in [07.2a](../ssot_07_2a_writing_guide/2-reference.md), "Technical Precision."

## IMPLEMENTATION

Implementation has four parts. Each is one entry below.

### Reader protocol

1. Read the one-sheet in the editor. Wrap each load-bearing term as `==term==`. Wrap multi-word terms whole, for example `==commander's intent==`.
2. Do not stop to define. Do not bold. Do not annotate inline.
3. At the end of a reading block, run the harvest.

### Harvest

The command:

```
python _tools/vocab_harvest.py "<path to the one-sheet>" --senses <senses.json>
```

- **Reads:** every `==term==`, with its section heading and the sentence it sits in. It dedupes by term.
- **Writes the per-source VOCAB page:** `KNOWLEDGE_AREAS/_vocab/<ID>.vocab.md`, in the 2023 Logseq VOCAB shape. It holds the source's section outline, one `**term** — sense` line per mark, and the source sentence beneath.
- **Writes the Command register:** `_0.1_BVX_LEARN/_meta/VOCABULARY.md`. One row per (term, source), appended, never hand-typed.
- **`--senses`:** supplies each term's sense as JSON. A term without a sense is written with its sentence only. The console lists it so the sense can be supplied on the next run.

### Writer protocol

- The writer follows the [07.2a writing guide](../ssot_07_2a_writing_guide/2-reference.md) as written.
- Bold is spent on structure and on the first instance of a technical term, defined at once.
- Italic uses underscores.
- The writer does not pre-highlight terms for the reader.

### Retro-conversion

- **What it does:** converts marks already made in bold. The writer lists the exact bold spans and passes them to the harvest with `--convert-bold terms.txt`.
- **Scope:** only listed spans convert. Template bolds stay bold.
- **Producing the list:** from the git diff between the generated sheet and the marked sheet.
- **Instance:** MIL.01 converted this way on 2026-09-06: 63 spans, 62 terms after case merge.

## EXAMPLES

**Example 1: a reader mark in a Touchstone.** Before, writer-side only:

```
1. **Friction is permanent.** Friction resists all action and saps energy.
```

After the reader's pass:

```
1. **Friction is permanent.** Friction resists all action and saps ==energy==.
```

The harvest writes to `MIL.01.vocab.md`:

```
- **energy** — the capacity to act, which friction drains
  - ↳ "Friction resists all action and saps energy."
```

**Example 2: promotion.** The term `==commander's intent==` appears in MIL.01, MIL.08 and MIL.09. It receives its own note. In all three sheets the highlight becomes `[[commander's intent]]`. The register rows remain, now pointing at a note.
