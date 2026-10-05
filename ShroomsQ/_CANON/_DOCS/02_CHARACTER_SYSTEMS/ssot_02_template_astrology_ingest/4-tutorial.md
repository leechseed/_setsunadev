---
title: "Astrology ingest template: tutorial"
type: tutorial
for: "A newcomer filling an astrology ingest for the first time"
does: "Walks one learner through a minimum viable chart using the form's own structure"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_astrology_ingest.md
source_version: 1.0.0
---

**Who it's for:** a newcomer filling the form for the first time · **What it does:** one guided pass to a minimum viable chart · **Type:** tutorial

# Astrology ingest template: tutorial

You will fill the form as far as `minimum_viable` and read the result. Lookups are in the [reference](2-reference.md).

> **OPEN:** the source holds no completed instance of this form. It is blank. Victoria Midnight has Dramatica values in the vertical slice, but her signs are not on record. This lesson fills structure and derivations. Signs come from the DAI doc, and you supply them.

## Before you start

You need a locked Dramatica Ingest for your character and the DAI doc open. Use Victoria Midnight's L12 values from the [vertical slice](../ssot_02_character_systems_vertical_slice/2-reference.md) as the Dramatica input. They are MC Problem Equity, methodology Proaction, evaluation Result, purpose Actuality, limit Optionlock.

## Step 1. Copy and clean the form

1. Copy the file to `victoria_midnight_astrology_ingest.md`.
2. Delete the usage section and the frontmatter.
3. Keep every section number.

## Step 2. Fill the header

Write the character id, the IP, `tier: 3`, the path to the Dramatica Ingest, and the storyform id. Set `template_status: draft`.

## Step 3. Fill section 1

1. Take Mars first. Its source is Approach plus the Motivation quad.
2. Look up the DAI rule for Mars. Choose the sign.
3. Write the derivation in two sentences: the input, the rule, why it fits.
4. If the Dramatica Ingest lacks a value, write `⏸` and the reason.

Check: every row has a sign or a `⏸`, and every sign has a derivation.

## Step 4. Fill sections 2 and 3 for the minimum

A minimum viable chart needs Saturn and the Ascendant from these two sections. Fill those with derivations. Leave Jupiter, Uranus, Neptune, Pluto and the other angles for later.

## Step 5. Add three aspects

1. Add one row for a pair in tension, such as Problem against Solution. Use Opposition.
2. Add a second row from the Focus and Direction pair. Use Square.
3. Add a third from reinforcing elements in a quad. Use Trine.
4. Name the gate in each row.

Check: three rows, each with a Dramatica tension source.

## Step 6. Place the houses

Write the MC Domain emphasis pattern. Then give Sun, Moon, Mercury, Venus, Mars and Saturn each a house and a justification. Leave the Ascendant at 1.

## Step 7. Summarize and map

1. Write the chart summary: six to ten plain sentences.
2. Fill the feed map row by row. Write yes, no or exception against each layer value.
3. Write n/a on L12.

## Step 8. Set the status

Skip sections 6 and 7. Skip the Feed Validation Checklist. Set `template_status` to `minimum_viable`.

You made a chart that passes the Step 1 gate as a yellow light. Layers it feeds carry `[ASTROLOGY_PENDING]`. To reach `locked`, fill sections 6 and 7 and pass the Feed Validation Checklist. The steps are in the [how-to](3-how-to.md).
