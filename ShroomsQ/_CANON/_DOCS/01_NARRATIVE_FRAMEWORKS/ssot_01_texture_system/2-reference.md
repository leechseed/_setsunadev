---
title: "The texture system: reference"
type: reference
for: "A writer or tool builder who looks up a texture layer, field, check or source"
does: "Lists every component of the texture system doc with its fields, values and links"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_texture_system.md
source_version: 1.0.0
---

**Who it's for:** a writer or tool builder looking up a layer or field · **What it does:** lists every component of the texture system doc · **Type:** reference

# The texture system: reference

Source: [📐 ssot_01_texture_system.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_texture_system.md), version 1.0.0, trunk BLACK, rung standard. Chief RULED it 2026-10-04 ("REC", BOLO 100 texture batch 1). Why it exists: [concept](1-concept.md).

**Header facts.** Applies to all IPs. Sources: BVX.0598, 0596, 0273, 0084, 0279, 0061, 0175, 0349. Dependencies: `ssot_01_texture_layer`, `ssot_01_story_spine_comparative_tree`, `ssot_01_scale_ladder`, `ssot_01_medium_grammars`, `ssot_03_setting_system`, `ssot_04_plot_system`, `ssot_02_character_systems_vertical_slice`.

**Owns:** the discourse side of the telling, the TELLING PROFILE, the scene card's `telling:` line, and the medium's re-instrumenting. **Does not own:** structure (Dramatica), events (plot systems), place (setting slice), persons (LEECHSEED Character System).

**Root claim.** Every telling is one configuration of a fixed set of answers. Who speaks and who sees are two decisions.

## MIND MODELS

Three diagrams hold the whole system. The source draws them in Mermaid. This page describes them in words.

