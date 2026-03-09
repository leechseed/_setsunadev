---

## type: ssot_00_foundations category: number_systems version: 1.0.0 last_updated: 2026-03-08 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the base 60 (sexagesimal) number system as the foundational source for all integers in the LEECHSEED character pipeline. Establishes the divisor lattice, valid scale classes, pattern catalog, scale assignments, point budget recalibration, derived stat recalibration, and flag threshold recalibration." dependencies: [] supersedes_ranges_in: ["ssot_03_character_systems_vertical_slice"]
---

# 📐 SSOT: Base 60 Number System

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [Why Base 60](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#why-base-60)
3. [The Divisor Lattice of 60](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-divisor-lattice-of-60)
4. [Pattern Catalog: Divisor Chains](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pattern-catalog-divisor-chains)
5. [Pattern Catalog: Matrix Decompositions](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pattern-catalog-matrix-decompositions)
6. [Pattern Catalog: Tensor Decompositions](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pattern-catalog-tensor-decompositions)
7. [Scale Classes](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#scale-classes)
8. [Scale Assignment Table](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#scale-assignment-table)
9. [Point Budget Recalibration](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#point-budget-recalibration)
10. [Derived Statistic Recalibration](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#derived-statistic-recalibration)
11. [Flag Trigger Threshold Recalibration](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#flag-trigger-threshold-recalibration)
12. [Victoria Midnight Re-Expression](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#victoria-midnight-re-expression)
13. [Design Rules for Future Variables](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#design-rules-for-future-variables)
14. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

Every integer in the LEECHSEED character system derives from base 60. No numeric scale, point cost, threshold, or range is arbitrary. All are locked to patterns within the sexagesimal divisor lattice.

This document is the mathematical foundation. The Variable Registry (Phase 1) consumes this document for all numeric range definitions. The Vertical Slice SSOT consumes this document for point budgets, derived stat formulas, and flag trigger thresholds. Every downstream system that touches a number references this SSOT as the authority on why that number exists.

---

## Why Base 60

60 is the smallest number divisible by 1, 2, 3, 4, 5, and 6. It is a superior highly composite number — it has more divisors relative to its size than any smaller integer.

**The prime factorization:** 60 = 2² × 3 × 5

**The divisor count:** 12 divisors: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

**What this means for character systems:**

A scale built on 60 subdivides cleanly into halves, thirds, quarters, fifths, sixths, tenths, twelfths, fifteenths, twentieths, and thirtieths. Every derived statistic formula that divides one variable by 2, 3, 4, 5, or 6 produces an exact integer. No rounding. No floor operations. No accumulated precision errors across cascading calculations.

The previous system used base 10 scales (0-10 for sub-variables, 10-base for GURPS attributes). Base 10 has 4 divisors: {1, 2, 5, 10}. Division by 3 on a 0-10 scale produces fractions. The derived stat formula `SOCIAL - (projection_tendency / 3)` required a floor operation. In base 60, that formula produces exact integers for all valid inputs.

Historical precedent: Sumerian and Babylonian mathematics used base 60 for astronomy, timekeeping, and angular measurement. 360 degrees (6 × 60), 60 minutes per hour, 60 seconds per minute. These systems endure because the divisibility properties make complex calculations tractable without approximation.

---

## The Divisor Lattice of 60

The divisor lattice is the partial order of all divisors of 60 by the divisibility relation. If a divides b, then a sits below b in the lattice.

```
                            60
                         /  |  \
                       30   20   12
                      / \   |  / | \
                    15  10   4   6
                    |  / \ / \ / |
                    5    2    3
                     \   |   /
                       \ | /
                         1
```

**Reading the lattice:** Every upward path from 1 to 60 is a valid divisor chain. Every node divides all nodes above it that it connects to. The lattice defines all legal relationships between scale classes in the system.

**Key structural properties:**

- **Width at each level:** The lattice has maximum width 4 at the {6, 4, 10, 15} level, meaning up to 4 independent scale classes can coexist at that granularity.
- **Lattice height:** The longest chain from 1 to 60 has length 5 (e.g., 1→2→4→12→60). This defines the maximum nesting depth for hierarchical subdivisions.
- **Meet and join:** Any two divisors have a greatest common divisor (meet) and a least common multiple (join) within the lattice. This guarantees that any two scale classes can be combined through a well-defined operation.

---

## Pattern Catalog: Divisor Chains

A divisor chain is a totally ordered subset of the divisor lattice where each element divides the next. Chains define valid scale hierarchies — nested subdivisions of the 60-unit space where each level of granularity divides cleanly into the next.

### Maximal Chains (1 to 60)

Every maximal chain passes through 1 and 60 and cannot be extended by inserting additional divisors.

|Chain ID|Sequence|Step Ratios|Character System Application|
|---|---|---|---|
|C01|1 → 2 → 4 → 12 → 60|×2, ×2, ×3, ×5|Binary splits within a 12-unit display, nested in 60|
|C02|1 → 2 → 4 → 20 → 60|×2, ×2, ×5, ×3|Binary splits within a 20-unit display, nested in 60|
|C03|1 → 2 → 6 → 12 → 60|×2, ×3, ×2, ×5|Pair → hex → dodecimal → full|
|C04|1 → 2 → 6 → 30 → 60|×2, ×3, ×5, ×2|Pair → hex → 30-unit range → full|
|C05|1 → 2 → 10 → 20 → 60|×2, ×5, ×2, ×3|Pair → decimal → vigesimal → full|
|C06|1 → 2 → 10 → 30 → 60|×2, ×5, ×3, ×2|Pair → decimal → 30-unit range → full|
|C07|1 → 3 → 6 → 12 → 60|×3, ×2, ×2, ×5|Triad → hex → dodecimal → full|
|C08|1 → 3 → 6 → 30 → 60|×3, ×2, ×5, ×2|**Tier chain**: 3 tiers → 6 movements → 30-unit → full|
|C09|1 → 3 → 15 → 30 → 60|×3, ×5, ×2, ×2|Triad → 15 categories (Astrology) → 30-unit → full|
|C10|1 → 5 → 10 → 20 → 60|×5, ×2, ×2, ×3|Pentad → decimal → vigesimal → full|
|C11|1 → 5 → 10 → 30 → 60|×5, ×2, ×3, ×2|Pentad → decimal → 30-unit → full|
|C12|1 → 5 → 15 → 30 → 60|×5, ×3, ×2, ×2|Pentad → 15 categories → 30-unit → full|
|C13|1 → 2 → 4 → 20 → 60|×2, ×2, ×5, ×3|Binary subdivisions of vigesimal|
|C14|1 → 3 → 12 → 60|×3, ×4, ×5|**Layer chain**: 3 tiers → 12 layers → 60|
|C15|1 → 4 → 12 → 60|×4, ×3, ×5|Quad → dodecimal → full|
|C16|1 → 5 → 20 → 60|×5, ×4, ×3|Pentad → vigesimal → full|
|C17|1 → 6 → 12 → 60|×6, ×2, ×5|**Movement chain**: 6 movements → 12 layers → full|
|C18|1 → 6 → 30 → 60|×6, ×5, ×2|6 movements → 30-unit range → full|

### Architecturally Significant Chains

**C14 (1 → 3 → 12 → 60):** The Layer Chain. 3 tiers nest into 12 layers nest into the 60-unit numerical space. This chain is the structural spine of the character system. It confirms that the 3-tier / 12-layer architecture is native to base 60.

**C08 (1 → 3 → 6 → 30 → 60):** The Tier-Movement Chain. 3 tiers → 6 movements → 30-unit attribute range → 60-unit internal space. Links the tier structure to the lifecycle structure to the numeric system.

**C09 (1 → 3 → 15 → 30 → 60):** The Astrology Chain. 3 tiers → 15 Character Astrology categories → 30-unit range → 60-unit space. Links the tier structure to the astrology framework to the numeric system.

**C17 (1 → 6 → 12 → 60):** The Movement-Layer Chain. 6 movements → 12 layers → 60. Links the lifecycle protocol to the layer structure to the numeric system.

---

## Pattern Catalog: Matrix Decompositions

A matrix decomposition of 60 is a factorization into two dimensions: 60 = rows × columns. Each decomposition defines a valid 2D data structure within the 60-unit space.

|Decomposition|Rows × Cols|System Mapping|
|---|---|---|
|60 = 2 × 30|2 × 30|Binary state (active/inactive) across a 30-unit scale|
|60 = 3 × 20|3 × 20|**3 tiers × 20-unit attribute scale**|
|60 = 4 × 15|4 × 15|4 throughlines × 15 astrology categories|
|60 = 5 × 12|5 × 12|**5 inner planets × 12 layers**|
|60 = 6 × 10|6 × 10|**6 movements × 10 outer variables per movement**|
|60 = 10 × 6|10 × 6|10 planets × 6 aspect types|
|60 = 12 × 5|12 × 5|**12 layers × 5 core variables per layer**|
|60 = 15 × 4|15 × 4|15 astrology categories × 4 element types|
|60 = 20 × 3|20 × 3|20-unit scale × 3 tier classes|
|60 = 30 × 2|30 × 2|30-unit scale × binary (static/dynamic)|

### Architecturally Significant Matrices

**3 × 20:** The Tier-Attribute Matrix. 3 tiers of characters, each scored on a 0-20 display scale. This is the primary attribute matrix for L1-L3.

**5 × 12:** The Planet-Layer Matrix. 5 inner planets mapped against 12 character layers. Defines which planets feed which layers (the feed map from deliverable 3A expressed as a matrix).

**12 × 5:** The Layer-Variable Matrix. 12 layers, each carrying up to 5 core variables. This provides a structural budget: no layer should define more than 5 primary variables without justification for exceeding the matrix constraint.

---

## Pattern Catalog: Tensor Decompositions

A tensor decomposition of 60 factors into three or more dimensions. These define multi-axis data structures.

|Decomposition|Dimensions|System Mapping|
|---|---|---|
|60 = 2 × 2 × 15|2 × 2 × 15|Binary × binary × 15 astrology categories|
|60 = 2 × 2 × 3 × 5|2 × 2 × 3 × 5|Full prime factorization: max dimensional decomposition|
|60 = 2 × 3 × 10|2 × 3 × 10|Static/dynamic × 3 tiers × 10-unit sub-scale|
|60 = 2 × 5 × 6|2 × 5 × 6|Binary × 5 planets × 6 movements|
|60 = 2 × 6 × 5|2 × 6 × 5|Static/dynamic × 6 movements × 5 variables|
|60 = 3 × 4 × 5|3 × 4 × 5|**3 tiers × 4 throughlines × 5 variables**|
|60 = 3 × 2 × 10|3 × 2 × 10|3 tiers × binary × 10-unit scale|
|60 = 4 × 3 × 5|4 × 3 × 5|4 signposts × 3 tiers × 5 variables|
|60 = 5 × 4 × 3|5 × 4 × 3|5 planets × 4 aspect types × 3 tiers|
|60 = 6 × 2 × 5|6 × 2 × 5|6 movements × binary × 5 state variables|

### Architecturally Significant Tensors

**3 × 4 × 5:** The Tier-Throughline-Variable Tensor. 3 character tiers × 4 Dramatica throughlines × 5 variables per intersection. A complete mapping of which variables exist at each tier-throughline intersection. 60 cells total, one per conceptual "slot" in the system.

**2 × 5 × 6:** The State-Planet-Movement Tensor. Static/dynamic flag × 5 inner planets × 6 movements. Tracks which planetary variables are static versus dynamically modified across the lifecycle. 60 cells.

---

## Scale Classes

A scale class is a valid numeric range derived from the divisor lattice. Every variable in the system is assigned to exactly one scale class. The scale class defines the variable's display range, internal range, step size, and divisibility properties.

**Notation:** SC-N means a scale class with N+1 valid values (0 through N), where N is a divisor of 60.

|Scale Class|Display Range|Internal Range|Step (internal)|Valid Display Values|Divisible By|
|---|---|---|---|---|---|
|**SC-4**|0–4|0–60|15|{0, 1, 2, 3, 4}|1, 2, 4|
|**SC-5**|0–5|0–60|12|{0, 1, 2, 3, 4, 5}|1, 5|
|**SC-6**|0–6|0–60|10|{0, 1, 2, 3, 4, 5, 6}|1, 2, 3, 6|
|**SC-10**|0–10|0–60|6|{0, 1, 2, ..., 10}|1, 2, 5, 10|
|**SC-12**|0–12|0–60|5|{0, 1, 2, ..., 12}|1, 2, 3, 4, 6, 12|
|**SC-15**|0–15|0–60|4|{0, 1, 2, ..., 15}|1, 3, 5, 15|
|**SC-20**|0–20|0–60|3|{0, 1, 2, ..., 20}|1, 2, 4, 5, 10, 20|
|**SC-30**|0–30|0–60|2|{0, 1, 2, ..., 30}|1, 2, 3, 5, 6, 10, 15, 30|
|**SC-60**|0–60|0–60|1|{0, 1, 2, ..., 60}|1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60|

### Scale Class Selection Rules

When assigning a scale class to a variable, apply these rules in order:

**Rule 1:** The scale class must be a divisor of 60. No exceptions.

**Rule 2:** The scale class must provide enough granularity to express meaningful character differentiation. If two characters who should feel different would receive the same value on a given scale, the scale is too coarse.

**Rule 3:** The scale class must be compatible with every formula that consumes the variable. If a formula divides the variable by N, then N must be in the variable's "Divisible By" set. If it is not, either change the scale class or redesign the formula.

**Rule 4:** Prefer SC-12 as the default scale class. 12 is the most versatile divisor of 60 — it divides by 1, 2, 3, 4, 6, and 12. It provides sufficient granularity for most character variables. It is the number of layers in the system. When in doubt, use SC-12.

**Rule 5:** Use SC-20 for primary attributes (L1-L3) where the GURPS legacy requires broader range and where the human default (average person) sits at the midpoint.

---

## Scale Assignment Table

This table assigns every numeric variable in the character system to a scale class. It replaces all previous implicit range definitions.

### Tier 1: Primary Attributes

|Variable|Old Range|New Scale Class|Display Range|Default|Internal Step|Justification|
|---|---|---|---|---|---|---|
|L1 CORE|~6-20|**SC-20**|0–20|10|3|GURPS IQ-equivalent. Broad range needed for cognitive differentiation. Default 10 = human average. SC-20 divides by 2, 4, 5, 10 — covers all current formula needs.|
|L2 VITAL|~6-20|**SC-20**|0–20|10|3|GURPS DX-equivalent. Same logic as CORE.|
|L3 SOCIAL|~6-20|**SC-20**|0–20|10|3|GURPS HT-equivalent. Same logic.|

### Tier 2: Secondary Attributes

|Variable|Old Range|New Scale Class|Display Range|Default|Derivation|Justification|
|---|---|---|---|---|---|---|
|L4 WILL|~6-20|**SC-20**|0–20|=CORE|WILL = CORE, buyable ±1-3|Must match CORE scale for derivation.|
|L5 WOUND|0-10|**SC-12**|0–12|0|Assigned from history|SC-12 provides 20% more granularity than old SC-10. Division by 2, 3, 4, 6 all exact. Critical for Stress Threshold and Collapse Risk formulas.|
|L6 DRIVE|~6-20|**SC-20**|0–20|=VITAL|DRIVE = VITAL, buyable|Must match VITAL scale for derivation.|

### Tier 3: Sub-Variables (All Layers)

|Variable Category|Old Range|New Scale Class|Display Range|Justification|
|---|---|---|---|---|
|Attachment scores|0-10|**SC-12**|0–12|SC-12 default for sub-variables|
|Emotional range|0-10|**SC-12**|0–12|SC-12 default|
|Flexibility scores|0-10|**SC-12**|0–12|SC-12 default|
|Stability scores|0-10|**SC-12**|0–12|SC-12 default|
|Density scores|0-10|**SC-12**|0–12|SC-12 default|
|Tendency scores|0-10|**SC-12**|0–12|SC-12 default|
|Index scores (shame, desire)|0-10|**SC-12**|0–12|SC-12 default|
|Resistance index|0-10|**SC-12**|0–12|SC-12 default|
|Origin seeds|0-10|**SC-12**|0–12|SC-12 default|
|Coherence scores|0-10|**SC-12**|0–12|SC-12 default|
|Tech level|0-10|**SC-12**|0–12|SC-12 default|

### Dualism Charges (Layer-Locked Module)

|Variable|Old Range|New Scale Class|Display Range|Justification|
|---|---|---|---|---|
|Dualism charge|-30 to +30|**SC-60 (signed)**|-30 to +30|Already base-60 native. 60-unit range centered on 0. No change needed.|
|Snap boundaries|±60|**SC-60 (extended)**|-60 to +60|120-unit total range = 2 × 60. Native.|

### Point Budget Values

|Variable|Old Cost|New Scale Class|New Cost|Justification|
|---|---|---|---|---|
|CORE per level above default|20 pts|**SC-20**|**20 pts**|20 is a divisor of 60. No change needed.|
|VITAL per level above default|20 pts|**SC-20**|**20 pts**|Same.|
|SOCIAL per level above default|10 pts|**SC-20**|**10 pts**|10 is a divisor of 60. No change.|
|WILL buy-up/down per level|5 pts|**SC-20**|**5 pts**|5 is a divisor of 60. No change.|
|DRIVE buy-up/down per level|3 pts|**SC-20**|**3 pts**|3 is a divisor of 60. No change.|

**Finding:** All existing GURPS-derived point costs are already divisors of 60. No recalibration of cost-per-level is required. The point budget system is base-60 native as designed.

### Tier Budget Totals

Tier budgets recalibrate because WOUND shifted from SC-10 to SC-12, which changes the weight of Tier 3 variable assignments.

|Tier|Old Budget|New Budget|Justification|
|---|---|---|---|
|Tier 1 (L1-L3)|~75 pts|**~75 pts**|Primary attribute costs unchanged. Budget stable.|
|Tier 2 (L4-L6)|~140 pts|**~140 pts**|WILL/DRIVE costs unchanged. WOUND is assigned not bought — does not consume budget. Budget stable.|
|Tier 3 (L7-L12)|Uncapped|**Uncapped**|Sub-variables are not point-purchased. They are assigned from documentation. No budget change.|

**Finding:** Tier budgets require no recalibration. The shift from SC-10 to SC-12 for sub-variables affects the granularity of assigned values, not their point cost (Tier 3 sub-variables are not purchased from a point budget — they are assigned from canonical documentation).

---

## Point Budget Recalibration

### Summary: No Structural Changes Required

The point budget system is already base-60 compatible:

- All per-level costs (20, 10, 5, 3) are divisors of 60
- Primary attribute scale (SC-20) retains the same default (10) and the same cost structure
- Tier budget totals are unchanged

The only change is the **display convention** for documentation: all point costs and budget calculations should explicitly note their position in the divisor lattice.

**Example documentation format:**

```
L1 CORE: 13 (SC-20, display)
  Internal: 39 (13 × 3, on 0-60 scale)
  Cost: 3 levels above default × 20 pts/level = 60 pts
  Budget note: 60 pts = 1 × 60 (one full base unit consumed)
```

The fact that Victoria's CORE cost is exactly 60 points — one full base unit — is not a coincidence in the recalibrated system. It is the system expressing itself.

---

## Derived Statistic Recalibration

All derived statistics are reformulated to operate on the new scale classes. The critical requirement: every formula produces exact integers for all valid inputs.

### Cross-Scale Formula Handling

When a formula combines variables from different scale classes, the operation is performed in internal (0-60) space, then the result is assigned to its own scale class.

**Conversion to internal:** `internal = display × step` **Conversion to display:** `display = internal / step`

For SC-20 variables: step = 3. Display 13 → internal 39. For SC-12 variables: step = 5. Display 8 → internal 40.

### Recalibrated Formulas

**Basic Damage Resistance**

- Old: `WILL - (WOUND / 2)` (floor operation required)
- New: `(WILL_internal - (WOUND_internal / 2)) / result_step`
- Internal: `(WILL × 3) - ((WOUND × 5) / 2)`
- For WOUND on SC-12, WOUND × 5 is always a multiple of 5. Divided by 2 requires WOUND × 5 to be even. Since 5 is odd, WOUND must be even for exact division.
- **Resolution:** Redefine Basic Damage Resistance to operate in internal space and output on SC-20:

```
BDR_internal = WILL_internal - WOUND_internal_half
             = (WILL_display × 3) - ((WOUND_display × 5) / 2)

Output scale: SC-20 (display = BDR_internal / 3)
```

- **Divisibility constraint on WOUND for BDR:** WOUND_display × 5 must be divisible by 2. This is satisfied when WOUND_display is even (0, 2, 4, 6, 8, 10, 12). When WOUND_display is odd, the raw internal result is non-integer.
- **Design decision:** Constrain WOUND to **even values only** on SC-12 (effective grid: {0, 2, 4, 6, 8, 10, 12} = 7 valid values, step = 10 internal). OR redesign the formula.
- **Recommended formula redesign:**

```
Basic Damage Resistance = WILL - (WOUND × 5 / 6)
```

In internal space: `BDR = (WILL × 3) - (WOUND × 5 × 5 / 6)`... this gets worse.

**Cleaner approach — redesign all formulas to avoid cross-scale division:**

```
Basic Damage Resistance = WILL_display - WOUND_adj
  where WOUND_adj = (WOUND_display × 5) / 3, rounded to SC-20
```

This still requires WOUND × 5 to be divisible by 3, which only works for WOUND = {0, 3, 6, 9, 12}...

**Cleanest approach — unify the formula scale:**

All derived statistics operate on a single output scale class. Variables are normalized to that scale before the formula executes.

**Selected output scale: SC-12.** (Maximally divisible among practical display ranges.)

**Normalization rules:**

|Source Scale|To SC-12|Formula|
|---|---|---|
|SC-20 variable|Normalize to SC-12|`SC12_value = (SC20_value × 3) / 5`|
|SC-12 variable|No change|identity|

For SC-20 → SC-12 conversion to produce integers: SC20_value × 3 must be divisible by 5. This requires SC20_value to be a multiple of 5 (0, 5, 10, 15, 20 on display scale). That is too restrictive.

**Final approach — accept that derived statistics operate in internal (SC-60) space and display on a dedicated scale:**

```
All derived statistics are computed in internal (0-60) space.
All derived statistics display on SC-12 (divide internal result by 5).
All input variables are converted to internal before computation.
```

**Recalibrated derived stat formulas (all in internal space):**

|Derived Stat|Formula (Internal)|Output Display|Division Safety|
|---|---|---|---|
|**Basic Damage Resistance**|`WILL_i - (WOUND_i / 2)`|SC-30|WOUND_i = WOUND_d × 5. /2 requires result divisible by 2. WOUND_d × 5 / 2 is integer when WOUND_d is even. **Constraint: WOUND assigned in even increments (0, 2, 4, 6, 8, 10, 12).**|
|**Social Legibility**|`SOCIAL_i - (projection_i / 3)`|SC-20|projection_i = proj_d × 5. /3 requires result divisible by 3. proj_d × 5 / 3 is integer when proj_d is a multiple of 3 (0, 3, 6, 9, 12). **Constraint: projection_tendency assigned in multiples of 3.**|
|**Narrative Momentum**|`DRIVE_i + (resistance_i / 2)`|SC-30|resistance_i = res_d × 5. /2 same constraint as BDR. **Constraint: resistance_index assigned in even increments.**|
|**Stress Threshold**|`WILL_i - WOUND_i`|SC-60 (no division)|No division. Always exact. No constraint.|
|**Collapse Risk**|`(WOUND_i + shadow_density_i) / 2`|SC-30|Both are ×5 internal. Sum of two ×5 values is always ×5, but /2 requires the sum to be even. Two ×5 values sum to ×5 which is odd when one is odd×5 and other is even×5. **Constraint: WOUND + shadow_density must be even (both even or both odd on display scale).**|
|**Truth Exposure Index**|`SOCIAL_i + (12 - shame_index_d) × 5`|SC-60 (no division)|No division. Expression `12 - shame_d` replaces old `10 - shame_d` due to SC-12 scale shift. Always exact.|

### Derived Stat Divisibility Constraints Summary

The formulas impose constraints on which display values certain variables can take. These constraints are not limitations — they are the base 60 system enforcing clean mathematics.

|Variable|Constraint|Valid Display Values (SC-12)|Number of Valid Values|
|---|---|---|---|
|WOUND|Even only|{0, 2, 4, 6, 8, 10, 12}|7|
|projection_tendency|Multiples of 3 only|{0, 3, 6, 9, 12}|5|
|resistance_index|Even only|{0, 2, 4, 6, 8, 10, 12}|7|
|shadow_density|Parity must match WOUND|If WOUND is even, shadow_density is even; if odd, odd. Since WOUND is constrained to even: **shadow_density = even**|7|

All other SC-12 variables have no divisibility constraint and may use any value 0-12.

All SC-20 variables (CORE, VITAL, SOCIAL, WILL, DRIVE) have no divisibility constraint and may use any value 0-20.

---

## Flag Trigger Threshold Recalibration

All flag trigger conditions are re-expressed using the new scale classes. The logic is unchanged — only the threshold values adjust to the new scales.

### SHADOW_DENIAL

Old: `WOUND > 6 AND SHADOW.projection_tendency >= 5 AND IMPRINT.conditional_patterns contains "merit_earns_freedom"`

New: `WOUND > 6 AND SHADOW.projection_tendency >= 6 AND IMPRINT.conditional_patterns contains "merit_earns_freedom"`

**Adjustment:** projection_tendency is now SC-12 constrained to multiples of 3. Old threshold 5 (SC-10) maps proportionally to 6 (SC-12). 5/10 = 50% → 6/12 = 50%. Preserves the same proportional threshold.

### TRUTH_VULNERABILITY

Old: `SOCIAL < 12 AND FUNCTION.motivation_element = "Equity" AND SHADOW.shadow_density > 6`

New: `SOCIAL < 12 AND FUNCTION.mc_problem_element = "Equity" AND SHADOW.shadow_density > 6`

**Adjustment:** SOCIAL is SC-20 (unchanged range, threshold 12 is valid). shadow_density SC-12, old threshold 6 (SC-10) → new threshold 6 is valid on SC-12 (6/12 = 50%, old was 6/10 = 60%). For strict proportional equivalence, use 8 (8/12 = 67% ≈ 60%). **Decision: use 6 on SC-12.** This slightly lowers the trigger threshold, which is narratively appropriate — Truth Vulnerability should fire more easily, not less.

Also incorporates the schema clarification from Phase 4: `motivation_element` → `mc_problem_element`.

### OPTIONLOCK_PROGRESSION

Old: `WOUND > 7 AND DESTINY.resistance_index > 7 AND FUNCTION.limit_type = "Optionlock"`

New: `WOUND > 8 AND DESTINY.resistance_index > 8 AND FUNCTION.limit_type = "Optionlock"`

**Adjustment:** WOUND SC-12 even-constrained: old 7 (SC-10, 70%) → new 8 (SC-12, 67%). Next valid even value above proportional equivalent. resistance_index SC-12 even-constrained: same logic, 8.

### EARNED_JUDGEMENT

Old: `FUNCTION.dramatica_archetype = "Protagonist" AND FUNCTION.story_outcome = "Failure" AND WILL > 10`

New: `FUNCTION.dramatica_archetype = "Protagonist" AND FUNCTION.story_outcome = "Failure" AND WILL > 10`

**Adjustment:** None. WILL is SC-20, threshold 10 is the default/midpoint. No change needed.

### KINSHIP_COLLAPSE

Old: `IMPRINT.attachment_style_score > 5 AND primary_attachment_object = "deceased" AND WOUND > 7`

New: `IMPRINT.attachment_style_score > 6 AND primary_attachment_object = "deceased" AND WOUND > 8`

**Adjustment:** attachment_style_score SC-12: old 5 (SC-10, 50%) → new 6 (SC-12, 50%). WOUND: same as OPTIONLOCK, 8.

---

## Victoria Midnight Re-Expression

Victoria's complete numeric profile recalibrated to the base 60 system.

### Tier 1

|Variable|Old Value (SC-10/20)|New Value|Scale Class|Internal (0-60)|Cost|
|---|---|---|---|---|---|
|CORE|13|**13**|SC-20|39|60 pts (3 levels × 20)|
|VITAL|14|**14**|SC-20|42|80 pts (4 levels × 20)|
|SOCIAL|10|**10**|SC-20|30|0 pts (default)|

**Tier 1 Total: 140 pts** (unchanged)

### Tier 2

|Variable|Old Value|New Value|Scale Class|Internal|Notes|
|---|---|---|---|---|---|
|WILL|14|**14**|SC-20|42|CORE + 1. Buy-up 5 pts.|
|WOUND|8 (SC-10)|**10** (SC-12)|SC-12|50|8/10 = 80% → 10/12 = 83%. Nearest even value preserving narrative severity. She is at 83% wound capacity. Story requires protagonist load-bearing; 12/12 = collapse. 10 maintains function with minimal margin.|
|DRIVE|12|**12**|SC-20|36|VITAL - 2. Meaning-driven. Buy-down returns 6 pts.|

### Tier 3 Sub-Variables

|Layer|Variable|Old (SC-10)|New (SC-12)|Constraint|Justification|
|---|---|---|---|---|---|
|L7|origin_stability|4|**4**|none|4/10 → 4/12. Lower proportional value. Narratively consistent — salvage economy origin is unstable.|
|L7|family_coherence|7|**8**|none|7/10 = 70% → 8/12 = 67%. Sibling bond is strong for the origin class.|
|L7|origin_wound_seed|6|**7**|none|6/10 = 60% → 7/12 = 58%. Close proportional match.|
|L7|tech_level|6|**7**|none|Same logic as wound_seed.|
|L8|attachment_style_score|6|**7**|none|6/10 → 7/12. Secure-anxious in the upper register.|
|L8|emotional_range|9|**11**|none|9/10 = 90% → 11/12 = 92%. Near-maximum emotional range.|
|L8|imprint_flexibility|3|**4**|none|3/10 = 30% → 4/12 = 33%. Low flexibility. Patterns deeply set.|
|L9|desire_vector|3|**4**|none|3/10 → 4/12.|
|L9|shame_index|2|**2**|none|2/10 = 20% → 2/12 = 17%. Low shame. Venus trine Mars.|
|L10|shadow_density|7|**8**|even (matches WOUND parity)|7/10 = 70% → 8/12 = 67%. Even value, matches WOUND even constraint.|
|L10|projection_tendency|6|**6**|multiples of 3|6/10 = 60% → 6/12 = 50%. Valid multiple of 3.|
|L11|resistance_index|8|**8**|even|8/10 = 80% → 8/12 = 67%. Even value. Constitutionally opposed to her own solution.|

### Recalibrated Derived Statistics

All computed in internal (0-60) space, then displayed.

|Stat|Formula (Internal)|Computation|Internal Result|Display (Scale)|
|---|---|---|---|---|
|Basic Damage Resistance|WILL_i - (WOUND_i / 2)|42 - (50 / 2) = 42 - 25|**17**|17/60 (SC-60)|
|Social Legibility|SOCIAL_i - (proj_i / 3)|30 - (30 / 3) = 30 - 10|**20**|20/60 (SC-60)|
|Narrative Momentum|DRIVE_i + (resist_i / 2)|36 + (40 / 2) = 36 + 20|**56**|56/60 (SC-60)|
|Stress Threshold|WILL_i - WOUND_i|42 - 50|**-8**|-8/60 (SC-60)|
|Collapse Risk|(WOUND_i + shadow_i) / 2|(50 + 40) / 2 = 90 / 2|**45**|45/60 (SC-60)|
|Truth Exposure Index|SOCIAL_i + (12 - shame_d) × 5|30 + (12 - 2) × 5 = 30 + 50|**80**|80 (SC-60, uncapped)|

**Key observations from recalibration:**

**Stress Threshold is now NEGATIVE (-8).** In the old system, Stress Threshold = WILL - WOUND = 14 - 8 = 6 (positive). In the new system, WILL_internal = 42, WOUND_internal = 50. The wound exceeds the will in internal space. This is not an error — it is the base 60 system revealing something the old system obscured. Victoria's wound (50) exceeds her will (42) in raw internal magnitude. The old system masked this because WILL and WOUND were on different scales (SC-20 vs SC-10). On a unified internal scale, the wound is heavier than the will. A negative Stress Threshold means she is operating past her structural limit — she functions because WILL provides qualitative resistance (stubbornness, resolve type) that the raw number does not capture. The negative value is diagnostically significant.

**Truth Exposure Index exceeds 60.** TEI = 80 on the internal scale. This means her signal legibility exceeds the maximum of the base unit. In the old system, TEI = 18 on an uncapped scale. The new value (80) is consistent — she is maximally legible and the number says so. TEI is an uncapped diagnostic, not a bounded scale. Values exceeding 60 are valid and indicate extreme exposure.

**Narrative Momentum is near-maximum (56/60).** This confirms the chart analysis — Mars exaltation + Jupiter domicile produce extreme forward energy. She is driven almost to the ceiling of the system's capacity.

---

## Design Rules for Future Variables

When any new variable is added to the system (including Layer-Locked Module sub-tables, plugin extensions, or new layer variables):

**Rule 1:** The variable must be assigned to a scale class from this document. No ad hoc ranges.

**Rule 2:** If the variable participates in a derived formula, the formula must be validated against the divisibility constraints in this document. If the formula introduces a new division operation, the constraint table must be updated.

**Rule 3:** If the variable has no formula dependency, prefer SC-12 as the default. SC-12 is the maximally divisible practical scale.

**Rule 4:** Point costs for any buyable variable must be a divisor of 60.

**Rule 5:** Flag trigger thresholds must use values valid on the variable's scale class, respecting any divisibility constraints.

**Rule 6:** Document the variable's position in the divisor lattice chain. Example: a SC-12 variable with an even-only constraint lives on the sub-chain {0, 2, 4, 6, 8, 10, 12}, which maps to internal {0, 10, 20, 30, 40, 50, 60} — this is the SC-6 grid promoted to SC-12 notation. Name the effective grid.

**Rule 7:** When converting old SC-10 values to SC-12, use proportional mapping rounded to the nearest valid value on the target scale class. Document the rounding direction and narrative justification.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-08|Initial SSOT. Establishes base 60 as foundational number system. Divisor lattice, 18 maximal chains, 10 matrix decompositions, 10 tensor decompositions, 9 scale classes, complete scale assignment table, point budget validation (no changes required), derived stat recalibration with divisibility constraints, flag threshold recalibration, Victoria Midnight full re-expression with diagnostic analysis.|