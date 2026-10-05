---
title: "Variable registry: reference"
type: "reference"
for: "A writer or designer looking up one variable, formula, flag or path"
does: "Lists every component and part of the variable registry"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_variable_registry.md"
source_version: "1.2.1"
---

**Who it's for:** a writer or designer looking up a variable · **What it does:** lists every variable, formula, flag and path in the registry · **Type:** reference

# Variable registry: reference

Source: `ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_variable_registry.md`, version 1.2.1, status canonical. The source sits on trunk BLACK at tier foundation, rung "standard · NASA four, ruled 2026-09-15 (BOLO 50)". It was last updated 2026-10-04. Dependencies: `ssot_00_base_60_number_system`, `ssot_02_character_systems_vertical_slice`. Why it exists: see the [concept](1-concept.md).

Entry shorthand: "SC-12" is a scale class from the [base 60 reference](../ssot_00_base_60_number_system/2-reference.md). Tag is Static, Dynamic or Derived. "Contextual" means the field feeds no formula and gives reference for other fields.

## Namespace Convention

Every variable path is `[DOMAIN].[LAYER_CODE].[variable_name]`.

### Domain Prefixes

| Prefix | Scope | Example |
|---|---|---|
| `T1` | Tier 1 primary attributes | `T1.CORE.base_value` |
| `T2` | Tier 2 secondary attributes | `T2.WOUND.wound_score` |
| `T3` | Tier 3 deep variable stacks | `T3.SHADOW.shadow_density` |
| `T3X` | Tier 3 extended sub-tables | `T3X.FUNC_EXT.mc_domain` |
| `DRV` | Derived statistics | `DRV.stress_threshold` |
| `FLG` | Status flags | `FLG.shadow_denial` |
| `AST` | Character Astrology | `AST.PERSONAL.sun_sign` |
| `STT` | State diff fields | `STT.wound_score` |
| `META` | Character metadata | `META.character_id` |
| `REL` | Relationship records | `REL.relationship_type` |
| `MOD` | Layer-Locked Module variables | `MOD.[MODULE_CODE].[variable_name]` |

### Layer Codes

| Code | Layer | Tier |
|---|---|---|
| `CORE` | L1 Cognitive/Psychological Mass | 1 |
| `VITAL` | L2 Physical/Energetic Presence | 1 |
| `SOCIAL` | L3 Relational Interface | 1 |
| `WILL` | L4 Psychological Resistance | 2 |
| `WOUND` | L5 Accumulated Damage | 2 |
| `DRIVE` | L6 Motivation Fuel | 2 |
| `ORIGIN` | L7 Birth Context | 3 |
| `IMPRINT` | L8 Emotional Conditioning | 3 |
| `EROS` | L9 Psycho-Sexual Conditioning | 3 |
| `SHADOW` | L10 Repressed Content | 3 |
| `DESTINY` | L11 Growth Vector | 3 |
| `FUNC` | L12 Narrative Function (core) | 3 |
| `FUNC_EXT` | L12 Dramatica Extended | 3 (sub-table) |

### Naming Rules

- Variable names use `snake_case`.
- Layer codes use `UPPER_CASE`.
- Domain prefixes use `UPPER_CASE` abbreviations.
- No variable name exceeds 30 characters.
- No two variables share a canonical name, whatever the namespace.
- Enum values use `snake_case` in brackets: `{secure, anxious, avoidant, disorganized}`.

## Ownership Rule

Each system owns its fields in its own doc. The registry holds the character fields (L1 to L12), derived statistics, flags, astrology and state-diff paths, and the `MOD` namespace. For every other system it holds one pointer row. It never copies a field, because a field kept in two places drifts.

| System | Owning doc | Owns |
|---|---|---|
| Setting (03) | `ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md` | S1 to S12 layer fields, including S12 FUNCTION |
| Plot (04) | `04_PLOT_SYSTEMS/📐 ssot_04_plot_system.md` and `📐 ssot_04_fabula.md` | P1 to P12 layer fields, including P12 FUNCTION. The fabula owns event ids. |
| Theme (07) | `06_THEME_SYSTEMS/📐 ssot_06_theme_system.md` | Theme fields and the argument record |
| Tracking (08) | `08_TRACKING_SYSTEMS/📐 ssot_08_tracking_system.md` | Time codes and story points |
| Worldbuilding (09) | `05_WORLDBUILDING_SYSTEMS/📐 ssot_05_worldbuilding_system.md` | Worldbuilding fields |

L12 FUNCTION is fed from the storyform. Its field list lives in `02_CHARACTER_SYSTEMS/🔮 ssot_02_dramatica_integration_protocol.md`. This registry mirrors it.

## Registry Format

Each variable entry has these fields.

| Field | Meaning |
|---|---|
| Canonical Path | Full namespace path |
| Display Name | Human-readable label |
| Type | `int`, `float`, `str`, `enum`, `array_str`, `array_enum`, `bool`, `object`, `array_object` |
| Scale Class | SC-N from the Base 60 SSOT, numeric variables only |
| Display Range | Human-facing value range |
| Constraint | Divisibility or parity constraint, if any |
| Default | Default value, if any |
| Source | `dramatica`, `astrology`, `authored`, `derived`, `computed` |
| Tag | Static (set once at origin), Dynamic (changes across the story, each change a state diff) or Derived (computed, never a diff). Copied from the slice table "Field tags · every field". A field with split sub-field tags says so. No variable ships without a Tag. |
| Feeds | Derived stats, flags or systems that consume it |
| Tier Min | Minimum tier that requires it |
| Behavior | One-sentence LoL-ability-style description |

The Slice Fields section uses one table row per field. Its columns are Canonical Path, Type, Scale Class, Tag, Source, Consumer, Values and sub-fields. The Behavior of each slice field lives in the slice layer paragraph it cites.

