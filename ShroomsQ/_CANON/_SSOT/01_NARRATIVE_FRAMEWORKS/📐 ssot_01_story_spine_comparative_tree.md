---
type: ssot_01_narrative_frameworks
category: story_spine
version: 1.0.0
last_updated: 2026-08-25
applies_to: [OVEREXITOUT, BVX-LEARN, all future IPs]
status: canonical — spine ruled by Papi 2026-08-25 (comparative tree, Dramatica canonical + rivals mapped)
purpose: "THE STORY SPINE — the canonical tree of what makes a story. The reference Papi designs IPs against, and the keying structure the BVX-LEARN library (CRE/LIT holdings) organizes onto. Front door to the BVX reference system."
dependencies: ["ssot_02_dramatica_integration_protocol", "oxo-storyform (populated instance)"]
trunk: BLACK
---

# 📐 SSOT: THE STORY SPINE — the comparative tree of what makes a story

**What this is:** the single canonical answer to "what are the components of a story." Dramatica is the ruled spine (it is the only model that is a complete tree rather than a list); every rival model is mapped onto it as a lens. This doc is (a) the design reference for making IPs, (b) the keying structure the library organizes against, (c) the trunk the multimedia ingestion (BOLO 15) will later feed.

**Division of labor (from the integration protocol, canon):** Dramatica = the narrative structure engine — the argument and each character's mechanical role in it. It does **not** produce plot events, psychology, or presentation — those belong to plot_systems, the 12-Layer Database, and Character Astrology. The spine below covers what a story IS; the house systems dramatize and flesh it.

---

## THE TREE

### L0 · What a story is — the root claim

**Dramatica:** a story is a **Grand Argument** — a complete argument, made through a single Story Mind, that a particular approach to a problem leads to success or failure, and is worth it or not. Everything below the root exists to make that argument airtight from every angle.

| Rival root claims | |
|---|---|
| Aristotle | mimesis of a complete action (plot primacy) |
| Egri | proof of a premise ("X leads to Y") — the direct ancestor of the Grand Argument |
| McKee | character revealed through choice under pressure; the controlling idea |
| Storr / Cron (neuro school) | a simulation the brain runs to learn; models the *audience*, not the artifact |

### L1 · The four throughlines — one problem, four perspectives

The argument is complete because the same problem is examined from all four seats:

| Throughline | Perspective | Rival vocabulary |
|---|---|---|
| **OS** — Overall Story | THEY — the problem among everyone | "the A-plot," McKee's arch-plot, the external genre (Coyne) |
| **MC** — Main Character | I — the problem from inside one skin | the hero's journey (Campbell/Vogler models ONLY this line) |
| **IC** — Influence Character | YOU — the perspective that pressures the MC to change | mentor/shadow/love interest (mis-typed as cast roles by most rivals); McKee's Character (BVX.0064) used for the house IC derivation |
| **RS** — Relationship Story | WE — the argument between MC and IC | "the B-story" (Snyder), the internal genre (Coyne) |

**No rival model has all four.** Most collapse MC+OS and treat IC/RS as subplot. This is the single largest structural advantage of the spine.

### L2 · The structural nesting — Domain → Concern → Issue → Problem

Each throughline descends four levels; each level is a **quad** (four elements in dynamic tension — pairs of pairs, not lists):

| Level | Count | What it fixes |
|---|---|---|
| **Domain** (Class) | 4 | where the problem lives: **Situation** (Universe — a fixed external state) · **Activity** (Physics — a problematic doing) · **Fixed Attitude** (Mind — a stuck mindset) · **Manipulation** (Psychology — a broken way of thinking) |
| **Concern** (Type) | 16 | what the throughline is *about* (e.g., Situation → The Past / Progress / The Future / The Present) |
| **Issue** (Variation) | 64 | the thematic axis, always with a **Counterpoint** (its dynamic pair) |
| **Problem** (Element) | 64 unique | the atomic engine: **Problem / Solution / Symptom (Focus) / Response (Direction)** |

Each throughline claims one Domain (all four always in play, one per throughline — the OXO §9 rotation is an instance of this exclusivity). The structure chart itself is held: **BVX.0091**.

### L3 · The story dynamics — the eight switches

Structure says where the problem lives; dynamics say how the story *moves* and how it *ends*:

| Dynamic | Values | OXO instance (canon) |
|---|---|---|
| Resolve | Change / Steadfast | Change |
| Growth | Start / Stop | Stop |
| Approach | Do-er / Be-er | Do-er |
| Problem-Solving Style | Linear / Holistic | Linear |
| Driver | Action / Decision | Action |
| Limit | Optionlock / Timelock | Optionlock |
| Outcome | Success / Failure | Failure |
| Judgment | Good / Bad | Good |

