---
type: ssot_00_foundations
category: module_registry
module_of: ssot_00_module_architecture
version: 1.2.0
tier: foundation
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
trunk: BLACK
purpose: "The complete registry of all Layer-Locked Modules (field modules): current, absorbed, planned, and conceptual. Each entry defines the module's attachment point, variable set, access pattern, and development status."
dependencies: ["ssot_00_module_architecture", "ssot_00_variable_registry", "ssot_02_character_systems_vertical_slice"]
---
# 📐 SSOT: Layer-Locked Module Registry

## Table of Contents

1. [Purpose](#purpose)
2. [Registry Overview](#registry-overview)
3. [Active Modules](#active-modules)
4. [Absorbed Modules](#absorbed-modules)
5. [Planned Modules](#planned-modules)
6. [Conceptual Modules](#conceptual-modules)
7. [Module Dependency Map](#module-dependency-map)
8. [Version History](#version-history)

---

## Purpose

This is the complete catalog of every field module that attaches to the LEECHSEED Character System. A field module is a set of variables beneath a layer. A doc module is a sibling document in `02_CHARACTER_SYSTEMS`. This registry lists field modules only ([📐 ssot_00_module_architecture.md](📐%20ssot_00_module_architecture.md), Field Modules and Doc Modules). When a new module is conceived, it is registered here before any variables are defined. When a module moves from planned to active, its full API declaration is documented here.

---

## Registry Overview

|Module ID|Display Name|Attachment|Tier|Status|Variables|Derived|Flags|
|---|---|---|---|---|---|---|---|
|`DUALISM`|Dualism Charge System|All layers|3|**active**|12+|Yes|Yes|
|`LOL_TAX`|LoL Character Taxonomy|Multiple|3|**planned**|70+|Yes|No|
|`WALK`|Walking Style|L2 VITAL|3|**planned**|3|No|No|
|`COMBAT`|Combat Archetype|L2, L4|3|**planned**|5|Yes|No|
|`SEX_PROF`|Sexuality Profile|L9 EROS|3|**absorbed**|0 (was 5)|No|No|
|`MUSIC`|Music Interests|L8 IMPRINT|3|**planned**|4|No|No|
|`VOICE`|Vocal Signature|L2, L3|3|**absorbed**|0 (was 4)|No|No|
|`FASHION`|Fashion/Aesthetic Profile|L3 SOCIAL|3|**planned**|5|No|No|
|`COPING`|Coping Mechanism Catalog|L4 WILL|3|**planned** (narrowed)|2 (was 4)|Yes|Yes|
|`DECOMP`|Decompensation Profile|L5 WOUND|3|**planned**|4|No|Yes|
|`PHYS`|Physical Detail|L2 VITAL|3|**planned**|6|No|No|
|`CULTURE`|Cultural Conditioning|L7, L8|3|**conceptual**|⏸|⏸|⏸|
|`SPIRIT`|Spiritual Framework|L11 DESTINY|3|**conceptual**|⏸|⏸|⏸|
|`DESIGN`|Design Focus Power Board|Meta|3|**conceptual**|12|Yes|No|

**Audit, 2026-10-04 (slice 3.3.1):** 1 active, 2 absorbed, 8 planned, 3 conceptual. None dropped. The core schema absorbed SEX_PROF and VOICE. COPING narrowed. Each planned module reads below. **⏸** marks `⏸ module build (phase 2)`: the scope is method and is written now, the variable list is instance content and waits for the module build.

---

## Active Modules

### MOD.DUALISM — Dualism Charge System

```yaml
MODULE_DECLARATION:
  module_id: DUALISM
  display_name: Dualism Charge System
  version: 1.0.0
  author: LEECHSEED
  attachment_points: [CORE, VITAL, SOCIAL, WILL, WOUND, DRIVE, ORIGIN,
                      IMPRINT, EROS, SHADOW, DESTINY, FUNC]
  tier_min: 3
  depends_on: []
  description: Assigns a bipolar charge value (-30 to +30) to each layer,
    encoding the character's position on a dualistic spectrum per domain,
    with snap boundaries at +/-60 for transcendent outliers.
```

**Variables (per layer, 12 instances):**

|Path|Type|Scale|Range|Constraint|Tag|
|---|---|---|---|---|---|
|`MOD.DUALISM.[LAYER].charge_value`|`int`|SC-60 (signed)|-30 to +30|None|Dynamic|
|`MOD.DUALISM.[LAYER].pole_negative`|`str`|N/A|Freeform label|Trait name|Static|
|`MOD.DUALISM.[LAYER].pole_positive`|`str`|N/A|Freeform label|Trait name|Static|
|`MOD.DUALISM.[LAYER].behavior_desc`|`str`|N/A|Freeform|LoL ability-style sentence|Static|

Every module variable carries a `Static` or `Dynamic` tag, as the Variable Declaration Block in the module architecture requires (IF-00-02-27; IF catalog call 4, ruled 2026-10-05). Each planned module declares its tags when it moves to `draft`.

**Reads:** All core layer base values, `T3.FUNC.resolve`

**Derived:**

```
MOD.DUALISM.total_charge = sum of all 12 charge_values
MOD.DUALISM.charge_variance = standard deviation of all 12 charge_values
```

**Flags:**

```
MOD.DUALISM.FLG.transcendent_outlier:
  Trigger: any MOD.DUALISM.[LAYER].charge_value > 30 OR < -30
  (snap boundary exceeded — character has moved beyond the normal dualistic range
   in at least one domain)
```

**Notes:** This module is the only module that attaches to ALL 12 layers. It is architecturally unique because it adds a parallel dimension to every layer rather than extending a single layer. The -30/+30 range is already base-60 native (60-unit total span). The snap boundaries at ±60 use the full SC-60 extended range.

---

## Absorbed Modules

An absorbed module is closed. The core schema now holds its fields, so the module never builds. The tables below say where each variable went. The slice is [📐 ssot_02_character_systems_vertical_slice.md](../02_CHARACTER_SYSTEMS/📐%20ssot_02_character_systems_vertical_slice.md) at 3.3.1.

### MOD.SEX_PROF — Sexuality Profile (absorbed)

|Old variable|Where it went|
|---|---|
|`orientation_coding`|L9 `orientation_dimensions` (behavior, desire, identity) and `attraction_channels`. L1 `identity_frame` holds the stated label.|
|`power_dynamic`|L9 `polarity_role` for the role. L9 `power_exchange` for the bond.|
|`display_confidence`|L9 `exposure_shame` and L3 `self_presentation`.|
|`repression_index`|L9 `exposure_shame` and L10 `moral_incongruence`.|
|`erotic_autonomy`|L9 `desire_vector.desire_object` and `consent_posture`.|
|Derived `sexual_legibility_internal`, flag `erotic_suppression`|Dropped with the module. `DRV.truth_exposure_index` and `DRV.expressive_range` measure legibility.|

### MOD.VOICE — Vocal Signature (absorbed)

|Old variable|Where it went|
|---|---|
|`register`|L3 `voice_sheet.register`.|
|`speech_pace`|L3 `voice_sheet.native_pace`.|
|`texture`|Kept by Texture, the writing rule for how the voice is narrated (slice, L3 `voice_sheet`).|
|`silence_usage`|Dropped. The slice has no field for it.|

---

## Planned Modules

### MOD.LOL_TAX — LoL Character Taxonomy

```yaml
MODULE_DECLARATION:
  module_id: LOL_TAX
  display_name: League of Legends Character Taxonomy
  version: 0.1.0
  author: LEECHSEED
  attachment_points: [VITAL, SOCIAL, WILL, IMPRINT, EROS, SHADOW]
  tier_min: 3
  depends_on: [COMBAT]
  description: The 12-domain character taxonomy from the LoL analysis project,
    consolidated under existing layers with foreign key references.
```

**Domain-to-Layer Mapping:**

|LoL Domain|Attachment Layer|Notes|
|---|---|---|
|Physical Appearance|L2 VITAL (via MOD.PHYS)|Body data|
|Psychological Archetype|L8 IMPRINT|Psych conditioning|
|Kinetic Behavior|L2 VITAL|Movement style|
|Coping Mechanisms|L4 WILL (via MOD.COPING)|Stress management|
|Decompensation|L5 WOUND (via MOD.DECOMP)|Breakdown patterns|
|Mental Illness Predisposition|L5 WOUND|Clinical echoes|
|Sexuality Profile|L9 EROS (core fields, SEX_PROF absorbed)|Sexual dynamics|
|Openness/Disposition|L3 SOCIAL|Big Five traits|
|Fetish/Kink Alignment|L9 EROS|Desire communities|
|Combat Archetype|L2 VITAL (via MOD.COMBAT)|Fight role|
|Social Role|L3 SOCIAL|Group positioning|
|Design Focus Power Board|Meta (via MOD.DESIGN)|Meta-distribution|

**Status:** Still planned. Depends on MOD.COMBAT being built first. SEX_PROF is absorbed, so the Sexuality Profile domain reads the L9 fields directly. Several domains map to other planned modules, creating a composite dependency chain.

---

### MOD.WALK — Walking Style

```yaml
MODULE_DECLARATION:
  module_id: WALK
  display_name: Walking Style
  version: 0.1.0
  author: LEECHSEED
  attachment_points: [VITAL]
  tier_min: 3
  depends_on: []
  description: Catalogs the character's gait, pace, and physical movement signature
    as expressions of L2 VITAL physicality.
```

**Variables:**

|Path|Type|Scale|Behavior|
|---|---|---|---|
|`MOD.WALK.gait_type`|`enum`|N/A|`{measured, urgent, languid, predatory, bouncing, shuffling, mechanical, flowing}`|
|`MOD.WALK.pace_default`|`enum`|N/A|`{slow, moderate, brisk, variable}`|
|`MOD.WALK.signature_tell`|`str`|N/A|The one physical detail a witness would remember — "leads with shoulders", "feet barely leave the ground".|

**Reads:** `T1.VITAL.base_value`, `T3.SHADOW.regression_pattern`

---

### MOD.COMBAT — Combat Archetype

```yaml
MODULE_DECLARATION:
  module_id: COMBAT
  display_name: Combat Archetype
  version: 0.1.0
  author: LEECHSEED
  attachment_points: [VITAL, WILL]
  tier_min: 3
  depends_on: []
  description: Defines the character's fighting philosophy, win condition,
    and martial identity as an intersection of physical capacity and psychological resistance.
```

**Variables:**

|Path|Type|Scale|Behavior|
|---|---|---|---|
|`MOD.COMBAT.archetype`|`enum`|N/A|`{striker, grappler, tactician, berserker, guardian, ghost, controller, predator}`|
|`MOD.COMBAT.philosophy`|`str`|N/A|The one-sentence fight doctrine.|
|`MOD.COMBAT.win_condition`|`str`|N/A|What "winning" looks like for this fighter.|
|`MOD.COMBAT.lethality`|`int`|SC-12|0 = incapable of lethal force; 12 = killing is the default output.|
|`MOD.COMBAT.survivability`|`int`|SC-12|0 = glass; 12 = refuses to stay down.|

**Reads:** `T1.VITAL.base_value`, `T2.WILL.base_value`, `T3.SHADOW.regression_pattern`

**Derived:**

```
MOD.COMBAT.threat_index_internal = (lethality × 5 + survivability × 5) / 2
  Constraint: lethality + survivability must be even
```

---

### MOD.MUSIC — Music Interests

```yaml
MODULE_DECLARATION:
  module_id: MUSIC
  display_name: Music Interests
  version: 0.1.0
  author: LEECHSEED
  attachment_points: [IMPRINT]
  tier_min: 3
  depends_on: []
  description: Catalogs the character's music taste as an expression of
    emotional conditioning and aesthetic DNA.
```

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.MUSIC.primary_genre`|`str`|The genre the character returns to under stress.|
|`MOD.MUSIC.formative_artist`|`str`|The artist or band that imprinted during conditioning period.|
|`MOD.MUSIC.listening_mode`|`enum`|`{immersive, background, social, analytical, emotional_regulation}`|
|`MOD.MUSIC.sonic_signature`|`str`|Freeform — the quality of sound this character gravitates toward ("heavy bass, minimal vocals", "acoustic, raw, confessional").|

**Reads:** `T3.IMPRINT.emotional_range`, `T3.IMPRINT.conditional_patterns`

---

### MOD.FASHION — Fashion/Aesthetic Profile

```yaml
MODULE_DECLARATION:
  module_id: FASHION
  display_name: Fashion/Aesthetic Profile
  version: 0.1.0
  attachment_points: [SOCIAL]
  tier_min: 3
  depends_on: []
  description: How the character presents visually as social signal management.
```

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.FASHION.aesthetic_code`|`str`|"Workwear utility", "curated minimalism", "institutional uniform"|
|`MOD.FASHION.signal_intent`|`enum`|`{invisible, functional, aspirational, defiant, seductive, institutional}`|
|`MOD.FASHION.grooming_level`|`int` SC-12|0 = completely unmanaged; 12 = meticulously curated.|
|`MOD.FASHION.brand_relationship`|`enum`|`{indifferent, hostile, strategic, devotional, aspirational}`|
|`MOD.FASHION.body_display`|`enum`|`{concealed, functional, highlighted, weaponized, neutral}`|

**Reads:** `T1.SOCIAL.base_value`, `T3.EROS.shame_index`

---

### MOD.COPING — Coping Mechanism Catalog

```yaml
MODULE_DECLARATION:
  module_id: COPING
  display_name: Coping Mechanism Catalog
  version: 0.1.0
  attachment_points: [WILL]
  tier_min: 3
  depends_on: []
  description: How the character manages stress before decompensation — the tools they reach for when WILL is tested.
```

**Narrowed 2026-10-04:** the strategy itself now lives at L4 `coping_strategy` (slice 2.1.0), so the module's two strategy enums are gone. The module keeps the two scores and the stats built on them.

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.COPING.effectiveness`|`int` SC-12|0 = coping strategies consistently fail; 12 = coping strategies reliably restore function.|
|`MOD.COPING.cost_to_others`|`int` SC-12|0 = coping is self-contained; 12 = coping inflicts maximum collateral damage on others.|

**Reads:** `T2.WILL.coping_strategy`

**Derived:**

```
MOD.COPING.sustainability_internal =
  (effectiveness × 5) - (cost_to_others × 5 / 2)
  Constraint: cost_to_others must be even
```

**Flags:**

```
MOD.COPING.FLG.coping_failure:
  Trigger: MOD.COPING.effectiveness < 4 AND T2.WOUND > 6
```

---

### MOD.DECOMP — Decompensation Profile

```yaml
MODULE_DECLARATION:
  module_id: DECOMP
  display_name: Decompensation Profile
  version: 0.1.0
  attachment_points: [WOUND]
  tier_min: 3
  depends_on: [COPING]
  description: What happens when coping fails — the specific breakdown pattern when WOUND exceeds WILL's capacity.
```

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.DECOMP.breakdown_type`|`enum`|`{rage, collapse, dissociation, paranoia, self_harm, flight, freeze, performance_escalation}`|
|`MOD.DECOMP.visibility`|`int` SC-12|0 = breakdown is invisible to others; 12 = breakdown is maximally public.|
|`MOD.DECOMP.recovery_speed`|`int` SC-12|0 = does not recover without intervention; 12 = bounces back immediately.|
|`MOD.DECOMP.residue`|`str`|What the breakdown leaves behind — "trust deficit", "reputation damage", "physical injury".|

**Flags:**

```
MOD.DECOMP.FLG.decompensation_risk:
  Trigger: DRV.stress_threshold < 0 AND MOD.COPING.effectiveness < 6
```

---

### MOD.PHYS — Physical Detail

```yaml
MODULE_DECLARATION:
  module_id: PHYS
  display_name: Physical Detail
  version: 0.1.0
  attachment_points: [VITAL]
  tier_min: 3
  depends_on: []
  description: Extended physical description data — body type, distinguishing marks, physicality source.
```

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.PHYS.body_type`|`enum`|`{lean, athletic, heavy, wiry, compact, imposing, fragile, unremarkable}`|
|`MOD.PHYS.physicality_source`|`enum`|`{labor, sport, military, dance, martial_art, genetic, neglect, institutional}`|
|`MOD.PHYS.distinguishing_marks`|`array_str`|Scars, tattoos, physical tells|
|`MOD.PHYS.beauty_read`|`str`|How the character's appearance is received — "striking but nonconforming", "invisible", "threatening"|
|`MOD.PHYS.age_presentation`|`enum`|`{younger_than_actual, accurate, older_than_actual, ambiguous}`|
|`MOD.PHYS.physical_confidence`|`int` SC-12|0 = disconnected from body; 12 = body is primary instrument of identity.|

**Reads:** `T1.VITAL.base_value`

---

### Audit of Planned Modules (2026-10-04)

|Module|Slice check|Verdict|
|---|---|---|
|`LOL_TAX`|Composes other modules. Its Sexuality Profile domain now reads L9.|Still planned. Depends on COMBAT only.|
|`WALK`|No gait field in the slice.|Still planned.|
|`COMBAT`|No combat field in the slice.|Still planned.|
|`MUSIC`|No music field in the slice.|Still planned.|
|`FASHION`|L3 `self_presentation` covers the public persona only, not dress, grooming or body display.|Still planned.|
|`COPING`|L4 `coping_strategy` holds the strategy.|Still planned, narrowed to the two scores.|
|`DECOMP`|L5 `wound_work` covers how a wound is worked, not the breakdown pattern.|Still planned. Depends on COPING.|
|`PHYS`|L2 `physiology_stack` is a text checklist. The typed fields here go beyond it.|Still planned. Reads `physiology_stack`.|

An MS reads the vertical slice and reports one verdict per module. Chief rules the verdict: absorbed, retired, or still planned. The author then records where each variable went in the Absorbed Modules table.

---

## Conceptual Modules

These modules have been identified as potential extensions but do not yet have variable definitions. They are registered to reserve their module IDs and attachment points.

### MOD.CULTURE — Cultural Conditioning

|Field|Value|
|---|---|
|Module ID|`CULTURE`|
|Attachment|L7 ORIGIN, L8 IMPRINT|
|Concept|Extended cultural background — language, religion, ethnic identity, diaspora status, cultural code-switching ability|
|Scope|Holds the cultural conditioning that shaped the character. Reads L7 `origin_class` and `origin_disciplinary_formation`, L8 `conditional_patterns` and L3 `community_membership`.|
|Variables|⏸ module build (phase 2)|
|Status|Conceptual|

### MOD.SPIRIT — Spiritual Framework

|Field|Value|
|---|---|
|Module ID|`SPIRIT`|
|Attachment|L11 DESTINY|
|Concept|Belief system analysis — religious/spiritual orientation, relationship to transcendence, existential framework, death attitude|
|Scope|Holds the character's belief system and how it bends the growth vector. Reads L11 `growth_axis`, `soul_evolution_archetype` and `karmic_memory`, and L8 `conditional_patterns`.|
|Variables|⏸ module build (phase 2)|
|Status|Conceptual|

### MOD.DESIGN — Design Focus Power Board

|Field|Value|
|---|---|
|Module ID|`DESIGN`|
|Attachment|Meta (all layers)|
|Concept|The meta-distribution of design energy across all other domains — which aspects of this character received the most authorial investment and which were left at default. 12 domains from the LoL taxonomy rated on SC-12.|
|Scope|Rates the authorial investment per domain. Reads every layer's base value and writes none.|
|Status|Conceptual|

---

## Module Dependency Map

```
Independent (no dependencies):
  WALK, COMBAT, MUSIC, FASHION, COPING, PHYS, DUALISM

Single dependency:
  DECOMP → COPING
  LOL_TAX → COMBAT (SEX_PROF was absorbed)

Absorbed (closed, no build):
  SEX_PROF, VOICE

Conceptual (scope written, variable list parked):
  CULTURE (reads L7, L8, L3; no dependencies)
  SPIRIT  (reads L11, L8; no dependencies)
  DESIGN  (reads every layer; no dependencies)
```

Build order for maximum independence: WALK → PHYS → COMBAT → FASHION → MUSIC → COPING → DECOMP → LOL_TAX

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-08|Initial registry. 1 active module (DUALISM), 10 planned modules with full declarations, 3 conceptual modules with reserved IDs. Dependency map and recommended build order.|
|1.1.0|2026-10-04|BOLO 100 base batch 1 (B1, B2, B3, B9, B10, B13, B15), RULED Chief "REC.": frontmatter repaired with `trunk`; `module_of: ssot_00_module_architecture` stamped; table-of-contents links repointed; audit against slice 3.3.1 (SEX_PROF and VOICE absorbed, COPING narrowed, the rest still planned, none dropped); conceptual scopes written for CULTURE, SPIRIT and DESIGN with their variable lists parked as `⏸ module build (phase 2)`; dependency map and build order redone.|
|1.1.1|2026-10-05|BOLO 102 batch A (Chief: "All recs go"): DESIGN and LOL_TAX counts set to 12 to match the 12-row mapping table.|
|1.1.2|2026-10-05|BOLO 102 batch C (Chief: "all recs"): C11, who reports and who rules an audit verdict (absorbed, retired, still planned).|
|1.2.0|2026-10-05|BOLO 102 stage 2 (Chief: "My word"): call 4, the DUALISM variables carry the `Static` or `Dynamic` tag the module architecture now requires.|