## Tier 1 Variables

### T1.CORE.basevalue

`T1.CORE.base_value`, CORE. int, SC-20, 0–20, default 10, source authored, tier min 1, tag Dynamic. Feeds `DRV.basic_damage_resistance` (via WILL) and `T2.WILL.base_value`. Behavior: governs mental skill defaults. High CORE thinks in frameworks; low CORE processes in fragments.

### T1.VITAL.basevalue

`T1.VITAL.base_value`, VITAL. int, SC-20, 0–20, default 10, authored, tier 1, Dynamic. Feeds `T2.DRIVE.base_value` and `DRV.narrative_momentum` (via DRIVE). Behavior: governs body precision. Above 12 the body is a primary instrument; below 8 physicality is a liability.

### T1.SOCIAL.basevalue

`T1.SOCIAL.base_value`, SOCIAL. int, SC-20, 0–20, default 10, authored, tier 1, Dynamic. Feeds `DRV.social_legibility` and `DRV.truth_exposure_index`. Behavior: governs how the world reads the character. Above 14 the character controls their signal; below 8 it leaks.

## Tier 2 Variables

### T2.WILL.basevalue

`T2.WILL.base_value`, WILL. int, SC-20, 0–20, default `= T1.CORE.base_value`, source derived from CORE (buyable ±1-3 at 5 pts per level). Tier min 2, Dynamic. Feeds `DRV.basic_damage_resistance`, `DRV.stress_threshold`, `FLG.earned_judgement`, `FLG.optionlock_progression`. Behavior: WILL above CORE is more stubborn than smart; below CORE the character understands but cannot sustain resistance.

### T2.WOUND.woundscore

`T2.WOUND.wound_score`, WOUND. int, SC-12, 0–12, constraint even values only {0, 2, 4, 6, 8, 10, 12}, default 0. It is authored from history (not purchased), tier 2, Dynamic. Feeds `DRV.basic_damage_resistance`, `DRV.stress_threshold`, `DRV.collapse_risk`, `FLG.shadow_denial`, `FLG.optionlock_progression`, `FLG.kinship_collapse`. Behavior: records damage that failed to resolve. At 12 the character reaches the functional collapse threshold.

### T2.DRIVE.basevalue

`T2.DRIVE.base_value`, DRIVE. int, SC-20, 0–20, default `= T1.VITAL.base_value`, derived from VITAL (buyable at 3 pts per level), tier 2, Dynamic. Feeds `DRV.narrative_momentum`. Behavior: DRIVE equal to VITAL is ambition-driven; below VITAL is meaning-driven.

## Tier 3 Variables: L7 ORIGIN

All L7 entries: source authored, tier min 3, tag Static, default none.

### T3.ORIGIN.originclass

`T3.ORIGIN.origin_class`. enum `{institutional, professional, working, working_criminal_adjacent, criminal, subsistence, unknown}`. Feeds L8, L9, L10 as context. Behavior: the socioeconomic stratum the character came from.

### T3.ORIGIN.originstability

`T3.ORIGIN.origin_stability`. int, SC-12, 0–12. Context for `T2.WOUND.wound_score` baseline. 0 is chaos; 12 is complete stability.

### T3.ORIGIN.familycoherence

`T3.ORIGIN.family_coherence`. int, SC-12, 0–12. Context for `T3.IMPRINT.attachment_style_score`. 0 is a fragmented or absent family; 12 a unified family with clear roles.

### T3.ORIGIN.originwoundseed

`T3.ORIGIN.origin_wound_seed`. int, SC-12, 0–12. Baseline input for `T2.WOUND.wound_score`. 0 is a protective origin; 12 an origin that is itself the primary wound.

### T3.ORIGIN.techlevel

`T3.ORIGIN.tech_level`. int, SC-12, 0–12. Contextual. The technological sophistication of the formative environment.

### T3.ORIGIN.systemexposure

`T3.ORIGIN.system_exposure`. enum `{none, early_pre_awareness, early_aware, mid_integration, late_integration, institutional_native}`. Context for L11 DESTINY and Movement assignment. Defines when the character first met systemic forces.

## Tier 3 Variables: L8 IMPRINT

All L8 entries: tier min 3, default none unless stated.

### T3.IMPRINT.attachmentstyle

`T3.IMPRINT.attachment_style`. enum `{secure, anxious, avoidant, fearful_avoidant}` (four-way, slice 2.1.0). Legacy values `secure_anxious`, `secure_avoidant`, `disorganized` stay readable. A locked record keeps its value. Source authored, informed by `AST.PERSONAL.moon_sign`. Feeds `FLG.kinship_collapse`. Tag Static. The default relational wiring.

### T3.IMPRINT.attachmentstylescore

`T3.IMPRINT.attachment_style_score`, Attachment Intensity. int, SC-12, 0–12, authored, Static. Feeds `FLG.kinship_collapse`. 0 is relationally flat; 12 bonds at maximum intensity.

### T3.IMPRINT.emotionalrange

`T3.IMPRINT.emotional_range`. int, SC-12, 0–12, authored, Static. Context for behavioral texture. 0 is emotionally flat; 12 spans euphoria to devastation.

### T3.IMPRINT.conditionalpatterns

`T3.IMPRINT.conditional_patterns`. array_str, freeform (e.g. `merit_earns_freedom`, `loyalty_to_kinship`), default `[]`, authored, Static. Feeds `FLG.shadow_denial`. The if/then rules the character runs on.

### T3.IMPRINT.imprintflexibility

`T3.IMPRINT.imprint_flexibility`. int, SC-12, 0–12, authored, Static. Context for arc resistance. 0 is immovable conditioning; 12 rewires easily.

### T3.IMPRINT.primaryattachmentobject

