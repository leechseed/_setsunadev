---

## type: ingest_template category: dramatica version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT] status: draft purpose: "Dramatica Ingest for Victoria Midnight. Phase 4 validation run." dependencies: ["ssot_02_character_dramatica_integration"]
---
# 📐 Dramatica Ingest — Victoria "Tori" Midnight

## Header

|Field|Value|
|---|---|
|character_id|victoria_midnight|
|character_name|Victoria "Tori" Midnight|
|ip|overexitout|
|storyform_id|oxo_primary_v1|
|storyform_version|1.0|
|storyform_status|locked|
|template_version|1.0.0|
|template_status|**draft**|
|completed_by|LEECHSEED / Phase 4 Validation|
|completion_date|2026-03-03|



## Section 1: Storyform Dynamics

|Variable|Value|Source|
|---|---|---|
|story_outcome|Failure|From Vertical Slice L12|
|story_judgement|Good|From Vertical Slice L12|
|story_driver|**[MISSING — requires storyform extraction]**|Action / Decision|
|story_limit|Optionlock|From Vertical Slice L12|
|story_goal|**[MISSING — requires storyform extraction]**||
|story_consequence|**[MISSING — requires storyform extraction]**||
|story_cost|**[MISSING — requires storyform extraction]**||
|story_dividend|**[MISSING — requires storyform extraction]**||
|story_forewarnings|**[MISSING — requires storyform extraction]**||
|story_prerequisites|**[MISSING — requires storyform extraction]**||
|story_preconditions|**[MISSING — requires storyform extraction]**||
|story_requirements|**[MISSING — requires storyform extraction]**||

**STATUS: PARTIAL — 3 of 12 fields populated. Remaining 9 require direct storyform extraction.**

---

## Section 2: Character Structural Role

|Variable|Value|Source|
|---|---|---|
|structural_role|mc_protagonist|Authoritative doc Section 1|
|dramatica_archetype|Protagonist|Authoritative doc Section 1|
|resolve|Change|Authoritative doc Section 1|
|growth|**[MISSING — requires storyform]**|Start / Stop|
|approach|Do-er|Inferred from Behavior Under Pressure: "Acts through certainty, not consensus. Moves early. Converts fear into action."|
|mental_sex|**[MISSING — requires storyform]**|Male / Female|

**STATUS: PARTIAL — 4 of 6 fields populated. growth and mental_sex require storyform.**

---

## Section 3: Character Element Quads

### Motivation

|Element|Value|
|---|---|
|motivation_primary|Consider|
|motivation_secondary|Pursuit|

### Methodology

|Element|Value|
|---|---|
|methodology_primary|Certainty|
|methodology_secondary|Proaction|

### Evaluation

|Element|Value|
|---|---|
|evaluation_primary|Proven|
|evaluation_secondary|Effect|

### Purpose

|Element|Value|
|---|---|
|purpose_primary|Knowledge|
|purpose_secondary|Actuality|

**Structural meaning statement** [AUTHORED]:

> Tori acts once convinced, moves early rather than late, evaluates based on tangible outcomes, and seeks to understand what is really happening beneath appearances.

_Source: Authoritative document Section 2 — transcribed verbatim as this statement is canonical._

**STATUS: COMPLETE — all 8 elements + structural meaning populated.**

---

## Section 4: MC Throughline

