---
title: "The plot system (syuzhet): reference"
type: reference
for: "A writer or maintainer looking up a plot-system axis, P-layer, card field, told-order mode or rule."
does: "Lists every component and part of the plot system with its fields, values and rules."
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_plot_system.md
source_version: 1.3.2
---

**Who it's for:** a writer or maintainer looking up a plot-system field · **What it does:** lists each component, part and field · **Type:** reference

# The plot system (syuzhet): reference

Frontmatter: category `plot_system`, tier `narratology`, trunk BLACK, rung standard, `applies_to: [all IPs]`, last updated 2026-10-04. This doc is the told-order third of the plot system. The other two are the [fabula](../ssot_04_fabula/2-reference.md) (world time) and the [trope graph](../ssot_04_trope_graph/2-reference.md) (the rails). Read the Touchstones register first.

**Owns:** the told order, turns, escalation, the twelve-layer PLOT SLICE, the PLOT CARD.
**Does not own:** world time (fabula), legal moves (trope graph), structure (Dramatica), psychology (the character database), place (03).

**Root claim:** plot converts the storyform's static checkpoints into felt experience. Every unit runs value-in, turn, value-out at some rung of the ladder. A unit that does not turn is exposition, description or scenery.

## MIND MODELS

- **Diagram 1.** Root: the syuzhet. Branches: Taxonomy (four axes), The Told Order, The Plot Slice (twelve P-layers, P12 from the storyform). The other branches are The Plot Card (paired to the Scene Card), Library (five distills), Boundaries.
- **Diagram 2, five sources, one engine.** All five feed one engine. The five are a Dramatica signpost, McKee's Gap, Coyne's Five Commandments, a Truby step and a Snyder beat. The engine runs value-in, turn, value-out.
- **Diagram 3, the unit up the ladder.** Value-in, turn (driver fires), value-out, which recurs one rung up. The engine runs at R1 BEAT, R2 SCENE, R3 SEQUENCE and R4 ACT.

## PART B · THE TAXONOMY, four axes

### Axis 1 · SCALE, plot units on the existing ladder

Plot units use the containers of ssot_01_scale_ladder. They add what happens inside a container, never a new size class.

| Rung | Container | Completion test |
|---|---|---|
| R1 BEAT | One exchange. | Something tried, answered, slightly changed. |
| R2 SCENE | The smallest container that turns. | A value turn (McKee) and all five commandments (Coyne). |
| R3 SEQUENCE | A chain of scenes on one dramatic question. | The question is answered, usually replaced by a worse one. |
| R4 ACT/MOVEMENT | One throughline's signpost, turned by a driver. | All four throughlines advanced one signpost. |
| R5 STORY | The whole storyform. | All four throughlines complete; Outcome and Judgment delivered. |

### Axis 2 · THE TURN, what changes inside a unit

- **McKee's value turn:** a charged value flips polarity. No turn, no scene.
- **Coyne's polarity:** a scene shifts from a value state to its opposite or its double.
- **McKee's Gap:** a small action provokes a bigger reaction. The gap between expected and necessary holds the turn.
- **R2 floor:** a value turn plus the five commandments: inciting incident, complication, crisis, climax, resolution. At R1 only the value micro-shift is required.

### Axis 3 · FUNCTION, what a plot unit does for the argument

| Function | What the unit does | Source |
|---|---|---|
| Signpost | Consumes a fixed checkpoint, one per throughline. | Dramatica |
| Journey | Carries a throughline between two signposts. | Dramatica |
| Setup/Payoff | Plants knowledge, then delivers it. | McKee |
| Reveal | Changes what someone knows, building toward a reversal. | Truby; Coyne |
| Reversal | A surprising, redirecting turning point. | McKee; Truby |
| Escalation | Each unit's risk or cost exceeds the last. | McKee; Coyne |

### Axis 4 · DRIVE, drivers and act turns

| Vocabulary | What precipitates the turn |
|---|---|
| Dramatica Driver | Action or Decision. A story-level dynamic. |
| McKee | Inciting Incident and Crisis. |
| Coyne | Inciting Incident, Crisis, Climax, at every unit. |
| Snyder | Page-keyed beats: Catalyst p.12, Break Into Two p.25, Midpoint p.55, All Is Lost p.75, Break Into Three p.85. |

OXO's ruled story-level Driver is Action (spine L3). A unit's local driver may be a Decision. Any rollup to R5 must agree with the ruling.

## PART A · THE PLOT SLICE, twelve layers, mirror of the character and setting stacks

Layer names are house coinage, ruled 2026-09-16. P12 is fed from the storyform.

