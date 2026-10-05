---
title: "The collision engine: reference"
type: reference
for: A writer or builder looking up a class, contact, proof row or record shape
does: Lists every component of the collision engine with its fields and rules
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_collision_engine.md
source_version: 1.0.1
---

**Who it's for:** a writer or builder looking up a collision fact · **What it does:** lists each class, contact, row and record · **Type:** reference

# The collision engine: reference

Source: [📐 ssot_01_collision_engine.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_collision_engine.md). Status: canonical, lattice Module 5, built on Chief's go 2026-08-26 (BOLO 17). Trunk: BLACK. The contact vocabulary is provisional. Concepts: [concept](1-concept.md).

## THE FOUR CLASSES

Each class pairs two kinds of slice. The engine reads the pair and writes one output record.

| Class | Machinery | Output record |
|---|---|---|
| C×C, character vs character | Cat 11 activated: aspect mesh (planet-to-planet contacts) plus composite chart (the relationship as its own virtual entity) | Relationship table row: two `character_id`s, mesh, composite |
| C×S, character vs setting | The diagonal: Lx against Sx down the twelve mirrored rows. Astrology analog: relocation | Diagonal table: 12 rows, each with contact, reading and scene potential |
| C×Situation | Cat 13 activated: a setting state plus a social configuration pings the static chart | State diff on the character, keyed to the firing address |
| C×G, character vs group | Mesh at N members plus group composite. The character's L7 ORIGIN and L8 IMPRINT receive | Group mesh plus per-member rows. Specced at first ensemble need |

Rules:
- When the pair is the storyform's RS, the composite chart is the RS throughline's astrological body.
- The chart defines which variables are vulnerable. Plot_systems and the scene card define when pings fire.
- The C×G check on the Dramatica side asks whether the group's 64-element distribution makes the Story Mind complete.
- Architecture, ruled 2026-08-26: a layer above the entity schemas. It feeds down as overlays. Baselines never mutate. Every output is keyed to a ladder address or span.

## CONTACT VOCABULARY — how a row classifies (provisional, astrology-native)

| Contact | Reads as | Drama value |
|---|---|---|
| Conjunction | Fusion: the two share the trait; mutual recognition or exposure | High, intimate |
| Trine | Flow: the place feeds the character. A trine from a hostile entity is a seduction | High when weaponized |
| Square | Friction: grinding, chronic conflict | The workhorse scene fuel |
| Opposition | Confrontation: direct, stakes-explicit | High, climactic |
| Void | No contact: the row produces no drama, a legal and informative result | None |

The discrimination rule: a healthy collision table has cold rows. An engine that declares every row hot is astrology-as-flattery.

## THE PROOF — Tori Midnight × the DCUS, all twelve rows

Run 2026-08-26 from canon: victoria-midnight (chart, gates, layer values) against the DCUS slice of the setting system. Scope: `tori × DCUS [OXO.primary.M2–M4]`.

| # | Row | Contact | One-line reading |
|---|---|---|---|
| 1 | L1 CORE (13) × S1 BODY | Void→Trine | Earth-built identity reads heritage masonry fluently. Cold row |
| 2 | L2 VITAL (14) × S2 WEATHER | Trine | Mars-exalted physicality thrives in Gulf heat. Underpowered: S2 is canon-thin, a surfaced gap |
| 3 | L3 SOCIAL (10) × S3 SENSORIUM | Square | Unfiltered presentation inside surfaces that broadcast. Truth Exposure Index 18 |
| 4 | L4 WILL (14) × S4 LAW | Opposition | The compliance collision. Sun□Saturn is the Ban mechanism. S4 is the Ban's institutional body |
| 5 | L5 WOUND (8) × S5 SCAR | Conjunction | Her wound is a deletion she caused. The campus is deletion institutionalized |
| 6 | L6 DRIVE (12) × S6 ECONOMY | Square | The economy prices ambition; her tank runs on meaning. Re-derives the economic tracker's first detection |
| 7 | L7 ORIGIN × S7 FOUNDING | Square, with echo | Salvage-economy origin against legacy-prestige founding. Both carry a buried truth |
| 8 | L8 IMPRINT (secure_anxious 6) × S8 HABIT | Square | Attachment architecture meets belonging machinery. M3's V-Sync trances hack L8 |
| 9 | L9 EROS × S9 ALLURE | Trine-as-trap | The hottest row. The promise hooks the sole unguarded line of the chart. Growth: Stop is the un-falling |
| 10 | L10 SHADOW × S10 UNDERSIDE | Conjunction | Mutual excavation. SHADOW_DENIAL is active. Movement 3's forensic mode is this row firing |
| 11 | L11 DESTINY × S11 VECTOR | Conjunction, dark | Growth vector and decay vector are one line run opposite ways. The Failure/Good geometry lives here |
| 12 | L12 FUNCTION × S12 FUNCTION | Structural | Free from the storyform: MC bound into the OS arena. Problem (Equity); story_cost = Memories |

The verdict: seven hot rows (3, 4, 5, 8, 9, 10, 11) form the scene menu for Movements 2–4. Two cold rows (1, 2) prove discrimination. One canon gap surfaced (S2 WEATHER). One beat re-derived (row 6). One row structural-for-free (12).

## OUTPUT CONTRACT

- **Collision record:** `{pair, class, scope (ladder address/span), rows[{layers, contact, reading, scene_potential}]}`. Stored beside the slices, never inside them.
- **Overlay record** (C×Situation): a state diff on the character keyed to the firing address. The scene card's `touchstones:`-adjacent line names its source.
- **Scene card wiring:** the card gains a `collision:` line naming the row(s) that seeded the scene. A scene seeded by no row justifies itself.

## THREE-CHECK LINES (three-check pass 1.0, kept 2026-09-29)

| Check | Line | Tag |
|---|---|---|
| fantasy | God of chemistry: cast two charts and read the sparks off the table | F10 |
| sexy | Synastry is about chemistry; the tool stays clinical so the output can burn | S10 |
| aesthetic | The mirror diagonal; aspect angles as architecture | A10 |

**Open items the source lists**

- Contact vocabulary: provisional, awaiting ruling.
- C×C first run, Tori × Anna: needs Anna's chart authored first.
- C×G spec: at first ensemble need (the Diaspora is the candidate).
- Automation: v1 is a method run in-session; a script is a later tool.

Dependencies: ssot_02_character_astrology (Cats 11–13), ssot_03_setting_system, [scale ladder](../ssot_01_scale_ladder/2-reference.md) (addresses), oxo-storyform §9, victoria-midnight, delta-coast-ultra-school. Version 1.0.1 renamed scene-card `invariants:` to `touchstones:`.