- **Diagram 1, the whole system on one screen.** Root: THE TEXTURE SYSTEM. Branches: the Ten Questions · the Texture Slice (twelve T-layers, T11 medium, T12 fed from storyform) · the Telling Profile (R5 instrument, scene card override) · Library (BVX.0598 the DNS, 0596 the focalizor, 0273 the distance dial, 0084 the seven functions). Also in the library: 0279 the mood curve, 0061 levels of penetration, 0175 show not tell, 0349 the gutter · Boundaries (structure is Dramatica, events are plot systems, place is the setting slice, persons are the 12 layer DB).
- **Diagram 2, the mediation chain and the distance dial.** Flow: Fabula → the focalizor (who sees). Next: the narrator (who speaks) → the words (register, distance policy, FID). Last: the narratee and implied reader. The distance dial (cinematic, light, deep) sets the words. T11 medium governs the focalizor, the narrator and the words.
- **Diagram 3, the telling per unit.** States: Baseline → Override (the scene card's telling line fires). Next: Response (focal shift, duration change, register change) → MoodCurve (interest, curiosity, anticipation, suspense, surprise). Last: Payoff (surprise, disappointment or relief) → Baseline. The cycle recurs at every ladder rung. T2 and T6 carry most of the mood curve's weight.

## PART B · THE TAXONOMY, the Ten Questions restated as axes

The Ten Questions as one table. The layer doc stays the taxonomy source: [📐 ssot_01_texture_layer.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_texture_layer.md). Its translation grid is linked, not reproduced.

| Question | Decides | Law or dial | Source |
|---|---|---|---|
| T1 WHO SPEAKS | person, level, reliability, time of narration | voice is a speech act, never a vision; a narratorless text still carries an impersonal narrating agency | BVX.0598, 0596 |
| T2 WHO SEES | focalization mode, focal character, perceptual scope, informational denial | who speaks is not who sees; EF/CF plus perceptible or non-perceptible marking | BVX.0598, 0596, 0273 |
| T3 IN WHAT ORDER | story-time against discourse-time, anachronies, reach, extent | the telling rearranges the sequence the ladder's R4 signposts fix | BVX.0596 |
| T4 AT WHAT SPEED | the five speeds, scene through ellipsis | dialogue is the default accelerator, narrative the default brake | BVX.0084, 0596 |
| T5 HOW OFTEN | singulative, repetitive, iterative | repetitive is trauma's signature, iterative is habit's (S8 HABIT) | BVX.0596 |
| T6 IN WHAT WORDS | diction, syntax, register, distance policy, FID | the distance dial: cinematic, light, deep | BVX.0273, 0061, 0084 |
| T7 WITH WHAT FEELING | tone, mood, target mood curve | interest is the master emotion; curiosity, anticipation, suspense and surprise are its forms | BVX.0279 |
| T8 THROUGH WHAT THRESHOLDS | paratext apparatus | a detail earns its place by pointing at theme or distinctiveness | BVX.0349 |
| T9 BREAKING WHICH FRAMES | metalepsis policy | direct address is normal in some mediums and a violation in others | BVX.0596 |
| T10 TO WHOM | narratee construction, implied reader | the three V's: voyeuristic, vicarious, visceral | BVX.0279, 0596 |

**The law.** Who speaks is not who sees. The DNS model of Hühn, Schmid and Schönert splits mediation into perception, reflection and mediation proper (BVX.0598). Bal names the split EF against CF (BVX.0596). Both sources show the single `focalization_mode` value bundles two decisions. PART A carries them as separate fields.

**The dial.** Distance has three settings inside limited third person (BVX.0061): cinematic (camera only, no thoughts). Light (the narrator dips in and out). Deep (no thought tags; the character's judgment colors every clause). Hall (BVX.0273) turns deep into a checkable technique inventory. T6's distance policy carries this scale as house vocabulary.

## PART A · THE TEXTURE SLICE, twelve layers, mirror of the character, setting and plot stacks

The architecture mirrors the LEECHSEED Character System, the setting slice and the plot slice. T12 is fed independently from the storyform. The layer names are ruled (OPEN 2, 9/16).

| Layer | Name | Question | Source | Field it writes |
|---|---|---|---|---|
| T1 | VOICE | Who speaks, at what level, how reliably, when? | BVX.0596, 0598 | `voice_person` (homo or hetero), `voice_level`, `reliability`, `narration_time` |
| T2 | FOCALIZATION | Who sees, and what is the reader denied? | BVX.0598, 0596, 0273 | `focalization_mode`, `focal_character`, `perceptual_scope`, `informational_denial` |
| T3 | ORDER | In what order is it told against the order it happened? | BVX.0596 | `order_baseline`, `licensed_anachronies` |
| T4 | DURATION | At what speed does the telling move? | BVX.0596, 0084 | `duration_mode`, `signature_moves` |
| T5 | FREQUENCY | How often is an event told against how often it happened? | BVX.0596 | `frequency_mode` (singulative, repetitive, iterative) |
| T6 | WORDS | In what words, register and distance? | BVX.0273, 0061, 0084 | `register`, `distance_policy` (cinematic, light, deep), `fid` |
| T7 | FEELING | With what feeling, whose tone, what is the reader meant to feel? | BVX.0279 | `mood_curve` entries (emotion, technique, payoff owed) |
| T8 | THRESHOLDS | Through what thresholds does the reader enter the text? | BVX.0349 | `paratext_apparatus` |
| T9 | FRAMES | Breaking which frames, and is it licensed? | BVX.0596 | `metalepsis_policy` |
| T10 | NARRATEE | To whom is the telling aimed? | BVX.0279, 0596 | `narratee_construction` |
| T11 | MEDIUM | Which channel's grammar re-instruments the telling (M1 to M10)? | [📐 ssot_01_medium_grammars.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_medium_grammars.md) | `medium`, `grammar_overrides` |
| T12 | FUNCTION | What does this telling do for the Grand Argument? | BVX.0089 | `story_point`, `storyform_id` |

**Sub-values and checks** (ruled 9/16, built 2026-10-04):

- **T2 split.** `perceptual_scope` records whose view the reader gets. `informational_denial` records what the reader is denied.
- **T2 sub-values.** `focalization_mode` allows `silence` and `memory`. Silence is a focalized character's deliberate non-report of her own thought (BVX.0084). Memory is retrospective, unreliable, sense-based and itself narrativized (BVX.0596).
- **T1/T2 gap flag.** `t1_t2_gap: none | flagged (note)` records the gap. The gap lies between a T1 reading and a T2 reading of one passage. It is Bal's manipulation check as one field.
- **T4 pause test.** Where a scene marks the Pause speed, check delimitation, motivation and rhetorical binding (BVX.0596).
- **T6 distance instrument.** Count barrier words per 100 words (BVX.0273). Bands: cinematic, light, deep. The first trial passage calibrates the cut points.
- **T7 reflection axis.** T7 absorbs the cognitive, emotive and normative mark-up of what is perceived (BVX.0598).
- **T7 mood-curve entry.** One line of three fields: emotion · technique · payoff owed (BVX.0279).
- **T7 payoff ledger.** A running list of owed payoffs. An entry closes when the story pays it. It sits outside the twelve layers as a reader model. The reader's trust in a character is tracked in [§9A The Reader Model](../../../_SSOT/08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md#9a-the-reader-model). The tracker keys it by `character_id` and `shifted_at`. The ledger uses the same time code.
- **Dialogue function count.** Kempton's seven-function test audits a line by removal (BVX.0084). It is a named revision check, not a schema field (OPEN 7).

**Binding rule.** T12 is fed independently from the storyform, keyed by `storyform_id`, as L12, S12 and P12 are. T12 empty means a style with no argument. T12 filled means the telling serves the argument. The count is twelve (OPEN 1, ruled 9/16). T11 and T12 are house additions beyond the layer doc's ten questions.

## THE INSTRUMENT · the TELLING PROFILE and the telling line

No new card. The TELLING PROFILE from the layer doc is the slice's instance format, recorded per ladder address, usually R5.

| Field | Holds |
|---|---|
| `scope` | ladder address, for example `OXO.primary` |
| T1 voice | hetero or homo · level · reliability · narration time |
| T2 sees | focalization mode · focal characters · perceptual scope · informational denial |
| T3 order | baseline and licensed anachronies |
| T4 speed | default gait and signature moves |
| T5 frequency | signature uses |
| T6 words | register · distance policy · FID yes or no · barrier words per 100 |
| T7 feeling | tone · target mood curve (emotion, technique, payoff owed) · reflection mark-up |
| T8 thresholds | paratext apparatus |
| T9 frames | metalepsis policy |
| T10 aimed at | narratee construction |
| T11 medium | channel and grammar overrides |
| T12 function | story point discharged · `storyform_id` |
| `gap` | `t1_t2_gap`: none, or flagged with a note |

**The `telling:` line** is the per-unit override. Its content stays lean:

```
telling:  voice/level + focal character (T1+T2) · speed (T4) · register (T6) · t1_t2_gap
```

**Register slot.** Kempton's seven genre registers are the readiest source (BVX.0084). They could seed the translation grid's craft-term column and let a scene card flag a mismatch, as `duration:` flags pace. **Deep-PoV checklist.** Hall's checklist shows T1, T2 and T6 at the strictest setting. They use hetero or homodiegetic voice, internal fixed focalization, one mind per scene, distance at deep (BVX.0273).

## THE INSTANCE · worked example (phase 2 fills)

⏸ OXO telling profile (phase 2)

The method does not depend on this example. Every value below is a proposal. Chief strikes or keeps the lines one by one when OXO prose opens. The layer doc's finding stands: OXO has no ruled Telling Profile and no prose exists.

| Layer | OXO (proposed) |
|---|---|
| T1 | Heterodiegetic, subsequent narration, reliable narrator with a reliability gap reserved for the Administration's documents |
| T2 | Internal fixed on Tori by default, variable per movement by design |
| T3 | Order told matches order happened as baseline; a licensed analepsis at each movement threshold recovers the buried name, Skeeter Creek, as forensic mode in Movement 3 |
| T4 | Scene-gait default, with stretch reserved for the crash |
| T5 | Iterative for the Star-Rating's ritual life and the Sync mechanics; repetitive reserved for the rename lattice's recurring legibility violation |
| T6 | Deep distance, FID yes, Southern Gothic register |
| T7 | Tone tracks the six-movement descent, clean to NEON-ROT to hunt; curiosity and dread across Movements 1 and 2, suspense and thrill across 3 to 5, relief withheld to match Outcome Failure, Judgment Good |
| T8 | In-world documents, the Star-Rating, Administration memos, as paratext |
| T9 | Metalepsis withheld by default; the Feed-linked legibility apparatus is the nearest analogue to direct address, never crossed into second person |
| T10 | Implied reader stands where Tori's meritocratic belief (S9 ALLURE) has not yet broken; no narratee construction beyond the Administration's address to "students" |
| T11 | M1 prose with an M3 serial grammar |
| T12 | The MC throughline, `storyform_id: oxo_primary_v1`, discharging DCUS's S12 record, the OS Domain Situation, the Past |

The values rest on canon: Tori as MC, the Driver ruled Action ([story spine](../ssot_01_story_spine_comparative_tree/2-reference.md)). They also rest on the six-movement descent and Southern Gothic register on the DCUS instance. They rest on the rename lattice (Skeeter Creek to Red Hills to DCUS) as S5 SCAR paratext. The setting system covers it ([📐 ssot_03_setting_system.md](../../../_SSOT/03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md)).

## TEXTURE × LIBRARY

| ID | Book | Feeds hardest | Gives the system |
|---|---|---|---|
| BVX.0598 | Hühn, Schmid and Schönert | T2 | the DNS three-dimension model; the reflection axis, ruled into T7 |
| BVX.0596 | Bal | T2 | EF/CF, perceptible marking, narrator/focalizer discrepancy as a manipulation diagnostic |
| BVX.0273 | Hall | T6 | barrier words as a countable instrument; the distance dial |
| BVX.0084 | Kempton | T6 | the seven-function test for dialogue; viewpoint silence |
| BVX.0279 | Iglesias | T7 | the seven-emotion mood curve, the three V's, the payoff owed |
| BVX.0061 | Card | T6 | levels of penetration; viewpoint is out of scope for the twelve character layers |
| BVX.0175 | McKee | T6 | show, don't tell as a distance dial; text against subtext |
| BVX.0349 | Kennedy | T8 | the gutter of implication; apophatic detail; a caution against over-filling paratext |

**The shelf.** 105 items keyed 9/16 (BOLO 18); eight distilled to date. Next candidates: Bell's *VOICE* (BVX.0256), Block's *The Visual Story* (BVX.1103), the Routledge handbook of stylistics (BVX.0647). After those come the *Handbook of Narratology* (BVX.0584) and Thomas and Turner's *Clear and Simple as the Truth*. The last is Landon's *Building Great Sentences*. Queued acquisitions: Genette *Narrative Discourse*, Booth *The Rhetoric of Fiction*, and Bal's theory volume (BVX.0591), undistilled.

**OPEN calls, all closed** (ruled 9/16, "texture calls go"; built 2026-10-04). 1 Twelve layers. 2 The twelve names stand. 3 T2 perceptual and informational sub-fields. 4 Reflection axis absorbed by T7. 5 T6 distance scale and instrument. 6 Register slot on the telling line. 7 Dialogue function count held as a revision check. 8 Viewpoint silence as a T2 sub-value. 9 The `t1_t2_gap` flag. 10 Memory as a T2 sub-value and the T4 pause test. 11 Mood-curve entry format and the reader ledger. 12 OXO profile parked (⏸ OXO telling profile). 13 Acquisitions queued.

**Version history.** 1.0.0 (2026-10-04): RULED, texture batch 1; the layer doc is stamped `module_of` this system. 0.1.1 (2026-09-16): the thirteen OPEN calls ruled. 0.1.0 (2026-09-16): first version, from the TEXTURE shelf's eight distills.
