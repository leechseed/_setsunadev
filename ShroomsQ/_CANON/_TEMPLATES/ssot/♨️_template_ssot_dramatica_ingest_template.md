---
## type: ingest_template category: dramatica version: 1.0.0 last_updated: 2026-03-02 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Canonical intake form for Dramatica storyform data per Tier 3 character. Completion of this template is required before a Vertical Slice can proceed past Step 1 Source Verification." dependencies: ["ssot_02_character_dramatica_integration"]
---
# ♨️ Dramatica Ingest Template

> **Usage:** Copy this template into the character's canonical folder. Fill all fields from the locked Dramatica storyform. Fields marked `[FROM_STORYFORM]` must be extracted from Dramatica reports. Fields marked `[AUTHORED]` are written by the narrative designer based on the storyform data. Fields marked `[IF_APPLICABLE]` are filled only when the character holds the relevant throughline role.
> 
> **Lock Condition:** This document is locked when all `[FROM_STORYFORM]` fields are populated and the narrative designer has signed off on all `[AUTHORED]` fields. Once locked, changes require a new version number and a documented reason.

---

## Header

|Field|Value|
|---|---|
|`character_id`|`[CHARACTER_ID]`|
|`character_name`|`[FULL_NAME]`|
|`ip`|`[IP_NAME]`|
|`storyform_id`|`[STORYFORM_ID]`|
|`storyform_version`|`[VERSION]`|
|`storyform_status`|`locked` / `draft`|
|`template_version`|`1.0.0`|
|`template_status`|`locked` / `draft`|
|`completed_by`|`[NAME_OR_HANDLE]`|
|`completion_date`|`[YYYY-MM-DD]`|

---

## Section 1: Storyform Dynamics

These values are story-global. They apply to every character in this storyform. Extract from the **Story Dynamics Report**.

|Variable|Value|Source|
|---|---|---|
|`story_outcome`|`[FROM_STORYFORM]`|Success / Failure|
|`story_judgement`|`[FROM_STORYFORM]`|Good / Bad|
|`story_driver`|`[FROM_STORYFORM]`|Action / Decision|
|`story_limit`|`[FROM_STORYFORM]`|Timelock / Optionlock|
|`story_goal`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_consequence`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_cost`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_dividend`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_forewarnings`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_prerequisites`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_preconditions`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|
|`story_requirements`|`[FROM_STORYFORM]`|_(Dramatica concern element)_|

---

## Section 2: Character Structural Role

These values define the character's mechanical position in the storyform. Extract from the **Character Report** and **Story Dynamics Report**.

