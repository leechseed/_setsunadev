---
title: "Step 1 source verification protocol: how-to"
type: how-to
for: A narrative designer running the Step 1 gate on a character
does: Gives the steps for running the gate, reading the light and fixing a failure
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_step_1_source_verification_protocol.md
source_version: 1.1.2
---

**Who it's for:** a narrative designer starting a Vertical Slice · **What it does:** step lists for running the gate and fixing failures · **Type:** how-to

# Step 1 source verification protocol: how-to

Check wording lives in the [reference](2-reference.md).

## Run the Step 1 gate on a Tier 3 character

1. Confirm the three documents sit in `_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/`.
2. Run Component 1, checks 1.1 to 1.7. Stop on any failure.
3. Run Component 2, checks 2.1 to 2.9. Stop on any failure.
4. Run Component 3, checks 3.1 to 3.8.
5. Read the light: green, yellow or red.
6. Proceed to Step 2 only on green or yellow.

## Run the gate on a Tier 2 character

1. Confirm the Authoritative Character Document is LOCKED.
2. Confirm a Dramatica element signature is documented (2-4 elements plus relational role tags).
3. Note any partial astrology chart (Sun, Moon, one defining aspect). It never gates.
4. Proceed to Step 2 if steps 1 and 2 hold.

## Run the gate on a Tier 1 character

1. Confirm a character brief exists.
2. Check that it holds enough detail to assign L1-L3 values.
3. Proceed to Step 2.

## Fix a failed Component 1

1. No authoritative document: write it and lock it.
2. Not locked: review it, resolve every draft element, and lock it.
3. Missing sections: complete them, using checks 1.3 to 1.7 as the list.
4. Re-run Component 1.

## Fix a failed Component 2

1. No ingest: complete the template from the locked storyform.
2. Not locked: resolve draft fields and set both status fields to `locked`.
3. Missing sections: extract the data in report priority order.
4. Match Section 10 to the L12 core list in the integration doc.
5. Re-run Component 2.

## Fix a failed Component 3

1. No ingest: run the DAI derivation from the locked Dramatica Ingest.
2. Incomplete chart: add Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant with justifications.
3. Add at least 3 aspects, each with its Dramatica tension source.
4. Add houses for the seven planets, the Chart Summary and the LEECHSEED Feed Map.
5. Point `dramatica_ingest_ref` at the locked Dramatica Ingest.
6. Re-run Component 3.

## Proceed on a yellow light

1. Tag each L1-L11 value that leans on astrology data `[ASTROLOGY_PENDING]`.
2. Version the Vertical Slice data block as `draft`.
3. Complete the astrology ingest to full status.
4. Run the Feed Validation Checklist.
5. Remove the tags and lift the `draft` label once the checklist passes.

## Set up a character's canonical folder

1. Create `_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/`.
2. Add the authoritative, Dramatica ingest and astrology ingest files named by the pattern in the reference.
3. Leave the slice file for Step 7.
4. Create `states/` when you author the first state diff.
5. Store relationship records at `_AUTHORITATIVE/[IP]/relationships/`, not in the character folder.
