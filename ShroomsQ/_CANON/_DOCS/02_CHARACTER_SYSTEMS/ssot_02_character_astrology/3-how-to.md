---
title: "Character astrology: how-to"
type: how-to
for: "A writer building or checking a character's chart who already knows what the system is"
does: "Gives numbered steps for each task the Character Astrology doc defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_astrology.md
source_version: 1.1.1
---

**Who it's for:** a writer building or checking a chart · **What it does:** numbered steps for each chart task · **Type:** how-to

# Character astrology: how-to

Lookup tables: [reference](2-reference.md). Why the rules exist: [concept](1-concept.md). Sign-by-sign translation tables live in the [DAI doc](../ssot_02_character_astrology_dai/2-reference.md). The blank form is the [astrology ingest template](../ssot_02_template_astrology_ingest/3-how-to.md).

> **OPEN:** the source gives the rules for each task but not the sign choice. The DAI doc owns the sign tables. These steps stop where the source stops.

## Decide how deep a character's chart goes

1. Find the character's tier.
2. For Tier 3, plan a full chart.
3. For Tier 2, plan a partial chart: Sun, Moon and one or two defining aspects, from the element signature.
4. For Tier 1, write no chart.
5. For a partial chart that must still feed L1-L11, assign the seven core placements. The seven are Sun, Moon, Mercury, Venus, Mars, Saturn, Ascendant.
6. Leave Jupiter, Uranus, Neptune, Pluto, progressions and transits for later.

## Assign a planet or angle

1. Open the locked Dramatica ingest. Do not start without one.
2. Follow the derivation order in the DAI doc. Skip no step and reorder none.
3. Find the planet's Dramatica inputs in the [reference](2-reference.md). Use Category 3 for inner planets, 4 for outer planets and 5 for angles.
4. Write the sign. Write the Dramatica input and the rule that justified it.
5. If the source for a planet is missing, leave it empty and mark it. Never guess.

## Resolve a conflict between astrology and Dramatica

1. Compare the astrological suggestion with the locked Dramatica data.
2. If they disagree, keep the Dramatica data.
3. Revise the astrological assignment.
4. Do not edit the storyform to fit the chart.

## Assign an aspect between two planets

1. Name the two Dramatica elements behind the two planets.
2. Ask whether the elements are in natural tension, such as Equity and Inequity as Problem and Solution.
3. If they are, give a hard aspect: Square or Opposition.
4. If they flow within the same quad, give a soft aspect: Trine or Sextile.
5. Use a Conjunction only when the two Dramatica functions fuse in this character.
6. Record the gate: Conjunction is AND, Square is NOT, Opposition is XOR, Trine is OR, Sextile is OR.

## Assign a house

1. Read the MC Domain.
2. Situation: weight the planets toward houses 1, 4, 7, 10.
3. Activity: spread them across angular and succedent houses.
4. Fixed Attitude: weight them toward cadent and succedent houses.
5. Psychology: spread them across all three house types.
6. Write a justification for each placement.

## Assign a dignity or a debility

1. Take the Dramatica element on the planet.
2. Compare it with the natural mode of the planet's sign.
3. If they align, mark Essential Dignity.
4. If they conflict, mark Essential Debility.
5. For a debility, write the behavioral texture, not a flaw.
6. Send that texture to L10 SHADOW and L5 WOUND.

## Place a planet in the 12th House

1. List the Dramatica functions the character carries but cannot access directly.
2. Check the MC Problem. If the character does not see it until late in the arc, it is a strong candidate.
3. Place the planet in the 12th House, or give it an aspect to a 12th House planet.
4. Check Mercury. An aspect from Mercury to a 12th House planet produces the Hauntology Effect.

## Sort a category or datum as character-level or story-level

1. Ask: does it say who the character IS at canonical definition?
2. If yes, it is character-level. It goes in the static chart and the ingest template.
3. If it says what is HAPPENING at one narrative moment, it is story-level.
4. Route story-level data in three ways. Send network and synastry to relationship tables. Send progressions and transits to the state overlay system. Send movements and reset to plot systems.
5. Never edit the natal chart for story-level data.

## Connect a finished chart to the 12 layers

1. Confirm the character has a locked Dramatica ingest and a chart.
2. Open the 12-layer mapping doc.
3. Feed each layer from the planets the source names. Sun feeds L1, Mars feeds L2, and Saturn feeds L4 and L5. Moon feeds L8, Venus feeds L9, shadow aspects feed L10, and growth axis feeds L11.
4. Leave the schema 2.5.0 and 3.0.0 fields unfed. Set them from the authoritative document.
5. Keep both the chart and the 12-layer slice in the character's canonical folder.