`T3.IMPRINT.primary_attachment_object`, a read alias of `secure_base_object` (slice 2.1.0). str: a character ID, `deceased`, `absent` or `none`. Default `none`. Authored. Feeds `FLG.kinship_collapse` and relational tracking. Tag Dynamic. The person the character orients their relational system around.

## Tier 3 Variables: L9 EROS

All L9 entries: tier min 3, default none unless stated.

### T3.EROS.eroticblueprinttype

`T3.EROS.erotic_blueprint_type`. enum `{kinesthetic, sensual, energetic, sexual, shapeshifter}`. Authored, informed by `AST.PERSONAL.venus_sign`. Context for intimacy behavior. Static. The primary channel of erotic connection.

### T3.EROS.desirevector

`T3.EROS.desire_vector`. int, SC-12, 0–12, authored, Dynamic. Contextual. 0 is absent or suppressed desire; 12 is desire as the dominant driver.

### T3.EROS.shameindex

`T3.EROS.shame_index`, a read alias of `exposure_shame` (slice 2.2.0). int, SC-12, 0–12, authored, Dynamic. Feeds `DRV.truth_exposure_index`. 0 is no shame; 12 is shame as the dominant filter on intimate expression.

### T3.EROS.armorindex

`T3.EROS.armor_index`. int, SC-12, 0–12, authored (adopted 2026-08-15, L9 v2 ingest, Walker PSY.01; propagated 2026-08-24). Feeds `DRV.expressive_range`. Dynamic. Chronic protective constriction. Independent of shame: low shame with high armor is the armored-but-readable paradox.

### T3.EROS.satisfactioncycletruncation

`T3.EROS.satisfaction_cycle_truncation`. enum `{none, yield, push, reach, grasp, pull}`, default `none`. Authored (adopted 2026-08-15, Walker and Bainbridge-Cohen). Contextual: the somatic mechanism for `T2.WOUND.wound_score`. Static. Names the phase of the yield, push, reach, grasp, pull cycle where engagement breaks.

### T3.EROS.eroticsafetyprecondition

`T3.EROS.erotic_safety_precondition`. str, freeform (e.g. `control`, `privacy`, `trust`, `ritual`). Authored (introduced 2026-08-15, Walker Invariant 4). Context for intimacy behavior and arc design. Dynamic. What the nervous system must register before pleasure is accessible.

### T3.EROS.intimacymode

`T3.EROS.intimacy_mode`. enum `{partnered_merge, parallel_presence, solo_directed, bounded_no_strings}` (slice 3.2.0, CL2). Legacy values `face_to_face`, `performance`, `pursuit`, `dissolution`, `withholding` stay readable. A list of `{ref, value}` scopes it per partner or audience. Authored, Dynamic. How the character structures closeness.

### T3.EROS.sourceconfidence

`T3.EROS.source_confidence`. enum `{canonical, inferred, speculative}`, default `inferred`, authored, Static. A validation flag: `inferred` values need follow-up extraction.

## Tier 3 Variables: L10 SHADOW

All L10 entries: tier min 3, default none unless stated, authored.

### T3.SHADOW.shadowdensity

`T3.SHADOW.shadow_density`. int, SC-12, 0–12, constraint even only (must match WOUND parity). Informed by `AST` debilitated planets and 12th House contents. Feeds `DRV.collapse_risk` and `DRV.social_legibility` (via projection_tendency). Dynamic.

### T3.SHADOW.projectiontendency

`T3.SHADOW.projection_tendency`. int, SC-12, 0–12, constraint multiples of 3 only {0, 3, 6, 9, 12}. Feeds `DRV.social_legibility` and `FLG.shadow_denial`. Dynamic. At 12 the character cannot tell self-generated distress from external harm.

### T3.SHADOW.regressionpattern

`T3.SHADOW.regression_pattern`. enum `{control_escalation, withdrawal, dissociation, aggression, performance, people_pleasing, intellectualization, substance_seeking}`. Feeds behavior under stress. Static. What the character does when shadow content activates.

### T3.SHADOW.shadowcontent

`T3.SHADOW.shadow_content`. array_str, freeform, default `[]`. Informed by `AST` 12th House and Pluto aspects. Contextual for flag triggers. Dynamic. Each entry is one thing the character cannot face about themselves.

## Tier 3 Variables: L11 DESTINY

All L11 entries: tier min 3, authored, default none.

### T3.DESTINY.growthaxis

`T3.DESTINY.growth_axis`. str. Informed by `AST.STRUCTURAL.uranus_sign`. Context for arc design. Static. The direction the arc demands.

### T3.DESTINY.resistanceindex

`T3.DESTINY.resistance_index`. int, SC-12, 0–12, constraint even only. Informed by `AST` Jupiter-Saturn aspects. Feeds `DRV.narrative_momentum`, `FLG.optionlock_progression`. Dynamic. At 12 the character opposes their own solution.

### T3.DESTINY.soulevolutionarchetype

`T3.DESTINY.soul_evolution_archetype`. str. Contextual. Static. Names the kind of transformation (tactical_disruptor, wounded_healer, fallen_idealist).

### T3.DESTINY.karmicmemory

`T3.DESTINY.karmic_memory`. str. Contextual. Static. The deep-pattern belief the arc will challenge or destroy.

### T3.DESTINY.growthrequirement

`T3.DESTINY.growth_requirement`. str. Informed by Dramatica MC Solution. Feeds arc design and `FLG.earned_judgement`. Static. Stated as an action ("accept_asymmetry", "release_control", "trust_without_proof").

## Tier 3 Variables: L12 FUNCTION

L12 entries: tier min 3 unless stated, tag Static.

### T3.FUNC.dramaticaarchetype

