---
type: ssot_01_narrative_frameworks
category: texture_layer
version: 1.0.0
last_updated: 2026-08-26
applies_to: [OVEREXITOUT, all future IPs, BVX-LEARN keying]
status: canonical — Module 3 of the lattice, delivered on Papi's clear 2026-08-26
purpose: "THE TEXTURE LAYER — the discourse side of narrative: the critical-writing categories (narratology) organized as the Ten Questions of the Telling, the craft-term translation grid, and the TELLING PROFILE instrument. Lattice limb 3 of 4."
dependencies: ["ssot_01_story_spine_comparative_tree", "ssot_01_scale_ladder", "ssot_03_setting_system (scene card)"]
trunk: BLACK
---

# 📐 SSOT: THE TEXTURE LAYER — how the telling is made

**What this is:** the "ancillary" layer Papi called — which turns out not to be ancillary at all. The load-bearing frame is **Chatman's story/discourse distinction** (BVX.0167): **story** = WHAT is told (events + existents — characters, settings); **discourse** = HOW it is told. The spine, the ladder, and the setting system are all story-side. **Texture is the entire discourse side** — the dimension the spine deliberately lacks, and the vocabulary critics actually categorize with.

**The communication model (Chatman)** — every narrative runs this pipeline, and texture decisions live at every arrow:

real author → **implied author** → **narrator** → **narratee** → implied reader → real reader

---

## THE TEN QUESTIONS OF THE TELLING

Every telling is a configuration of ten answers. This is the taxonomy.

### T1 · WHO SPEAKS — voice / narration
- **Person:** homodiegetic (narrator inside the story) vs heterodiegetic (outside it).
- **Level:** extradiegetic (the outermost teller) → intradiegetic (a character tells) → metadiegetic (a story inside that story) — frame narratives; nests like the ladder's R6.
- **Reliability:** the unreliable narrator (Booth) — the gap between narrator's account and implied author's truth.
- **Time of narration:** subsequent (past-tense default) · simultaneous (present) · prior (prophetic) · interpolated (diary/epistolary).

### T2 · WHO SEES — focalization (mood)
- **Zero** (unrestricted, "omniscient") · **internal** (through a character — fixed, variable, or multiple) · **external** (camera-eye, surfaces only).
- **The law: who speaks ≠ who sees.** A heterodiegetic narrator can see through Tori only (internal fixed). Collapsing these two is the most common craft confusion; separating them is the grid below.

### T3 · IN WHAT ORDER — order
- Story-time vs discourse-time. **Anachronies:** analepsis (flashback) · prolepsis (flashforward); each with **reach** (how far) and **extent** (how long).
- Story-side echo: the ladder's R4 signpost order is story sequence; T3 is the *telling's* rearrangement of it.

### T4 · AT WHAT SPEED — duration (pacing, formalized)
- The five speeds: **scene** (1:1) · **summary** (compresses) · **stretch** (dilates) · **pause** (description halts story-time) · **ellipsis** (skips).
- Pacing = the *pattern* of speeds across units. Already wired into the scene card's `duration:` field.
- Description theory (Bal): description is the pause/stretch machinery — this is where Setting (Module 2) meets Texture.

### T5 · HOW OFTEN — frequency
- **Singulative** (tell once what happened once) · **repetitive** (tell n times what happened once — trauma's signature) · **iterative** (tell once what happened n times — habit's signature; the S8 HABIT layer renders iteratively).

### T6 · IN WHAT WORDS — style / register
- Diction (Aristotle's *lexis*), syntax rhythm, sentence economy; speech representation: direct → indirect → **free indirect discourse** (the novel's signature instrument — narrator and character voice fused).
- **Distance:** diegesis (telling) vs mimesis (showing) — "show, don't tell" is a distance dial, not a commandment.

### T7 · WITH WHAT FEELING — tone & affect
- **Tone** = implied author's attitude; **mood** = the reader-side atmosphere. Hogan's affective narratology (0554): emotion as the structuring principle of stories, not decoration on them.

### T8 · THROUGH WHAT THRESHOLDS — paratext
- Genette's Paratexts (0582): titles, chapter heads, epigraphs, covers, forewords, codex entries — the apparatus the reader crosses before and around the text. For an IP builder this is a *design surface*: episode titles, movement names, in-world documents.

