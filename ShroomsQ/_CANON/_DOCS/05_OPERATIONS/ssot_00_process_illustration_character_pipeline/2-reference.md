---
title: "Process Illustration: reference"
type: reference
for: "a narrative designer looking up a flow, step, decision point, or the next action in the character pipeline"
does: "lists every component of the Process Illustration"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_00_process_illustration_character_pipeline.md
source_version: 1.0.1
---

**Who it's for:** a narrative designer looking up a flow, step, decision point, or the next action in the character pipeline · **What it does:** lists every component of the Process Illustration · **Type:** reference

# Process Illustration: reference

The source has type `ssot_00_foundations`, category process_illustration, version 1.0.1, module of `ssot_02_character_systems_vertical_slice`, tier operations, trunk BLACK, last updated 2026-10-04. It applies to OVEREXITOUT, ASTRO7EX, LAKAD. Status: canonical. Its purpose: it "illustrates the complete LEECHSEED character pipeline as four sequential flows with decision points, inputs, outputs, and embedded Mermaid diagrams for Obsidian rendering."

The doc modules per flow:

| Flow | Doc module |
|---|---|
| A | `📐 ssot_02_template_dramatica_ingest.md` and `🔮 ssot_02_dramatica_integration_protocol.md` |
| B | `🔮 ssot_02_character_astrology_dai.md` and `📐 ssot_02_template_astrology_ingest.md` |
| C | `🔮 ssot_02_step_1_source_verification_protocol.md` (the Step 1 gate) |
| D | `🔮 ssot_02_character_state_architecture.md` |

## The Four Flows

| Flow | Name | Input | Output | When |
|---|---|---|---|---|
| **A** | Dramatica Extraction | Locked storyform in Dramatica software | Dramatica Ingest Template (`[CHARACTER_ID]_dramatica_ingest.md`), copied from the blank form | Once per Tier 3 character per storyform |
| **B** | DAI Translation | Locked Dramatica Ingest Template | Character Astrology Ingest Template (`[CHARACTER_ID]_astrology_ingest.md`), `locked` or `minimum_viable` | Once per Tier 3 character |
| **C** | Vertical Slice | Step 1 gate passed: authoritative document plus both ingest templates | 12-Layer Vertical Slice (.md) with a structured data block, every key tagged | Once per character (base record) |
| **D** | State Diffing | Locked base record plus a fabula event | Checkpoint: a state record with `state_diffs` (.md) | Per fabula event per character |

Flows A, B, C run in order for each new Tier 3 character. Flow D runs repeatedly. A revised storyform re-runs parts of all three (see the Cascade). Tier 2 and Tier 1 characters do not use the ingest forms.

## Master Pipeline Overview

The master diagram has six groups:

- **Upstream sources:** Dramatica software (locked storyform) and the authoritative document (character bible).
- **Flow A:** extract reports (Dynamics, Theme, Character) into the Dramatica Ingest Template.
- **Flow B:** the DAI derivation sequence (18 steps) into the Character Astrology Ingest Template.
- **Flow C:** Step 1 source verification gate (PASS or FAIL/BLOCKED), then Step 2 Tier 1 assignment, Step 3 Tier 2 derivation, Step 4 Tier 3 population, Step 5 derived stats, Step 6 flag evaluation, Step 7 structured data block.
- **Flow D:** the structured data block is the base record; a fabula event (`event_id`) and the base record compute a state diff, which yields a checkpoint (.md).
- **Canonical folder:** `_AUTHORITATIVE/IP/characters/CHARACTER_ID/` receives the Dramatica ingest, astrology ingest, structured data block, and checkpoint.

## Flow A: Dramatica → Dramatica Ingest Template

### Overview

The designer extracts structural data from the locked Dramatica storyform and fills the Dramatica Ingest Template. It is a data transfer with sequenced extraction priorities.

### Flow Diagram

The order follows the form's extraction priority: Section 1, then 4, then 3 and 2, then 6, 5 and 7, with Section 8 as the log. The form serves Tier 3 characters only. Steps:

