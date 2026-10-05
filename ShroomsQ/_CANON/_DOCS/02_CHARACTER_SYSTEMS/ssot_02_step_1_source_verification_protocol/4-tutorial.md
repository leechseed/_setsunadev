---
title: "Step 1 source verification protocol: tutorial"
type: tutorial
for: A new narrative designer learning the gate by running it once
does: Walks one Tier 3 gate run, with a yellow-light ending, from the first check to the decision
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_step_1_source_verification_protocol.md
source_version: 1.1.1
---

**Who it's for:** a new narrative designer · **What it does:** one gate run for a Tier 3 character · **Type:** tutorial

# Tutorial: run the gate on a Tier 3 character

You will run Step 1 on a Tier 3 character and read the light. The source names Victoria Midnight's "Character Authority Document" as its authoritative-document example, so we use her as the subject. Check wording is in the [reference](2-reference.md).

> **OPEN:** the source documents no actual gate run for Victoria. This lesson shows the method on a made-up state of her folder, marked as such, not a recorded result.

## Step 1: Open the folder

Open `_AUTHORITATIVE/[IP]/characters/victoria_midnight/`. You expect an authoritative file, a Dramatica ingest and an astrology ingest.

Assume the first two are locked and the astrology ingest says `minimum_viable`. This is the lesson's scenario, not canon.

## Step 2: Run Component 1

Check 1.1 to 1.7 against the authoritative document, in order.

1. 1.1: the file exists.
2. 1.2: the header reads LOCKED with a version number.
3. 1.3: full name, narrative role and primary bond are present.
4. 1.4: MC role, Change resolve and the Problem/Solution pair are present.
5. 1.5: origin context, family architecture and the wound are present.
6. 1.6: behavior under pressure is documented.
7. 1.7: the non-negotiables are listed.

All seven hold, so Component 1 passes. If any failed, you would stop here. Components 2 and 3 cannot pass without it.

## Step 3: Run Component 2

Open the Dramatica ingest. Check 2.1 to 2.9.

1. Both status fields read `locked` (2.2).
2. Sections 1, 2 and 3 are fully populated (2.3 to 2.5).
3. Victoria is the MC, so Section 4 is populated. Section 6 (OS) is populated (2.6).
4. Section 9 holds at least one Touchstone (2.7).
5. Section 10 lists exactly the ten Tier 3 core variables from the integration doc (2.8).
6. The handoff checklist is fully ticked (2.9).

Component 2 passes.

## Step 4: Run Component 3

Open the astrology ingest. Check 3.1 to 3.8.

1. It points at the locked Dramatica ingest (3.2).
2. Seven planets are assigned with justifications (3.3).
3. Three aspects are listed, each with a Dramatica tension source (3.4).
4. Houses, the Chart Summary and the Feed Map are filled (3.5 to 3.7).
5. The status reads `minimum_viable` (3.8).

Every check holds, but 3.8 is minimum-viable. Component 3 is a conditional pass.

## Step 5: Read the light

Components 1 and 2 pass. Component 3 passes at minimum-viable level. That is a yellow light.

## Step 6: Apply the yellow-light constraints

1. Tag the astrology-dependent L1-L11 values `[ASTROLOGY_PENDING]`.
2. Version the slice data block as `draft`.
3. Remember that the Feed Validation Checklist waits for the full chart.

Now proceed to Step 2 (Tier 1 Assignment).

## What you learned

You ran three components in dependency order. You saw that a failure stops the chain at its root. You read a yellow light and its three constraints. Next, see the [how-to](3-how-to.md) for fixing a red light.
