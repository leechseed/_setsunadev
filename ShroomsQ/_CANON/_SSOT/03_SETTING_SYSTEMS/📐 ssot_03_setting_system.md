---
type: ssot_03_setting_systems
category: setting_system
version: 1.0.0
last_updated: 2026-08-25
applies_to: [OVEREXITOUT, all future IPs]
status: canonical — Module 2 of the lattice, delivered on Papi's clear 2026-08-25; layer names provisional pending Papi's ruling
purpose: "THE SETTING SYSTEM — character-grade place: the taxonomy of what setting IS, the 12-layer SETTING SLICE schema (mirror of the 12-Layer Character Database), the SCENE CARD notation, and the DCUS starter instance as proof."
dependencies: ["ssot_01_story_spine_comparative_tree", "ssot_01_scale_ladder", "ssot_02_character_astrology_12_layer_mapping (mirrored)", "delta-coast-ultra-school (first instance)"]
trunk: BLACK
---

# 📐 SSOT: THE SETTING SYSTEM — place at character grade

**What this is:** setting promoted from backdrop to system — built B→A→instance per Papi's ruling: the **taxonomy** (what setting is), the **SETTING SLICE** (a 12-layer schema instanced per place, the architectural twin of the 12-Layer Character Database), the **SCENE CARD** (the notation slot reserved at ladder R2), and **DCUS instanced** as the proof of rig.

**Root claim:** setting is the **pressure field** — the total state of the world at a story address, exerting force on every unit of the ladder. In spine terms: setting is where the argument becomes matter — a Domain embodied. A place that pressures nothing is scenery, not setting.

---

## PART B · THE TAXONOMY — four axes

### Axis 1 · SCALE — places nest (rhymes with the ladder's 8 rungs)

spot → room → site → locale → settlement → region → world → cosmos

Every slice declares its scale class and its parent/child places. Address form: `DCUS.campus.hall3.room12`. A scene (ladder R2) plays on some span of setting scale exactly as it sits at some ladder address.

### Axis 2 · STRATA — what a place is made of

The twelve layers of the slice (Part A). Derived from the holdings: Buckham's active-setting functions, the worldbuilding shelf's category sets (Kobold/GURPS gazetteer structure — the TTRPG scaffolding Papi called), narratology's space/description theory (Bal, Chatman).

### Axis 3 · FUNCTION — what setting DOES (Buckham-derived deployment modes)

| Mode | The setting is... |
|---|---|
| **Anchor** | orienting — reader knows where/when they stand |
| **Characterize** | revealing — the room tells who lives in it |
| **Pressure** | opposing — obstacle, constraint, danger |
| **Mood** | emotional weather — valence before a word of dialogue |
| **Argue** | thematic — the place makes the story's argument in matter |
| **Afford** | action surface — what the space permits/forbids (fight, chase, hide; games call it level design) |

A scene deploys one or two modes deliberately; all six at once is noise. The SCENE CARD records which.

### Axis 4 · TIME — baseline and states (the setting arc)

A slice is the **baseline**; **states** are dated overlays keyed to ladder addresses. The *setting arc* (thread, Module 1) is the sequence of states: `DCUS[M1] → DCUS[M4]`. Mirrors the character state architecture in 02. This is how a place "evolves over the plot."

---

## PART A · THE SETTING SLICE — twelve layers, mirror of the character stack

Same architecture as the 12-Layer Character Database: surface → depth → structural function, S12 fed independently from the storyform exactly as L12 FUNCTION is fed from the Dramatica ingest. **Layer names are house coinage — provisional, awaiting Papi's ruling.**

