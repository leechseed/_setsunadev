---
title: "The trope register: tutorial"
type: tutorial
for: "A new writer who has never pulled or keyed a trope"
does: "Teaches the register by keying the Signature Wound and pulling a layer list"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_trope_register.md
source_version: 1.1.0
---

**Who it's for:** a new writer · **What it does:** teaches the register by keying one worked record · **Type:** tutorial

# Tutorial: key the Signature Wound

You will build the register's one Command-local record, field by field. Then you will find the layer it keys to. Keep the [reference](2-reference.md) open.

## Step 1: name the pattern

Chief's own recurring wound: a sibling dies in a vehicle disaster. It appears in two worlds. Tori (OXO/DCUS): a car crash, and her brother Jebb dies. Mayari (LEECHSEED): a helicopter crash, a brother ejected, a father burns alive. "Ariel" in old notes is Tori's earlier name.

Check: the pattern spans two separate worlds and is kept on purpose.

## Step 2: write the identity fields

```
slug:    SignatureWound
name:    The Signature Wound — a sibling dies in a vehicle disaster
def:     Chief's own recurring wound, kept on purpose across separate worlds, not a contradiction between them
source:  command-local
```

The slug is a Command-local name. It is not a TV Tropes page id.

## Step 3: pick the domains and keys

The wound is a character pattern and a theme pattern.

```
domains: [character, theme]
keys:    {character: L5, theme: R2}
conf:    high
```

L5 is WOUND. R2 is Death. Check: each domain has one key.

## Step 4: list the instances

```
instances:
  - Tori (OXO/DCUS): car crash, brother Jebb dies
  - Mayari (LEECHSEED): helicopter crash, brother ejected, father burns alive
```

## Step 5: add the note

The source adds a note: a likely match, Dead Sibling or Survivor Guilt, may already sit in `register.json`. Nobody has cross-checked it. Write that note. On the next data pass, attach the record to the matching entry.

## Step 6: pull a layer list

Open [LAYERS.md](../../../../../_tools/tropes/data/domains/LAYERS.md). Find character L5. Check whether Dead Sibling or Survivor Guilt appears. This is the cross-check the source leaves open.

> **OPEN:** the source says the cross-check was not done. This tutorial does not report its result.

## What you did

You wrote a Command-local record from start to finish and learned where to find the check it needs. Next, read the [how-to](3-how-to.md) for the other keying tasks.
