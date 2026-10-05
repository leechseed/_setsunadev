---
title: "Character system (LEECHSEED vertical slice): how-to"
type: how-to
for: "A writer or builder who knows the character system and needs to build, check or extend a slice"
does: "Gives numbered steps for each task the character system defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_systems_vertical_slice.md
source_version: 3.4.0
---

**Who it's for:** a writer or builder building, checking or extending a slice · **What it does:** numbered steps for each task · **Type:** how-to

# Character system (LEECHSEED vertical slice): how-to

Lookups: [reference](2-reference.md). Why: [concept](1-concept.md). A worked pass: [tutorial](4-tutorial.md).

## Choose a character's tier

1. Ask how much load-bearing weight the story puts on the character.
2. For a background character, use Tier 1: L1 to L3.
3. For a recurring supporting character, use Tier 2: L4 to L6.
4. For a protagonist or antagonist, use Tier 3: L7 to L12. This is mandatory.
5. Do not fill every field on a background character. That is a schema error.

## Build a vertical slice for a new character

1. Run the Step 1 source verification gate. Stop on a red result.
2. Assign Tier 1, then Tier 2, then Tier 3, in that order.
3. Compute the derived statistics.
4. Evaluate the flags.
5. Generate the structured data block.
6. Tag every field: static, dynamic or derived.
7. Mark every field you cannot source as null with the `⏸` marker. Invent no canon.

## Run the Step 1 source verification

1. Open the Step 1 gate module (version 1.1.0).
2. Check three things: the authority document, the Dramatica ingest and the astrology ingest.
3. Fix any red result. A red result stops the slice.
4. Note that numeric instability in the source produces unstable values.

## Assign Tier 1

1. Assign CORE, VITAL and SOCIAL. The default is 10 for each.
2. Price any level above 10: 20 pts for CORE, 20 pts for VITAL, 10 pts for SOCIAL.
3. Read the three values alone. They must suggest a recognizable character outline.
4. If they do not, revise the primary values.

## Derive Tier 2

1. Derive WILL from CORE (`WILL = CORE`). Adjust by documented resolve behavior. Buying costs 5 pts per level.
2. Assign WOUND from the character's history. Do not buy it. It records what happened.
3. Write `severity` as the same number. Add `triggers`.
4. Derive DRIVE from VITAL (`DRIVE = VITAL`). Keep it equal for an ambition-driven character. Lower it for a meaning-driven one. Buying costs 3 pts per level.
5. Check `want_need.need`. A Tier 2 or 3 character with an empty `need` is incomplete.

## Populate Tier 3

1. Populate L7 to L12 from canonical source documentation.
2. Give each variable a documented source.
3. If no source exists, mark the variable `[INFERRED]` and note the basis.
4. Schedule a follow-up extraction query for each inferred value. The layer is not complete until it runs.
5. Where the setting has a matching S4, S6 or S8 entry, cite it through `setting_ref`.
6. Fill L12 from the storyform, keyed by `storyform_id`. Use the Dramatica integration protocol for the field list.
7. For a Protagonist, document the necessity: show the character forced into the role.
8. Where a field names a world fact (a regime, a community, a civic standing or a tech level), set its `catalog_ref` to the 05 catalog entry id.
9. Set L11 `rail_ref` to the 06 theme rails (R1 to R4) the character carries.
10. Write L12 `touchstone` as the TS n:m id, with the slug as alias.

## Compute the derived statistics

1. Apply the seven formulas. Round all fractions down.
2. Basic Damage Resistance is `WILL - (WOUND / 2)`.
3. Social Legibility is `SOCIAL - (SHADOW.projection_tendency / 3)`.
4. Narrative Momentum is `DRIVE + (DESTINY.resistance_index / 2)`.
5. Stress Threshold is `WILL - WOUND`.
6. Collapse Risk is `(WOUND + SHADOW.shadow_density) / 2`.
7. Truth Exposure Index is `SOCIAL + max(0, 10 - EROS.shame_index)`.
8. Expressive Range is `12 - EROS.armor_index`.
9. Read Truth Exposure Index and Collapse Risk first. They most reliably show whether the numbers cohere.

## Evaluate the flags

1. Take each flag's trigger. Each is a SQL WHERE clause.
2. Test it against the computed values.
3. Set the state: ACTIVE, PENDING, FIRED_PRE_STORY or INACTIVE.
4. Record the narrative timing. For a PENDING or FIRED_PRE_STORY flag, store the fabula `event_id` beside it as `<FLAG>_event_id`. A PENDING flag with no event yet reads `null` with a `⏸` comment.
5. If a flag fires unexpectedly, investigate the contributing layer values before going on.

## Generate the structured data block

1. Write the header: `CHARACTER_ID`, `IP`, `STATUS`, `VERSION`.
2. Write each tier and layer section with its values.
3. Write `null` with a `⏸` comment for each blank.
4. Add the `L12_DRAMATICA_EXTENDED` and `DERIVED` sections.
5. Add `FLAGS` with the five states.
6. Check that every key carries a tag in the field-tag table.

## Tell the villain arc from the change arc

1. Read `resistance_index`, `change_cause` and flag SHADOW_DENIAL together.
2. Check the wound. Is it refused, faced or staged?
3. If a cause the character defeats leaves SHADOW_DENIAL ACTIVE at the climax, mark path (a), the villain arc.
4. If the character accepts the cause and the shield collapses, mark path (b), the change arc.
5. If `severity` oscillates and `wound_work` reads `reenacted_in_play`, mark path (c). Healing never finishes, and that is a valid value.

## Scope a field to an audience or a partner

1. Pick one of the four fields: `intimacy_mode`, `disclosure_posture`, `love_lust_cleft` or `self_presentation`.
2. Write a list of {ref, value}. The `ref` is a character_id or an audience name.
3. Keep the bare value as the default.
4. Tag the list as Dynamic.

## Add a new field to the schema

1. Check the schema-pass table. If a coined name is already an alias, use the target field.
2. Name the layer. A layer owns one domain, so do not overlap another.
3. Write the field's structure: sub-fields, value lists and ranges.
4. Give the field a tag: static, dynamic or derived. Apply the Decision Test. Would the value differ if you froze the character at two points?
5. Add it to the layer's domain declaration, the field-tag table and the structured data block.
6. Add the book to CHARACTER × LIBRARY with the layers it feeds.
7. Mark Victoria Midnight's instance `⏸ VM fill pass (phase 2)`.
8. Get Chief's ruling. Bump the version and add the version history line.

## Rename or merge a field without breaking old records

1. Keep the old name as a read alias for the new one.
2. Add the old name to the schema-pass table with its call: MERGE INTO the new field.
3. Leave stored values unchanged.
4. Tag the new field and record the rename in the version history.

## Cite a library source

1. Find the book's ID, such as BVX.0075 or MSX.18.
2. Add a row to CHARACTER × LIBRARY: ID, book, layers fed, what it gives.
3. Name the call or field it shapes, such as `CL16 want_need`.
4. Add the ID to the doc's `sources` list.
