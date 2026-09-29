---
type: ssot_03_setting_systems
category: state_architecture
version: 1.1.0
last_updated: 2026-09-29
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "RULED 2026-09-29 — BOLO 90 step 3; 1.1.0 2026-09-29: BOLO 90 step 7 trial, RULED 2026-09-29, Chief: 'line up the recs' — Checkpoint 3 gets a told_at note, the backstory movement tag is ruled (not proposed), backward diffs stated as Rule 7"
purpose: "Defines the architecture for tracking place change over narrative time without modifying the static base Setting Slice. Establishes the state diff system for places, the state record format, checkpoints and story points, state sources, faction-card state, and boundaries with the static Setting Slice, the tracking system, and the fabula. Mirrors ssot_02_character_state_architecture layer for layer, the way the Setting Slice itself mirrors the 12-Layer Character Database."
dependencies: ["ssot_03_setting_system", "ssot_02_character_state_architecture", "ssot_08_tracking_system", "ssot_04_fabula", "delta-coast-ultra-school (first instance)"]
---

# 🔮 SSOT: Setting State Architecture

## Table of Contents

1. [Purpose](#1-purpose)
2. [The Core Principle](#2-the-core-principle)
3. [What Is Static vs What Is Dynamic](#3-what-is-static-vs-what-is-dynamic)
4. [State Record Format](#4-state-record-format)
5. [Checkpoints and Story Points](#5-checkpoints-and-story-points)
6. [State Diff Rules](#6-state-diff-rules)
7. [Querying a Place at a Narrative Moment](#7-querying-a-place-at-a-narrative-moment)
8. [State Sources](#8-state-sources)
9. [Faction States](#9-faction-states)
10. [Boundaries](#10-boundaries)
11. [THE INSTANCE — the DCUS rename lattice](#11-the-instance--the-dcus-rename-lattice)
12. [Version History](#12-version-history)

---

## 1. Purpose

Places change over the course of a story the same way characters do. A campus is built, damaged, renamed, sold, rebranded. A faction's grip tightens or slips. The 12-layer Setting Slice ([📐 ssot_03_setting_system.md](📐%20ssot_03_setting_system.md), PART A) captures a place at the point of canonical definition — but the story demands we know what DCUS *is* at its founding as Skeeter Creek, at the Red Hills rename, at the Bishop acquisition, at Movement 4's collapse.

This document defines how to track that change without modifying the static base slice. The architecture is: one immutable base slice per place, plus any number of state diffs keyed to narrative time coordinates. The base slice is the deed and the survey. The state diffs are the renovation history.

This is a direct mirror of [🔮 ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md) v1.2.0. Where that document says "character," read "place." Where it says "layer," read "S-layer." The mirror is deliberate and load-bearing: one query engine should be able to read a checkpoint for a character or a place with the same code.

---

## 2. The Core Principle

**The static Setting Slice never changes.**

The 12-layer Setting Slice (S1–S12) and the slice header represent the place's canonical architecture — what it structurally IS at the point of canonical definition. This record is produced once, locked, and placed in the place's canonical folder (or its canon node, per [_CANON_NODES/delta-coast-ultra-school.md](../../../../_CANON_NODES/delta-coast-ultra-school.md)). It is never edited during story development. If the record needs revision, a new version is created with a documented reason, and the old version is archived — exactly as [📐 ssot_03_setting_system.md](📐%20ssot_03_setting_system.md) already does with its own version history.

**Place states are overlays.** A state record describes what is different about the place at a specific narrative moment compared to its base slice. It does not duplicate the base slice. It lists only the S-layer values, header fields, and flags that have changed, and the reason for the change.

**The base slice plus a state diff equals the place at that moment.** To know what DCUS is at the Red Hills rename, read the base slice and then apply the Red Hills-rename state diff. The result is the complete place at that point in the story.

---

## 3. What Is Static vs What Is Dynamic

Setting inherits the mirror's shape from character state (§3 of ssot_02), but not its static/dynamic split field-for-field. A layer's mirror partner's static-ness does not transfer automatically — S1 BODY mirrors L1 CORE, but where CORE never changes within a story arc, a building can be demolished. Each S-layer is judged on its own terms, using the same test.

### Static (Lives in the Base Slice, Never Changes)

| Data | Reason |
|---|---|
| S7 FOUNDING | Historical record — who built it, why, the founding stack. Origin does not change; it is history, the same reasoning as L7 ORIGIN. (The present-tense-bite test, ssot_03 §S7, governs whether a founding fact still *bites now* — that is a reading, not a rewrite of the fact.) |
| S12 FUNCTION binding | The storyform Domain a place embodies is fixed for that storyform, the same reasoning as L12 FUNCTION. A place may hold multiple S12 records keyed by `storyform_id` if it serves more than one storyform, but each one is fixed once bound. |
| Scale class (Axis 1) | A campus does not become a room. Axis 1 SCALE is structural, not narrative. |
| Parent/child place links | Structural nesting, not narrative content. |
| Canon node link | Administrative pointer. |
| The historical fact that a name was once used | That Skeeter Creek was the founding name is a permanent fact once it happens. What changes is which name is *live* — see Dynamic, below. |

### Dynamic (Lives in State Diffs)

| Data | Reason |
|---|---|
| S1 BODY | Construction, demolition, renovation, and damage change the physical fabric. The border/seam sub-field (ssot_03 §S1) can also change — a passageway can open or close. |
| S2 WEATHER — functional/experiential reading only | The climate facts (Gulf heat, hurricane season, day/night rhythm) are a static baseline. What the weather *means* — who gets relief from it, what it costs — is dynamic, split the same way L8 IMPRINT splits `conditional_patterns` (static) from `attachment_style_score` (dynamic). DCUS's own S2 arc is the worked case: "brochure weather (M1, Anchor + Mood) → a cost (M2–4, Pressure + Argue)" (ssot_03 §S2). |
| S3 SENSORIUM | The presentation surface shifts with institutional change — DCUS's own six-movement palette descent, clean → NEON-ROT, is a state track by definition. |
| S4 LAW | Governance and institutional mechanics change with regime and ownership. |
| S5 SCAR | **Accretes.** Damage, erasure, and rename entries are added; none is ever removed or overwritten, even when a later era's telling changes how an old scar reads. See Rule 1a, §6. |
| S6 ECONOMY | Resource flows, funding models, and ownership capital change — the ownership-change category, §8. |
| S8 HABIT | Patterned life shifts with population and regime — who belongs, what the rituals are, changes when the people holding them change. |
| S9 ALLURE | The place's promise can be dismantled, intensified, or replaced — mirrors L9 EROS, fully dynamic. |
| S10 UNDERSIDE | Tier shifts: a fact moves from secret to folk to public (or the reverse) under narrative pressure — mirrors L10 SHADOW's surfacing/deepening. |
| S11 VECTOR | Trajectory by definition — updated at each checkpoint as the setting arc advances. |
| Header: live name / active aliases | Changes at a rename event. This is the field a scrub test reads — §11. |
| Header: state track pointer | Which `state_id` is current for a given narrative moment. |

### The Decision Test

Same test as the character doc, read for a place: **would this value be different if we froze the place at two different points in the narrative?**

If yes: dynamic. It belongs in a state diff. If no: static. It belongs in the base slice only.

---

## 4. State Record Format

A state record is a structured data block that describes the delta between the base slice and the place at a specific narrative moment.

### Required Fields

| Field | Description | Example |
|---|---|---|
| `place_id` | Place this state belongs to | `dcus` |
| `state_id` | Unique identifier for this state | `dcus_red_hills_rename` |
| `origin_event` | The fabula event that produced this state. An `event_id` from [📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md), grammar `<movement>_<slug>`. `null` only for Category 5 progression overlays, which have no single event. ⧗ when no fabula record exists yet — see §11 | `⧗ backstory_red_hills_rename` |
| `told_at` | A list of time codes ([📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) §4) marking every point the audience is shown this state on the grid. An empty list means the state is true but offstage | `["M3 · S06 \| 021.1.1"]` or `[]` |
| `narrative_moment` | Generated from the time code, not authored. A readable label only, produced from `origin_event` and `told_at` so it can never drift from the real coordinate | `The first erasure — Skeeter Creek sanded to Red Hills` |
| `movement` | Which movement this state falls in, where one applies. Deep past with no Mn to file under carries the ruled `backstory` tag (RULED 2026-09-29, BOLO 90 step 7 trial) — see §11 | `backstory` |
| `state_version` | Version of this state record | `1.0` |
| `base_slice_version` | Version of the base slice this diffs against | `1.4.1` |

### The State Diffs Parent

The three blocks below sit under one parent field, `state_diffs:`, mirroring the character doc's `state_diffs` parent exactly.

```yaml
origin_event: dcus_red_hills_rename
state_diffs:
  MODIFIED_LAYERS:  { ... }
  MODIFIED_HEADER:  { ... }
  MODIFIED_FLAGS:   { ... }
```

### Modified Layers Block

Only S-layer values that differ from the base slice appear here. Omitted layers are read from the base slice. This is the setting equivalent of the character doc's `MODIFIED_VALUES` — renamed because a place's dynamic content is S-layer content, not a stat block.

```yaml
MODIFIED_LAYERS:
  S5_SCAR:
    - skeeter_creek_sanded_to_red_hills   # NEW — accretes, see Rule 1a
  S6_ECONOMY: "grandfather-vs-son ownership war; prestige-based, pre-Bishop"  # was Bishop acquisition capital in base
  S8_HABIT: "alumni-legacy bloc forming under a single ownership line; no Sync-era cohort yet"  # was split alumni/Sync loyalty in base
```

### Modified Header Block (renames)

This block has no character-doc analog — it is setting-specific, standing in the character doc's second-block slot (`MODIFIED_DERIVED`). A place's header carries names and aliases; a character's derived stats do not need a place-shaped equivalent. Only header fields that differ from the base slice appear.

```yaml
MODIFIED_HEADER:
  live_name: "Red Hills Academy"                       # was "Delta Coast Ultra School (DCUS)" in base
  aliases_active: ["Red Hills Academy", "The Academy"]
  aliases_legacy: ["Skeeter Creek"]                     # historical, still true, no longer live
```

### Modified Flags Block

Flags are re-evaluated against the modified values, mirroring the character doc exactly. Setting does not yet have a ruled flag taxonomy the way character has (`KINSHIP_COLLAPSE`, `SHADOW_DENIAL`); this block is reserved and stays empty until one exists. Cite the gap rather than inventing flags to fill it.

```yaml
MODIFIED_FLAGS: {}   # reserved — no place-flag taxonomy ruled yet
```

### State Narrative Note

A brief prose note (2–5 sentences) explaining what happened at this narrative moment. Same format as the character doc.

```
STATE_NOTE: >
  The son sells his father's century of Red Hills prestige for spoils. The
  Bishops rename it DCUS the way the world's core system overwrites a
  process — a rebrand as Boot Sequence, done to a campus. S5 SCAR takes its
  second entry: the erasure that sanded Skeeter Creek to Red Hills now
  happens again, Red Hills to DCUS. The live name flips.
```

---

## 5. Checkpoints and Story Points

Everything above this line is a **checkpoint**: a complete state at a fabula event, mirroring the character doc's own §Checkpoints and Story Points (v1.2). A checkpoint re-derives every S-layer value and header field that changed; that weight is right for a fabula event and too heavy for a single-field tick between events.

Single-field changes are **story points** and do not live in this document — they live in [📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) §5, `subject.kind: place`. A trait like S9 ALLURE's promise doesn't have to jump in one checkpoint; it can tick down across several story points between the founding checkpoints and a collapse checkpoint, `ramp: true` for a value like S9's glamour that fades rather than flips.

**Rule 6, amended (mirrors ssot_02 v1.2):** "one state per narrative moment per place" applies to checkpoints. A moment may carry many story points for the same place without either bordering checkpoint being revised.

---

## 6. State Diff Rules

Six rules, mirroring the character doc's six exactly, adapted for places.

**Rule 1: Diffs are additive, not destructive.** A state diff adds or modifies values. It never deletes base-slice fields. If a value returns to its base-slice level, the state diff for that moment simply omits the field, and the base-slice value is read.

**Rule 1a: S5 SCAR is append-only, a special case of Rule 1.** A scar diff may add an entry. It may never remove or overwrite a prior entry, even when a later era's telling changes how an old scar reads. Skeeter Creek's erasure stays on record even after DCUS's rebrand adds a second entry on top of it — the scar accretes, it does not replace.

**Rule 2: State diffs are independent of each other.** Each state diff is computed against the base slice, not against the previous state diff. A checkpoint dated earlier than the base slice's own moment (see §11, "diffing backward") still diffs against the base slice, not against a later checkpoint — this prevents error propagation the same way it does for character state.

**Rule 3: WEATHER_EXPERIENCED is a state-only field, mirroring the character doc's WILL_EFFECTIVE special case.** The base slice's S2 WEATHER holds the permanent climate facts. State diffs may contain a `WEATHER_EXPERIENCED` value — the functional read of weather under current institutional conditions (who gets relief, what it costs). The formula, if any, is authored by the narrative designer, not computed automatically.

**Rule 4: Flag re-evaluation is mandatory once a place-flag taxonomy exists.** Every state diff must re-evaluate all flag trigger conditions against the modified values. Until a taxonomy is ruled (§4, Modified Flags Block), this rule is prospective.

**Rule 5: State diffs are versioned.** If a state diff is revised, the old version is archived and a new version replaces it. The base slice is never involved in this revision.

**Rule 6: One checkpoint per narrative moment per place.** A place does not have two simultaneous checkpoints for the same moment. This rule governs checkpoints only (§5) — story points may be many per moment.

**Rule 7: Backward diffs are allowed (RULED 2026-09-29, BOLO 90 step 7 trial, "line up the recs").** A place's base slice is whatever state canon describes — not necessarily its earliest chronological state. DCUS's own base slice (§11, below) is written at the current DCUS/Bishop era, not the founding. A checkpoint dated earlier than the base slice's own narrative position diffs *backward*: each field is modified to its earlier value, the same additive shape as Rule 1, nothing deleted. §11's "A note on direction" flagged this as a new usage pattern when it first appeared; it is now the rule, for places and, by the same reasoning, for characters ([🔮 ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md) carries the mirrored line).

---

## 7. Querying a Place at a Narrative Moment

To assemble the complete place at a given moment:

**Step 1:** Load the base slice (the 12-layer Setting Slice plus its header).

**Step 2:** Load the checkpoint at or nearest before the requested time code. Unlike a character, who typically has a checkpoint authored close to every moment a scene visits them, a place holds continuously — most of the story, nothing about it changes. The correct checkpoint is the most recent one at or before the requested moment, per ssot_08 §5's step behavior (a value holds at its last point until the next one).

**Step 3:** Apply `MODIFIED_LAYERS`. For every S-layer present, replace the base-slice value with the state-diff value. For every S-layer not present, retain the base-slice value.

**Step 4:** Apply `MODIFIED_HEADER`. This determines which name is *live* for narration at this moment — the field the scrub test (§11) exists to guarantee is read correctly.

**Step 5:** Apply `MODIFIED_FLAGS`, once any exist.

**Step 6:** Apply any story points logged between the checkpoint found in Step 2 and the requested moment (ssot_08 §5) — single-field ticks that haven't yet been folded into a new checkpoint.

**The result is a complete place record at that narrative moment.** It contains all twelve S-layers, the header (with the correct live name), and any flag states. This assembled record is what a writer or AI system reads when working on a scene set at that moment.

---

## 8. State Sources

State diffs for a place are produced by five categories of narrative event, mirroring the character doc's five-category structure.

### Category 1: Construction/Damage Events

**Signature:** S1 BODY changes (a structure built, damaged, or demolished). S5 SCAR may accrete an entry if the damage is not repaired. S11 VECTOR may shift.

**Example (hypothetical, ⧗):** a wing of DCUS damaged in a hurricane, left unrepaired as a budget signal — S1 changes, S5 gains an entry, S11's collapse trajectory reads one notch further along.

### Category 2: Institutional Change Events

**Signature:** S4 LAW changes (new governance, new mechanics). S8 HABIT shifts (rituals and routines change with the regime). S12 FUNCTION is untouched unless a new storyform enters — the binding is fixed per storyform, not per policy.

**Example:** the Administration installing Star-Rating and Feed-linked clothing — S4 changes; S8's belonging gradient reorganizes around Sync-era mechanics.

### Category 3: Ownership Change Events

**Signature:** S6 ECONOMY changes (capital flow, funding model, who owns it). S9 ALLURE may shift — a new owner pitches a new promise. `MODIFIED_HEADER` may also change if the ownership change includes a rename.

**Example:** the Bishop acquisition of Red Hills Academy — S6 flips from a prestige-endowment model to acquisition capital converting prestige into product.

### Category 4: Rename/Erasure Events

**Signature:** `MODIFIED_HEADER` changes (the live name flips). S5 SCAR accretes (Rule 1a — a new entry, never a replacement). S10 UNDERSIDE may gain a tier-shift entry — the old name sinks from public to folk or secret.

**Example:** Skeeter Creek → Red Hills, and Red Hills → DCUS — THE INSTANCE, §11.

### Category 5: Seasonal/Cyclic Events (Progression Overlay)

**Signature:** No single event triggers it. S2 WEATHER's dynamic sub-value drifts with season or cycle — background state change, not event-driven, mirroring the character doc's astrology progressions.

**Example:** hurricane season arriving across M2–M4 without a dated trigger event; the Gulf heat's functional cost (§3, S2) intensifies gradually rather than at one checkpoint.

---

## 9. Faction States

A FACTION / NATION CARD ([📐 ssot_03_setting_system.md](📐%20ssot_03_setting_system.md), §THE FACTION / NATION CARD) is not a place, but its fields change the same way a place's S-layers do: a card is static at authoring, and a state diff can modify any field (`binding_principle`, `government`, `economy_tier`, `border_seam_rating`, `one_secret`) keyed to the same `origin_event` / `told_at` / time-code shape as a place checkpoint. Rule 6 applies per faction — one checkpoint per moment per faction, and a faction may carry story points between checkpoints the same way a place does.

**Worked case (ssot_03, THE INSTANCE):** the Bishops' `border_seam_rating` reads low-friction at the Red Hills acquisition (an open purchase) and high-friction once DCUS is live ("saying 'Red Hills' is a legibility violation," ssot_03 §THE BISHOPS). That's a state diff on the faction card, not a new card — the same architecture as a place's header rename, applied to one field of a bounded stat block instead of a slice.

---

## 10. Boundaries

This document defines place state tracking: the base-slice/diff split, the record format, the diff rules, and the query protocol. It does not own the following, each of which belongs elsewhere:

- **The grid, the time code, and the checkpoint/story-point split** live in [📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) — exactly as they do for character state (ssot_02 v1.2, its own Boundaries section). `told_at` and the time code this document's checkpoints carry are ssot_08's fields, read the same way.
- **World events** live in [📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md). Every event, including a rename, is an `event_id` in the fabula's registry; a place checkpoint points to one through `origin_event`, the same field character checkpoints use. Where no fabula record exists yet, `origin_event` is marked ⧗ proposed rather than invented as canon — see §11.
- **The DCUS eras themselves are not re-authored here as a new timeline.** The fabula's own ruling already settled this (ssot_04_fabula.md, OPEN call 4, RULED 2026-09-24): "the setting doc stays the one authoring surface" for the Skeeter Creek → Red Hills → DCUS lattice; the fabula only cross-references it. This document is additive to that boundary — it gives the lattice its formal checkpoint shape for the first time, still authored in the setting system.

---

## 11. THE INSTANCE — the DCUS rename lattice

The first instance of this architecture, built entirely from existing canon: [📐 ssot_03_setting_system.md](📐%20ssot_03_setting_system.md) THE INSTANCE (base slice, v1.4.1), [_CANON_NODES/delta-coast-ultra-school.md](../../../../_CANON_NODES/delta-coast-ultra-school.md) (the ruling and the fusion table), and [📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md) THE WORLD CLOCK, which already reads the lattice as three eras and explicitly declines to re-author them (§10, above).

**A note on direction.** Tori's checkpoints (ssot_04_fabula.md, THE INSTANCE) all move forward from an early moment toward story-present. DCUS's base slice (ssot_03 v1.4.1) is already written at the *current* era — its S4 LAW, S6 ECONOMY, and S9 ALLURE content describes the Administration, the Bishops, and the Feed, all DCUS-era-only facts. The two earlier checkpoints below therefore diff *backward*: they show what the base slice's dynamic layers looked like before they held their current values. This stays legal under Rule 1 — nothing is deleted, each field is modified to its earlier value — but it is a new usage pattern this document is the first to need, flagged here originally; **RULED 2026-09-29 as Rule 7 (§6)** — backward diffs are now legal by rule, not merely an allowed-but-unlabeled usage.

**A note on `origin_event`.** No fabula record exists for any of the three transitions. The fabula's own world clock is explicit: "No calendar date exists in these sources for any of the three transitions; this doc records reach and extent as ranges... and does not invent a year" (ssot_04_fabula.md, THE WORLD CLOCK). All three `origin_event` values below are therefore ⧗ proposed, offered in the fabula's `backstory_<slug>` grammar, not yet entered in the fabula's own registry. **RULED 2026-09-29 (BOLO 90 step 7 trial, "line up the recs"):** the `backstory` movement tag and `backstory_<slug>` event-id grammar are now the rule, not a proposal, for deep pre-M1 history with no Mn ([📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) §2 states it too) — the ⧗ on these three values marks only that the fabula's own registry has no entry for them yet, not that the grammar itself is unsettled.

**A note on `movement`.** The fabula's `<movement>_<slug>` grammar and `movement` field assume every event lands in some `Mn`, even a pre-story one (Tori's crash carries `movement: "M1B"` despite a `reach` of "pre-story"). DCUS's founding lattice has no such mapping — it is a century-plus of history with no scene, movement, or reach relative to any Mn. `movement: "backstory"` below carries the ruled tag for exactly this case (RULED 2026-09-29, BOLO 90 step 7 trial): events before M1 take `movement: "backstory"` instead of an `Mn`, with event ids in that stratum reading `backstory_<slug>`.

### Checkpoint 1 — the founding, as Skeeter Creek

```yaml
place_id: dcus
state_id: dcus_skeeter_creek_founding
origin_event: "⧗ backstory_skeeter_creek_founding"   # proposed; no fabula record exists
told_at: []   # true but offstage; no scene card exists yet to log a time code
narrative_moment: "The founding — before either erasure"
movement: "backstory"   # ruled tag for deep pre-story history with no Mn (RULED 2026-09-29) — see note above
state_version: "1.0"
base_slice_version: "1.4.1"

state_diffs:
  MODIFIED_LAYERS:
    S5_SCAR: []   # no erasure has happened yet — the base slice's two-entry scar list does not exist here
    # S1, S2, S3, S4, S6, S8, S9, S10, S11 stay thin per the fill rule (ssot_03 PART A):
    # no scene has yet needed to know DCUS's fabric, law, economy, or allure at this era beyond
    # the two facts the founding and fabula docs already state (S7 FOUNDING, static, and S5 above).

  MODIFIED_HEADER:
    live_name: "Skeeter Creek"
    aliases_active: ["Skeeter Creek"]
    aliases_legacy: []   # nothing to bury yet — this IS the unburied name

  MODIFIED_FLAGS: {}   # reserved, no taxonomy

STATE_NOTE: >
  Before any rename, the place is Skeeter Creek — the founding stratum
  [delta-coast-ultra-school.md](../../../../_CANON_NODES/delta-coast-ultra-school.md)
  names as "renamed 2026-09-24" fact, was Red Stick Creek. No scene has been
  carded for this era; the checkpoint exists to anchor the lattice's start,
  not to fill layers no scene has pressured yet.
```

### Checkpoint 2 — the first erasure, Skeeter Creek sanded to Red Hills

```yaml
place_id: dcus
state_id: dcus_red_hills_rename
origin_event: "⧗ backstory_red_hills_rename"   # proposed; no fabula record exists
told_at: []   # true but offstage; Movement 3's forensic mode is expected to surface this
              # (ssot_03 §S10 UNDERSIDE: "the first name under the second") but no scene card
              # exists yet, so no time code can be logged
narrative_moment: "The first erasure — Skeeter Creek sanded to Red Hills"
movement: "backstory"   # ruled tag (RULED 2026-09-29) — see note above
state_version: "1.0"
base_slice_version: "1.4.1"

state_diffs:
  MODIFIED_LAYERS:
    S5_SCAR:
      - skeeter_creek_sanded_to_red_hills   # NEW — first accretion; a century-scale erasure
    S6_ECONOMY: "grandfather-vs-son ownership war; prestige-based, pre-Bishop"
      # was "Bishop acquisition capital; prestige converted to product" in base
      # source: delta-coast-ultra-school.md, WHAT FUSED — Red Hills lineage
    S8_HABIT: "the alumni-legacy student bloc forms; split faculty loyalties begin under a single ownership line, no Sync-era cohort yet"
      # was the alumni-legacy-vs-Sync-era split in base; here it's the origin of that bloc, not yet the split itself
      # source: delta-coast-ultra-school.md, WHAT FUSED — Red Hills lineage
    S9_ALLURE: "⧗ old-money prestige draw — a century of private standing, pre-Feed, pre-meritocratic-promise reframing"
      # inferred from "100+ year private prestige school" (delta-coast-ultra-school.md);
      # the Feed and the meritocratic-promise framing (base S9) don't exist until the Bishops
    S10_UNDERSIDE: "⧗ Skeeter Creek sinks from stated name to folk/secret tier — legacy speech may still carry it, but it is no longer the name on record"
      # inferred from the S5/S10 cross-reference pattern (ssot_03 §S5, §S10); not a direct quote

  MODIFIED_HEADER:
    live_name: "Red Hills Academy"
    aliases_active: ["Red Hills Academy", "The Academy"]
    aliases_legacy: ["Skeeter Creek"]   # buried, still true, no longer live

  MODIFIED_FLAGS: {}   # reserved, no taxonomy

STATE_NOTE: >
  The founding name is sanded to Red Hills a century before the Bishops
  arrive (ssot_03 §S7 FOUNDING). This is the erasure S5 SCAR calls the first
  of two. Ownership stays inside the founding line — the grandfather-vs-son
  war is a Red Hills-era fact (delta-coast-ultra-school.md, WHAT FUSED), not
  yet a Bishop-era one. The live name flips from Skeeter Creek to Red Hills.
```

### Checkpoint 3 — the second erasure, the Bishop acquisition and the DCUS rebrand

```yaml
place_id: dcus
state_id: dcus_bishop_rebrand
origin_event: "⧗ backstory_dcus_rebrand"   # proposed; no fabula record exists
told_at: []   # true but offstage; the ownership war and the rebrand are referenced across
              # M1-M4 by the base slice itself, but no single scene card logs the moment
              # of acquisition, so no time code can be given
narrative_moment: "The second erasure — Red Hills sanded to DCUS, the Bishop acquisition"
movement: "backstory"   # ruled tag (RULED 2026-09-29) — see note above
state_version: "1.0"
base_slice_version: "1.4.1"

state_diffs:
  MODIFIED_LAYERS: {}
    # No delta from the base slice. This checkpoint's moment IS the base slice's own dated
    # position (ssot_03 THE INSTANCE, v1.4.1, is already written at the DCUS/Bishop era) — S4
    # LAW, S6 ECONOMY, S8 HABIT, S9 ALLURE, S10 UNDERSIDE, and S11 VECTOR all already hold
    # their DCUS-era values in the base slice. Per Rule 1, a value equal to base is simply
    # omitted, not restated.

  MODIFIED_HEADER:
    live_name: "Delta Coast Ultra School (DCUS)"
    aliases_active: ["DCUS", "the Ultra School"]
    aliases_legacy: ["Red Hills Academy", "Skeeter Creek"]
    # matches the base slice's own header exactly — restated here because this checkpoint
    # is the event that PRODUCES that header state, not because it differs from it

  MODIFIED_FLAGS: {}   # reserved, no taxonomy

STATE_NOTE: >
  The son sells his father's century of Red Hills prestige for spoils, to
  the Bishops. The rebrand is the world's Boot Sequence at institutional
  scale, done to a campus (delta-coast-ultra-school.md, PROVISIONAL TISSUE).
  S5 SCAR takes its second entry — the erasure that sanded Skeeter Creek to
  Red Hills now happens again, Red Hills to DCUS ("erasure done twice,"
  ssot_03 §S5). The live name flips a second time. Because the base slice
  is already written at this era, this checkpoint's own layer diff is
  empty — it is the moment the base slice's DCUS-era content became true,
  not a departure from it.
```

**A note on `told_at` (RULED 2026-09-29, BOLO 90 step 7 trial).** The M2 grief-outburst sequence (`_tools/bolostatus/work/90/TRIAL-M2-grief.md`) is this checkpoint's first onstage attestation of the Administration's routine-diagnostic mechanic — the first carded scene to put S4 LAW's DCUS-era content in front of the audience at all. Its time code is a candidate addition to `told_at` above, pending only on the scene's own address being fixed ([📐 ssot_08_tracking_system.md](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) §4's `Q`/`S` grammar) — not added now.

### The scrub test (ruled 2026-09-24)

[delta-coast-ultra-school.md](../../../../_CANON_NODES/delta-coast-ultra-school.md) rules the rename lattice itself on 2026-09-24 ("RENAMED 2026-09-24, Chief: the founding stratum is Skeeter Creek... The lattice now reads Skeeter Creek → Red Hills → DCUS"). That ruling is a naming fact; this document turns it into a mechanical test any query engine over this architecture must pass:

**Scrubbing the timeline past a rename's time code must flip the place's live name in every view that reads it.** A view that reads only the base slice's header will show "DCUS" even while playing back a Skeeter Creek-era or Red Hills-era scene — that is the exact failure `MODIFIED_HEADER` exists to prevent. Querying DCUS at Checkpoint 1 or Checkpoint 2 (above) must return "Skeeter Creek" or "Red Hills" as the live name, per §7 Step 4, not "DCUS" read straight off the base slice. Scrubbing forward past Checkpoint 3's time code (once one exists) flips it back to "DCUS." The base slice never changes; only which checkpoint's `MODIFIED_HEADER` is currently in force changes what a scene, a card, or an inspector panel displays as the name.

---

## 12. Version History

| Version | Date | Changes |
|---|---|---|
| 1.1.0 | 2026-09-29 | RULED 2026-09-29, Chief: "line up the recs" (BOLO 90 step 7 trial). Checkpoint 3 (§11) gets a note: the M2 grief sequence is its first onstage attestation of the Administration's diagnostic, time code pending. `movement: "backstory ⧗"` reworded to `movement: "backstory"` throughout (§4 table, all three checkpoints, the "note on movement" paragraph) — the tag is now ruled, not proposed; `origin_event` values stay ⧗, unchanged, since the fabula's own registry still has no entry for these transitions. §6 gains Rule 7: backward diffs are allowed by rule, not merely an unlabeled usage; §11's "note on direction" updated to point at it. Additive; no field removed. |
| 1.0.0 | 2026-09-29 | Initial document. BOLO 90 step 3, RULED 2026-09-29 ("Recommendations"): mirrors ssot_02_character_state_architecture v1.2.0 for places — the core principle (static base slice vs dynamic diffs), the per-S-layer static/dynamic table (S5 SCAR accretes, S7 FOUNDING static, header names dynamic), the state record format (`place_id`/`state_id`/`origin_event`/`told_at`/`narrative_moment`/`movement`/`state_version`/`base_slice_version`), the `state_diffs` parent (`MODIFIED_LAYERS`/`MODIFIED_HEADER`/`MODIFIED_FLAGS`), the six diff rules (Rule 1a for S5's append-only accretion, Rule 6 amended to checkpoints only), checkpoints and story points per ssot_08, the query protocol, five state-source categories (construction/damage, institutional change, ownership change, rename/erasure, seasonal/cyclic), a short faction-state section, and boundaries with ssot_08 and the fabula. THE INSTANCE: the DCUS rename lattice as three checkpoints (Skeeter Creek founding → Red Hills rename → DCUS/Bishop rebrand), all three `origin_event` values ⧗ proposed pending a fabula ruling, the 9/24-ruled scrub test stated as a mechanical requirement. |
