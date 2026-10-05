---
title: "Base 60 number system: reference"
type: "reference"
for: "A writer or designer looking up a chain, scale class, formula, threshold or rule"
does: "Lists every component and part of the base 60 doc"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_base_60_number_system.md"
source_version: "1.0.1"
---

**Who it's for:** a writer or designer looking up a number rule · **What it does:** lists every table, formula and rule in the base 60 doc · **Type:** reference

# Base 60 number system: reference

Source: `ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_base_60_number_system.md`, version 1.0.1, status canonical. The source sits on trunk BLACK at tier foundation and has no dependencies. It supersedes ranges in `ssot_02_character_systems_vertical_slice`. Last updated 2026-10-04. Why it exists: see the [concept](1-concept.md).

Notation: SC-N is a scale class with N+1 valid values (0 through N), where N divides 60. Internal means the 0-60 space. `internal = display × step`; `display = internal / step`.

## Why Base 60

- 60 is the smallest number divisible by 1, 2, 3, 4, 5 and 6. It is also a superior highly composite number.
- Prime factorization: 60 = 2² × 3 × 5.
- Divisors (12): 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.
- Effect: any formula dividing by 2, 3, 4, 5 or 6 gives an exact integer.
- Old base 10 has four divisors (1, 2, 5, 10). The old formula `SOCIAL - (projection_tendency / 3)` needed a floor operation.
- Precedent: Sumerian and Babylonian astronomy, 360 degrees, 60 minutes, 60 seconds.

## The Divisor Lattice of 60

The partial order of divisors of 60 by divisibility. The source draws it as a diagram from 1 up to 60.

- **Reading it:** every upward path from 1 to 60 is a valid divisor chain.
- **Width:** at most 4, at the {6, 4, 10, 15} level. Up to four independent scale classes coexist there.
- **Height:** the longest chain, 1→2→4→12→60, has length 5. That sets the maximum nesting depth.
- **Meet and join:** any two divisors have a greatest common divisor and a least common multiple in the lattice.

## Pattern Catalog: Divisor Chains

A divisor chain is a totally ordered subset where each element divides the next. It defines a valid scale hierarchy.

### Maximal Chains (1 to 60)

Every maximal chain passes through 1 and 60 and cannot take another divisor. The source lists 18 (C01 to C18).

| ID | Sequence | Application |
|---|---|---|
| C01 | 1→2→4→12→60 | Binary splits within a 12-unit display |
| C02 | 1→2→4→20→60 | Binary splits within a 20-unit display |
| C03 | 1→2→6→12→60 | Pair, hex, dodecimal, full |
| C04 | 1→2→6→30→60 | Pair, hex, 30-unit range, full |
| C05 | 1→2→10→20→60 | Pair, decimal, vigesimal, full |
| C06 | 1→2→10→30→60 | Pair, decimal, 30-unit range, full |
| C07 | 1→3→6→12→60 | Triad, hex, dodecimal, full |
| C08 | 1→3→6→30→60 | Tier chain: 3 tiers, 6 movements, 30-unit, full |
| C09 | 1→3→15→30→60 | Triad, 15 categories (Astrology), 30-unit, full |
| C10 | 1→5→10→20→60 | Pentad, decimal, vigesimal, full |
| C11 | 1→5→10→30→60 | Pentad, decimal, 30-unit, full |
| C12 | 1→5→15→30→60 | Pentad, 15 categories, 30-unit, full |
| C13 | 1→2→4→20→60 | Binary subdivisions of vigesimal |
| C14 | 1→3→12→60 | Layer chain: 3 tiers, 12 layers, 60 |
| C15 | 1→4→12→60 | Quad, dodecimal, full |
| C16 | 1→5→20→60 | Pentad, vigesimal, full |
| C17 | 1→6→12→60 | Movement chain: 6 movements, 12 layers, full |
| C18 | 1→6→30→60 | 6 movements, 30-unit range, full |

