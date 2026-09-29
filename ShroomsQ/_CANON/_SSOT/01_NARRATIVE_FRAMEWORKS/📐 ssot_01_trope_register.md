---
type: ssot_01_narrative_frameworks
category: trope_register
version: 0.2.0
last_updated: 2026-09-29
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

**The keys (ruled 9/29):** character → L1–L12 · setting → S1–S12 · genre → G1–G12 · sexuality → the character layers (mostly L9 EROS) · theme → the four rails R1–R4 of the [theme system](../07_THEME_SYSTEMS/📐%20ssot_07_theme_system.md), or null.

## THE COUNTS (2026-09-29)

**4,948 tropes**, all keyed (v0.2.0, after the theme sub-index pass) · confidence: high 3,835 · medium 564 · low 707 · 207 serve more than one domain.

| Domain (index) | Keyed by layer |
|---|---|
| **character** (Characters As Device · Characterization · Archetypal Character) | L1 291 · L2 38 · L3 156 · L4 32 · L5 26 · L6 34 · L7 31 · L8 43 · L9 26 · L10 40 · L11 51 · **L12 508** · null 348 |
| **sexuality** (Sex Tropes · Queer Romance) | **L9 428** · L5 11 · L2 2 · L1 1 · L7 1 · null 2 |
| **setting** (Settings) | **S1 276** · S2 3 · S3 24 · S4 40 · S5 21 · S6 14 · S7 30 · S8 37 · S9 21 · S10 35 · S11 55 · S12 21 · null 66 |
| **genre** (Genres · Genre Tropes) | **G1 60** · G2 11 · G3 2 · G5 2 · G8 2 · G11 2 · null 26 |
| **theme** (Truth and Lies · Death · Family · Betrayal · Revenge · Authority · Memory · The Secret · Promises and Vows) | R1 274 · **R2 560** · R3 321 · R4 386 · null 797 |

**The pull list:** [LAYERS.md](../../../../_tools/tropes/data/domains/LAYERS.md) lists every layer with every trope keyed to it.

## READING THE SKEW

- **Character piles on L12 FUNCTION (508) and L1 CORE (291).** The Characters As Device index is mostly cast roles and types; that is what the index holds, not a keying fault.
- **Setting piles on S1 BODY (276).** The Settings index lists place types (the castle, the diner); the deeper layers (S2 WEATHER 3) are thin because TV Tropes has few tropes for them.
- **Theme nulls run high (797)** because Death (1,035) and Family are broad: most of those tropes argue none of the four rails. That is the rails being narrow, not a keying fault.
- **1,157 tropes had no one-line definition** on their index page and were keyed from the name alone; most of the 658 low-confidence keys are these.

## OPEN

- **Theme sub-index pass — DONE 0.2.0.**
- **The 658 low-confidence keys** — a second pass once definitions are pulled from the trope pages' first line (one-line only, the public-repo rule).
- **Consumers** — each system gets a TROPES section pointing at its layer lists (character, setting, genre, theme); the tracking system's story points can carry a trope id ([ssot_08](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md)).

## Version history

- **0.2.0 — 2026-09-29.** Theme sub-index pass (Chief, "Recommendations"): eight sub-indexes added, 1,854 new tropes (4,948 total), 2,012 theme keys by two PS on 9 batches (T1–T9); RANGE caught four files in the wrong JSON shape, string nulls, and five misspelled slugs, all fixed → 0.
- **0.1.0 — 2026-09-29.** BOLO 89: register stood up. 3,094 tropes fetched (`fetch.py --domains`), keyed by three PS (haiku) on 16 disjoint batches, RANGE (`work/89/range.py`) 5 findings fixed → 0.
