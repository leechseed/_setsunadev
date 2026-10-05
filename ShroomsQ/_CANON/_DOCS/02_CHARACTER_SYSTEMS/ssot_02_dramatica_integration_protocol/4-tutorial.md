---
title: "Dramatica integration protocol: tutorial"
type: tutorial
for: A new narrative designer learning the binding by doing it once
does: Walks one Tier 3 character, Victoria Midnight, through binding and L12 entry
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮 ssot_02_dramatica_integration_protocol.md
source_version: 1.3.0
---

**Who it's for:** a new narrative designer · **What it does:** one worked binding, start to finish · **Type:** tutorial

# Tutorial: bind Victoria Midnight to the primary storyform

You will write the binding record and the L12 entries for one Tier 3 character. Every value below comes from the source's own example. Definitions are in the [reference](2-reference.md).

## Step 1: Name the storyform

The OVEREXITOUT primary storyform needs an id. Write these fields.

- `storyform_id`: `oxo_primary_v1`
- `ip`: `overexitout`
- `scope`: `full_narrative`
- `parent_storyform_id`: `null`
- `status`: `locked`
- `version`: `1.0`

## Step 2: Write the binding record

Victoria is the MC. Write one binding record.

- `character_id`: `victoria_midnight`
- `storyform_id`: `oxo_primary_v1`
- `structural_role`: `mc_protagonist`
- `archetype`: `Protagonist`
- `resolve`: `Change`
- `throughline`: `mc`

You wrote one record, so her core L1-L11 record stays singular.

## Step 3: Fill the L12 core block

The source gives only some core values for Victoria. Write the two it gives.

- `resolve`: `Change`
- `dramatica_archetype`: `Protagonist`

> **OPEN:** the source gives no Victoria values for `methodology_element`, `evaluation_element`, `purpose_element`, `touchstone`, `story_outcome`, `story_judgement` or `limit_type`. The MC Problem in the sub-table is `Equity`. Fill the rest from her locked ingest.

## Step 4: Fill the extended sub-table

Copy the source's example values.

| Variable | Value |
|---|---|
| `mc_domain` | `Situation` |
| `mc_issue` | `Interdiction` |
| `mc_problem` | `Equity` |
| `mc_solution` | `Inequity` |
| `mc_unique_ability` | `Destiny` |
| `mc_critical_flaw` | `Truth` |
| `mc_focus` | `Desire` |
| `mc_direction` | `Ability` |
| `motivation_quad` | `[Consider, Pursuit]` |
| `methodology_quad` | `[Certainty, Proaction]` |
| `evaluation_quad` | `[Proven, Effect]` |
| `purpose_quad` | `[Knowledge, Actuality]` |

## Step 5: Leave the open fields open

Some fields read "from storyform" in the source: `mc_concern`, `mc_symptom`, `mc_response`, `mc_benchmark` and the OS, IC and RS sets. Leave them empty. An empty field means the ingest has not yielded it yet.

> **OPEN:** the source gives no Victoria values for the OS, IC and RS fields or for `mc_concern`, `mc_symptom`, `mc_response` and `mc_benchmark`.

## Step 6: Check your work

- One binding record exists, and it names `oxo_primary_v1`.
- The sub-table carries `storyform_id` as its binding key.
- You guessed no empty field.

## What you learned

You bound one character to one storyform. You filled the working core and the reference sub-table. You saw why an empty field is honest. Next, see the [how-to](3-how-to.md) for the other tasks.
