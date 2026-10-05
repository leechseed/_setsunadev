---
title: "The trope register: how-to"
type: how-to
for: "A writer, designer or script author who pulls, adds or keys tropes"
does: "Gives the numbered steps for the tasks the trope register defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_trope_register.md
source_version: 1.1.1
---

**Who it's for:** a writer, designer or script author working with tropes · **What it does:** steps for the register's recurring tasks · **Type:** how-to

# The trope register: how-to

Source: [📐 ssot_01_trope_register.md](../../../_SSOT/01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_trope_register.md). Fields and keys are in the [reference](2-reference.md).

## Pull the tropes for a layer

1. Open [LAYERS.md](../../../../../_tools/tropes/data/domains/LAYERS.md).
2. Find the layer id, for example L5 or S10.
3. Read the tropes keyed to it.
4. Check each trope's confidence in `register.json`. High keys are firmest.

## Key a trope to a layer

1. Choose the trope's domain or domains: character, setting, genre, sexuality, theme, texture, tracking or style.
2. For each domain, pick one key from that domain's vocabulary. Use null if no layer fits. Write it in `register.json`, the one key store.
3. Set `conf` to `high`, `medium` or `low`.
4. Write the record in the register's format.

## Key a trope with no definition

1. Check that the index gave no one-line definition.
2. Write `def: undefined`.
3. Key the trope by its title and its domain tags.
4. Set `conf` to match. Most of these land low.

No run is needed to fill the definition.

## Write a definition

1. Take the one-line definition from the TV Tropes index page.
2. Never copy page text. The repo is public.

## Add a Command-local record

1. Confirm Chief keeps the pattern on purpose across the Command's own worlds.
2. Write the record in the register's format.
3. Set `source: command-local`.
4. Set `slug` to a Command-local name, not a TV Tropes page id.
5. List each place the pattern appears under `instances`.
6. Add a `note` if a likely match exists in `register.json`.
7. On the next data pass, attach the record to the matching TV Tropes entry.

Changing a character is a separate step. A record names a pattern, not a fix.

## Read the skew

1. Find the layer with a large pile.
2. Check whether the index is the cause. Character roles pile on L12 because the Characters As Device index is mostly cast roles.
3. Treat an index-caused pile as a fact about the source, not a keying fault.
4. Treat a default dump as a fault. Re-key it with sharper rules.

## Check a keying batch

1. Run the script reviewer (RANGE) over the batch files.
2. Fix each broken file, misspelled slug and illegal key.
3. Re-run until it reports zero findings.
4. Run the spread check: confirm no layer swallowed a domain.

## Add a consumer TROPES section

1. Open the consumer system's doc.
2. Add one TROPES section that points at that system's layer lists.
3. Make it a call in that doc's own batch.

⏸ TROPES pointer sections (phase 2) are parked until then.

## Rebuild the register

1. Run `python _tools/tropes/fetch.py --domains` to pull the indexes. The script waits one second per request, skips slugs already cached, and stores no page bodies.
2. Have PS batches write the keys to `_tools/bolostatus/work/89/keys.batch*.json`.
3. Run `python _tools/tropes/build_register.py` with no arguments.
4. Read the output. The script writes `register.json` and `LAYERS.md` and prints the counts table.
