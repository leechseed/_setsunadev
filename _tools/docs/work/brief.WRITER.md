# BOLO 102 · the core docs · writer brief (MS, one per system slice)

Repo root: C:\Users\U01_LEECHSEED\Desktop\_setsunadev. Write every file as UTF-8.

## The order

Chief, 10/4: "all 4 types of documentation for each system down to the minute smallest component". RULED 10/4: "core first". Core = each system's top-level docs in `ShroomsQ/_CANON/_SSOT/0*/`. Shelves (subfolders) are NOT core: do not document them. Chief, 10/5: "lets get all that documentation done".

You write the four pages for each core doc in YOUR SLICE (listed at the bottom of your prompt). Nothing else.

## Read

1. `ShroomsQ/_CANON/_SSOT/06_STYLE_GUIDES/📐 ssot_06_2_documents_style.md`, the section "THE DOCUMENTATION RULES — THE CORE (BOLO 95)" only. These rules are law for every page you write.
2. `_tools/docs/out/components.json`: your docs' components (H2) and parts (H3). Your reference page must cover every one.
3. Each source doc in your slice, whole.

Read nothing else. Do not consult other agents.

## Write

For each source doc, one folder: `ShroomsQ/_CANON/_DOCS/<system folder>/<stem>/`, where `<stem>` is the file name without the emoji, leading spaces and `.md` (e.g. `📐 ssot_02_character_astrology.md` → `ssot_02_character_astrology`). Four files, in this writing order (DOC-SOP 1.3):

| File | Type | Job |
|---|---|---|
| `1-concept.md` | concept | The why, read front to back. Classic voice. Headings state ideas. May end with one section "The long read". |
| `2-reference.md` | reference | Facts looked up and left. **One H2 per component, named exactly as in components.json, in that order; one H3 per part, named exactly.** Each entry: what it is, its fields/values/rules, where it connects. This is where "down to the smallest component" is met. |
| `3-how-to.md` | how-to | One H2 per task a user of this system performs ("Add a variable to the registry"), numbered steps. Tasks come from the source's procedures, steps, pipelines and rules. |
| `4-tutorial.md` | tutorial | One lesson, start to finish, learned by doing. Use a worked example the source already holds (e.g. an instance it documents). |

Every file starts with this front matter (DOC-SOP 2.2–2.3):

```
---
title: <plain title, e.g. "Character astrology: reference">
type: concept | reference | how-to | tutorial
for: <who it's for, reader + situation>
does: <the one job, one line>
owner: Chief
state: draft
reviewed: 2026-10-05
source: <repo-relative path of the source doc>
source_version: <the source's version, or "unversioned">
---
```

Then the first body line is the thin strip (DOC-SOP 2.1), exactly this shape:

```
**Who it's for:** … · **What it does:** … · **Type:** concept
```

Then a `# ` H1 title, then the page.

## Rules that bite

- **Facts only from the source.** Never invent canon, numbers, fields or steps. Where the source is silent and a page needs it, write one line `> **OPEN:** <what is missing>` and move on. A gap is a finding, not a failure.
- **Words (DOC-SOP 3.1–3.2):** one word for each thing, the source's word. Define a term the first time. One idea per sentence, 20 words at most. Every sentence names who does what: "the writer fills layer 3", never "layer 3 is filled". Quoted text stays verbatim even if long.
- **Voice (3.5):** concept = classic voice, no hedges. Reference, how-to, tutorial = practical voice.
- **Standing rulings to honor:** the series is **The Outliers**; the school is **Delta Coast Ultra School (DCUS)**; "Ariel" in old text is **Tori**; universe eras are 1 Skeeter Creek · 2 DCUS · 3 LAKAD · 4 ASTRO7EX · 5 beyond; invariants are **Touchstones** (cite TS 1:3); the studio is **BoldVenture** (Ultrasin is its ORANGE arm); the operation is **the Command**, the user is **Chief**. BOLO 100: no pilot writing; docs describe the method, they do not write story.
- **Private detail stays private:** no health, provider or personal sexual detail about Chief on any page. Story and method content (including adult story systems) is fine as the source states it.
- **A doc with zero components, or a retired / pointer / legacy doc:** write only `2-reference.md`, with `state: retired` if the source says it is superseded, and one line naming its successor. Skip the other three and list the skip in your reply.
- Links: link to sibling pages by relative path (`[reference](2-reference.md)`), and to the source doc by its repo path.
- Do not edit any source doc. Do not edit anything outside your slice's `_DOCS` folders.

## Reply

Three lines at most: docs done · pages written · OPEN count, and any skipped type with the reason.
