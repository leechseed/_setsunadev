# EUROPATCH: the brief (locked 2026-10-31)

Chief, 10/31, "lock it": one model for building anything complex out of modules, jacks and cables, like a
Eurorack synth or an Unreal / ComfyUI node graph. Generative, not on/off logic: set the parameters, the seed
rolls the thing (the Minecraft world-settings model). Name EUROPATCH (provisional; "europatch it" = use this model).

## Goal
A model (the SOP side) and a screen (the patch bay) that turn a patch of modules into seeded, repeatable JSON
instances, starting with characters from LEECHSEED.

## In
- **Module:** one lens or one layer (first set: LEECHSEED's 12 character layers). It carries dials, jacks in, jacks out.
- **Dials, stacked:** a type preset sets sliders (0 to 100) and weighted pick-lists in one move; Chief nudges any one dial after.
- **Jack:** a named input or output on a module (the interfaces, BOLO 102's layer).
- **Cable:** carries one value from an out-jack and bends the dial it plugs into, by a strength Chief sets.
- **Patch:** modules + dials + cables, saved as plain JSON. Sub-patches (a group saved as one block) and saved presets.
- **Seed:** rolls one instance from a patch. Same patch + same seed = same result; a new seed = a new instance with the same characteristics.
- **Output:** JSON parameters per module (the patch, the seed, what was rolled). Downstream tools read it: character sheet, place card, scene card, prompt.
- **Generation:** seeded dice inside the set ranges, drawing on what the Command holds (the trope register, the distills, the catalog). A model writes prose only after, from the JSON, when asked.
- **Screen:** a Console page on LiteGraph (ComfyUI's graph library): drag nodes, wire cables, group sub-patches, save and load patches as JSON.

## Out
- Binary logic gates (on/off switching); cables bend, they do not switch.
- A game engine now (Unreal / Godot); an export comes later, only if a game needs the patches.
- Model calls inside the roll; prose comes after, from the JSON.
- Pilot or fabula writing (BOLO 100: systems first). This is system work.

## Decisions made
1. Both: the model (SOP) and the screen. RULED.
2. Parameters first, then the seed rolls (the Minecraft model). RULED.
3. First patch: a character from LEECHSEED; second: a place cabled to it, so a place rolls its people. RULED.
4. Dials: presets + sliders + weighted lists, stacked. RULED.
5. Screen: the Console on LiteGraph first, engine export later. RULED.
6. Name: EUROPATCH. Provisional.

## Open calls, recs taken with "lock it" (provisional until Chief reads them)
1. Where the model lives: a short model doc beside the SSOT systems (00_EPISTEMOLOGY) + one glossary term so "europatch" means this.
2. A BOLO for it: BOLO 173, under BOLO 100's systems-first gate as system work.
3. The cable math: add or multiply with a strength, plus a curve; nothing on/off.
