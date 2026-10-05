---
title: "Character astrology: concept"
type: concept
for: "A writer or builder who needs to know why the character system carries an astrological chart at all"
does: "Explains why Character Astrology exists, what it refuses to do, and how it sits between Dramatica and the 12 layers"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_astrology.md
source_version: 1.1.1
---

**Who it's for:** a writer or builder asking why the character system carries a chart · **What it does:** explains why Character Astrology exists and where it stops · **Type:** concept

# Character astrology: concept

Pages in this set: [reference](2-reference.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md). The source is [ssot_02_character_astrology.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_character_astrology.md).

## A chart is a second notation for a character Dramatica already settled

Dramatica fixes the narrative truth of a character. Character Astrology writes that same truth in a second vocabulary: planets, signs, houses, aspects and dignities. The result is a **chart**. The chart is not a horoscope. It adds no new fact about the character. It restates locked facts so that depth, contradiction and texture show up that a single number cannot hold.

The source gives three definitions that carry the rest. The chart is the character's source code. The character is the compiled entity, the behavior that appears when the chart's variables interact. The story is the execution environment, the outside conditions that switch variables on, off or over.

## The story rules the chart, never the reverse

The governing line is short: the chart serves the story, and the story does not serve the chart. Every assignment must trace to a locked Dramatica position. When astrological vocabulary suggests a behavior that Dramatica contradicts, the writer revises the chart and leaves the storyform alone.

This is why the system calls itself deterministic. Traditional astrology interprets. Character Astrology derives. A behavior that cannot be traced back to a variable means the chart is incomplete. It does not mean the character is wrong.

## The system is a translation layer, so it refuses three jobs

Character Astrology produces a symbolic dataset and nothing else. It does not build narrative structure, which is Dramatica's work. It does not assign numbers to character layers, which is the 12-layer system's work. It does not write plot events or timelines, which belong to plot systems.

Those refusals keep the three systems from drifting into each other. Each downstream system consumes the chart. The chart never reaches into them.

## Fifteen categories split by one question: who is the character, or what is happening to them

The source keeps fifteen categories from the older framework. It sorts them with a single test. If the data says who the character is at the point of canonical definition, it is character-level. If the data says what is happening to the character at one narrative moment, it is story-level.

Nine categories pass the first test and form the static chart. Six pass the second and go to relationship tables, state overlays or plot systems. The static record never changes. Progressions and transits layer state diffs on top of it. Synastry writes relationship records that point at two charts. The six movements point at the main character's chart.

## Chart depth follows the tier of the character

Not every character needs a full chart. A Tier 3 character gets full chart generation. A Tier 2 character gets a partial chart: Sun, Moon and one or two defining aspects. A Tier 1 character gets none. A partial chart with the seven core placements is enough to fill layers 1 through 11. The outer planets and the advanced configurations arrive as development continues.

## The chart sits in the middle of a pipeline and feeds the 12 layers

Dramatica data goes in. The Dramatica-Astrology Interface (DAI) translates it. The chart comes out and feeds layers 1 through 11 of the LEECHSEED vertical slice. Layer 12 comes straight from Dramatica, so the chart never touches it.

The chart and the 12 layers are parallel datasets, not a hierarchy. The chart supplies symbolic depth, internal contradiction and a way to detect collisions between two characters. The 12 layers supply numbers, derived statistics and machine-readable blocks. A complete Tier 3 character holds both, and neither replaces the other.

## The long read

The source works hard to keep this system from swallowing its neighbors. Three guards stand out. First, the DAI table lives in one place only, the DAI doc, so the two documents cannot disagree. Second, twelve schema fields added in later passes have no chart feed at all. The authors set them from the authoritative document. Third, the story-level categories are written down here only "for completeness" and "to prevent scope creep into the static character record".

The pattern is consistent. The system defines its edge, names the neighbor that owns what lies beyond it, and stops. A reader who wants the translation rules goes to the DAI doc. A reader who wants the layer feeds goes to the 12-layer mapping doc. A reader who wants a blank form goes to the astrology ingest template.
