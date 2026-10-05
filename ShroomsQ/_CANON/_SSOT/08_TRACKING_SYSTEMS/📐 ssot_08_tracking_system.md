---
type: ssot_08_tracking_systems
category: tracking_system
version: 1.2.0
tier: fabula
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "v1.2.0 2026-10-05: RULED, Chief (\"My word\") — BOLO 102 stage 2: new section 4A, The Address (the time code is the one address in every system); `subject.kind` widened; hook ledger and Touchstone breach log in 9A. Earlier: v1.1.0 2026-10-04: RULED, Chief (\"rec\") — BOLO 100 follow-up: proportion lane in §7 (act and third shares, 25/50/25 default) and a reversibility score on stakes_delta. Earlier: v1.0.0 2026-10-04: RULED, Chief (\"REC\") — BOLO 100 tracking/worldbuilding batch 1: theme and trope hooks, tempo and meter shapes, time-code ordering, reader track in the map, open steps closed. Earlier: 0.3.0 reader model (9A); 0.2.0 sequence segment, iterative fields, provisional cables."
purpose: "THE TRACKING SYSTEM: the shared time grid and record model under character state, setting overlays, and world time — the grid (tick · beat · bar · time signature · tempo), the time code, checkpoints and story points, setup → payoff cables, and the Ableton-style track map. One store, many views."
dependencies: ["ssot_01_scale_ladder", "ssot_02_character_state_architecture", "ssot_03_setting_system", "ssot_04_fabula", "ssot_04_plot_system", "ssot_05_worldbuilding_system", "ssot_01_trope_register"]
trunk: BLACK
sources: ["_tools/bolostatus/work/90/DISTILL.md", "BVX.0236 — The Story Grid: What Good Editors Know — Coyne (2015)"]
rung: standard
---

# 📐 SSOT: THE TRACKING SYSTEM — one store, many views

## Table of Contents

