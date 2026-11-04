---
type: ssot_00_epistemology
category: europatch
version: 0.1.1
tier: foundation
last_updated: 2026-11-04
reader: "the CDR and the writers, before building or extending any system; Chief, ruling the open calls"
doc_type: concept
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "v0.1.0 2026-10-31: PROVISIONAL. Written from the locked brief (Chief: \"lock it and run what you need\", BOLO 173). The name EUROPATCH is provisional; every rule below is provisional until Chief reads it."
purpose: "EUROPATCH: one model for building anything complex (a character, a place of any size, a scene) out of modules, jacks and cables. Set the dials, the seed rolls the thing, the result is JSON. Saying 'europatch it' means: build this system in the standard below."
dependencies: ["_tools/europatch/BRIEF.md (the locked brief)", "ssot_02_character_systems_vertical_slice (LEECHSEED, the first module set)", "ssot_03_setting_system (S1–S12, the second)", "ssot_05_worldbuilding_system (the lens)", "ssot_08_tracking_system (cables)", "ssot_00_interface_catalog (jacks)", "ssot_01_trope_register (a draw source)", "ssot_00_module_architecture (field modules)", "ssot_01_collision_engine (friction)"]
trunk: BLACK
sources: ["BOLO 173 (spoken 10/31)", "_tools/europatch/BRIEF.md"]
rung: standard
---

# 📐 SSOT: EUROPATCH — modules, jacks and cables; set the dials, the seed rolls it

**Who it's for:** anyone building a system, a character, a place or a scene · **What it does:** gives every system one way to be built, wired and rolled · **Type:** concept · **Status:** provisional 0.1.0

## WHAT THIS IS

**EUROPATCH** is one model for building anything complex out of small parts. The parts are **modules**. Each module has **dials** you set and **jacks** you plug into. **Cables** run between jacks and carry values from one module to the next. A saved set of modules, dials and cables is a **patch**. A number called the **seed** rolls the patch into one result, an **instance**, saved as JSON.

Chief spoke it on 10/31 (BOLO 173):

- "if i were to create a city/state … each of those perspectives would be a node system in itself"
- "the whole idea of modularity of like euro racks"
- "like the whole graph type shit in unreal … generating the modules, then having a place to patch em all together … spit out like a json type parameters thing"
- "lock it and run what you need"

**Generative, not on/off.** A cable bends a dial. It never switches anything on or off. EUROPATCH has no logic gates.

**Parameters first, then the seed rolls.** This is the Minecraft world-settings model. You pick the world type and the settings, then the seed builds the world. The same settings with the same seed give the same world. A new seed gives a new world with the same character.

**Root claim:** every complex thing in the Command is a patch. Build the modules once, in one standard, and any system can wire into any other.

---

## THE PARTS

| Part | What it is |
|---|---|
| **Module** | One lens or one layer, as a box with dials, in-jacks and out-jacks. The first set is LEECHSEED's twelve layers, L1 CORE to L12 FUNCTION. |
| **Dial** | One setting on a module. Four kinds, below. |
| **Jack** | A named input or output on a module. An **out-jack** offers a rolled value. An **in-jack** takes a cable and bends one dial. |
| **Cable** | Carries one value from an out-jack to an in-jack. It has a **mode** (add or multiply), a **strength** (−1 to +1, set by Chief) and a **curve** (linear, ease-in, ease-out or S-curve). |
| **Patch** | Modules plus dials plus cables. Saved as plain JSON. |
| **Sub-patch** | A group of modules saved as one block, with its own outer jacks. It drops into a bigger patch like a single module. |
| **Preset** | A saved set of dial values. It sets many dials in one move. |
| **Seed** | A whole number that drives the dice. Same patch + same seed = same instance. |
| **Instance** | One rolled result of a patch. |
| **Output** | The instance as JSON: the patch, the seed and what each module rolled. |
| **Downstream reader** | Any tool that reads the output: the character sheet, the place card, the SCENE CARD, a prompt. A model writes prose only after the roll, from the JSON, and only when asked. |

### The four kinds of dial

