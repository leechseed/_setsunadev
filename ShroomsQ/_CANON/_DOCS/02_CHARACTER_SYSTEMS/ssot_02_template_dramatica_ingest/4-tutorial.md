---
title: "Dramatica ingest template: tutorial"
type: tutorial
for: "A newcomer filling a Dramatica ingest for the first time"
does: "Walks one learner through the form using Victoria Midnight's L12 values from the vertical slice"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_dramatica_ingest.md
source_version: 1.0.1
---

**Who it's for:** a newcomer filling the form for the first time · **What it does:** one guided pass using Victoria Midnight's L12 values · **Type:** tutorial

# Dramatica ingest template: tutorial

You will fill the sections you can check against Victoria Midnight's locked L12 block, then generate Section 10. Lookups are in the [reference](2-reference.md).

> **OPEN:** the source form is blank. The only worked values on record sit in the [vertical slice](../ssot_02_character_systems_vertical_slice/2-reference.md) instance. That instance holds the L12 fields and the motivation quad, not the full storyform. The lesson fills what it can and marks the rest `⏸`.

## Step 1. Copy and clean the form

1. Copy the file to `victoria_midnight_dramatica_ingest.md`.
2. Delete the usage section and the frontmatter.
3. Keep every section number.

## Step 2. Fill the header

Write `character_id: victoria_midnight`, the IP `overexitout`, and `tier: 3`. Set both statuses to `draft`.

## Step 3. Fill Section 1 from the record

The vertical slice gives these values. Write them in.

| Field | Value |
|---|---|
| `story_outcome` | Failure |
| `story_judgement` | Good |
| `story_limit` | Optionlock |

Write `⏸` and a reason for `story_driver`. The slice does not record it. Never guess.

## Step 4. Fill Section 2

1. Write `dramatica_archetype` as Protagonist.
2. Write `resolve` as Change.
3. Write `⏸` on `growth`, `approach`, `mental_sex` and `structural_role`. The slice does not record them.

## Step 5. Fill Section 3

1. The slice gives the motivation quad as Consider and Pursuit. Write both.
2. Write `⏸` on the other three quads. The slice gives only one element for each: Proaction, Result and Actuality. It does not give both.

Check: the form needs all eight element fields to lock. This lesson stays `draft`, and you now know why.

## Step 6. Fill Section 4

Write `mc_problem` as Equity. Write `⏸` on the rest of the thirteen fields.

## Step 7. Generate Section 10

Copy values into the L12 block.

| Block field | Value |
|---|---|
| `dramatica_archetype` | Protagonist |
| `mc_problem_element` | Equity |
| `methodology_element` | Proaction |
| `evaluation_element` | Result |
| `purpose_element` | Actuality |
| `touchstone` | cost_and_meaning |
| `story_outcome` | Failure |
| `story_judgement` | Good |
| `limit_type` | Optionlock |
| `resolve` | Change |

These are the slice's own values. Section 10 must match Sections 1 to 9. Your filled sections now agree with it for the fields you wrote.

## Step 8. Read the result

The record stays `draft`. Section 3 has gaps, the throughlines are mostly `⏸`, and Section 9 has no written Touchstone statement. The handoff checklist would fail on those items.

You have seen the whole path: fill in extraction order, write `⏸` for honest gaps, generate Section 10 last, and lock only when the checklist passes. The steps are in the [how-to](3-how-to.md).
