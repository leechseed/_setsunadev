---
title: "The theme system: how-to"
type: how-to
for: "A writer building or checking a story's theme with the four-part method"
does: "Gives numbered steps for each task the theme system defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/06_THEME_SYSTEMS/📐 ssot_06_theme_system.md
source_version: 1.3.2
---

**Who it's for:** a writer who already knows what theme is · **What it does:** step-by-step recipes for the theme system's tasks · **Type:** how-to

# The theme system: how-to

Look up terms in the [reference](2-reference.md). Read the [concept](1-concept.md) for the why.

## Write a controlling idea

1. Draft candidate sentences in the form *[value] happens because [cause]*.
2. Cut the story down to one sentence. Keep going until exactly one candidate survives.
3. Write the mechanism line. Answer "how does the system pull this off, concretely."
4. Test it: rebuild the story's whole shape from the sentence alone.
5. Check that the mechanism line explains the how without repeating the what.
6. Ask "what might this sentence be covering?" Record the answer as the latent-theme line.

## Build the rails

1. Take the storyform's locked Issue and Counterpoint pair for each throughline: world, protagonist, foil, relationship.
2. Phrase each pair as a question a character could ask out loud.
3. Keep 3 to 5 debates.
4. Name one outside idea each debate meets, and write it in the `meets` field.
5. Check that scenes argue each side of every debate, not only the winning side.
6. Check that the set of debates sums back to the controlling idea.

## Build a value scale

1. Name the value the controlling idea turns on.
2. Write plain words for four steps, worst to best: positive, contrary, contradictory, negation of the negation.
3. Read the four as a ladder. Rewrite any step that reads as an unrelated mood.
4. Add a second gauge only if one point of view runs on a different value. Give it the same four steps.
5. Test it: every scene's value-in and value-out on the plot card names one step.

> **OPEN:** the source says to write the four steps "worst to best" but lists them best to worst (positive first, the negation of the negation last).

## Choose and check motifs

1. Pick 2 to 4 images already present in the setting or character material.
2. Tie each image to one rail or one scale step.
3. Check that each appearance advances or reverses that tie.
4. Run the two motif checks: the image recurs, and its uses converge on one meaning.
5. Hand a reader the story without the theme sentence. Confirm they can point at the pattern.
6. Drop any motif that ties to no rail and no step.

## Add a civilization gauge

1. Pick the civilization's value. Use the four steps: positive, contrary, contradictory, negation of the negation.
2. Write the last step as the lie the civilization tells about itself.
3. Put the four steps on the civilization's catalog entry in 09. The rule stays in the theme doc.
4. Tag world scenes set in that civilization to read its gauge beside Fairness.

## Run the scene tests on a scene card

1. Fill the citation test. Name the rule every actor followed in a harm scene.
2. If a scene needs a hidden evil motive, rewrite it or mark it as the exception.
3. Fill the knowledge gradient. Name who in the scene knows better.
4. Check the hard case: a character who knows better and complies. Let the scene feel it.
5. Fill the two-transcripts field. Say whether the scene plays on the public script or the hidden transcript.
6. State what changes between the two.
7. Read the rider: the idea describes what the system allows, never what a person is.

## Add a Touchstone to the handshake

1. Take the new live Touchstone from the [Touchstones register](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_touchstones_register.md).
2. Add a row check against every rail, R1 to R4.
3. For each rail, write how the rail may still argue around the Touchstone.
4. Finish all four rows before treating any scene already carded under a rail as bound.

## Key a trope to a rail

1. Open the trope's record in `register.json`. The [trope register](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_trope_register.md) is built from it.
2. Read its one-line `def`.
3. Set `keys.theme` to the one rail, R1 to R4, whose debate the trope argues. Set it to null if the trope argues none.
4. Set `conf` to low when `def` is undefined.
5. Run `build_register.py`.
6. Ask Chief about any trope that needs two rails. Chief decides.

To pull known patterns for a layer, use the theme list in `_tools/tropes/data/domains/LAYERS.md`.