`T3.FUNC.dramatica_archetype`. enum `{Protagonist, Antagonist, Guardian, Contagonist, Reason, Emotion, Sidekick, Skeptic, Complex}`. Source dramatica. Feeds `FLG.earned_judgement`.

### T3.FUNC.mcproblemelement

`T3.FUNC.mc_problem_element`. str, dramatica. Feeds `FLG.truth_vulnerability` and Character Astrology Moon derivation. The core narrative friction. Renamed from `motivation_element` (Phase 4 schema clarification).

### T3.FUNC.methodologyelement

`T3.FUNC.methodology_element`. str, dramatica. Feeds Character Astrology Mercury derivation.

### T3.FUNC.evaluationelement

`T3.FUNC.evaluation_element`. str, dramatica. Contextual.

### T3.FUNC.purposeelement

`T3.FUNC.purpose_element`. str, dramatica. Feeds Character Astrology Venus derivation.

### T3.FUNC.touchstone

`T3.FUNC.touchstone`. str, authored. Alias `narrative_invariant` (old name, read alias for old ingests, renamed BOLO 100). Feeds as a structural constraint on all downstream story development.

### T3.FUNC.storyoutcome

`T3.FUNC.story_outcome`. enum `{Success, Failure}`, dramatica. Feeds `FLG.earned_judgement` and Character Astrology Pluto derivation.

### T3.FUNC.storyjudgement

`T3.FUNC.story_judgement`. enum `{Good, Bad}`, dramatica. Feeds `FLG.earned_judgement` and Character Astrology Pluto derivation.

### T3.FUNC.limittype

`T3.FUNC.limit_type`. enum `{Timelock, Optionlock}`, dramatica. Feeds `FLG.optionlock_progression`.

### T3.FUNC.resolve

`T3.FUNC.resolve`. enum `{Change, Steadfast}`, dramatica. Feeds Character Astrology (mutable versus fixed emphasis) and arc design.

### Tier 2 L12 Format

A Tier 2 character's L12 uses a different variable set: the next three entries.

### T3.FUNC.tier

`T3.FUNC.tier`. int `{1, 2, 3}`. Static.

### T3.FUNC.elementsignature

`T3.FUNC.element_signature`. array_str of 2-4 Dramatica element names. Authored from the Dramatica element vocabulary. Tier min 2. Static.

### T3.FUNC.relationalroles

`T3.FUNC.relational_roles`. array of `{target: str, role: enum}`. Roles `{mirror, foil, catalyst, threshold_guardian, herald, mentor, trickster, shapeshifter, anchor}`. Authored. Tier min 2. Static.

## L12 DRAMATICA EXTENDED

The extended sub-table. Type is `str` unless noted. Source dramatica, tier min 3, tag Static for all: the storyform is locked, and a revision makes a new version.

| Path | Display name |
|---|---|
| `T3X.FUNC_EXT.storyform_id` | Storyform ID |
| `.mc_domain`, `.mc_concern`, `.mc_issue`, `.mc_counterpoint` | MC Domain, Concern, Issue, Counterpoint |
| `.mc_problem`, `.mc_solution`, `.mc_symptom`, `.mc_response` | MC Problem, Solution, Symptom, Response |
| `.mc_unique_ability`, `.mc_critical_flaw`, `.mc_benchmark` | MC Unique Ability, Critical Flaw, Benchmark |
| `.mc_focus`, `.mc_direction` | MC Focus, Direction |
| `.mc_signpost_1` to `.mc_signpost_4` | MC Signpost 1 to 4 |
| `.motivation_quad`, `.methodology_quad`, `.evaluation_quad`, `.purpose_quad` | Quads (array) |
| `.os_domain`, `.os_concern`, `.os_issue`, `.os_problem` | OS Domain, Concern, Issue, Problem |
| `.ic_domain`, `.ic_concern` | IC Domain, Concern |
| `.rs_domain`, `.rs_concern` | RS Domain, Concern |

Each path above starts with `T3X.FUNC_EXT`.

## Slice Fields (added in 1.2.0)

The slice reached 3.3.1. These are the fields it added after the first registry, one row each, in layer order, each with a Tag. `shadow_content` entries also carry a `kind`: denied_wish, assigned_by_world, feared_double, standing_alarm, scrubbed_bond or imposed_self_image. All slice fields have source authored. Columns below: path, type (scale class), tag, consumer, values.

### Slice fields · L1 CORE

- `T1.CORE.psychology_stack`: object, Dynamic. Egri text checklist: moral standards, ambition, frustrations, temperament, attitude to life, complexes, extrovert or introvert, abilities, qualities, IQ. Context under `T1.CORE.base_value`.
- `T1.CORE.identity_frame`: object, Dynamic. Gender persona, orientation label, era category, gender script per audience. Context for `T3.EROS.orientation_dimensions`.
- `T1.CORE.identity_frame.assigned_labels`: array_object, Dynamic. `{label, by, year, accepted}`; `by` is law, medicine, church, state, buyer, family or peers. Context for `T1.SOCIAL.civic_standing`.
- `T1.CORE.neurotype`: object. Static for `label`, `known_to_self`; Dynamic for `masked_by`, `attention_pattern`. `{label, known_to_self, masked_by: novelty/effort/none, attention_pattern: hyperfocus/scattered/mixed}`. Store it as one cause among others. Read by the `T2.DRIVE.drive_texture` fade note.

### Slice fields · L2 VITAL

- `T1.VITAL.physiology_stack`: object, Dynamic. Egri checklist: heredity, appearance, defects, posture, health. Heredity sits at L7. Context under `T1.VITAL.base_value`.
- `T1.VITAL.body_capital`: object, Dynamic. `{price_factors, window{curve,start_age,end_age}, venue_tier, trust_signal, working_body_gap, embodied_cost}`. Adults only.

### Slice fields · L3 SOCIAL

