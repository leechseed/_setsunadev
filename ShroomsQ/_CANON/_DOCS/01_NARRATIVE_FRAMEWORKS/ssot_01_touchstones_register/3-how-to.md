---
title: "The Touchstones register: how-to"
type: how-to
for: "A writer, Chief or Claude who cites, proposes or checks Touchstones"
does: "Gives the numbered steps for the tasks the Touchstones register defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_touchstones_register.md
source_version: 1.0.0
---

**Who it's for:** a writer, Chief or Claude working with Touchstones · **What it does:** steps for the register's recurring tasks · **Type:** how-to

# The Touchstones register: how-to

Source: [📐 ssot_01_touchstones_register.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_touchstones_register.md). Fields are in the [reference](2-reference.md).

## Cite a Touchstone

1. Find the Touchstone in the register.
2. Write its id as `TS book:number`, for example TS 1:1.
3. Cite the id and not the old word "invariant." Machine fields keep the old name until the schema pass.

## Propose a Touchstone candidate (Claude)

1. Find the statement in a source.
2. Quote the statement. Do not rewrite it.
3. List the source in `sources`.
4. Offer the candidate to Chief.
5. Do not mint an id. An id mints only on Chief's ruling.

## Rule a Touchstone in (Chief)

1. Read the quoted candidate.
2. Rule it in or out.
3. If ruled in, the register mints the id as `TS n:m`, with m next in the book.
4. Record the date and BOLO in `ruled`.
5. Leave `strength` at soft unless you say hard.

## Make a Touchstone hard

1. Chief says "hard" for that Touchstone.
2. Change `strength` from `soft` to `hard`.
3. Record the date of the ruling.

Never set hard without Chief's word.

## Add a Touchstone entry

1. Open the book the entry belongs to. Book 1 is Chief's direct rulings. Book 2 is Modern Poetics.
2. Write the heading: id and name.
3. Write `strength`.
4. Write the one-line statement from the source.
5. Write `sources`, `ruled` and, if needed, `scope`.
6. For a Modern Poetics principle, point to its law. Do not copy the law.

## Add a pushback

1. Use the `PB n:m` id space.
2. Fill the same fields as a Touchstone entry.
3. Mint the id only when Chief rules.

## Check the ids

1. Run `_tools/review/touchstone_check.py`.
2. The script greps every `TS \d+:\d+` under `ShroomsQ/_CANON/_SSOT/`.
3. Read the result. Each id must exist in the register.
4. Fix any id the script cannot find.

## Give a Touchstone an address span

1. Open the [scale ladder](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_scale_ladder.md).
2. Pick the span the Touchstone governs.
3. Write it in the optional `scope` field.

## Park instance content

1. Decide whether the content belongs to the OXO instance.
2. If it does, list it under PARKED (phase 2) with a ⏸ mark and its name.
3. Leave the fabula untouched.