> **OPEN:** C13 repeats C02's sequence. The source lists both without comment.

### Architecturally Significant Chains

- **C14, the Layer Chain:** 3 tiers nest into 12 layers nest into 60. It is the spine of the character system and shows the 3-tier, 12-layer architecture is native to base 60.
- **C08, the Tier-Movement Chain:** 3 tiers, 6 movements, 30-unit range, 60-unit space.
- **C09, the Astrology Chain:** 3 tiers, 15 Character Astrology categories, 30-unit range, 60.
- **C17, the Movement-Layer Chain:** 6 movements, 12 layers, 60.

## Pattern Catalog: Matrix Decompositions

A matrix decomposition is 60 = rows × columns, one valid 2D structure.

| Rows × Cols | Mapping |
|---|---|
| 2 × 30 | Binary state across a 30-unit scale |
| 3 × 20 | 3 tiers × 20-unit attribute scale |
| 4 × 15 | 4 throughlines × 15 astrology categories |
| 5 × 12 | 5 inner planets × 12 layers |
| 6 × 10 | 6 movements × 10 outer variables per movement |
| 10 × 6 | 10 planets × 6 aspect types |
| 12 × 5 | 12 layers × 5 core variables per layer |
| 15 × 4 | 15 astrology categories × 4 element types |
| 20 × 3 | 20-unit scale × 3 tier classes |
| 30 × 2 | 30-unit scale × binary (static/dynamic) |

### Architecturally Significant Matrices

- **3 × 20, Tier-Attribute Matrix:** 3 tiers scored on a 0-20 display scale. The primary attribute matrix for L1-L3.
- **5 × 12, Planet-Layer Matrix:** which of 5 inner planets feed which of 12 layers. It expresses the feed map of deliverable 3A.
- **12 × 5, Layer-Variable Matrix:** each layer carries up to 5 core variables. A layer needs justification to define more than 5 primary variables.

## Pattern Catalog: Tensor Decompositions

A tensor decomposition factors 60 into three or more dimensions.

| Dimensions | Mapping |
|---|---|
| 2 × 2 × 15 | Binary × binary × 15 astrology categories |
| 2 × 2 × 3 × 5 | Full prime factorization, maximum decomposition |
| 2 × 3 × 10 | Static/dynamic × 3 tiers × 10-unit sub-scale |
| 2 × 5 × 6 | Binary × 5 planets × 6 movements |
| 2 × 6 × 5 | Static/dynamic × 6 movements × 5 variables |
| 3 × 4 × 5 | 3 tiers × 4 throughlines × 5 variables |
| 3 × 2 × 10 | 3 tiers × binary × 10-unit scale |
| 4 × 3 × 5 | 4 signposts × 3 tiers × 5 variables |
| 5 × 4 × 3 | 5 planets × 4 aspect types × 3 tiers |
| 6 × 2 × 5 | 6 movements × binary × 5 state variables |

### Architecturally Significant Tensors

- **3 × 4 × 5, Tier-Throughline-Variable Tensor:** which variables exist at each tier-throughline intersection. 60 cells, one per conceptual slot.
- **2 × 5 × 6, State-Planet-Movement Tensor:** which planetary variables are static or dynamic across the lifecycle. 60 cells.

## Scale Classes

Every variable gets exactly one scale class. The class fixes display range, internal range, step and divisibility.

| Class | Display | Internal | Step | Divisible by |
|---|---|---|---|---|
| SC-4 | 0–4 | 0–60 | 15 | 1, 2, 4 |
| SC-5 | 0–5 | 0–60 | 12 | 1, 5 |
| SC-6 | 0–6 | 0–60 | 10 | 1, 2, 3, 6 |
| SC-10 | 0–10 | 0–60 | 6 | 1, 2, 5, 10 |
| SC-12 | 0–12 | 0–60 | 5 | 1, 2, 3, 4, 6, 12 |
| SC-15 | 0–15 | 0–60 | 4 | 1, 3, 5, 15 |
| SC-20 | 0–20 | 0–60 | 3 | 1, 2, 4, 5, 10, 20 |
| SC-30 | 0–30 | 0–60 | 2 | 1, 2, 3, 5, 6, 10, 15, 30 |
| SC-60 | 0–60 | 0–60 | 1 | all 12 divisors |

