---
title: "Markdown marking: how-to"
type: how-to
for: "A writer or reader who knows the four marks and needs to do one marking task"
does: "Gives numbered steps for the recurring tasks in markdown marking 07.2b"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_2b_markdown_marking.md"
source_version: "1.0.3"
---

**Who it's for:** a writer or reader doing one marking task · **What it does:** gives numbered steps for each recurring 07.2b task · **Type:** how-to

# Markdown marking: how-to

Terms are defined in the [reference](2-reference.md).

## Mark a document as a reader

1. Open the one-sheet in the editor.
2. When you reach a load-bearing term, wrap it: `==term==`.
3. Wrap a multi-word term whole.
4. Do not define it. Do not bold. Do not annotate inline.
5. Skip unknown words. Send those to the dictation lexicon or the spell dictionary.
6. At the end of the reading block, run the harvest.

## Run the harvest

1. Prepare a `senses.json` with a sense for each term you want defined.
2. Run:

```
python _tools/vocab_harvest.py "<path to the one-sheet>" --senses <senses.json>
```

3. Open the per-source page at `KNOWLEDGE_AREAS/_vocab/<ID>.vocab.md`.
4. Check the register at `_0.1_BVX_LEARN/_meta/VOCABULARY.md` for the new rows.
5. Read the console list of terms with no sense.
6. Add senses for those terms to `senses.json` and run the harvest again.

## Mark a document as a writer

1. Follow the writing guide.
2. Bold only structure and the first instance of a technical term. Define the term at once.
3. Write italic with underscores, for captions, source lines and asides.
4. Do not pre-highlight terms for the reader.

## Convert marks made in bold

1. Produce the list of exact bold spans from the git diff between the generated sheet and the marked sheet.
2. Save the list as `terms.txt`.
3. Run the harvest with `--convert-bold terms.txt`.
4. Confirm that only the listed spans converted and the template bolds stayed bold.

## Promote a term to a wikilink

1. Confirm the term earned its own note, for example because it recurs across several sheets.
2. Create the note.
3. In every sheet, replace `==term==` with `[[term]]`.
4. Leave the register rows in place. They now point at the note.

## Remove a highlight

1. Check the two permitted cases: the term is promoted, or review finds it not load-bearing.
2. If neither applies, keep the highlight.
3. If one applies, delete the `==` marks (or replace them with the wikilink).
