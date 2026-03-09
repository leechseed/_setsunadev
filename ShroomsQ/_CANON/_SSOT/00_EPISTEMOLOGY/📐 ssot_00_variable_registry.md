---

## type: ssot_00_foundations category: variable_registry version: 1.0.0 last_updated: 2026-03-08 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "The complete code library index for every variable in the LEECHSEED character system. Defines canonical names, namespace paths, data types, scale classes, valid ranges, sources, consumers, and behavioral descriptions for all layer variables, derived statistics, flags, astrology variables, and state diff fields." dependencies: ["ssot_00_base60_number_system"]
---
# 📐 SSOT: Variable Registry / Code Library Index

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [Namespace Convention](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#namespace-convention)
3. [Registry Format](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#registry-format)
4. [Tier 1 Variables (L1-L3)](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-1-variables)
5. [Tier 2 Variables (L4-L6)](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-2-variables)
6. [Tier 3 Variables: L7 ORIGIN](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l7-origin)
7. [Tier 3 Variables: L8 IMPRINT](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l8-imprint)
8. [Tier 3 Variables: L9 EROS](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l9-eros)
9. [Tier 3 Variables: L10 SHADOW](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l10-shadow)
10. [Tier 3 Variables: L11 DESTINY](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l11-destiny)
11. [Tier 3 Variables: L12 FUNCTION](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-3-l12-function)
12. [L12 DRAMATICA EXTENDED](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#l12-dramatica-extended)
13. [Derived Statistics](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#derived-statistics)
14. [Status Flags](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#status-flags)
15. [Character Astrology Variables](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#character-astrology-variables)
16. [State Diff Variables](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#state-diff-variables)
17. [Character Metadata](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#character-metadata)
18. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This is the single lookup for every variable in the system. When any document, template, formula, flag, or tool references a variable, it uses the canonical name defined here. When any new variable is added to the system, it is registered here first.

---

## Namespace Convention

All variables follow this path structure:

```
[DOMAIN].[LAYER_CODE].[variable_name]
```

### Domain Prefixes

|Prefix|Scope|Example|
|---|---|---|
|`T1`|Tier 1 primary attributes|`T1.CORE.base_value`|
|`T2`|Tier 2 secondary attributes|`T2.WOUND.wound_score`|
|`T3`|Tier 3 deep variable stacks|`T3.SHADOW.shadow_density`|
|`T3X`|Tier 3 extended sub-tables|`T3X.FUNC_EXT.mc_domain`|
|`DRV`|Derived statistics|`DRV.stress_threshold`|
|`FLG`|Status flags|`FLG.shadow_denial`|
|`AST`|Character Astrology|`AST.PERSONAL.sun_sign`|
|`STT`|State diff fields|`STT.wound_score`|
|`META`|Character metadata|`META.character_id`|
|`REL`|Relationship records|`REL.relationship_type`|
|`MOD`|Layer-Locked Module variables|`MOD.[MODULE_CODE].[variable_name]`|

### Layer Codes

|Code|Layer|Tier|
|---|---|---|
|`CORE`|L1 — Cognitive/Psychological Mass|1|
|`VITAL`|L2 — Physical/Energetic Presence|1|
|`SOCIAL`|L3 — Relational Interface|1|
|`WILL`|L4 — Psychological Resistance|2|
|`WOUND`|L5 — Accumulated Damage|2|
|`DRIVE`|L6 — Motivation Fuel|2|
|`ORIGIN`|L7 — Birth Context|3|
|`IMPRINT`|L8 — Emotional Conditioning|3|
|`EROS`|L9 — Psycho-Sexual Conditioning|3|
|`SHADOW`|L10 — Repressed Content|3|
|`DESTINY`|L11 — Growth Vector|3|
|`FUNC`|L12 — Narrative Function (core)|3|
|`FUNC_EXT`|L12 — Dramatica Extended|3 (sub-table)|

### Naming Rules

- All variable names use `snake_case`
- All layer codes use `UPPER_CASE`
- All domain prefixes use `UPPER_CASE` abbreviations
- No variable name exceeds 30 characters
- No two variables share the same canonical name regardless of namespace
- Enum values use `snake_case` within brackets: `{secure, anxious, avoidant, disorganized}`

---

## Registry Format

Each variable entry contains:

|Field|Description|
|---|---|
|**Canonical Path**|Full namespace path|
|**Display Name**|Human-readable label|
|**Type**|`int`, `float`, `str`, `enum`, `array_str`, `array_enum`, `bool`|
|**Scale Class**|SC-N designation from Base 60 SSOT (numeric variables only)|
|**Display Range**|Human-facing value range|
|**Constraint**|Divisibility or parity constraint (if any)|
|**Default**|Default value (if any)|
|**Source**|`dramatica`, `astrology`, `authored`, `derived`, `computed`|
|**Feeds**|Which derived stats, flags, or downstream systems consume this|
|**Tier Min**|Minimum tier that requires this variable|
|**Behavior**|One-sentence LoL-ability-style description|

---

## Tier 1 Variables

### T1.CORE.base_value

|Field|Value|
|---|---|
|Canonical Path|`T1.CORE.base_value`|
|Display Name|CORE|
|Type|`int`|
|Scale Class|SC-20|
|Display Range|0–20|
|Constraint|None|
|Default|10|
|Source|`authored`|
|Feeds|`DRV.basic_damage_resistance` (via WILL derivation), `T2.WILL.base_value` (default derivation)|
|Tier Min|1|
|Behavior|Governs all mental skill defaults — when CORE is high, the character thinks in frameworks; when CORE is low, the character processes in fragments.|

### T1.VITAL.base_value

|Field|Value|
|---|---|
|Canonical Path|`T1.VITAL.base_value`|
|Display Name|VITAL|
|Type|`int`|
|Scale Class|SC-20|
|Display Range|0–20|
|Constraint|None|
|Default|10|
|Source|`authored`|
|Feeds|`T2.DRIVE.base_value` (default derivation), `DRV.narrative_momentum` (via DRIVE)|
|Tier Min|1|
|Behavior|Governs body precision and physical expressiveness — when VITAL exceeds 12, the character's body is a primary instrument; below 8, physicality is a liability.|

### T1.SOCIAL.base_value

|Field|Value|
|---|---|
|Canonical Path|`T1.SOCIAL.base_value`|
|Display Name|SOCIAL|
|Type|`int`|
|Scale Class|SC-20|
|Display Range|0–20|
|Constraint|None|
|Default|10|
|Source|`authored`|
|Feeds|`DRV.social_legibility`, `DRV.truth_exposure_index`|
|Tier Min|1|
|Behavior|Governs how the world reads the character — when SOCIAL exceeds 14, the character controls their signal; below 8, the signal leaks or distorts.|

---

## Tier 2 Variables

### T2.WILL.base_value

|Field|Value|
|---|---|
|Canonical Path|`T2.WILL.base_value`|
|Display Name|WILL|
|Type|`int`|
|Scale Class|SC-20|
|Display Range|0–20|
|Constraint|None|
|Default|`= T1.CORE.base_value`|
|Source|`derived` (from CORE), buyable ±1-3 at 5 pts/level|
|Feeds|`DRV.basic_damage_resistance`, `DRV.stress_threshold`, `FLG.earned_judgement`, `FLG.optionlock_progression`|
|Tier Min|2|
|Behavior|When WILL exceeds CORE, the character is more stubborn than smart; when WILL falls below CORE, the character understands the problem but cannot sustain resistance to it.|

### T2.WOUND.wound_score

|Field|Value|
|---|---|
|Canonical Path|`T2.WOUND.wound_score`|
|Display Name|WOUND|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|**Even values only** {0, 2, 4, 6, 8, 10, 12}|
|Default|0|
|Source|`authored` (assigned from character history, not purchased)|
|Feeds|`DRV.basic_damage_resistance`, `DRV.stress_threshold`, `DRV.collapse_risk`, `FLG.shadow_denial`, `FLG.optionlock_progression`, `FLG.kinship_collapse`|
|Tier Min|2|
|Behavior|Records damage that failed to resolve — at 0 the character is undamaged; at 12 the character has reached functional collapse threshold and cannot sustain protagonist-level load.|

### T2.DRIVE.base_value

|Field|Value|
|---|---|
|Canonical Path|`T2.DRIVE.base_value`|
|Display Name|DRIVE|
|Type|`int`|
|Scale Class|SC-20|
|Display Range|0–20|
|Constraint|None|
|Default|`= T1.VITAL.base_value`|
|Source|`derived` (from VITAL), buyable at 3 pts/level|
|Feeds|`DRV.narrative_momentum`|
|Tier Min|2|
|Behavior|When DRIVE equals VITAL, the character is ambition-driven and burns at full physical capacity; when DRIVE falls below VITAL, the fuel source is damaged and the character is meaning-driven.|

---

## Tier 3 Variables: L7 ORIGIN

### T3.ORIGIN.origin_class

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.origin_class`|
|Display Name|Origin Class|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{institutional, professional, working, working_criminal_adjacent, criminal, subsistence, unknown}`|
|Default|None|
|Source|`authored`|
|Feeds|Contextual reference for L8, L9, L10|
|Tier Min|3|
|Behavior|Defines the socioeconomic stratum the character emerged from — determines which institutions the character trusts, fears, or has never encountered.|

### T3.ORIGIN.origin_stability

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.origin_stability`|
|Display Name|Origin Stability|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for `T2.WOUND.wound_score` baseline|
|Tier Min|3|
|Behavior|At 0 the character grew up in chaos with no predictable structure; at 12 the environment was completely stable and the character's expectations of order are deeply set.|

### T3.ORIGIN.family_coherence

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.family_coherence`|
|Display Name|Family Coherence|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for `T3.IMPRINT.attachment_style_score`|
|Tier Min|3|
|Behavior|At 0 the family unit was fragmented or absent; at 12 the family operated as a unified system with clear roles and mutual support.|

### T3.ORIGIN.origin_wound_seed

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.origin_wound_seed`|
|Display Name|Origin Wound Seed|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Baseline input for `T2.WOUND.wound_score`|
|Tier Min|3|
|Behavior|The pre-story damage potential baked into the origin — at 0 the origin was protective; at 12 the origin was itself the primary wound source.|

### T3.ORIGIN.tech_level

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.tech_level`|
|Display Name|Tech Level|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual|
|Tier Min|3|
|Behavior|The technological sophistication of the character's formative environment — determines baseline digital literacy, tool familiarity, and system interface expectations.|

### T3.ORIGIN.system_exposure

|Field|Value|
|---|---|
|Canonical Path|`T3.ORIGIN.system_exposure`|
|Display Name|System Exposure|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{none, early_pre_awareness, early_aware, mid_integration, late_integration, institutional_native}`|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for L11 DESTINY, Movement assignment|
|Tier Min|3|
|Behavior|Defines when the character first became visible to or aware of systemic forces — determines whether the character enters the story knowing the rules or learning them.|

---

## Tier 3 Variables: L8 IMPRINT

### T3.IMPRINT.attachment_style

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.attachment_style`|
|Display Name|Attachment Style|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{secure, secure_anxious, secure_avoidant, anxious, avoidant, disorganized}`|
|Default|None|
|Source|`authored`, informed by `AST.PERSONAL.moon_sign`|
|Feeds|Contextual for relational behavior, `FLG.kinship_collapse`|
|Tier Min|3|
|Behavior|The character's default relational wiring — secure characters extend trust first; anxious characters monitor for abandonment; avoidant characters maintain distance as safety; disorganized characters oscillate unpredictably.|

### T3.IMPRINT.attachment_style_score

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.attachment_style_score`|
|Display Name|Attachment Intensity|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|`FLG.kinship_collapse`|
|Tier Min|3|
|Behavior|At 0 the character is relationally flat and bonds form weakly; at 12 the character bonds with maximum intensity and severed bonds produce maximum damage.|

### T3.IMPRINT.emotional_range

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.emotional_range`|
|Display Name|Emotional Range|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for behavioral texture|
|Tier Min|3|
|Behavior|At 0 the character is emotionally flat and affective display is minimal; at 12 the character experiences and expresses the full spectrum from euphoria to devastation.|

### T3.IMPRINT.conditional_patterns

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.conditional_patterns`|
|Display Name|Conditional Patterns|
|Type|`array_str`|
|Scale Class|N/A|
|Valid Values|Freeform strings (e.g., `merit_earns_freedom`, `loyalty_to_kinship`)|
|Default|`[]`|
|Source|`authored`|
|Feeds|`FLG.shadow_denial`|
|Tier Min|3|
|Behavior|The operational belief patterns established before story entry — these are the if/then rules the character runs on: "if I work hard, then I earn freedom."|

### T3.IMPRINT.imprint_flexibility

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.imprint_flexibility`|
|Display Name|Imprint Flexibility|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for arc resistance|
|Tier Min|3|
|Behavior|At 0 the character's conditioning is immovable and therapeutic intervention cannot reach it; at 12 the character rewires easily and past conditioning has minimal hold.|

### T3.IMPRINT.primary_attachment_object

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.primary_attachment_object`|
|Display Name|Primary Attachment Object|
|Type|`str`|
|Scale Class|N/A|
|Valid Values|Character ID, `deceased`, `absent`, `none`|
|Default|`none`|
|Source|`authored`|
|Feeds|`FLG.kinship_collapse`, relational tracking|
|Tier Min|3|
|Behavior|The person the character orients their relational system around — when this object is lost, the entire attachment architecture destabilizes.|

---

## Tier 3 Variables: L9 EROS

### T3.EROS.erotic_blueprint_type

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.erotic_blueprint_type`|
|Display Name|Erotic Blueprint|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{kinesthetic, sensual, energetic, sexual, shapeshifter}`|
|Default|None|
|Source|`authored`, informed by `AST.PERSONAL.venus_sign`|
|Feeds|Contextual for intimacy behavior|
|Tier Min|3|
|Behavior|The primary channel through which the character experiences erotic connection — kinesthetic characters connect through motion and pressure; sensual through texture and environment; energetic through anticipation and charge; sexual through explicit stimulation; shapeshifters adapt to partner.|

### T3.EROS.desire_vector

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.desire_vector`|
|Display Name|Desire Vector|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|Contextual|
|Tier Min|3|
|Behavior|At 0 desire is absent or fully suppressed; at 12 desire is the dominant driver of relational and intimate behavior and overrides other priorities under stress.|

### T3.EROS.shame_index

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.shame_index`|
|Display Name|Shame Index|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|`DRV.truth_exposure_index`|
|Tier Min|3|
|Behavior|At 0 the character experiences no shame around desire or sexuality and broadcasts freely; at 12 shame is the dominant filter on all intimate expression and the character cannot access desire without triggering self-punishment.|

### T3.EROS.intimacy_mode

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.intimacy_mode`|
|Display Name|Intimacy Mode|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{parallel_presence, face_to_face, performance, pursuit, dissolution, withholding}`|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for relational behavior|
|Tier Min|3|
|Behavior|How the character structures closeness — parallel_presence characters bond by doing things side by side; face_to_face through direct emotional engagement; performance through display; pursuit through chase dynamics; dissolution through merging boundaries; withholding through controlled access.|

### T3.EROS.source_confidence

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.source_confidence`|
|Display Name|Source Confidence|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{canonical, inferred, speculative}`|
|Default|`inferred`|
|Source|`authored`|
|Feeds|Validation flag — `inferred` values require follow-up extraction|
|Tier Min|3|
|Behavior|Tracks whether L9 data was drawn from canonical documentation, inferred from adjacent evidence, or speculatively assigned pending validation.|

---

## Tier 3 Variables: L10 SHADOW

### T3.SHADOW.shadow_density

|Field|Value|
|---|---|
|Canonical Path|`T3.SHADOW.shadow_density`|
|Display Name|Shadow Density|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|**Even values only** (must match WOUND parity)|
|Default|None|
|Source|`authored`, informed by `AST` debilitated planets and 12th House contents|
|Feeds|`DRV.collapse_risk`, `DRV.social_legibility` (via projection_tendency)|
|Tier Min|3|
|Behavior|At 0 the character is relatively integrated with minimal repressed content; at 12 the shadow dominates and behavior under stress is almost entirely driven by unconscious material.|

### T3.SHADOW.projection_tendency

|Field|Value|
|---|---|
|Canonical Path|`T3.SHADOW.projection_tendency`|
|Display Name|Projection Tendency|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|**Multiples of 3 only** {0, 3, 6, 9, 12}|
|Default|None|
|Source|`authored`|
|Feeds|`DRV.social_legibility`, `FLG.shadow_denial`|
|Tier Min|3|
|Behavior|At 0 the character owns their shadow content and does not project it onto others; at 12 the character attributes all disowned qualities to external targets and cannot distinguish self-generated distress from externally caused harm.|

### T3.SHADOW.regression_pattern

|Field|Value|
|---|---|
|Canonical Path|`T3.SHADOW.regression_pattern`|
|Display Name|Regression Pattern|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{control_escalation, withdrawal, dissociation, aggression, performance, people_pleasing, intellectualization, substance_seeking}`|
|Default|None|
|Source|`authored`|
|Feeds|Behavioral texture under stress|
|Tier Min|3|
|Behavior|The specific behavioral mode the character defaults to when shadow content is activated — the thing they DO when they cannot face what they ARE.|

### T3.SHADOW.shadow_content

|Field|Value|
|---|---|
|Canonical Path|`T3.SHADOW.shadow_content`|
|Display Name|Shadow Content|
|Type|`array_str`|
|Scale Class|N/A|
|Valid Values|Freeform strings|
|Default|`[]`|
|Source|`authored`, informed by `AST` 12th House + Pluto aspects|
|Feeds|Contextual for flag triggers, behavioral texture|
|Tier Min|3|
|Behavior|The specific repressed, denied, or projected content the character carries — each entry is one thing the character cannot face about themselves.|

---

## Tier 3 Variables: L11 DESTINY

### T3.DESTINY.growth_axis

|Field|Value|
|---|---|
|Canonical Path|`T3.DESTINY.growth_axis`|
|Display Name|Growth Axis|
|Type|`str`|
|Scale Class|N/A|
|Default|None|
|Source|`authored`, informed by `AST.STRUCTURAL.uranus_sign`|
|Feeds|Contextual for arc design|
|Tier Min|3|
|Behavior|The named direction the character must grow toward — not where they currently stand, but where the arc demands they move.|

### T3.DESTINY.resistance_index

|Field|Value|
|---|---|
|Canonical Path|`T3.DESTINY.resistance_index`|
|Display Name|Resistance Index|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|**Even values only**|
|Default|None|
|Source|`authored`, informed by `AST` Jupiter-Saturn aspects|
|Feeds|`DRV.narrative_momentum`, `FLG.optionlock_progression`|
|Tier Min|3|
|Behavior|At 0 the character is ready to change and the arc resolves quickly; at 12 the character is constitutionally opposed to their own solution and the full story duration is required to force transformation.|

### T3.DESTINY.soul_evolution_archetype

|Field|Value|
|---|---|
|Canonical Path|`T3.DESTINY.soul_evolution_archetype`|
|Display Name|Soul Evolution Archetype|
|Type|`str`|
|Scale Class|N/A|
|Default|None|
|Source|`authored`|
|Feeds|Contextual|
|Tier Min|3|
|Behavior|The archetypal pattern of the character's transformation — names what kind of evolution this is (tactical_disruptor, wounded_healer, fallen_idealist, etc.).|

### T3.DESTINY.karmic_memory

|Field|Value|
|---|---|
|Canonical Path|`T3.DESTINY.karmic_memory`|
|Display Name|Karmic Memory|
|Type|`str`|
|Scale Class|N/A|
|Default|None|
|Source|`authored`|
|Feeds|Contextual|
|Tier Min|3|
|Behavior|The deep-pattern belief the character carries from before the story — the thing they "know" to be true that the arc will challenge or destroy.|

### T3.DESTINY.growth_requirement

|Field|Value|
|---|---|
|Canonical Path|`T3.DESTINY.growth_requirement`|
|Display Name|Growth Requirement|
|Type|`str`|
|Scale Class|N/A|
|Default|None|
|Source|`authored`, informed by Dramatica MC Solution|
|Feeds|Arc design, `FLG.earned_judgement`|
|Tier Min|3|
|Behavior|The specific transformation the character must undergo — stated as an action ("accept_asymmetry", "release_control", "trust_without_proof").|

---

## Tier 3 Variables: L12 FUNCTION

### T3.FUNC.dramatica_archetype

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.dramatica_archetype`|
|Display Name|Dramatica Archetype|
|Type|`enum`|
|Valid Values|`{Protagonist, Antagonist, Guardian, Contagonist, Reason, Emotion, Sidekick, Skeptic, Complex}`|
|Source|`dramatica`|
|Feeds|`FLG.earned_judgement`|
|Tier Min|3|

### T3.FUNC.mc_problem_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.mc_problem_element`|
|Display Name|MC Problem Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|`FLG.truth_vulnerability`, Character Astrology Moon derivation|
|Tier Min|3|
|Behavior|The core narrative friction — the element that drives all of the character's difficulty.|

_Note: This field was previously named `motivation_element`. Renamed per Phase 4 schema clarification._

### T3.FUNC.methodology_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.methodology_element`|
|Display Name|Methodology Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|Character Astrology Mercury derivation|
|Tier Min|3|

### T3.FUNC.evaluation_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.evaluation_element`|
|Display Name|Evaluation Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|Contextual|
|Tier Min|3|

### T3.FUNC.purpose_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.purpose_element`|
|Display Name|Purpose Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|Character Astrology Venus derivation|
|Tier Min|3|

### T3.FUNC.narrative_invariant

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.narrative_invariant`|
|Display Name|Narrative Invariant|
|Type|`str`|
|Source|`authored`|
|Feeds|Structural constraint on all downstream story development|
|Tier Min|3|

### T3.FUNC.story_outcome

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.story_outcome`|
|Display Name|Story Outcome|
|Type|`enum`|
|Valid Values|`{Success, Failure}`|
|Source|`dramatica`|
|Feeds|`FLG.earned_judgement`, Character Astrology Pluto derivation|
|Tier Min|3|

### T3.FUNC.story_judgement

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.story_judgement`|
|Display Name|Story Judgement|
|Type|`enum`|
|Valid Values|`{Good, Bad}`|
|Source|`dramatica`|
|Feeds|`FLG.earned_judgement`, Character Astrology Pluto derivation|
|Tier Min|3|

### T3.FUNC.limit_type

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.limit_type`|
|Display Name|Limit Type|
|Type|`enum`|
|Valid Values|`{Timelock, Optionlock}`|
|Source|`dramatica`|
|Feeds|`FLG.optionlock_progression`|
|Tier Min|3|

### T3.FUNC.resolve

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.resolve`|
|Display Name|Resolve|
|Type|`enum`|
|Valid Values|`{Change, Steadfast}`|
|Source|`dramatica`|
|Feeds|Character Astrology (mutable vs fixed emphasis), arc design|
|Tier Min|3|

### Tier 2 L12 Format

For Tier 2 characters, L12 uses a different variable set:

### T3.FUNC.tier

| Canonical Path | `T3.FUNC.tier` | | Type | `int` | | Valid Values | `{1, 2, 3}` |

### T3.FUNC.element_signature

| Canonical Path | `T3.FUNC.element_signature` | | Type | `array_str` | | Valid Values | 2-4 Dramatica element names | | Source | `authored` from Dramatica element vocabulary | | Tier Min | 2 |

### T3.FUNC.relational_roles

| Canonical Path | `T3.FUNC.relational_roles` | | Type | `array` of `{target: str, role: enum}` | | Valid Roles | `{mirror, foil, catalyst, threshold_guardian, herald, mentor, trickster, shapeshifter, anchor}` | | Source | `authored` | | Tier Min | 2 |

---

## L12 DRAMATICA EXTENDED

All variables in the extended sub-table. Type is `str` unless noted. Source is `dramatica` for all. Tier Min is 3 for all.

|Canonical Path|Display Name|
|---|---|
|`T3X.FUNC_EXT.storyform_id`|Storyform ID|
|`T3X.FUNC_EXT.mc_domain`|MC Domain|
|`T3X.FUNC_EXT.mc_concern`|MC Concern|
|`T3X.FUNC_EXT.mc_issue`|MC Issue|
|`T3X.FUNC_EXT.mc_counterpoint`|MC Counterpoint|
|`T3X.FUNC_EXT.mc_problem`|MC Problem|
|`T3X.FUNC_EXT.mc_solution`|MC Solution|
|`T3X.FUNC_EXT.mc_symptom`|MC Symptom|
|`T3X.FUNC_EXT.mc_response`|MC Response|
|`T3X.FUNC_EXT.mc_unique_ability`|MC Unique Ability|
|`T3X.FUNC_EXT.mc_critical_flaw`|MC Critical Flaw|
|`T3X.FUNC_EXT.mc_benchmark`|MC Benchmark|
|`T3X.FUNC_EXT.mc_focus`|MC Focus|
|`T3X.FUNC_EXT.mc_direction`|MC Direction|
|`T3X.FUNC_EXT.mc_signpost_1`|MC Signpost 1|
|`T3X.FUNC_EXT.mc_signpost_2`|MC Signpost 2|
|`T3X.FUNC_EXT.mc_signpost_3`|MC Signpost 3|
|`T3X.FUNC_EXT.mc_signpost_4`|MC Signpost 4|
|`T3X.FUNC_EXT.motivation_quad`|Motivation Quad (array)|
|`T3X.FUNC_EXT.methodology_quad`|Methodology Quad (array)|
|`T3X.FUNC_EXT.evaluation_quad`|Evaluation Quad (array)|
|`T3X.FUNC_EXT.purpose_quad`|Purpose Quad (array)|
|`T3X.FUNC_EXT.os_domain`|OS Domain|
|`T3X.FUNC_EXT.os_concern`|OS Concern|
|`T3X.FUNC_EXT.os_issue`|OS Issue|
|`T3X.FUNC_EXT.os_problem`|OS Problem|
|`T3X.FUNC_EXT.ic_domain`|IC Domain|
|`T3X.FUNC_EXT.ic_concern`|IC Concern|
|`T3X.FUNC_EXT.rs_domain`|RS Domain|
|`T3X.FUNC_EXT.rs_concern`|RS Concern|

---

## Derived Statistics

All derived stats compute in internal (0-60) space per Base 60 SSOT.

### DRV.basic_damage_resistance

|Field|Value|
|---|---|
|Canonical Path|`DRV.basic_damage_resistance`|
|Formula (internal)|`(T2.WILL × 3) - ((T2.WOUND × 5) / 2)`|
|Input Constraints|WOUND must be even|
|Output Space|Internal (0-60), may go negative|
|Source|`computed`|

### DRV.social_legibility

|Field|Value|
|---|---|
|Canonical Path|`DRV.social_legibility`|
|Formula (internal)|`(T1.SOCIAL × 3) - ((T3.SHADOW.projection_tendency × 5) / 3)`|
|Input Constraints|projection_tendency must be multiple of 3|
|Output Space|Internal (0-60)|
|Source|`computed`|

### DRV.narrative_momentum

|Field|Value|
|---|---|
|Canonical Path|`DRV.narrative_momentum`|
|Formula (internal)|`(T2.DRIVE × 3) + ((T3.DESTINY.resistance_index × 5) / 2)`|
|Input Constraints|resistance_index must be even|
|Output Space|Internal (0-60)|
|Source|`computed`|

### DRV.stress_threshold

|Field|Value|
|---|---|
|Canonical Path|`DRV.stress_threshold`|
|Formula (internal)|`(T2.WILL × 3) - (T2.WOUND × 5)`|
|Input Constraints|None|
|Output Space|Internal, may go negative|
|Source|`computed`|
|Behavior|When negative, the character is operating past structural limit — function is maintained by qualitative stubbornness, not quantitative margin.|

### DRV.collapse_risk

|Field|Value|
|---|---|
|Canonical Path|`DRV.collapse_risk`|
|Formula (internal)|`((T2.WOUND × 5) + (T3.SHADOW.shadow_density × 5)) / 2`|
|Input Constraints|WOUND + shadow_density must be even (both even — enforced by constraints on both variables)|
|Output Space|Internal (0-60)|
|Source|`computed`|

### DRV.truth_exposure_index

|Field|Value|
|---|---|
|Canonical Path|`DRV.truth_exposure_index`|
|Formula (internal)|`(T1.SOCIAL × 3) + ((12 - T3.EROS.shame_index) × 5)`|
|Input Constraints|None|
|Output Space|Internal, uncapped (may exceed 60)|
|Source|`computed`|
|Behavior|Values exceeding 60 indicate the character's signal legibility exceeds the system's maximum containment threshold — the system cannot ignore this character.|

---

## Status Flags

### FLG.shadow_denial

|Field|Value|
|---|---|
|Canonical Path|`FLG.shadow_denial`|
|Trigger|`T2.WOUND > 6 AND T3.SHADOW.projection_tendency >= 6 AND T3.IMPRINT.conditional_patterns contains "merit_earns_freedom"`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|

### FLG.truth_vulnerability

|Field|Value|
|---|---|
|Canonical Path|`FLG.truth_vulnerability`|
|Trigger|`T1.SOCIAL < 12 AND T3.FUNC.mc_problem_element = "Equity" AND T3.SHADOW.shadow_density > 6`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|

### FLG.optionlock_progression

|Field|Value|
|---|---|
|Canonical Path|`FLG.optionlock_progression`|
|Trigger|`T2.WOUND > 8 AND T3.DESTINY.resistance_index > 8 AND T3.FUNC.limit_type = "Optionlock"`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|

### FLG.earned_judgement

|Field|Value|
|---|---|
|Canonical Path|`FLG.earned_judgement`|
|Trigger|`T3.FUNC.dramatica_archetype = "Protagonist" AND T3.FUNC.story_outcome = "Failure" AND T2.WILL > 10`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|

### FLG.kinship_collapse

|Field|Value|
|---|---|
|Canonical Path|`FLG.kinship_collapse`|
|Trigger|`T3.IMPRINT.attachment_style_score > 6 AND T3.IMPRINT.primary_attachment_object = "deceased" AND T2.WOUND > 8`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|

---

## Character Astrology Variables

### Personal Stack

|Canonical Path|Type|Source|
|---|---|---|
|`AST.PERSONAL.sun_sign`|`enum` (zodiac signs)|DAI Step 1|
|`AST.PERSONAL.sun_element`|`enum` `{fire, earth, air, water}`|Derived from sun_sign|
|`AST.PERSONAL.sun_modality`|`enum` `{cardinal, fixed, mutable}`|Derived from sun_sign|
|`AST.PERSONAL.moon_sign`|`enum`|DAI Step 2|
|`AST.PERSONAL.mercury_sign`|`enum`|DAI Step 4|
|`AST.PERSONAL.venus_sign`|`enum`|DAI Step 5|
|`AST.PERSONAL.mars_sign`|`enum`|DAI Step 6|

### Structural Stack

|Canonical Path|Type|Source|
|---|---|---|
|`AST.STRUCTURAL.saturn_sign`|`enum`|DAI Step 7|
|`AST.STRUCTURAL.jupiter_sign`|`enum`|DAI Step 8|
|`AST.STRUCTURAL.uranus_sign`|`enum`|DAI Step 9|
|`AST.STRUCTURAL.neptune_sign`|`enum`|DAI Step 10|
|`AST.STRUCTURAL.pluto_sign`|`enum`|DAI Step 11|

### Angles

|Canonical Path|Type|Source|
|---|---|---|
|`AST.ANGLE.ascendant_sign`|`enum`|DAI Step 3|
|`AST.ANGLE.midheaven_sign`|`enum`|DAI Step 12|
|`AST.ANGLE.descendant_sign`|`enum`|Computed (opposite of ascendant)|
|`AST.ANGLE.ic_sign`|`enum`|Computed (opposite of midheaven)|

### Aspects

|Canonical Path|Type|Notes|
|---|---|---|
|`AST.ASPECT.[id].planet_a`|`str`|Planet name|
|`AST.ASPECT.[id].planet_b`|`str`|Planet name|
|`AST.ASPECT.[id].type`|`enum` `{conjunction, square, opposition, trine, sextile}`||
|`AST.ASPECT.[id].gate_type`|`enum` `{AND, NOT, XOR, OR}`||
|`AST.ASPECT.[id].dramatica_source`|`str`|Tension source|

### Houses

|Canonical Path|Type|
|---|---|
|`AST.HOUSE.[planet_name].house_number`|`int` (1-12)|
|`AST.HOUSE.[planet_name].house_type`|`enum` `{angular, succedent, cadent}`|

### Dignities

|Canonical Path|Type|
|---|---|
|`AST.DIGNITY.[planet_name].status`|`enum` `{domicile, exaltation, peregrine, detriment, fall}`|

---

## State Diff Variables

State diffs use the `STT` prefix and mirror the variable they modify, with additional metadata.

|Canonical Path|Type|Purpose|
|---|---|---|
|`STT.state_id`|`str`|Unique state identifier|
|`STT.narrative_moment`|`str`|Human-readable when|
|`STT.movement`|`str`|Movement tag|
|`STT.mc_distance_temporal`|`int`|Temporal distance from MC|
|`STT.mc_distance_narrative`|`int`|Causal distance from MC|
|`STT.base_record_version`|`str`|Version of base record|
|`STT.[any_layer_variable]`|(matches source type)|Modified value — replaces base on query|
|`STT.WILL_EFFECTIVE`|`int` SC-20|State-only field — temporary WILL reduction|
|`STT.state_note`|`str`|Prose justification for diff|

---

## Character Metadata

|Canonical Path|Type|Purpose|
|---|---|---|
|`META.character_id`|`str`|Unique character identifier|
|`META.character_name`|`str`|Display name|
|`META.ip`|`str`|Intellectual property|
|`META.tier`|`int` `{1, 2, 3}`|Character tier|
|`META.status`|`enum` `{draft, locked, archived}`|Record status|
|`META.version`|`str`|Record version|
|`META.storyform_id`|`str`|Bound storyform|

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-08|Initial registry. 50+ layer variables, 6 derived statistics, 5 status flags, 25+ astrology variables, state diff fields, character metadata. Full namespace convention. All numeric variables assigned to base 60 scale classes with constraints.|