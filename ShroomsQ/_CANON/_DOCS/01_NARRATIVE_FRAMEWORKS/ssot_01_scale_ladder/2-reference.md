---
title: "The scale ladder: reference"
type: reference
for: A writer or builder looking up a rung, thread, address or constraint rule
does: Lists every rung, thread and rule of the scale ladder
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_scale_ladder.md
source_version: 1.1.0
---

**Who it's for:** a writer or builder looking up a ladder fact · **What it does:** lists each rung, thread, address and rule · **Type:** reference

# The scale ladder: reference

Source: [📐 ssot_01_scale_ladder.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md). Version 1.1.0. Canonical, Module 1 of the lattice, delivered on Chief's clear 2026-08-25. Trunk: BLACK. Applies to OVEREXITOUT, all future IPs, BVX-LEARN keying. Why: [concept](1-concept.md).

## THE RUNGS — bottom-up

Rungs are containers. Each has a definition, a completion test, a governing system and holdings.

### R1 · BEAT

- **Is:** the smallest dramatic exchange: one action met by one reaction. It produces one micro-shift in a value or intention (McKee's behavior-exchange unit).
- **Completion test:** something was tried, something answered, something is now slightly different.
- **Governed by:** plot_systems (below the spine's floor). Storyform-blind: beats serve the scene.
- **Holdings:** McKee *Story* (0175); Coyne (0236, micro-beats within commandments).

### R2 · SCENE

- **Is:** a unit of continuous dramatic attention (typically unified time and place) that completes a miniature dramatic arc. The smallest container that turns.
- **Completion test (dual, both required):** (1) value turn (McKee): at least one value polarity flips. No turn, no scene. (2) Five commandments present (Coyne): inciting incident, complication, crisis, climax, resolution.
- **Pacing:** Genette's duration, the ratio of story-time to page or screen time. Scene is about 1:1. Summary compresses. Stretch dilates. Pause halts. Ellipsis skips. Full treatment in Module 3 (Texture).
- **Notation:** the house SCENE CARD: commandments, value charge, duration, setting state. Specced in Module 2 (the [setting system](../../../_SSOT/03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md)).
- **Holdings:** Coyne (0236); McKee (0175); Alderson *Deep Scenes* (0274); Munier (0154); Dunne (0062); Rayne Hall (0281).

### R3 · SEQUENCE

- **Is:** a chain of scenes unified by one dramatic question or objective. The head raises it and the tail answers it. Classical Hollywood ran films as about 8 sequences.
- **Completion test:** the sequence-level question is answered, and usually replaced by a worse one.
- **Holdings:** Aronson (0188); Frayne (0228); Coyne (0236). The five commandments repeat at scene, sequence, act and global scale.

### R4 · ACT / MOVEMENT

- **Is:** one span of the argument. Structurally, the span in which each throughline consumes one Signpost (Dramatica: 4 signposts plus 3 journeys per throughline). A Driver turns the span.
- **Completion test:** all four throughlines have advanced one signpost, and a driver (action or decision) has turned the story.
- **House note:** OXO's six Movements are presentation containers (storyweaving). Signposts are structural order (storyforming). Six movements can carry four signposts, since journeys and multi-movement signposts absorb the difference.
- **Holdings:** Dramatica (0089); Yorke (0127, fractal five-act); three-act via Aronson and Fink (0188/0092).

> **OPEN:** the Movement-to-Signpost mapping table is plot_systems work, flagged and not yet built.

### R5 · STORY (the storyform)

- **Is:** one complete Grand Argument: the spine's whole tree, satisfied. One storyform is one story.
- **Completion test:** all four throughlines complete; Outcome and Judgment delivered; the argument closed from every seat.
- **Governed by:** the spine (ssot_01_story_spine_comparative_tree) plus the integration protocol. Instance: `_CANON_NODES/oxo-storyform.md`.

### R6 · NESTED STORYFORM — story within story

- **Is:** a complete argument inside a parent argument. Canon already: integration protocol Pattern 1. It has its own `storyform_id`. A character may hold different roles across forms (MC in the parent, IC in a nested form). The parent has authority on conflict.
- **Completion test:** complete as a storyform (the R5 test) and consistent with the parent.
- **Use cases:** an episode with its own argument; a movement-level mini-form; a book inside a series. More use cases: a flashback story; a story a character tells.
- **Holdings:** integration protocol; Mittell (0565).

### R7 · IP / SERIES — many stories, one container

- **Is:** the owned narrative property holding multiple storyforms plus their shared canon.

| Pattern | Mechanism | Example shape |
|---|---|---|
| Anthology | Independent storyforms, shared premise or world only | Season is new cast, new form |
| Serialized | One storyform stretched across many installments | Novel-in-episodes; OXO's primary form across six movements |
| Episodic-with-mythology | Nested forms (episode arguments) under a parent form (the series argument) | Case-of-the-week plus season arc |
| Braided / ensemble | Parallel storyforms sharing one OS, different MC seats | Multi-protagonist epics |

- **Completion test:** every member storyform closed; the shared canon uncontradicted; if a parent form exists, it closes last.
- **House status:** OXO is serialized, with nested forms architecturally ready. IP-level meta-forms are flagged in the protocol, not implemented. Transmedia distribution: McErlean (0126), connects to the [medium grammars](../ssot_01_medium_grammars/2-reference.md).
- **Holdings:** Mittell (0565); McErlean (0126); integration protocol.

### R8 · UNIVERSE / CANON

- **Is:** multiple IPs sharing substrate: world rules, entities, systems. The integration protocol scopes `applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]`.
- **Completion test:** none. A universe never completes. The test is canon integrity.
- **Governed by:** the canon machinery: `_CANON_NODES/` plus the SSOT system. Cross-IP arguments would be R7 meta-forms spanning IPs (flagged).
- **Catalog (IF catalog call 3, ruled 2026-10-05):** the writer holds R8's shared world rules, entities and systems as entries. The entries live in the [05 worldbuilding catalog](../../../_SSOT/05_WORLDBUILDING_SYSTEMS/📐%20ssot_05_worldbuilding_system.md) (`WB-<TYPE>-<nnnn>`). The canon-integrity test reads those entries.
- **Holdings:** Collaborative Worldbuilding (0067); the worldbuilding shelf.

## THREADS — what runs through the containers

A thread is a tracked line of change with a span, not a boundary.

| Thread | Tracks | Typical span |
|---|---|---|
| Character arc | Resolve line: the MC's Change or Steadfast progression | R5, visible per scene |
| Setting arc | A place's state over time (Module 2) | Any, scene to universe |
| Relationship arc | The RS throughline's growth | R5; braids across R6 forms |
| Thematic motif | An Issue or Counterpoint recurrence; the 06 theme system supplies the rails R1–R4 and the `motif.<slug>` ids | Any |
| Trope instance | A register entry playing out | Any |

Rule: arcs are threads, never containers. Provisional house ruling, awaiting Chief.

## THE CONSTRAINT CHECK — Touchstones over the ladder (wired 2026-08-25)

Touchstones are neither containers nor threads. A thread changes. A Touchstone forbids. They are the standing constraint layer, governed by `DOCTRINE-0-INVARIANTS.md`. Its meta-rule IV ("holds at every scale: line, scene, movement, series") is this ladder's dimension.

**Enforcement rule:** every rung's completion test carries one last implicit clause: and no in-scope Touchstone is breached. A scene that turns while breaking a Touchstone is a breach (meta-rule VII). It invalidates downstream units that trusted it.

**Breach record (IF catalog call 6, ruled 2026-10-05):** the writer logs each breach in the Touchstone breach log. The log lives in 08 §9A (address · TS id · invalidated units). The address is an 08 time code.

**Census mapped to rungs:**

| Touchstone set | Rung |
|---|---|
| Layer 0 Invariants 1 to 5 (world physics) | R8 |
| Invariants of Power (KLK) | R7 |
| `touchstone` (for example `cost_and_meaning`) | R5 |
| Six Movements set (one per movement: Equity to Collapse) | R4 |
| Ecclesial Laws (place-scoped) | The setting slice S12 |
| Per-character sets (Tori ×4) | Character threads |

A Touchstone declares its scope as a ladder address span.

## THE ADDRESS SCHEME (provisional, rulable)

Any unit or thread span gets a canonical address: `IP.form.act.sequence.scene.beat`, truncated to depth.

| Address | Names |
|---|---|
| `OXO.primary` | The storyform (R5) |
| `OXO.primary.M2` | Movement 2 (R4) |
| `OXO.primary.M2.q3.s12` | Sequence 3, scene 12 (R3/R2) |
| `OXO.primary.M2.q3.s12.b4` | A beat (R1) |
| `tori.arc[OXO.primary.M1–M6]` | A thread span |

Tree addresses (`SPINE.Lx`) locate concepts. Ladder addresses locate instances. A library source keys to tree addresses. A manuscript unit keys to ladder addresses.

**One address (IF catalog call 1, ruled 2026-10-05).** The 08 time code (`M2 · Q1 · S04 | 012.3.2`, 08 §The address) is the one address for anything dated, in any system. This scheme maps onto it, as the table below shows. `IP.form` names the story, and the story's tracking file carries it, not the code.

| Ladder part | Time-code part |
|---|---|
| Movement `M<n>` | `M<n>` |
| Sequence `q<n>` | `Q<n>` |
| Scene `s<nn>` | `S<nn>` |
| Beat `b<n>` | The `bar.beat` after the `|` |

So `OXO.primary.M2.q3.s12` reads `M2 · Q3 · S12`.

## LADDER × LIBRARY

`feeds:` assignments for this limb:

| Source | Feeds |
|---|---|
| Coyne 0236 | R2, R3, and the fractal rule |
| McKee 0175 | R1, R2 |
| Alderson 0274, Munier 0154, Dunne 0062, Hall 0281 | R2 |
| Aronson 0188, Frayne 0228 | R3 |
| Yorke 0127, Dramatica 0089 | R4 |
| The spine | R5 |
| Mittell 0565 | R6, R7 |
| McErlean 0126 | R7 |
| Collaborative Worldbuilding 0067 | R8 |

**Interfaces.** Read by 00: the pattern library takes R1–R8 as the values of each pattern's Scales field (IF-00-01-01). Naming rule (IF catalog call 10, ruled 2026-10-05): "scale ladder" means R1–R8 only. The 05 worldbuilding system calls its three tiers "the reach".

**Open items the source lists:** arc-as-thread ruling; the Movement-to-Signpost table (6 movements × 4 signposts × 4 throughlines). The source also lists IP-level and cross-IP meta-forms (supported, not designed). The SCENE CARD slot was delivered with Module 2.

Dependencies: ssot_01_story_spine_comparative_tree, ssot_02_dramatica_integration_protocol.