Four fields (`intimacy_mode`, `disclosure_posture`, `love_lust_cleft`, `self_presentation`) take a list of `{ref, value}`. The bare value is the default.

- `T1.SOCIAL.sociology_stack`: object, Dynamic. Egri checklist: class, occupation, education, home life, political affiliation. `voice_sheet.noticing_filter` derives from it.
- `T1.SOCIAL.circumplex`: object, SC-10 signed -5 to +5, Dynamic. `{agency, communion}`. Agency runs yielding to dominant; communion runs cold to warm. Optional dial, null by default.
- `T1.SOCIAL.knowledge_map`: array_object, Dynamic. Per relationship: what each knows, what each knows the other knows, who may claim not to know. Read by `T3.EROS.consent_posture`. L3 `disclosure_posture` is a view onto it.
- `T1.SOCIAL.knowledge_map.cover`: array_object, Dynamic. `{kind: overcompensation/double_life/passing/hidden_in_plain_view, sized_to, cost}`. Feeds `T3.SHADOW.shadow_content` for a double life.
- `T1.SOCIAL.community_membership`: object, Dynamic. The chosen community, its places, press and codes, and each room's code. Kept apart from `civic_standing`.
- `T1.SOCIAL.community_membership.standing`: object, Dynamic. `{earned_by, vouched_by, cost_to_lose}`. A reputation he can lose is a plot handle.
- `T1.SOCIAL.agreement_style`: object, Dynamic. Fuzzy or legalistic, open or closed; `form`, `symmetry`, `veto`, `reopen_triggers`. Paired with `T3.EROS.desire_vector.group_position`.
- `T1.SOCIAL.risk_management_practice`: object, Dynamic. The safety rules he makes and keeps. Shared with L6.
- `T1.SOCIAL.risk_management_practice.risk_account`: enum `{justification, excuse, informed_consent_frame, none}`, Dynamic.
- `T1.SOCIAL.self_presentation`: object, Dynamic. The desirable self he builds for a public: apps, sites, a brand. Scopable by `{ref, value}`. Context for L9 `exposure_shame`.
- `T1.SOCIAL.pair_register`: array_object, Dynamic. Keyed by `character_id`: `{attachment_dimensions, pacing, rules, rule_gap}`. `T3.EROS.power_exchange` reads the same keying.
- `T1.SOCIAL.civic_standing`: object, Dynamic. `{category, rank_or_score, rights_held, what_can_be_taken, by_whom, exemptions, last_reranked}`. Class modifies it.
- `T1.SOCIAL.disclosure_posture`: object, Dynamic. Outness. List of `{audience, concealed_trait, strategy, stake}`, plus `stages`, `cost_ledger`, `hiding_incentive`. The L9 field of the same name is separate.
- `T1.SOCIAL.voice_sheet`: object, Dynamic. `{register, dialect, native_pace: slow/even/fast, tic_with_reason, noticing_filter}`. Texture narrates the voice.
- `T1.SOCIAL.voice_sheet.noticing_filter`: array_str, Dynamic. What the character notices first. Derived by hand from `sociology_stack` and `conditional_patterns`.

### Slice fields · L4 WILL

- `T2.WILL.coping_strategy`: enum, Dynamic. Schmidt's five strategies. Sited on L4. `MOD.COPING` reads it.
- `T2.WILL.locus_of_control`: int, SC-10 signed -5 to +5, Dynamic. -5 fully internal; +5 fully external.
- `T2.WILL.system_stance`: enum `{cog, believer, mask, bystander, resister}` plus `offstage_audience`, Dynamic. A stated stance is a performance until a second source checks it.
- `T2.WILL.resistance_mode`: array_str, Dynamic. Everyday tactics against a system: dress, space, passing, hidden worlds.

### Slice fields · L5 WOUND

- `T2.WOUND.severity`: int, SC-12, Dynamic. Read alias of `wound_score`: one number, two names. Even values only.
- `T2.WOUND.triggers`: array_object, Static. Conditions that fire the wound. A `minority_stress` trigger fires through the strain of belonging to a stigmatized group. Each entry takes an optional `setting_ref`. `FLG` states read the wound.
- `T2.WOUND.relational_refs`: array_object, Dynamic. `{kind, character_id, note}`. `kind` is ghost, revenant, mentor, shapeshifter, helper, opponent, sender, receiver, rival or beloved.
- `T2.WOUND.wound_kind`: enum `{injury_suffered, error_committed, loss_unrecognized}` plus a note, Static.
- `T2.WOUND.wound_work`: enum `{none, avoided, reenacted_in_play, processed}` plus `terminating: bool`, Dynamic. Read by the Villain-Arc Fork path (c).
- `T2.WOUND.mentor_state`: enum `{present, absent, flawed}`, Dynamic.
- `T2.WOUND.wound_belief_set`: array_str, Dynamic. The beliefs the wound installed. `T2.DRIVE.want_need.false_belief` links here, so one belief is stored once.

### Slice fields · L6 DRIVE

- `T2.DRIVE.motivation_stack`: array_object, Dynamic. Ordered motives, stated versus real. Entries gain `audience`.
- `T2.DRIVE.motivation_stack.audience`: array_object, Dynamic. `{who, named: bool}`.
- `T2.DRIVE.drive_texture`: enum, Dynamic. The felt shape of the drive: more, risk, novelty, abundance. For hyperfocus, write its fade as a state diff.
- `T2.DRIVE.futurity_stance`: enum `{planned, hoped, foreclosed, none, refused, horizon}`, Dynamic. Foreclosed means taken. Refused means he turns it down.
- `T2.DRIVE.want_need`: object, Dynamic. `{want, need, false_belief, need_kind: psychological/moral, cost, fusion_beat}`. Step 3 check: an empty `need` on a Tier 2 or 3 character is incomplete.
- `T2.DRIVE.want_need.false_belief`: str, Dynamic. The belief the want rests on. Links to `wound_belief_set`.

