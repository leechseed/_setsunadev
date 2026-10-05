---
type: ssot_01_narrative_frameworks
category: scale_ladder
version: 1.1.0
tier: narratology
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, all future IPs, BVX-LEARN keying]
status: canonical — Module 1 of the lattice, delivered on Chief's clear 2026-08-25
purpose: "THE SCALE LADDER — the container hierarchy from beat to universe: what each unit IS, its completion test, its address, and how multiple stories nest inside one series. Lattice limb 1 of 4."
dependencies: ["ssot_01_story_spine_comparative_tree", "ssot_02_dramatica_integration_protocol"]
trunk: BLACK
---

# 📐 SSOT: THE SCALE LADDER — from beat to universe

**What this is:** the container hierarchy of narrative. The spine says what a story IS; the ladder says **what size things come in and how they nest** — the answer to "scene → sequence → arc → story → stories within one large series." Every unit gets: a definition, a **completion test** (what makes one whole), its governing system, and holdings.

**Touchstones:** read [the Touchstones register](📐%20ssot_01_touchstones_register.md) first.

**One name (IF-01-05-12; IF catalog call 10, ruled 2026-10-05):** "scale ladder" means this document's R1–R8 and nothing else. The 05 worldbuilding system calls its three tiers (world-economy, nation-state, locality) "the reach".

**The core conceptual move — CONTAINERS vs THREADS.** The ladder's rungs are *containers*: units of presentation with boundaries. **Arcs are not a rung — arcs are *threads*:** tracked lines of change (character arc, setting arc, relationship arc, thematic motif) that run *through* containers at any span. TV vocabulary blurs this ("story arc" as a container of episodes); the house keeps it clean: **containers hold, threads change.** *(Provisional ruling — flagged for Chief; matches the Weiland arc vocabulary already in the library.)*

---

## THE RUNGS — bottom-up

