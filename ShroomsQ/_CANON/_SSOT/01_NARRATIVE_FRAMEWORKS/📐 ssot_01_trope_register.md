---
type: ssot_01_narrative_frameworks
category: trope_register
version: 1.2.0
tier: narratology
last_updated: 2026-10-31
applies_to: [OVEREXITOUT, all future IPs]
status: "v1.2.0 2026-10-31 (Chief: \"run what you need\"; provisional, Chief asleep): register v0.6.0, the 642 low-confidence tropes re-keyed by reading (RR1–RR7), RANGE 0; the plot graph reads the full register. v1.0.0 2026-10-04: RULED, Chief (\"rec\") — BOLO 100 registers batch 1: undefined-trope rule written; OPEN list closed. Earlier: RULED 2026-09-29 — BOLO 89 (Chief, \"I'll recommend\" · \"go\" · \"all recommendations\"); keyed by three PS batches, RANGE-checked (0 findings)"
purpose: "THE TROPE REGISTER: one trope layer under every system. 8,700 TV Tropes tropes, each tagged with the domains it serves and keyed to a layer of that domain's slice, so any layer can pull its tropes."
dependencies: ["ssot_04_trope_graph (the plot consumer)", "ssot_02_character_systems_vertical_slice", "ssot_03_setting_system", "ssot_01_genre_system", "ssot_06_theme_system"]
trunk: BLACK
sources: ["_tools/tropes/fetch.py --domains", "_tools/bolostatus/work/89/keys.batch*.json (01–16 · T · R · A · AR · AT · B · BR · RR1–RR7)", "_tools/tropes/build_register.py"]
rung: standard
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

**Undefined tropes (RULED 2026-10-04):** a trope with no one-line definition keys by its title and its domain tags. The record carries `def: undefined`. No run is needed to fill it.

**The keys (ruled 9/29):** character → L1–L12 · setting → S1–S12 · genre → G1–G12 · sexuality → the character layers (mostly L9 EROS) · theme → the four rails R1–R4 of the [theme system](../06_THEME_SYSTEMS/📐%20ssot_06_theme_system.md), or null. **Added 0.4.0 (wave A, ruled 9/29 "all recs"):** texture → T1–T12 of the [texture system](📐%20ssot_01_texture_system.md) · tracking → the parts of the [tracking system](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md): world_clock · told_order · grid · story_point · cable · tempo.

**One key store (IF-01-04-22; IF catalog call 10, ruled 2026-10-05).** `register.json` is the one key store for every trope. The plot trope graph reads its keys from it. The graph's node keying (`node`, `alt`, `conf`) is a view of the same fetch, not a second store. The setting-domain keys S1–S12 live here only.

**Interfaces.** Read from 06 (IF-01-06-06): rail ids R1–R4 as the value of `keys.theme`; null if a trope argues no rail; `conf` low when `def` is undefined; Chief decides tropes that need two rails.

## THE COUNTS (2026-10-31, v0.6.0)

**8,700 tropes, all keyed** · confidence: high 6,395 · medium 2,140 · low 165 · 757 still have no one-line definition (112 of them low).

| Domain (index) | Keyed by layer |
|---|---|
| **character** (Characters As Device · Characterization · Archetypal Character) | L1 319 · L2 63 · L3 201 · L4 57 · L5 41 · L6 69 · L7 83 · L8 50 · L9 62 · L10 86 · L11 58 · **L12 533** · null 2 |
| **sexuality** (Sex Tropes · Queer Romance) | **L9 431** · L5 10 · L2 2 · L1 1 · L7 1 · null 0 |
| **setting** (Settings · Religion · School · Motor Vehicle · Cyberpunk · Drugs · Military and Warfare) | S1 396 · S2 38 · S3 57 · **S4 419** · S5 79 · S6 143 · S7 74 · **S8 379** · S9 40 · S10 113 · S11 105 · S12 23 · null 431 |
| **genre** (Genres · Genre Tropes) | **G1 66** · G2 11 · G3 5 · G4 3 · G5 6 · G6 2 · G8 3 · G9 3 · G10 1 · G11 4 · null 1 |
| **theme** (the nine thematic indexes + wave B: Love · Power · Emotion · Identity) | R1 428 · **R2 854** · R3 400 · R4 455 · null 1,215 |
| **texture** (Narrative Devices · Framing Device · Narrative Tropes · Point of View) | T1 53 · T2 62 · T3 86 · T4 42 · T5 17 · T6 39 · T7 79 · T8 31 · T9 41 · T10 12 · T11 20 · T12 14 · null 248 |
| **tracking** (Time Tropes) | world_clock 48 · grid 43 · tempo 13 · told_order 5 · story_point 2 · null 5 |
| **style** (wave B: Language · Costume · Graphical · Lighting · Amazing Technicolor) | 07.1 PROSE 267 · **07.3 PAGES 440** · null 125 |

