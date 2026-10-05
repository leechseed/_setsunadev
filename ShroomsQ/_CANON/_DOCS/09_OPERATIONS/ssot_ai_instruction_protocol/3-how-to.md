---
title: "AI instruction protocol: how-to"
type: how-to
for: "an operator who wants an AI to produce one SSOT document"
does: "gives the steps to run the master prompt and check its output"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_ai_instruction_protocol.md
source_version: 1.3.0
---

**Who it's for:** an operator who wants an AI to produce one SSOT document · **What it does:** gives the steps to run the master prompt and check its output · **Type:** how-to

# AI instruction protocol: how-to

## Generate an SSOT document with the master prompt

1. Paste the whole protocol file, then one raw concept, in a single message. This gives the AI its instruction set and its input together.
2. Let the AI categorize it into one of six categories: epistemology, narrative_frameworks, character_systems, plot_systems, style_guides, operations.
3. Let the AI sanitize the input. Let it map the input to the frame and the body for its page type (07.2).
4. Let the AI refine for hedging.
5. Let the AI name the file `📐 ssot_[category]_[name].md`.
6. Save the file in the folder for its category.

   | Category | Folder |
   |---|---|
   | epistemology | `00_EPISTEMOLOGY` |
   | narrative_frameworks | `01_NARRATIVE_FRAMEWORKS` |
   | character_systems | `02_CHARACTER_SYSTEMS` |
   | plot_systems | `04_PLOT_SYSTEMS` |
   | style_guides | `07_STYLE_GUIDES` |
   | operations | `09_OPERATIONS` |

7. Ask Chief where content for domains 03, 05, 06 and 08 lands, because no category names them.

## Check the AI's output

1. Confirm the filename is the first line, above the YAML.
2. Confirm the file begins with `📐 ssot_`.
3. Confirm the YAML has `type`, `category`, `applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]`, `status: canonical`, wikilink `dependencies`, a `rung` (policy, procedure, standard or handbook), and a `trunk` (BLACK or ORANGE).
4. Confirm the frame: YAML, title, Table of Contents, Purpose, Version History. Confirm the body follows the page's type (07.2).
5. Confirm at least two examples on a concept page.
6. Scan for hedge words.

## Add a technical term to a document

1. Bold the term at its first use.
2. Define it in the same sentence or the next.
