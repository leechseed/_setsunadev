---

## type: ssot_02_character_systems category: dramatica_integration version: 1.0.0 last_updated: 2026-03-02 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the role of Dramatica within the LEECHSEED character pipeline, establishes storyform-to-character binding architecture, L12 sub-table structure, tier-level integration rules, and report manifest." dependencies: ["ssot_03_character_systems_vertical_slice"]
---
# 🔮 SSOT: Dramatica Integration Protocol

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [What Dramatica Is in This System](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-dramatica-is-in-this-system)
3. [What Dramatica Is Not](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-dramatica-is-not)
4. [Storyform Architecture](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#storyform-architecture)
5. [Character-Storyform Binding](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#character-storyform-binding)
6. [Tier Integration Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-integration-rules)
7. [L12 FUNCTION Architecture](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#l12-function-architecture)
8. [Dramatica Report Manifest](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#dramatica-report-manifest)
9. [Pipeline Position](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pipeline-position)
10. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This document defines the role of Dramatica within the LEECHSEED character development pipeline. It establishes how Dramatica storyform outputs bind to characters, which data Dramatica provides at each tier of the 12-Layer Character Database, and where Dramatica sits relative to Character Astrology and the Vertical Slice protocol.

Dramatica is the first upstream system in the character pipeline. Its outputs are consumed by Character Astrology and by the 12-Layer system directly. No Tier 3 character enters the Vertical Slice without a locked Dramatica ingest.

---

## What Dramatica Is in This System

Dramatica is the **narrative structure engine**. It produces the thematic argument of the story and assigns each character a mechanical role within that argument. In LEECHSEED terms:

- Dramatica defines **what the story is about** (the storyform).
- Dramatica defines **what each character does to the argument** (their structural function).
- Dramatica defines **the terms of transformation** (resolve, growth, outcome, judgment).

Dramatica output is deterministic. A locked storyform produces a fixed set of character assignments. Those assignments do not change unless the storyform itself is revised — which constitutes a new version, not an edit.

---

## What Dramatica Is Not

Dramatica does not produce personality, psychology, physicality, sexuality, origin, trauma, shadow content, or aesthetic presentation. Those domains belong to the 12-Layer Character Database and to Character Astrology. Dramatica produces the **narrative skeleton**. The other systems produce the flesh.

Dramatica also does not produce plot. Plot is the sequence of events that dramatizes the storyform. The storyform constrains what the plot must accomplish, but the specific events, scenes, and beats are authored in the plot_systems domain, which is outside the scope of this document.

---

## Storyform Architecture

### The Primary Unit: One Storyform Per Story

The foundational unit is one complete Dramatica storyform per story. A storyform represents one Grand Argument — a complete thematic proposition with a beginning, middle, and end. For OVEREXITOUT, the primary storyform governs the complete narrative arc from Movement 1 through Movement 6.

### Nested Storyforms (Pattern 1)

The system supports nested storyforms for multi-arc or episodic structures. Each nested storyform operates as a complete argument within the boundaries of a parent storyform.

**Rules for nesting:**

- Every nested storyform receives its own `storyform_id`.
- A character may hold different structural roles across storyforms (MC in the parent, IC in a nested form).
- When a character holds roles in multiple storyforms, each role produces a separate L12 sub-table record keyed to the relevant `storyform_id`.
- The parent storyform has authority. When nested storyform assignments conflict with the parent, the parent governs.
- Nested storyforms are optional. The system does not require them. A single primary storyform is sufficient for any story.

### Storyform Identification

Every storyform in the system carries the following metadata:

|Field|Description|Example|
|---|---|---|
|`storyform_id`|Unique identifier|`oxo_primary_v1`|
|`ip`|Intellectual property|`overexitout`|
|`scope`|What the storyform covers|`full_narrative`|
|`parent_storyform_id`|Parent form if nested|`null` (for primary)|
|`status`|Lock state|`locked` / `draft`|
|`version`|Storyform version|`1.0`|

### Future Scaling (Flagged for plot_systems)

Act-level mini-forms and IP-level meta-forms are architecturally possible but not yet implemented. The `storyform_id` keying system supports them without schema changes. When plot_systems development begins, sub-storyforms for acts, episodes, and cross-IP arguments can be added using the same binding architecture defined here. No character-system changes will be required.

---

## Character-Storyform Binding

Every character who holds a Dramatica structural role is bound to at least one storyform. The binding record connects a `character_id` to a `storyform_id` and specifies the role.

**Binding record structure:**

|Field|Description|Example|
|---|---|---|
|`character_id`|Character identifier|`victoria_midnight`|
|`storyform_id`|Which storyform|`oxo_primary_v1`|
|`structural_role`|Dramatica role held|`mc_protagonist`|
|`archetype`|Dramatica archetype|`Protagonist`|
|`resolve`|Change / Steadfast|`Change`|
|`throughline`|Assigned throughline|`mc`|

A character with roles in multiple storyforms has multiple binding records. The core 12-layer character record (L1-L11) remains singular regardless of how many storyform bindings exist.

---

## Tier Integration Rules

### Tier 3 (Deep Characters — Protagonists, Antagonists, Key IC)

**Dramatica integration: Full.**

Tier 3 characters receive:

- A complete storyform binding record.
- A full L12 FUNCTION core block (10 variables).
- A full L12_DRAMATICA_EXTENDED sub-table (all throughline and element data).
- A locked Dramatica Ingest Template (.md) as source documentation.

Tier 3 is the only tier that requires a Dramatica ingest before the Vertical Slice can proceed.

### Tier 2 (Standard Characters — Recurring Supporting)

**Dramatica integration: Partial.**

Tier 2 characters receive:

- An **element signature**: 2-4 Dramatica elements drawn from the Motivation, Methodology, Evaluation, and Purpose sets that define their behavioral fingerprint.
- One or more **relational role tags** specifying their narrative function relative to specific Tier 3 characters.
- No storyform binding record. No throughline assignment. No full L12_DRAMATICA_EXTENDED sub-table.

The element signature uses the same vocabulary as Tier 3 elements, enabling cross-tier database queries. A query for "all characters carrying the Faith element" returns both Tier 3 characters with `motivation_element: Faith` and Tier 2 characters with `element_signature` containing `Faith`.

**Relational role taxonomy:**

|Role|Definition|
|---|---|
|`mirror`|Reflects a Tier 3 character's traits or situation back to them|
|`foil`|Presents an opposing approach to the same thematic problem|
|`catalyst`|Accelerates change in a Tier 3 character through interaction|
|`threshold_guardian`|Tests readiness before a Tier 3 character can advance|
|`herald`|Signals incoming change or threat relevant to a Tier 3 character|
|`mentor`|Provides knowledge, skill, or perspective a Tier 3 character lacks|
|`trickster`|Disrupts assumptions or exposes contradictions|
|`shapeshifter`|Allegiance or identity is unstable relative to a Tier 3 character|
|`anchor`|Stabilizing presence that a Tier 3 character relies on or resists|

A Tier 2 character may hold multiple relational roles against different Tier 3 characters.

### Tier 1 (Flat Characters — Background, Environmental)

**Dramatica integration: None.**

Tier 1 characters do not interact with Dramatica. They carry L1-L3 values only. Their narrative function is environmental — they populate the world. If a Tier 1 character becomes significant enough to require tracking, they are promoted to Tier 2 and receive an element signature.

---

## L12 FUNCTION Architecture

### Design Decision: Option C — Core + Sub-Table

L12 operates as a two-part structure: a core block that participates in derived statistics and flag triggers, and an extended sub-table that holds the complete Dramatica dataset for reference and cross-character querying.

### L12 Core Block (All Tiers That Carry L12)

The core block contains the variables that the 12-layer system actively uses for computation.

**Tier 3 L12 Core:**

|Variable|Source|Used By|
|---|---|---|
|`dramatica_archetype`|Storyform|Flag triggers|
|`motivation_element`|Character element set|Flag triggers, derived stats|
|`methodology_element`|Character element set|Behavioral reference|
|`evaluation_element`|Character element set|Behavioral reference|
|`purpose_element`|Character element set|Behavioral reference|
|`narrative_invariant`|Authored|Flag triggers|
|`story_outcome`|Storyform dynamics|Flag triggers|
|`story_judgement`|Storyform dynamics|Flag triggers|
|`limit_type`|Storyform dynamics|Flag triggers|
|`resolve`|Storyform dynamics|Flag triggers, derived stats|

**Tier 2 L12 Core:**

|Variable|Source|
|---|---|
|`tier`|`2`|
|`element_signature`|Authored from Dramatica element vocabulary|
|`relational_roles`|Authored (array of target + role pairs)|

### L12_DRAMATICA_EXTENDED Sub-Table (Tier 3 Only)

This sub-table attaches to L12 for Tier 3 characters. It holds the complete throughline and element data exported from Dramatica. These variables do not participate in derived stat computation or flag triggers. They exist for reference, cross-character querying, and downstream consumption by Character Astrology.

|Variable|Description|Example (Victoria Midnight)|
|---|---|---|
|`storyform_id`|Binding key|`oxo_primary_v1`|
|`mc_domain`|MC throughline domain|`Situation`|
|`mc_concern`|MC throughline concern|_(from storyform)_|
|`mc_issue`|MC throughline issue|`Interdiction`|
|`mc_problem`|MC throughline problem|`Equity`|
|`mc_solution`|MC throughline solution|`Inequity`|
|`mc_symptom`|MC throughline symptom|_(from storyform)_|
|`mc_response`|MC throughline response|_(from storyform)_|
|`mc_unique_ability`|MC unique ability|`Destiny`|
|`mc_critical_flaw`|MC critical flaw|`Truth`|
|`mc_benchmark`|MC benchmark|_(from storyform)_|
|`mc_focus`|MC focus|`Desire`|
|`mc_direction`|MC direction|`Ability`|
|`motivation_quad`|Full motivation set|`[Consider, Pursuit]`|
|`methodology_quad`|Full methodology set|`[Certainty, Proaction]`|
|`evaluation_quad`|Full evaluation set|`[Proven, Effect]`|
|`purpose_quad`|Full purpose set|`[Knowledge, Actuality]`|
|`os_domain`|OS throughline domain|_(from storyform)_|
|`os_concern`|OS throughline concern|_(from storyform)_|
|`os_issue`|OS throughline issue|_(from storyform)_|
|`os_problem`|OS throughline problem|_(from storyform)_|
|`ic_domain`|IC throughline domain|_(from storyform)_|
|`ic_concern`|IC throughline concern|_(from storyform)_|
|`rs_domain`|RS throughline domain|_(from storyform)_|
|`rs_concern`|RS throughline concern|_(from storyform)_|

Fields marked _(from storyform)_ are populated when the Dramatica Ingest Template is completed. The sub-table schema is fixed. Empty fields indicate data that has not yet been extracted from the storyform, not data that does not exist.

---

## Dramatica Report Manifest

Dramatica software exports analysis as PDF reports. Not all reports are relevant to the character pipeline. The following manifest categorizes each report type by its function in the system.

### Character-Pipeline Reports (Load-Bearing)

These reports contain data that directly feeds the Dramatica Ingest Template or L12 variables.

|Report|What It Contains|Feeds|
|---|---|---|
|**Character Report**|Per-character element assignments, archetype, motivation/methodology/evaluation/purpose|L12 core, element signatures|
|**Theme Report (per throughline)**|Domain, Concern, Issue, Problem, Solution, Symptom, Response, Unique Ability, Critical Flaw, Benchmark|L12_DRAMATICA_EXTENDED|
|**Story Dynamics Report**|Resolve, Growth, Outcome, Judgment, Limit, Driver, Timelock/Optionlock|L12 core (resolve, outcome, judgment, limit_type)|
|**Character Relationships Report**|Relationship mappings between characters|Tier 2 relational role assignment reference|

### Story-Level Reports (Reference)

These reports contain story-structure data relevant to plot_systems but not directly consumed by the character pipeline.

|Report|What It Contains|Future Use|
|---|---|---|
|**Plot Progression Report**|Signpost sequence per throughline|plot_systems (act structure)|
|**Storyweaving Report**|Scene-level argument progression|plot_systems (scene design)|
|**Story Points Report**|Complete storyform point listing|Master reference / validation|

### Informational Reports (Non-Load-Bearing)

These reports provide narrative prose or analysis that may inform authorial decisions but do not feed structured data into the pipeline.

|Report|What It Contains|Use|
|---|---|---|
|**Audience Appreciation Reports**|Prose descriptions of how elements feel to an audience|Writing guide reference|
|**Storytelling Reports**|Suggestions for dramatizing storyform elements|Writing guide reference|
|**Genre Reports**|Genre classification analysis|IP-level reference|

### Report Extraction Priority

When completing a Dramatica Ingest Template for a Tier 3 character, extract data in this order:

1. **Story Dynamics Report** — Lock resolve, outcome, judgment, limit type first.
2. **Theme Report (MC throughline)** — Lock the MC's full throughline variable set.
3. **Character Report** — Lock element quads and archetype.
4. **Theme Reports (OS, IC, RS)** — Lock remaining throughline data.
5. **Character Relationships Report** — Reference for Tier 2 relational roles.

Reports not listed in the extraction priority are consulted as needed but do not block template completion.

---

## Pipeline Position

```
┌─────────────────────┐
│   DRAMATICA          │
│   (Storyform)        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  DRAMATICA INGEST    │
│  TEMPLATE (.md)      │
│  [LOCKED]            │
└────────┬────────────┘
         │
         ├──────────────────────────┐
         │                          │
         ▼                          ▼
┌─────────────────────┐   ┌─────────────────────┐
│  CHARACTER ASTROLOGY │   │  12-LAYER VERTICAL   │
│  (consumes Dramatica │   │  SLICE               │
│   to derive chart)   │   │  (L12 populated      │
│                      │   │   directly from       │
│                      │   │   Dramatica ingest)   │
└────────┬────────────┘   └────────┬────────────┘
         │                          │
         ▼                          │
┌─────────────────────┐            │
│  CHAR ASTROLOGY      │            │
│  INGEST TEMPLATE     │            │
│  (.md) [LOCKED]      │────────────┘
└─────────────────────┘     (also feeds L7-L11
                             via astrology-to-layer
                             mapping)
```

**Reading the diagram:**

1. A locked Dramatica storyform produces a Dramatica Ingest Template.
2. The Dramatica Ingest Template feeds two consumers simultaneously: Character Astrology (which derives the natal chart from narrative positions) and the 12-Layer system (which populates L12 directly).
3. Character Astrology produces its own ingest template, which feeds additional data into L7-L11 of the 12-Layer system.
4. Step 1 Source Verification confirms both ingest templates exist and are locked before the Vertical Slice proceeds to Step 2.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-02|Initial SSOT. Establishes Dramatica role, storyform architecture, tier integration, L12 Option C structure, report manifest, pipeline position.|