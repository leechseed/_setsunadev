---
title: "Astrology ingest template: concept"
type: concept
for: "A writer deciding whether and why each Tier 3 character needs a chart form"
does: "Explains why the astrology ingest form exists and what its structure protects"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_astrology_ingest.md
source_version: 1.0.0
---

**Who it's for:** a writer deciding why each Tier 3 character needs a chart form · **What it does:** explains why the form exists and what its structure protects · **Type:** concept

# Astrology ingest template: concept

Pages in this set: [reference](2-reference.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md). The source is [ssot_02_template_astrology_ingest.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_template_astrology_ingest.md). The method behind it is in [character astrology](../ssot_02_character_astrology/1-concept.md).

## The form turns a method into a record

The Character Astrology doc says how a chart is derived. This template is the place where one character's chart is written down. It is a blank fill-in form. The writer makes one copy per Tier 3 character. The filled copy holds the natal chart derived from the Dramatica Ingest through the DAI rules.

A method without a form lets every writer record a different shape. A form fixes the shape, so a checker can read any chart the same way.

## The section numbers are a contract

The form tells the writer to delete the instructions and frontmatter but to keep the section numbers. The reason is that the Step 1 checks cite those numbers. A renumbered form breaks the citations.

The section order follows the DAI order: planets, then angles, aspects, houses, dignities and the 12th House. The writer works down the form in the same order the derivation runs.

## Every sign must carry its reason

The form demands a one or two sentence derivation for every sign. The derivation names the Dramatica input, the rule used and why the sign fits. A sign with no derivation is a guess, and the system forbids guesses. Where the storyform gives nothing yet, the writer writes `⏸` and the reason. An honest gap is allowed. A guessed value is not.

## The chart justifies the layers and never sets them

Section 9 maps the chart onto the 12 layers. The form states the direction plainly: the chart justifies a layer value and never sets one. Layer 12 has no chart source at all. It comes from the Dramatica Ingest. The 12-layer values stay authoritative, and the chart is checked against them.

## A minimum chart lets work continue

The form defines a minimum viable chart: sections 1 to 5 and 8 to 10. It needs seven planets and angles placed, at least three aspects, and houses for those seven. Sections 6 and 7 can wait. A minimum viable chart passes the Step 1 gate as a yellow light. The layers it feeds carry `[ASTROLOGY_PENDING]` until the chart is `locked`.

This keeps the pipeline moving without pretending the chart is finished.

## The long read

The form is small because the real rules live elsewhere. The header points to the locked Dramatica Ingest. The derivations point to the DAI doc. The feed map points to the mapping doc. The lock checklist points to the mapping doc's Feed Validation Checklist.

That design means the form can stay stable while the rules around it change. A reader who wants to know why Venus sits where it does reads the DAI doc. A reader who wants to know whether a chart is finished reads section 10.

A Tier 2 character does not use this form. That character gets a partial chart in a lighter record. So the form stays reserved for the characters who carry full weight.
