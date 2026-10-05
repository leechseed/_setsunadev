---
title: "Base 60 number system: how-to"
type: "how-to"
for: "A designer adding or converting a numeric variable"
does: "Gives the steps for the number tasks the base 60 doc defines"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_base_60_number_system.md"
source_version: "1.0.3"
---

**Who it's for:** a designer adding or converting a numeric variable · **What it does:** gives the steps for each number task · **Type:** how-to

# Base 60 number system: how-to

Tables and rules live in the [reference](2-reference.md).

## Assign a scale class to a new variable

1. Take the class from the Scale Class table. It must divide 60.
2. Check the class gives enough granularity to tell two characters apart.
3. List every formula that consumes the variable.
4. For each division by N, confirm N is in the class's "Divisible by" set. If not, change the class or the formula.
5. If no formula depends on the variable, pick SC-12.
6. Pick SC-20 for a primary attribute (L1-L3).
7. Add the variable to the Scale Assignment Table.

## Set the point cost of a buyable variable

1. Choose a cost that divides 60.
2. Note the cost's lattice position in the documentation.
3. Write the example format: display value, internal value, levels × cost, budget note.

## Add a variable to a derived formula

1. Convert each input to internal space: `internal = display × step`.
2. Compute the formula in internal space.
3. Check every division gives an exact integer.
4. If a division needs a constraint, add a row to the Divisibility Constraints table.
5. Name the output class.

## Convert an old SC-10 value to SC-12

1. Divide the old value by 10.
2. Multiply by 12 and round to the nearest valid value.
3. Apply any constraint on the variable (even only, multiples of 3, parity with WOUND).
4. Write the rounding direction and the narrative reason.

## Re-express a character in base 60

1. Keep Tier 1 values. Convert to internal (CORE 13 is 39).
2. Recompute each cost: levels above default × per-level cost.
3. Re-assign WOUND on SC-12, even values only.
4. Convert each Tier 3 sub-variable to SC-12 with the proportional rule.
5. Compute every derived statistic in internal space.
6. Read the results. A negative Stress Threshold means the wound exceeds the will.

## Set a flag threshold on the new scale

1. Take the old threshold and its percentage of the old scale.
2. Map it to the same percentage on SC-12.
3. Round to the nearest valid value on the target scale. Respect any divisibility constraint.
4. Two valid values may sit equally near, or the nearest may break a constraint. Then ask Chief to pick the direction by narrative need.
5. Record the old and new threshold, the rounding direction and the reason.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [tutorial](4-tutorial.md)
