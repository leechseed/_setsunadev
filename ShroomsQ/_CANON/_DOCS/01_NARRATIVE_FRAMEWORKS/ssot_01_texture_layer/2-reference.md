---
title: "The texture layer: reference"
type: reference
for: "A writer or designer who looks up one of the Ten Questions, a grid row or a profile field"
does: "Lists every component and part of the texture layer doc with its values and links"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_texture_layer.md
source_version: 1.0.1
---

**Who it's for:** a writer or designer looking up a question or field · **What it does:** lists every component of the texture layer doc · **Type:** reference

# The texture layer: reference

Source: [📐 ssot_01_texture_layer.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_texture_layer.md), version 1.0.1, trunk BLACK, RULED by Chief 2026-10-04 ("REC"). Module 3 of the lattice, limb 3 of 4. It is a module of the [texture system](../ssot_01_texture_system/2-reference.md). Why it exists: [concept](1-concept.md).

**Frame.** Chatman's story/discourse distinction (BVX.0167). Story is what is told. Discourse is how. The communication model runs: real author → implied author → narrator → narratee → implied reader → real reader.

**Dependencies:** `ssot_01_story_spine_comparative_tree`, `ssot_01_scale_ladder`, `ssot_03_setting_system` (scene card).

## THE TEN QUESTIONS OF THE TELLING

Every telling is a configuration of ten answers.

### T1 · WHO SPEAKS — voice / narration

- **Person:** homodiegetic (narrator inside the story) or heterodiegetic (outside it).
- **Level:** extradiegetic (outermost teller) → intradiegetic (a character tells) → metadiegetic (a story inside that story). Frame narratives nest like the ladder's R6.
- **Reliability:** the unreliable narrator (Booth), a gap between the narrator's account and the implied author's truth.
- **Time of narration:** subsequent (past tense default) · simultaneous (present) · prior (prophetic) · interpolated (diary, epistolary).

### T2 · WHO SEES — focalization (mood)

- **Modes:** zero (unrestricted, "omniscient") · internal (through a character: fixed, variable or multiple) · external (camera-eye, surfaces only).
- **The law:** who speaks is not who sees.

### T3 · IN WHAT ORDER — order

- Story-time against discourse-time. **Anachronies:** analepsis (flashback) and prolepsis (flashforward). Each has a **reach** (how far) and an **extent** (how long).
- The ladder's R4 signpost order is story sequence. T3 is the telling's rearrangement of it.

### T4 · AT WHAT SPEED — duration (pacing, formalized)

- **Five speeds:** scene (1:1) · summary (compresses) · stretch (dilates) · pause (description halts story-time) · ellipsis (skips).
- Pacing is the pattern of speeds across units. The scene card's `duration:` field already carries it.
- Bal's description theory: description is the pause and stretch machinery. Setting (Module 2) meets Texture here.

### T5 · HOW OFTEN — frequency

| Value | Meaning | Signature |
|---|---|---|
| Singulative | tell once what happened once | default |
| Repetitive | tell n times what happened once | trauma |
| Iterative | tell once what happened n times | habit; the S8 HABIT layer renders iteratively |

### T6 · IN WHAT WORDS — style / register

