---
title: "The trope register: reference"
type: reference
for: "A writer, designer or script author who looks up a record field, a key vocabulary or a count"
does: "Lists every component of the trope register doc with its fields, keys and counts"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_trope_register.md
source_version: 1.0.1
---

**Who it's for:** a writer, designer or script author looking up a field, key or count · **What it does:** lists every component of the trope register · **Type:** reference

# The trope register: reference

Source: [📐 ssot_01_trope_register.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_trope_register.md), version 1.0.0, trunk BLACK. Chief RULED it 2026-10-04 ("rec", BOLO 100 registers batch 1). Earlier ruling: 2026-09-29, BOLO 89. Applies to OVEREXITOUT and all future IPs. Why it exists: [concept](1-concept.md).

**Dependencies:** `ssot_04_trope_graph` (the plot consumer), `ssot_02_character_systems_vertical_slice`, `ssot_03_setting_system`, `ssot_01_genre_system`, `ssot_07_theme_system`. **Sources:** `_tools/tropes/fetch.py --domains`, `_tools/bolostatus/work/89/keys.batch01–16.json`, `_tools/tropes/build_register.py`.

**Root claim.** A trope is a reusable pattern a layer can draw on. The register is the trope layer for every system. The plot [trope graph](../../../_SSOT/04_PLOT_SYSTEMS/📐%20ssot_04_trope_graph.md) keys 1,034 Plot-index tropes onto 135 plot nodes. The register keys the other indexes to each domain's own twelve-layer slice.

## THE RECORD (ruled 9/29)

One record per trope, in `_tools/tropes/data/domains/register.json`.

| Field | Meaning |
|---|---|
| `slug` | TV Tropes page id, for example `AnythingYouCanDoICanDoBetter` |
| `name` | the trope's name |
| `def` | the TV Tropes index's one-line definition. Never page text, because the repo is public. |
| `domains` | one or more of character · setting · genre · sexuality · theme |
| `keys` | one key per domain: a layer id, or null. For example `{character: L3}`. |
| `conf` | `high`, `medium` or `low` |
| `links` | the trope's Main/ links, the raw edges |

**Undefined tropes (RULED 2026-10-04).** A trope with no one-line definition keys by its title and its domain tags. The record carries `def: undefined`. No run is needed to fill it.

**The keys.**

| Domain | Key vocabulary |
|---|---|
| character | L1 to L12 |
| setting | S1 to S12 |
| genre | G1 to G12 |
| sexuality | the character layers (mostly L9 EROS) |
| theme | the four rails R1 to R4 of the [theme system](../../../_SSOT/07_THEME_SYSTEMS/📐%20ssot_07_theme_system.md), or null |
| texture (added 0.4.0, ruled 9/29) | T1 to T12 of the [texture system](../ssot_01_texture_system/2-reference.md) |
| tracking (added 0.4.0) | the parts of the [tracking system](../../../_SSOT/08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md): world_clock · told_order · grid · story_point · cable · tempo |

## THE COUNTS (2026-10-03, v0.5.0)

**8,700 tropes, all keyed.** Confidence: high 6,241 · medium 1,435 · low 1,024. 1,018 still have no one-line definition.

| Domain (index) | Keyed by layer |
|---|---|
| character (Characters As Device · Characterization · Archetypal Character) | L1 316 · L2 59 · L3 198 · L4 54 · L5 37 · L6 63 · L7 70 · L8 47 · L9 60 · L10 85 · L11 56 · L12 485 · null 94 |
| sexuality (Sex Tropes · Queer Romance) | L9 430 · L5 10 · L2 2 · L1 1 · L7 1 · null 1 |
| setting (Settings · Religion · School · Motor Vehicle · Cyberpunk · Drugs · Military and Warfare) | S1 385 · S2 36 · S3 54 · S4 399 · S5 74 · S6 133 · S7 63 · S8 328 · S9 41 · S10 108 · S11 104 · S12 23 · null 549 |
| genre (Genres · Genre Tropes) | G1 66 · G2 8 · G3 5 · G4 3 · G5 6 · G6 2 · G8 3 · G9 3 · G10 1 · G11 3 · null 5 |
| theme (nine thematic indexes plus wave B: Love · Power · Emotion · Identity) | R1 448 · R2 853 · R3 409 · R4 460 · null 1,182 |
| texture (Narrative Devices · Framing Device · Narrative Tropes · Point of View) | T1 44 · T2 51 · T3 68 · T4 35 · T5 17 · T6 38 · T7 36 · T8 28 · T9 41 · T10 9 · T11 19 · T12 14 · null 344 |
| tracking (Time Tropes) | world_clock 51 · grid 43 · tempo 7 · told_order 4 · null 11 |
| style (wave B: Language · Costume · Graphical · Lighting · Amazing Technicolor) | 06.1 PROSE 264 · 06.3 PAGES 404 · null 164 |