1. Open Dramatica and load the storyform. Check whether it is LOCKED. If not, lock it first; no extraction from drafts.
2. Copy the blank form to the character folder as `CHARACTER_ID_dramatica_ingest.md`. Delete the how-to section and the frontmatter. Keep the section numbers.
3. Fill the Header: `character_id`, `storyform_id`, `storyform_version`, `authoritative_doc_ref`.
4. Extract 1: Story Dynamics Report to Section 1 (outcome, judgement, driver, limit).
5. Extract 2: Theme Report (MC) to Section 4 (the MC throughline variable set).
6. Extract 3: Character Report to Section 3 (the eight element fields and the meaning statement), then Section 2 (structural role, archetype, resolve, growth, approach, mental sex).
7. Choose throughlines. OS (every character) to Section 6; IC to Section 5; RS principal to Section 7.
8. Log Section 8, the Report Source Log: one line per report read, in extraction order.
9. Derive Section 9, Touchstones, from the storyform (minimum 1).
10. Generate Section 10, the L12 Core Block, from Sections 1 to 9, filled last.
11. Run Section 11, the Downstream Handoff Checklist.
12. If all checks pass, set `storyform_status` and `status` to locked and place the file in the canonical folder. If not, find the gaps and return to the relevant extraction step.

### Decision Point Annotations

- **DP-A1: "Is storyform LOCKED?"** A draft storyform can change, which can invalidate the template. Never extract from a draft. This is a hard gate. A storyform revised after the template locks is a new version, and the Cascade applies.
- **DP-A2: "Which throughlines?"** The structural role decides which sections apply. An MC fills Section 4, an IC Section 5, an RS principal Section 7. Every character fills Section 6 (OS). A character with more than one role fills each section the roles call for.
- **DP-A3: "All checks pass?"** The handoff checklist (Section 11) validates completeness. A failed check means the gap is upstream, in the extraction. A field the storyform does not give yet stays empty with `⏸` and the reason. Never guess. The Step 1 gate reads these sections by number (Checks 2.3 to 2.9).

## Flow B: Dramatica Ingest → Character Astrology Ingest (via DAI)

### Overview

The designer translates locked Dramatica data into astrological notation with the 18-step DAI derivation sequence. Each step yields one or more chart assignments. The form is `📐 ssot_02_template_astrology_ingest.md`, copied as `[CHARACTER_ID]_astrology_ingest.md`, for Tier 3 characters only. Every sign carries a one or two sentence derivation: the Dramatica input, the rule, and why the sign fits.

### Flow Diagram

1. Load the locked Dramatica Ingest Template. Copy the blank astrology form and set `dramatica_ingest_ref`.
2. **Step 1, Sun Sign:** Domain, Element, Concern, Modality Grid, Sign. Validate: does the sign encode the identity axis? If not, re-examine the modality assignment (Concern-to-Modality has the most flex).
3. **Step 2, Moon Sign:** Problem, planetary resonance, Response, stress collapse, select sign. Validate: does the sign encode the stress-collapse pattern? If not, reselect.
4. **Step 3, Ascendant:** Approach to Cardinal/Fire or Fixed/Water; Critical Flaw to exploit vector.
5. **Step 4, Mercury:** Unique Ability plus Methodology gives the processing-style sign.
6. **Step 5, Venus:** Concern plus Purpose gives the desire-quality sign.
7. **Step 6, Mars:** Approach plus Motivation gives the action-style sign.
8. **Step 7, Saturn:** Critical Flaw plus Inhibitor gives the limit sign. Decision: seven signs placed (Steps 1 to 7)? Proceed to the full chart, or skip to aspects.
9. **Step 8, Jupiter:** Unique Ability gives the expansion sign.
10. **Step 9, Uranus:** Solution gives the disruption sign.
11. **Step 10, Neptune:** Symptom gives the illusion sign.
12. **Step 11, Pluto:** Outcome plus Judgement gives the terminal sign.
13. **Step 12, Midheaven:** Goal plus OS Role gives the legacy sign.
14. **Step 13, Descendant:** Direction, opposite of the Ascendant.
15. **Step 14, IC:** Benchmark, opposite of the Midheaven.
16. **Step 15, Aspects:** analyze Dramatica tensions and assign logic gates (minimum 3, target 5 to 7).
17. **Step 16, Houses:** Domain gives the emphasis pattern; assign each planet to a house.
18. **Step 17, Dignities:** check each planet's sign against traditional dignities; apply the narrative-first override if needed.
19. **Step 18, 12th House:** assign submerged functions; identify the Hauntology trigger.
20. Write Section 8, the Chart Summary (6 to 10 sentences). Fill Section 9, the 12-Layer Feed Map, and validate each layer feed. Run Section 10, Status and Lock.
21. If all checks pass, set `status` to locked or `minimum_viable` and place the file in the canonical folder. If not, return to the relevant step.

