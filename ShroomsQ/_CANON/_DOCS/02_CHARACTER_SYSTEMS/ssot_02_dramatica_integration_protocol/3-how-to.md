---
title: "Dramatica integration protocol: how-to"
type: how-to
for: A narrative designer binding or revising a character's Dramatica data
does: Gives the steps for the recurring tasks in the Dramatica integration protocol
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮 ssot_02_dramatica_integration_protocol.md
source_version: 1.2.2
---

**Who it's for:** a narrative designer who already knows the pipeline · **What it does:** step lists for the protocol's recurring tasks · **Type:** how-to

# Dramatica integration protocol: how-to

Field definitions live in the [reference](2-reference.md).

## Register a storyform

1. Pick a unique `storyform_id`, such as `oxo_primary_v1`.
2. Fill `ip`, `scope`, `status` and `version`.
3. Set `parent_storyform_id` to `null` for a primary form.
4. Set `status` to `locked` only when the storyform is final.

## Nest a storyform inside a parent

1. Give the nested storyform its own `storyform_id`.
2. Set `parent_storyform_id` to the parent's id.
3. Bind each character to the nested form with a separate binding record.
4. Create one L12 sub-table record per role, keyed to the right `storyform_id`.
5. Where the nested form conflicts with the parent, follow the parent.

## Bind a character to a storyform

1. Write one binding record with `character_id`, `storyform_id`, `structural_role`, `archetype`, `resolve` and `throughline`.
2. Write one more record for each extra storyform the character joins.
3. Leave the L1-L11 record singular.

## Fill a Tier 3 Dramatica Ingest Template

1. Open the blank form: [ssot_02_template_dramatica_ingest.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_template_dramatica_ingest.md).
2. Extract from the Story Dynamics Report. Lock resolve, outcome, judgment and limit type.
3. Extract from the MC Theme Report. Lock the MC variable set.
4. Extract from the Character Report. Lock the element quads and archetype.
5. Extract from the OS, IC and RS Theme Reports.
6. Consult the Character Relationships Report for Tier 2 roles.
7. Lock the template.

## Build the L12 block for a Tier 3 character

1. Fill the 10 core variables from the storyform and the element set.
2. Author the `touchstone`. Cite it as TS n:m.
3. Fill the L12_DRAMATICA_EXTENDED sub-table from the ingest.
4. Leave a field empty if the ingest has not yielded it yet.
5. Add `convention_role` only if a genre applies.

## Give a Tier 2 character a Dramatica fingerprint

1. Choose 2-4 elements from the Motivation, Methodology, Evaluation and Purpose sets. Write them as `element_signature`.
2. Pick a relational role for each Tier 3 character it touches. The choices are mirror, foil, catalyst, threshold_guardian, herald, mentor, trickster, shapeshifter or anchor.
3. Write the pairs into `relational_roles`.
4. Skip the binding record, throughline and sub-table.

## Promote a Tier 1 character

1. Confirm the character now needs tracking.
2. Promote the character to Tier 2.
3. Add an element signature and relational roles as above.

## Revise a storyform

1. Create a new storyform version. Never edit the locked one.
2. Pass the new ingest through the Step 1 gate.
3. Re-run the DAI derivation. Save the new chart as its own file. Mark the old chart superseded.
4. Re-extract the L12 core block and sub-table.
5. Re-run Vertical Slice Steps 5 and 6. Save a new base record version.
6. Read each state diff. Check each "was ..." value against the new base.
7. Revise or retire each mismatched diff. Log the change.
