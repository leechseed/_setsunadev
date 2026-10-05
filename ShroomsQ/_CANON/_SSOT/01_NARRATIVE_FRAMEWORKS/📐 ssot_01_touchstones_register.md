---
type: ssot_01_narrative_frameworks
category: touchstones_register
version: 1.0.1
tier: narratology
last_updated: 2026-10-05
applies_to: [all IPs]
status: "v1.0.0 2026-10-04: RULED, Chief (\"REC.\") — BOLO 100 TOUCH BATCH 1: schema, rules, field rename, front-door links; ten Modern Poetics principles ruled in as TS 2:1 to TS 2:10."
purpose: "THE TOUCHSTONES REGISTER: the one home for every Touchstone, the rules the story guides itself by, and the front door a reader enters by."
dependencies: ["ssot_01_modern_poetics"]
trunk: BLACK
---

# The Touchstones register

**What this is.** The one home for every Touchstone (formerly "invariants") and the pushbacks beside them. Each entry follows the schema below. Cite an entry as TS book:number, for example TS 1:1.

Chief, 2026-09-24: *"the invariants should come last, after all the systems are put through … at least for now, just some sort of bootstrap to keep there as a placeholder, just to know that we have it."*

**Built last, read first.** Chief, 9/24: *"invariants first … basically user-end first. While the system underneath is more complex, invariants are … the easy way in to understand."* The register is the front door a reader enters by. The systems underneath are the machinery. It was written last so it describes the finished machinery.

## THE ENTRY

Every Touchstone entry carries these fields.

- **id:** `TS n:m`. Book n is the source book. Number m runs in order within the book.
- **name:** a short phrase.
- **strength:** `soft` or `hard`. The default is soft.
- **statement:** one line, taken from the source.
- **sources:** where the statement comes from.
- **ruled:** the date and the BOLO of Chief's ruling.
- **scope** (optional): a ladder address span. See the [scale ladder](📐%20ssot_01_scale_ladder.md).

**Books.** Book 1 is Chief's direct rulings. Book 2 is Modern Poetics.

**Pushbacks.** A pushback is a Touchstone-shaped counter-rule. It has its own id space, `PB n:m`, and the same fields. The register holds a PB entry the same way it holds a TS entry.

## THE RULES

1. **Hard only on Chief's word.** A Touchstone is soft unless Chief says hard. Soft means a tendency, never a rule. A Touchstone guides the story and opens up the opportunity.
2. **Claude never writes a Touchstone's content.** Claude proposes candidates quoted from their source. An id mints only on Chief's ruling.
3. **Check the ids.** The script `_tools/review/touchstone_check.py` greps every `TS \d+:\d+` under `ShroomsQ/_CANON/_SSOT/`. It confirms each id exists in this register. The author runs `python _tools/review/touchstone_check.py` from the repo root, with no arguments. The script prints `register ids: N | citations checked: M`, then one `MISSING TS x:y  path:line` per unknown id. It ends with `PASS` or `FAIL (n unregistered)`. It exits 0 on a pass and 1 on a fail.

## TOUCHSTONES (live)

### Book 1 — Chief's rulings

**TS 1:1 — the bounded container.** *strength: soft*

Erotic or ritual power tends to hold inside a container — a circle, a rite, an end date, a boundary — and fade or turn dangerous without one. **Soft** means a tendency, never a rule: the sex stays fantasy first.

**Chief's refinement:** the container lives *outside* the story, as a viewer-discretion disclaimer at the front of every book (fantasy, not a how-to) — so the scenes inside the book stay free of it.

**Sources:** PSY.33 *Magia Sexualis*, MSX.15 *The New Topping Book*.

**Ruled:** 2026-09-29, BOLO 91.

### Book 2 — Modern Poetics

[Modern Poetics](📐%20ssot_01_modern_poetics.md) gives ten principles, each with a forbid-list. Chief ruled all ten in on 2026-10-04. Each entry points to its law. This register does not copy the law.

**TS 2:1 — entertainment-first.** *strength: soft*

The primary function of storytelling is to entertain; all other objectives ride on its back.

**Sources:** `ssot_01_modern_poetics.md`, section P1 (ENTERTAINMENT-FIRST) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:2 — the American Center.** *strength: soft*

House stories are for Americans: rooted, localized, specific; universality comes by depth into the specific.

**Sources:** `ssot_01_modern_poetics.md`, section P2 (THE AMERICAN CENTER) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:3 — saturation.** *strength: soft*

Sexuality is aesthetic, not genre: woven into the narrative's DNA, never flattened to sex scenes nor neutered to metaphor.

**Sources:** `ssot_01_modern_poetics.md`, section P3 (SATURATION) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:4 — originality as craft.** *strength: soft*

Originality is mastery recombined with intent, never rebellion from ignorance.

**Sources:** `ssot_01_modern_poetics.md`, section P4 (ORIGINALITY AS CRAFT) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:5 — the setpiece principle.** *strength: soft*

The setpiece is the apex unit of Entertainment-First design: engineered spectacle carrying theme, stakes and arc.

**Sources:** `ssot_01_modern_poetics.md`, section P5 (THE SETPIECE PRINCIPLE) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:6 — the serial hook.** *strength: soft*

