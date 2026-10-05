---
title: "Astrology ingest template: how-to"
type: how-to
for: "A writer who must produce a filled astrology ingest for a Tier 3 character"
does: "Gives numbered steps for each task of filling and locking the form"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_astrology_ingest.md
source_version: 1.0.0
---

**Who it's for:** a writer filling an astrology ingest for a Tier 3 character · **What it does:** numbered steps for each fill, feed and lock task · **Type:** how-to

# Astrology ingest template: how-to

Field lookups: [reference](2-reference.md). Why: [concept](1-concept.md). Prerequisite: a locked [Dramatica ingest](../ssot_02_template_dramatica_ingest/3-how-to.md).

## Start a character's astrology ingest

1. Confirm the character is Tier 3. A Tier 2 character does not use this form.
2. Confirm a locked Dramatica Ingest exists for the character.
3. Copy the blank file to the character's folder as `[CHARACTER_ID]_astrology_ingest.md`.
4. Delete the "How to use this form" section and the frontmatter.
5. Keep every section number.
6. Fill the Header: `character_id`, `ip`, `tier: 3`, `dramatica_ingest_ref`, `storyform_id`, `storyform_version`, `dai_doc_version`.
7. Set `template_status` to `draft`.

## Fill the planets and angles

1. Open the DAI doc. Work in its order.
2. For each of Sun, Moon, Mercury, Venus and Mars (section 1), read the Dramatica source in the table.
3. Pull those values from the Dramatica Ingest. Choose the sign.
4. Write a one or two sentence derivation: the Dramatica input, the rule you used, why the sign fits.
5. Repeat for Saturn, Jupiter, Uranus, Neptune and Pluto (section 2).
6. Repeat for Ascendant, Midheaven, Descendant and IC (section 3). Place the Descendant opposite the Ascendant and the IC opposite the Midheaven.
7. If the storyform gives no value yet, write `⏸` and the reason. Never guess.

## Build the aspect map

1. Pick pairs of planets whose Dramatica elements are in tension or flow.
2. Add one row per aspect: Planet A, Planet B, Aspect, Dramatica tension source, Gate, Note.
3. Use Opposition for Problem and Solution, and Square for Focus and Direction. Use Conjunction or Square for Unique Ability and Critical Flaw. Use Trine for reinforcing quad elements.
4. Write at least three rows for a minimum viable chart.
5. If sign geometry disagrees with the Dramatica tension, follow the tension.

## Place the houses

1. Write the MC Domain emphasis pattern on the first line of section 5.
2. Add a row for Sun, Moon, Mercury, Venus, Mars and Saturn with a house and a justification.
3. Leave the Ascendant at house 1.

## Add dignities and the 12th House contents

1. For each planet, write the sign and one dignity value: Essential Dignity, Essential Debility or Peregrine.
2. If you override the default, write the justification.
3. In section 7, list each planet whose Dramatica function is submerged.
4. Link each to its L10 SHADOW content.
5. Skip sections 6 and 7 if you are aiming only for `minimum_viable`.

## Write the chart summary

1. Write six to ten sentences in plain words.
2. State what the chart says about the character.
3. State where the chart pulls in two directions.

## Fill the 12-layer feed map

1. Open the 12-layer mapping doc.
2. For each layer L1 to L11, read the chart source in the form's table.
3. Compare the chart with the layer's value. Write yes, no or exception.
4. In the notes column, explain any conflict and how you resolved it. The layer value stays authoritative.
5. Write n/a on L12. It comes from the Dramatica Ingest.
6. Do not fill schema 2.5.0 or 3.0.0 fields from the chart.

## Lock the chart

1. Check the seven items in section 10. They are locked Dramatica reference, seven planets with derivations and three or more aspects. They also include seven houses, the summary, the feed map and the Feed Validation Checklist.
2. For `minimum_viable`, skip the Feed Validation Checklist. Set `template_status` to `minimum_viable`.
3. Expect a yellow light at the Step 1 gate. Layers fed by the chart carry `[ASTROLOGY_PENDING]`.
4. For `locked`, run the Feed Validation Checklist in the mapping doc. Pass it, or log the exceptions.
5. Set `locked_on` and `template_status: locked` only after the checklist passes.