- Diction (Aristotle's *lexis*), syntax rhythm, sentence economy.
- **Speech representation:** direct → indirect → free indirect discourse (FID), where narrator and character voice fuse.
- **Distance:** diegesis (telling) against mimesis (showing). "Show, don't tell" is a distance dial.

### T7 · WITH WHAT FEELING — tone & affect

- **Tone:** the implied author's attitude. **Mood:** the reader-side atmosphere.
- Hogan's affective narratology (BVX.0554): emotion structures stories.

### T8 · THROUGH WHAT THRESHOLDS — paratext

- Genette's *Paratexts* (BVX.0582): titles, chapter heads, epigraphs, covers, forewords, codex entries.
- For an IP builder this is a design surface: episode titles, movement names, in-world documents.

### T9 · BREAKING WHICH FRAMES — metalepsis & the unnatural

- **Metalepsis:** violations between diegetic levels, such as a narrator entering the story or a character addressing the reader.
- Unnatural narratology (BVX.0654): impossible tellings (dead narrators, second-person protagonists, contradictory timelines) are catalogued, not forbidden.

### T10 · TO WHOM — narratee & implied reader

- The narratee is who the telling addresses inside the text. The implied reader is the reader-shape the text assumes.
- Forms: direct address, "dear reader," tutorial voice. In games the player and narratee fuse (Module 4 territory).

## THE TRANSLATION GRID — craft vocabulary → texture configuration

| Craft term | Configuration |
|---|---|
| First person | homodiegetic + internal fixed focalization |
| Third limited | heterodiegetic + internal fixed |
| Third omniscient | heterodiegetic + zero focalization |
| Head-hopping | heterodiegetic + internal variable, unmanaged |
| Camera-eye / objective | heterodiegetic + external |
| Second person | narratee-as-protagonist (usually with simultaneous narration) |
| Epistolary | homodiegetic + interpolated narration |
| Unreliable narrator | any homodiegetic + a reliability gap (T1) |
| "Show don't tell" | distance dial toward mimesis (T6) |
| Flashback / flashforward | analepsis / prolepsis (T3) |
| "Slow burn" / "breakneck" | duration pattern (T4) |

## THE INSTRUMENT — the TELLING PROFILE

The discourse twin of the storyform. It records a work's fixed answers to the ten questions at a ladder address, usually R5. A unit may override it, since a movement may shift focalization by design.

| Field | Holds |
|---|---|
| `scope` | ladder address, for example `OXO.primary` |
| T1 voice | hetero or homo · level · reliability · narration time |
| T2 sees | focalization mode and focal character(s) |
| T3 order | baseline and licensed anachronies |
| T4 speed | default gait and signature moves |
| T5 frequency | signature uses (iterative? repetitive?) |
| T6 words | register · distance policy · FID yes or no |
| T7 feeling | tone and target mood curve |
| T8 thresholds | paratext apparatus |
| T9 frames | metalepsis policy (permitted? never?) |
| T10 aimed at | narratee construction |

**Pointer.** T11 MEDIUM, T12 FUNCTION and the T2 sub-fields live in the [texture system](../ssot_01_texture_system/2-reference.md). That doc carries the full twelve-field profile. This doc keeps the ten-field original.

**Scene-card wiring.** The card gains a `telling:` line (T1, T2 and T4 for that scene). It is the per-scene override of the profile.

**House finding.** OXO has no ruled Telling Profile. No prose exists (`outliers.fdx` is empty). The whole discourse configuration is an unmade decision set. The profile is rulable whenever OXO prose opens.

## TEXTURE × LIBRARY

The `feeds:` keys for this limb:

| Source | Feeds |
|---|---|
| Chatman, BVX.0167 | the frame: story/discourse and the communication model |
| Bal, BVX.0591 / 0596 | focalization and description theory |
| Handbook of Narratology 0584 and its diachronic volume 0583 | the reference shelf |
| Genette, *Paratexts* 0582 | T8 |
| Hogan 0554 | T7 |
| Alber/Richardson 0654 | T9 |
| Meister 0566 | computational treatment |
| Mittell 0565 | TV-specific discourse (also R6/R7) |
| McKee 0175 | distance and dialogue |
| Weiland shelf | POV and showing craft |
| Bell 0159 | revision as texture editing |

**Acquisition gaps (BVX.1107+ candidates):** Genette *Narrative Discourse* (the T3 to T5 source text) · Booth *The Rhetoric of Fiction* (reliability, implied author) · Wood *How Fiction Works* (optional, FID popularizer).

**OPEN items in the source.** The OXO Telling Profile is unruled; it fires when OXO prose opens, or sooner on Chief's call. The Ten Questions naming (T1 to T10) was ruled 9/16 in the texture system and is closed. The Genette and Booth acquisitions sit in the BVX.1107+ queue. Per-medium texture variants were built in medium grammars 1.2.0 and are closed.

**Version history.** 1.0.1 (2026-10-04, BOLO 100 texture batch 1): stamped `module_of: ssot_01_texture_system`, added the pointer to T11, T12 and the sub-fields, closed the naming and per-medium OPENs, no change to the ten questions. 1.0.0 (2026-08-26): Module 3 of the lattice delivered.
