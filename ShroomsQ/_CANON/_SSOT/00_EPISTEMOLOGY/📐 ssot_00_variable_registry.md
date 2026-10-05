---
type: ssot_00_foundations
category: variable_registry
rung: standard · NASA four, ruled 2026-09-15 (BOLO 50)
version: 1.3.0
tier: foundation
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
trunk: BLACK
purpose: "The complete code library index for every variable in the LEECHSEED character system. Defines canonical names, namespace paths, data types, scale classes, valid ranges, tags, sources, consumers, and behavioral descriptions for all layer variables, derived statistics, flags, astrology variables, and state diff fields."
dependencies: ["ssot_00_base_60_number_system", "ssot_02_character_systems_vertical_slice"]
---
# 📐 SSOT: Variable Registry / Code Library Index

## Table of Contents

1. [Purpose](#purpose)
2. [Namespace Convention](#namespace-convention)
3. [Ownership Rule](#ownership-rule)
4. [Registry Format](#registry-format)
5. [Tier 1 Variables (L1-L3)](#tier-1-variables)
6. [Tier 2 Variables (L4-L6)](#tier-2-variables)
7. [Tier 3 Variables: L7 ORIGIN](#tier-3-variables-l7-origin)
8. [Tier 3 Variables: L8 IMPRINT](#tier-3-variables-l8-imprint)
9. [Tier 3 Variables: L9 EROS](#tier-3-variables-l9-eros)
10. [Tier 3 Variables: L10 SHADOW](#tier-3-variables-l10-shadow)
11. [Tier 3 Variables: L11 DESTINY](#tier-3-variables-l11-destiny)
12. [Tier 3 Variables: L12 FUNCTION](#tier-3-variables-l12-function)
13. [L12 DRAMATICA EXTENDED](#l12-dramatica-extended)
14. [Slice Fields (added in 1.2.0)](#slice-fields-added-in-120)
15. [Derived Statistics](#derived-statistics)
16. [Status Flags](#status-flags)
17. [Character Astrology Variables](#character-astrology-variables)
18. [State Diff Variables](#state-diff-variables)
19. [Character Metadata](#character-metadata)
20. [Version History](#version-history)

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
|`SET`|Setting layer fields S1 to S12, owned by 03|`SET.S8.reason_remembered`|
|`PLT`|Plot layer fields P1 to P12, owned by 04|`PLT.P7.reveal_content`|
|`MOD`|Layer-Locked Module variables|`MOD.[MODULE_CODE].[variable_name]`|

**`REL` note.** The 02 state architecture owns the `REL.*` fields (IF-00-02-26; IF catalog call 4, ruled 2026-10-05), and this registry holds one pointer row for them. Chief decides each `REL` variable. The author fills all twelve Registry Format fields for it in the state architecture. The author checks first that no existing relational field already holds it: `T1.SOCIAL.knowledge_map`, `T3.FUNC.relational_roles` and `T2.WOUND.relational_refs`.

**`SET` and `PLT` note.** The `SET` prefix names the S1 to S12 setting fields. The `PLT` prefix names the P1 to P12 plot fields (IF-00-03-04 and IF-00-04-08; IF catalog call 4, ruled 2026-10-05). The path is `[SET or PLT].[S or P layer].[field_name]`. Setting (03) and Plot (04) own the fields. This registry holds the prefixes and the pointer rows only.

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

## Ownership Rule

**Each system owns its fields in its own doc.** This registry holds the character fields (L1 to L12), the derived statistics, the flags, the astrology and state-diff paths, and the `MOD` namespace. For every other system it holds one pointer row, and the pointer never copies a field. A field kept in two places drifts.

|System|Doc that owns the fields|What it owns|
|---|---|---|
|Narrative (01)|[📐 ssot_01_story_spine_comparative_tree.md](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_story_spine_comparative_tree.md), [📐 ssot_01_spine_house_inventory.md](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_spine_house_inventory.md)|The `feeds:` library-keying field, the `module_of:` front-matter field and the spine addresses (`SPINE.L4`, `SPINE.L2.OS.concern`) (IF-00-01-10, IF-00-01-05, IF-00-01-06).|
|Character state (02)|[🔮ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md)|The `REL.*` relationship fields (IF-00-02-26). The 139-row alias table stays in the vertical slice (see Read aliases).|
|Setting (03)|[📐 ssot_03_setting_system.md](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md)|The S1 to S12 layer fields under the `SET` prefix, including S12 FUNCTION.|
|Plot (04)|[📐 ssot_04_plot_system.md](../04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md), [📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md)|The P1 to P12 layer fields under the `PLT` prefix, including P12 FUNCTION. The fabula owns the event ids. The storyform record is Plot's, and `META.storyform_id` and `T3X.FUNC_EXT.storyform_id` point at it (IF-00-04-07).|
|Theme (06)|[📐 ssot_06_theme_system.md](../06_THEME_SYSTEMS/📐%20ssot_06_theme_system.md)|The theme fields and the argument record.|
|Tracking (08)|[📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md)|Time codes and story points.|
|Worldbuilding (05)|[📐 ssot_05_worldbuilding_system.md](../05_WORLDBUILDING_SYSTEMS/📐%20ssot_05_worldbuilding_system.md)|The worldbuilding fields.|
|Style (07)|[📐 ssot_07_1_prose_style.md](../07_STYLE_GUIDES/📐%20ssot_07_1_prose_style.md)|No fields. Style consumes `T1.SOCIAL.voice_sheet`, which stays an L3 field in this registry (IF-00-07-05).|
|Operations (09)|[📐 ssot_ai_instruction_protocol.md](../09_OPERATIONS/📐%20ssot_ai_instruction_protocol.md)|The front-matter keys every doc carries.|

L12 FUNCTION is fed from the storyform. Its field list lives in the [Dramatica integration protocol](../02_CHARACTER_SYSTEMS/🔮%20ssot_02_dramatica_integration_protocol.md), and this registry mirrors it.

---

## Registry Format

Each variable entry contains:

|Field|Description|
|---|---|
|**Canonical Path**|Full namespace path|
|**Display Name**|Human-readable label|
|**Type**|`int`, `float`, `str`, `enum`, `array_str`, `array_enum`, `bool`, `object`, `array_object`|
|**Scale Class**|SC-N designation from Base 60 SSOT (numeric variables only)|
|**Display Range**|Human-facing value range|
|**Constraint**|Divisibility or parity constraint (if any)|
|**Default**|Default value (if any)|
|**Source**|`dramatica`, `astrology`, `authored`, `derived`, `computed`|
|**Tag**|`Static`, `Dynamic` or `Derived`. Copied from the slice table "Field tags · every field". Static is set once at origin. Dynamic changes across the story, and the state architecture records each change as a state diff. Derived is computed from layer values and never stored as a diff. A field with split sub-field tags says so. No variable ships without a Tag.|
|**Feeds**|Which derived stats, flags, or downstream systems consume this|
|**Tier Min**|Minimum tier that requires this variable|
|**Behavior**|One-sentence LoL-ability-style description|

The Slice Fields section (1.2.0) lists the fields the slice added after the first registry. It uses one table row per field with these columns: Canonical Path, Type, Scale Class, Tag, Source, Consumer, and Values and sub-fields. The row holds the same facts as an entry. The Behavior of each field lives in the slice layer paragraph it cites.

### Retire a variable

Chief rules each retirement. The author keeps the entry and marks it retired with the date and BOLO. The author names any replacement. The author keeps an alias row for the old name. The author removes the variable from every Feeds line that lists it. Character records keep their data. The author adds a version-history row.

### Read aliases

The vertical slice keeps the 139-row alias table, THE SCHEMA PASS: the coined names the schema pass aliased or dropped. This registry cites that table as its alias list and does not copy it (IF-00-02-28; IF catalog call 4, ruled 2026-10-05). The table names three read aliases: `shame_index` for `exposure_shame`, `primary_attachment_object` for `secure_base_object`, and `motivation_element` for `mc_problem_element`. The author keeps an alias row on the entry of each renamed field.

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

---

## Tier 3 Variables: L8 IMPRINT

### T3.IMPRINT.attachment_style

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.attachment_style`|
|Display Name|Attachment Style|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{secure, anxious, avoidant, fearful_avoidant}` (four-way, slice 2.1.0). Legacy values `secure_anxious`, `secure_avoidant` and `disorganized` stay readable. A locked record keeps its value and is not reclassified.|
|Default|None|
|Source|`authored`, informed by `AST.PERSONAL.moon_sign`|
|Feeds|Contextual for relational behavior, `FLG.kinship_collapse`|
|Tier Min|3|
|Behavior|The character's default relational wiring — secure characters extend trust first; anxious characters monitor for abandonment; avoidant characters maintain distance as safety; disorganized characters oscillate unpredictably.|
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

### T3.IMPRINT.primary_attachment_object

|Field|Value|
|---|---|
|Canonical Path|`T3.IMPRINT.primary_attachment_object`|
|Display Name|Primary Attachment Object (read alias of `secure_base_object`, slice 2.1.0)|
|Type|`str`|
|Scale Class|N/A|
|Valid Values|Character ID, `deceased`, `absent`, `none`|
|Default|`none`|
|Source|`authored`|
|Feeds|`FLG.kinship_collapse`, relational tracking|
|Tier Min|3|
|Behavior|The person the character orients their relational system around — when this object is lost, the entire attachment architecture destabilizes.|
|Tag|Dynamic (read alias of `secure_base_object`)|

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
|Tag|Static|

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
|Tag|Dynamic|

### T3.EROS.shame_index

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.shame_index`|
|Display Name|Shame Index (read alias of `exposure_shame`, slice 2.2.0)|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored`|
|Feeds|`DRV.truth_exposure_index`|
|Tier Min|3|
|Behavior|At 0 the character experiences no shame around desire or sexuality and broadcasts freely; at 12 shame is the dominant filter on all intimate expression and the character cannot access desire without triggering self-punishment.|
|Tag|Dynamic (read alias of `exposure_shame`)|

### T3.EROS.armor_index

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.armor_index`|
|Display Name|Armor Index|
|Type|`int`|
|Scale Class|SC-12|
|Display Range|0–12|
|Constraint|None|
|Default|None|
|Source|`authored` (adopted 2026-08-15, L9 v2 ingest — Walker PSY.01; propagated 2026-08-24)|
|Feeds|`DRV.expressive_range`|
|Tier Min|3|
|Behavior|Chronic protective constriction — at 0 the character is unarmored and fully expressive; at 12 the character is maximally defended and can deliberately send almost nothing. Independent of shame: low shame with high armor is the armored-but-readable paradox.|
|Tag|Dynamic|

### T3.EROS.satisfaction_cycle_truncation

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.satisfaction_cycle_truncation`|
|Display Name|Satisfaction Cycle Truncation|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{none, yield, push, reach, grasp, pull}`|
|Default|`none`|
|Source|`authored` (adopted 2026-08-15, L9 v2 ingest — Walker / Bainbridge-Cohen)|
|Feeds|Contextual — somatic mechanism for `T2.WOUND.wound_score`|
|Tier Min|3|
|Behavior|Names the phase of the yield→push→reach→grasp→pull cycle where the character's engagement breaks — locates any documented wound on a somatic sequence.|
|Tag|Static|

### T3.EROS.erotic_safety_precondition

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.erotic_safety_precondition`|
|Display Name|Erotic Safety Precondition|
|Type|`str`|
|Scale Class|N/A|
|Valid Values|Freeform (e.g., `control`, `privacy`, `trust`, `ritual`)|
|Default|None|
|Source|`authored` (introduced 2026-08-15, L9 v2 ingest — Walker Invariant 4)|
|Feeds|Contextual for intimacy behavior and arc design|
|Tier Min|3|
|Behavior|What the nervous system must register before pleasure is accessible — when the story makes this precondition structurally unavailable, pleasure is architecturally foreclosed.|
|Tag|Dynamic|

### T3.EROS.intimacy_mode

|Field|Value|
|---|---|
|Canonical Path|`T3.EROS.intimacy_mode`|
|Display Name|Intimacy Mode|
|Type|`enum`|
|Scale Class|N/A|
|Valid Values|`{partnered_merge, parallel_presence, solo_directed, bounded_no_strings}` (slice 3.2.0, CL2). Legacy values `face_to_face`, `performance`, `pursuit`, `dissolution` and `withholding` stay readable. A list of `{ref, value}` scopes it per partner or audience.|
|Default|None|
|Source|`authored`|
|Feeds|Contextual for relational behavior|
|Tier Min|3|
|Behavior|How the character structures closeness — parallel_presence characters bond by doing things side by side; face_to_face through direct emotional engagement; performance through display; pursuit through chase dynamics; dissolution through merging boundaries; withholding through controlled access.|
|Tag|Dynamic|

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
|Tag|Static|

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
|Tag|Dynamic|

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
|Tag|Dynamic|

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
|Tag|Static|

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
|Tag|Dynamic|

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
|Tag|Static|

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
|Tag|Dynamic|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

### T3.FUNC.evaluation_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.evaluation_element`|
|Display Name|Evaluation Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|Contextual|
|Tier Min|3|
|Tag|Static|

### T3.FUNC.purpose_element

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.purpose_element`|
|Display Name|Purpose Element|
|Type|`str`|
|Source|`dramatica`|
|Feeds|Character Astrology Venus derivation|
|Tier Min|3|
|Tag|Static|

### T3.FUNC.touchstone

|Field|Value|
|---|---|
|Canonical Path|`T3.FUNC.touchstone`|
|Display Name|Touchstone|
|Alias|`narrative_invariant` (old name; read alias for old ingests, renamed BOLO 100)|
|Type|`str`|
|Value|The Touchstone id in the register form `TS n:m`, for example `TS 1:3`. The field then joins the Touchstones register. The slug the field held before is a read alias of the id (IF catalog call 4, ruled 2026-10-05).|
|Source|`authored`|
|Feeds|Structural constraint on all downstream story development|
|Tier Min|3|
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

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
|Tag|Static|

### Tier 2 L12 Format

For Tier 2 characters, L12 uses a different variable set:

### T3.FUNC.tier

| Canonical Path | `T3.FUNC.tier` | | Type | `int` | | Valid Values | `{1, 2, 3}` | | Tag | Static |

### T3.FUNC.element_signature

| Canonical Path | `T3.FUNC.element_signature` | | Type | `array_str` | | Valid Values | 2-4 Dramatica element names | | Source | `authored` from Dramatica element vocabulary | | Tier Min | 2 | | Tag | Static |

### T3.FUNC.relational_roles

| Canonical Path | `T3.FUNC.relational_roles` | | Type | `array` of `{target: str, role: enum}` | | Valid Roles | `{mirror, foil, catalyst, threshold_guardian, herald, mentor, trickster, shapeshifter, anchor}` | | Source | `authored` | | Tier Min | 2 | | Tag | Static |

---

## L12 DRAMATICA EXTENDED

All variables in the extended sub-table. Type is `str` unless noted. Source is `dramatica` for all. Tier Min is 3 for all. Tag is Static for all: the storyform is locked, and a revision makes a new version.

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

## Slice Fields (added in 1.2.0)

The slice reached 3.3.1. These are the fields it added after the first registry, one row each, in layer order. Each carries its Tag. The Behavior of each field lives in the slice layer paragraph named in the section line. `shadow_content` entries also carry a `kind`: denied_wish, assigned_by_world, feared_double, standing_alarm, scrubbed_bond or imposed_self_image.

### Slice fields · L1 CORE

Layer paragraph: slice, L1 CORE. Egri psychology, labels and neurotype.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T1.CORE.psychology_stack`|object|N/A|Dynamic|authored|Contextual under `T1.CORE.base_value`|Egri text checklist: moral standards, ambition, frustrations, temperament, attitude to life, complexes, extrovert or introvert, abilities, qualities, IQ.|
|`T1.CORE.identity_frame`|object|N/A|Dynamic|authored|Contextual for `T3.EROS.orientation_dimensions`|The frame he names himself by: gender persona, orientation label, era category, and the gender script per audience.|
|`T1.CORE.identity_frame.assigned_labels`|array_object|N/A|Dynamic|authored|Contextual for `T1.SOCIAL.civic_standing`|`{label, by, year, accepted}`. `by` is law, medicine, church, state, buyer, family or peers.|
|`T1.CORE.neurotype`|object|N/A|Static for `label`, `known_to_self`. Dynamic for `masked_by`, `attention_pattern`.|authored|`T2.DRIVE.drive_texture` fade note|`{label, known_to_self, masked_by: novelty/effort/none, attention_pattern: hyperfocus/scattered/mixed}`. Store it as one cause among others.|

### Slice fields · L2 VITAL

Layer paragraph: slice, L2 VITAL.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T1.VITAL.physiology_stack`|object|N/A|Dynamic|authored|Contextual under `T1.VITAL.base_value`|Egri text checklist: heredity, appearance, defects, posture, health. Heredity itself sits at L7.|
|`T1.VITAL.body_capital`|object|N/A|Dynamic|authored|Contextual (adults only)|`{price_factors, window{curve,start_age,end_age}, venue_tier, trust_signal, working_body_gap, embodied_cost}`.|

### Slice fields · L3 SOCIAL

Layer paragraph: slice, L3 SOCIAL. Four fields (`intimacy_mode`, `disclosure_posture`, `love_lust_cleft`, `self_presentation`) take a list of `{ref, value}`. The bare value is the default.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T1.SOCIAL.sociology_stack`|object|N/A|Dynamic|authored|`T1.SOCIAL.voice_sheet.noticing_filter` derives from it|Egri text checklist: class, occupation, education, home life, political affiliation.|
|`T1.SOCIAL.circumplex`|object|SC-10 (signed, -5 to +5)|Dynamic|authored|Optional dial, null by default|`{agency, communion}`. Agency runs yielding to dominant. Communion runs cold to warm.|
|`T1.SOCIAL.knowledge_map`|array_object|N/A|Dynamic|authored|`T3.EROS.consent_posture`. L3 `disclosure_posture` is a view onto it.|Per relationship: what each knows, what each knows the other knows, who may claim not to know.|
|`T1.SOCIAL.knowledge_map.cover`|array_object|N/A|Dynamic|authored|`T3.SHADOW.shadow_content` for a double life|`{kind: overcompensation/double_life/passing/hidden_in_plain_view, sized_to, cost}`.|
|`T1.SOCIAL.community_membership`|object|N/A|Dynamic|authored|`T1.SOCIAL.civic_standing` (kept apart)|The chosen community, its places, press and codes, and each room's code.|
|`T1.SOCIAL.community_membership.standing`|object|N/A|Dynamic|authored|A reputation he can lose is a plot handle|`{earned_by, vouched_by, cost_to_lose}`. Built on reliable conduct.|
|`T1.SOCIAL.agreement_style`|object|N/A|Dynamic|authored|`T3.EROS.desire_vector.group_position` (paired)|Fuzzy or legalistic, open or closed; `form`, `symmetry`, `veto`, `reopen_triggers`.|
|`T1.SOCIAL.risk_management_practice`|object|N/A|Dynamic|authored|Shared with L6|The safety rules he makes and keeps.|
|`T1.SOCIAL.risk_management_practice.risk_account`|enum|N/A|Dynamic|authored|Contextual|`{justification, excuse, informed_consent_frame, none}`.|
|`T1.SOCIAL.self_presentation`|object|N/A|Dynamic|authored|Contextual for L9 `exposure_shame`|The desirable self he builds for a public: apps, sites, a brand. Scopable by `{ref, value}`.|
|`T1.SOCIAL.pair_register`|array_object|N/A|Dynamic|authored|`T3.EROS.power_exchange` reads the same keying|List keyed by `character_id`: `{attachment_dimensions, pacing, rules, rule_gap}`.|
|`T1.SOCIAL.civic_standing`|object|N/A|Dynamic|authored|Class modifies it|`{category, rank_or_score, rights_held, what_can_be_taken, by_whom, exemptions, last_reranked}`.|
|`T1.SOCIAL.disclosure_posture`|object|N/A|Dynamic|authored|A view onto `knowledge_map`|Outness. List of `{audience, concealed_trait, strategy, stake}`, plus `stages`, `cost_ledger`, `hiding_incentive`. The L9 field of the same name is a second, separate field.|
|`T1.SOCIAL.voice_sheet`|object|N/A|Dynamic|authored|Contextual; Texture narrates the voice|`{register, dialect, native_pace: slow/even/fast, tic_with_reason, noticing_filter}`.|
|`T1.SOCIAL.voice_sheet.noticing_filter`|array_str|N/A|Dynamic|authored|Derived by hand from `sociology_stack` and `conditional_patterns`|What the character notices first.|

### Slice fields · L4 WILL

Layer paragraph: slice, L4 WILL.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T2.WILL.coping_strategy`|enum|N/A|Dynamic|authored|`MOD.COPING` reads it|Schmidt's five strategies. Sited on L4.|
|`T2.WILL.locus_of_control`|int|SC-10 (signed, -5 to +5)|Dynamic|authored|Contextual|-5 is fully internal. +5 is fully external.|
|`T2.WILL.system_stance`|enum|N/A|Dynamic|authored|A stated stance is a performance until a second source checks it|`{cog, believer, mask, bystander, resister}` plus `offstage_audience`.|
|`T2.WILL.resistance_mode`|array_str|N/A|Dynamic|authored|Contextual|Everyday tactics against a system: dress, space, passing, hidden worlds.|

### Slice fields · L5 WOUND

Layer paragraph: slice, L5 WOUND.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T2.WOUND.severity`|int|SC-12|Dynamic|authored|Read alias of `wound_score`: one number, two names|Same scale as `T2.WOUND.wound_score`. Even values only.|
|`T2.WOUND.triggers`|array_object|N/A|Static|authored|`FLG` states read the wound|Conditions that fire the wound. A trigger of type `minority_stress` fires it through the strain of belonging to a stigmatized group. Each entry takes an optional `setting_ref`.|
|`T2.WOUND.relational_refs`|array_object|N/A|Dynamic|authored|Contextual|`{kind, character_id, note}`. `kind` is ghost, revenant, mentor, shapeshifter, helper, opponent, sender, receiver, rival or beloved.|
|`T2.WOUND.wound_kind`|enum|N/A|Static|authored|Contextual|`{injury_suffered, error_committed, loss_unrecognized}` plus a note.|
|`T2.WOUND.wound_work`|enum|N/A|Dynamic|authored|The Villain-Arc Fork path (c)|`{none, avoided, reenacted_in_play, processed}` plus `terminating: bool`.|
|`T2.WOUND.mentor_state`|enum|N/A|Dynamic|authored|Contextual|`{present, absent, flawed}`.|
|`T2.WOUND.wound_belief_set`|array_str|N/A|Dynamic|authored|`T2.DRIVE.want_need.false_belief` links here, so one belief is stored once|The beliefs the wound installed.|

### Slice fields · L6 DRIVE

Layer paragraph: slice, L6 DRIVE.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T2.DRIVE.motivation_stack`|array_object|N/A|Dynamic|authored|Contextual|Ordered motives, stated versus real. Entries gain `audience`.|
|`T2.DRIVE.motivation_stack.audience`|array_object|N/A|Dynamic|authored|Contextual|`{who, named: bool}`.|
|`T2.DRIVE.drive_texture`|enum|N/A|Dynamic|authored|Contextual|The felt shape of the drive: more, risk, novelty, abundance. Where the drive is hyperfocus, write its fade as a state diff.|
|`T2.DRIVE.futurity_stance`|enum|N/A|Dynamic|authored|Contextual|`{planned, hoped, foreclosed, none, refused, horizon}`. Foreclosed means taken. Refused means he turns it down.|
|`T2.DRIVE.want_need`|object|N/A|Dynamic|authored|Step 3 check: an empty `need` on a Tier 2 or 3 character is incomplete|`{want, need, false_belief, need_kind: psychological/moral, cost, fusion_beat}`.|
|`T2.DRIVE.want_need.false_belief`|str|N/A|Dynamic|authored|Links to `wound_belief_set`|The belief the want rests on.|

### Slice fields · L7 ORIGIN

Layer paragraph: slice, L7 ORIGIN.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.ORIGIN.hereditary_predisposition`|str|N/A|Static|authored|Contextual|The trait inherited rather than formed (Egri's one homeless field).|
|`T3.ORIGIN.origin_disciplinary_formation`|str|N/A|Static|authored|Contextual|The institution that bonded and policed him: team, unit, club, church. Takes an optional `setting_ref`.|
|`T3.ORIGIN.system_exposure.layers`|array_object|N/A|Static|authored|Contextual|`{regime, years, trace_still_showing}`. `system_exposure` holds when he met the system.|
|`T3.ORIGIN.life_script`|object|N/A|Static for `source`, `version`. Dynamic for `stance`, `cost`.|authored|`T3.DESTINY.growth_requirement` may read `stance`|`{source, version, stance: accept/bend/refuse, cost}`.|

### Slice fields · L8 IMPRINT

Layer paragraph: slice, L8 IMPRINT.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.IMPRINT.secure_base_object`|str|N/A|Dynamic|authored|Canonical name. `primary_attachment_object` is the read alias.|The person or thing that serves as his secure base.|
|`T3.IMPRINT.attachment_dimensions`|object|SC-12|Dynamic|authored|Beside the scalar `attachment_style_score`|`{anxiety, avoidance}`. Each on SC-12 (Rule 4: no stated range, no formula).|
|`T3.IMPRINT.protest_behaviors`|array_str|N/A|Dynamic|authored|Contextual|How he protests when the bond is threatened.|
|`T3.IMPRINT.deactivating_strategies`|array_str|N/A|Dynamic|authored|Contextual|How he shuts the bond down.|
|`T3.IMPRINT.appeasement_strategies`|array_str|N/A|Dynamic|authored|Cross-reference `polarity_role`, so chosen submission is told apart from a defense|Self-erasure by submission.|
|`T3.IMPRINT.vandalism_event`|object|N/A|Static|authored|Paired with `T3.EROS.template_origin`|The dated early event that bent the lovemap. Sub-fields: `valence: taught/rewired/wounded/mixed`, `what_it_taught`, `what_it_still_powers`, `place`, `year`.|
|`T3.IMPRINT.somatic_archive`|str|N/A|Dynamic|authored|Contextual|What the body has learned to answer, built by habit.|
|`T3.IMPRINT.sexual_script_acquisition`|str|N/A|Static|authored|Read beside `T3.EROS.erotic_craft`|Who and what taught him what sex means, and at which level.|

### Slice fields · L9 EROS

Layer paragraph: slice, L9 EROS. `desire_vector` is the L9 parent; its group, fantasy and pleasure parts hang beneath it.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.EROS.arousal_curve`|object|SC-10 (amplitude, spasm_size)|Static for the curve. Dynamic for `concordance`, `refractory_minutes`.|authored|Contextual|`{spike/plateau/current, signature{amplitude, areas, speed, time_to_peak_min, spasm_size}, climb_rule, SES, SIS1, SIS2}`.|
|`T3.EROS.arousal_curve.concordance`|enum|N/A|Dynamic|authored|Contextual|`{aligned, decoupled, variable}`.|
|`T3.EROS.arousal_curve.refractory_minutes`|int|N/A (minutes)|Dynamic|authored|Contextual|Integer or null.|
|`T3.EROS.desire_vector.resolution_type`|enum|N/A|Static|authored|A null sexual channel makes `desire_vector` run non-terminating|`{terminating, additive}`.|
|`T3.EROS.desire_vector.group_size`|int|N/A (count)|Dynamic|authored|Contextual|The people in the group. 3 is a triad.|
|`T3.EROS.desire_vector.group_position`|object|N/A|Dynamic|authored|Pair with `agreement_style` and `compersion`|`{structure, standing, rule_setter, motives, script_followed}`.|
|`T3.EROS.desire_vector.triangle_position`|object|N/A|Dynamic|authored|Merged into `desire_vector` (slice 2.5.0; kept at 3.3.0)|The triangle parts, now under the group sub-fields.|
|`T3.EROS.desire_vector.compersion`|object|SC-10 (`level`)|Dynamic|authored|Contextual|`{level, kind: erotic/emotional/none, learned: bool}`.|
|`T3.EROS.desire_vector.fantasy_ledger`|array_object|N/A|Dynamic|authored|A fantasy that fails the consent or risk test stays fantasy|`{theme, told_to, acted: yes/no, real_vs_imagined}`.|
|`T3.EROS.desire_vector.desire_object`|enum|N/A|Dynamic|authored|Contextual|`{pleasure, activity, being_wanted, the_others_pleasure}`.|
|`T3.EROS.desire_vector.pleasure_evidence`|object|N/A|Dynamic|authored|Contextual|`{asks_for, accepts}`. Moved here from `resonance_profile`.|
|`T3.EROS.desire_vector.sex_creed`|enum|N/A|Dynamic|authored|Contextual|`{reproductive, romantic, pleasure, communication}`.|
|`T3.EROS.erotic_craft`|object|N/A|Dynamic. `training` is Static.|authored|Read beside `sexual_script_acquisition`|`{domains, level: novice/competent/expert/master, training: self/partner/teacher/tradition, flow_access: reliable/sometimes/blocked}`.|
|`T3.EROS.power_exchange`|array_object|N/A|Static per bond. `stage` is Dynamic.|authored|Keyed by `character_id`, like `pair_register`|`{scope, protocol, container, duration, stage: trial/trained/owned, function, role_integrity}`.|
|`T3.EROS.power_exchange.container`|object|N/A|Dynamic|authored|Touchstone 1:1, the bounded container|`{space, ritual, time_bound}`.|
|`T3.EROS.consent_posture`|object|N/A|Dynamic|authored|Distinct from `erotic_safety_precondition`|`scope`, `redefended_per_scene`, `enthusiasm_standard`, `precommitments`, `veto_points`, `limits{hard,soft}`, `recall`, `negotiation`, `signals`, `debrief`, and a consent model.|
|`T3.EROS.client_script`|enum|N/A|Dynamic|authored|Staged or paid intimacy|The scripted to spontaneous axis. Revisable mid-scene.|
|`T3.EROS.signal_fluency`|enum|N/A|Dynamic|authored|Contextual|`{fluent, functional, illiterate}`.|
|`T3.EROS.exposure_shame`|int|SC-12|Dynamic|authored|`DRV.truth_exposure_index` via the `shame_index` alias|Plus `direction` and `coping_style`. Slice 3.3.2 runs it on SC-12 to match `shame_index`.|
|`T3.EROS.role_shame`|int|SC-12|Dynamic|authored|Contextual|Plus `target`: erection, orgasm, pretense, receiving, initiative, femininity, other. Same SC-12 as its sibling.|
|`T3.EROS.erotic_safety_precondition_scope`|enum|N/A|Dynamic|authored|Contextual|`{internal, external}`.|
|`T3.EROS.risk_role`|enum|N/A|Dynamic|authored|Contextual|`{precondition, spark, trust_token}`. Reads `erotic_safety_precondition`.|
|`T3.EROS.template_origin`|object|N/A|Static|authored|Pointer to the L8 imprint event|Holds the lovemap design and `core_erotic_theme`.|
|`T3.EROS.orientation_dimensions`|object|SC-6 (Kinsey score per age)|Dynamic|authored|Contextual|`{behavior, desire, identity}` as three settings.|
|`T3.EROS.orientation_dimensions.attraction_channels`|object|SC-10 (each channel)|Dynamic|authored|A null sexual channel makes `desire_vector` run non-terminating|Sexual, romantic, sensual, platonic, aesthetic. Each 0 to 10 or null, with its own target gender.|
|`T3.EROS.charmed_circle_position`|array_object|N/A|Dynamic|authored|Reads beside `consent_posture` (adults only)|Per act: which side of the world's good-sex line it falls on.|
|`T3.EROS.resonance_profile`|object|N/A|Dynamic|authored|Contextual|What lands now, how it shifts, how it goes stale. Fantasy and practice as two registers, plus `type_tags`, `exceeds_type`.|
|`T3.EROS.polarity_role`|object|N/A|Dynamic|authored|`reversal_wish` feeds `shadow_content`|`{role: top/bottom/switch/dom/sub, reason, reversal_wish, history, stage: beginner/working/fluent}`.|
|`T3.EROS.polarity_role.reversal_wish`|str|N/A|Dynamic|authored|`T3.SHADOW.shadow_content` as denied_wish|The wish the role denies.|
|`T3.EROS.love_lust_cleft`|str|N/A|Dynamic|authored|Contextual|How he settles saintly love against sinful lust.|
|`T3.EROS.touch_rule`|object|N/A|Dynamic|authored|Beside `polarity_role`|`{gives, receives, no_touch: bool}`.|
|`T3.EROS.dissolution`|object|SC-10 (`depth`)|Dynamic|authored|Beside `polarity_role`|`{depth, with}`.|
|`T3.EROS.compartment_practice`|object|N/A|Dynamic|authored|The leak point feeds `shadow_content`|`{technique: schedule/dissociation/ritual_boundary/rule_set, reserved_act, leak_point}`.|
|`T3.EROS.disclosure_posture`|object|N/A|Dynamic|authored|Sexual-health register only|The L3 field of the same name holds outness. This one is a separate field.|

### Slice fields · L10 SHADOW

Layer paragraph: slice, L10 SHADOW.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.SHADOW.dark_triad`|object|SC-10 (each)|Dynamic|authored|Optional dial, null by default|`{narcissism, machiavellianism, psychopathy}`.|
|`T3.SHADOW.light_triad`|object|SC-10 (each)|Dynamic|authored|Optional dial, null by default|`{kantianism, humanism, faith_in_humanity}`.|
|`T3.SHADOW.moral_incongruence`|str|N/A|Dynamic|authored|A ready-made secret for scenes to test|The gap between what he believes about his desire and what he does.|
|`T3.SHADOW.disinhibition_context`|object|N/A|Dynamic|authored|Scope `shadow_driven` feeds Collapse Risk (CL18)|`{triggers, scope: self_permitted/shadow_driven, authentic: bool}`.|

### Slice fields · L11 DESTINY

Layer paragraph: slice, L11 DESTINY. Value sets for these three come from the cited books; the slice does not fix a list.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.DESTINY.arc_type`|str|N/A|Static|authored|The Villain-Arc Fork|Growth versus transformation (BVX.0196).|
|`T3.DESTINY.change_cause`|str|N/A|Static|authored|The Villain-Arc Fork|The four causes of change (BVX.0061).|
|`T3.DESTINY.catalyst_archetype`|str|N/A|Static|authored|Contextual|Growth pairing (BVX.0045).|
|`T3.DESTINY.rail_ref`|str|N/A|Static|authored|Theme (06) rails|The 06 rail the character argues for, so the character's side of the argument names its rail (IF catalog call 2, ruled 2026-10-05).|

### Slice fields · L12 FUNCTION

Layer paragraph: slice, L12 FUNCTION. The field list lives in the Dramatica integration protocol.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`T3.FUNC.convention_role`|object|N/A|Static|authored|Advisory. Never overrides `dramatica_archetype`.|`{genre_role, actant_slot: subject/object/sender/receiver/helper/opponent}`. Blank when no genre applies.|
|`T3.FUNC.necessity`|str|N/A|Static|authored|Protagonist rule: a Protagonist needs documented necessity|For example `satisfied`.|

### Slice fields · Shared sub-field

One sub-field serves several parents.

|Canonical Path|Type|Scale Class|Tag|Source|Consumer|Values and sub-fields|
|---|---|---|---|---|---|---|
|`setting_ref` (sub-field of `triggers`, `origin_class`, `origin_disciplinary_formation` entries)|object|N/A|Static|authored|Step 4: cite the S4, S6 or S8 entry|`{setting_id, S-layer}`. Optional.|
|`catalog_ref` (sub-field of `T3.ORIGIN.system_exposure.layers` `regime`, `T1.SOCIAL.civic_standing`, `T1.SOCIAL.community_membership`, `T3.ORIGIN.tech_level`)|str|N/A|Same as its parent|authored|Worldbuilding (05) catalog|The id of the 05 catalog entry that the free-text world field names (IF catalog call 3, ruled 2026-10-05). Optional.|

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
|Tag|Derived|

### DRV.social_legibility

|Field|Value|
|---|---|
|Canonical Path|`DRV.social_legibility`|
|Formula (internal)|`(T1.SOCIAL × 3) - ((T3.SHADOW.projection_tendency × 5) / 3)`|
|Input Constraints|projection_tendency must be multiple of 3|
|Output Space|Internal (0-60)|
|Source|`computed`|
|Tag|Derived|

### DRV.narrative_momentum

|Field|Value|
|---|---|
|Canonical Path|`DRV.narrative_momentum`|
|Formula (internal)|`(T2.DRIVE × 3) + ((T3.DESTINY.resistance_index × 5) / 2)`|
|Input Constraints|resistance_index must be even|
|Output Space|Internal (0-60)|
|Source|`computed`|
|Tag|Derived|

### DRV.stress_threshold

|Field|Value|
|---|---|
|Canonical Path|`DRV.stress_threshold`|
|Formula (internal)|`(T2.WILL × 3) - (T2.WOUND × 5)`|
|Input Constraints|None|
|Output Space|Internal, may go negative|
|Source|`computed`|
|Behavior|When negative, the character is operating past structural limit — function is maintained by qualitative stubbornness, not quantitative margin.|
|Tag|Derived|

### DRV.collapse_risk

|Field|Value|
|---|---|
|Canonical Path|`DRV.collapse_risk`|
|Formula (internal)|`((T2.WOUND × 5) + (T3.SHADOW.shadow_density × 5)) / 2`|
|Input Constraints|WOUND + shadow_density must be even (both even — enforced by constraints on both variables)|
|Output Space|Internal (0-60)|
|Source|`computed`|
|Tag|Derived|

### DRV.truth_exposure_index

|Field|Value|
|---|---|
|Canonical Path|`DRV.truth_exposure_index`|
|Formula (internal)|`(T1.SOCIAL × 3) + ((12 - T3.EROS.shame_index) × 5)`|
|Formula (display)|`T1.SOCIAL + max(0, 10 - T3.EROS.shame_index)` — slice 3.3.2 clamps the shame term at 0 on SC-12 (Chief, 10/4: "REC.")|
|Input Constraints|None|
|Output Space|Internal, uncapped (may exceed 60)|
|Source|`computed`|
|Behavior|Values exceeding 60 indicate the character's signal legibility exceeds the system's maximum containment threshold — the system cannot ignore this character.|
|Tag|Derived|

### DRV.expressive_range

|Field|Value|
|---|---|
|Canonical Path|`DRV.expressive_range`|
|Formula (display)|`12 - T3.EROS.armor_index`|
|Input Constraints|None|
|Output Space|Display `12 - armor_index`, 0 to 12. The internal mapping follows `armor_index` at SC-12. Slice 3.3.2 ruled the constant (Chief, 10/4: "Rick").|
|Source|`computed`|
|Behavior|The deliberate-signal metric — `DRV.truth_exposure_index` measures what leaks; this measures what the character can intentionally send. Low range with high TEI marks a character the system reads completely while they can express almost nothing.|
|Tag|Derived|

---

## Status Flags

A flag in PENDING stores the fabula `event_id` of the event that makes it true. A flag in FIRED_PRE_STORY stores the `event_id` of the story-entry marker (IF-00-04-06; IF catalog call 5, ruled 2026-10-05).

### FLG.shadow_denial

|Field|Value|
|---|---|
|Canonical Path|`FLG.shadow_denial`|
|Trigger|`T2.WOUND > 6 AND T3.SHADOW.projection_tendency >= 6 AND T3.IMPRINT.conditional_patterns contains "merit_earns_freedom"`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|
|Tag|Derived|

### FLG.truth_vulnerability

|Field|Value|
|---|---|
|Canonical Path|`FLG.truth_vulnerability`|
|Trigger|`T1.SOCIAL < 12 AND T3.FUNC.mc_problem_element = "Equity" AND T3.SHADOW.shadow_density > 6`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|
|Tag|Derived|

### FLG.optionlock_progression

|Field|Value|
|---|---|
|Canonical Path|`FLG.optionlock_progression`|
|Trigger|`T2.WOUND > 8 AND T3.DESTINY.resistance_index > 8 AND T3.FUNC.limit_type = "Optionlock"`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|
|Tag|Derived|

### FLG.earned_judgement

|Field|Value|
|---|---|
|Canonical Path|`FLG.earned_judgement`|
|Trigger|`T3.FUNC.dramatica_archetype = "Protagonist" AND T3.FUNC.story_outcome = "Failure" AND T2.WILL > 10`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|
|Tag|Derived|

### FLG.kinship_collapse

|Field|Value|
|---|---|
|Canonical Path|`FLG.kinship_collapse`|
|Trigger|`T3.IMPRINT.attachment_style_score > 6 AND T3.IMPRINT.primary_attachment_object = "deceased" AND T2.WOUND > 8`|
|States|`{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`|
|Source|`computed`|
|Tag|Derived|

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
|`STT.narrative_moment`|`str`|The Tracking (08) time code of the state (IF-00-08-03). Free text retires as an alias.|
|`STT.movement`|`str`|Retired 2026-10-05 (BOLO 102, IF catalog call 1). The M part of `narrative_moment` replaces it. Read alias for old records.|
|`STT.mc_distance_temporal`|`int`|Temporal distance from MC|
|`STT.mc_distance_narrative`|`int`|Causal distance from MC|
|`STT.base_record_version`|`str`|Version of base record|
|`STT.[any_layer_variable]`|(matches source type)|Modified value — replaces base on query|
|`STT.WILL_EFFECTIVE`|`int` SC-20|State-only field — temporary WILL reduction|
|`STT.state_note`|`str`|Prose justification for diff|

`STT.narrative_moment` holds the one Tracking address, for example `M2 · Q1 · S03 | bar.beat.tick`. Movement is M, sequence is Q, scene is S, and beat is `bar.beat` (IF catalog call 1, ruled 2026-10-05). `STT.mc_distance_temporal` and `STT.mc_distance_narrative` key to the same time code.

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
|1.1.0|2026-08-24|STATE #3 executed: added `T3.EROS.armor_index`, `T3.EROS.satisfaction_cycle_truncation`, `T3.EROS.erotic_safety_precondition`, `DRV.expressive_range` (L9 v2 propagation). `mc_problem_element` rename was already present (Phase 4). armor_index scale-class assignment was left open then. Assigned SC-12 in 1.2.0.|
|1.2.0|2026-10-04|BOLO 100 base batch 1 (B1 to B8, B13, B15), RULED Chief "REC.": frontmatter repaired to a multi-line block with `trunk` and `rung`, table-of-contents links repointed; the 05 copy is archived to `ShroomsQ/_ARCHIVE/ssot_legacy/` and this file is the one registry (B5); Registry Format gains the `Tag` row and the `object` types; new Slice Fields section adds 94 field rows from slice 3.3.1, each with tag, scale class, source and consumer (B6); Tag row added to every entry; `T3.EROS.armor_index` assigned SC-12 and the two "pending" lines deleted (B7); Ownership Rule with five pointer rows (B8); `attachment_style` and `intimacy_mode` value sets brought to the slice; `exposure_shame` and `role_shame` held at SC-12 to match `shame_index`, where the slice text says 0 to 10; the `10 - armor_index` constant is the slice's and gives a negative value at 11 or 12; dependency names fixed to real stems (B13).|
|1.2.1|2026-10-04|BOLO 100 TOUCH BATCH 1, Chief "REC.": field `narrative_invariant` renamed `touchstone` (TS-B3), one alias row kept.|
|1.2.2|2026-10-05|BOLO 102 batch C (Chief: "all recs"): C18, a note under the `REL` prefix (Chief decides each REL variable, check the three relational fields first); C19, a "Retire a variable" subsection under Registry Format.|
|1.3.0|2026-10-05|BOLO 102 stage 2 (Chief: "My word"): call 4, prefixes `SET` and `PLT`, ownership rows for 01, 02 (REL), 07 and 09, the storyform record owned by 04, the `touchstone` field holds the TS id, the alias table cited; call 1, `STT.narrative_moment` is the Tracking time code and `STT.movement` retires; call 2, `T3.DESTINY.rail_ref`; call 3, `catalog_ref` sub-field; call 5, PENDING and FIRED_PRE_STORY flags store the fabula `event_id`.|