### Scale Class Selection Rules

Apply in order.

1. The class must divide 60. No exceptions.
2. The class must give enough granularity to tell two different characters apart.
3. The class must suit every formula that consumes the variable. If a formula divides by N, N must be in the "Divisible by" set. Otherwise change the class or the formula.
4. Prefer SC-12 as the default. It divides by 1, 2, 3, 4, 6 and 12, and matches the number of layers.
5. Use SC-20 for primary attributes (L1-L3), where the GURPS legacy needs range and the human average sits at the midpoint.

## Scale Assignment Table

Assigns every numeric variable to a scale class. It replaces all earlier implicit ranges.

### Tier 1: Primary Attributes

| Variable | Class | Default | Internal step | Note |
|---|---|---|---|---|
| L1 CORE | SC-20 | 10 | 3 | GURPS IQ-equivalent. Default 10 is human average. |
| L2 VITAL | SC-20 | 10 | 3 | GURPS DX-equivalent. |
| L3 SOCIAL | SC-20 | 10 | 3 | GURPS HT-equivalent. |

### Tier 2: Secondary Attributes

| Variable | Class | Default | Derivation |
|---|---|---|---|
| L4 WILL | SC-20 | = CORE | WILL = CORE, buyable ±1-3. Matches CORE for derivation. |
| L5 WOUND | SC-12 | 0 | Assigned from history. Old range 0-10. Exact division by 2, 3, 4, 6. |
| L6 DRIVE | SC-20 | = VITAL | DRIVE = VITAL, buyable. Matches VITAL. |

### Tier 3: Sub-Variables (All Layers)

All sub-variables move from the old 0-10 range to SC-12 (0–12). The categories are attachment scores, emotional range, flexibility, stability, density and tendency. They also include index scores (shame, desire), armor index (L9), resistance index, origin seeds, coherence scores and tech level. The armor index was assigned 2026-10-04 by Selection Rules 1 to 4. Its one formula, `10 - armor_index`, subtracts and never divides, so Rule 3 holds.

### Dualism Charges (Layer-Locked Module)

- **Dualism charge:** SC-60 (signed), -30 to +30. Already base-60 native.
- **Snap boundaries:** SC-60 (extended), -60 to +60. Total range 120 = 2 × 60.

### Point Budget Values

| Variable | Cost | Class |
|---|---|---|
| CORE per level above default | 20 pts | SC-20 |
| VITAL per level above default | 20 pts | SC-20 |
| SOCIAL per level above default | 10 pts | SC-20 |
| WILL buy-up/down per level | 5 pts | SC-20 |
| DRIVE buy-up/down per level | 3 pts | SC-20 |

Finding: every cost already divides 60. No change.

### Tier Budget Totals

| Tier | Old | New |
|---|---|---|
| Tier 1 (L1-L3) | ~75 pts | ~75 pts |
| Tier 2 (L4-L6) | ~140 pts | ~140 pts |
| Tier 3 (L7-L12) | Uncapped | Uncapped |

WOUND is assigned, not bought, so it uses no budget. Tier 3 sub-variables are assigned from documentation, not purchased.

## Point Budget Recalibration

The point budget needs no structural change.

### Summary: No Structural Changes Required

- All per-level costs (20, 10, 5, 3) divide 60.
- SC-20 keeps its default (10) and cost structure.
- Tier totals are unchanged.
- The one change is a documentation convention: note each cost's lattice position.
- Format example: `L1 CORE: 13 (SC-20, display)`, internal 39 (13 × 3). The cost is 3 levels × 20 pts = 60 pts, one full base unit.

