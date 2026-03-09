---

## type: ssot_02_character_systems category: state_architecture version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the architecture for tracking character change over narrative time without modifying the static core record. Establishes the state diff system, state record format, overlay resolution rules, and boundaries with the static character record, relationship tables, and plot_systems." dependencies: ["ssot_03_character_systems_vertical_slice", "ssot_02_character_astrology"]
---
# 🔮 SSOT: Character State Architecture

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [The Core Principle](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-core-principle)
3. [What Is Static vs What Is Dynamic](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-is-static-vs-what-is-dynamic)
4. [State Record Format](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#state-record-format)
5. [State Diff Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#state-diff-rules)
6. [Querying a Character at a Narrative Moment](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#querying-a-character-at-a-narrative-moment)
7. [State Sources](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#state-sources)
8. [Relationship Records](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#relationship-records)
9. [Boundaries with plot_systems](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#boundaries-with-plot-systems)
10. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

Characters change over the course of a story. Layer values shift. Flags fire. Wounds deepen or partially heal. Relationships form and collapse. The 12-Layer Vertical Slice captures the character at the point of canonical definition — but the story demands that we track who the character is at Movement 1A, at the moment of the crash, at the Ban, at collapse.

This document defines how to track that change without modifying the static core record. The architecture is: one immutable base record per character, plus any number of state diffs keyed to narrative time coordinates. The base record is the birth certificate. The state diffs are the medical history.

---

## The Core Principle

**The static character record never changes.**

The 12-Layer Vertical Slice and the Character Astrology natal chart represent the character's canonical identity — who they ARE. This record is produced once, locked, and placed in the character's canonical folder. It is never edited during story development. If the record needs revision, a new version is created with a documented reason, and the old version is archived.

**Character states are overlays.** A state record describes what is different about the character at a specific narrative moment compared to their base record. It does not duplicate the base record. It lists only the values that have changed and the reason for the change.

**The base record plus a state diff equals the character at that moment.** To know who Victoria Midnight is at M1B Delta Coast, read the base record and then apply the M1B state diff. The result is the complete character at that point in the story.

---

## What Is Static vs What Is Dynamic

### Static (Lives in the Base Record, Never Changes)

|Data|Reason|
|---|---|
|L1 CORE value|Cognitive capacity does not change within a single story arc|
|L2 VITAL value|Physical capacity baseline does not change (injuries are state diffs)|
|L3 SOCIAL value|Social interface baseline does not change (reputation is a state diff)|
|L12 FUNCTION (entire layer)|Dramatica structural role is fixed for the storyform|
|Character Astrology natal chart|The chart is the source code — it does not mutate|
|Natal aspects|Internal friction architecture is permanent|
|Natal dignities|Efficiency ratings are permanent|
|House placements|Environmental directories are permanent|
|L7 ORIGIN variable stack|Origin does not change — it is historical record|
|L8 IMPRINT conditional_patterns|Core conditioning patterns are permanent (their activation state changes)|

### Dynamic (Lives in State Diffs)

|Data|Reason|
|---|---|
|L4 WILL (effective value)|Systemic pressure can temporarily reduce effective WILL|
|L5 WOUND value|Wounds accumulate and occasionally partially heal|
|L6 DRIVE value|Drive is spent and recovered across the narrative|
|L8 IMPRINT attachment_style_score|Attachment security fluctuates based on relational events|
|L8 IMPRINT primary_attachment_object|Attachment targets change (death, new bonds, betrayal)|
|L9 EROS desire_vector, shame_index|Sexual and intimate patterns shift with experience|
|L10 SHADOW shadow_density, projection_tendency|Shadow content surfaces or deepens across the arc|
|L11 DESTINY resistance_index|Resistance to growth changes as the character approaches transformation|
|All derived statistics|Recomputed from modified layer values in the state diff|
|All flag states|Re-evaluated against modified values in the state diff|
|Progressed planetary positions|Progressions create slow-moving state overlays|
|Active transits|Transits create temporary state overlays|
|Relationship states|Tracked in separate relationship records (see Section 8)|

### The Decision Test

When deciding whether something is static or dynamic, apply this test: **would this value be different if we froze the character at two different points in the narrative?**

If yes: dynamic. It belongs in a state diff. If no: static. It belongs in the base record only.

---

## State Record Format

A state record is a structured data block that describes the delta between the base record and the character at a specific narrative moment.

### Required Fields

|Field|Description|Example|
|---|---|---|
|`character_id`|Character this state belongs to|`victoria_midnight`|
|`state_id`|Unique identifier for this state|`vm_m1b_post_crash`|
|`narrative_moment`|Human-readable description of when|`Movement 1B — immediately after the crash`|
|`movement`|Which movement this state falls in|`m1b`|
|`mc_distance_temporal`|Temporal distance from MC's current scene|`0` (this IS the MC)|
|`mc_distance_narrative`|Causal steps from MC's throughline|`0`|
|`state_version`|Version of this state record|`1.0`|
|`base_record_version`|Version of the base record this diffs against|`1.0.0`|

### Modified Values Block

Only values that differ from the base record appear here. Omitted values are read from the base record.

```
MODIFIED_VALUES:
  WOUND: 8          # was 4 pre-crash
  DRIVE: 12         # was 14 pre-crash
  WILL_EFFECTIVE: 13 # base WILL is 14, reduced under active trauma
  
  L8_IMPRINT:
    primary_attachment_object: brother_deceased  # was brother_alive
    attachment_style_score: 6  # was 7 pre-crash

  L10_SHADOW:
    shadow_density: 7  # was 4 pre-crash
    shadow_content: 
      - culpability_for_brother  # NEW — did not exist pre-crash
      - distrust_of_own_judgment  # NEW
```

### Modified Derived Statistics Block

Derived statistics are recomputed using the modified values. Only statistics that change from the base record appear here.

```
MODIFIED_DERIVED:
  basic_damage_resistance: 10  # 13 - (8/2) — was 11 pre-crash
  stress_threshold: 5          # 13 - 8 — was 10 pre-crash  
  collapse_risk: 6             # (8 + 4) / 2 — was 4 pre-crash
  # note: uses WILL_EFFECTIVE for stress_threshold in state context
```

### Modified Flags Block

Flags are re-evaluated against the modified values. Only flags whose state changes from the base record appear here.

```
MODIFIED_FLAGS:
  KINSHIP_COLLAPSE: FIRED       # was INACTIVE in base
  SHADOW_DENIAL: ACTIVE         # was INACTIVE in base
  TRUTH_VULNERABILITY: ACTIVE   # was INACTIVE in base
```

### State Narrative Note

A brief prose note (2-5 sentences) explaining what happened at this narrative moment that produced these changes. This is the human-readable justification for the diff.

```
STATE_NOTE: >
  The crash kills Jebb. Victoria survives. The wound is not grief — 
  it is the knowledge that she chose not to listen. WOUND jumps from 
  4 to 8. SHADOW content adds culpability and self-doubt. The 
  KINSHIP_COLLAPSE flag fires. All subsequent behavior operates 
  without a secure attachment base.
```

### Character Astrology State Overlay (Optional)

If progressions or transits are active at this narrative moment, they are documented here as chart overlays.

```
ASTROLOGY_OVERLAY:
  progressed_sun: [sign if changed from natal]
  progressed_moon: [current progressed moon sign]
  active_transits:
    - transit_saturn_conjunct_natal_moon: "System audit hitting emotional core"
    - transit_mars_square_natal_saturn: "Kinetic pressure against the wall"
```

---

## State Diff Rules

**Rule 1: Diffs are additive, not destructive.** A state diff adds or modifies values. It never deletes base record fields. If a value returns to its base record level (e.g., DRIVE recovers to VITAL), the state diff for that moment simply omits the field, and the base record value is read.

**Rule 2: State diffs are independent of each other.** Each state diff is computed against the base record, not against the previous state diff. This prevents error propagation. If state M1B has WOUND = 8 and state M3 has WOUND = 9, state M3 is diffed against the base record (WOUND was originally assigned during the Vertical Slice as the entry-point value), not against M1B.

**Rule 3: WILL_EFFECTIVE is a state-only field.** The base record contains WILL (the permanent value). State diffs may contain WILL_EFFECTIVE — the operating WILL under current conditions. The formula for temporary WILL reduction is authored by the narrative designer, not computed automatically. The distinction preserves the permanent value while acknowledging that sustained trauma can temporarily reduce effective psychological resistance.

**Rule 4: Flag re-evaluation is mandatory.** Every state diff must re-evaluate all flag trigger conditions against the modified values. A flag that was INACTIVE in the base record may fire in a state diff. A flag that was ACTIVE in the base record may (rarely) become INACTIVE if the triggering condition is no longer met.

**Rule 5: State diffs are versioned.** If a state diff is revised (because the narrative designer changes what happens at that moment), the old version is archived and a new version replaces it. The base record is never involved in this revision.

**Rule 6: One state per narrative moment per character.** A character does not have two simultaneous state diffs for the same moment. If a narrative moment is subdivided (e.g., M1B pre-crash and M1B post-crash), they are separate states with separate `state_id` values.

---

## Querying a Character at a Narrative Moment

To assemble the complete character at a given moment:

**Step 1:** Load the base record (12-Layer Vertical Slice structured data block).

**Step 2:** Load the state diff for the requested narrative moment.

**Step 3:** Apply the state diff. For every field present in `MODIFIED_VALUES`, replace the base record value with the state diff value. For every field NOT present in the state diff, retain the base record value.

**Step 4:** Apply `MODIFIED_DERIVED` statistics. These replace the base record derived statistics.

**Step 5:** Apply `MODIFIED_FLAGS`. These replace the base record flag states.

**Step 6:** If Character Astrology state overlay exists, apply it alongside the natal chart. The natal chart remains visible. The overlay indicates what is currently active in the narrative sky.

**The result is a complete character record at that narrative moment.** It contains all 12 layers, all derived statistics, all flag states, and (optionally) the chart with active overlays. This assembled record is what a writer, game designer, or AI system reads when working on a scene set at that moment.

---

## State Sources

State diffs are produced by five categories of narrative event. Each category has a characteristic signature in the diff.

### Category 1: Trauma Events

Sudden, high-impact events that produce immediate value changes.

**Signature:** WOUND increases. New shadow_content entries appear. Flags fire. DRIVE may drop. Attachment objects may change.

**Example:** Victoria's crash. WOUND jumps. KINSHIP_COLLAPSE fires. Primary attachment object changes to deceased.

### Category 2: Systemic Pressure Events

Sustained institutional or environmental forces that erode values over time.

**Signature:** WILL_EFFECTIVE decreases. SHADOW projection_tendency increases. resistance_index in L11 may decrease (the character is being worn down toward their growth requirement).

**Example:** The Ban. Victoria's social legibility is weaponized against her. WILL_EFFECTIVE drops. SHADOW_DENIAL flag intensity increases.

### Category 3: Relational Events

Bonds forming, deepening, breaking, or transforming.

**Signature:** L8 attachment variables change. L9 variables may shift. New relationship records are created or existing ones are modified.

**Example:** A new bond forms post-crash. attachment_style_score shifts. A new attachment object appears.

### Category 4: Awakening Events

Moments of perception where the character sees something they could not see before.

**Signature:** L11 resistance_index drops sharply. SHADOW shadow_density may drop (integration of previously repressed content). New flag states may fire (EARNED_JUDGEMENT moving from PENDING to ACTIVE).

**Example:** Movement 4 (Bourne). Victoria perceives the structural framework. resistance_index drops. Shadow content begins integrating.

### Category 5: Progression Overlays

Slow-moving internal changes that accumulate between narrative moments rather than firing at a specific event.

**Signature:** Progressed planetary positions change in the astrology overlay. Effective emotional state (Moon progression) shifts gradually. These are background state changes, not event-driven.

**Example:** Between M2 and M3, progressed Moon moves from one sign to the next. The character's emotional default shifts subtly. L8 attachment_style_score drifts by 1 point.

---

## Relationship Records

Relationships between characters are tracked in a separate data structure, not inside either character's record. This prevents the problem of needing to edit Character A's record when something happens to Character B.

### Relationship Record Format

|Field|Description|Example|
|---|---|---|
|`relationship_id`|Unique identifier|`vm_jebb_siblings`|
|`character_a`|First character|`victoria_midnight`|
|`character_b`|Second character|`jebb_midnight`|
|`relationship_type`|Category|`sibling` / `romantic` / `antagonist` / `mentor` / `institutional`|
|`status`|Current state|`active` / `severed` / `transformed` / `dormant`|
|`synastry_data`|Chart comparison data (if both characters have charts)|`[aspect mesh, composite chart variables]`|
|`state_history`|Array of relationship state changes|`[{moment: m1a, status: active}, {moment: m1b_post_crash, status: severed}]`|

### Relationship State Changes

Relationship records carry their own state history — a timeline of status changes keyed to narrative moments. These changes are linked to but not stored inside the character state diffs. When a character state diff notes a change to `primary_attachment_object`, the corresponding relationship record should show a status change at the same narrative moment.

### Synastry Data

If both characters have locked Character Astrology charts, the relationship record includes synastry data — the aspect mesh between the two charts and the composite chart. This data is computed once from the two natal charts and stored in the relationship record. It does not change (natal charts are static). It provides the symbolic foundation for understanding the relationship dynamics.

**Synastry belongs here, not in either character's record.** This is the architectural decision that keeps character records clean while preserving full relationship analysis capability.

---

## Boundaries with plot_systems

This document defines character state tracking. It does not define story structure, scene sequencing, or narrative timeline management. Those belong to plot_systems, which is flagged for future development.

**What this document provides to plot_systems (when built):**

- The state diff format that plot_systems will consume and produce.
- The narrative moment identification scheme that plot_systems will use for timeline coordinates.
- The MC-relative distance fields (`mc_distance_temporal`, `mc_distance_narrative`) that plot_systems will populate.
- The movement tagging system that links character states to macro-arc positions.

**What plot_systems will eventually provide to this architecture:**

- The formal timeline coordinate system (replacing the current freeform `narrative_moment` field with structured temporal keys).
- The movement sequence definition (which moments belong to which movements).
- The scene-to-state mapping (which scenes produce which state diffs).
- The Victoria-as-(0,0) coordinate system for measuring all other characters' temporal and narrative distance.

Until plot_systems is built, state diffs use freeform `narrative_moment` descriptions and authored `movement` tags. The architecture supports the transition to structured coordinates without schema changes.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial state architecture. Establishes static/dynamic boundary, state diff format, diff rules, query assembly protocol, five state source categories, relationship record format, and plot_systems boundaries.|