| Layer | Name | Question | Fields |
|---|---|---|---|
| P1 | ADDRESS | Where does the unit sit on the ladder? | `address` (IP.form.act.sequence.scene.beat); optional `paired_unit` |
| P2 | DRIVER | What precipitates the turn? | `driver_type` (action or decision), `driver_event`, `opposition_goal` (dynamic) |
| P3 | VALUE-IN | What value enters, at what polarity? | `value`, `polarity_in` |
| P4 | TURN | What mechanism flips the value? | `turn_mechanism`; optional `test_phase` (contract, contest, consequence) |
| P5 | VALUE-OUT | What polarity on exit? Is it ironic? | `polarity_out`, `irony_flag` |
| P6 | SIGNPOST/JOURNEY SEAT | Which throughline and act does the unit serve? | `throughline`, `signpost_or_journey`, `act` |
| P7 | REVEAL | What is learned, and does it reverse expectation? | `reveal_content`, `reveal_type` (action or revelation), `reveal_quality` |
| P8 | COLLISION | Which character × setting row fires? | `collision_row` (e.g. L9×S9) |
| P9 | STAKES/ESCALATION | How does risk compare to the last unit? | `stakes_delta` |
| P10 | GENRE OBLIGATION | Which reader-contract obligation does it discharge? | `genre_obligation` |
| P11 | TIME | Order told versus order happened? | `order_told`, `order_happened`, `duration_mode`, `frequency_mode`, `anachrony` |
| P12 | FUNCTION | What does the unit do for the Grand Argument? | `story_point`, `storyform_id` |

**Binding rule.** P12 is keyed by `storyform_id`. A unit with no storyform link may run P1 to P11 only. P12 filled makes the unit load-bearing.

**Folded rules (2026-09-29, 77-AA).**

- **P1 percentage addressing.** `address` may carry a percent-of-manuscript position beside the ladder key.
- **P6 multi-POV stacking.** Several heroes' beats may stack under one manuscript. Record each hero's seat as its own P6 line, keyed to that hero's throughline.
- **P6 told-unit-to-act map (ruled 2026-10-04).** Each story declares its own map once, in its instance file. The map may hold any count of movements. No story borrows another's map. OXO's table is parked: `⏸ OXO signpost seating (phase 2)`.
- **P7 `reveal_quality`.** Aristotle's ranked recognitions, from a scar or token (least artful) to discovery from the actions themselves (best).
- **P1 `paired_unit` (1.3.0).** It pairs an entry unit with its exit unit. The return is the real trial.
- **P2 `opposition_goal` (1.3.0).** `{standing_goal, fallback_if_this_unit_fails}`, dynamic. A recurring villain keeps a goal that survives defeat. A shared failure is procedural, not one villain's plan.
- **P7 hook test (1.3.0).** Every logged fabula event names one present consequence and one live hook. The writer cuts any event that does not. Chain: event, present consequence, live hook. The fabula fields are parked: `⏸ fabula placements (phase 2)`.
- **P7 cascade recipe (1.3.0).** Choose one rule that binds an institution. Show a near-miss. Break it through a personal-scale event. Each step is an existing `cause` or `enable` edge. The collapse has no villain.
- **P9 repeat-turn exception.** A resurrection beat forces a second full pass, so `stakes_delta` may show a repeated peak.
- **P9 first-unit baseline (ruled 2026-10-04).** The first unit of a sequence sets `stakes_delta: baseline`. The trend test starts at the second unit.

**P10 ruling (2026-09-29, BOLO 91).** Story level reads cultcore. Scene level reads Snyder's Institutionalized, then varies by movement:

| Movement | Scene-level obligation |
|---|---|
| M1 | Opening (Snyder's Opening Image and Catalyst register) |
| M2-M3 | Institutionalized |
| M4-M5 | Reversal |
| M6 | War / attrition |

**General rule (ruled 2026-10-04).** Scene-level obligation may vary by movement, and each story states its values in its own instance. Story-level genre stays fixed. OXO's four values are parked: `⏸ OXO genre reading (phase 2)`.

## THE PLOT CARD, the notation slot for one plot unit

The plot card sits beside the SCENE CARD. The scene card carries setting and state. The plot card carries the turn. Four scene-card lines overlap it: `address`, `value turn`, `collision`, part of `threads`. The two stay siblings sharing one `address` key.

Fields: address (P1) · driver (P2) · opposition goal (P2) · value-in (P3) · turn (P4) · value-out (P5) · signpost seat (P6) · reveal (P7) · collision (P8) · stakes delta (P9) · genre oblig (P10) · time (P11) · function (P12).

**Address grammar (ruled 2026-09-29).** The q-scheme `OXO.primary.M2.q1.s3` is legacy. The canonical form is the tracking-system time code `M2 · Q1 · S03 | 012.3.2`. Conversion: `q1.s3` becomes `Q1 · S03`.

**What each field reads.**

| Field | Reads from |
|---|---|
| P2 driver | The fabula event's `event_id` and `transition`. |
| P3 value-in | The state-before half of `transition`. |
| P4 turn | The `cause` or `enable` edge from value-in to value-out. |
| P5 value-out | The state-after half. |
| P6 signpost seat | The trope graph's walk. |
| P7 reveal | A fabula event that was `logged` but untold. |
| P9 stakes delta | The `cause` and `enable` chain back to the prior event. |
| P11 time | `order_happened` is the fabula `time`. `order_told` is this doc's field. |

P1, P8, P10 and P12 are unchanged by the split.

## THE TOLD ORDER

The syuzhet's own record shows where a fabula event surfaces in the telling. It also shows how long the telling dwells and how often it repeats.

- **Pointing at the fabula.** A unit points at one or more fabula `event_id`s and reads their `transition`.
- **order_told versus order_happened.** `order_happened` is the fabula's `time` block. `order_told` is the unit's position in the telling.
- **Anachrony.** Analepsis (earlier than the present position): external, internal or mixed. Internal splits into heterodiegetic and homodiegetic; paralipsis is a lateral omission. Prolepsis (later than the present position).
- **Duration modes.** Scene (about 1:1), summary (compresses), ellipsis (told time zero). The other two are pause (told time runs, happened time holds) and stretch (told time longer).
- **Frequency modes.** Singulative (told once, happened once), repetitive (told more than once, happened once). The third is iterative (told once, happened many times).
- **What P11 measures (ruled 2026-10-04).** `frequency_mode` describes the telling, never the event. The event's repeat lives in the fabula `repeat` flag.
- **Sternberg's three gap effects.** Curiosity (effect shown, cause withheld). Suspense (suspected future outcome withheld). Surprise (unforeshadowed reordering). All three are queries against the fabula, not stored fields.

Template fields: `plot_unit_id`, `event_id`, `order_told`, `order_happened`. It also has `anachrony` (`type`: none, analepsis_external, analepsis_internal, analepsis_mixed, prolepsis; `reach`; `extent`). The last fields are `duration_mode`, `frequency_mode` and `gap_effect` (curiosity, suspense, surprise, none).

## THE INSTANCE, M2 row 9 filled into the plot slice — worked example (phase 2 fills)

Source: oxo-scene-card-M2-row9.md, collision row 9, L9 EROS × S9 ALLURE. Fields marked `⏸ row 9 fill pass (phase 2)` await Chief's story call.

| Layer | Row 9 |
|---|---|
| P1 | `OXO.primary.M2.q1.s3` (legacy q-scheme). |
| P2 | Decision, local to the CR beat: reach or pull out. Fabula pointer `m2_first_sync_verified`. `opposition_goal` parked. |
| P3 | Whole, polarity minus (grey, unranked, control-as-safety). |
| P4 | The Gap: saying "breathe" draws a bigger institutional response. Five commandments present. Pointer `m2_grief_outbursts`. `test_phase` parked. |
| P5 | Whole, minus to plus for Tori's read; owned, plus to minus underneath for the audience. Ironic. |
| P6 | MC throughline, signpost 1, The Past, Movement 2 (re-seated 2026-09-24; Act 1 = M1+M2). |
| P7 | Audience: the hook is a trap (dramatic irony). Tori: a win. Mixed type, action plus revelation ("Verified"). |
| P8 | L9×S9 (seed); echoes rows 6 and 3; seeds row 8. |
| P9 | `stakes_delta: baseline` (first unit). |
| P10 | Story: cultcore. Scene: Institutionalized. |
| P11 | `anachrony.type: none`; duration scene; frequency singulative, though the fabula event is iterative. |
| P12 | Discharges a Requirement toward the OS Goal, Equity (parked). Seeds M3's V-Sync (row 8). `storyform_id: oxo_primary_v1`. |

Result: ten of twelve layers fill from a card written before this doc. P9 needs a prior unit, a scope gap. P10 is a new read.

The fabula holds six Tori events: `m1b_crash_jebb_death`, `m1b_untouchable_resolve`, `m2_recruited`, `m2_first_sync_verified`, `m2_grief_outbursts`, `m3_underground_search`. A singulative unit may zoom in on one member of an iterative record.

## PLOT × LIBRARY

- **`test_phase` (1.2.0).** Greimas's test in threes: qualifying, main, glorifying (CRE.07). Fill it only where the unit's role in a test is in doubt. It sits beside Coyne's commandments. Other CRE.07 cites: P2 `driver_type`, P3, P7 `reveal_type`, P9 `stakes_delta`.
- **Library follow-up (1.3.0).** BVX.1179 (hook test), BVX.1182 (cascade recipe), BVX.0343 (recurring villain goal). The list also holds CRE.08 (paired entry and exit).
- **Feeds.** Dramatica BVX.0089: P1, P2, P6, P12. McKee BVX.0175: P3, P4, P5, P9. Coyne BVX.0236: P4, P9, P10. Truby BVX.0193: P4, P7. Snyder BVX.0163: P10, P11. Vogler BVX.1124: P6, P4. Brody BVX.1125: P1, P6, multi-POV. Aristotle BVX.1126: P4, P7.
- **Templates are instances, not rivals.** Snyder's 15 beats, Truby's 22 steps and Coyne's Foolscap are pre-filled P-layer sequences. None overrides the spine's sixteen signposts.
- **The shelf.** 162 items keyed 9/16 (BOLO 18); five distilled for the first version.

## Other sections

The source also holds OPEN (fifteen calls, all closed or moved to phase 2). It also holds the 1.0 bar (one filled card per movement, M1 to M6). It holds a version history from 0.1.0 (2026-09-16) to 1.3.2 (2026-10-04).
