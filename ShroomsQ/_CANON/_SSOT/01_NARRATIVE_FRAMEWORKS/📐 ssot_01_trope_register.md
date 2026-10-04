---
type: ssot_01_narrative_frameworks
category: trope_register
version: 0.4.0
last_updated: 2026-10-03
applies_to: [OVEREXITOUT, all future IPs]
status: "RULED 2026-09-29 — BOLO 89 (Chief, \"I'll recommend\" · \"go\" · \"all recommendations\"); keyed by three PS batches, RANGE-checked (0 findings)"
purpose: "THE TROPE REGISTER: one trope layer under every system. 4,948 TV Tropes tropes, each tagged with the domains it serves and keyed to a layer of that domain's slice, so any layer can pull its tropes."
dependencies: ["ssot_04_trope_graph (the plot consumer)", "ssot_02_character_systems_vertical_slice", "ssot_03_setting_system", "ssot_01_genre_system", "ssot_07_theme_system"]
trunk: BLACK
sources: ["_tools/tropes/fetch.py --domains", "_tools/bolostatus/work/89/keys.batch01–16.json", "_tools/tropes/build_register.py"]
---

# 📐 SSOT · THE TROPE REGISTER — one trope layer through every system

**What this is:** the trope layer for every system, not just plot. The plot [trope graph](../04_PLOT_SYSTEMS/📐%20ssot_04_trope_graph.md) keys 1,034 tropes from TV Tropes' Plot indexes onto 135 plot nodes. This register pulls TV Tropes' character, setting, genre, sexuality, and theme indexes and keys each trope to a layer of its own domain's twelve-layer slice. The trope graph is the register's first consumer; nothing in it is rebuilt.

**Root claim:** a trope is a reusable pattern a layer can draw on. A character's L5 WOUND, a place's S10 UNDERSIDE, and a genre's G1 LABEL each get a pull list of known patterns, keyed and ready.

## THE RECORD (ruled 9/29)

One record per trope, in `_tools/tropes/data/domains/register.json`:

```yaml
slug:    AnythingYouCanDoICanDoBetter   # TV Tropes page id
name:    Anything You Can Do, I Can Do Better
def:     the TV Tropes index's one-line definition (never page text: the repo is public)
domains: [character]                    # one or more of character · setting · genre · sexuality · theme
keys:    {character: L3}                # one key per domain: a layer id, or null
conf:    high | medium | low
links:   [...]                          # the trope's Main/ links, the raw edges
```

**The keys (ruled 9/29):** character → L1–L12 · setting → S1–S12 · genre → G1–G12 · sexuality → the character layers (mostly L9 EROS) · theme → the four rails R1–R4 of the [theme system](../07_THEME_SYSTEMS/📐%20ssot_07_theme_system.md), or null. **Added 0.4.0 (wave A, ruled 9/29 "all recs"):** texture → T1–T12 of the [texture system](📐%20ssot_01_texture_system.md) · tracking → the parts of the [tracking system](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md): world_clock · told_order · grid · story_point · cable · tempo.

## THE COUNTS (2026-10-03, v0.4.0)

