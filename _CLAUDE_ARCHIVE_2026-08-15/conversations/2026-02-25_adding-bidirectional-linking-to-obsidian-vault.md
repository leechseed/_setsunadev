---
title: "Adding bidirectional linking to Obsidian vault"
uuid: 90689e45-d9d8-4138-b28b-d33631b652e0
created: 2026-02-25
updated: 2026-02-25
trunk: BLACK
messages: 4
chars: 2741
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Adding bidirectional linking to Obsidian vault

> **Conversation Overview**

The user inquired about Claude's ability to add bidirectional linking to an Obsidian project, initially asking whether this would require Claude Code or could be done in the regular chat interface. Claude explained that for small to medium vaults (under a few hundred notes), the task could be accomplished directly in chat by uploading a zipped vault, with Claude parsing markdown files, identifying cross-references, and adding wikilinks bidirectionally before repackaging for download.

The conversation evolved when the user clarified that their vault contains no existing links, asking whether Claude could determine appropriate connections from scratch. This shifted the discussion to semantic linking based on content analysis rather than simply formalizing existing references. Claude outlined an approach involving building concept maps from note content, identifying shared themes and entities across notes, scoring relationship relevance, and strategically placing inline wikilinks where connections feel natural in the prose rather than dumping them in footers. Claude acknowledged the limitation that judgment calls about meaningful relationships might not always align with the user's intended knowledge structure, but positioned this as a solid first-pass solution that would allow the user to review and refine rather than build connections from zero. The user expressed interest in proceeding with this approach.

---
## 🧑 Papi  <sub>2026-02-25 20:42:59</sub>

If I gave you an obsidian project would you be able to take it and add bi directional linking? Or would that be like a claude code thing

---

## 🤖 Claude  <sub>2026-02-25 20:43:07</sub>

Quick answer about capabilities.Yeah, you could do it here actually — you'd just zip up the vault and upload it, and I could parse all the markdown files, identify concepts/notes that reference each other, and inject `[[wikilinks]]` bidirectionally across the files, then package it back up for download.

The main limitation here is file count/size. If your vault is small to medium (say, under a few hundred notes), it's totally doable in this chat. I'd:

1. Unzip and scan all `.md` files
2. Build a map of note titles and aliases
3. Find unlinked mentions of other note names in each file
4. Add the `[[links]]` where missing and update both sides
5. Repackage and hand it back

For a very large vault (thousands of notes), Claude Code would be better since it can work directly on your filesystem without the upload/download overhead and won't run into context limits as easily.

What's the rough size of your vault?

---

## 🧑 Papi  <sub>2026-02-25 20:53:02</sub>

Well there are no links. Would you be able to sort of figure out how to link

---

## 🤖 Claude  <sub>2026-02-25 20:53:12</sub>

They're asking if I can infer which notes should be linked even when there are no existing links - essentially semantic linking based on content analysis.Yeah, that's actually the more interesting problem. Since there are no existing links to go off of, I'd be doing **semantic/conceptual linking** — reading the actual content of each note and deciding what relates to what.

The approach would be something like:

**What I'd look for:**
- Notes that share key concepts, terms, or themes
- Notes where one explains something another references (even informally)
- Named entities — people, places, projects, ideas — that appear across multiple notes
- Notes that are clearly "parent/child" in topic scope

**How I'd handle it:**
- Build a concept map from all the notes first
- Score relationships by relevance
- Add `[[links]]` inline where the connection is natural in the prose, not just dump them in a footer
- Optionally add a `related:` frontmatter section for softer connections

**Honest limitation:** I'd be making judgment calls on what's meaningfully related vs. just tangentially similar. For a personal knowledge base, some of those calls might feel off to you since you know the intended meaning behind your notes better than I can infer.

But it could be a really solid first pass — you'd review and prune rather than having to build from scratch.

Want to try it? Zip the vault and drop it here.