**The pull list.** [LAYERS.md](../../../../../_tools/tropes/data/domains/LAYERS.md) lists every layer with every trope keyed to it.


## READING THE SKEW

The source reads each pile as a fact about the index.

- **Character piles on L12 FUNCTION (485) and L1 CORE (316)**. The Characters As Device index is mostly cast roles and types.
- **Setting piles on S4 LAW (399), S1 BODY (385) and S8 HABIT (328).** The Settings index lists place types such as the castle and the diner. Deeper layers, such as S2 WEATHER (36), are thin because TV Tropes has few tropes for them.
- **Theme nulls run high (1,182).** Death (1,035) and Family are broad. Most of their tropes argue none of the four rails. The rails are narrow. That is not a keying fault.
- **1,018 tropes have no one-line definition** on their index page and were keyed from the name alone. Most of the 1,024 low-confidence keys are these.


## COMMAND-LOCAL RECORDS (ruled 9/29, BOLO 91)

A record Chief keeps on purpose across the Command's own worlds files here in the register's format. It is flagged `source: command-local`. It attaches onto a matching TV Tropes entry in `register.json` on the next data pass.

Added fields: `source` (`command-local`), `instances` (a list of where the pattern appears), `note`.

**The Signature Wound.**

| Field | Value |
|---|---|
| slug | `SignatureWound` (Command-local, not a TV Tropes page id) |
| name | The Signature Wound: a sibling dies in a vehicle disaster |
| def | Chief's own recurring wound, kept on purpose across separate worlds, not a contradiction between them |
| source | command-local |
| domains | character, theme |
| keys | character L5 (WOUND), theme R2 (Death) |
| conf | high |
| instances | Tori (OXO/DCUS): car crash, brother Jebb dies (Ariel is Tori's earlier name) · Mayari (LEECHSEED): helicopter crash, brother ejected, father burns alive |
| note | likely matches Dead Sibling or Survivor Guilt already in `register.json`; not cross-checked in this pass; attach there once confirmed |

No character is changed by this ruling. It names a pattern, not a fix.

**OPEN items in the source.** Definitions (closed 2026-10-04): 1,018 tropes keep `def: undefined`; the keys stand. Consumer TROPES sections: ⏸ TROPES pointer sections (phase 2). Each system doc gets one section pointing at its layer lists, as a call in that doc's own batch. The tracking system's story points can carry a trope id. Done earlier: wave B (0.5.0), theme sub-index pass (0.2.0), low-confidence pass (0.3.0).

**Version history.**

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-10-04 | Undefined-trope rule written; OPEN list closed; TROPES pointer sections parked |
| 0.5.0 | 2026-10-03 | Wave B keyed: 2,175 keys on 9 PS batches (theme 1,013, style 831, 351 stragglers); RANGE caught one file with unquoted keys and three missing domain keys, then 0; the spread check passed |
| 0.4.0 | 2026-10-03 | Wave A keyed: 2,122 tropes (texture 641, tracking 111, setting 1,412) on 12 batches; default dumps caught and re-keyed (S1 797 to 366, T7 336 to 25) |
| 0.3.1 | 2026-09-29 | Command-local Signature Wound added (BOLO 91) |
| 0.3.0 | 2026-09-29 | Low-confidence pass: 952 definitions pulled; character nulls 348 to 94; low confidence 707 to 232 |
| 0.2.0 | 2026-09-29 | Theme sub-index pass: 1,854 new tropes (4,948 total), 2,012 theme keys on 9 batches |
| 0.1.0 | 2026-09-29 | BOLO 89: register stood up; 3,094 tropes fetched, keyed on 16 batches |
