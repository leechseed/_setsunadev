---
title: "SSOT writing guide: tutorial"
type: tutorial
for: "A new SSOT writer learning the frame by building one small document"
does: "Teaches the SSOT frame by building the skeleton of a reference document"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_2a_writing_guide.md"
source_version: "2.2.1"
---

**Who it's for:** a new SSOT writer learning by doing · **What it does:** builds one SSOT skeleton with you · **Type:** tutorial

# SSOT writing guide: build one skeleton

The source's own file is a worked instance. This lesson mirrors its frame. You will build the skeleton of a small reference document called `ssot_demo`. Keep the [reference](2-reference.md) open.

## Step 1: open the YAML

Put three dashes alone on line 1. The guide requires the YAML boundary there.

## Step 2: write flat metadata

Add these lines, then close the block with three dashes:

```
type: ssot_06_style_guides
version: 0.1.0
reader: "a writer learning the frame"
doc_type: reference
owner: "Chief"
state: draft
reviewed: 2026-10-05
dependencies: ["[[📐 ssot_07_2a_writing_guide]]"]
```

Check each rule. Every key has a space after its colon. The wikilink sits in double quotes. A list would use square brackets.

## Step 3: write the title and contents

Write the H1 with 📐 and `ssot_` in front: `# 📐 ssot_demo`. Add a short, linked table of contents.

## Step 4: write the purpose

Write one paragraph that defines the scope. Bold the first technical term and define it at once. Use present tense and active voice. Strike any hedge.

## Step 5: pick the body

You named this a reference page. So the body holds facts as tables or entries. It does not hold numbered steps or a lesson. One page, one type.

## Step 6: close with the version history

End with a table. Give it Version, Date and Changes columns, and one row: `0.1.0`, today, "Initial draft."

You now hold a valid SSOT frame. For other tasks, see the [how-to](3-how-to.md).