**The pull list:** [LAYERS.md](../../../../_tools/tropes/data/domains/LAYERS.md) lists every layer with every trope keyed to it.

## READING THE SKEW

- **Character piles on L12 FUNCTION (533) and L1 CORE (319).** The Characters As Device index is mostly cast roles and types; that is what the index holds, not a keying fault.
- **Setting piles on S4 LAW (419), S1 BODY (396) and S8 HABIT (379).** The Settings index lists place types (the castle, the diner); the deeper layers (S2 WEATHER 38) are thin because TV Tropes has few tropes for them.
- **Theme nulls run high (1,215)** because Death (1,035) and Family are broad: most of those tropes argue none of the four rails. That is the rails being narrow, not a keying fault.
- **757 tropes have no one-line definition** and are keyed from the name alone. The v0.6.0 re-key read every low-confidence trope again: a well-known name went to medium, high only where a definition plainly fits the layer, and a theme key with no definition stays low (IF-01-06-06). 165 low remain, 112 of them undefined.
- **Setting and texture nulls (431 · 248) are plot content, not a keying fault.** The Military, Religion and Narrative Tropes indexes carry combat, plot and gag tropes (Zerg Rush, Evil Plan) that describe events, not a place or a telling; they key null, as wave A ruled for texture.

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

- **Definitions (closed 2026-10-04; retried 2026-10-31)** — 757 tropes keep `def: undefined` under the rule above; the keys stand. The 10/31 run of `fetch_defs.py` (certifi CA bundle, 404s and redirects recorded in `defs_status.json`, stops on the first 403) got **HTTP 403 from TV Tropes on its first request** and stopped; 34 defs came from the plot pull's index instead. The script resumes as is if the site lets it back in.
- **Consumer TROPES sections** — `⏸ TROPES pointer sections (phase 2)`. Each system doc gets one section pointing at its layer lists, as a call in that doc's own batch. The tracking system's story points can carry a trope id ([ssot_08](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md)).
- **Done earlier:** wave B (0.5.0) · theme sub-index pass (0.2.0) · low-confidence pass (0.3.0).

## Rebuild the register

The author runs `python _tools/tropes/fetch.py --domains` to pull the indexes. The script waits one second per request, skips slugs already cached, and stores no page bodies. PS batches write the keys to `_tools/bolostatus/work/89/keys.batch*.json`. The author then runs `python _tools/tropes/build_register.py` with no arguments. It writes `register.json` and `LAYERS.md` and prints the counts table.

## Version history

