---

## type: ssot_00_foundations category: module_registry version: 1.0.0 last_updated: 2026-03-08 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "The complete registry of all Layer-Locked Modules — current, planned, and conceptual. Each entry defines the module's attachment point, variable set, access pattern, and development status." dependencies: ["ssot_00_module_architecture", "ssot_00_variable_registry"]
---
# 📐 SSOT: Layer-Locked Module Registry

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [Registry Overview](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#registry-overview)
3. [Active Modules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#active-modules)
4. [Planned Modules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#planned-modules)
5. [Conceptual Modules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#conceptual-modules)
6. [Module Dependency Map](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#module-dependency-map)
7. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This is the complete catalog of every module that attaches to the 12-Layer Character Database. When a new module is conceived, it is registered here before any variables are defined. When a module moves from planned to active, its full API declaration is documented here.

---

## Registry Overview

|Module ID|Display Name|Attachment|Tier|Status|Variables|Derived|Flags|
|---|---|---|---|---|---|---|---|
|`DUALISM`|Dualism Charge System|All layers|3|**active**|12+|Yes|Yes|
|`LOL_TAX`|LoL Character Taxonomy|Multiple|3|**planned**|70+|Yes|No|
|`WALK`|Walking Style|L2 VITAL|3|**planned**|3|No|No|
|`COMBAT`|Combat Archetype|L2, L4|3|**planned**|5|Yes|No|
|`SEX_PROF`|Sexuality Profile|L9 EROS|3|**planned**|5|Yes|Yes|
|`MUSIC`|Music Interests|L8 IMPRINT|3|**planned**|4|No|No|
|`VOICE`|Vocal Signature|L2, L3|3|**planned**|4|No|No|
|`FASHION`|Fashion/Aesthetic Profile|L3 SOCIAL|3|**planned**|5|No|No|
|`COPING`|Coping Mechanism Catalog|L4 WILL|3|**planned**|4|Yes|Yes|
|`DECOMP`|Decompensation Profile|L5 WOUND|3|**planned**|4|No|Yes|
|`PHYS`|Physical Detail|L2 VITAL|3|**planned**|6|No|No|
|`CULTURE`|Cultural Conditioning|L7, L8|3|**conceptual**|TBD|TBD|TBD|
|`SPIRIT`|Spiritual Framework|L11 DESTINY|3|**conceptual**|TBD|TBD|TBD|
|`DESIGN`|Design Focus Power Board|Meta|3|**conceptual**|14|Yes|No|

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

|Path|Type|Scale|Range|Constraint|
|---|---|---|---|---|
|`MOD.DUALISM.[LAYER].charge_value`|`int`|SC-60 (signed)|-30 to +30|None|
|`MOD.DUALISM.[LAYER].pole_negative`|`str`|N/A|Freeform label|Trait name|
|`MOD.DUALISM.[LAYER].pole_positive`|`str`|N/A|Freeform label|Trait name|
|`MOD.DUALISM.[LAYER].behavior_desc`|`str`|N/A|Freeform|LoL ability-style sentence|

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
  depends_on: [SEX_PROF, COMBAT]
  description: The 14-domain character taxonomy from the LoL analysis project,
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
|Sexuality Profile|L9 EROS (via MOD.SEX_PROF)|Sexual dynamics|
|Openness/Disposition|L3 SOCIAL|Big Five traits|
|Fetish/Kink Alignment|L9 EROS|Desire communities|
|Combat Archetype|L2 VITAL (via MOD.COMBAT)|Fight role|
|Social Role|L3 SOCIAL|Group positioning|
|Design Focus Power Board|Meta (via MOD.DESIGN)|Meta-distribution|

**Status:** Planned. Depends on MOD.SEX_PROF and MOD.COMBAT being built first. Several domains map to other planned modules, creating a composite dependency chain.

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

### MOD.SEX_PROF — Sexuality Profile

```yaml
MODULE_DECLARATION:
  module_id: SEX_PROF
  display_name: Sexuality Profile
  version: 0.1.0
  author: LEECHSEED
  attachment_points: [EROS]
  tier_min: 3
  depends_on: []
  description: Extended sexuality analysis beyond core L9 EROS — orientation coding,
    power dynamics, display confidence, and erotic autonomy.
```

**Variables:**

|Path|Type|Scale|Behavior|
|---|---|---|---|
|`MOD.SEX_PROF.orientation_coding`|`enum`|N/A|`{heteronormative, queer_coded, fluid, ambiguous, asexual_coded}` — how the design reads, not the character's stated identity.|
|`MOD.SEX_PROF.power_dynamic`|`enum`|N/A|`{dominant, submissive, switch, neutral, contextual}`|
|`MOD.SEX_PROF.display_confidence`|`int`|SC-12|0 = sexual presentation is invisible; 12 = sexuality is a primary broadcast channel.|
|`MOD.SEX_PROF.repression_index`|`int`|SC-12, even|0 = no repression; 12 = sexual identity is fully suppressed.|
|`MOD.SEX_PROF.erotic_autonomy`|`int`|SC-12|0 = desire is entirely other-directed; 12 = desire is fully self-authored.|

**Reads:** `T3.EROS.shame_index`, `T3.EROS.erotic_blueprint_type`, `T3.SHADOW.shadow_density`

**Derived:**

```
MOD.SEX_PROF.sexual_legibility_internal =
  (display_confidence × 5) - (repression_index × 5 / 2)
  Constraint: repression_index must be even
```

**Flags:**

```
MOD.SEX_PROF.FLG.erotic_suppression:
  Trigger: MOD.SEX_PROF.repression_index > 8 AND T3.EROS.shame_index > 6
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

### MOD.VOICE — Vocal Signature

```yaml
MODULE_DECLARATION:
  module_id: VOICE
  display_name: Vocal Signature
  version: 0.1.0
  attachment_points: [VITAL, SOCIAL]
  tier_min: 3
  depends_on: []
  description: The character's voice as physical instrument (L2) and social signal (L3).
```

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.VOICE.register`|`enum`|`{bass, baritone, tenor, alto, mezzo, soprano}`|
|`MOD.VOICE.texture`|`str`|"Gravel and warmth", "thin and precise", "resonant, fills rooms"|
|`MOD.VOICE.speech_pace`|`enum`|`{deliberate, rapid, variable, monotone, rhythmic}`|
|`MOD.VOICE.silence_usage`|`enum`|`{frequent, rare, strategic, uncomfortable, weaponized}`|

**Reads:** `T1.VITAL.base_value`, `T1.SOCIAL.base_value`, `T3.SHADOW.regression_pattern`

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

**Variables:**

|Path|Type|Behavior|
|---|---|---|
|`MOD.COPING.primary_strategy`|`enum`|`{exercise, substance, isolation, socialization, work, intellectualization, creative_expression, ritualization, denial}`|
|`MOD.COPING.secondary_strategy`|`enum`|Same set as primary.|
|`MOD.COPING.effectiveness`|`int` SC-12|0 = coping strategies consistently fail; 12 = coping strategies reliably restore function.|
|`MOD.COPING.cost_to_others`|`int` SC-12|0 = coping is self-contained; 12 = coping inflicts maximum collateral damage on others.|

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

## Conceptual Modules

These modules have been identified as potential extensions but do not yet have variable definitions. They are registered to reserve their module IDs and attachment points.

### MOD.CULTURE — Cultural Conditioning

|Field|Value|
|---|---|
|Module ID|`CULTURE`|
|Attachment|L7 ORIGIN, L8 IMPRINT|
|Concept|Extended cultural background — language, religion, ethnic identity, diaspora status, cultural code-switching ability|
|Status|Conceptual|

### MOD.SPIRIT — Spiritual Framework

|Field|Value|
|---|---|
|Module ID|`SPIRIT`|
|Attachment|L11 DESTINY|
|Concept|Belief system analysis — religious/spiritual orientation, relationship to transcendence, existential framework, death attitude|
|Status|Conceptual|

### MOD.DESIGN — Design Focus Power Board

|Field|Value|
|---|---|
|Module ID|`DESIGN`|
|Attachment|Meta (all layers)|
|Concept|The meta-distribution of design energy across all other domains — which aspects of this character received the most authorial investment and which were left at default. 14 domains from the LoL taxonomy rated on SC-12.|
|Status|Conceptual|

---

## Module Dependency Map

```
Independent (no dependencies):
  WALK, COMBAT, SEX_PROF, MUSIC, VOICE, FASHION, COPING, PHYS, DUALISM

Single dependency:
  DECOMP → COPING

Multi-dependency:
  LOL_TAX → SEX_PROF, COMBAT

Conceptual (dependencies TBD):
  CULTURE, SPIRIT, DESIGN
```

Build order for maximum independence: WALK → PHYS → COMBAT → VOICE → FASHION → MUSIC → SEX_PROF → COPING → DECOMP → LOL_TAX

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-08|Initial registry. 1 active module (DUALISM), 10 planned modules with full declarations, 3 conceptual modules with reserved IDs. Dependency map and recommended build order.|