**7,070 tropes keyed** (wave A added 2,122: texture, tracking, and OXO's setting indexes) · **1,630 listed, not yet keyed** (wave B, fetching: theme + style) · 8,700 in the index.

| Domain (index) | Keyed by layer |
|---|---|
| **character** (Characters As Device · Characterization · Archetypal Character) | L1 316 · L2 59 · L3 198 · L4 54 · L5 37 · L6 63 · L7 70 · L8 47 · L9 60 · L10 85 · L11 56 · **L12 485** · null 94 |
| **sexuality** (Sex Tropes · Queer Romance) | **L9 430** · L5 10 · L2 2 · L1 1 · L7 1 · null 1 |
| **setting** (Settings + wave A: Religion · School · Motor Vehicle · Cyberpunk · Drugs · Military and Warfare) | **S1 366** · S2 33 · S3 52 · **S4 339** · S5 67 · S6 118 · S7 58 · **S8 278** · S9 38 · S10 105 · S11 102 · S12 21 · null 475 |
| **genre** (Genres · Genre Tropes) | **G1 66** · G2 8 · G3 5 · G4 3 · G5 6 · G6 2 · G8 3 · G9 3 · G10 1 · G11 3 · null 5 |
| **theme** (Truth and Lies · Death · Family · Betrayal · Revenge · Authority · Memory · The Secret · Promises and Vows) | R1 274 · **R2 566** · R3 324 · R4 383 · null 791 |
| **texture** (wave A: Narrative Devices · Framing Device · Narrative Tropes · Point of View) | T1 39 · T2 46 · T3 35 · T4 32 · T5 13 · T6 37 · T7 25 · T8 21 · T9 39 · T10 7 · T11 19 · T12 11 · **null 318** |
| **tracking** (wave A: Time Tropes) | world_clock 49 · grid 43 · tempo 6 · told_order 4 · null 9 |

**The pull list:** [LAYERS.md](../../../../_tools/tropes/data/domains/LAYERS.md) lists every layer with every trope keyed to it.

## READING THE SKEW

- **Character piles on L12 FUNCTION (508) and L1 CORE (291).** The Characters As Device index is mostly cast roles and types; that is what the index holds, not a keying fault.
- **Setting piles on S1 BODY (276).** The Settings index lists place types (the castle, the diner); the deeper layers (S2 WEATHER 3) are thin because TV Tropes has few tropes for them.
- **Theme nulls run high (797)** because Death (1,035) and Family are broad: most of those tropes argue none of the four rails. That is the rails being narrow, not a keying fault.
- **1,157 tropes had no one-line definition** on their index page and were keyed from the name alone; most of the 658 low-confidence keys are these.

## COMMAND-LOCAL RECORDS (ruled 9/29, BOLO 91)

Not every pattern is a TV Tropes import. A record Chief keeps on purpose across the Command's own worlds files here in the register's format, flagged `source: command-local`, for attachment onto a matching TV Tropes entry in `register.json` on the next data pass.

```yaml
slug:    SignatureWound             # Command-local; not a TV Tropes page id
name:    The Signature Wound — a sibling dies in a vehicle disaster
def:     Chief's own recurring wound, kept on purpose across separate worlds, not a contradiction between them
source:  command-local
domains: [character, theme]
keys:    {character: L5, theme: R2}   # WOUND · Death — the character/theme skew's own heaviest bins
conf:    high
instances:
  - Tori (OXO/DCUS): car crash, brother Jebb dies (Ariel is Tori's earlier name)
  - Mayari (LEECHSEED): helicopter crash, brother ejected, father burns alive
note:    "likely match already in register.json (Dead Sibling / Survivor Guilt candidates) — not cross-checked against the data file in this pass; attach there once confirmed"
```

No character is changed by this ruling — it names a pattern, not a fix.

## OPEN

- **Wave B — FETCHING 10/03.** Love · Power · Emotion · Identity (theme) and Language · Costume · Graphical · Lighting · Amazing Technicolor (style → 06.1 / 06.3). Keying follows the fetch.

- **Theme sub-index pass — DONE 0.2.0.**
- **The low-confidence pass — DONE 0.3.0.** 952 definitions fetched (first sentence only), re-keyed by two PS; low confidence fell 707 → 232. 380 tropes still have no definition (their pages open without a plain first paragraph).
- **Consumers** — each system gets a TROPES section pointing at its layer lists (character, setting, genre, theme); the tracking system's story points can carry a trope id ([ssot_08](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md)).

## Version history

- **0.4.0 — 2026-10-03.** Wave A keyed: 2,122 tropes (texture 641 · tracking 111 · setting 1,412, some multi-domain) on 12 batches (A1–A12) by PS; RANGE caught a broken file, two misspelled slugs and five illegal keys → 0. **The default-dump caught at the fan-in:** the first pass put 797 setting tropes on S1 and 336 texture tropes on T7; a re-key on six batches (AR1–AR6) with sharper rules brought S1 to 366 overall and T7 to 25, and a third pass on the 281 texture nulls (AT1) confirmed most are plot content the Narrative Tropes index carries, not the telling (texture null 318). Keys for texture and tracking added to `work/89/keys.md`; `range.py` and `build_register.py` learn them.

- **0.3.1 — 2026-09-29 (BOLO 91).** Command-local record added: the SIGNATURE WOUND (a sibling dies in a vehicle disaster), Chief's own recurring pattern kept on purpose across worlds (Tori/Jebb in OXO, Mayari/brother+father in LEECHSEED); flagged for attachment to a matching TV Tropes entry (Dead Sibling / Survivor Guilt candidates) in `register.json` on the next data pass. No character changed.
- **0.3.0 — 2026-09-29.** The low-confidence pass: `fetch_defs.py` pulled 952 first-sentence definitions; two PS re-keyed them on 6 batches (R1–R6), RANGE 0 findings; character nulls 348 → 94, low confidence 707 → 232.
- **0.2.0 — 2026-09-29.** Theme sub-index pass (Chief, "Recommendations"): eight sub-indexes added, 1,854 new tropes (4,948 total), 2,012 theme keys by two PS on 9 batches (T1–T9); RANGE caught four files in the wrong JSON shape, string nulls, and five misspelled slugs, all fixed → 0.
- **0.1.0 — 2026-09-29.** BOLO 89: register stood up. 3,094 tropes fetched (`fetch.py --domains`), keyed by three PS (haiku) on 16 disjoint batches, RANGE (`work/89/range.py`) 5 findings fixed → 0.
