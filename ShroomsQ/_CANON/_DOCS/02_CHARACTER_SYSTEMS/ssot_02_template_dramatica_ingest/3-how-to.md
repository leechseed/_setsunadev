---
title: "Dramatica ingest template: how-to"
type: how-to
for: "A writer who must produce a locked Dramatica ingest for a Tier 3 character"
does: "Gives numbered steps for each task of filling, generating and locking the form"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_template_dramatica_ingest.md
source_version: 1.0.2
---

**Who it's for:** a writer filling a Dramatica ingest for a Tier 3 character · **What it does:** numbered steps for each fill, generate and lock task · **Type:** how-to

# Dramatica ingest template: how-to

Field lookups: [reference](2-reference.md). Why: [concept](1-concept.md). After this form locks, go to the [astrology ingest how-to](../ssot_02_template_astrology_ingest/3-how-to.md).

## Start a character's Dramatica ingest

1. Confirm the character is Tier 3. A Tier 2 character gets an element signature and relational roles instead.
2. Copy the blank file to the character's folder as `[CHARACTER_ID]_dramatica_ingest.md`.
3. Delete the "How to use this form" section and the frontmatter.
4. Keep every section number.
5. Fill the Header: `character_id`, `ip`, `tier: 3`, `storyform_id`, `storyform_version`, `authoritative_doc_ref`.
6. Set `storyform_status` and `status` to `draft`.

## Fill the sections in extraction order

1. Fill Section 1 first, from the Story Dynamics Report.
2. Fill Section 4 (MC throughline) from the MC Theme Report.
3. Fill Section 3 (element quads) and Section 2 (structural role) from the Character Report and the Story Dynamics Report.
4. Fill Section 6 (OS throughline). Fill it for every character.
5. Fill Section 5 (IC) if the character is the IC. Fill Section 7 (RS) if the character is an RS principal.
6. Keep Section 8 as the log while you work.
7. Leave any field the storyform has not given yet empty. Write `⏸` and the reason. Never guess.

## Lock the storyform dynamics

1. Open the Story Dynamics Report.
2. Write `story_outcome` as Success or Failure.
3. Write `story_judgement` as Good or Bad.
4. Write `story_driver` as Action or Decision.
5. Write `limit_type` as Timelock or Optionlock.

## Fill the structural role and the quads

1. Write the six role fields: `structural_role`, `dramatica_archetype`, `resolve` (Change or Steadfast), `growth` (Start or Stop), `approach` (Do-er or Be-er), `mental_sex`.
2. Fill all eight element fields: two per quad, for the motivation, methodology, evaluation and purpose quads.
3. Write the structural meaning statement. Use two or three plain sentences. Say what this element set makes the character do to the argument.

## Fill the MC, OS, IC and RS throughlines

1. For an MC, fill all thirteen fields in Section 4, including `mc_inhibitor`.
2. For every character, fill the six fields in Section 6, including `os_role` and `story_goal`.
3. For an IC, fill `ic_domain` and `ic_concern`. Add any other IC points as free text.
4. For an RS principal, fill `rs_domain` and `rs_concern`.
5. Skip a throughline section the character does not need.

## Keep the report source log

1. Add one line for each report as you consult it, in extraction order.
2. Write the report name, what it fed, the file or page, and the date read.
3. Use the five rows the form starts with: Story Dynamics, Theme (MC), Character, Theme (OS, IC, RS), Character Relationships.

## Add a Touchstone

1. Write one structural law the storyform produces, in one sentence.
2. Write its number as TS and a number.
3. Cite the storyform source.
4. State what it costs the character.
5. Add at least one Touchstone for a Tier 3 character.

## Generate the L12 core block

1. Finish Sections 1 to 9 first.
2. Open the Dramatica integration doc and read its list of Tier 3 L12 core variables.
3. Write the `L12_FUNCTION` block with those variables. The form lists ten.
4. Copy each value from Sections 1 to 9. Match the section field names to the block names.
5. If the integration doc's list has changed, change the block to match it.

## Lock the record

1. Run the Downstream Handoff Checklist in Section 11.
2. Confirm Section 1 matches the Story Dynamics Report.
3. Confirm Section 2 has six fields and Section 3 has eight element fields plus the meaning statement.
4. Confirm Section 9 has at least one Touchstone.
5. Confirm Section 10 matches Sections 1 to 9.
6. Set `storyform_status` and `status` to `locked`. Set `locked_on` to the date.
7. Cite this file in `dramatica_ingest_ref` on the astrology form.
