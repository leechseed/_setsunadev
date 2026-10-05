---
title: "AI instruction protocol: how-to"
type: how-to
for: "an operator who wants an AI to produce one SSOT document"
does: "gives the steps to run the master prompt and check its output"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_ai_instruction_protocol.md
source_version: 1.2.1
---

**Who it's for:** an operator who wants an AI to produce one SSOT document · **What it does:** gives the steps to run the master prompt and check its output · **Type:** how-to

# AI instruction protocol: how-to

## Generate an SSOT document with the master prompt

1. Give the AI the protocol as its instruction set.
2. Supply the raw concept.
3. Let the AI categorize it into one of six categories: epistemology, narrative_frameworks, character_systems, plot_systems, style_guides, operations.
4. Let the AI sanitize the input and map it to the frame and the body for its page type (07.2).
5. Let the AI refine for hedging.
6. Let the AI name the file `📐 ssot_[category]_[name].md`.

> **OPEN:** the source does not say what the operator pastes to start the run or how the six categories map to folders.

## Check the AI's output

1. Confirm the filename is the first line, above the YAML.
2. Confirm the file begins with `📐 ssot_`.
3. Confirm the YAML has `type`, `category`, `applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]`, `status: canonical`, and wikilink `dependencies`.
4. Confirm the frame: YAML, title, Table of Contents, Purpose, Version History. Confirm the body follows the page's type (07.2).
5. Confirm at least two examples on a concept page.
6. Scan for hedge words.

## Add a technical term to a document

1. Bold the term at its first use.
2. Define it in the same sentence or the next.