1. [What This Is](#1-what-this-is)
2. [The Two Rulers](#2-the-two-rulers)
3. [The Grid](#3-the-grid)
4. [The Time Code](#4-the-time-code)
    - 4A. [The Address](#4a-the-address)
5. [The Records](#5-the-records)
6. [Cables](#6-cables)
7. [Tempo](#7-tempo)
8. [The Ableton Map](#8-the-ableton-map)
9. [Who Consumes This](#9-who-consumes-this)
    - 9A. [The Reader Model](#9a-the-reader-model)
10. [Open](#10-open)
11. [Version History](#11-version-history)

---

## 1. What This Is

Tracking means writing down what's true at one moment, and writing down the event that changed it (DISTILL §1). A moment can be a character, a place, a trope, or the story world itself. Everything downstream — a state query, a setting overlay, a trope firing — reads a starting record and applies every change up to the moment asked about.

**Root claim: one store, many views.** Every dated fact — a checkpoint, a story point, a cable end — is a record in one store. Character state, setting overlays (Axis 4), and the arrangement of scenes are not separate data; they are different views onto the same records, the way Ableton's Session and Arrangement views read the same clips (DISTILL §12, "one store, two views, not two tools"). This document owns the grid, the time code, the two rulers, and the record shapes that view reads.

---

## 2. The Two Rulers

Chief asked whether fabula needs its own store (DISTILL §12). Ruled: one store, two rulers, not two tools.

- **The world clock** is when things happened. The fabula runs on it — `M1`, `M2`… movement-relative dating, locked until something needs finer precision (DISTILL §13, Step 1 call 1; [📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md), THE WORLD CLOCK). It has no bars and no tempo — nobody experiences world time at a pace. Events before M1 carry the movement tag `backstory` instead of an `Mn` (RULED 2026-09-29, BOLO 90 step 7 trial), for deep past history with no Mn to file under — their event ids read `backstory_<slug>` in place of the usual `<movement>_<slug>` ([🔮 ssot_03_setting_state_architecture.md](../03_SETTING_SYSTEMS/🔮%20ssot_03_setting_state_architecture.md) §11 has the worked case).
- **The grid** is when the audience is told. The told order runs on it — ticks, beats, bars, time signature, tempo. Every told unit already points at a fabula event ([📐 ssot_04_plot_system.md](../04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md), THE TOLD ORDER), so nothing is stored twice (DISTILL §12).

**Flip or stack.** One key flips the ruler, the way Ableton flips Session and Arrangement. A split view stacks both, with a cable running from every told unit down to its world event. A flashback is a cable running backward — a told unit early on the grid pointing at a fabula event late on the world clock, or vice versa (DISTILL §12).

**Resources.** The records are small text; a story of a few thousand events and story points loads instantly. The cost is drawing, not storing — semantic zoom (§4) means the tool draws bundles and counts when zoomed out, never every tick (DISTILL §12).

---

## 3. The Grid

The grid is the musical time layer under the timeline — Ableton's bars and beats under every clip. BOLO 35 already ruled music theory as the basis for the story's structural layer (DISTILL §10, citing BOLO 35 9/23, "structure on a score layer"); the grid is that layer, built out.

| Unit | Music | Story |
|---|---|---|
| **Tick** | the smallest subdivision of a beat | one line, one gesture, one look — the smallest thing that happens |
| **Beat** | one count | McKee's beat: one action and its reaction. This is the scale ladder's R1 |
| **Bar** | a group of beats, set by the time signature | a run of beats that lands one push — one tactic tried and answered. Sits between beat and scene |
| **Time signature** | beats per bar (4/4, 3/4, 7/8) | a scene's meter: how many beats it takes to land a push. 4/4 is steady, 3/4 is lilting, 7/8 is off-balance, a lurch. Set per scene; default 4/4 |
| **Tempo (BPM)** | speed | pace — how fast the beats come. Optional; an automation lane (§7) |
| **Scene and up** | sections: verse, chorus | the ladder's rungs: R2 SCENE → R3 SEQUENCE → R4 MOVEMENT… |

**Ruled 2026-09-29** (DISTILL §13):
- **Bar**, not measure — Chief's pick over the recommendation.
- Time signature is set per scene; default 4/4.
- Ticks are counted in order; there is no fixed number of ticks per beat.
- The grid belongs to the tracking system, not the scale ladder. The ladder is unchanged — BEAT stays R1 ([📐 ssot_01_scale_ladder.md](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md), R1 · BEAT) — the grid is the clock the ladder's containers sit on.

---

## 4. The Time Code

A time code is the address of one moment on the grid. Grammar (DISTILL §10, §13; sequence segment RULED 2026-09-29, BOLO 90 step 7 trial):

```
M2 · Q1 · S04 | 012.3.2
```

Read left to right: **movement** (`M2`) · **sequence** (`Q1`) · **scene** (`S04`), then a bar `|`, then **bar.beat.tick** (`012.3.2`).

**Grammar:**
- `M<n>` — movement number, no padding (`M2`, `M12`).
- `Q<n>` — sequence number, no padding (`Q1`, `Q12`) — the R3 SEQUENCE unit the scene sits inside (RULED 2026-09-29, closing the field trial's flagged two-grammar gap; see [📐 ssot_04_plot_system.md](../04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md) for the legacy q-scheme's conversion).
- `S<nn>` — scene number, zero-padded to 2 digits (`S04`, `S23`).
- `<bar>.<beat>.<tick>` — bar zero-padded to 3 digits (`012`), beat and tick unpadded integers within that bar's time signature and that beat's tick count (`3.2`).
- The movement·sequence·scene half and the bar.beat.tick half are joined by ` | `.

**Examples:**
- `M1 · Q1 · S02 | 004.1.1` — Movement 1, Sequence 1, Scene 2, bar 4, beat 1, tick 1 (a scene's opening tick).
- `M3 · Q2 · S09 | 041.2.3` — Movement 3, Sequence 2, Scene 9, bar 41, beat 2, tick 3.

Every story point, cable end, and state change carries one, so any moment is addressable (DISTILL §10).

**Ordering rule.** To sort two time codes, compare movement first, then sequence, then scene, then bar, beat, and tick. Every segment compares as a number, so `M2` sorts before `M12` and `S04` before `S23`. A different told order never changes the world-clock order of events; the world clock (§2) sorts by its own `Mn` dating.

**Zoom stops map to the ladder rungs.** The scroll wheel zooms time, like Premiere's and Ableton's arrangement view; each stop shows the detail that rung holds — semantic zoom, ruled for the rails 2026-09-24 and extended here to the whole tracking system (DISTILL §9 requirement 1, §9 requirement 5).

| Zoom stop | Rung | What the time code shows |
|---|---|---|
| Finest | R1 BEAT | single ticks inside one beat |
| | R2 SCENE | the full bar.beat.tick string inside one scene |
| | R3 SEQUENCE | the address's `Q<n>` segment names the sequence directly (RULED 2026-09-29); scenes bundle under it, bar counts collapse to a scene-level count badge |
| | R4 ACT/MOVEMENT | scenes bundle further under the movement |
| | R5 STORY | movements lay out end to end |
| | R6 NESTED | a nested storyform's own time code runs in a sub-lane |
| | R7 SERIES | stories lay out end to end |
| Coarsest | R8 UNIVERSE | IPs lay out end to end; fabula-only, no grid |

Zoomed out, story points and cables that would overlap bundle into a count badge on the containing clip. Zoomed in, they fan out to the exact tick (DISTILL §9 requirement 5).

---

## 4A. The Address

The time code is the one address for anything dated in any system (IF catalog call 1, ruled 2026-10-05). Every system that dates a fact writes it as a time code. No system keeps a second dating scheme.

**Ladder mapping.** The scale ladder's address names a unit by rung. The time code names the same unit in the same order. Each system that cites a ladder address converts it as the table shows.

| Ladder address segment | Time code segment | Note |
|---|---|---|
| `OXO.primary` (IP · form) | none | The story is named by the track or record that holds the code, not by the code |
| `M2` (movement) | `M2` | Same number |
| `q3` (sequence) | `Q3` | Same number, capital letter |
| `s12` (scene) | `S12` | Same number, zero-padded to 2 digits |
| `b4` (beat) | `bar.beat`, for example `012.4` | The code gives the bar and the beat inside that bar; a tick may follow |

So `OXO.primary.M2.q3.s12.b4` reads `M2 · Q3 · S12 | bar.beat`. Writers address a fact at the rung it lives at. A movement-level fact writes `M2`, and a scene-level fact writes through `S12`. Writers add the bar half only when the fact sits inside a scene.

**Fields that carry the time code.** Each owning document holds its field. This document gives only the address, as it does for hooks in §5.

| Field | Owner | What the time code replaces |
|---|---|---|
| `STT.narrative_moment`; `STT.movement`; `STT.mc_distance_temporal`; `STT.mc_distance_narrative` (IF-00-08-03) | 02 character state | The free-text "when". `mc_distance_temporal` already reads a time code (§9) |
| Relationship `state_history.moment` (IF-02-08-09) | 02 character state | Movement tags such as `m1a` |
| Fabula event `time` (IF-04-08-12) | 04 fabula | Nothing is lost. The time code sits beside the calendar year, and the world clock (§2) still sorts by `Mn` |
| P11 `order_told` (IF-04-08-13); T3 `order_baseline` and its anachronies (IF-01-08-17); medium T3 order (IF-01-08-13) | 04 plot; 01 texture and medium grammars | A bare position in the telling. The time code is the told order, set against the fabula's `order_happened` |
| T4 `duration_mode` and T12 `story_point` (IF-01-08-18); medium T4 speed (IF-01-08-13) | 01 texture and medium grammars | Tempo of each unit reads the §7 `tempo_point`. A T12 story point is a §5 story point |
| Genre `contract_state` entry `from_unit` (IF-01-08-12) | 01 genre system | A bare unit name |
| Collision records and state diffs (IF-01-08-11) | 01 collision engine | A ladder address or span. A state diff is a one-field change, so it is a §5 story point |
| LEDGER_DUE future states | 03 setting state | A free-text due date |
| Hook ledger and Touchstone breach log (§9A) (IF-01-08-14, IF-01-08-16) | 08 | The ladder address. Both ledgers key to time codes |
| Catalog `narrated_in` | 05 worldbuilding | Free text |
| CT5 bookends (IF-05-08-04) | 05 worldbuilding | The one `era` range. A founding endpoint and a current endpoint are two checkpoints, each with a time code |

**Retired aliases.** Free text and movement tags retire as aliases for a time code. A record that still holds one is read as its time code, and the writer replaces it on the next edit. The `backstory` tag (§2) is not an alias. It dates events before M1 on the world clock and stays.

**No SC class.** A time code takes no Base 60 SC class (IF catalog call 8, ruled 2026-10-05; IF-00-08-06). An address names a place on the grid. It is not a scale. Story-point and layer numerics in other systems keep the classes their own documents give them.

---

## 5. The Records

Rule 6 of the character state doc (one state per narrative moment) is too heavy for tick-level tracking (DISTILL §14 call 3). The tracking system splits records into two kinds, the way Ableton splits clips from automation points.

**Checkpoints** are full states at fabula events — what the character, place, or story world doc already builds. A checkpoint is a clip: a complete state at one address.

**Story points** are one-field changes at any time code, not only at logged fabula events — a trait ticks up, a trope fires, a flag flips. A story point is an automation point: a marker on a track at a moment (DISTILL §9 requirement 3, §14 call 3).

**Value behavior between points.** By default a value **steps** — it holds at its last point's value until the next point, the way a switch automation holds in Ableton. A value marked `ramp: true` moves continuously between two points instead, drawn as a slope — for values like tension, attraction, or dread that don't change instantly (DISTILL §14 call 4).

**YAML shape for a story point:**

```yaml
story_point_id: "<slug>"
subject:
  kind: character | trait | trope | place | relationship | theme | gauge | group | belief | custom | tech | wardrobe | architecture | world
  id: "<subject_id>"
field: "<field path>"              # e.g. L5_WOUND.value, a trope_id's status, or motif.<slug>
value: "<new value>"
at: "M2 · Q1 · S04 | 012.3.2"      # the time code (§4)
origin_event: "<fabula event_id>"  # optional — the world-clock anchor, when this point reads from a dated fabula event
ramp: false                        # true = continuous slope to the next point; false/omitted = step (holds until the next point)
repeat_count: "<int>"              # optional — how many times this point's change recurred; used only when frequency_mode: iterative (Genette's "happened many times, told once")
span: "<time-code range>"          # optional — e.g. "M2 · Q1 · S01 | 001.1.1 – M2 · Q1 · S02 | 014.4.3", the range the repeats cover; used only when frequency_mode: iterative
```

**Iterative field (RULED 2026-09-29, BOLO 90 step 7 trial).** `repeat_count` and `span` are additive, optional fields for a story point whose `frequency_mode` (the syuzhet's own field, [📐 ssot_04_plot_system.md](../04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md) THE TOLD ORDER) reads `iterative` — Genette's "told once, happened many times." A `ramp: true` value already draws the slope between two points; `repeat_count`/`span` name how many happenings and what stretch of grid that slope stands for, closing the field trial's flagged gap that `bar.beat.tick` addresses one instant only.

**Subject kinds (IF catalog calls 2 and 3, ruled 2026-10-05).** The first five kinds are the original set. The rest are new.

| `subject.kind` | Holds | Id form |
|---|---|---|
| `theme` | A theme track. 06 names the rails and motifs. A point at a scene's time code records the rail it tests (R1 to R4) and the side it argues (IF-06-08-04). 06's scene card is the source | `holders:` on each 06 rail name 08 track ids; motif points use `field: motif.<slug>` |
| `gauge` | A continuous value lane under a character or world track: the Freedom, Fairness and civilization gauges, each one of four steps (IF-06-08-03, IF-06-08-06). It is an automation lane (§8) | The gauge name |
| `group` · `belief` · `custom` · `tech` · `wardrobe` · `architecture` | A catalog thing from 05 Worldbuilding, with `place` already in the set (IF-05-08-05, IF-05-08-06) | `<kind>:<slug>`; the catalog entry id is `WB-<TYPE>-<nnnn>` |
| `world` | The story world itself, for world-level changes such as a rebrand or a world rule (IF-05-08-07) | `world:<slug>` |

**Which fields a story point may change.** A story point changes only a field the 02 field-tag table marks Dynamic. It never changes a Static field. Derived values are never stored (IF-02-08-11).

**Theme and trope hooks (RULED 2026-10-04, BOLO 100).** A trope is a track of `kind: trope`; its story points use the trope's `id` as `subject.id`. A theme motif is a story point whose `field` is `motif.<id>`. The trope register owns trope ids, and 06 mints the `motif.<slug>` ids (IF-06-08-02). This document gives only the address.

A checkpoint keeps the shape already defined in [🔮ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md) §State Record Format; that shape is unchanged by this document.

---

## 6. Cables

A cable links a setup to its payoff (DISTILL §9 requirement 4). It rides on the fabula's `enable` edge — "A opens the possibility B later realizes" ([📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md), CAUSAL EDGES table) — read as a typed pair rather than a single edge type.

A cable can run between any two tracks (§8), at any distance apart on the grid. A setup with no logged payoff, or a payoff with no logged setup, is flagged an **orphan** rather than silently dropped.

**YAML shape for a cable:**

```yaml
cable_id: "<slug>"
type: setup_payoff
setup:
  track: "<thread id>"           # e.g. character:victoria_midnight, trope:t114
  at: "M1 · Q1 · S02 | 004.1.1"
payoff:
  track: "<thread id>"
  at: "M3 · Q2 · S09 | 041.2.3"
edge: enable                     # the fabula causal-edge type this cable rides on
orphan: none                     # none | setup_no_payoff | payoff_no_setup | provisional
```

**`provisional` (RULED 2026-09-29, BOLO 90 step 7 trial).** A fourth `orphan` value for the case the field trial surfaced: both ends exist narratively — a setup dated, a payoff card drafted — but at least one time code is still unset, so the cable is neither finished (`none`) nor genuinely missing an end. `none` and `provisional` both mean "not an orphan"; `provisional` additionally flags that a real time code is still owed before the cable is load-bearing for scrubbing or the query engine.

Comparing two versions of a passage — Ableton's take-lane sense of "A/B" — is a separate, deferred idea (DISTILL §9 requirement 4, "can come later"; §8 take lanes).

---

## 7. Tempo

The grid itself is automated, like Ableton's tempo lane (DISTILL §11).

- **Tempo curve.** A curve of speed-ups, slow-downs, and ramps drawn on the ruler.
- **Time-signature markers.** A time-signature change is a marker on the ruler, the way Ableton drops a 7/8 marker mid-song.
- **Two tempos, because the story has two clocks** (DISTILL §11):
  - **Story tempo** — how much world time passes per beat. The syuzhet already names the moves this measures: compress, stretch, elide, repeat — Genette's duration (summary, scene, stretch, pause, ellipsis).
  - **Audience tempo** — how fast beats reach the reader or viewer: beats per 1,000 words for prose, beats per minute for screen.
- **Record shapes.** The tool reads two short records for the tempo lane.

```yaml
tempo_point:
  at: "M2 · Q1 · S04 | 012.1.1"   # the time code (§4)
  story_bpm: "<beats per unit of world time>"
  audience_bpm: "<beats per 1,000 words, or per minute>"
  ramp: false                      # true = slope to the next point; false = step

meter_marker:
  at: "M2 · Q1 · S04 | 012.1.1"
  beats_per_bar: 4                 # 3, 4, 7 and so on; the marker holds until the next one
```

- **Planned vs measured lanes.** Chief sets the intended tempo curve; the tool measures the real one from the draft by counting beats against words or seconds. 07.1 reads the planned audience tempo for prose and sets the beat-boundary mark the tool counts (IF catalog calls 6 and 7, ruled 2026-10-05; IF-07-08-02, IF-07-08-03). The gap between the planned lane and the measured lane is the readout — where the draft drags or rushes against the plan.

- **Proportion lane.** A `proportion` lane sits beside the tempo lane. It plans and measures how much of the story each act or third takes (BVX.0236: Beginning, Middle and End average 25/50/25). The default plan is 25/50/25. The tool measures the share from P1 percentage addresses. The readout is the drift between plan and draft.

```yaml
proportion:
  span: act            # act | third
  planned_share: 0.25  # default plan 25/50/25
  measured_share: 0.31 # measured from P1 percentage addresses
```

- **Reversibility score.** P9 `stakes_delta` takes an optional `reversibility` score, 1 to 10. The "trend up" test can then run on numbers.

---

## 8. The Ableton Map

One table maps the whole tracking system onto Ableton's own vocabulary (DISTILL §9 requirement 2).

| Ableton concept | Tracking-system equivalent |
|---|---|
| **Tracks** | Threads — one lane per character, trait, trope, place, or relationship ([📐 ssot_01_scale_ladder.md](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md), THREADS) |
| **Clips / locators** | Rungs — the ladder's containers (R1–R8, §4) |
| **Automation lanes** | Continuous values under a track — a trait's value, tension, a setting layer, a gauge (§5) |
| **Session ↔ Arrangement** | Fabula ↔ told order — the two rulers (§2) |
| **Reader track** | An automation lane per character: the reader's belief and trust over time (§9A) |
| **Take lanes** | A/B version compare — deferred (§6) |

---

## 9. Who Consumes This

- **Character state** ([🔮ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md), v1.2) — checkpoints keep their existing shape; `told_at` and `mc_distance_temporal` now read time codes from this document (see v1.2's own record, §Boundaries with plot_systems).
- **Setting overlays (Axis 4)** ([📐 ssot_03_setting_system.md](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md)) — dated the same way fabula is, per Step 1 call 2 (DISTILL §13): the same world-clock dating this document's §2 defines.
- **Fabula** ([📐 ssot_04_fabula.md](../04_PLOT_SYSTEMS/📐%20ssot_04_fabula.md)) — supplies the world clock and the `enable` edge that cables (§6) ride on.
- **Character state** also reads the reader track: `disclosure` marks what the reader has been shown (§9A). The character system's OPEN call 9 is closed here and moved to §9A.
- **The story workspace** (BOLO 79) — the arrangement view (tracks, rung ruler, playhead, cables) is this document's shell (DISTILL §9, "What this changes in the build order"). 07.3 rules its hover and Info View behavior (IF-07-08-05).
- **The timeline tool** (BOLO 35) — its store-shape fork is answered here: one store, every track reads it (DISTILL §9; see §1 of this document).

**Interfaces.** One line per wiring that another system states.

- Reads from 00 (IF-00-08-01): `T3.IMPRINT.primary_attachment_object` (a character id, `deceased`, `absent` or `none`) is a field a story point may change.
- Read by 05 (IF-05-08-02, IF-05-08-03): each catalog entry's `state: "<08 subject id>"` is a `<kind>:<slug>`. The world-view compiler reads that subject's story points and checkpoints.
- Read by 09 (IF-08-09-01): the character pipeline writes a single-field change between fabula events as a §5 story point, never as a checkpoint.
- Read by 01 texture (IF-01-08-04): the T7 payoff ledger reads `character_id` and `shifted_at` from §9A.
- Read by 07.1 (IF-07-08-01): 07.1 reads the audience tempo (beats per 1,000 words for prose) and the planned and measured tempo lanes from §7.

---

## 9A. The Reader Model

The audience trust ledger (RULED 2026-10-04, BOLO 100, Chief: "all rec"; moved from the character system's OPEN call 9). It sits outside the twelve character layers. It tracks what the reader believes about a character, and how far the reader trusts that belief, over time. The character record holds who the character is; this ledger holds what the reader thinks. The two can differ, and the gap is a source of dramatic irony.

Each entry is one story point (§5) on a reader track. It carries the fields below and no others.

```yaml
reader_entry_id: "<slug>"
character_id: "<subject_id>"       # the character the reader is judging
belief: "<what the reader believes about the character>"
trust: 0                           # 0-10, how far the reader trusts that belief
shifted_at: "M2 · Q1 · S04 | 012.3.2"   # the time code (§4) of the scene where it shifted
disclosure: revealed | concealed   # revealed = the reader has been shown the truth; concealed = the story still hides it
```

**Reading it.** The value steps by default (§5). A scene that moves the reader's belief or trust writes a new entry at its time code. A `concealed` entry with high `trust` marks a lie the reader still holds; the reveal scene flips it to `revealed` and drops `trust`. A cable (§6) can run from the scene that plants a belief to the scene that overturns it.

**Anna's reader track (IF catalog call 2, ruled 2026-10-05).** Anna's reader track lives here. 06 cites it to hold open whether she is a cog, a believer or a mask (IF-06-08-05). Her entries stay `concealed` while the story holds the question open, and the reveal scene flips them to `revealed`.

**Hook ledger (IF catalog call 6, ruled 2026-10-05).** The ledger sits beside the T7 payoff ledger that 01 texture keeps. It tracks serial hooks a container leaves open. Each entry holds the fields below.

```yaml
hook_id: "<slug>"
type: "<P6 hook type>"             # Mystery | Consequence | Thematic Echo | Character | Mechanical
container: "<ladder rung unit>"    # the unit that closes on the hook, as a time code (§4A)
payoff_at: "M3 · Q2 · S09"         # the time code (§4A) where the hook pays off; unset while the hook is open
```

A hook with no `payoff_at` is open, and the tool flags it the way it flags an orphan cable (§6) (IF-01-08-14).

**Touchstone breach log (IF catalog call 6, ruled 2026-10-05).** A breach invalidates every downstream unit that trusted the breached unit. The log records each breach once.

```yaml
breach_at: "M2 · Q1 · S04 | 012.3.2"   # the time code (§4A) of the breach
touchstone_id: "TS 1:3"                # the Touchstone breached, by its TS id
invalidated_units: ["<time code>"]     # downstream units that trusted the breached unit
```

(IF-01-08-16.)

**Sources:** BVX.0279 (Iglesias, the reader's emotion as the thing a script manages) · BVX.1147 (Doležel, the epistemic system: known, unknown, believed; deception keeps the split).

---

## 10. Open

The method is complete. The items below are build work or phase 2, one line each (DISTILL §7 steps 3–7).

- **Setting state full doc** (step 3): ⏸ setting state full doc (phase 2). The setting system owns it.
- **Timeline-tool data model** (step 4): answered. One store, every track a view (DISTILL §9).
- **Trope-graph movements-to-acts map** (step 5): ⏸ trope-graph act map (phase 2). The trope register owns it.
- **Workspace shell** (step 6): a tool build, not method. Build it as an arrangement view first (DISTILL §9).
- **Inspector wiring** (step 7): a tool build, not method. It connects the query-assembly protocol ([🔮ssot_02_character_state_architecture.md](../02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md) §Querying a Character at a Narrative Moment) to the inspector panel.
- **World calendar**: a ruled non-goal (DISTILL §13, Step 1 call 1). The world clock stays movement-relative.

---

## 11. Version History

|Version|Date|Changes|
|---|---|---|
|1.2.0|2026-10-05|BOLO 102 stage 2 (Chief: "My word"): new §4A, The Address (the time code is the one address in every system, the ladder mapping, the fields that carry it, no SC class); `subject.kind` gains `theme`, `gauge`, 05's kinds and `world`; §9A gains Anna's reader track, a hook ledger and a Touchstone breach log; §7 names 07.1 as reader of planned tempo; Interfaces lines in §9.|
|1.1.1|2026-10-04|BOLO 100 D3: Sources line added to §9A (BVX.0279, BVX.1147).|
|1.1.0|2026-10-04|RULED 2026-10-04, Chief ("rec"), BOLO 100 follow-up TR-1. §7 gains the `proportion` lane (`span`, `planned_share`, `measured_share`; 25/50/25 default; measured from P1 percentage addresses) and an optional 1 to 10 reversibility score on P9 `stakes_delta`. Source BVX.0236 cited. Additive.|
|1.0.0|2026-10-04|RULED 2026-10-04, Chief ("REC"), BOLO 100 tracking/worldbuilding batch 1. Theme and trope hooks (§5); `tempo_point` and `meter_marker` shapes (§7); time-code ordering rule (§4); reader track in the map and consumers (§8, §9); §10 rewritten, with the open build steps tagged phase 2 or tool builds; dependencies add the worldbuilding system and trope register. The `provisional` rule reworded to "still unset". Method gaps closed.|
|0.3.0|2026-10-04|RULED 2026-10-04, Chief: "all rec" (BOLO 100 character batch 1). New §9A, the reader model: the audience trust ledger, moved from the character system's OPEN call 9. Fields kept minimal: `character_id`, `belief`, `trust` (0–10), `shifted_at`, `disclosure` (revealed or concealed). Additive; no existing section changed.|
|0.2.0|2026-09-29|RULED 2026-09-29, Chief: "line up the recs" (BOLO 90 step 7 trial). The time code (§4) gains a `Q<n>` sequence segment, `M2 · Q1 · S04 \| 012.3.2`; every time-code example in this document updated. Story points (§5) gain optional `repeat_count` and `span` fields for `frequency_mode: iterative`. Cables (§6) gain a fourth `orphan` value, `provisional` — both ends exist narratively, at least one time code still unset. §2 The Two Rulers notes the `backstory` movement tag for events before M1. Additive; no field removed.|
|0.1.0|2026-09-29|Initial document. BOLO 90 steps 1–2, RULED 2026-09-29 (DISTILL §13, §14): the two rulers (world clock vs grid), the grid (tick/beat/bar/time signature/tempo, "bar" not "measure"), the time code and its mapping to scale-ladder zoom stops, checkpoints and story points as the two record kinds (step vs ramp value behavior), setup → payoff cables on the fabula `enable` edge with orphan flags, tempo curves and two-tempo (story/audience) automation, and the Ableton concept map. Consumers and open build steps recorded.|