## Derived Statistic Recalibration

Every derived formula must give exact integers for all valid inputs.

### Cross-Scale Formula Handling

When a formula mixes scale classes, compute in internal 0-60 space, then assign the result to its own class. SC-20 step is 3 (display 13 is internal 39). SC-12 step is 5 (display 8 is internal 40).

### Recalibrated Formulas

The final rule: compute every derived statistic in internal space. Source text says display on SC-12.

| Stat | Internal formula | Output class | Constraint |
|---|---|---|---|
| Basic Damage Resistance | `WILL_i - (WOUND_i / 2)` | SC-30 | WOUND even only |
| Social Legibility | `SOCIAL_i - (projection_i / 3)` | SC-20 | projection_tendency in multiples of 3 |
| Narrative Momentum | `DRIVE_i + (resistance_i / 2)` | SC-30 | resistance_index even only |
| Stress Threshold | `WILL_i - WOUND_i` | SC-60 | none, no division |
| Collapse Risk | `(WOUND_i + shadow_density_i) / 2` | SC-30 | WOUND + shadow_density must be even |
| Truth Exposure Index | `SOCIAL_i + (12 - shame_index_d) × 5` | SC-60, uncapped | none, no division |

The Truth Exposure Index uses `12 - shame_d`, replacing the old `10 - shame_d`.

> **OPEN:** the source's rule says derived stats "display on SC-12", but its table assigns SC-30, SC-20 and SC-60 output classes, and the Victoria table shows SC-60. The source does not reconcile them. The source also keeps three abandoned formula attempts in this section.

### Derived Stat Divisibility Constraints Summary

| Variable | Constraint | Valid values (SC-12) | Count |
|---|---|---|---|
| WOUND | Even only | 0, 2, 4, 6, 8, 10, 12 | 7 |
| projection_tendency | Multiples of 3 | 0, 3, 6, 9, 12 | 5 |
| resistance_index | Even only | 0, 2, 4, 6, 8, 10, 12 | 7 |
| shadow_density | Parity matches WOUND, so even | 0, 2, 4, 6, 8, 10, 12 | 7 |

All other SC-12 variables take any value 0-12. All SC-20 variables (CORE, VITAL, SOCIAL, WILL, DRIVE) take any value 0-20.

## Flag Trigger Threshold Recalibration

The logic stays. Only the thresholds move to the new scales.

### SHADOWDENIAL

- Old: `WOUND > 6 AND SHADOW.projection_tendency >= 5 AND IMPRINT.conditional_patterns contains "merit_earns_freedom"`
- New: same with `projection_tendency >= 6`.
- Why: 5/10 = 50% maps to 6/12 = 50%.

### TRUTHVULNERABILITY

- Old: `SOCIAL < 12 AND FUNCTION.motivation_element = "Equity" AND SHADOW.shadow_density > 6`
- New: `SOCIAL < 12 AND FUNCTION.mc_problem_element = "Equity" AND SHADOW.shadow_density > 6`
- Why: the threshold stays 6 on SC-12. It fires slightly more easily, which suits the narrative. The field `motivation_element` is renamed `mc_problem_element`.

### OPTIONLOCKPROGRESSION

- Old: `WOUND > 7 AND DESTINY.resistance_index > 7 AND FUNCTION.limit_type = "Optionlock"`
- New: `WOUND > 8 AND DESTINY.resistance_index > 8 AND FUNCTION.limit_type = "Optionlock"`
- Why: 7/10 maps to the next valid even value, 8.

### EARNEDJUDGEMENT

- Old and new: `FUNCTION.dramatica_archetype = "Protagonist" AND FUNCTION.story_outcome = "Failure" AND WILL > 10`
- Why: no change. WILL is SC-20 and 10 is the midpoint.

### KINSHIPCOLLAPSE

