---
title: "The Touchstones register: reference"
type: reference
for: "A writer, designer or script author who looks up a Touchstone, a field or a rule"
does: "Lists every component of the Touchstones register with its fields, ids and links"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_touchstones_register.md
source_version: 1.0.0
---

**Who it's for:** a writer, designer or script author looking up a Touchstone · **What it does:** lists every component of the register · **Type:** reference

# The Touchstones register: reference

Source: [📐 ssot_01_touchstones_register.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_touchstones_register.md), version 1.0.0, trunk BLACK, RULED by Chief 2026-10-04 (BOLO 100 TOUCH BATCH 1, "REC."). Applies to all IPs. Dependency: `ssot_01_modern_poetics`. Why it exists: [concept](1-concept.md).

**What it holds.** Every Touchstone (formerly "invariants") and the pushbacks beside them. Cite as TS book:number.

**Built last, read first.** Chief, 9/24: the register is the user-end front door. The systems underneath are the machinery.

## THE ENTRY

Every Touchstone entry carries these fields.

| Field | Meaning |
|---|---|
| `id` | `TS n:m`. n is the source book. m runs in order within the book. |
| `name` | a short phrase |
| `strength` | `soft` or `hard`. Default soft. |
| `statement` | one line, taken from the source |
| `sources` | where the statement comes from |
| `ruled` | the date and BOLO of Chief's ruling |
| `scope` | optional; a ladder address span. See the [scale ladder](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md). |

**Books.** Book 1 is Chief's direct rulings. Book 2 is Modern Poetics.

**Pushbacks.** A pushback is a Touchstone-shaped counter-rule. Its id space is `PB n:m`. It has the same fields. The register holds it the same way as a TS entry.

## THE RULES

| # | Rule |
|---|---|
| 1 | **Hard only on Chief's word.** A Touchstone is soft unless Chief says hard. Soft means a tendency, never a rule. A Touchstone guides the story and opens up the opportunity. |
| 2 | **Claude never writes a Touchstone's content.** Claude proposes candidates quoted from their source. An id mints only on Chief's ruling. |
| 3 | **Check the ids.** `_tools/review/touchstone_check.py` greps every `TS \d+:\d+` under `ShroomsQ/_CANON/_SSOT/`. It confirms each id exists in this register. |

## TOUCHSTONES (live)

Eleven entries stand, all soft.

### Book 1 — Chief's rulings

**TS 1:1 — the bounded container.** Strength: soft.

- **Statement:** erotic or ritual power tends to hold inside a container (a circle, a rite, an end date, a boundary) and fade or turn dangerous without one. Soft means a tendency, never a rule: the sex stays fantasy first.
- **Chief's refinement:** the container lives outside the story, as a viewer-discretion disclaimer at the front of every book (fantasy, not a how-to). The scenes inside the book stay free of it.
- **Sources:** PSY.33 *Magia Sexualis*, MSX.15 *The New Topping Book*.
- **Ruled:** 2026-09-29, BOLO 91.

### Book 2 — Modern Poetics

Modern Poetics ([📐 ssot_01_modern_poetics.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_modern_poetics.md)) gives ten principles, each with a forbid-list. Chief ruled all ten in on 2026-10-04 (BOLO 100 TOUCH BATCH 1). Each entry points to its law. The register does not copy the law. All ten are soft.

| Id | Name | Statement | Law (section) |
|---|---|---|---|
| TS 2:1 | entertainment-first | The primary function of storytelling is to entertain; all other objectives ride on its back. | P1 ENTERTAINMENT-FIRST |
| TS 2:2 | the American Center | House stories are for Americans: rooted, localized, specific; universality comes by depth into the specific. | P2 THE AMERICAN CENTER |
| TS 2:3 | saturation | Sexuality is aesthetic, not genre: woven into the narrative's DNA, never flattened to sex scenes nor neutered to metaphor. | P3 SATURATION |
| TS 2:4 | originality as craft | Originality is mastery recombined with intent, never rebellion from ignorance. | P4 ORIGINALITY AS CRAFT |
| TS 2:5 | the setpiece principle | The setpiece is the apex unit of Entertainment-First design: engineered spectacle carrying theme, stakes and arc. | P5 THE SETPIECE PRINCIPLE |
| TS 2:6 | the serial hook | Every container closes on compulsion. | P6 THE SERIAL HOOK |
| TS 2:7 | the narrative dilemma | The highest-efficiency device: mutually exclusive options, real stakes on every path, double fallout for inaction. | P7 THE NARRATIVE DILEMMA |
| TS 2:8 | the fantasy drive | Every element carries its intended fantasy: what the audience gets to be, feel or do through it. | P8 THE FANTASY DRIVE |
| TS 2:9 | the sexy check | At every address, ask: is this sexy? Yes or no, then one line of why. | P9 THE SEXY CHECK |
| TS 2:10 | the aesthetic check | Every element must be interesting in at least one of color, shape or texture. | P10 THE AESTHETIC CHECK |

