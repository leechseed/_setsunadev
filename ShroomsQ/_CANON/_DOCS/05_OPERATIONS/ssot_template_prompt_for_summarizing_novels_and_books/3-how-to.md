---
title: "Template Prompt for Summarizing Novels and Books: how-to"
type: how-to
for: "a writer or agent summarizing one book into the vault"
does: "gives the steps to build, extend, and run the summary prompt"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_template_prompt_for_summarizing_novels_and_books.md
source_version: 1.0.0
---

**Who it's for:** a writer or agent summarizing one book into the vault · **What it does:** gives the steps to build, extend, and run the summary prompt · **Type:** how-to

# Template Prompt for Summarizing Novels and Books: how-to

## Summarize a book end to end

1. Copy the Universal System Prompt block as the foundation.
2. Pick the add-on(s) that fit the book (3A, 3B, 3C, 3D) and append them.
3. Run Pass 1: the Universal System Prompt alone, against the full text.
4. Run Pass 2: the same text against the prompt plus the add-ons.
5. Run Pass 3: merge both outputs, remove redundancy, and check the result against the Output Structure Specification.
6. Optionally run Pass 4: elaborate the merged document with the elaboration directive.
7. Optionally run Pass 5: split the output into one file per model, named `[author_last]_[model_short_name].md`.

## Choose an add-on

1. For narratology, criticism, or craft books, use 3A.
2. For summaries that feed Dramatica work, use 3B.
3. For output that goes straight into Obsidian, Hugo, or a similar system, use 3C.
4. For a single-author theoretical work where you want the author's models, use 3D.

## Cross-reference against outside sources

1. Append the Reference Sources block to the system prompt.
2. Edit the source list for this task.
3. Check that the output gives examples where the sources reinforce or complicate the book's claims.

## Prepare a summary for the vault

1. Turn on add-on 3C.
2. Fill the YAML: `id`, `title`, `author`, `type: summary`, `source_type`, `tags`, `status: draft`, `updated`.
3. Use `##` or `###` for headers and `[[wikilinks]]` for cross-references.
4. End with a Related Entries section of 3-5 links.

## Check a finished summary

1. Confirm the sections follow the 12-row order, with only the rows your add-ons call for.
2. Confirm the TL;DR holds 6-12 bullets and the concepts section holds 10-25 entries.
3. Confirm each major section ends with a Key Idea line.
4. Confirm there is no preamble or sign-off.
5. Confirm gaps read "Not explicitly stated in provided material."

## Add a new summarization pattern

1. Do not write a new prompt elsewhere in the vault.
2. Add the pattern as a modular add-on in section 3 of the template.
