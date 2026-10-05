---
title: "Astrology ingest template: reference"
type: reference
for: "A writer filling the blank astrology ingest form who needs to know what each section holds"
does: "Lists every section of the form with its fields, sources and rules"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_astrology_ingest.md
source_version: 1.0.0
---

**Who it's for:** a writer filling the blank astrology ingest form · **What it does:** lists every section of the form with its fields, sources and rules · **Type:** reference

# Astrology ingest template: reference

Why the form exists: [concept](1-concept.md). Steps: [how-to](3-how-to.md). A fill-in lesson: [tutorial](4-tutorial.md). Source: [ssot_02_template_astrology_ingest.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_template_astrology_ingest.md), version 1.0.0, status RULED, BOLO 100 C18.

Dependencies named in the source: character astrology, the DAI doc, the 12-layer mapping doc, the Dramatica ingest template, the Step 1 source verification protocol. Applies to OVEREXITOUT, ASTRO7EX and LAKAD.

## How to use this form

Five instructions, then a minimum chart rule.

1. Copy the file to the character's folder as `[CHARACTER_ID]_astrology_ingest.md`, as the Step 1 protocol sets out.
2. Delete this section and the frontmatter. Keep the section numbers. The Step 1 checks cite them.
3. Work in DAI order: planets, then angles, aspects, houses, dignities, the 12th House.
4. Give every sign a one or two sentence derivation: the Dramatica input, the rule used, why the sign fits.
5. Leave a field empty if the storyform does not give it yet. Write `⏸` and the reason. Never guess.

**Minimum viable chart** (status `minimum_viable`): sections 1 to 5 and 8 to 10. It needs Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant signs, at least three aspects, and houses for those seven planets. Sections 6 and 7 can wait.

A Tier 2 character gets a partial chart (Sun, Moon, one defining aspect) and does not use this form.

## Header

A YAML block. One per character.

| Field | Meaning |
|---|---|
| `character_id` | The character's id. |
| `ip` | The intellectual property. |
| `tier` | Set to 3. |
| `dramatica_ingest_ref` | Path to the locked Dramatica Ingest. |
| `storyform_id` | The storyform's id. |
| `storyform_version` | The storyform's version. |
| `template_status` | `draft`, `minimum_viable` or `locked`. Starts at `draft`. |
| `dai_doc_version` | The DAI doc version used. |
| `locked_on` | Lock date. |

## 1. Personal Planets

Table columns: Planet (function), Dramatica source, Sign, Derivation.

| Planet | Function | Dramatica source |
|---|---|---|
| Sun | `IDENTITY_AXIS` | MC Domain + MC Concern |
| Moon | `INTERNAL_STATE` | MC Problem + MC Response |
| Mercury | `CODE_INTERPRETATION` | Unique Ability + Methodology quad |
| Venus | `VALUE_VECTOR` | MC Concern + Purpose quad |
| Mars | `ACTION_PROTOCOL` | Approach + Motivation quad |

## 2. Structural Planets

Same columns.

| Planet | Function | Dramatica source |
|---|---|---|
| Saturn | `ENTROPY_LIMITER` | MC Critical Flaw + Inhibitor |
| Jupiter | `REDUNDANCY` | MC Unique Ability |
| Uranus | `BREACH_PROTOCOL` | MC Solution |
| Neptune | `HAUNT_SIGNAL` | MC Symptom |
| Pluto | `TERMINATION_CODE` | Story Outcome + Story Judgment |

## 3. Angles

Same columns.

| Angle | Function | Dramatica source |
|---|---|---|
| Ascendant | `CHARACTER_UI_SKIN` | Approach + MC Critical Flaw |
| Midheaven | `CHARACTER_OUTPUT_LOG` | Story Goal + OS role |
| Descendant | `CHARACTER_SHADOW_INTERFACE` | MC Direction (opposite the Ascendant) |
| IC | `CHARACTER_ROOT_ORIGIN` | MC Benchmark (opposite the Midheaven) |

## 4. Aspect Map

At least three aspects for the minimum viable chart. Each cites its Dramatica tension source.

Columns: Planet A, Planet B, Aspect, Dramatica tension source, Gate, Note.

Aspect types and their Dramatica sources:

| Aspect | Source of tension |
|---|---|
| Opposition | Problem / Solution |
| Square | Focus / Direction |
| Conjunction or Square | Unique Ability / Critical Flaw |
| Trine | Reinforcing elements in a quad |

Rule: where sign geometry disagrees with the Dramatica tension, the Dramatica tension governs.

> **OPEN:** the aspect list omits the Sextile that the astrology doc names as a soft aspect.

## 5. House Placements

Opens with one line: MC Domain emphasis pattern. Then a table: Planet, House, Justification.

Rows: Sun, Moon, Mercury, Venus, Mars, Saturn, and Ascendant. The Ascendant house is fixed at 1.

## 6. Dignities

Columns: Planet, Sign, Dignity, Override and justification. Dignity takes one of three values: Essential Dignity, Essential Debility, Peregrine. This section can wait for a minimum viable chart.

## 7. 12th House / Void Contents

Columns: Planet, Submerged Dramatica function, Link to L10 SHADOW content. This section can wait for a minimum viable chart.

## 8. Chart Summary

Six to ten sentences in plain words. The summary says what the chart says about the character and where it pulls in two directions.

## 9. 12-Layer Feed Map

Fill in against the 12-layer mapping doc. The chart justifies a layer value and never sets one. Schema 2.5.0 and 3.0.0 fields are not chart-fed.

Columns: Layer, Chart source, Consistent with the layer value? (yes, no or exception), Feed notes and conflict resolution.

| Layer | Chart source |
|---|---|
| L1 CORE | Sun, Mercury |
| L2 VITAL | Mars, Ascendant |
| L3 SOCIAL | Ascendant, Venus, 7th House |
| L4 WILL | Saturn, Sun-Saturn aspects |
| L5 WOUND | Debilitated planets, hard Moon aspects, 8th House |
| L6 DRIVE | Mars, Jupiter |
| L7 ORIGIN | IC, 4th House, Moon (partial) |
| L8 IMPRINT | Moon, Moon aspects, Moon dignity |
| L9 EROS | Venus, Mars-Venus aspect, 5th and 8th House (supplemental) |
| L10 SHADOW | 12th House, debilitated planets, Pluto |
| L11 DESTINY | Jupiter, Uranus, Midheaven |
| L12 FUNCTION | None (fed from the Dramatica Ingest). The row reads n/a. |

When the authoritative document is ambiguous, log the resolution in the notes column, as the mapping doc's conflict protocol says.

## 10. Status and Lock

A checklist with seven boxes.

- `dramatica_ingest_ref` points to a locked Dramatica Ingest.
- Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant are assigned, each with a derivation.
- The aspect map has at least three aspects.
- Houses are assigned for the seven planets.
- The chart summary is written.
- The feed map is complete.
- The Feed Validation Checklist (mapping doc) was run and passed, or exceptions were logged. This is needed for `locked`, not for `minimum_viable`.

Then the line `template_status`. A `minimum_viable` chart passes the Step 1 gate as a yellow light. Layers fed by the chart carry `[ASTROLOGY_PENDING]` until `locked`.
