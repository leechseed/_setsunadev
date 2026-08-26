---
type: ssot_01_narrative_frameworks
category: scale_ladder
version: 1.0.0
last_updated: 2026-08-25
applies_to: [OVEREXITOUT, all future IPs, BVX-LEARN keying]
status: canonical — Module 1 of the lattice, delivered on Papi's clear 2026-08-25
purpose: "THE SCALE LADDER — the container hierarchy from beat to universe: what each unit IS, its completion test, its address, and how multiple stories nest inside one series. Lattice limb 1 of 4."
dependencies: ["ssot_01_story_spine_comparative_tree", "ssot_02_dramatica_integration_protocol"]
trunk: BLACK
---

# 📐 SSOT: THE SCALE LADDER — from beat to universe

**What this is:** the container hierarchy of narrative. The spine says what a story IS; the ladder says **what size things come in and how they nest** — the answer to "scene → sequence → arc → story → stories within one large series." Every unit gets: a definition, a **completion test** (what makes one whole), its governing system, and holdings.

**The core conceptual move — CONTAINERS vs THREADS.** The ladder's rungs are *containers*: units of presentation with boundaries. **Arcs are not a rung — arcs are *threads*:** tracked lines of change (character arc, setting arc, relationship arc, thematic motif) that run *through* containers at any span. TV vocabulary blurs this ("story arc" as a container of episodes); the house keeps it clean: **containers hold, threads change.** *(Provisional ruling — flagged for Papi; matches the Weiland arc vocabulary already in the library.)*

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
- **Holdings:** Collaborative Worldbuilding (0067 — multi-author canon management) · the worldbuilding shelf.

---

## THREADS — what runs through the containers

A thread is a tracked line of change with a span, not a boundary:

| Thread | Tracks | Span it typically runs |
|---|---|---|
| **Character arc** | Resolve line — the MC's Change/Steadfast progression | R5, visible per-scene |
| **Setting arc** | a place's state over time (Module 2 builds this) | any — scene to universe |
| **Relationship arc** | the RS throughline's growth | R5; braids across R6 forms |
| **Thematic motif** | an Issue/Counterpoint recurrence | any |
| **Trope instance** | a register entry playing out (lattice trope register) | any |

Threads are **addressed by their span** across rungs — which requires:

## THE ADDRESS SCHEME (provisional, rulable)

Any unit or thread span gets a canonical address: `IP.form.act.sequence.scene.beat`, truncated to depth.

- `OXO.primary` — the storyform (R5)
- `OXO.primary.M2` — Movement 2 (R4)
- `OXO.primary.M2.q3.s12` — sequence 3, scene 12 (R3/R2)
- `OXO.primary.M2.q3.s12.b4` — beat (R1)
- Thread span: `tori.arc[OXO.primary.M1–M6]`

Tree addresses (`SPINE.Lx`) locate *concepts*; ladder addresses locate *instances*. A library source keys to tree addresses; a manuscript unit keys to ladder addresses. Both provisional until Papi rules notation.

## LADDER × LIBRARY

`feeds:` assignments for this limb: Coyne 0236 → R2/R3 (and the fractal rule) · McKee 0175 → R1/R2 · Alderson 0274, Munier 0154, Dunne 0062, Hall 0281 → R2 · Aronson 0188, Frayne 0228 → R3 · Yorke 0127, Dramatica 0089 → R4 · the spine → R5 · Mittell 0565 → R6/R7 · McErlean 0126 → R7 · Collaborative Worldbuilding 0067 → R8.

## OPEN

- **"Arc = thread, never a container"** — provisional house ruling, awaiting Papi.
- **Address notation** — provisional (`IP.form.M.q.s.b`), awaiting Papi.
- **Movement↔Signpost mapping table** (OXO: 6 movements × 4 signposts ×4 throughlines) — plot_systems work, flagged.
- **IP-level / cross-IP meta-forms** — architecturally supported, not designed.
- **SCENE CARD notation** — slot reserved at R2; delivered with Module 2 (needs setting-state fields).

## Version history

- **1.0.0 — 2026-08-25.** Module 1 of the lattice, delivered on Papi's clear: eight rungs with completion tests, containers-vs-threads doctrine, four series patterns, address scheme, library keying.
