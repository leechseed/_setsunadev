---
title: "Process Illustration: how-to"
type: how-to
for: "a narrative designer running one step of the character pipeline"
does: "gives the steps for each pipeline task, from Dramatica extraction to state diffs and cascades"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_00_process_illustration_character_pipeline.md
source_version: 1.1.0
---

**Who it's for:** a narrative designer running one step of the character pipeline · **What it does:** gives the steps for each pipeline task, from Dramatica extraction to state diffs and cascades · **Type:** how-to

# Process Illustration: how-to

## Extract a Dramatica Ingest (Flow A)

1. Open Dramatica and load the storyform. Confirm it is LOCKED. If not, lock it first.
2. Copy the blank form to the character folder as `CHARACTER_ID_dramatica_ingest.md`. Delete the how-to section and the frontmatter. Keep the section numbers.
3. Fill the Header: `character_id`, `storyform_id`, `storyform_version`, `authoritative_doc_ref`.
4. Extract the Story Dynamics Report into Section 1.
5. Extract the Theme Report (MC) into Section 4.
6. Extract the Character Report into Section 3, then Section 2.
7. Fill the throughline sections the character's roles call for. Fill OS to Section 6 (every character), IC to Section 5, and RS principal to Section 7.
8. Log each report you read in Section 8, one line each, in order.
9. Derive Section 9, Touchstones, with at least one.
10. Generate Section 10, the L12 Core Block, last.
11. Run the Section 11 checklist. If a check fails, return to the extraction step. Leave an unknown field empty with `⏸` and the reason.
12. Set `storyform_status` and `status` to locked and file it in the canonical folder.

## Translate to a Character Astrology Ingest (Flow B)

1. Load the locked Dramatica Ingest. Copy the blank astrology form as `[CHARACTER_ID]_astrology_ingest.md` and set `dramatica_ingest_ref`.
2. Place the Sun, then check that the sign encodes the identity axis. If not, revisit the modality assignment.
3. Place the Moon, then check that it reads as an instinctual regression. If not, reselect.
4. Place the Ascendant, Mercury, Venus, Mars, and Saturn (Steps 3 to 7).
5. Decide: continue to the full chart or skip to aspects.
6. For the full chart, place Jupiter, Uranus, Neptune, Pluto, Midheaven, Descendant, and IC (Steps 8 to 14).
7. Assign aspects (minimum 3, target 5 to 7), houses, dignities, and the 12th House (Steps 15 to 18).
8. Write the Chart Summary (6 to 10 sentences), fill the LEECHSEED Feed Map, and run Status and Lock.
9. Write one or two sentences of derivation for every sign: the Dramatica input, the rule, and why the sign fits.

## Mark a minimum viable chart

1. Complete Sections 1 to 5 and 8 to 10. Include the seven signs, at least three aspects, houses for the seven planets, the summary, and the feed map.
2. Set the template status to `minimum_viable`.
3. Plan to complete the full chart before the final Vertical Slice lock.

## Build the Vertical Slice (Flow C)

1. Run the Step 1 gate. It makes seven checks on the authoritative document, nine on the Dramatica ingest, and eight on the astrology ingest.
2. On GREEN, proceed. On YELLOW, proceed and tag chart-fed values `ASTROLOGY_PENDING`. On RED, stop and complete the missing document.
3. Assign T1.CORE, T1.VITAL, T1.SOCIAL. Check that the three numbers alone suggest the character.
4. Derive T2.WILL, T2.WOUND (even values only), and T2.DRIVE. Check that `want_need.need` is not empty.
5. Populate L7 to L12. Mark [INFERRED] where the source is silent. Cite `setting_ref` where the setting has an S4, S6, or S8 entry.
6. Compute the 7 derived stats in internal (0 to 60) space. Read TEI and Collapse Risk first.
7. Evaluate the flags.
8. Generate the structured data block. Tag every key Static, Dynamic, or Derived. Leave unfilled fields null with `⏸` and the reason.
9. Run the Feed Validation Checklist (15 items). Lock the slice and file it.

## Fix stats or flags that feel wrong

1. Do not change the stat or the flag. The source says to fix the inputs.
2. For wrong stats, re-enter Flow C at Step 2 or Step 4 and check the layer values.
3. For an unexpected flag, re-enter at Step 4.

## Record a checkpoint (Flow D)

1. Identify the character and load the locked base record.
2. Decide whole state or one field. If it is one field between events, write a story point in the tracking system, section 5, and stop.
3. Pick the event type: Trauma, Systemic Pressure, Relational, Awakening, or Progression.
4. Set the required fields: `character_id`, `state_id`, `origin_event`, `told_at`, `base_record_version`.
5. List only Dynamic fields that differ from base under `state_diffs`.
6. Recompute derived values and re-evaluate flags.
7. Write the STATE_NOTE (2 to 5 sentences). Add ASTROLOGY_OVERLAY if transits or progressions are active.
8. Check every modified value sits on its scale class grid. Round to the nearest valid value and document the direction.
9. Save to the character's `states/` subfolder.
10. If the event affects a relationship, update the relationship record's status and `state_history` too.
11. If the event changes a place, check the setting state. Write or revise the place checkpoint that shares the same `origin_event`.

## Handle a revised storyform (Cascade)

1. Fill a new Dramatica Ingest from the new storyform and pass the Step 1 gate.
2. Re-run the DAI sequence into a new chart file, stamped to the new storyform version. Mark the old chart superseded.
3. Re-extract the L12 core block and the L12_DRAMATICA_EXTENDED sub-table. Re-run derived stats and flags. Save a new base record version.
4. Check every state diff against the new base. Revise or retire any diff whose "was ..." values no longer match, and log the change.

## Attach a field module

1. Confirm the base record exists.
2. Select the module from the Module Registry.
3. Confirm the module's attachment points are valid for the character's tier.
4. Initialize the module's variables to defaults or UNASSIGNED.
5. Populate them. Install any dependency modules first.
6. Compute derived stats and evaluate flags if the module has them.
7. Save the module data as a sub-table block in the character record.
8. Put dynamic module variables in state diffs under `MOD.[CODE]`.

## Find the next action

1. Open the Quick Reference table in the reference.
2. Find the row that matches what you hold.
3. Run the flow in its Execute column.