Each entry's ruling date is 2026-10-04, BOLO 100 TOUCH BATCH 1. Applications of P8 to P10: [three-check pass](../ssot_01_three_check_pass/2-reference.md).

## PARKED (phase 2)

Instance content. The OXO fill is phase 2. The fabula stays untouched.

- ⏸ the three vetoes (phase 2): the Truth-is-Enough Veto, the Heroic Recognition Veto and the Reset Veto. They tie to the OXO storyform. Chief rules them later.
- ⏸ cost_and_meaning (phase 2): LOCKED on the OXO storyform.
- ⏸ S12 Star-Rating rule (phase 2): ruled keep 9/15 in the worldbuilding catalog.
- ⏸ pushbacks, three (phase 2): Effectiveness Without Fairness, The Mirror of Participation, Interior Ownership of Choice. They mint as `PB n:m` when Chief rules.

## Where to go next

The ten systems, one line each.

| System | Link | Role |
|---|---|---|
| 00 Epistemology | [variable registry](../../../_SSOT/00_EPISTEMOLOGY/📐%20ssot_00_variable_registry.md) | names every field, including `touchstone` |
| 01 Narrative frameworks | [scale ladder](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md) | gives a Touchstone its address span |
| 02 Character | [character system](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_character_systems_vertical_slice.md) | carries a Touchstone at L12 |
| 03 Setting | [setting system](../../../_SSOT/03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md) | carries Touchstones on the scene card |
| 04 Plot | [plot system](../../../_SSOT/04_PLOT_SYSTEMS/📐%20ssot_04_plot_system.md) | tells the argument in time |
| 05 Operations | [standards ladder](../../../_SSOT/05_OPERATIONS/📐%20ssot_05_operations_standards_ladder.md) | sets the rung of every document |
| 06 Style guides | [prose style guide](../../../_SSOT/06_STYLE_GUIDES/📐%20ssot_06_1_prose_style.md) | cites TS 1:1 |
| 07 Theme | [theme system](../../../_SSOT/07_THEME_SYSTEMS/📐%20ssot_07_theme_system.md) | argues; Touchstones hold |
| 08 Tracking | [tracking system](../../../_SSOT/08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) | tracks state |
| 09 Worldbuilding | [worldbuilding system](../../../_SSOT/09_WORLDBUILDING_SYSTEMS/📐%20ssot_09_worldbuilding_system.md) | holds the shared world |

**Sources and shelf.** Nothing in the register is new canon. The rules about rules: [DOCTRINE 0](../../../../../DOCTRINE-0-INVARIANTS.md), ratified 2026-09-03, seven rules; the file keeps its name. The 9/24 distill: [DISTILL.md](../../../../../_tools/bolostatus/work/81/DISTILL.md) (22 invariants in canon, 5 contradictions). The old reference shelf: [NNI-INDEX.md](../../../../../_tools/bolostatus/work/81/NNI-INDEX.md) (47 works, 188 invariants, three pushbacks quoted in full). Live wires: the scale ladder's completion tests, the collision engine's L12 × S12 row, character L12 `touchstone`, setting S12, and the scene cards' `touchstones:` field.

**Version history.** 1.0.0 (2026-10-04, BOLO 100 TOUCH BATCH 1): schema, rules, field rename, front-door links; TS 2:1 to TS 2:10 ruled in; vetoes and instance rules parked. 0.9.0 (2026-10-04, registers batch 1): frontmatter normalized; P1 to P10 listed as candidates. 0.1.0 (2026-09-29): TS 1:1 landed by direct ruling (BOLO 91); bootstrap stood up 2026-09-24.