Every container closes on compulsion.

**Sources:** `ssot_01_modern_poetics.md`, section P6 (THE SERIAL HOOK) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:7 — the narrative dilemma.** *strength: soft*

The highest-efficiency device: mutually exclusive options, real stakes on every path, double fallout for inaction.

**Sources:** `ssot_01_modern_poetics.md`, section P7 (THE NARRATIVE DILEMMA) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:8 — the fantasy drive.** *strength: soft*

Every element carries its intended fantasy: what the audience gets to be, feel or do through it.

**Sources:** `ssot_01_modern_poetics.md`, section P8 (THE FANTASY DRIVE) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:9 — the sexy check.** *strength: soft*

At every address, ask: is this sexy? Yes or no, then one line of why.

**Sources:** `ssot_01_modern_poetics.md`, section P9 (THE SEXY CHECK) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

**TS 2:10 — the aesthetic check.** *strength: soft*

Every element must be interesting in at least one of color, shape or texture.

**Sources:** `ssot_01_modern_poetics.md`, section P10 (THE AESTHETIC CHECK) — [the law, forbids and dictum](📐%20ssot_01_modern_poetics.md).

**Ruled:** 2026-10-04, BOLO 100 TOUCH BATCH 1.

## PARKED (phase 2)

These are instance content. The OXO fill is phase 2. The fabula stays untouched.

- ⏸ the three vetoes (phase 2) — the Truth-is-Enough Veto, the Heroic Recognition Veto and the Reset Veto. They tie to the OXO storyform. Chief rules them later.
- ⏸ cost_and_meaning (phase 2) — LOCKED on the OXO storyform.
- ⏸ S12 Star-Rating rule (phase 2) — ruled keep 9/15 in the worldbuilding catalog.
- ⏸ pushbacks, three (phase 2) — Effectiveness Without Fairness, The Mirror of Participation, Interior Ownership of Choice. They mint as `PB n:m` when Chief rules.

## Sources and shelf

Nothing here is new canon.

- **The rules about rules:** [DOCTRINE 0](../../../../DOCTRINE-0-INVARIANTS.md), ratified 2026-09-03. Seven rules. The file keeps its name; the name ruling closed 9/24.
- **Everything the Command holds, distilled 9/24:** [`_tools/bolostatus/work/81/DISTILL.md`](../../../../_tools/bolostatus/work/81/DISTILL.md) — the 22 invariants in canon, where each is wired, 5 contradictions, the seams not wired.
- **The old reference shelf:** [`_tools/bolostatus/work/81/NNI-INDEX.md`](../../../../_tools/bolostatus/work/81/NNI-INDEX.md) — 47 works, 188 invariants (script-counted), and the three pushbacks quoted in full.
- **The live wires:** the scale ladder's completion tests · the collision engine's L12 × S12 row · character L12 `touchstone` · setting S12 · the scene cards' `touchstones:` field.

## Where to go next

The ten systems, one line each.

- **00 Epistemology:** [the variable registry](../00_EPISTEMOLOGY/📐%20ssot_00_variable_registry.md) names every field, including `touchstone`.
- **01 Narrative frameworks:** [the scale ladder](📐%20ssot_01_scale_ladder.md) gives a Touchstone its address span.
- **02 Character:** [the character system](../02_CHARACTER_SYSTEMS/📐%20ssot_02_character_systems_vertical_slice.md) carries a Touchstone at L12.
- **03 Setting:** [the setting system](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md) carries Touchstones on the scene card.
- **04 Plot:** [the plot system](../04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md) tells the argument in time.
- **09 Operations:** [the standards ladder](../09_OPERATIONS/📐%20ssot_09_operations_standards_ladder.md) sets the rung of every document.
- **07 Style guides:** [the prose style guide](../07_STYLE_GUIDES/📐%20ssot_07_1_prose_style.md) cites TS 1:1.
- **06 Theme:** [the theme system](../06_THEME_SYSTEMS/📐%20ssot_06_theme_system.md) argues; Touchstones hold.
- **08 Tracking:** [the tracking system](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) tracks state.
- **05 Worldbuilding:** [the worldbuilding system](../05_WORLDBUILDING_SYSTEMS/📐%20ssot_05_worldbuilding_system.md) holds the shared world.

## Version history

- **1.0.1 — 2026-10-05.** BOLO 102 batch C (Chief: "all recs"): command-line form and output of the check script written into rule 3 (C37).
- **1.0.0 — 2026-10-04 (BOLO 100 TOUCH BATCH 1, Chief "REC.").** Schema, rules, field rename, front-door links; Chief ruled the candidates in as TS 2:1 to TS 2:10. Vetoes and instance rules parked by name. The "What waits" list closed; its pointer, [DOPE SHEET 81](https://claude.ai/artifact/Uc8e84mmzY8gBjSHPjrCW7), moves here.
- **0.9.0 — 2026-10-04 (BOLO 100 registers batch 1, Chief "rec").** Frontmatter normalized to the 01 shape (R10). P1–P10 listed as candidate Touchstones (R7).
- **0.1.0 — 2026-09-29.** TS 1:1, the bounded container, landed early by direct ruling (BOLO 91). Bootstrap register stood up 2026-09-24.
