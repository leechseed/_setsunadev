---
title: "Dramatica integration protocol: concept"
type: concept
for: A narrative designer who needs to know why Dramatica sits first in the character pipeline
does: Explains what Dramatica gives a character, what it never gives, and why the binding is built this way
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮 ssot_02_dramatica_integration_protocol.md
source_version: 1.2.2
---

**Who it's for:** a narrative designer new to the character pipeline · **What it does:** explains why Dramatica comes first and how far its reach goes · **Type:** concept

# Dramatica integration protocol: the idea

## Dramatica supplies the skeleton and nothing else

Dramatica is the narrative structure engine of the Command's character pipeline. It states what the story is about. It assigns each character a mechanical role in that argument. It sets the terms of transformation: resolve, growth, outcome and judgment.

Dramatica does not produce personality, psychology, physicality, sexuality, origin, trauma, shadow or aesthetics. The LEECHSEED Character System and Character Astrology own those. The source puts it in one line: Dramatica produces the narrative skeleton, and the other systems produce the flesh.

Dramatica does not produce plot either. The storyform constrains what the plot must accomplish. The plot_systems domain authors the events, scenes and beats.

## Because the output is deterministic, a revision is a new version

A locked storyform produces a fixed set of character assignments. Those assignments stay put. The only way to change them is to revise the storyform. A revision counts as a new version, never as an edit.

This rule explains the whole cascade. The chart, the L12 block and the state diffs all hang off one storyform version. A new version forces each of them to be re-checked.

## One storyform per story keeps the argument whole

The foundational unit is one storyform per story. One storyform holds one Grand Argument with a beginning, a middle and an end. A single primary storyform is enough for any story.

Nesting is optional. A nested storyform is a complete argument inside a parent. The parent governs when the two conflict.

## The binding record keeps the character singular

A character who holds a Dramatica role gets a binding record. The record ties one `character_id` to one `storyform_id` and names the role. A character in two storyforms gets two records.

The core 12-layer record (L1-L11) stays singular no matter how many bindings exist. The story can ask a character to play different roles. The character's identity does not split.

## Tiers spend Dramatica in proportion to the character's weight

Tier 3 characters get everything: the binding, the full L12 core and the full sub-table. Tier 2 characters get a light fingerprint, an element signature, plus relational role tags. Tier 1 characters get nothing, because they only populate the world.

Tier 2 uses the same element vocabulary as Tier 3. So one query can find every character who carries the same element.

## L12 splits into a working core and a reference table

L12 FUNCTION has two parts (Option C). The core block holds the variables the 12-layer system computes with. The extended sub-table holds the full Dramatica dataset for reference and querying. The sub-table never feeds derived statistics or flags.

This document holds the only copy of both field lists. The main document's L12 row points here.

## Dramatica sits upstream of everything

Dramatica feeds the Dramatica Ingest Template. The template feeds two consumers at once: Character Astrology and the L12 layer. Character Astrology then feeds L1-L11. No Tier 3 character enters the Vertical Slice without a locked Dramatica ingest.

## The long read

The protocol treats a story as a machine with one fixed blueprint. The storyform is the blueprint, and each character is a part cut to fit it. The designer never sands a part to fit a mood. If the part is wrong, the blueprint changes. Then every part downstream is re-checked in order: chart, then L12, then state diffs. The strictness is the point. It lets a writer trust that a character's structural role never drifts between scenes.

See also: [reference](2-reference.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md) · source: [🔮 ssot_02_dramatica_integration_protocol.md](../../../_SSOT/02_CHARACTER_SYSTEMS/🔮%20ssot_02_dramatica_integration_protocol.md)