### Decision Point Annotations

- **DP-B1: "Does sign encode identity axis?"** The Sun sign validation gate. Compare the sign's elemental and modal qualities against the character's MC Domain plus Concern. A sign that describes a different kind of person than the Dramatica data is wrong. The common error is misidentifying the Concern's modality, so revisit that step first.
- **DP-B2: "Does sign encode stress-collapse pattern?"** The Moon sign validation gate. The Moon is where the character goes when Sun-level processing fails. A Moon that feels too comfortable, too rational, or too like the Sun is wrong. It should feel like a regression: older, more instinctual.
- **DP-B3: "Minimum Viable Chart complete?"** The minimum viable chart is Sections 1 to 5 and 8 to 10: the Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant signs, at least three aspects, houses for those seven planets, the chart summary and the feed map. Sections 6 and 7 (dignities, the 12th House) can wait. The designer marks the template `minimum_viable`. The Step 1 gate reads that as a yellow light. The full chart is complete before the final Vertical Slice lock.

## Flow C: Both Ingests → 12-Layer Vertical Slice

### Overview

The main production flow. It consumes both locked ingest templates plus the authoritative document and produces the complete 12-layer character record with derived statistics, flags, and a structured data block.

### Flow Diagram

1. **Step 1, Source Verification:** Component 1 (authoritative doc, 7 checks), Component 2 (Dramatica ingest, 9 checks), Component 3 (astrology ingest, 8 checks). Gate result: GREEN proceeds. YELLOW proceeds, with chart-fed values tagged ASTROLOGY_PENDING and the block draft until the chart locks. RED is BLOCKED; see the failure diagnostic in the Step 1 protocol.
2. **Step 2, Tier 1 assignment:** assign T1.CORE, T1.VITAL, T1.SOCIAL. Check that Tier 1 alone suggests the character; if not, the primary values are wrong.
3. **Step 3, Tier 2 derivation:**
   - 3A: derive T2.WILL from T1.CORE, buying up or down on documented resolve.
   - 3B: assign T2.WOUND from character history (even values only, SC-12). It is a record, not a choice.
   - 3C: derive T2.DRIVE from T1.VITAL. Ambition-driven: DRIVE = VITAL. Meaning-driven: DRIVE < VITAL.
   - 3D: check `want_need.need` is not empty (Tier 2 and 3).
4. **Step 4, Tier 3 population** (L7 to L12 variable stacks): mark [INFERRED] where the source is silent; cite `setting_ref` where the setting has an S4, S6 or S8 entry.
   - 4A: L7 ORIGIN (authoritative doc plus AST.ANGLE.ic_sign).
   - 4B: L8 IMPRINT (authoritative doc plus AST.PERSONAL.moon_sign).
   - 4C: L9 EROS (authoritative doc plus AST Venus/Mars data); mark INFERRED if needed.
   - 4D: L10 SHADOW (authoritative doc plus AST 12th House and debilities); `shadow_density` even only; `projection_tendency` a multiple of 3.
   - 4E: L11 DESTINY (authoritative doc plus AST Jupiter/Uranus/MC); `resistance_index` even only.
   - 4F: L12 FUNCTION, direct from the Dramatica Ingest Section 10 L12 Core Block plus the Extended sub-table.
5. **Step 5, Derived stats:** compute all 7 in internal (0 to 60) space, including Expressive Range. Examples: `DRV.stress_threshold = WILL_i - WOUND_i` (may be negative); `DRV.truth_exposure_index = SOCIAL_i + (12 - shame_d) x 5` (uncapped). Read TEI and Collapse Risk first. If the stats feel wrong, investigate the layer values and return to Step 2.
6. **Step 6, Flag evaluation:** evaluate each trigger against computed values. An unexpected flag signals a schema inconsistency; investigate the contributing values and return to Step 4.
7. **Step 7, Structured data block:** generate a machine-readable YAML block with all values, derived stats, and flag states. Every key carries a tag: Static, Dynamic or Derived. Unfilled fields stay null with `⏸` and the reason.
8. Run the Feed Validation Checklist (15 items from the Astrology to 12-Layer Mapping). If all pass, lock the Vertical Slice and place it in the canonical folder. If not, resolve the inconsistency per the Conflict Resolution Protocol.

### Decision Point Annotations