1. **Preset.** A type that sets many dials at once. The bay's six presets are archetypes. LEECHSEED's tiers (Tier 1 Flat, Tier 2 Standard, Tier 3 Deep) are depth levels, not presets.
2. **Slider.** A value from 0 to 100, with a window. The seed rolls inside the window. A narrow window means the result is nearly fixed. A wide window means the seed decides more.
3. **Weighted list.** A pick-list where each choice has a weight. The seed draws from it. Heavier choices come up more often.
4. **Stacked.** The dials apply in a fixed order: the preset sets them, Chief nudges any one of them, the cables bend them, then the seed rolls.

**One roll.** Each module rolls after every module cabled into it. Its out-jacks pass the rolled values on, and the bay writes the JSON after the last roll.

**The cable math (provisional, brief call 3).** A cable carries a value from 0 to 1, shaped by its curve. **Add** moves the dial's centre by `strength × curve(value) × the dial's range`. **Multiply** scales it by `1 + strength × curve(value)`. The result stays inside the dial's limits.

**The output shape (provisional).** One example, with placeholder values:

```json
{
  "europatch": "0.1.0",
  "patch": "character.tier2",
  "seed": 48213,
  "modules": {
    "L5_WOUND": {"dials": {"wound": {"window": [40, 70]}}, "rolled": {"wound": 58}},
    "L4_WILL":  {"dials": {"will":  {"window": [30, 80], "bent_by": ["c1"]}}, "rolled": {"will": 47}}
  },
  "cables": [
    {"id": "c1", "from": "L5_WOUND.out.wound", "to": "L4_WILL.in.will", "mode": "add", "strength": -0.3, "curve": "linear"}
  ],
  "tension": {"L4_WILL.will": 0.0}
}
```

The `tension` field is defined under THE TWO PATTERNS.

**The screen.** The patch bay is a Console page on LiteGraph, ComfyUI's graph library, built under `_tools/europatch/` (brief, decision 5). This doc is the model; the screen follows it.

---

## WHAT THE COMMAND ALREADY HAS

Most of EUROPATCH is already in the Command, in pieces. Each system below gives a part and lacks a part.

| System | What it already gives | What it lacks |
|---|---|---|
| **LEECHSEED** ([02 vertical slice](../02_CHARACTER_SYSTEMS/📐%20ssot_02_character_systems_vertical_slice.md), v3.5.0) | The first module set, L1–L12. The tiers are depth levels, not presets; the bay's six presets are archetypes. The **derived statistics** are hard-wired cables (Stress Threshold is `WILL - WOUND`). The **structured data block**, "the database seed record", is the output's ancestor. | Values are entered, not rolled: no windows, weights or seed. Its formulas are fixed, with no strength to turn. |
| **Field modules** ([00 module architecture](📐%20ssot_00_module_architecture.md), v1.1.1) | "The 12 layers do not change. Modules attach beneath them." A field module becomes extra dials on its layer's module. | No cables beyond its read list. |
| **The lens** ([05 worldbuilding](../05_WORLDBUILDING_SYSTEMS/📐%20ssot_05_worldbuilding_system.md), v1.2.0, BOLO 93) | A perspective asked across every system. The catalog holds shared things (groups, styles, customs) to draw from. | A lens is ruled to own no data, only questions (SOP §5). It needs dials to sit in a patch (open call 3). |
| **The setting slice** ([03 setting](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md), v1.11.1) | The second module set, S1 BODY to S12 FUNCTION, mirroring L1–L12. Axis 1 SCALE runs spot to cosmos. **The polder test** is a ready sub-patch: the ring (S1), the keepers (S4), the flood (S11), the inside law (S4). | No windows, weights or seed. The polder test asks; it does not roll. |
| **Cables** ([08 tracking](../08_TRACKING_SYSTEMS/📐%20ssot_08_tracking_system.md) §6, v1.2.0, BOLO 90) | A cable links a setup to its payoff on the fabula's `enable` edge. A cable missing an end is an **orphan**, flagged, never dropped. | No strength, no curve. Those cables run through story time; these run inside one roll (open call 2). |
| **The interface layer** ([00 interface catalog](📐%20ssot_00_interface_catalog.md), v0.2.0, BOLO 102) | 514 interfaces across 45 system pairs, one IF id each. Every **DATA** interface is a ready jack pair. | **CONTROL** interfaces gate or trigger, so they stay outside the patch. No values or strengths. |
| **The trope register** ([01 trope register](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_trope_register.md), v1.1.1, BOLO 89) | About 8,700 tropes keyed to layers (L1–L12, S1–S12, G1–G12): a pull list for every weighted-list dial. | No weights. Its `conf` field can seed them (open call 7). |
| **Friction** ([01 collision engine](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_collision_engine.md), v1.0.1) | "Any slice against any slice, producing friction", proven on Tori × DCUS. | It compares finished slices. EUROPATCH measures the pull during the roll. |

---

## THE TWO PATTERNS

Chief named two patterns on 10/31. Both read off the cables.

**Tension.** When two or more cables plug into one dial, the bay measures how hard they pull against each other:

`tension = (the sum of each pull's size) − (the size of their sum)`

If every cable pulls the same way, tension is 0. If they cancel, tension is high even when the dial barely moves.

### Set pieces live where lenses collide

A **set piece** is a big scene the story builds toward. It belongs where cables pull opposite ways on one place: the dial looks calm because it is held still by force.

**Worked example (placeholders).** Place P's S4 LAW and S10 UNDERSIDE both cable into P's dial `visibility`. LAW pulls it up (+0.7); UNDERSIDE pulls it down (−0.6). The dial nets +0.1 and looks quiet, but tension is 1.3 − 0.1 = 1.2. The bay flags P as a set-piece candidate. It writes no event; a writer decides what happens there.

**An already-canon case.** At DCUS, the S5 SCAR row records the rename lattice, Skeeter Creek → Red Hills → DCUS. Legacy students saying "Red Hills" "commit a small legibility violation every time they speak" ([03 setting](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md), THE INSTANCE, S5). In patch terms, S8 HABIT (the old name) and S4 LAW (enforced legibility) pull opposite ways on one dial: what the place is called. That dial is where a set piece can live.

### Reflective moments live where lenses agree

A **reflective moment** is a quiet beat where the place states its argument without a fight. It belongs where several cables pull the same way on one dial: tension near 0, total pull large.

**Worked example (placeholders).** Place Q's S2 WEATHER (+0.4), S6 ECONOMY (+0.5) and S8 HABIT (+0.3) all cable into the dial `who belongs`. Tension is 0; total pull is 1.2. The bay flags Q as a reflective-moment candidate.

**An already-canon case.** The DCUS S2 row rules "the cooled-building split": "Feed-conditioned interiors, the Gulf heat left outside for whoever doesn't rate a cooled building: class by budget line, not verdict" ([03 setting](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md), THE INSTANCE, S2). Weather and economy agree. Standing in the heat outside a cooled building says the controlling idea with no conflict at all.

---

## SCALING

**One rack, any size.** The same modules work at every rung of Axis 1. A block is a sub-patch; a district holds blocks; a region holds districts. Places already nest by address, such as `DCUS.campus.hall3.room12`.

**Parents bend children.** A region's S2 climate band can cable into the S2 dial of every place inside it. Each child still rolls its own seed, so the blocks differ but share a climate.

**One character to a cast.** Roll one character patch with ten seeds for ten people with the same characteristics. The Hierarchy Rule holds: background people take Tier 1 depth, leads take Tier 3.

**A place rolls its people.** This is the second patch (brief, decision 3). The place patch cables into the character patch, for example S6 ECONOMY into L7 ORIGIN, S8 HABIT into L3 SOCIAL, S4 LAW into L4 WILL. One place dial sets how many people to roll. One jack of this kind already exists: S8's tier `price` names a `witness`, a `character_id` (IF catalog call 5). The first build decides the real cable set.

---

## REAL-WORLD KIN

| Kin | What it teaches |
|---|---|
| **Eurorack** (modular synths) | Modules from many makers work together because they share one power rail and one voltage range. The standard is the trick. |
| **Unreal and ComfyUI node graphs** | Wiring as the interface, sub-graphs as groups. ComfyUI saves a graph as JSON, so a patch is a file you can share. |
| **Minecraft world presets** | Parameters first, then a small, repeatable seed. |
| **Christopher Alexander, *A Pattern Language*** (1977) | Patterns run from regions down to rooms, each linked to those above and below. One rack, every scale. |
| **Kevin Lynch, *The Image of the City*** (1960) | A city as residents picture it: paths, edges, districts, nodes, landmarks. A resident's lens is a module. |
| **Dwarf Fortress** (world generation) | Simulations stacked on one map: terrain, climate, history, peoples. Depth comes from stacking, not scripting. |

---

## THE RULE THAT MAKES IT WORK: THE SHARED STANDARD

Eurorack works because every module speaks the same voltage. **The shared standard** is EUROPATCH's voltage: the keys every module speaks.

1. **Layer ids.** A module is named by a key the Command already uses: L1–L12, S1–S12, G1–G12, and the other keys the trope register lists.
2. **Jack names.** `<module>.in.<dial>` and `<module>.out.<value>`. A jack that matches a DATA interface carries its IF id.
3. **One value range on the cable.** Every cable carries 0 to 1. Each jack declares its own native range (0–100, LEECHSEED's native scales per the spine's scale column, a list) and converts at the jack. The bay's 0–100 sliders are a display of the normalized value. LEECHSEED's canonical store is normalized 0–1 (RULED 2026-11-04, BOLO 176, a design rule that is not built yet).
4. **One address.** Anything placed in time carries the 08 time code, the one address in every system (08 §4A).
5. **One file format.** Patches, presets and instances are plain JSON in the shape above.

**"Europatch it."** When Chief says "europatch it" about a system, the system ships in the standard:

- its **modules**, one per layer or lens, named by key;
- each module's **dials**, with windows, weights and at least one preset;
- its **jacks**, named in the standard, with IF ids where they exist;
- one test patch and one seeded roll that comes out the same twice.

A new system that skips this can still be written. It just cannot be wired.

---

## OUT OF SCOPE

From the brief:

- **Logic gates.** No on/off switching. Cables bend; they do not switch.
- **A game engine now.** Unreal or Godot export comes later, only if a game needs the patches.
- **Model calls inside the roll.** The roll is dice only. Prose comes after, from the JSON.
- **Pilot or fabula writing.** This is system work under BOLO 100, systems first.

---

## OPEN CALLS

Each call has a rec. All are provisional until Chief rules.

1. **The word "module" now has three meanings** (field module, doc module, and this). **Rec:** write "patch module" whenever the bare word could mean another; inside EUROPATCH docs, plain "module" is fine.
2. **The word "cable" clashes with 08 tracking's cables** (setup → payoff over story time). **Rec:** 08 keeps "cable"; in mixed text, EUROPATCH writes "patch cable".
3. **"Lens" is ruled to own no data,** but Chief's patterns say lenses collide. **Rec:** a lens that gets dials becomes a module; the question set keeps the word "lens"; the two pattern names stay as Chief said them.
4. **Where instances live and what they are.** **Rec:** rolled instances are draft output under `_tools/europatch/`, never canon, until Chief promotes one (the research-not-fabula rule, BOLO 156). EUROPATCH is a model, a way of building, not a fifth word beside system, layer, lens and view.
5. **Feedback loops** (a cable path that circles back). **Rec:** none in 0.1. A loop has no roll order, so the bay flags it as an error.
6. **How the seed reaches each module.** **Rec:** each module gets its own seed made from the patch seed plus its module id. Editing one module then rerolls only it and the modules downstream.
7. **Default weights from the trope register.** **Rec:** `conf` high = 3, medium = 2, low = 1, and Chief nudges from there.
8. **The name.** **Rec:** keep EUROPATCH; it says what it is and "europatch it" works as a verb.

---

## Version history

- **0.1.0 — 2026-10-31.** PROVISIONAL. First write, from the locked brief (BOLO 173, Chief: "lock it and run what you need"). Parts, mapping, the two patterns, scaling, kin, the shared standard, eight open calls.
- **0.1.1 — 2026-11-04.** Chief: go recs path cleanup (BOLO 176), and Chief: go (normalized store, BOLO 176). Tiers are depth levels, not presets; the bay's presets are archetypes. Shared standard notes the normalized store (ruled, not built) and the scale column.