**Outcome × Judgment is the ending matrix:** Success/Good (triumph) · Failure/Good (**personal triumph** — OXO's shape) · Success/Bad (hollow victory) · Failure/Bad (tragedy). Weiland's arc taxonomy (positive / flat / negative) is this matrix plus Resolve, renamed.

### L4 · Plot — the argument dramatized in time

- **Static appreciations (8):** Goal · Consequence · Cost · Dividend · Requirements · Prerequisites · Preconditions · Forewarnings.
- **Progressive:** each throughline runs **4 Signposts + 3 Journeys** = a fixed 4-act order per throughline (16 signposts across the form); **Drivers** (action or decision) turn the acts.
- **Below the spine's floor:** scenes, sequences, beats — the storyform constrains what plot must accomplish; the events themselves are authored in plot_systems (out of scope here, per the integration protocol).

| Rival plot models → where they land | |
|---|---|
| Three-act (Field) | act turns ≈ Drivers; models the OS progressive skeleton only |
| Save the Cat (Snyder/Brody) | 15 beats = a *timed commercial template* over the signpost layer |
| Hero's journey (Campbell/Vogler) | stations ≈ MC-throughline signpost sequence wearing mythic dress |
| Five acts (Yorke) | fractal act logic; change-as-universal ≈ Resolve generalized |
| Story Grid (Coyne) | five commandments (inciting → turn → crisis → climax → resolution) recur fractally scene → sequence → act → global; the scene-level grammar the spine doesn't specify |
| McKee | gap between expectation and result; value charge per scene — the beat-level dramatization engine |
| Propp / plot genotypes (Murphy) | function sequences = the signpost grammar's folk ancestor |

### L5 · Character — functions before persons

- **The 64 elements** distribute across the cast in four quads of quads: **Motivation · Methodology · Evaluation · Purpose** — every element held by someone, so the Story Mind is complete.
- **The 8 archetypes** (Protagonist · Antagonist · Guardian · Contagonist · Reason · Emotion · Sidekick · Skeptic) are pre-bundled element sets; complex characters are custom bundles.
- **Protagonist ≠ MC, Antagonist ≠ IC** — function and perspective are independent axes (the spine's second-biggest advantage over rivals).
- **House binding:** L12_FUNCTION carries `dramatica_archetype` · `mc_problem_element` (RULED 8/24) · methodology/evaluation/purpose elements · dynamics; L12_DRAMATICA_EXTENDED carries the deep cells. Persons (psychology, body, sexuality, origin) are L1–L11 + Character Astrology — **downstream of the spine, never in it.**

| Rival character models → where they land | |
|---|---|
| Egri | three dimensions (physiology/sociology/psychology) = proto-L1–L11, not spine; unity of opposites ≈ Problem/Solution pairing |
| Truby | character web = element distribution seen socially; moral argument ≈ theme levels |
| Vogler | archetype cast ≈ the 8 archetypes with mythic names |
| Weiland (Creating Character Arcs) | arc mechanics = Resolve × ending matrix applied to the MC line |
| McKee Character (BVX.0064) | role/cast design; already consumed by the house for the IC derivation |

### L6 · Theme — the argument's value layer

Not a "message" bolted on: theme is **structural position**. Issue vs Counterpoint (the 64-level pair) argued through the throughline; Problem vs Solution at the atomic level; Outcome + Judgment pass the verdict. McKee's controlling idea = OS Problem/Solution + Outcome compressed to a sentence; Egri's premise = the same, stated up front; Weiland's theme book = the craft of dramatizing it.

### L7 · Genre, medium, audience — the outermost ring

- **Dramatica's own stance:** genre = audience appreciations (arena, style, feel) — thin, the model's weakest ring.
- **Coyne's genre clover + obligatory conventions** and **Truby's Anatomy of Genres** are the strong holdings here: genre as reader-contract (conventions owed) and as moral-argument tradition respectively. Snyder's genre wheels = the commercial compression.
- **Storyforming vs storyencoding vs storyweaving vs reception** — the spine's four production stages: decide the argument → clothe it in subject matter → order its exposure → the audience runs it. The library's neuro shelf (Storr, Cron) explains stage four.

---

## THE SETTING TOUCHPOINT MAP — RULED 2026-08-26

**The ruling:** setting stays an **entity** (the 03 domain), never a spine level — and this map answers the traditional grouping (plot/character/setting/theme as siblings) with links instead of membership. The plain version: the old textbooks put setting on the ingredient list; the lattice makes it a *person* — a place has its own 12-layer sheet, changes over time, and can be compared against characters. A bullet point can't do any of that. This map says where the person stands when you're at each spine level:

| Spine level | Where setting plugs in |
|---|---|
| **L2 Nesting** | S12 FUNCTION — a load-bearing place *embodies* a throughline's Domain (DCUS = OS Situation/The Past) |
| **L3 Dynamics** | S11 VECTOR — a place's trajectory can run the ending's geometry (DCUS collapse = the Failure/Good corridor) |
| **L4 Plot** | scene cards (setting + state per scene) · setting states keyed to acts · the setting arc as a plot thread |
| **L5 Character** | the collision diagonal — Lx × Sx (Module 5); C×Situation transits fire through place-states |
| **L6 Theme** | the **Argue** function mode — the place makes the argument in matter |
| **L7 Genre** | **genre-setting contracts** — the join tradition half-sees: "Southern Gothic," "western," "space opera" are genres that ARE setting promises |

## THE BRANCHES — first layer down (breadth pass, RULED + delivered 2026-08-26)

Each level's first sub-layer plus its starter shelf (house holdings + library). The deepening doctrine, proven by precedent: **a branch that outgrows its shelf becomes a domain** — L5 already did (→ 02), Setting did (→ 03), and L4 Plot is next. Full source sweeps: BOLO 18; **stage 1 banked** → [📐 ssot_01_spine_house_inventory.md](📐%20ssot_01_spine_house_inventory.md), the whole house corpus keyed by level. ⚠️ **Numbering collision surfaced by the sweep:** an empty `03_PLOT_SYSTEMS/` was already reserved before `03_SETTING_SYSTEMS/` was stood up (and `04_STYLE_GUIDES/` exists empty) — domain numbers await Papi's ruling.

### L0 · Root — theories of what story is
**Branches:** argument theory (Dramatica/Egri lineage — the ruled position) · mimesis theory (Aristotle) · audience-simulation theory (the neuro school — explains reception, not structure) · myth/transmission theory (Campbell).
**Shelf:** BVX.0089 · 0603 · 0232 · 0257 · 0616 · *Egri + Poetics = acquisition gaps.* House: this doc; the BVX four-domains artifact (answer-first doctrine).

### L1 · Throughlines — the four seats, each its own anatomy
**Branches:** OS anatomy · MC anatomy · IC anatomy (impact mechanics — the BVX.0064 derivation method is house canon) · RS anatomy (+ the composite-chart join, Module 5) · perspective theory (I/you/they/we) · cross-form roles (a character MC here, IC there — R6).
**Shelf:** 0064 (distilled) · 0193. House: oxo-storyform §§2–6 · victoria-midnight · the Anna IC derivation · integration protocol (binding records).

### L2 · Nesting — the chart itself
**Branches:** the four Domains, one node each (with their 4 Concerns) · quad theory (pairs-of-pairs mechanics) · Issue/Counterpoint mechanics · the atomic quad (Problem/Solution/Symptom/Response) · chart navigation.
**Shelf:** 0089 · 0090 (the Dictionary) · **0091 — the structure chart, this level's literal map.** House: oxo-storyform §9 (a fully populated descent).

### L3 · Dynamics — the eight switches, one node each
**Branches:** Resolve · Growth · Approach · Style · Driver · Limit · Outcome · Judgment · the ending matrix · the arc-taxonomy translation (positive/flat/negative = matrix + Resolve).
**Shelf:** 0071/0072 (Weiland arcs) · 0127 (Yorke, change-as-universal). House: storyform §1 (the ruled instance with rationales).

### L4 · Plot — the richest branch; next domain candidate (plot_systems, 04)
**Branches:** static appreciations · signposts & journeys · drivers & act turns · act theory (3/4/5-act compared) · sequence method · scene grammar (five commandments + value turn — the ladder R2/R3 join) · beat mechanics · **the Movement↔Signpost mapping (standing flag — lands here)** · plot templates as instances (StC beats, monomyth stations) · pacing of events (T4's story-side twin).
**Shelf:** 0175 · 0236 · 0154 · 0226 · 0274 · 0238 · 0188 · 0092 · 0228 · 0163/0164 · 0127 · 0105 · 0244. House: plot_sequence.TXT + story_engine_settings.TXT (engine exports) · the Six Movements sources · Character Astrology Cat 10 (lifecycle) + Cat 13 (transit firing).

### L5 · Character — already a domain
**Branches:** → **`02_CHARACTER_SYSTEMS/` is this level's branch-down**: archetypes/64 elements · the 12-layer stack · the DAI (Dramatica→astrology derivation) · state architecture · vertical slice · collision Cat 11.
**Shelf:** 0064 · 0071/0072 · 0193 (character web) · *Egri gap.* House: the entire 02 domain + victoria-midnight (the worked instance).

### L6 · Theme — the value layer
**Branches:** premise lineage (Egri → controlling idea) · Issue/Counterpoint argumentation · value spectrums (Coyne) · moral argument (Truby) · theme-craft (Weiland) · **the invariants join — `cost_and_meaning` is theme with enforcement teeth (the Law).**
**Shelf:** 0289 · 0193 · 0236 · 0175. House: DOCTRINE-0 · the storyform's Judgment rationale.

### L7 · Genre & Audience — the outer ring
**Branches:** genre as reader-contract (conventions owed) · genre as moral tradition · commercial compression (wheels/beats) · audience appreciations · reception neuroscience · **genre-setting contracts (the touchpoint)** · seriality as TV-genre poetics · the four production stages.
**Shelf:** 0191 (Anatomy of Genres) · 0236 + 0103 (Story Grid + Four Core) · 0163 · 0232 · 0257 · 0554 · 0565. House: the Southern Gothic register ruling (DCUS) · medium grammars doc (M3).

## THE RIVAL MAP — one row per model

| Model | Holdings | What it actually models | Verdict vs the spine |
|---|---|---|---|
| **Dramatica** (Phillips/Huntley) | BVX.0089 · 0090 · 0091 + house SSOT | the whole tree | **CANONICAL SPINE** |
| Aristotle, *Poetics* | BVX.0603 (guidebook only — ⚠️ primary text not held) | first taxonomy: plot·character·thought·diction·melody·spectacle | root ancestor; OS-biased |
| Egri, *Art of Dramatic Writing* | ❌ **NOT HELD — GAP** | premise-as-proof; character dimensions | Grand Argument's direct ancestor |
| Campbell / Vogler | BVX.0616 · 0244 · 0098 (+ mythology corpus 0110–0112, 0823–0841) | MC throughline in mythic dress | one line mistaken for the whole |
| McKee (*Story* · *Character* · *Action*) | BVX.0175 · 0064 · 0050 · 0174 | scene/beat value mechanics; controlling idea; cast design | the beat-level engine below the spine's floor |
| Truby (*Anatomy of Story* · *of Genres*) | BVX.0193 · 0191 | 22-step merged MC/OS line; character web; moral argument; genre traditions | best rival synthesis; no IC/RS separation |
| Field / three-act | ❌ not held directly (covered via Aronson 0188 · Fink 0092 · Frayne 0228) | OS plot skeleton | subset of L4 |
| Snyder / Brody | BVX.0163 · 0164 | timed beat template; commercial genre wheels | template, not theory |
| Coyne / Story Grid | BVX.0236 · 0049 · 0103 | fractal scene grammar; genre conventions; editor's diagnostics | strongest below-the-floor + L7 complement |
| Yorke, *Into the Woods* | BVX.0127 | fractal five-act; change-as-universal | L3/L4 corroboration |
| Weiland (7 vols) | BVX.0046 · 0071 · 0072 · 0146–0148 · 0182 · 0183 · 0271 · 0289 | arcs, outlining, structure, theme — craft translation layer | the applied workbook shelf |
| Storr / Cron | BVX.0232 · 0257 | audience neuroscience | explains WHY the spine works; models the reader |
| Propp lineage | BVX.0105 (Murphy, plot genotypes) | function-sequence grammar | signpost ancestor |
| Mittell, *Complex TV* | BVX.0565 | seriality, episodic architecture | maps to nested storyforms (integration protocol Pattern 1) |

**Acquisition gaps (BVX.1107+ candidates):** Egri *The Art of Dramatic Writing* · Aristotle *Poetics* (primary) · Field *Screenplay* (historic completeness; model already covered).

---

## THE HOUSE LAYER — how the spine is wired in

- **Populated reference instance:** [oxo-storyform.md](../../../../_CANON_NODES/oxo-storyform.md) — storyform v2.0, §9 engine form canon. Read the tree abstract here, then see it filled there.
- **Character pipeline:** spine → Dramatica ingest → L12 binding → Character Astrology → 12-Layer → Vertical Slice (per the integration protocol; unchanged by this doc).
- **Library keying (the Zotero concern):** every CRE/LIT source gets a spine address via the locked `feeds:` field — vocabulary: `feeds: [SPINE.L4]` (levels L0–L7; optional node path e.g. `SPINE.L2.OS.concern`). Rival-map rows above are the first 40+ assignments. **Provisional notation — usable now, rulable later.**
- **plot_systems** (future domain): owns everything below L4's floor — scenes, beats, sequences. The spine constrains; it never authors.
- **BOLO 15** (multimedia ingestion, seed): non-book media enter by the same addresses when built.

## THE LATTICE — the spine's four limbs (RULED 2026-08-25)

The spine covers the STRUCTURE axis. Papi ordered the full milieu same session; four sibling modules grow off this trunk, delivered in ruled order, one module per session (same-session continuation on Papi's call):

> **Standing doctrine (Papi, 2026-08-26): the lattice is IP-agnostic — built to create ANY story. The Outliers (OXO) is the test bed: the guinea-pig instance every module validates against, not the lattice's owner.**

| # | Limb | Doc | Status |
|---|---|---|---|
| 1 | **THE SCALE LADDER** — beat → universe nesting; containers vs threads | [📐 ssot_01_scale_ladder.md](📐%20ssot_01_scale_ladder.md) | ✅ delivered 2026-08-25 |
| 2 | **THE SETTING SYSTEM** — character-grade place: taxonomy → schema → DCUS instance (B→A→instance, RULED) | [../03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md) | ✅ delivered 2026-08-25 |
| 3 | **THE TEXTURE LAYER** — the discourse side: the Ten Questions of the Telling, craft translation grid, TELLING PROFILE | [📐 ssot_01_texture_layer.md](📐%20ssot_01_texture_layer.md) | ✅ delivered 2026-08-26 |
| 4 | **THE MEDIUM GRAMMARS** — ten channel contracts; story-side survives adaptation, texture re-instruments per medium | [📐 ssot_01_medium_grammars.md](📐%20ssot_01_medium_grammars.md) | ✅ delivered 2026-08-26 — **THE LATTICE IS COMPLETE**; M6–M8 scaffolds await BOLO 16 |

**Cross-cutting, ruled same session:**
- **THE COLLISION ENGINE — Module 5, BUILT 2026-08-26** ([📐 ssot_01_collision_engine.md](📐%20ssot_01_collision_engine.md)): generalized synastry over the lattice — C×C (Cat 11 activated) · C×S (the mirror diagonal) · C×Situation (Cat 13 transits) · C×G. Proven on Tori×DCUS, twelve rows.
- **THE CONSTRAINT LAYER — narrative invariants (wired 2026-08-25, break-break).** Invariants are not a level of the tree — they are the prescriptive register *over* the whole lattice: constraints that hold at every scale (DOCTRINE 0, meta-rule IV). Governance: [DOCTRINE-0-INVARIANTS.md](../../../../DOCTRINE-0-INVARIANTS.md) (v0.1, **awaiting ratification**). The lattice's contribution: **scope gets a canonical address** — universe-scoped (Layer 0 Invariants 1–5) · IP-scoped (Invariants of Power) · story-scoped (`narrative_invariant`, e.g. `cost_and_meaning`) · movement-scoped (Six Movements set) · place-scoped (Ecclesial Laws → S12) · character-scoped (per-character sets, Tori ×4). Enforcement rides the ladder's completion tests. Polarity vs tropes: **tropes describe, invariants forbid.** Rename ruling (Tenet/Ethos leading) was gated on decision #3 — **#3 executed 8/24, the gate is open.**
- **Trope register** — not a limb; tropes are named recurring patterns keyed to lattice addresses. TV Tropes: hand-picked articles distilled to house-vocabulary summaries (no mining, no full ingestion) — BOLO 15.
- **Domain lexicons** — subject-matter shelves (not tree nodes) keyed to the setting schema. **Starter shelf RULED: weaponology (seed: MIL's 46) · food · cars**; grows as tagging hits.
- **TTRPG scaffolding** — feeds Setting (the sourcebook/gazetteer format is a candidate setting-slice notation) as well as Mediums.

## OPEN

- Spine-address notation (`SPINE.Lx`) — provisional, awaiting Papi's ruling.
- Egri / Poetics / Field acquisitions → BVX.1107+ queue.
- Distills beyond BVX.0064: *Story* (0175), *Anatomy of Story* (0193), *Story Grid* (0236) are the highest-leverage next reads for the tree.
- THE GAP (3,768 z-lib favorites, unindexed) — story-craft holdings inside it unknown; the spine addresses them at ingest.

## Version history

- **1.0.0 — 2026-08-25.** Authored on Papi's clear (boresight chain closed same session): comparative tree, Dramatica canonical, 14 rival models mapped, holdings + gaps recorded, library keying proposed.
