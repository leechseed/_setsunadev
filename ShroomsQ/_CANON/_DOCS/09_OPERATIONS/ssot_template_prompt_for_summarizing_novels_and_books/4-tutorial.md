---
title: "Template Prompt for Summarizing Novels and Books: tutorial"
type: tutorial
for: "a writer running a first book summary through the template"
does: "walks one theory book through the passes with a narratology add-on"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_template_prompt_for_summarizing_novels_and_books.md
source_version: 1.0.0
---

**Who it's for:** a writer running a first book summary through the template · **What it does:** walks one theory book through the passes with a narratology add-on · **Type:** tutorial

# Summarize your first book

You will run the template on one book from the source's own list of lenses. The book is a screenwriting craft book such as McKee's *Story*. You finish with a merged summary in the canonical order.

## Step 1. Build the prompt

Copy the Universal System Prompt. A craft book is narratology-adjacent, so append add-on 3A. You want the output in the vault, so also append 3C.

## Step 2. Run Pass 1

Run the Universal System Prompt alone on the full text. You get a structured summary: metadata, abstract, TL;DR, contents, breakdown, concepts, synthesis.

## Step 3. Run Pass 2

Run the prompt plus 3A and 3C on the same text. Each framework now has a definition, explanation, relevance to a writer, and lineage. The YAML front matter and Related Entries appear.

## Step 4. Merge

Combine both outputs. Remove duplicated bullets. Check the order against the 12-row table: front matter first, Related Entries last.

## Step 5. Check yourself

- The abstract is one paragraph with no bullets.
- The TL;DR has between 6 and 12 bullets.
- Nothing speaks to the reader outside the summary.
- Every unknown reads "Not explicitly stated in provided material."

## Step 6. File it

Save one file for the one book. Tag it in the YAML. Link the Related Entries.

Next, read the [how-to](3-how-to.md) for the optional elaboration and split passes.
