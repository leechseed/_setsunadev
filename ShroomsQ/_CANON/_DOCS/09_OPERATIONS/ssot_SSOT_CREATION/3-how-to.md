---
title: "SSOT creation guide: how-to"
type: how-to
for: "a writer producing a new SSOT document"
does: "gives the steps to create, fix, and file an SSOT document"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐ssot_SSOT_CREATION.md
source_version: 1.8.1
---

**Who it's for:** a writer producing a new SSOT document · **What it does:** gives the steps to create, fix, and file an SSOT document · **Type:** how-to

# SSOT creation guide: how-to

## Create an SSOT document

1. Decide whether the content is a methodology. If it is project-specific, send it to `_AUTHORITATIVE/` and stop.
2. Draft the core methodology and examples. Write with no hedges and in present tense. Contractions are allowed. Bold each technical term at first use.
3. Generate the YAML block from the standardized template. Check that `type`, `category`, and `applies_to` are present.
4. Check the file in Obsidian. If the YAML shows as a code block, run the next task.
5. Save the file as `📐 ssot_[category]_[name].md` in `_CANON/_SSOT/`.

## Make pasted YAML show as Properties

1. Put the first `---` at Line 1, Column 1.
2. If the YAML is still a code block, delete the first `---`.
3. Type three dashes `---` by hand at the top.
4. Check that the Properties UI now shows the fields.

## Name a new SSOT file

1. Write `📐 ssot_` first.
2. Add the category, an underscore, and the name.
3. Use lowercase and underscores in place of spaces.
4. Pick the emoji by content: 📐 for methodology, 🎯 for story or project content, ⚙️ for workflow or AI instructions.

> **OPEN:** the source does not say which emoji prefixes a file in `_AUTHORITATIVE/` beyond the taxonomy, or what the name rules are for `🎯` files.