### Slice fields · L7 ORIGIN

- `T3.ORIGIN.hereditary_predisposition`: str, Static. The trait inherited rather than formed (Egri's one homeless field).
- `T3.ORIGIN.origin_disciplinary_formation`: str, Static. The institution that bonded and policed him: team, unit, club, church. Optional `setting_ref`.
- `T3.ORIGIN.system_exposure.layers`: array_object, Static. `{regime, years, trace_still_showing}`. `system_exposure` holds when he met the system.
- `T3.ORIGIN.life_script`: object. Static for `source`, `version`; Dynamic for `stance`, `cost`. `{source, version, stance: accept/bend/refuse, cost}`. `T3.DESTINY.growth_requirement` may read `stance`.

### Slice fields · L8 IMPRINT

- `T3.IMPRINT.secure_base_object`: str, Dynamic. The canonical name. `primary_attachment_object` is the read alias.
- `T3.IMPRINT.attachment_dimensions`: object, SC-12, Dynamic. `{anxiety, avoidance}`, each SC-12 (Rule 4: no stated range, no formula). Sits beside `attachment_style_score`.
- `T3.IMPRINT.protest_behaviors`: array_str, Dynamic. How he protests when the bond is threatened.
- `T3.IMPRINT.deactivating_strategies`: array_str, Dynamic. How he shuts the bond down.
- `T3.IMPRINT.appeasement_strategies`: array_str, Dynamic. Self-erasure by submission. Cross-reference `polarity_role`, so chosen submission is told apart from a defense.
- `T3.IMPRINT.vandalism_event`: object, Static. The dated early event that bent the lovemap. `valence: taught/rewired/wounded/mixed`, `what_it_taught`, `what_it_still_powers`, `place`, `year`. Paired with `T3.EROS.template_origin`.
- `T3.IMPRINT.somatic_archive`: str, Dynamic. What the body has learned to answer, built by habit.
- `T3.IMPRINT.sexual_script_acquisition`: str, Static. Who and what taught him what sex means, and at which level. Read beside `T3.EROS.erotic_craft`.

### Slice fields · L9 EROS

`desire_vector` is the L9 parent. Its group, fantasy and pleasure parts hang beneath it.

- `T3.EROS.arousal_curve`: object, SC-10 (amplitude, spasm_size). Static for the curve; Dynamic for `concordance`, `refractory_minutes`. `{spike/plateau/current, signature{amplitude, areas, speed, time_to_peak_min, spasm_size}, climb_rule, SES, SIS1, SIS2}`.
- `T3.EROS.arousal_curve.concordance`: enum `{aligned, decoupled, variable}`, Dynamic.
- `T3.EROS.arousal_curve.refractory_minutes`: int (minutes) or null, Dynamic.
- `T3.EROS.desire_vector.resolution_type`: enum `{terminating, additive}`, Static. A null sexual channel makes `desire_vector` run non-terminating.
- `T3.EROS.desire_vector.group_size`: int (count), Dynamic. The people in the group. 3 is a triad.
- `T3.EROS.desire_vector.group_position`: object, Dynamic. `{structure, standing, rule_setter, motives, script_followed}`. Pair with `agreement_style` and `compersion`.
- `T3.EROS.desire_vector.triangle_position`: object, Dynamic. Merged into `desire_vector` (slice 2.5.0; kept at 3.3.0).
- `T3.EROS.desire_vector.compersion`: object, SC-10 (`level`), Dynamic. `{level, kind: erotic/emotional/none, learned: bool}`.
- `T3.EROS.desire_vector.fantasy_ledger`: array_object, Dynamic. `{theme, told_to, acted: yes/no, real_vs_imagined}`. A fantasy that fails the consent or risk test stays fantasy.
- `T3.EROS.desire_vector.desire_object`: enum `{pleasure, activity, being_wanted, the_others_pleasure}`, Dynamic.
- `T3.EROS.desire_vector.pleasure_evidence`: object `{asks_for, accepts}`, Dynamic. Moved here from `resonance_profile`.
- `T3.EROS.desire_vector.sex_creed`: enum `{reproductive, romantic, pleasure, communication}`, Dynamic.
- `T3.EROS.erotic_craft`: object. Dynamic; `training` is Static. `{domains, level: novice/competent/expert/master, training: self/partner/teacher/tradition, flow_access: reliable/sometimes/blocked}`.
- `T3.EROS.power_exchange`: array_object. Static per bond; `stage` is Dynamic. `{scope, protocol, container, duration, stage: trial/trained/owned, function, role_integrity}`. Keyed by `character_id`, like `pair_register`.
- `T3.EROS.power_exchange.container`: object, Dynamic. `{space, ritual, time_bound}`. Touchstone 1:1, the bounded container.
- `T3.EROS.consent_posture`: object, Dynamic. `scope`, `redefended_per_scene`, `enthusiasm_standard`, `precommitments`, `veto_points`, `limits{hard,soft}`, `recall`, `negotiation`, `signals`, `debrief`, and a consent model. Distinct from `erotic_safety_precondition`.
- `T3.EROS.client_script`: enum, Dynamic. The scripted to spontaneous axis. Revisable mid-scene. For staged or paid intimacy.
- `T3.EROS.signal_fluency`: enum `{fluent, functional, illiterate}`, Dynamic.
- `T3.EROS.exposure_shame`: int, SC-12, Dynamic. Plus `direction` and `coping_style`. Slice 3.3.2 runs it on SC-12 to match `shame_index`. Feeds `DRV.truth_exposure_index` via the `shame_index` alias.
- `T3.EROS.role_shame`: int, SC-12, Dynamic. Plus `target`: erection, orgasm, pretense, receiving, initiative, femininity, other.
- `T3.EROS.erotic_safety_precondition_scope`: enum `{internal, external}`, Dynamic.
- `T3.EROS.risk_role`: enum `{precondition, spark, trust_token}`, Dynamic. Reads `erotic_safety_precondition`.
- `T3.EROS.template_origin`: object, Static. The lovemap design and `core_erotic_theme`. Points to the L8 imprint event.
- `T3.EROS.orientation_dimensions`: object, SC-6 (Kinsey score per age), Dynamic. `{behavior, desire, identity}` as three settings.
- `T3.EROS.orientation_dimensions.attraction_channels`: object, SC-10 per channel, Dynamic. Sexual, romantic, sensual, platonic, aesthetic. Each 0 to 10 or null, with its own target gender.
- `T3.EROS.charmed_circle_position`: array_object, Dynamic. Per act: which side of the world's good-sex line it falls on. Adults only. Read beside `consent_posture`.
- `T3.EROS.resonance_profile`: object, Dynamic. What lands now, how it shifts, how it goes stale. Fantasy and practice as two registers, plus `type_tags`, `exceeds_type`.
- `T3.EROS.polarity_role`: object, Dynamic. `{role: top/bottom/switch/dom/sub, reason, reversal_wish, history, stage: beginner/working/fluent}`.
- `T3.EROS.polarity_role.reversal_wish`: str, Dynamic. The wish the role denies. Feeds `T3.SHADOW.shadow_content` as denied_wish.
- `T3.EROS.love_lust_cleft`: str, Dynamic. How he settles saintly love against sinful lust.
- `T3.EROS.touch_rule`: object `{gives, receives, no_touch: bool}`, Dynamic. Beside `polarity_role`.
- `T3.EROS.dissolution`: object `{depth, with}`, SC-10 (`depth`), Dynamic. Beside `polarity_role`.
- `T3.EROS.compartment_practice`: object, Dynamic. `{technique: schedule/dissociation/ritual_boundary/rule_set, reserved_act, leak_point}`. The leak point feeds `shadow_content`.
- `T3.EROS.disclosure_posture`: object, Dynamic. Sexual-health register only. The L3 field of the same name holds outness.

### Slice fields · L10 SHADOW

- `T3.SHADOW.dark_triad`: object, SC-10 each, Dynamic. `{narcissism, machiavellianism, psychopathy}`. Optional dial, null by default.
- `T3.SHADOW.light_triad`: object, SC-10 each, Dynamic. `{kantianism, humanism, faith_in_humanity}`. Optional dial, null by default.
- `T3.SHADOW.moral_incongruence`: str, Dynamic. The gap between what he believes about his desire and what he does. A ready-made secret for scenes to test.
- `T3.SHADOW.disinhibition_context`: object, Dynamic. `{triggers, scope: self_permitted/shadow_driven, authentic: bool}`. Scope `shadow_driven` feeds Collapse Risk (CL18).

### Slice fields · L11 DESTINY

Value sets for these three come from the cited books. The slice fixes no list.

- `T3.DESTINY.arc_type`: str, Static. Growth versus transformation (BVX.0196). Read by the Villain-Arc Fork.
- `T3.DESTINY.change_cause`: str, Static. The four causes of change (BVX.0061). Read by the Villain-Arc Fork.
- `T3.DESTINY.catalyst_archetype`: str, Static. Growth pairing (BVX.0045).

### Slice fields · L12 FUNCTION

The field list lives in the Dramatica integration protocol.

- `T3.FUNC.convention_role`: object, Static. `{genre_role, actant_slot: subject/object/sender/receiver/helper/opponent}`. Blank when no genre applies. Advisory. Never overrides `dramatica_archetype`.
- `T3.FUNC.necessity`: str, Static. For example `satisfied`. Protagonist rule: a Protagonist needs documented necessity.

### Slice fields · Shared sub-field

- `setting_ref`: object, Static. A sub-field of `triggers`, `origin_class` and `origin_disciplinary_formation` entries. `{setting_id, S-layer}`. Optional. Step 4: cite the S4, S6 or S8 entry.

## Derived Statistics

All derived stats compute in internal (0-60) space per the Base 60 SSOT. Source `computed`, tag Derived.

### DRV.basicdamageresistance

`DRV.basic_damage_resistance`. Formula `(T2.WILL × 3) - ((T2.WOUND × 5) / 2)`. WOUND must be even. Output internal 0-60, may go negative.

### DRV.sociallegibility

`DRV.social_legibility`. Formula `(T1.SOCIAL × 3) - ((T3.SHADOW.projection_tendency × 5) / 3)`. projection_tendency must be a multiple of 3. Output internal 0-60.

### DRV.narrativemomentum

`DRV.narrative_momentum`. Formula `(T2.DRIVE × 3) + ((T3.DESTINY.resistance_index × 5) / 2)`. resistance_index must be even. Output internal 0-60.

### DRV.stressthreshold

`DRV.stress_threshold`. Formula `(T2.WILL × 3) - (T2.WOUND × 5)`. No constraints. Output internal, may go negative. When negative, the character works past the structural limit, held up by stubbornness, not margin.

### DRV.collapserisk

`DRV.collapse_risk`. Formula `((T2.WOUND × 5) + (T3.SHADOW.shadow_density × 5)) / 2`. WOUND plus shadow_density must be even, which both constraints enforce. Output internal 0-60.

### DRV.truthexposureindex

`DRV.truth_exposure_index`. Internal formula `(T1.SOCIAL × 3) + ((12 - T3.EROS.shame_index) × 5)`. Display formula `T1.SOCIAL + max(0, 10 - T3.EROS.shame_index)`. Slice 3.3.2 clamps the shame term at 0 on SC-12 (Chief, 10/4: "REC."). No constraints. Output internal, uncapped, may exceed 60. A value over 60 means the character's legibility exceeds the system's containment threshold.

### DRV.expressiverange

`DRV.expressive_range`. Display formula `12 - T3.EROS.armor_index`, 0 to 12. Slice 3.3.2 ruled the constant (Chief, 10/4: "Rick"). The internal mapping follows `armor_index` at SC-12. It measures what the character can send on purpose. `truth_exposure_index` measures what leaks.

The version history records an earlier constant, `10 - armor_index`. Chief replaced it with `12 - armor_index` on 2026-10-04, so the result never goes negative.

## Status Flags

Every flag has source `computed`, tag Derived, and states `{ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE}`.

### FLG.shadowdenial

`FLG.shadow_denial`. Trigger: `T2.WOUND > 6 AND T3.SHADOW.projection_tendency >= 6 AND T3.IMPRINT.conditional_patterns contains "merit_earns_freedom"`.

### FLG.truthvulnerability

`FLG.truth_vulnerability`. Trigger: `T1.SOCIAL < 12 AND T3.FUNC.mc_problem_element = "Equity" AND T3.SHADOW.shadow_density > 6`.

### FLG.optionlockprogression

`FLG.optionlock_progression`. Trigger: `T2.WOUND > 8 AND T3.DESTINY.resistance_index > 8 AND T3.FUNC.limit_type = "Optionlock"`.

### FLG.earnedjudgement

`FLG.earned_judgement`. Trigger: `T3.FUNC.dramatica_archetype = "Protagonist" AND T3.FUNC.story_outcome = "Failure" AND T2.WILL > 10`.

### FLG.kinshipcollapse

`FLG.kinship_collapse`. Trigger: `T3.IMPRINT.attachment_style_score > 6 AND T3.IMPRINT.primary_attachment_object = "deceased" AND T2.WOUND > 8`.

## Character Astrology Variables

### Personal Stack

| Path | Type | Source |
|---|---|---|
| `AST.PERSONAL.sun_sign` | enum (zodiac signs) | DAI Step 1 |
| `AST.PERSONAL.sun_element` | enum {fire, earth, air, water} | Derived from sun_sign |
| `AST.PERSONAL.sun_modality` | enum {cardinal, fixed, mutable} | Derived from sun_sign |
| `AST.PERSONAL.moon_sign` | enum | DAI Step 2 |
| `AST.PERSONAL.mercury_sign` | enum | DAI Step 4 |
| `AST.PERSONAL.venus_sign` | enum | DAI Step 5 |
| `AST.PERSONAL.mars_sign` | enum | DAI Step 6 |

### Structural Stack

| Path | Type | Source |
|---|---|---|
| `AST.STRUCTURAL.saturn_sign` | enum | DAI Step 7 |
| `AST.STRUCTURAL.jupiter_sign` | enum | DAI Step 8 |
| `AST.STRUCTURAL.uranus_sign` | enum | DAI Step 9 |
| `AST.STRUCTURAL.neptune_sign` | enum | DAI Step 10 |
| `AST.STRUCTURAL.pluto_sign` | enum | DAI Step 11 |

### Angles

| Path | Type | Source |
|---|---|---|
| `AST.ANGLE.ascendant_sign` | enum | DAI Step 3 |
| `AST.ANGLE.midheaven_sign` | enum | DAI Step 12 |
| `AST.ANGLE.descendant_sign` | enum | Computed (opposite of ascendant) |
| `AST.ANGLE.ic_sign` | enum | Computed (opposite of midheaven) |

### Aspects

| Path | Type | Notes |
|---|---|---|
| `AST.ASPECT.[id].planet_a` | str | Planet name |
| `AST.ASPECT.[id].planet_b` | str | Planet name |
| `AST.ASPECT.[id].type` | enum {conjunction, square, opposition, trine, sextile} | |
| `AST.ASPECT.[id].gate_type` | enum {AND, NOT, XOR, OR} | |
| `AST.ASPECT.[id].dramatica_source` | str | Tension source |

### Houses

| Path | Type |
|---|---|
| `AST.HOUSE.[planet_name].house_number` | int (1-12) |
| `AST.HOUSE.[planet_name].house_type` | enum {angular, succedent, cadent} |

### Dignities

| Path | Type |
|---|---|
| `AST.DIGNITY.[planet_name].status` | enum {domicile, exaltation, peregrine, detriment, fall} |

## State Diff Variables

State diffs use the `STT` prefix. They mirror the variable they modify, with extra metadata.

| Path | Type | Purpose |
|---|---|---|
| `STT.state_id` | str | Unique state identifier |
| `STT.narrative_moment` | str | Human-readable when |
| `STT.movement` | str | Movement tag |
| `STT.mc_distance_temporal` | int | Temporal distance from MC |
| `STT.mc_distance_narrative` | int | Causal distance from MC |
| `STT.base_record_version` | str | Version of base record |
| `STT.[any_layer_variable]` | matches source type | Modified value, replaces base on query |
| `STT.WILL_EFFECTIVE` | int SC-20 | State-only field: temporary WILL reduction |
| `STT.state_note` | str | Prose justification for the diff |

## Character Metadata

| Path | Type | Purpose |
|---|---|---|
| `META.character_id` | str | Unique character identifier |
| `META.character_name` | str | Display name |
| `META.ip` | str | Intellectual property |
| `META.tier` | int {1, 2, 3} | Character tier |
| `META.status` | enum {draft, locked, archived} | Record status |
| `META.version` | str | Record version |
| `META.storyform_id` | str | Bound storyform |

> **OPEN:** the `REL` prefix is declared in Domain Prefixes but the registry defines no `REL` variable beyond the example `REL.relationship_type`.

Related pages: [concept](1-concept.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md)