- **DP-C1: "Gate Result?"** Component 1 has seven checks, Component 2 nine, Component 3 eight. Green means all pass. Yellow means Components 1 and 2 pass and Component 3 is at minimum_viable; chart-fed values carry `[ASTROLOGY_PENDING]` and the block stays draft until the chart locks and the Feed Validation Checklist passes. Red means any component fails and is a hard block. The designer completes the missing upstream document.
- **DP-C2: "Tier 1 alone suggests the character?"** Three numbers (CORE, VITAL, SOCIAL) must produce a recognizable human outline without any other layer. The source's example: CORE=13, VITAL=14, SOCIAL=10 should read as "smart, physically elite, socially unfiltered." This gate prevents downstream waste, since every later layer builds on Tier 1.
- **DP-C3: "Stats feel right?"** Derived statistics are diagnostic instruments. A positive Stress Threshold for a character who operates past their limit, or a low Truth Exposure Index for a maximally legible character, means something is wrong upstream. The stats expose numeric assignment errors.
- **DP-C4: "Any flags fire unexpectedly?"** A flag that fires when it should not, or fails to fire when it should, indicates a schema inconsistency between the trigger condition and the layer values. The designer does not adjust the flag; the flag correctly evaluates the numbers given.
- **DP-C5: "Does every key carry a tag?"** No field ships without a tag. Static or dynamic follows the state architecture's Decision Test: would the value differ if the character froze at two points in the narrative? Derived values are recomputed from layer values and never stored as a diff. The tag table is in the slice, under "Field tags · every field".

## Flow D: Vertical Slice → State Diffs

### Overview

Flow D produces state records that describe how a character differs from the base record at specific story points. A full state record is a checkpoint: a complete state at a fabula event. State diffs overlay the base record and never modify it. Single-field changes between events are story points. They live in the tracking system, section 5 (`📐 ssot_08_tracking_system.md`), not in a checkpoint. The method is in the state architecture.

### Flow Diagram

1. A fabula event occurs (`event_id`). Identify the affected character and load the locked base record (the Vertical Slice structured data block).
2. Decide: whole state at a fabula event, or one field between events? One field is a story point (tracking system section 5), not a checkpoint.
3. For a whole state, pick the event type and its signature:
   - **Trauma:** high-impact sudden event. WOUND increases, new `shadow_content`, flags may fire, DRIVE may drop, attachment may change.
   - **Systemic Pressure:** sustained institutional force. WILL_EFFECTIVE decreases, SHADOW projection increases, `resistance_index` may decrease.
   - **Relational:** bond forms, breaks, or transforms. IMPRINT variables change, EROS may shift, create or update a relationship record.
   - **Awakening:** perception breakthrough. `resistance_index` drops sharply, shadow may begin integrating, PENDING flags may fire.
   - **Progression:** slow internal change. Progressed Moon shifts, emotional baseline drifts, attachment score may drift by 1.
4. Create the checkpoint: (1) set required fields (`character_id`, `state_id`, `origin_event` = the fabula `event_id`, `told_at` time codes, `base_record_version`); (2) list MODIFIED_VALUES under `state_diffs`, Dynamic fields only, only values that differ from base; (3) recompute MODIFIED_DERIVED; (4) re-evaluate MODIFIED_FLAGS; (5) write STATE_NOTE (2 to 5 sentences of justification); (6) add ASTROLOGY_OVERLAY if transits or progressions are active.
5. Check that modified values respect scale class constraints; if not, adjust to the nearest valid grid value. Check that flags re-evaluate correctly; if not, investigate the values.
6. Save the state record (.md) in the character's `states/` subfolder.
7. If the event affects a relationship, update the relationship record's status and `state_history` in `_AUTHORITATIVE/IP/relationships/`.

### Decision Point Annotations

- **DP-D1: "What type of narrative event?"** The five categories come from the Character State Architecture SSOT. Each has a characteristic signature in the diff. A trauma diff with no WOUND change means something is missing.
- **DP-D2: "Modified values respect scale class constraints?"** Every modified value lands on a valid point in its scale class. WOUND is even on SC-12. `projection_tendency` is a multiple of 3 on SC-12. `resistance_index` is even. The designer rounds to the nearest valid value and documents the direction.
- **DP-D3: "Does this event affect a relationship?"** State diffs and relationship records are separate structures that often change at the same moment. The source's example: Victoria's crash killing Jebb. The state diff records the WOUND increase and attachment change, and the relationship record changes status from `active` to `severed`. Both update together.
- **DP-D4: "Whole state or one field?"** A checkpoint re-derives every value, derived statistic, and flag, a weight that fits a fabula event. A single trait tick or flag flip between events is a story point in the tracking system.
- **DP-D5: "Is the field Dynamic?"** Only fields the slice tags Dynamic appear in `MODIFIED_VALUES`. A Static field never changes; a revision makes a new base record. Derived values are recomputed, never stored as a diff.

