---
type: ssot_02_character_systems
category: template_dramatica_ingest
module_of: ssot_02_character_systems_vertical_slice
version: 1.0.2
tier: narratology
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "v1.0.0 2026-10-04: RULED — BOLO 100 C18"
purpose: "Blank fill-in form for the Dramatica Ingest Template. One copy per Tier 3 character. It holds the locked storyform data that feeds the L12 block and the Character Astrology derivation."
dependencies: ["ssot_02_dramatica_integration_protocol", "ssot_02_step_1_source_verification_protocol", "ssot_02_character_astrology_dai"]
---
# 📐 SSOT: Template — Dramatica Ingest

## How to use this form

1. Copy this file to the character's folder as `[CHARACTER_ID]_dramatica_ingest.md`, as set out in the [Step 1 protocol](🔮ssot_02_step_1_source_verification_protocol.md).
2. Delete this section and the frontmatter above. Keep the section numbers. The Step 1 checks cite them.
3. Fill the sections in the order of the extraction priority: Section 1, then 4, then 3 and 2, then 6, 5 and 7, with Section 8 as the log. Report names are in the [integration doc](🔮%20ssot_02_dramatica_integration_protocol.md).
4. Leave a field empty if the storyform does not give it yet. Write `⏸` and the reason. Never guess.
5. Section 10 is generated from Sections 1 to 9. Fill it last.

Tier 3 characters only. A Tier 2 character gets an element signature and relational roles instead (integration doc, Tier 2 section) and does not use this form.

---

## Header

```yaml
character_id: ____
ip: ____
tier: 3
storyform_id: ____          # e.g. oxo_primary_v1
storyform_version: ____
storyform_status: draft     # draft | locked
status: draft               # draft | locked
locked_on: ____             # date, when status is locked
authoritative_doc_ref: ____ # the locked character document
```

---

## 1. Storyform Dynamics

Source: Story Dynamics Report. Lock these first.

|Field|Value|
|---|---|
|`story_outcome`|____ (Success / Failure)|
|`story_judgement`|____ (Good / Bad)|
|`story_driver`|____ (Action / Decision)|
|`limit_type`|____ (Timelock / Optionlock)|

---

## 2. Structural Role

Source: Character Report and Story Dynamics Report.

|Field|Value|
|---|---|
|`structural_role`|____ (e.g. mc_protagonist)|
|`dramatica_archetype`|____|
|`resolve`|____ (Change / Steadfast)|
|`growth`|____ (Start / Stop)|
|`approach`|____ (Do-er / Be-er)|
|`mental_sex`|____|

---

## 3. Element Quads

Source: Character Report. Write both elements of each quad. All eight fields are required.

|Quad|Element 1|Element 2|
|---|---|---|
|`motivation_quad`|____|____|
|`methodology_quad`|____|____|
|`evaluation_quad`|____|____|
|`purpose_quad`|____|____|

**Structural meaning statement.** Two or three sentences, plain words: what this element set makes the character do to the argument.

> ____

---

## 4. MC Throughline

Source: Theme Report, MC throughline. Required if the character is the MC.

|Field|Value|
|---|---|
|`mc_domain`|____|
|`mc_concern`|____|
|`mc_issue`|____|
|`mc_problem_element`|____|
|`mc_solution`|____|
|`mc_symptom`|____|
|`mc_response`|____|
|`mc_unique_ability`|____|
|`mc_critical_flaw`|____|
|`mc_benchmark`|____|
|`mc_focus`|____|
|`mc_direction`|____|
|`mc_inhibitor`|____ (not in the L12 sub-table; the DAI uses it for Saturn)|

---

## 5. IC Throughline

Source: Theme Report, IC throughline. Required if the character is the IC.

|Field|Value|
|---|---|
|`ic_domain`|____|
|`ic_concern`|____|

Other IC points the storyform gives (free text): ____

---

## 6. OS Throughline

Source: Theme Report, OS throughline. Always required.

|Field|Value|
|---|---|
|`os_domain`|____|
|`os_concern`|____|
|`os_issue`|____|
|`os_problem`|____|
|`os_role`|____ (this character's role in the OS; the DAI uses it for the Midheaven)|
|`story_goal`|____ (the DAI uses it for the Midheaven)|

---

## 7. RS Throughline

Source: Theme Report, RS throughline. Required if the character is an RS principal.

|Field|Value|
|---|---|
|`rs_domain`|____|
|`rs_concern`|____|

---

## 8. Report Source Log

One line per report consulted, in extraction order.

|Report|Used for|File or page|Date read|
|---|---|---|---|
|Story Dynamics Report|Sections 1, 2|____|____|
|Theme Report (MC)|Section 4|____|____|
|Character Report|Sections 2, 3|____|____|
|Theme Reports (OS, IC, RS)|Sections 5, 6, 7|____|____|
|Character Relationships Report|Tier 2 relational roles (reference)|____|____|

---

## 9. Touchstones

A Touchstone is a structural law derived from the storyform. Every Tier 3 character has at least one. The machine field is `touchstone`; the old name `narrative_invariant` is an alias in the variable registry.

|Touchstone|Statement (one sentence)|Storyform source|What it costs the character|
|---|---|---|---|
|TS ____|____|____|____|

---

## 10. L12 Core Block

Generate this from Sections 1 to 9. It must list exactly the Tier 3 L12 core variables in the [integration doc](🔮%20ssot_02_dramatica_integration_protocol.md). If that list changes, this block follows it.

```yaml
L12_FUNCTION:
  dramatica_archetype: ____
  mc_problem_element: ____
  methodology_element: ____
  evaluation_element: ____
  purpose_element: ____
  touchstone: ____   # the Touchstone
  story_outcome: ____
  story_judgement: ____
  limit_type: ____
  resolve: ____
```

---

## 11. Downstream Handoff Checklist

- [ ] Section 1 is complete and matches the Story Dynamics Report.
- [ ] Section 2 has all six fields.
- [ ] Section 3 has all eight element fields and the meaning statement.
- [ ] The throughline sections this character needs are complete.
- [ ] Section 9 has at least one Touchstone.
- [ ] Section 10 matches Sections 1 to 9.
- [ ] `storyform_status` and `status` read `locked`.
- [ ] The Character Astrology Ingest can now cite this file in `dramatica_ingest_ref` ([astrology form](📐%20ssot_02_template_astrology_ingest.md)).

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-10-04|v1.0.0 2026-10-04: RULED — BOLO 100 C18. First blank form, built from the integration doc and the Step 1 checks (2.1 to 2.9).|
|1.0.1|2026-10-04|BOLO 100 TOUCH BATCH 1, Chief "REC.": field renamed, schema-pass wording closed (TS-B3).|
|1.0.2|2026-10-05|BOLO 102 batch A (Chief: "All recs go"): Section 1 `story_limit` renamed `limit_type`; Section 4 `mc_problem` renamed `mc_problem_element`, matching Section 10; Section 9's `touchstone` alias corrected to its old name, `narrative_invariant`, as the variable registry records it.|
