---
title: Module registry: how-to
type: how-to
for: A designer registering, auditing or building a field module
does: Gives the steps for each registry task
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_registry.md
source_version: 1.1.0
---

**Who it's for:** a designer keeping the module registry · **What it does:** gives the steps for each registry task · **Type:** how-to

# Module registry: how-to

Entries live in the [reference](2-reference.md).

## Register a new module

1. Confirm it is a field module, a set of variables beneath a layer. A doc module does not belong here.
2. Pick a unique module ID.
3. Add a row to the Registry Overview.
4. Set the status to `conceptual` if only the scope is known, or `planned` if the declaration is full.
5. Do this before defining any variable.

## Write a conceptual entry

1. Add a table with ID, attachment, concept, scope, variables and status.
2. Write the scope as method: which layers it reads and what it holds.
3. Write `⏸ module build (phase 2)` in the variables row.
4. Leave the variable list for the module build.

## Promote a planned module to active

1. Write the full API declaration in this registry.
2. List every variable with path, type, scale and behavior.
3. List reads, derived stats and flags.
4. Change the status to `active` in the overview and the entry.
5. Add the variables to the Variable Registry.

## Absorb a module into the core schema

1. Find where each old variable now lives in the slice.
2. Write a table of old variable and where it went.
3. Mark any variable the slice lacks as dropped.
4. Set the status to `absorbed` and the variable count to 0, with the old count in brackets.
5. Update the dependency map and any module that read the absorbed one.

## Audit the planned modules

1. Check each planned module against the current slice.
2. Ask whether the slice now holds its fields.
3. Record a verdict per module: still planned, narrowed, absorbed or dropped.
4. Update the overview counts and the build order.

## Read the build order

1. Find a module's dependencies in the Dependency Map.
2. Build independent modules first.
3. Build DECOMP after COPING, and LOL_TAX after COMBAT.
4. Follow the source order: WALK, PHYS, COMBAT, FASHION, MUSIC, COPING, DECOMP, LOL_TAX.

> **OPEN:** the source names the audit slice (3.3.1) but not who rules a module absorbed or dropped.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [tutorial](4-tutorial.md)