### R1 · BEAT
- **Is:** the smallest dramatic exchange — one action met by one reaction, producing one micro-shift in a value or intention. (McKee's behavior-exchange unit.)
- **Completion test:** something was tried, something answered, something is now slightly different.
- **Governed by:** plot_systems (below the spine's floor). Storyform-blind — beats serve the scene.
- **Holdings:** McKee *Story* (0175) · Coyne (0236, micro-beats within commandments).

### R2 · SCENE
- **Is:** a unit of continuous dramatic attention (typically unified time/place) that completes a miniature dramatic arc. The smallest container that *turns*.
- **Completion test — dual, both required:**
  1. **Value turn** (McKee): at least one value polarity flips (+→− or −→+). No turn, no scene — it's exposition wearing a costume.
  2. **Five commandments present** (Coyne): inciting incident → complication → crisis → climax → resolution.
- **Pacing lives here formally:** Genette's **duration** — the ratio of story-time to page/screen-time (scene ≈ 1:1, summary compresses, stretch dilates, pause halts, ellipsis skips). Full treatment = Module 3 (Texture); the ladder just fixes the address.
- **Notation:** the house **SCENE CARD** — commandments + value charge + duration + setting state. **Specced in Module 2** (needs the setting slice's state fields); the ladder reserves its slot.
- **Holdings:** Coyne (0236) · McKee (0175) · Alderson *Deep Scenes* (0274) · Munier (0154) · Dunne (0062) · Rayne Hall (0281).

### R3 · SEQUENCE
- **Is:** a chain of scenes unified by one dramatic question or objective — raised at the head, answered at the tail (classical Hollywood ran films as ~8 sequences; Coyne's commandments recur at this level).
- **Completion test:** the sequence-level question is answered (and usually replaced by a worse one).
- **Holdings:** Aronson (0188) · Frayne (0228) · Coyne (0236 — the fractal recursion is the load-bearing idea: **the five commandments repeat at scene, sequence, act, and global scale**).

### R4 · ACT / MOVEMENT
- **Is:** one span of the argument — structurally, the span in which each throughline consumes one **Signpost** (Dramatica: 4 signposts + 3 journeys per throughline), turned by a **Driver**.
- **Completion test:** all four throughlines have advanced one signpost; a driver (action or decision) has turned the story.
- **House note — OXO's six Movements vs four signposts:** Movements are *presentation* containers (storyweaving); signposts are *structural* order (storyforming). Six movements can carry four signposts (journeys and multi-movement signposts absorb the difference). **The Movement↔Signpost mapping table is plot_systems work — flagged, not yet built.**
- **Holdings:** Dramatica (0089) · Yorke (0127, fractal five-act) · three-act via Aronson/Fink (0188/0092).

### R5 · STORY (the storyform)
- **Is:** one complete Grand Argument — the spine's whole tree, satisfied. One storyform = one story.
- **Completion test:** all four throughlines complete; Outcome and Judgment delivered; the argument closed from every seat.
- **Governed by:** the spine ([📐 ssot_01_story_spine_comparative_tree.md](📐%20ssot_01_story_spine_comparative_tree.md)) + the integration protocol. Instance: [oxo-storyform.md](../../../../_CANON_NODES/oxo-storyform.md).

### R6 · NESTED STORYFORM — story within story
- **Is:** a complete argument living inside a parent argument. **Already canon** — integration protocol Pattern 1: own `storyform_id`; a character may hold different roles across forms (MC in the parent, IC in a nested form); **the parent has authority** on conflict.
- **Completion test:** complete as a storyform (R5 test) *and* consistent with the parent.
- **Use cases:** an episode with its own argument; a movement-level mini-form (flagged as "act-level mini-forms" in the protocol); a book inside a series; a flashback story; a story a character tells.
- **Holdings:** integration protocol · Mittell (0565).

### R7 · IP / SERIES — many stories, one container
- **Is:** the owned narrative property holding multiple storyforms plus their shared canon. **This rung answers "how do multiple stories exist within one large series" — there are four canonical patterns:**

| Pattern | Mechanism | Example shape |
|---|---|---|
| **Anthology** | independent storyforms, shared premise/world only | season = new cast, new form |
| **Serialized** | ONE storyform stretched across many installments | the novel-in-episodes; OXO's primary form across six movements |
| **Episodic-with-mythology** | nested forms (episode arguments) under a parent form (the series argument) | case-of-the-week + season arc |
| **Braided / ensemble** | parallel storyforms sharing one OS, different MC seats | multi-protagonist epics |
- **Completion test:** every member storyform closed; the shared canon uncontradicted; if a parent form exists, it closes last.
- **House status:** OXO = serialized (primary form, full narrative scope) with nested forms architecturally ready. **IP-level meta-forms flagged in the protocol, not implemented.** Transmedia distribution of one IP across mediums: McErlean (0126) — connects to Module 4.
- **Holdings:** Mittell (0565) · McErlean (0126) · integration protocol.

### R8 · UNIVERSE / CANON
- **Is:** multiple IPs sharing substrate — world rules, entities, systems. The LEECHSEED level: the integration protocol already scopes `applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]`.
- **Completion test:** none — a universe never completes; it stays *consistent*. The test is canon integrity.
- **Governed by:** the house canon machinery itself — `_CANON_NODES/` + the SSOT system ARE this rung's implementation. Cross-IP arguments would be R7 meta-forms spanning IPs (same flag).
- **Catalog (IF-01-05-09; IF catalog call 3, ruled 2026-10-05):** the writer holds R8's shared world rules, entities and systems as entries in the [05 worldbuilding catalog](../05_WORLDBUILDING_SYSTEMS/📐%20ssot_05_worldbuilding_system.md) (`WB-<TYPE>-<nnnn>`). The canon-integrity test reads those entries.
- **Holdings:** Collaborative Worldbuilding (0067 — multi-author canon management) · the worldbuilding shelf.

---

## THREADS — what runs through the containers

A thread is a tracked line of change with a span, not a boundary:

| Thread | Tracks | Span it typically runs |
|---|---|---|
| **Character arc** | Resolve line — the MC's Change/Steadfast progression | R5, visible per-scene |
| **Setting arc** | a place's state over time (Module 2 builds this) | any — scene to universe |
| **Relationship arc** | the RS throughline's growth | R5; braids across R6 forms |
| **Thematic motif** | an Issue/Counterpoint recurrence; the 06 theme system supplies the rails R1–R4 and the `motif.<slug>` ids (IF-01-06-09; IF catalog call 2) | any |
| **Trope instance** | a register entry playing out (lattice trope register) | any |

## THE CONSTRAINT CHECK — Touchstones over the ladder (wired 2026-08-25)

Touchstones are neither containers nor threads — a thread changes, a Touchstone forbids. They are the standing constraint layer, governed by [DOCTRINE-0-INVARIANTS.md](../../../../DOCTRINE-0-INVARIANTS.md), and DOCTRINE 0's meta-rule IV ("holds at every scale — line, scene, movement, series") is literally this ladder's dimension.

**The enforcement rule:** every rung's completion test carries one final implicit clause — ***…and no in-scope Touchstone is breached.*** A scene that turns beautifully while violating a standing Touchstone is not a whole scene; it is a breach (meta-rule VII), and it invalidates downstream units that trusted it.

**Breach record (IF-01-08-16; IF catalog call 6, ruled 2026-10-05):** the writer logs each breach in the Touchstone breach log in 08 §9A (address · TS id · invalidated units). The address is an 08 time code.

**The census, scope-mapped to rungs:** Layer 0 Invariants 1–5 (world physics) → R8 · Invariants of Power (KLK) → R7 · `touchstone` (e.g. `cost_and_meaning`) → R5 · Six Movements set (one per movement: Equity → Collapse) → R4 · Ecclesial Laws (place-scoped) → the setting slice S12 · per-character sets (Tori ×4) → character threads. A Touchstone declares its scope as a ladder address span — the lattice gives the corpus the address system it never had.

Threads are **addressed by their span** across rungs — which requires:

## THE ADDRESS SCHEME (provisional, rulable)

Any unit or thread span gets a canonical address: `IP.form.act.sequence.scene.beat`, truncated to depth.

- `OXO.primary` — the storyform (R5)
- `OXO.primary.M2` — Movement 2 (R4)
- `OXO.primary.M2.q3.s12` — sequence 3, scene 12 (R3/R2)
- `OXO.primary.M2.q3.s12.b4` — beat (R1)
- Thread span: `tori.arc[OXO.primary.M1–M6]`

Tree addresses (`SPINE.Lx`) locate *concepts*; ladder addresses locate *instances*. A library source keys to tree addresses; a manuscript unit keys to ladder addresses.

**One address (IF-01-08-15; IF catalog call 1, ruled 2026-10-05).** The 08 time code (`M2 · Q1 · S04 | 012.3.2`, 08 §The address) is the one address for anything dated, in any system. This scheme maps onto it: movement `M<n>` → `M<n>`, sequence `q<n>` → `Q<n>`, scene `s<nn>` → `S<nn>`, beat `b<n>` → the `bar.beat` after the `|`. `IP.form` names the story, and the story's tracking file carries it, not the code. So `OXO.primary.M2.q3.s12` reads `M2 · Q3 · S12`.

## LADDER × LIBRARY

`feeds:` assignments for this limb: Coyne 0236 → R2/R3 (and the fractal rule) · McKee 0175 → R1/R2 · Alderson 0274, Munier 0154, Dunne 0062, Hall 0281 → R2 · Aronson 0188, Frayne 0228 → R3 · Yorke 0127, Dramatica 0089 → R4 · the spine → R5 · Mittell 0565 → R6/R7 · McErlean 0126 → R7 · Collaborative Worldbuilding 0067 → R8.

**Interfaces.** Read by 00 (IF-00-01-01): the pattern library takes R1–R8 as the values of each pattern's Scales field.

## OPEN

- **"Arc = thread, never a container"** — provisional house ruling, awaiting Chief.
- ~~**Address notation** — provisional (`IP.form.M.q.s.b`), awaiting Chief.~~ ✅ ruled 2026-10-05 (IF catalog call 1): the 08 time code is the one address; this scheme maps onto it.
- **Movement↔Signpost mapping table** (OXO: 6 movements × 4 signposts ×4 throughlines) — plot_systems work, flagged.
- **IP-level / cross-IP meta-forms** — architecturally supported, not designed.
- ~~**SCENE CARD notation** — slot reserved at R2~~ ✅ delivered same session with Module 2: [../03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md).

## Version history

- **1.0.0 — 2026-08-25.** Module 1 of the lattice, delivered on Chief's clear: eight rungs with completion tests, containers-vs-threads doctrine, four series patterns, address scheme, library keying.
- **1.0.1 — 2026-10-04.** BOLO 100 TOUCH BATCH 1, Chief "REC.": field renamed (TS-B3); constraint-check prose swapped to Touchstone (TS-B4); front-door line (TS-B10).
- **1.1.0 — 2026-10-05.** BOLO 102 stage 2 (Chief: "My word"): the address scheme maps onto the 08 time code (call 1); R8 points at the 05 catalog (call 3); the breach record lands in 08 §9A (call 6); the thematic motif thread names 06 (call 2); "scale ladder" is R1–R8 only (call 10); interfaces line for 00.