| Layer | Name | Holds | Mirrors |
|---|---|---|---|
| **S1** | **BODY** | physical fabric: geography, terrain, architecture, dimensions, materials, layout | L1 CORE |
| **S2** | **WEATHER** | climate, seasons, light, temperature, atmosphere; the place's rhythms (day/night, tides, terms) | L2 VITAL |
| **S3** | **SENSORIUM** | how it meets the senses: soundscape, smellscape, texture, palette — the presentation surface | L3 SOCIAL |
| **S4** | **LAW** | the rules that bind: governance, institutional mechanics, permission/forbiddance systems | L4 WILL |
| **S5** | **SCAR** | damage in the fabric: ruins, erasures, renames, sanded-off strata, what was demolished | L5 WOUND |
| **S6** | **ECONOMY** | what fuels it: resources, money, flows, traffic, who feeds and powers it | L6 DRIVE |
| **S7** | **FOUNDING** | origin: who built it, why, the founding stack, the deep history | L7 ORIGIN |
| **S8** | **HABIT** | attachment architecture: the patterned life — rituals, routines, belonging gradients, insider/outsider | L8 IMPRINT |
| **S9** | **ALLURE** | the place's erotics: what it promises, what draws people in, its glamour and seduction | L9 EROS |
| **S10** | **UNDERSIDE** | what it represses: hidden zones, the unspoken, basements literal and social, what surfaces under pressure | L10 SHADOW |
| **S11** | **VECTOR** | trajectory: where the place is going — bloom, rot, collapse, redemption; feeds the setting arc | L11 DESTINY |
| **S12** | **FUNCTION** | storyform binding, fed from the spine, independent of S1–S11: which throughline Domain the place embodies, its argument role, its charge — **and its `narrative_invariant` set** (place-scoped invariants, e.g. Ecclesial Laws; mirrors L12's `narrative_invariant` field) | L12 FUNCTION |

**Slice header (machinery, not a layer):** `place_id` · names/aliases (the rename lattice) · scale class · parent/child places · canon node link · state track (dated overlays per Axis 4).

**Binding rule (mirror of the character-storyform binding):** a place that embodies a throughline Domain gets an S12 record per storyform, keyed by `storyform_id`. Places without argument roles (mere locations) may run S1–S11 only — S12 empty is legal; S12 filled is what makes a setting *load-bearing*.

---

## THE SCENE CARD — the R2 notation (slot reserved in the ladder, delivered here)

One card per scene. Ten fields, one screen:

```
SCENE CARD
address:        OXO.primary.M2.q3.s12        (ladder address)
setting:        DCUS.campus.hall3 @ state M2  (slice + state)
active strata:  S3 SENSORIUM · S4 LAW         (which layers are working)
function mode:  Pressure + Mood               (Axis 3, max two)
sensorium:      3 details max                 (Buckham's telling-detail discipline)
commandments:   II / TP / CR / CL / RES       (Coyne's five, one line each)
value turn:     safety + → −                  (McKee; no turn, no scene)
duration:       scene | summary | stretch | pause | ellipsis   (Genette)
telling:        voice + focalization for this scene            (per-scene override of the Telling Profile — Module 3)
threads:        tori.arc · rs.rivalry         (what advances through this container)
invariants:     in-scope set, checked          (a breach means the scene is wrong, not the invariant)
exit state:     what is now true that wasn't  (feeds the next card)
```

The card is the working notation for plot_systems when it opens; until then it documents any scene worth pinning.

---

## THE INSTANCE — DCUS starter slice (proof of rig)

Filled entirely from existing canon ([delta-coast-ultra-school.md](../../../../_CANON_NODES/delta-coast-ultra-school.md) + storyform §9 + handoff bundle). Starter depth — full instance lives with the canon node when Movements 2–4 open.

**Header:** `dcus` · names: Delta Coast Ultra School / "DCUS" / the Ultra School / *Red Hills Academy* (legacy) / *Red Stick Creek* (founding, buried) / *Inner Spiral Academy* (pre-ruling) · scale: **site (campus)** · parent: the Middle Bands, Delta Coast, tri-state Spiral (FL/AL/GA) · role: Setting / Institutional Antagonist Vessel, Movements 2–4.

| Layer | DCUS |
|---|---|
| S1 BODY | century-old Southern prestige campus, Delta Coast; Middle-Bands address ("Inner Spiral" reverting to geography per provisional tissue) |
| S2 WEATHER | Gulf-South: heat, humidity, hurricane season; Southern Gothic light. ⚠️ **canon-thin — authorable gap** |
| S3 SENSORIUM | Southern Gothic register (ruled) — old brick and moss carrying a retrofit: Feed-linked clothing glow; the six-movement palette descent **clean → NEON-ROT** |
| S4 LAW | the Administration as depersonalized OS · Star-Rating · Sync Cult mechanics · Feed-linked clothing as enforced legibility |
| S5 SCAR | the rename lattice — **Red Stick Creek → Red Hills → DCUS**: erasure done twice; legacy students saying "Red Hills" commit a small legibility violation every time they speak |
| S6 ECONOMY | Bishop acquisition capital; prestige converted to product; the ownership war (grandfather vs son — sold for spoils *to the Bishops*) |
| S7 FOUNDING | 100+ years of private prestige; the founding name sanded to "Red Hills" a century before the Bishops arrived |
| S8 HABIT | alumni-legacy bloc vs Sync-era students; split faculty loyalties; the ritual life of the Star-Rating |
| S9 ALLURE | **the meritocratic promise** — the exact premise Tori must stop believing (Growth: Stop); flagship-Ultra prestige; the Feed's glamour |
| S10 UNDERSIDE | the first name under the second (Movement 3's forensic mode); what the rebrand-as-Boot-Sequence overwrote; the disruption→collapse skeleton |
| S11 VECTOR | the six-movement descent: clean → NEON-ROT → hunt; collapse trajectory |
| S12 FUNCTION | `storyform_id: oxo_primary_v1` — **the OS Domain embodied: Situation / The Past.** Goal = The Past, story_cost = Memories: the campus IS personal history deleted for programming space, done to a place. The rebrand is the world's Boot Sequence at institutional scale. **Invariant set: the Institutional Invariants (Ecclesial Laws)** — `THE_ADMINISTRATION.md`, place-scoped |

**The proof reads:** every layer filled from canon on the first try, one authorable gap surfaced (S2), and S12 snapped onto the storyform without force — the schema fits the house.

---

## SETTING × LIBRARY

`feeds:` for this limb: Buckham 0268/0269/0270 (Active Setting 1–3) + 0267/0056 → Axis 3 + S3 · Rozelle 0081, Hall 0288 → S3 craft · Alderson 0274 → scene card · Kobold 0458/0541, GURPS 0447, Collaborative Worldbuilding 0067 → Axis 2 strata + R7/R8 scale · Against Worldbuilding 0349 → the counter-argument (worldbuilding serves pressure, not inventory — the doc's own root claim) · Bal 0591/0596, Chatman 0167 → space/description theory (deepens in Module 3) · Once Upon a Pixel 0144, narrative-design shelf → Afford mode (environmental storytelling).

## OPEN

- **The twelve layer names** (BODY … FUNCTION) — house coinage, awaiting Papi's ruling; bench on request.
- **`03_SETTING_SYSTEMS/` placement** — new SSOT domain created this session, mirroring 02; movable on ruling.
- **S2 WEATHER for DCUS** — authorable gap, first writing target when Movements 2–4 open.
- **Setting state architecture** — dated-overlay format specced at Axis 4; full doc mirrors `ssot_02_character_state_architecture` when first needed.
- **Scene card field trial** — first real scene of OXO should run one card end-to-end.

## Version history

- **1.0.0 — 2026-08-25.** Module 2 of the lattice, B→A→instance per ruling: four-axis taxonomy, 12-layer slice mirroring the character stack layer-for-layer, scene card delivered to its reserved R2 slot, DCUS instanced as proof.