|Variable|Value|Source|
|---|---|---|
|`structural_role`|`[FROM_STORYFORM]`|mc / ic / mc_protagonist / ic_antagonist / os_only / etc.|
|`dramatica_archetype`|`[FROM_STORYFORM]`|Protagonist / Antagonist / Guardian / Contagonist / Reason / Emotion / Sidekick / Skeptic / Complex|
|`resolve`|`[FROM_STORYFORM]`|Change / Steadfast|
|`growth`|`[FROM_STORYFORM]`|Start / Stop|
|`approach`|`[FROM_STORYFORM]`|Do-er / Be-er|
|`mental_sex`|`[FROM_STORYFORM]`|Male / Female _(Dramatica's term for problem-solving style)_|

---

## Section 3: Character Element Quads

The four element sets that define this character's behavioral mechanics. Extract from the **Character Report**.

### Motivation

|Element|Value|
|---|---|
|`motivation_primary`|`[FROM_STORYFORM]`|
|`motivation_secondary`|`[FROM_STORYFORM]`|

### Methodology

|Element|Value|
|---|---|
|`methodology_primary`|`[FROM_STORYFORM]`|
|`methodology_secondary`|`[FROM_STORYFORM]`|

### Evaluation

|Element|Value|
|---|---|
|`evaluation_primary`|`[FROM_STORYFORM]`|
|`evaluation_secondary`|`[FROM_STORYFORM]`|

### Purpose

|Element|Value|
|---|---|
|`purpose_primary`|`[FROM_STORYFORM]`|
|`purpose_secondary`|`[FROM_STORYFORM]`|

**Structural meaning statement** `[AUTHORED]`:

> _[One to three sentences explaining what these element combinations mean for how this character operates. Written by the narrative designer. Example: "Tori acts once convinced, moves early rather than late, evaluates based on tangible outcomes, and seeks to understand what is really happening beneath appearances."]_

---

## Section 4: MC Throughline [IF_APPLICABLE]

Complete this section only if the character holds the MC role. Extract from the **Theme Report (MC Throughline)**.

|Variable|Value|
|---|---|
|`mc_domain`|`[FROM_STORYFORM]`|
|`mc_concern`|`[FROM_STORYFORM]`|
|`mc_issue`|`[FROM_STORYFORM]`|
|`mc_counterpoint`|`[FROM_STORYFORM]`|
|`mc_thematic_conflict`|`[FROM_STORYFORM]`|
|`mc_problem`|`[FROM_STORYFORM]`|
|`mc_solution`|`[FROM_STORYFORM]`|
|`mc_symptom`|`[FROM_STORYFORM]`|
|`mc_response`|`[FROM_STORYFORM]`|
|`mc_unique_ability`|`[FROM_STORYFORM]`|
|`mc_critical_flaw`|`[FROM_STORYFORM]`|
|`mc_benchmark`|`[FROM_STORYFORM]`|
|`mc_focus`|`[FROM_STORYFORM]`|
|`mc_direction`|`[FROM_STORYFORM]`|

**MC signposts** (ordered sequence):

|Signpost|Value|
|---|---|
|`mc_signpost_1`|`[FROM_STORYFORM]`|
|`mc_signpost_2`|`[FROM_STORYFORM]`|
|`mc_signpost_3`|`[FROM_STORYFORM]`|
|`mc_signpost_4`|`[FROM_STORYFORM]`|

---

## Section 5: IC Throughline [IF_APPLICABLE]

Complete this section only if the character holds the IC role. Extract from the **Theme Report (IC Throughline)**.

|Variable|Value|
|---|---|
|`ic_domain`|`[FROM_STORYFORM]`|
|`ic_concern`|`[FROM_STORYFORM]`|
|`ic_issue`|`[FROM_STORYFORM]`|
|`ic_counterpoint`|`[FROM_STORYFORM]`|
|`ic_problem`|`[FROM_STORYFORM]`|
|`ic_solution`|`[FROM_STORYFORM]`|
|`ic_symptom`|`[FROM_STORYFORM]`|
|`ic_response`|`[FROM_STORYFORM]`|
|`ic_unique_ability`|`[FROM_STORYFORM]`|
|`ic_critical_flaw`|`[FROM_STORYFORM]`|
|`ic_benchmark`|`[FROM_STORYFORM]`|
|`ic_focus`|`[FROM_STORYFORM]`|
|`ic_direction`|`[FROM_STORYFORM]`|

**IC signposts** (ordered sequence):

|Signpost|Value|
|---|---|
|`ic_signpost_1`|`[FROM_STORYFORM]`|
|`ic_signpost_2`|`[FROM_STORYFORM]`|
|`ic_signpost_3`|`[FROM_STORYFORM]`|
|`ic_signpost_4`|`[FROM_STORYFORM]`|

---

## Section 6: OS Throughline

Every Tier 3 character participates in the Overall Story. Extract from the **Theme Report (OS Throughline)**.

|Variable|Value|
|---|---|
|`os_domain`|`[FROM_STORYFORM]`|
|`os_concern`|`[FROM_STORYFORM]`|
|`os_issue`|`[FROM_STORYFORM]`|
|`os_counterpoint`|`[FROM_STORYFORM]`|
|`os_problem`|`[FROM_STORYFORM]`|
|`os_solution`|`[FROM_STORYFORM]`|
|`os_symptom`|`[FROM_STORYFORM]`|
|`os_response`|`[FROM_STORYFORM]`|
|`os_catalyst`|`[FROM_STORYFORM]`|
|`os_inhibitor`|`[FROM_STORYFORM]`|
|`os_benchmark`|`[FROM_STORYFORM]`|

**OS signposts** (ordered sequence):

|Signpost|Value|
|---|---|
|`os_signpost_1`|`[FROM_STORYFORM]`|
|`os_signpost_2`|`[FROM_STORYFORM]`|
|`os_signpost_3`|`[FROM_STORYFORM]`|
|`os_signpost_4`|`[FROM_STORYFORM]`|

---

## Section 7: RS Throughline [IF_APPLICABLE]

Complete this section only if the character is one of the two principals in the Relationship Story. Extract from the **Theme Report (RS Throughline)**.

|Variable|Value|
|---|---|
|`rs_domain`|`[FROM_STORYFORM]`|
|`rs_concern`|`[FROM_STORYFORM]`|
|`rs_issue`|`[FROM_STORYFORM]`|
|`rs_counterpoint`|`[FROM_STORYFORM]`|
|`rs_problem`|`[FROM_STORYFORM]`|
|`rs_solution`|`[FROM_STORYFORM]`|
|`rs_catalyst`|`[FROM_STORYFORM]`|
|`rs_inhibitor`|`[FROM_STORYFORM]`|
|`rs_benchmark`|`[FROM_STORYFORM]`|

**RS signposts** (ordered sequence):

|Signpost|Value|
|---|---|
|`rs_signpost_1`|`[FROM_STORYFORM]`|
|`rs_signpost_2`|`[FROM_STORYFORM]`|
|`rs_signpost_3`|`[FROM_STORYFORM]`|
|`rs_signpost_4`|`[FROM_STORYFORM]`|

**RS partner character:** `[CHARACTER_ID of the other principal]`

---

## Section 8: Character Relationships (OS Level)

List all Dramatica-defined relationships between this character and other characters in the storyform. Extract from the **Character Relationships Report**.

|Partner Character|Relationship Dynamic|Dynamic Type|Notes|
|---|---|---|---|
|`[CHARACTER_ID]`|`[FROM_STORYFORM]`|`[dynamic_pair / companion / dependent / etc.]`|`[AUTHORED]`|
|`[CHARACTER_ID]`|`[FROM_STORYFORM]`|`[type]`|`[AUTHORED]`|

_(Add rows as needed)_

---

## Section 9: Narrative Invariants [AUTHORED]

Narrative invariants are structural laws derived from the storyform that cannot be violated during story development. They are authored by the narrative designer based on the storyform data, not extracted from Dramatica directly.

|Invariant ID|Statement|Derived From|
|---|---|---|
|`[ID]`|`[Invariant statement]`|`[Which storyform elements produce this constraint]`|
|`[ID]`|`[Invariant statement]`|`[Source elements]`|

_(Add rows as needed)_

**Example:**

|Invariant ID|Statement|Derived From|
|---|---|---|
|`cost_and_meaning`|Victoria finds meaning in systemic defeat because her internal architecture survives the external collapse.|`story_outcome: Failure` + `story_judgement: Good` + `resolve: Change`|

---

## Section 10: L12 Core Block (Auto-Generated)

This section is populated automatically from the data above. It represents the variables that enter the L12 FUNCTION core in the 12-Layer Vertical Slice.

```
L12_FUNCTION:
  dramatica_archetype: [FROM Section 2]
  motivation_element: [FROM Section 3 — motivation_primary]
  methodology_element: [FROM Section 3 — methodology_primary]
  evaluation_element: [FROM Section 3 — evaluation_primary]
  purpose_element: [FROM Section 3 — purpose_primary]
  narrative_invariant: [FROM Section 9 — primary invariant ID]
  story_outcome: [FROM Section 1]
  story_judgement: [FROM Section 1]
  limit_type: [FROM Section 1 — Timelock or Optionlock]
  resolve: [FROM Section 2]
```

---

## Section 11: Downstream Handoff Checklist

Before locking this template, confirm:

- [ ] All `[FROM_STORYFORM]` fields are populated from Dramatica reports
- [ ] All `[AUTHORED]` fields are completed by the narrative designer
- [ ] Structural meaning statement (Section 3) is written
- [ ] Narrative invariants (Section 9) are defined
- [ ] L12 Core Block (Section 10) matches the data in preceding sections
- [ ] Character Astrology can proceed — the DAI translation table has sufficient inputs from this template
- [ ] Template status changed to `locked`
- [ ] Template placed in character's canonical folder: `_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/`

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-02|Initial template. Covers storyform dynamics, structural role, element quads, all four throughlines, relationships, narrative invariants, L12 core block generation, and downstream handoff checklist.|