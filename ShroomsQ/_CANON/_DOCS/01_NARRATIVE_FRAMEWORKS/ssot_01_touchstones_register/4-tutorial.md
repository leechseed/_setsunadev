---
title: "The Touchstones register: tutorial"
type: tutorial
for: "A new writer who has never used a Touchstone"
does: "Teaches the register by reading TS 1:1, then citing and checking it"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_touchstones_register.md
source_version: 1.0.0
---

**Who it's for:** a new writer · **What it does:** teaches the register by reading, citing and checking TS 1:1 · **Type:** tutorial

# Tutorial: read, cite and check TS 1:1

You will read one Touchstone, cite it in a note, and check the id. Keep the [reference](2-reference.md) open.

## Step 1: read the entry

Open Book 1. Find **TS 1:1 — the bounded container**. Read the fields:

- `id`: TS 1:1
- `strength`: soft
- `statement`: erotic or ritual power tends to hold inside a container and fade or turn dangerous without one.
- `ruled`: 2026-09-29, BOLO 91

Check: the strength is soft. That word means a tendency, never a rule.

## Step 2: read Chief's refinement

The container lives outside the story. It is a viewer-discretion disclaimer at the front of every book. The scenes inside stay free of it.

Check: you can say where the container goes. Answer: the front of every book.

## Step 3: cite it

Write a note in your draft:

```
Touchstone: TS 1:1 (bounded container, soft) is met by the front-of-book disclaimer.
```

Use the id, not the word "invariant."

## Step 4: check the id

Run `_tools/review/touchstone_check.py`.

The script greps every `TS \d+:\d+` under `ShroomsQ/_CANON/_SSOT/`. It confirms each id exists in the register.

> **OPEN:** the source gives the script's path but not its command-line form or output format.

## Step 5: meet a Modern Poetics entry

Open Book 2. Find **TS 2:10 — the aesthetic check**. It says every element must be interesting in at least one of color, shape or texture. The entry points to its law in Modern Poetics, section P10, and does not copy it.

## What you did

You read, cited and checked a Touchstone, and saw that Book 2 points to its law. Next, read the [how-to](3-how-to.md) to propose your own candidate.