## Cascade: A Revised Storyform

A revised storyform is a new version, not an edit. The chart, the L12 block, and the state diffs hang off the old version. The method is in the integration protocol, section "Cascade on a Revised Storyform". The cascade has three steps:

| Step | Flow re-entered | What the narrative designer does |
|---|---|---|
| 1 | A, then B | Fills a new Dramatica Ingest from the new storyform and passes the Step 1 gate on it. Re-runs the DAI sequence. The new chart gets its own file, stamped to the new storyform version. The old chart stays on file, marked superseded. |
| 2 | C (Steps 5 and 6) | Re-extracts the L12 core block and the L12_DRAMATICA_EXTENDED sub-table from the new ingest. Re-runs the derived statistics and flags, because they read L12. The result is a new base record version. |
| 3 | D | Reads each state diff against the new base. Every value a diff names as "was ..." must match the new base. A diff that no longer matches is revised or retired, and the change is logged. A diff never edits the base. |

## Cross-Flow: Module Attachment

This section covers field modules (Layer-Locked Modules). A doc module, such as the Step 1 gate or the state architecture, is a step inside Flows A to D and is not activated here (see `📐 ssot_00_module_architecture.md`). Field modules attach at any point after the base record exists. They do not take part in Flows A to C. They activate during or after Flow C and persist through Flow D.

### Module Activation Flow

1. The base record exists (Vertical Slice complete). Select a module from the Module Registry.
2. Check that the module's attachment points are valid for the character's tier. If not, promote the character's tier or pick another module.
3. Initialize module variables to defaults or UNASSIGNED.
4. Populate module variables from the authoritative doc or authored content.
5. If the module has dependencies, check they are installed; if not, install them first, then populate again.
6. If the module has derived stats, compute them in internal (0 to 60) space.
7. If the module has flags, evaluate the trigger conditions.
8. Save module data as a sub-table block in the character record.
9. If module variables change during state diffs, the dynamic ones appear in state diffs under the `MOD.[CODE]` namespace. Otherwise they are static and live only in the base record.

### Module Data in State Diffs

When a narrative event changes a module's variables, the state diff includes the module namespace:

```yaml
MODIFIED_VALUES:
  T2.WOUND.wound_score: 10
  MOD.COPING.effectiveness: 4
  MOD.DECOMP.visibility: 8

MODIFIED_MOD_FLAGS:
  MOD.COPING.FLG.coping_failure: ACTIVE
  MOD.DECOMP.FLG.decompensation_risk: ACTIVE
```

Module flags are re-evaluated alongside core flags during state diff creation.

## Appendix: Quick Reference — "What Do I Do Next?"

| You have | You need | Execute |
|---|---|---|
| Locked storyform, no ingest | Dramatica Ingest Template | Flow A |
| Locked Dramatica Ingest, no chart | Character Astrology Ingest | Flow B |
| Both ingests locked, no Vertical Slice | 12-Layer base record | Flow C |
| Locked base record, narrative event occurred | State diff for that moment | Flow D |
| Locked base record, want to attach a field module (DUALISM is the only active one) | Module activation | Cross-Flow |
| Nothing locked | Character authoritative document | Write the character bible first. Everything starts there. |
| Authoritative doc exists but no Dramatica storyform | Storyform | Open Dramatica. Build the storyform. Lock it. Then Flow A. |
| Vertical Slice complete but derived stats feel wrong | Corrected layer values | Re-enter Flow C at Step 2 or Step 4. Fix the inputs, not the outputs. |
| Flag fires unexpectedly | Corrected layer values | Re-enter Flow C at Step 4. The flag is right. The inputs are wrong. |
| Character needs to exist at two narrative moments | Two checkpoints | Run Flow D twice, once per fabula event. Both diff against the base record, not against each other. |
| A checkpoint falls earlier than the base record's own narrative position | A backward diff | Flow D with Rule 7 of the state architecture. Each field is modified to its earlier value. Nothing is deleted. |
| One trait or flag changes between two fabula events | A story point | Write it in the tracking system, section 5. Do not build a checkpoint. |
| Storyform revised after the ingests locked | New chart, new base record version, re-checked diffs | The Cascade section. |
