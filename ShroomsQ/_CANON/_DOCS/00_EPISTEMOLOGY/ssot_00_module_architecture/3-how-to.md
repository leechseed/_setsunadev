---
title: "Module architecture: how-to"
type: "how-to"
for: "A designer building, enabling or retiring a field module"
does: "Gives the steps for each module task the architecture defines"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_architecture.md"
source_version: "1.0.2"
---

**Who it's for:** a designer building or running a field module · **What it does:** gives the steps for each module task · **Type:** how-to

# Module architecture: how-to

Blocks and tables live in the [reference](2-reference.md).

## Create a field module

1. Write the module declaration block: id, name, version, author, attachment points, tier_min, depends_on, description.
2. Write a variable declaration block for each variable.
3. Write the read dependencies block.
4. Add a computation block if the module derives a value or raises a flag.
5. Register the module in the Layer-Locked Module Registry.
6. Add the variables to the Variable Registry under `MOD.[CODE].*`.

## Attach a module to a layer

1. Name the layer or layers the module belongs to.
2. Ask whether the content falls within that layer's domain.
3. Check the Step 2 domain table for the layer.
4. If the content spans two layers, declare both.
5. Pick a unique 3-8 character uppercase module code.

## Register a module variable

1. Use the path `MOD.[MODULE_CODE].[variable_name]`.
2. Give a numeric variable a scale class from the Base 60 SSOT.
3. Declare its type from the standard set.
4. Declare its source: authored, derived or computed.
5. List the core variables it reads.

## Read another module's variable

1. Add `DEPENDS_ON: [MODULE_CODE]` to the reading module.
2. Confirm the other module is installed before activation.
3. Confirm the dependency is not circular.

## Enable a module in the application

1. Toggle the module on in the plugin panel.
2. Check the layer panels show its fields.
3. For existing characters, set each field to a default or `[UNASSIGNED]`.

## Populate a module for a character

1. Open the character in Edit mode.
2. Fill the module's fields.
3. Check the module's derived stats and flags in its panel.

## Disable or retire a module

1. To disable, toggle the module off. The data stays.
2. To retire, mark the version `retired`.
3. Leave data in the character records for the archive.

## Add a registry entry

1. Fill every registry field: id, name, version, status, attachment points, tier_min, variable count, derived, flags, depends_on, description.
2. Pick the status: `conceptual`, `planned`, `draft`, `active`, `absorbed` or `retired`.
3. Move a module to `planned` when its registry entry holds every field and a variable list.
4. Move it to `draft` when the author writes the module declaration and the variable declarations under `MOD.[CODE].*`.
5. Move it to `active` when the application can enable it and Chief rules it in.
6. Ask Chief to rule every move.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [tutorial](4-tutorial.md)