|Variable|Value|
|---|---|
|mc_domain|Situation|
|mc_concern|**[MISSING — requires storyform. Authoritative doc does not name it directly. MC Issue = Interdiction suggests the Concern is in the Situation/Present or Situation/Circumstances family. Interdiction lives under the Concern of "The Present" in Dramatica's structural model.]**|
|mc_issue|Interdiction|
|mc_counterpoint|**[MISSING — requires storyform]**|
|mc_thematic_conflict|**[MISSING — requires storyform]**|
|mc_problem|Equity|
|mc_solution|Inequity|
|mc_symptom|**[MISSING — requires storyform. The Focus = Desire suggests the Symptom may align with Desire or a related element.]**|
|mc_response|**[MISSING — requires storyform. The Direction = Ability suggests the Response may align with Ability or a related element.]**|
|mc_unique_ability|Destiny|
|mc_critical_flaw|Truth|
|mc_benchmark|**[MISSING — requires storyform]**|
|mc_focus|Desire|
|mc_direction|Ability|

**MC signposts:**

|Signpost|Value|
|---|---|
|mc_signpost_1|**[MISSING]**|
|mc_signpost_2|**[MISSING]**|
|mc_signpost_3|**[MISSING]**|
|mc_signpost_4|**[MISSING]**|

**STATUS: PARTIAL — 9 of 17 fields populated. mc_concern, mc_counterpoint, mc_thematic_conflict, mc_symptom, mc_response, mc_benchmark, and all 4 signposts require storyform extraction.**

**CRITICAL NOTE ON MC FOCUS/DIRECTION vs MC SYMPTOM/RESPONSE:** In Dramatica, Focus and Direction are the MC's perceived view of their problem. Symptom and Response are the broader story-level equivalent. The authoritative document lists Focus = Desire, Direction = Ability. These may or may not be identical to Symptom/Response depending on the storyform configuration. The storyform must be consulted to confirm.

---

## Section 5: IC Throughline

**[ENTIRE SECTION MISSING — The authoritative document does not identify the Impact Character or their throughline. Requires storyform extraction. The IC is likely a character who represents Steadfast conviction against Victoria's Change arc, but no candidate is named in the current documentation.]**

**STATUS: EMPTY — 0 of 17 fields populated.**

---

## Section 6: OS Throughline

**[ENTIRE SECTION MISSING — The authoritative document references the "system" as antagonist force and "procedural enforcement" as the conflict domain, but does not name OS Domain, Concern, Issue, or any OS throughline variables. Requires storyform extraction.]**

**STATUS: EMPTY — 0 of 15 fields populated.**

---

## Section 7: RS Throughline

**[ENTIRE SECTION MISSING — The authoritative document identifies Jebb Midnight as primary bond but does not map the Relationship Story throughline. RS Domain, Concern, and all RS variables require storyform extraction. The RS partner is likely Jebb (pre-crash) or a post-crash relational principal (TBD).]**

**STATUS: EMPTY — 0 of 14 fields populated.**

---

## Section 8: Character Relationships (OS Level)

|Partner Character|Relationship Dynamic|Dynamic Type|Notes|
|---|---|---|---|
|jebb_midnight|Sibling bond — navigator/driver, stabilizing attachment, pace-notes as love-embedded-procedure|companion|Pre-crash primary bond. Death at M1B is punitive removal by the system.|
|the_system|Institutional antagonist — procedural enforcement, legibility control, acquisition protocol|antagonist_force|Not a character but a systemic presence. Dramatica may encode this as the OS Antagonist archetype distributed across institutional agents.|

**STATUS: PARTIAL — Core relationships identified but Dramatica-level dynamic typing requires storyform character relationship data.**

---

## Section 9: Narrative Invariants

|Invariant ID|Statement|Derived From|
|---|---|---|
|cost_and_meaning|Victoria finds meaning in systemic defeat because her internal architecture survives the external collapse.|story_outcome: Failure + story_judgement: Good + resolve: Change|
|truth_is_exploit|When she speaks truth, it desyncs her hardware and triggers systemic response. Truth is not her virtue — it is her exploit vector.|mc_critical_flaw: Truth + mc_unique_ability: Destiny|
|merit_to_control|The arc moves from "merit earns freedom" through "visibility invites ownership" to "control is the only form of safety left." The meritocratic premise must collapse before the Change can land.|mc_problem: Equity + resolve: Change|
|optionlock_not_timelock|Exits close because of who she is, not because a clock runs out. Each non-negotiable (Section 7) corresponds to one option class closing permanently.|story_limit: Optionlock + non-negotiables|

**STATUS: COMPLETE — 4 invariants defined with derivation sources.**

---

## Section 10: L12 Core Block (Auto-Generated)

```
L12_FUNCTION:
  dramatica_archetype: Protagonist
  motivation_element: Consider
  methodology_element: Certainty
  evaluation_element: Proven
  purpose_element: Knowledge
  narrative_invariant: cost_and_meaning
  story_outcome: Failure
  story_judgement: Good
  limit_type: Optionlock
  resolve: Change
```

**CROSS-VALIDATION NOTE:** The existing Vertical Slice L12 block uses different primary elements:

- Vertical Slice has motivation_element: Equity (the MC Problem)
- This template has motivation_element: Consider (the Motivation quad primary)

This is a **schema clarification issue**, not a data error. The L12 core block field `motivation_element` must be defined as either: (a) the MC Problem element, or (b) the Motivation quad primary element. These are different Dramatica concepts. The existing Vertical Slice used the MC Problem. The template structure uses the quad primary.

**RECOMMENDATION:** L12 core `motivation_element` should map to the **MC Problem element** (Equity) because that is what fires flags and drives derived stats. The quad primaries belong in the L12_DRAMATICA_EXTENDED sub-table. Revise the template field label to `mc_problem_element` for clarity, or add a mapping note.

---

## Section 11: Downstream Handoff Checklist

- [x] All [FROM_STORYFORM] fields are populated — **FAIL: 40+ fields missing, require storyform**
- [x] All [AUTHORED] fields are completed — **PASS: structural meaning + invariants complete**
- [x] Structural meaning statement written — **PASS**
- [x] Narrative invariants defined — **PASS: 4 invariants**
- [x] L12 Core Block populated and matches — **CONDITIONAL: schema clarification needed on motivation_element**
- [ ] Character Astrology can proceed — **CONDITIONAL: core planets derivable from available data; full chart requires missing MC throughline fields**
- [ ] Template status changed to locked — **FAIL: template remains draft**
- [ ] Template placed in canonical folder — **PENDING**

**OVERALL TEMPLATE STATUS: DRAFT — Cannot lock. Storyform extraction required for 40+ fields across Sections 1, 2, 4, 5, 6, and 7.**