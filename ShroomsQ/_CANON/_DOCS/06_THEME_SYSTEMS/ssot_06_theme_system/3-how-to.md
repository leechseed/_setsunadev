---
title: "The theme system: how-to"
type: how-to
for: "A writer building or checking a story's theme with the four-part method"
does: "Gives numbered steps for each task the theme system defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/06_THEME_SYSTEMS/📐 ssot_06_theme_system.md
source_version: 1.4.1
---

**Who it's for:** a writer who already knows what theme is · **What it does:** step-by-step recipes for the theme system's tasks · **Type:** how-to

# The theme system: how-to

Look up terms in the [reference](2-reference.md). Read the [concept](1-concept.md) for the why.

## Write a controlling idea

1. Read genre G4 `core_binary` as the seed for your first candidate.
2. Draft candidate sentences in the form *[value] happens because [cause]*.
3. Cut the story down to one sentence. Keep going until exactly one candidate survives.
4. Write the mechanism line. Answer "how does the system pull this off, concretely."
5. Test it: rebuild the story's whole shape from the sentence alone.
6. Check that the mechanism line explains the how without repeating the what.
7. Ask "what might this sentence be covering?" Record the answer as the latent-theme line.
8. Point the spine's L6 theme at the sentence.
9. Set `ct11_verdict` on each 05 catalog entry: `argues`, `neutral` or `undercuts`. Rewrite or mark as the exception any entry that undercuts.

## Build the rails

1. Take the storyform's locked Issue and Counterpoint pair for each throughline: world, protagonist, foil, relationship.
2. Phrase each pair as a question a character could ask out loud.
3. Keep 3 to 5 debates.
4. Name one outside idea each debate meets, and write it in the `meets` field.
5. Check that scenes argue each side of every debate, not only the winning side.
6. Check that the set of debates sums back to the controlling idea.
7. Fill `holders:` on each rail with the 08 track ids that carry it, such as `character:tori`.

## Build a value scale

1. Name the value the controlling idea turns on.
2. Write plain words for four steps, best to worst: positive, contrary, contradictory, negation of the negation.
3. Read the four as a ladder. Rewrite any step that reads as an unrelated mood.
4. Add a second gauge only if one point of view runs on a different value. Give it the same four steps.
5. Test it: every scene's value-in and value-out on the plot card names one step.

## Choose and check motifs

1. Pick 2 to 4 images already present in the setting or character material.
2. Tie each image to one rail or one scale step.
3. Check that each appearance advances or reverses that tie.
4. Run the two motif checks: the image recurs, and its uses converge on one meaning.
5. Hand a reader the story without the theme sentence. Confirm they can point at the pattern.
6. Drop any motif that ties to no rail and no step.
7. Mint the motif's id as `motif.<slug>`.
8. Set `motif_ref` to the catalog id of the setting object behind the motif, such as WB-TEC-0001 for the Feed. Leave it empty when no entry exists.

## Add a civilization gauge

1. Pick the civilization's value. Use the four steps: positive, contrary, contradictory, negation of the negation.
2. Write the last step as the lie the civilization tells about itself.
3. Put the four steps in the `gauge:` field of the civilization's catalog entry in 05. The rule stays in the theme doc.
4. Tag world scenes set in that civilization to read its gauge beside Fairness.

## Run the scene tests on a scene card

1. Fill the theme record on the scene card or the plot card: `rail_tested`, `side_argued` and `gauge` (name plus step).
2. Fill the citation test. Name the rule every actor followed in a harm scene. Write it in the scene plan, not in the narration.
3. If a scene needs a hidden evil motive, rewrite it or mark it as the exception.
4. Fill the knowledge gradient. Name who in the scene knows better.
5. Check the hard case: a character who knows better and complies. Let the scene feel it.
6. Fill the two-transcripts field. Say whether the scene plays on the public script or the hidden transcript.
7. State what changes between the two.
8. Read the rider: the idea describes what the system allows, never what a person is.
9. Show the rule in speech or action when the scene is written. 07.1 forbids narration that states it.

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