- **1.2.0 — 2026-10-31 · register v0.6.0** (Chief: "run what you need"; provisional, Chief asleep). The 642 low-confidence tropes re-keyed by reading, in seven batches (RR1–RR7, `work/89/rr/`), each to a layer of its own domain's slice. RANGE 0 findings. Confidence high 6,389 → 6,395 · medium 1,669 → 2,140 · low 642 → 165. The old pass had parked plot-content texture tropes on T4 DURATION; those now key null. Definitions: TV Tropes answered 403, so no live fetch; 34 recovered from the plot pull, no-def 791 → 757. `build_register.py` now maps the BOLO 103 style renumber (06.x → 07.x) itself, so a rebuild no longer reverts it, and `range.py` accepts both. The plot trope graph (`build_graph.py`) now reads the full register for names, defs and links, and carries each shared trope's register keys (344 of its 1,034). Node keys and edges are unchanged.
- **1.1.1 — 2026-10-05.** BOLO 102 batch D (Chief: "All recommendations"): the 0.5.0 wave B count is corrected to the batch files, 2,198 keys on 2,175 tropes (theme 1,014 · style 832 · stragglers 352); the old line said 2,175 keys and its parts summed to 2,195.
- **1.1.0 — 2026-10-05.** BOLO 102 stage 2 (Chief: "My word"): `register.json` is the one key store and the trope graph reads it (call 10); interfaces line for 06.
- **1.0.2 — 2026-10-05.** BOLO 102 batch C (Chief: "all recs"): Rebuild the register section: command steps for fetch.py and build_register.py (C40).
- **1.0.1 · 2026-10-05** — BOLO 102 batch A (Chief: "All recs go"): purpose line says 8,700 tropes; skew section recomputed from the counts table.
- **1.0.0 — 2026-10-04 (BOLO 100 registers batch 1, Chief "rec").** Undefined-trope rule written: no definition means key by title and domain tags, flagged `undefined`. OPEN list closed; consumer TROPES sections parked as `⏸ TROPES pointer sections (phase 2)`.

- **0.5.0 — 2026-10-03.** Wave B keyed: 2,198 keys on 2,175 tropes on 9 PS batches (B1–B9) — theme 1,014 (Love · Power · Emotion · Identity) · style 832 (Language · Costume · Graphical · Lighting · Amazing Technicolor → 07.1 PROSE / 07.3 PAGES) · plus 352 straggler setting/texture/tracking keys from tropes that wave A's index re-run tagged after keying. RANGE caught one file with unquoted keys and three missing domain keys → 0. The spread check passed: no layer swallowed a domain. Every trope in the index is keyed.

- **0.4.0 — 2026-10-03.** Wave A keyed: 2,122 tropes (texture 641 · tracking 111 · setting 1,412, some multi-domain) on 12 batches (A1–A12) by PS; RANGE caught a broken file, two misspelled slugs and five illegal keys → 0. **The default-dump caught at the fan-in:** the first pass put 797 setting tropes on S1 and 336 texture tropes on T7; a re-key on six batches (AR1–AR6) with sharper rules brought S1 to 366 overall and T7 to 25, and a third pass on the 281 texture nulls (AT1) confirmed most are plot content the Narrative Tropes index carries, not the telling (texture null 318). Keys for texture and tracking added to `work/89/keys.md`; `range.py` and `build_register.py` learn them.

- **0.3.1 — 2026-09-29 (BOLO 91).** Command-local record added: the SIGNATURE WOUND (a sibling dies in a vehicle disaster), Chief's own recurring pattern kept on purpose across worlds (Tori/Jebb in OXO, Mayari/brother+father in LEECHSEED); flagged for attachment to a matching TV Tropes entry (Dead Sibling / Survivor Guilt candidates) in `register.json` on the next data pass. No character changed.
- **0.3.0 — 2026-09-29.** The low-confidence pass: `fetch_defs.py` pulled 952 first-sentence definitions; two PS re-keyed them on 6 batches (R1–R6), RANGE 0 findings; character nulls 348 → 94, low confidence 707 → 232.
- **0.2.0 — 2026-09-29.** Theme sub-index pass (Chief, "Recommendations"): eight sub-indexes added, 1,854 new tropes (4,948 total), 2,012 theme keys by two PS on 9 batches (T1–T9); RANGE caught four files in the wrong JSON shape, string nulls, and five misspelled slugs, all fixed → 0.
- **0.1.0 — 2026-09-29.** BOLO 89: register stood up. 3,094 tropes fetched (`fetch.py --domains`), keyed by three PS (haiku) on 16 disjoint batches, RANGE (`work/89/range.py`) 5 findings fixed → 0.