- Old: `IMPRINT.attachment_style_score > 5 AND primary_attachment_object = "deceased" AND WOUND > 7`
- New: `IMPRINT.attachment_style_score > 6 AND primary_attachment_object = "deceased" AND WOUND > 8`
- Why: 5/10 maps to 6/12. WOUND follows OPTIONLOCK.

## Victoria Midnight Re-Expression

Victoria's full numeric profile in base 60.

### Tier 1

| Variable | Value | Class | Internal | Cost |
|---|---|---|---|---|
| CORE | 13 | SC-20 | 39 | 60 pts (3 levels × 20) |
| VITAL | 14 | SC-20 | 42 | 80 pts (4 levels × 20) |
| SOCIAL | 10 | SC-20 | 30 | 0 pts (default) |

Tier 1 total: 140 pts, unchanged.

### Tier 2

| Variable | Value | Class | Internal | Note |
|---|---|---|---|---|
| WILL | 14 | SC-20 | 42 | CORE + 1. Buy-up 5 pts. |
| WOUND | 10 (was 8 on SC-10) | SC-12 | 50 | 83% of capacity. Nearest even value that keeps severity. 12/12 is collapse. |
| DRIVE | 12 | SC-20 | 36 | VITAL - 2. Buy-down returns 6 pts. |

### Tier 3 Sub-Variables

| Layer | Variable | Old | New | Constraint |
|---|---|---|---|---|
| L7 | origin_stability | 4 | 4 | none |
| L7 | family_coherence | 7 | 8 | none |
| L7 | origin_wound_seed | 6 | 7 | none |
| L7 | tech_level | 6 | 7 | none |
| L8 | attachment_style_score | 6 | 7 | none |
| L8 | emotional_range | 9 | 11 | none |
| L8 | imprint_flexibility | 3 | 4 | none |
| L9 | desire_vector | 3 | 4 | none |
| L9 | shame_index | 2 | 2 | none |
| L10 | shadow_density | 7 | 8 | even (matches WOUND) |
| L10 | projection_tendency | 6 | 6 | multiples of 3 |
| L11 | resistance_index | 8 | 8 | even |

### Recalibrated Derived Statistics

| Stat | Computation | Internal result |
|---|---|---|
| Basic Damage Resistance | 42 - (50 / 2) | 17 |
| Social Legibility | 30 - (30 / 3) | 20 |
| Narrative Momentum | 36 + (40 / 2) | 56 |
| Stress Threshold | 42 - 50 | -8 |
| Collapse Risk | (50 + 40) / 2 | 45 |
| Truth Exposure Index | 30 + (12 - 2) × 5 | 80 |

- **Stress Threshold is negative (-8).** Her wound (50) exceeds her will (42) in internal space. The old mixed scales hid this. The source reads it as diagnostic: she works past her structural limit.
- **Truth Exposure Index passes 60.** It is an uncapped diagnostic, so values over 60 are valid.
- **Narrative Momentum is 56 of 60.** It confirms extreme forward energy.

## Design Rules for Future Variables

Apply when any new variable enters the system, including Layer-Locked Module sub-tables, plugin extensions and new layer variables.

1. Assign a scale class from this doc. No ad hoc ranges.
2. If the variable joins a derived formula, validate it against the divisibility constraints. A new division updates the constraint table.
3. With no formula dependency, prefer SC-12.
4. Point costs for any buyable variable must divide 60.
5. Flag thresholds must use values valid on the variable's class and its constraints.
6. Document the variable's position in the lattice chain, and name the effective grid. Example: SC-12 with even-only is {0, 2, 4, 6, 8, 10, 12}. It maps to internal {0, 10, 20, 30, 40, 50, 60}, the SC-6 grid in SC-12 notation.
7. Converting old SC-10 values to SC-12, map proportionally and round to the nearest valid value. Document the direction and the narrative reason.

Related pages: [concept](1-concept.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md)
