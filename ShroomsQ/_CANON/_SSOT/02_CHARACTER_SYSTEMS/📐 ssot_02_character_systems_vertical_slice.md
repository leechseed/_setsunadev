---

## type: ssot_03_character_systems category: character_systems version: 1.0.0 last_updated: 2026-02-17 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Establishes the authoritative standard for the 12-Layer Character Database Vertical Slice, including tier structure, numeric variable definitions, derived statistic formulas, and flag trigger conditions." dependencies: ["[[📐_ssot_05_operations_writing_guide]]", "[[📐_ssot_05_operations_ai_instruction_protocol]]"]
---
# 📐 ssot_03_character_systems_vertical_slice

## Table of Contents

1. [Purpose](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd#purpose)
2. [Core Methodology](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd#core-methodology)
3. [Implementation](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd#implementation)
4. [Examples — Victoria Midnight Full Slice](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd#examples--victoria-midnight-full-slice)
5. [Version History](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd#version-history)



## Purpose

This document defines the **12-Layer Character Database Vertical Slice** protocol. A **Vertical Slice** is the complete traversal of all 12 layers for a single character, producing numeric values, derived statistics, boolean status flags, and a machine-readable structured data block. The Vertical Slice is the primary validation instrument for the layer system. It confirms that numeric assignments produce outputs that correspond to canonical character documentation. It also functions as the seed record for database ingestion when the system transitions from AI-augmented generation to hard-coded query infrastructure.

---

## Core Methodology

### The Three-Tier Structure

The 12-Layer system is modular. Tier depth determines character complexity and database weight.

|Tier|Layers|Character Class|Point Budget|
|---|---|---|---|
|**Tier 1**|L1–L3|Flat|~75 pts|
|**Tier 2**|L4–L6|Standard|~140 pts|
|**Tier 3**|L7–L12|Deep|Uncapped|

Tier 1 is sufficient for background characters. Tier 2 is sufficient for recurring supporting characters. Tier 3 is mandatory for all protagonists and antagonists.

---

### The 12 Layers: Domain Declarations

Each layer governs one and only one domain. Overlap between layers constitutes a schema error, not a character note.

**L1 — CORE:** Cognitive and psychological mass. Governs all mental skill defaults, ideological frameworks, and problem-solving capacity. Default value: 10. Point cost: 20 pts per level above 10 (IQ equivalent).

**L2 — VITAL:** Physical and energetic presence. Governs body precision, endurance, reaction capacity, and physical expressiveness. Default value: 10. Point cost: 20 pts per level above 10 (DX equivalent).

**L3 — SOCIAL:** Relational interface. Governs projection into the world, reception of others, social legibility, and reaction modifier math. Default value: 10. Point cost: 10 pts per level above 10 (HT equivalent).

**L4 — WILL:** Psychological resistance to coercion, manipulation, and systemic pressure. Derives from CORE by default (`WILL = CORE`). Buyable up or down at 5 pts per level.

**L5 — WOUND:** Accumulated psychological damage that failed to resolve. Assigned during character history entry. High WOUND reduces effective WILL and SOCIAL under trigger conditions. Scale: 0 (undamaged) to 10 (functional collapse threshold).

**L6 — DRIVE:** Narrative motivation fuel. Derives from VITAL by default (`DRIVE = VITAL`). Spent on active goal-pursuit; recovered through narrative resolution. Buyable at 3 pts per level.

**L7 — ORIGIN:** Birth context, socioeconomic class, family architecture, environmental formation, and system exposure timing. Numeric variables feed WOUND base and SOCIAL defaults.

**L8 — IMPRINT:** Formative emotional conditioning. Attachment architecture, emotional range, and operational belief patterns established prior to story entry.

**L9 — EROS:** Psycho-sexual conditioning. Desire structure, erotic patterning, shame architecture, and intimacy mode.

**L10 — SHADOW:** Repressed, projected, and denied content. High SHADOW values generate active disadvantage clusters and modify stress-state behavior.

**L11 — DESTINY:** Directional growth vector. The MC Solution element, growth requirement, resistance index, and soul evolution archetype. Describes what the character is building toward, not where they currently stand.

**L12 — FUNCTION:** Dramatica narrative role, objective story function, throughline assignment, and mechanical purpose in the story engine. Bridges psychological construction to narrative mechanics.

---

### Derived Statistics

Derived statistics are computed columns. They are not entered — they are calculated from primary layer values. All fractions round down.

|Derived Stat|Formula|
|---|---|
|Basic Damage Resistance|`WILL - (WOUND / 2)`|
|Social Legibility|`SOCIAL - (SHADOW.projection_tendency / 3)`|
|Narrative Momentum|`DRIVE + (DESTINY.resistance_index / 2)`|
|Stress Threshold|`WILL - WOUND`|
|Collapse Risk|`(WOUND + SHADOW.shadow_density) / 2`|
|Truth Exposure Index|`SOCIAL + (10 - EROS.shame_index)`|

**Truth Exposure Index** is the primary systemic legibility metric. A score above 15 indicates a character who cannot effectively manage their own signal visibility. This metric directly feeds antagonist targeting logic and systemic response escalation.

---

### Flag Trigger Conditions

**Status Flags** are boolean conditions that fire automatically when numeric thresholds are satisfied. Flags represent derived character states — they are not assigned, they are computed. Each flag is a valid SQL WHERE clause against the character record.

Four flag states exist:

- **ACTIVE** — Condition is currently met. Behavior consequences are in force.
- **PENDING** — Condition will be met at a defined narrative event. Used for climax-dependent flags.
- **FIRED_PRE_STORY** — Condition was met before story entry. Documents the character's pre-existing state.
- **INACTIVE** — Condition is not met. Flag is dormant.

---

### The Structured Data Block

Every Vertical Slice terminates in a machine-readable structured data block. This block is the database seed record. It contains all primary values, derived statistics, and flag states in a queryable format. When the system transitions from AI generation to hard-coded database infrastructure, the structured data block is the ingestion artifact.

---

## Implementation

### Step 1 — Source Verification

Before assigning any values, confirm that canonical documentation for the character exists and is locked. Do not run a Vertical Slice against a character whose narrative role, Dramatica function, or origin is still in development. Numeric instability in the source produces unstable values.

### Step 2 — Tier 1 Assignment

Assign CORE, VITAL, and SOCIAL. Read the Tier 1 values first and verify they produce a recognizable character outline without reference to any other layer. If Tier 1 alone does not suggest the character, the primary values are wrong.

### Step 3 — Tier 2 Derivation

Derive WILL from CORE, then adjust up or down based on documented resolve behavior. Assign WOUND from the character's history — this is the only value that is not a choice or a buy, it is a record of what happened. Derive DRIVE from VITAL, then adjust based on documented motivation source (ambition-driven characters maintain DRIVE = VITAL; meaning-driven characters reduce DRIVE below VITAL ceiling).

### Step 4 — Tier 3 Variable Population

Populate L7 through L12 variable stacks from canonical source documentation. Each variable requires a documented source. If the source does not exist, mark the variable as `[INFERRED]` and note the basis for inference. Inferred values require a follow-up extraction query before the layer is considered complete.

### Step 5 — Derived Statistic Computation

Compute all six derived statistics. Read the Truth Exposure Index and Collapse Risk values first — these two stats most reliably indicate whether the numeric assignments are coherent.

### Step 6 — Flag Evaluation

Evaluate each flag trigger condition against the computed values. Document flag state and narrative timing. Flags that fire unexpectedly indicate a schema inconsistency — investigate the contributing layer values before proceeding.

### Step 7 — Structured Data Block Generation

Produce the structured data block in the format defined in the Examples section. This block is the output artifact. All preceding documentation is human-readable justification for the values in this block.

---

## Examples — Victoria Midnight Full Slice

**IP:** OVEREXITOUT (The Outliers) **Character Status:** Canonical / Locked **Slice Version:** 1.0.0

---

### Tier 1 — Primary Layers

**L1 CORE: 13**

Victoria Midnight operates a sophisticated causal model (merit earns freedom), applies it consistently across conditions, and updates it only under catastrophic contradictory evidence. Her MC Problem is Equity — a philosophical framework error, not an intellectual failure. The cognitive architecture is sound; the premise is wrong. Score above average but not maximum. Point cost: 60 pts.

**L2 VITAL: 14**

Racing driver. Reaction time, spatial processing, mechanical intuition, and physical courage are primary operational tools pre-crash. Post-crash hardware requires a VITAL ceiling high enough to carry the manifestation load. "Motion under pressure, never ornamental" is a 14. Point cost: 80 pts.

**L3 SOCIAL: 10**

Her MC Critical Flaw is Truth — when she speaks truth, it desyncs her hardware and triggers Noise. Her social interface is not weak. It is accurate in a world that cannot process accuracy. She does not lack social intelligence; she lacks the capacity for social dishonesty. Average SOCIAL with a specific catastrophic exploit vector is more precise than a modified score. Point cost: 0 pts.

**Tier 1 Total: 140 pts**

---

### Tier 2 — Secondary Layers

**L4 WILL: 14 (CORE + 1)**

Resolve is Change — she bends eventually. The story arc requires maximum systemic pressure to achieve that change. She survives the crash, the brother's death, the academy intake, and the Ban before breaking. WILL sits one point above CORE: she is slightly more stubborn than she is intelligent. Buy-up cost: 5 pts.

**L5 WOUND: 8 / 10**

The wound is the pace-notes. She ignored her brother's guidance during the rally. The car exploded. He died. She survived. The wound is not grief — it is the knowledge that she chose not to listen. That choice killed him. Score 8 because the story requires her to continue functioning as protagonist. Score 9 or 10 produces behavioral collapse incompatible with protagonist load-bearing.

Active wound triggers: mechanical failure events; guidance she is inclined to refuse; her brother's name; scenes where listening would prevent harm and she does not.

**L6 DRIVE: 12 (VITAL - 2)**

Meaning-driven characters burn below their physical ceiling because their fuel source is already damaged at story entry. The crash did not destroy her DRIVE — it dented the tank. Reduction reflects the compromised fuel source, not reduced physical capacity. Buy-down return: 6 pts.

**Tier 2 Total (net): 139 pts**

---

### Tier 3 — Deep Variable Stacks

**L7 ORIGIN**

|Variable|Value|
|---|---|
|`origin_class`|working_criminal_adjacent|
|`origin_stability`|4|
|`family_coherence`|7|
|`origin_wound_seed`|6|
|`tech_level`|6|
|`system_exposure`|early_pre_awareness|

Her origin is outside institutional legibility. The salvage economy phase (M1A) precedes system awareness. The Delta Coast racing scene is the first context in which her output becomes visible at scale. The system's attention during M1B is acquisition, not admiration. She does not know the difference until the Ban is already in motion.

---

**L8 IMPRINT**

|Variable|Value|
|---|---|
|`attachment_style`|secure_anxious|
|`attachment_style_score`|6|
|`emotional_range`|9|
|`conditional_patterns`|[merit_earns_freedom, loyalty_to_kinship, distrust_of_institution]|
|`imprint_flexibility`|3|
|`primary_attachment_object`|brother_deceased|

Her primary attachment object was her brother. He functioned as navigator to her driver — the pace-notes were not technical data, they were the communication system of two people in complete mutual trust. When she overrode them, she did not commit a driving error. She violated the founding logic of her attachment architecture. WOUND at L5 is the damage. IMPRINT at L8 is why the damage is catastrophic rather than survivable.

---

**L9 EROS**

|Variable|Value|
|---|---|
|`erotic_blueprint_type`|kinesthetic|
|`desire_vector`|3|
|`shame_index`|2|
|`intimacy_mode`|parallel_presence|

Source: Inferred from aesthetic documentation ("beauty that is earned, not curated; motion under pressure, never ornamental"). This layer requires a follow-up extraction query: `Victoria Midnight sexuality intimacy desire relationships OVEREXITOUT`. Current values stand until contradicted by canonical source.

---

**L10 SHADOW**

|Variable|Value|
|---|---|
|`shadow_density`|7|
|`projection_tendency`|6|
|`regression_pattern`|control_escalation|
|`shadow_content`|[culpability_for_brother, distrust_of_own_judgment, fear_of_being_right_and_wrong_simultaneously]|

The shadow is the choice, not the grief. She heard the pace-notes and decided she knew better. Processing that choice fully requires accepting that she is capable of catastrophic error while certain she is correct. Her MC Problem (Equity) is the conscious-layer version of this recognition failure. Under stress, she doubles down on control behaviors rather than accepting input — the shadow content is the precise mechanism that makes the Optionlock activate.

---

**L11 DESTINY**

|Variable|Value|
|---|---|
|`growth_axis`|inequity|
|`resistance_index`|8|
|`soul_evolution_archetype`|tactical_disruptor|
|`karmic_memory`|meritocratic_certainty|
|`growth_requirement`|accept_asymmetry|

Her Destiny vector points toward a specific disillusionment that becomes precision rather than cynicism. The arc moves: "Merit earns freedom" → "Visibility invites ownership" → "Control is the only form of safety left" → [story climax] "Rigged is not the same as wrong." Resistance index 8 is why the arc requires the full story duration. She is constitutionally opposed to her own solution.

---

**L12 FUNCTION**

|Variable|Value|
|---|---|
|`dramatica_archetype`|Protagonist|
|`motivation_element`|Equity|
|`methodology_element`|Proaction|
|`evaluation_element`|Result|
|`purpose_element`|Actuality|
|`narrative_invariant`|cost_and_meaning|
|`story_outcome`|Failure|
|`story_judgement`|Good|
|`limit_type`|Optionlock|
|`resolve`|Change|

The Optionlock fires because her wound and resistance index combination systematically eliminates exits. The Truth-is-Enough Veto, the Heroic Recognition Veto, and the Reset Veto are narrative invariants that correspond directly to flag logic — each veto closes one option class permanently.

---

### Derived Statistics

|Stat|Formula|Result|
|---|---|---|
|Basic Damage Resistance|`14 - (8 / 2)`|**10**|
|Social Legibility|`10 - (6 / 3)`|**8**|
|Narrative Momentum|`12 + (8 / 2)`|**16**|
|Stress Threshold|`14 - 8`|**6**|
|Collapse Risk|`(8 + 7) / 2`|**8**|
|Truth Exposure Index|`10 + (10 - 2)`|**18**|

Truth Exposure Index 18 is the primary diagnostic value. It quantifies why the Ban activates against her and not against other characters with equivalent capability profiles. She is maximally legible to the system because she carries low shame and average social masking. The system cannot categorize a signal it can read completely and that refuses to self-regulate.

---

### Active Flags

**FLAG: SHADOW_DENIAL — ACTIVE**

Trigger: `WOUND > 6 AND SHADOW.projection_tendency >= 5 AND IMPRINT.conditional_patterns contains "merit_earns_freedom"`

She routes causal responsibility for the crash toward systemic injustice. "The institution is unfair" is factually correct. It also functions as a shield against "I chose not to listen and he died." Both propositions are simultaneously true. Her arc is the collapse of the shield — the moment she holds both at once is the Judgement: Good inflection point.

---

**FLAG: TRUTH_VULNERABILITY — ACTIVE**

Trigger: `SOCIAL < 12 AND FUNCTION.motivation_element = "Equity" AND SHADOW.shadow_density > 6`

When she speaks truth, wound content surfaces through her social interface. She does not code-switch, does not manage her signal, does not perform legibility. The Ban is the system's response to this flag firing in a public context. Truth is not her virtue — it is her exploit vector.

---

**FLAG: OPTIONLOCK_PROGRESSION — ACTIVE**

Trigger: `WOUND > 7 AND DESTINY.resistance_index > 7 AND FUNCTION.limit_type = "Optionlock"`

Exits close because of who she is, not because a clock runs out. Each Veto Rule in the canonical documentation corresponds to one option class closing permanently. This flag confirms the Optionlock structure by numeric derivation independent of the narrative documentation.

---

**FLAG: EARNED_JUDGEMENT — PENDING**

Trigger: `FUNCTION.dramatica_archetype = "Protagonist" AND FUNCTION.story_outcome = "Failure" AND WILL > 10`

Fires at story climax. WILL 14 provides sufficient internal structure to assign meaning to total systemic defeat. She finds Meaning in the wreckage because the architecture to do so remains intact even after everything external is stripped.

---

**FLAG: KINSHIP_COLLAPSE — FIRED_PRE_STORY**

Trigger: `IMPRINT.attachment_style_score > 5 AND primary_attachment_object = "deceased" AND WOUND > 7`

This flag fired at the crash. The character enters the story in a post-collapse attachment state. No primary attachment object is currently active. All relational behavior post-crash operates without a secure base.

---

### Structured Data Block

```
CHARACTER_ID: victoria_midnight
IP: overexitout
STATUS: locked
VERSION: 1.0.0

TIER_1:
  CORE: 13
  VITAL: 14
  SOCIAL: 10

TIER_2:
  WILL: 14
  WOUND: 8
  DRIVE: 12

L7_ORIGIN:
  origin_class: working_criminal_adjacent
  origin_stability: 4
  family_coherence: 7
  origin_wound_seed: 6
  tech_level: 6
  system_exposure: early_pre_awareness

L8_IMPRINT:
  attachment_style: secure_anxious
  attachment_style_score: 6
  emotional_range: 9
  conditional_patterns: [merit_earns_freedom, loyalty_to_kinship, distrust_of_institution]
  imprint_flexibility: 3
  primary_attachment_object: brother_deceased

L9_EROS:
  erotic_blueprint_type: kinesthetic
  desire_vector: 3
  shame_index: 2
  intimacy_mode: parallel_presence
  source_confidence: [INFERRED]

L10_SHADOW:
  shadow_density: 7
  projection_tendency: 6
  regression_pattern: control_escalation
  shadow_content: [culpability_for_brother, distrust_of_own_judgment, fear_of_being_right_and_wrong]

L11_DESTINY:
  growth_axis: inequity
  resistance_index: 8
  soul_evolution_archetype: tactical_disruptor
  karmic_memory: meritocratic_certainty
  growth_requirement: accept_asymmetry

L12_FUNCTION:
  dramatica_archetype: Protagonist
  motivation_element: Equity
  methodology_element: Proaction
  evaluation_element: Result
  purpose_element: Actuality
  narrative_invariant: cost_and_meaning
  story_outcome: Failure
  story_judgement: Good
  limit_type: Optionlock
  resolve: Change

DERIVED:
  basic_damage_resistance: 10
  social_legibility: 8
  narrative_momentum: 16
  stress_threshold: 6
  collapse_risk: 8
  truth_exposure_index: 18

FLAGS:
  SHADOW_DENIAL: ACTIVE
  TRUTH_VULNERABILITY: ACTIVE
  OPTIONLOCK_PROGRESSION: ACTIVE
  EARNED_JUDGEMENT: PENDING
  KINSHIP_COLLAPSE: FIRED_PRE_STORY
```

---

## Version History

|Version|Date|Changes|
|:--|:--|:--|
|1.0.0|2026-02-17|Initial vertical slice protocol with Victoria Midnight as canonical example.|