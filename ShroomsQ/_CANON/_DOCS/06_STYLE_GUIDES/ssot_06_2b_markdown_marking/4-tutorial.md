---
title: "Markdown marking: tutorial"
type: tutorial
for: "A new reader or writer learning the four marks by working the source's own example"
does: "Teaches the marking cycle by marking, harvesting and promoting one term"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/06_STYLE_GUIDES/📐 ssot_06_2b_markdown_marking.md"
source_version: "1.0.2"
---

**Who it's for:** a new reader or writer learning by doing · **What it does:** works the source's own example through mark, harvest and promotion · **Type:** tutorial

# Markdown marking: one term, start to finish

The source's example uses the sheet MIL.01. You will follow the same line through three stages. Keep the [reference](2-reference.md) open.

## Step 1: start with the writer's line

The writer wrote this line. It carries the writer's bold:

```
1. **Friction is permanent.** Friction resists all action and saps energy.
```

The bold is structure. Leave it alone.

## Step 2: mark as the reader

You read the line. The argument rests on the word "energy." Wrap it:

```
1. **Friction is permanent.** Friction resists all action and saps ==energy==.
```

You used highlight, not bold, because ink identifies the hand. Do not define the word. Do not annotate.

## Step 3: harvest

At the end of the reading block, run:

```
python _tools/vocab_harvest.py "<path to the one-sheet>" --senses <senses.json>
```

If your `senses.json` holds a sense for "energy," the script writes this to `MIL.01.vocab.md`:

```
- **energy** — the capacity to act, which friction drains
  - ↳ "Friction resists all action and saps energy."
```

It also appends one row for (energy, MIL.01) to the register, `VOCABULARY.md`.

## Step 4: promote

Suppose a term such as `==commander's intent==` shows up in MIL.01, MIL.08 and MIL.09. It has earned its own note. Create the note. Then, in all three sheets, replace the highlight with `[[commander's intent]]`.

The register rows stay. They now point at a note.

## Step 5: check your work

You touched all four marks. The writer's bold stayed. Your highlight became a harvest row. Promotion turned a highlight into a wikilink. Italic, the fourth mark, stays with the writer for captions. For other tasks, see the [how-to](3-how-to.md).