### T9 · BREAKING WHICH FRAMES — metalepsis & the unnatural
- **Metalepsis:** violations between diegetic levels (a narrator entering the story; a character addressing the reader). Unnatural narratology (0654): impossible tellings — dead narrators, second-person protagonists, contradictory timelines — catalogued, not forbidden.

### T10 · TO WHOM — narratee & implied reader
- Who the telling is aimed at inside the text (narratee) and the reader-shape the text assumes (implied reader). Direct address, "dear reader," tutorial voice; in games, the player-narratee fusion (Module 4 territory).

---

## THE TRANSLATION GRID — craft vocabulary → texture configuration

The workshop terms are compressed configurations of T1 × T2:

| Craft term | Actual configuration |
|---|---|
| First person | homodiegetic + internal fixed focalization |
| Third limited | heterodiegetic + internal fixed |
| Third omniscient | heterodiegetic + zero focalization |
| Head-hopping | heterodiegetic + internal *variable*, unmanaged |
| Camera-eye / objective | heterodiegetic + external |
| Second person | narratee-as-protagonist (+ usually simultaneous narration) |
| Epistolary | homodiegetic + interpolated narration |
| Unreliable narrator | any homodiegetic + reliability gap (T1) |
| "Show don't tell" | distance dial toward mimesis (T6) |
| Flashback / flashforward | analepsis / prolepsis (T3) |
| "Slow burn" / "breakneck" | duration pattern (T4) |

---

## THE INSTRUMENT — the TELLING PROFILE

The discourse twin of the storyform: a work's fixed configuration of the ten answers, recorded per ladder address (usually R5, overridable per unit — a movement may shift focalization by design).

```
TELLING PROFILE
scope:        OXO.primary                  (ladder address)
T1 voice:     hetero/homo · level · reliability · narration time
T2 sees:      focalization mode (+ focal character(s))
T3 order:     baseline + licensed anachronies
T4 speed:     default gait + signature moves
T5 frequency: signature uses (iterative? repetitive?)
T6 words:     register, distance policy, FID yes/no
T7 feeling:   tone; target mood curve
T8 thresholds: paratext apparatus (titles, epigraphs, in-world docs)
T9 frames:    metalepsis policy (permitted? never?)
T10 aimed at: narratee construction
```

**Scene card wiring:** the card gains a `telling:` line (T1+T2+T4 for that scene) — the per-scene override of the profile.

**House finding, flagged:** **OXO has no ruled Telling Profile.** No prose exists (`outliers.fdx` empty), so the entire discourse configuration — whose voice, who focalizes, what the movements' paratext apparatus is — is an *unmade decision set*. This module hands Papi the decision menu; the profile is a rulable artifact whenever OXO prose opens.

---

## TEXTURE × LIBRARY

`feeds:` for this limb: Chatman 0167 → the frame (story/discourse + communication model) · Bal 0591/0596 → focalization + description theory · Handbook of Narratology 0584 + diachronic 0583 → the reference shelf · Genette Paratexts 0582 → T8 · Hogan 0554 → T7 · Alber/Richardson 0654 → T9 · Meister 0566 → computational treatment · Mittell 0565 → TV-specific discourse (also R6/R7) · craft translations: McKee 0175 (distance, dialogue), Weiland shelf (POV/showing craft), Bell 0159 (revision as texture editing).

**Acquisition gaps (BVX.1107+ candidates):** Genette *Narrative Discourse* (the T3–T5 source text — Paratexts is held, the core work is not) · Booth *The Rhetoric of Fiction* (reliability, implied author) · Wood *How Fiction Works* (FID popularizer, optional).

## OPEN

- **The OXO Telling Profile** — unruled; fires when OXO prose opens (or on Papi's call sooner).
- **The Ten Questions naming** (T1–T10) — house coinage, awaiting ruling.
- **Genette/Booth acquisitions** → BVX.1107+ queue.
- Per-medium texture variants (game narration, PMV editing grammar as T3/T4 in video) → Module 4.

## Version history

- **1.0.0 — 2026-08-26.** Module 3 of the lattice: story/discourse frame, the Ten Questions taxonomy, craft translation grid, TELLING PROFILE instrument, scene-card `telling:` line, gaps queued.
