---
type: ssot_04_fabula
category: plot_system
version: 1.6.0
tier: fabula
last_updated: 2026-10-12
applies_to: [OVEREXITOUT, EVIL CHECK, LAKAD, ASTRO7EX, all future IPs]
status: "v1.6.0 2026-10-12, S1-S7 recs taken ('take all recs'): the Aldrin Sector opens era 4; Phase I gets two ids and one edge (era 1 + era 4); the MAXWING purge comes before the AI Collapse; the ASTRO7EX Severance is the AI Collapse seen from the Moon; the Myrtle find comes after the heist; the 2090s births are ancestors (lineage); the queenpin's name goes on the name bench (BOLO 48). v1.5.0 2026-10-12, batch 4 recs taken ('take all recs', re-read against I4): era 4's first four records (AN7L's fracture, the MAXWING program, the AI Collapse, the queenpin's heist) and four Moon place stubs, all provisional; I1 I5 I10 I12, the Myrtle order and the 2090s births held for Chief; I8 void. v1.4.0 2026-10-12, I4 ruled: era 4 runs alongside era 2 on the shared 2199 clock; Vivian's story ends at the LAKAD jump; the queenpin is a separate Moon character and holds the 2091 birth. v1.3.0 2026-10-12, batch 3 closed ('take all recs'): the failed first attempt and the first-comer allies open era 1 (provisional); the era 5 ship leaves the Moon (provisional); H10 held for the research list. v1.2.2 2026-10-12, H6 revised by Chief: the land sale comes right after the 2099 Moon Severance, not before. v1.2.1 2026-10-12, Chief hand-built H4 and H6: the second generation's heir renames the place Red Hills; the land sale comes before the 2099 Moon Severance. v1.2.0 2026-10-12, batch 3 recs taken ('take all recs'): the first event records in eras 1, 3 and 5 (THE ERA SPINES); H2 H3 H4 H6 H10 and the era 5 ship held for Chief. v1.1.3 2026-10-12, recs taken ('all recommendations'): Cartel Federal is the Narco Republic's middle stage; the AI Collapse sits in era 4. v1.1.2 2026-10-12, G4 and G7 hand-built: the scrub homestead is era 1's first place; the rocket is boarded and its crew taken prisoner aboard a station made of three or four stations. v1.1.1 2026-10-12, Chief hand-built G6 G8 G10 G11: the Narco Republic's first and last names, the rocket launch opens LAKAD, the AI Collapse on the Moon, era 5 as the generation ship. v1.1.0 2026-10-12, batch 2 recs ruled ('All recommendations'): the unplaced_ id prefix, the removal's inferred cause edge, places before events in eras 1, 3 and 5, A Land Remembered as era 1's skeleton (L1-L4), the era 5 exodus note held as lineage. v1.0.1 2026-10-11, F2 and F10 carried through (ids and prose). v1.0.0 2026-10-11, batch 1 F1-F12 ruled ('Take all recs'): stories values, era-prefixed ids, location rule, 2099/2199 held as lineage, Severance after the beam, two Severances kept apart, the removal event, the Feed event, long actor names. v0.3.0 2026-10-05, BOLO 102 stage 2 (Chief: \"My word\"): the event record gains `source_kind`, `canon_source`, `produces`, `scheduled` and the 08 time code beside the calendar year; the no-calendar line is corrected. v0.1.7 2026-09-29, BOLO 91 rulings: Anna Colson's origin fabula-filled (ice-skating death → the scientist's rebuild → the scientist's attachment → the father's reclaim → the scientist's own kept copy, a second Colson with her own origin node); Tori's family origin (the trash-zone delta, not Bikini Atoll) added as L7 ORIGIN context, the car crash confirmed as her WOUND. v0.1.4 2026-09-29: BOLO 90 step 7 trial, RULED 2026-09-29, Chief: 'line up the recs' — THE WORLD CLOCK gets the `backstory` movement tag for deep pre-M1 history, `event_id` grammar `backstory_<slug>`. v0.1.3 2026-09-24: BOLO 77 wave 3, plot doc OPEN call 12 executed — sixth event record `m2_first_sync_verified` added (row 9's rating-system / 'Verified' / reach-vs-pull-out moment), sourced from oxo-scene-card-M2-row9.md rather than victoria-midnight.md; ssot_04_plot_system.md's row-9 P2/P3/P5/P9 now read it. v0.1.1 2026-09-24: all six OPEN calls RULED (Chief: \"go on all recommendations\"); the v1.1 patch landed in the state architecture. v0.1.0 draft — BOLO 77 wave 1, \"go 77\" ruled 2026-09-24; Tori-only instance, EVIL CHECK events reserved for wave 2, state architecture v1.1 patch spec ships inside this doc"
rung: standard
dependencies: ["ssot_04_plot_system", "ssot_03_setting_system", "ssot_02_character_state_architecture", "ssot_02_character_astrology_12_layer_mapping", "ssot_01_scale_ladder"]
trunk: BLACK
sources: [BVX.0591, BVX.0167, BVX.0562, "_PRIVATE/notes/apple-notes-2026.digest.md (BOLO 91, Anna Colson Conway's origin)", "_PRIVATE/notes/phone-notes-2022-2023.digest.md (BOLO 91, Tori's family origin)"]
purpose: "THE FABULA, v0.1: the universe-level world-time layer beneath 04's syuzhet doc, one shared timeline for OXO and EVIL CHECK, the EVENT RECORD schema, typed CAUSAL EDGES, THE WORLD CLOCK, the ORIGIN MOMENTS rule for the twelve character layers, the Tori-only instance, and the state architecture v1.1 patch spec."
---

# 📐 SSOT · THE FABULA · world time

**What this is:** the fourth top-layer model's world-order half, split out from the told-order half that already lives in [📐 ssot_04_plot_system.md](📐%20ssot_04_plot_system.md). One fabula, one world timeline, sits under both stories in the shared universe: OXO (OVEREXITOUT) and EVIL CHECK, a second story in the same world. Bal's three-layer stack names the seam directly: "A narrative text is a text in which an agent or subject conveys to an addressee... a story in a medium... A story is the content of that text and produces a particular manifestation, inflection, and 'colouring' of a fabula. A fabula is a series of logically and chronologically related events that are caused or experienced by actors." ([[BVX.0591]], Bal 2017: 5) The syuzhet doc is the told order; this doc is the world order the syuzhet doc reads from.

**What it owns:** world time (events in their own logical and chronological sequence, independent of how any one story tells them); the EVENT RECORD schema; typed CAUSAL EDGES between events; THE WORLD CLOCK (eras, reach and extent, fuzzy and unknown dates, iterative events); the character ORIGIN MOMENTS rule, which of the twelve layers need a dated fabula event and which do not.

**What it does not own:** the told order (04's syuzhet doc owns P11 TIME, order_told vs order_happened, and reads this doc for order_happened); the pattern layer across events (wave 2's trope graph owns that, walking inside the storyform's signposts, Propp's functions "understood as an act of a character, defined from the point of view of its significance for the course of the action" (Propp 1968, ch.II) are that layer's job, not this one's); place itself (03, the setting system, owns where; this doc cross-references the setting doc's dated states rather than re-authoring them); the static character layers (02 owns CORE, VITAL, SOCIAL, FUNCTION; this doc supplies only the origin event for the layers that need one).

**Root claim:** a shared universe needs exactly one fabula, not one per story. Wolf's internarrative theory gives the direct warrant: "Imaginary worlds... are often transnarrative in scope, and have multiple stories occurring in them; not just nested stories, but separate stories that take place within the same world... In one sense, all the stories set in the same world can be seen as being nested within the overarching narrative of the history of the world itself." ([[BVX.0562]], Wolf 2012, ch.4) Wolf's mechanics note follows directly: "if a world's consistency is to be maintained, each additional story to be added to a world must take into account all of the narrative material already present in a world... stories are related chronologically to each other and can be arranged in a sequence, fitting together the stories' events on the timelines of the world" ([[BVX.0562]], same section). OXO and EVIL CHECK are two tellings that must fit one timeline of events, not two timelines that happen to resemble each other.

---

## MIND MODELS

**Diagram 1, the whole system on one screen.**

```mermaid
mindmap
  root((THE FABULA))
    World layer
      one timeline
      OXO and EVIL CHECK share it
      Bal's world-order events
    The Event Record
      event_id
      transition state-before to state-after
      actors and actant role
      kernel or satellite
      time reach and extent
      gap_type
      repeat flag
      stories field
      provenance and confidence
    Causal Edges
      precede
      cause
      enable
      embed
      specify
      simultaneous
    The World Clock
      eras
      fuzzy and unknown dates
      iterative events
    Origin Moments
      L5 WOUND needs one
      L7 ORIGIN needs one
      L8 IMPRINT needs one
      L9 EROS needs one
      L10 SHADOW needs one
      L1 L2 L3 L12 never need one
    Boundaries
      told order stays the syuzhet doc
      pattern layer is wave 2's trope graph
      place stays the setting system
      static layers stay the character docs
```

**Diagram 2, the handshake: fabula feeds the syuzhet, the character layers, and the setting.**

```mermaid
flowchart TD
    EV["THE EVENT RECORD<br/>event_id · transition · time (reach/extent)<br/>kernel or satellite · gap_type · stories"] --> SYZ
    EV --> CHAR
    EV --> SET
    SYZ["SYUZHET · 04 plot doc<br/>P2 driver_event · P3 value-in · P4 turn mechanism<br/>P5 value-out · P6 signpost seat · P7 reveal<br/>P9 stakes delta · P11 order_told vs order_happened"]
    CHAR["CHARACTER STATE · 02 state architecture v1.1<br/>origin_event points back to event_id<br/>state_diffs parent records the delta"]
    SET["SETTING · 03 setting system<br/>dated states on the setting arc<br/>cross-referenced only, fabula stays the source"]
```

---

## THE EVENT RECORD

**What an event is.** Bal's definition, verbatim: "An event is the transition from one state to another state, caused or experienced by actors." ([[BVX.0591]], Bal 2017: 5, 155) A state on its own is not an event; a change is (Bal 2017: 155-156). That single line is the schema's first rule: one record, one transition, never a scene or a summary label bundling several transitions.

**Kernel or satellite.** Bal narrows which transitions matter to fabula structure by two criteria beyond mere change: Choice (after Barthes, a functional event opens, realizes, or reveals the result of a choice between alternatives) and Confrontation (a functional event needs "two actors and one action... two arguments and one predicate," subject-predicate-object, both slots filled) ([[BVX.0591]], Bal 2017: 156-159). Chatman's parallel cut is kernel vs satellite: "Kernels are narrative moments that give rise to cruxes in the direction taken by events... Kernels cannot be deleted without destroying the narrative logic." A satellite "can be deleted without disturbing the logic of the plot... Satellites entail no choice, but are solely the workings-out of the choices made at the kernels." ([[BVX.0167]], Chatman 1980: 53-55) Bal's functional/non-functional split and Chatman's kernel/satellite split are the one clear cross-school agreement on what counts; every event record carries a `kernel_satellite` flag on that agreement, not on either school alone.

**Ids.** The state architecture's own gap section names the requirement directly: "the fabula must assign each event a unique `event_id`. A state record must carry the corresponding ID in `origin_event`" (state_architecture.md v1.1 gap, per PS2 wave 1 handshake). The one worked example in canon: `event_id: "m1b_crash_jebb_death"` paired to state diff `vm_m1b_post_crash`. This doc adopts `<movement>_<slug>` as the working grammar (OPEN call 3) until a formal one is ruled. The `story_beat` type that the character system uses is this `event_id` (IF catalog call 5, ruled 2026-10-05; IF-02-04-16). A PENDING or FIRED_PRE_STORY flag names its firing event by the same `event_id`, stored beside the flag state (IF catalog call 5; IF-00-04-06, IF-02-04-15).

**Time, reach, and extent.** Bal: "Events have been defined as processes. A process is a change, a development, and presupposes therefore a succession in time" (Bal 2017: ch.3 §4). Genette's pair gives the two numbers a fabula record needs per event even when only fuzzily known: reach (distance from the narrating present) and extent (span covered) (Genette 1980: 48) — both can be ranges rather than points. The 08 time code is the one address for an event's place on the grid. So `time` carries it beside the calendar year: `time_code` holds the code and `calendar_year` holds the year (IF catalog call 1, ruled 2026-10-05; IF-04-08-12).

**Gaps and iteration.** Bal: a linked series is "sometimes interrupted by a span of time in which nothing occurs — at least nothing that is narrated" (Bal 2017: 164) — silence in the telling is not the same as a gap in the world, so `gap_type` distinguishes `logged` (an event is on record) from `unknown` (nothing recorded, not the same claim as "nothing happened"). Genette's frequency axis covers iterative events, one record standing for a repeated class rather than one row per occurrence (Genette 1980: ch.3 "Frequency," p.113; Genette 1980: 53) — the `repeat` flag.

**Provenance.** Rimmon-Kenan is explicit that a story is a reconstruction, never the text itself: "Story… is not directly available to the reader… the text is the only observable and object-like aspect" (Rimmon-Kenan 2002: 3-6). When OXO and EVIL CHECK give conflicting glimpses of the same event, this doc is the adjudicated version, so every record carries a `provenance` block naming its source and a confidence level rather than silently picking one telling.

**Shared universe.** Wolf's mechanics note is the warrant for the `stories:` field: each event marks which telling(s) it is visible in — OXO, EVIL CHECK, ASTRO7EX, TREMOR CULT, LAKAD, or backstory-only (one value per story in the registry) — so every syuzhet doc can query the same table ([[BVX.0562]], Wolf 2012, ch.4).

**Source kind, canon source, products and schedule (IF catalog call 5, ruled 2026-10-05).** Four fields join the event record. `source_kind` tags the event with one of 03's five state-source categories or `character`. The five are construction, institutional, ownership, rename and seasonal. 03 reads from the tag which S-layers the event moves (IF-03-04-18). `canon_source` holds the canon-source citation that the truth check reads on every event; `provenance.source` stays the working note (IF-00-04-05). `produces` lists the `state_id`s the event yields across characters, the back-reference to each state's `origin_event` (IF-02-04-14). `scheduled` holds the 08 time code of a future state. 03's LEDGER_DUE flag fixes that state in advance. The field stays null for a past event (IF-03-04-20).

**The template:**

```yaml
event_id: "<movement>_<slug>"                 # e.g. m1b_crash_jebb_death; outside era 2 the era prefix leads: astro7ex_<slug> (F2)
transition: "<state-before> -> <state-after>" # Bal 2017: 155-156
actors:
  - actor: "<ruled long form, e.g. Anna Colson Conway, Tori Midnight>"   # F10
    actant_role: subject | object | helper | opponent  # Bal 2017: 5, 166-167
kernel_satellite: kernel | satellite          # Bal 2017: 156-159; Chatman 1980: 53-55
time:
  movement: "<Mn or Mn stage>"
  time_code: "<08 time code, e.g. M2 · Q1 · S03 | 012.3.2; null if not placed>"   # IF catalog call 1
  calendar_year: "<year where canon gives one, e.g. 2199; null if not>"          # IF catalog call 1
  reach: "<distance from story-present, a range if fuzzy>"   # Genette 1980: 48
  extent: "<span covered, point or duration>"                # Genette 1980: 48
gap_type: logged | unknown                    # Bal 2017: 164
repeat: true | false                          # Genette 1980: ch.3 "Frequency"
source_kind: construction | institutional | ownership | rename | seasonal | character   # IF catalog call 5
canon_source: "<canon-source citation the truth check reads>"                 # IF catalog call 5
produces: ["<state_id>", "<state_id>"]        # states this event yields, across characters; IF catalog call 5
scheduled: "<08 time code of a future state fixed in advance, or null>"       # IF catalog call 5; LEDGER_DUE
location: "<a 03 address, or the word GAP>"    # Bal 2017: ch.3 §5; the fabula never invents a place (F3)
stories: [OXO, EVIL_CHECK, ASTRO7EX, TREMOR_CULT, LAKAD, backstory_only]   # Wolf 2012, ch.4; one value per story in the registry (F1)
provenance:
  source: "<node file, section>"
  confidence: direct_quote | inferred | uncertain   # Rimmon-Kenan 2002: 3-6
causal_edges:
  - type: precede | cause | enable | embed | specify | simultaneous
    to: "<event_id>"
```

---

## CAUSAL EDGES

Bal's warning is the section's spine: precedence is necessary but not sufficient for causality (Bal 2017: 159). A flat "next event" chain would collapse that distinction, so every edge in the registry carries a type.

| Edge | Definition | Cite |
|---|---|---|
| **precede** | Chronological order only, no causal claim — A happened before B, nothing more | Bal 2017: 176-177; Genette's "order" |
| **cause** | A's realization produces B's occurrence — "effect succeeds cause; thus, the hero dies after the bullet strikes him" | [[BVX.0591]], Bal 2017: 159 |
| **enable** | A opens the possibility B later realizes, Bremond's virtuality phase before the event that acts on it | Bal 2017: 160 |
| **embed** | A's realization opens a second process's own possibility phase, nested rather than sequential | Bal 2017: 161 |
| **specify** | An embedded series specifies the primary series rather than causing it | Bal 2017: 162 |
| **simultaneous** | A and B occur at the same time; "some events can occur at the same time, others succeed one another" | Bal 2017: 164 |

Bal's process model behind `cause`, `enable`, `embed`, and `specify`: three phases per process, possibility/virtuality to event/realization to result/conclusion, any of which can fail to occur (Bal 2017: 159-163). An edge marked `cause` asserts all three phases fired and produced the target event; an edge marked `enable` asserts only that the possibility phase opened, not that the target event was forced.

---

## THE WORLD CLOCK

**Eras.** The setting doc's own DCUS proof gives a naming lattice with three stages, stated as a chronology, not merely a scar: "100+ years of private prestige; the founding name sanded to 'Red Hills' a century before the Bishops arrived" (S7 FOUNDING); "the rename lattice — Skeeter Creek → Red Hills → DCUS: erasure done twice" (S5 SCAR) ([📐 ssot_03_setting_system.md](../03_SETTING_SYSTEMS/📐%20ssot_03_setting_system.md)). Read as world-clock eras: **Skeeter Creek** (founding, buried, no date given), **Red Hills** (the first rename, reach roughly a century before the Bishop acquisition, extent unstated), **DCUS** (the current era, tied to the Bishop acquisition, "prestige converted to product; the ownership war — grandfather vs son — sold for spoils to the Bishops," S6 ECONOMY). No calendar date exists in these sources for any of the three transitions; this doc records reach and extent as ranges (OPEN call 5) and does not invent a year. Per OPEN call 4, the world clock cross-references these eras rather than re-authoring them as its own filled event records — the setting doc stays the one authoring surface.

**The universe eras (RULED 2026-09-29, Chief: "yes to all recommendations"; BOLO 82 boresight).** The LEECHSEED eon runs as **sequential eras with overlap allowed at the seams** (era 4 excepted: it runs alongside era 2, I4 ruled 2026-10-12) (five now: Skeeter Creek inserted as era 1 on 2026-09-29, "beyond" ⧗ as era 5), moving outward from Earth:

| Era | Story | Where | Status on this clock |
|---|---|---|---|
| **1 · the Skeeter Creek era** (RULED 2026-09-29) | ⧗ no story yet | Earth, the Delta Coast before the school was DCUS | from `skeeter_creek_backstory_skeeter_creek_founding` through the Red Hills century (`skeeter_creek_backstory_red_hills_rename`); ends at the Bishops' rebrand. First place (G4, Chief 2026-10-12: "G4 sounds good", provisional): **a scrub homestead at Skeeter Creek in the founding year**, the founding generation's, after the book's first generation (L1). **The Narco Republic rises here** ⧗ (Chief, 2026-09-29: "back it up one era"; see below) |
| **2 · the DCUS era** | OVEREXITOUT (*The Outliers*) · EVIL CHECK · TREMOR CULT | Earth, the Delta Coast | opens at `backstory_dcus_rebrand`; the only era with story event records (THE INSTANCE) |
| **3 · the LAKAD era** | LAKAD (codename) | cislunar space | opens at `lakad_first_launch`: the characters take a rocket into space, a hard break from era 2 (G8, Chief 2026-10-12: "that's where Lakad picks up. It's literally that hard break"); first place (G7, Chief 2026-10-12, provisional: "we'll figure something out"): **the rocket never arrives**. It is boarded, and the characters are taken prisoner aboard a massive station welded together from three or four space stations, post-apocalyptic in the register of Fallout 3. The station's name and owner ⧗ |
| **4 · the ASTRO7EX era** | ASTRO7EX | the Moon | **Runs at the same time as era 2** (I4, Chief 2026-10-12: "In the moon era, that takes place at the … outlier's time as … the outliers has taken place"; recs taken, "take both"): the Moon side of The Outliers' years, so its clock shares **2199**. Vivian's story ends at the jump to LAKAD ("her story kind of … ends at … whenever we go to Lakad"). The MAXWING survivor who pulls the Bitcoin heist and becomes the lunar queenpin **is not Vivian** ("that's not Vivian. That will be another character on the moon"): a separate Moon character, name ⧗. The 2091 Aldrin Sector birth belongs to the queenpin. The 2090s births (2091, 2095) move with the shared clock: ancestors or a century later ⧗. The rest of batch 4 waits in `_PRIVATE/intake/FABULA-BATCH-4.md` |
| **5 · the beyond era** ⧗ | ⧗ none yet | past the Moon | band only; named "beyond" (Chief, 2026-09-29 session 4). **The journey, not the landfall** (G11, Chief 2026-10-12, provisional: "maybe not on a new planet, but the journey to a new planet, like a generational ship"): era 5 is a generation ship's voyage toward a new planet. The Red Hills-tagged exodus note (one ship reaches a planet after 1000 years, digest.md:680) stays lineage |

**Era 1 inserted (RULED 2026-09-29, Chief: "era one will be the Skeeter Creek … it'll stay the same after"; Red Hills placed in era 1 on the same ruling).** Every later era moves down one number; their order is unchanged. The seam between 1 and 2 is the Bishops' rebrand of Red Hills Academy as DCUS.

**A Land Remembered is era 1's skeleton (RULED 2026-10-12, Chief: "i want skeeter creek to be heavilly bsed on the book A Land Remembered by Patrick Smith"; L1-L4 "All recommendations").** Patrick D. Smith's novel (1984) follows three generations of one Florida family, 1858-1968: survive the frontier, build the cattle fortune, sell the land and regret it. **L1 · translate, don't transplant:** the Delta Coast stays; the book's scrub, cattle, hurricanes and land boom become Delta Coast equivalents. **L2 · three generations span era 1:** the founding generation (survival), the Red Hills generation (the fortune), the generation that sells the land that becomes DCUS. **L3 · the skeleton, not the cast:** names and people are original; the generational arc, the frontier, the allies and the price of progress carry over. **L4 · the ending is the hinge into era 2** (provisional): the last generation's regret over the sold land is what DCUS is built on. Chief's own breakdown of the book sits in the vault (packet note M32).

**The calendar and the Moon Severance (RULED 2026-10-01, BOLO 96, Chief: "all rec"; held as lineage, F4 ruled 2026-10-11).** OXO's present is **2199**; the **Moon Severance** is **2099**, one hundred years back, in **era 1**. Both years stay on the Outliers clock only, flagged lineage. No ASTRO7EX event carries a `calendar_year`, so Vivian's 2091 stands alone. One note says the Kessler storm has stood fifty years; the 2099 to 2199 span is one hundred. That note is held as lineage, part of the PSP Fella opening (F6). The Moon colony went up in the 2050s–70s and had turned hell by the 2090s; unable to leave any other way, **the Moon cut itself off on purpose**: it detonated nukes in orbit and set off a Kessler cascade that walls Earth off from space. The wreck has been falling ever since, onto the Power Line ([WB-INS-0004](../05_WORLDBUILDING_SYSTEMS/catalog/INS/WB-INS-0004.md)). Some of the Moon's people came back down before the wall closed; their descendants survived in the trash pit and are **the Outliers**, carrying Moon-engineered radiation resistance and a sleeper mission in their blood they don't know they carry: take Earth so the Moon can come home (lineage ⧗; what the DNA does is Chief's to voice). The early Moon colony is era 1's buried secret; **ASTRO7EX (era 4) is Earth's return to the Moon**. Id: `skeeter_creek_backstory_moon_severance`. Ruled 2026-10-11 (F5): the beam comes first, then the Severance. ASTRO7EX's own "Moon Severance" (its Dramatica reports) is a separate event with its own id, `astro7ex_backstory_moon_severance`, until Chief voices a link. Source: `_CANON_NODES/outliers-moon-origin-seed.md`.

**The Narco Republic on this clock ⧗** (five scraps in the 2025 notes; nothing else is canon yet): it rises in **era 1** as one of the four regions of the Americas (the 6/20/2025 world dump: Antebellum South · Deepstate North · Outlaw West · Narco Republic; seed "the rise of the Narco Republic"), stands through **era 2** as a region on OXO's map, and by **era 4** is a mature vice economy over Central and South America (ASTRO7EX "Backdrop & Context", 5/11/2025). Era 3 is silent. Its names (Apple Notes 2025: Cartel Federal · Real Federale · Pax Cartel) and its flag (9/8/2025: the diving gold eagle, the rattlesnake on cacao, Mexican red and gold, CONSEQUENTIA REAL) wait on Chief's calls. **The name stages (G6, Chief 2026-10-12):** the final stage is **Real Federale**. The first stage is a crude joke name the founders never meant seriously, in the register of "cartel cullo … bitch, puta madre"; working name **Cartel Culo** ⧗. The arc runs from founders who were "not serious at all" to a state that is. The middle stage is **Cartel Federal** (rec taken 2026-10-12, "all recommendations"); Pax Cartel stays an alias. Order: Cartel Culo ⧗ → Cartel Federal → Real Federale.

**The two 3rd impacts ⧗ (RULED 2026-09-29, "all rec"; era 2).** The **south-pole 3rd impact** sets off a buried quantum-entangled object and wakes the Kudzu (ASTRO7EX setup note, 5/11/2025); the **ocean 3rd impact** is its pair, the **Atlantic nexus** (Apple Notes 2026: "evangelions · zakus · the kudzu zerg · pulsar · ocean 3rd impact · antarctica"). Ids: `backstory_south_pole_third_impact` · `backstory_ocean_third_impact` (tracking file `world:`). What the ocean impact wakes, and how both sit against the Deep Meridian beam, are open.

**The hinge (RULED 2026-09-29, Chief: "number two, yes"): the Deep Meridian beam.** At **Deep Meridian**, a geothermal drill front at a caldera run like a navy (its crews, the Drill Rangers, seal themselves behind rock on suicide missions), a needle probe into "the old city", a pressurized hot-water chamber, loses control and fires **a beam of radiation that punches a hole a mile wide into the sky. The beam signals the quasar that reaches the time of Vivian** (ASTRO7EX), "a century or two after" on the surface. **The Moon Severance** follows it (F5, ruled 2026-10-11). **The AI Collapse** (ASTRO7EX's Dramatica reports, `.ASTRO7EX.SYNC.JOPLIN/`) also follows it ⧗. It happens **on the Moon** (G10, Chief 2026-10-12): it turns the Moon people aggressive and set on going back to Earth, and "it happens everywhere all at once". It sits in **era 4, ASTRO7EX** (rec taken 2026-10-12, "all recommendations"): the Moon wanting Earth back is ASTRO7EX's fight, and the id keeps `astro7ex_backstory_ai_collapse`. It is a separate event from era 1's Moon Severance. In-world holidays: **Laser Core Admissions Day**, the day after **Space Laser Repentance Day**. Source: Chief's Apple Notes 2025 (BOLO 91). Ids (F2, ruled 2026-10-11): `skeeter_creek_deep_meridian_beam`, `astro7ex_backstory_moon_severance`, `astro7ex_backstory_ai_collapse`.

**Superseded, kept as history:** on 2026-02-09 Chief ruled the three "occur simultaneously… one entire eon" (`_CLAUDE_ARCHIVE_2026-08-15/conversations/2026-02-09_main-sonnet.md`). The eon still holds as the umbrella; its inside is now three eras in order. Each era's movements keep their own `Mn` dating; an era prefix (`era: skeeter_creek | dcus | lakad | astro7ex | beyond`) is read when the clock spans stories. Every `event_id` outside era 2 leads with its era prefix, like `astro7ex_<slug>` (F2, ruled 2026-10-11). Eras 1, 3 and 5 stay band-only for 1.0.0, each ⧗ stays marked, and Chief fills them by hand (F11). **Batch 2 (RULED 2026-10-12, Chief: "All recommendations").** `unplaced_<slug>` is a legal id prefix for an event with no movement yet (G1). Places come before events in eras 1, 3 and 5: Chief hand-builds one place per era before any event record enters it (G3). No event enters those eras until G4, G6, G7 and G11 have Chief's answers (G12). The era 1 to 2 seam stays the Bishops' rebrand, and `backstory_dcus_rebrand` carries no era prefix because it opens era 2 (G5). The two Severance ids stay apart (G9). The story list lives in the [story registry](../01_NARRATIVE_FRAMEWORKS/📐%20ssot_01_story_registry.md) (BOLO 82).

**Fuzzy and unknown dates.** None of the core narratology sources gives a formal null-value convention for an unknown date (a gap in the theory canon itself, not just this search); this doc's working answer is movement-relative dating — `M1`, `M2`, `M3`… — carried in each event's `time.movement` field, reach and extent filled as ranges or marked unknown rather than left blank. A calendar layer now sits beside it (IF catalog call 1, ruled 2026-10-05): `time.calendar_year` holds the year where canon gives one (OXO's present 2199, the Moon Severance 2099), and `time.time_code` holds the 08 grid coordinate. Both stay null where canon is silent, and this doc never invents either.

**Iterative events.** Genette's iterative note models a class of fabula record that is not one occurrence: "not... a single portion of elapsed time but... several portions taken as if they were alike and to some extent repetitive" (Genette 1980: 53). The `repeat` flag marks these; THE INSTANCE below carries a worked example (Tori's M2 outbursts).

**Gaps.** A `gap_type: unknown` event window is not a claim that nothing happened in the world during that span, only that nothing is on record for it (Bal 2017: 164) — distinct from a span this doc has deliberately not filled because the wave-1 instance is Tori-only (see THE INSTANCE, scope note).

**Backstory events (RULED 2026-09-29, BOLO 90 step 7 trial, "line up the recs").** Deep past with no Mn to file under — DCUS's founding lattice is the worked case ([🔮 ssot_03_setting_state_architecture.md](../03_SETTING_SYSTEMS/🔮%20ssot_03_setting_state_architecture.md) §11) — carries `movement: "backstory"` instead of an `Mn`, and its `event_id` reads `backstory_<slug>` in place of the usual `<movement>_<slug>`'s `Mn_<slug>` half. This is additive to OPEN call 3's `<movement>_<slug>` grammar (ruled 2026-09-24): `backstory` is a legal value everywhere `<movement>` would otherwise be `M1`, `M2`… for an event that precedes the story's own M1.

---

## ORIGIN MOMENTS

PS2's wave-1 extraction reads all twelve character layers against "What Is Static vs What Is Dynamic" (the state architecture doc, §3) and sorts them by whether the layer's baseline needs a dated fabula event to have formed, or whether it is static, storyform-fed, or trajectory rather than a single origin.

| Layer | Name | Needs an origin moment? | Rule |
|---|---|---|---|
| L1 | CORE | No | Static trait; "does not change within a single story arc" |
| L2 | VITAL | No | Static trait; injuries are state diffs, not a re-origin |
| L3 | SOCIAL | No | Static trait; reputation shifts are state diffs, not a re-origin |
| L4 | WILL | Optional | Derives from CORE; an origin event is needed only if WILL changes durably post-story |
| L5 | WOUND | **Yes** | "Assigned during character history entry. This is a record of what happened, not a choice" — needs a dated trigger |
| L6 | DRIVE | Optional | Derives from VITAL; origin is the character's base fuel type, not a single event |
| L7 | ORIGIN | **Yes** | Birth context and formation set starting conditions; authored from documented backstory |
| L8 | IMPRINT | **Yes** | Formative conditioning locks in through early relational events with datable antecedents |
| L9 | EROS | **Yes** | Authored from documented intimate history with datable antecedents |
| L10 | SHADOW | **Yes** | Shadow content forms from wounded events that feed `shadow_content` entries |
| L11 | DESTINY | Optional | Trajectory, not a single event; `resistance_index` may respond to transformative events as state diffs |
| L12 | FUNCTION | No | Fed entirely from the Dramatica ingest template; no feed relationship with Character Astrology |

**The rule:** a layer needs an origin moment when its baseline crystallizes from one datable (even if fuzzily dated) fabula event, rather than from an ongoing trajectory, a derived state, or a storyform binding. L5, L7, L8, L9, and L10 fail this test the same way each time: they name a specific formation point in their own definitions (a wound's trigger, a birth context, a locked-in attachment pattern, a documented intimate history, a debilitated domain). L4, L6, and L11 pass because they describe a rate or a direction, not a point; L1, L2, L3, and L12 pass because they never move within a story arc or come from character work at all.

---

## THE HANDSHAKE

**To the syuzhet doc.** The plot card's fabula-facing fields read this doc's event registry directly:

| Plot card field | Reads from the fabula |
|---|---|
| P2 `driver_event` | An event's `event_id` and `transition` — the event that precipitates the unit's turn |
| P3 `value`, `polarity_in` | The referenced event's state-before half of `transition` |
| P4 `turn_mechanism` | The `cause` or `enable` edge linking the value-in event to the value-out event |
| P5 `polarity_out`, `irony_flag` | The referenced event's state-after half of `transition` |
| P6 `throughline`, `signpost_or_journey`, `act` | **Not from the fabula** (ruled 2026-09-24, plot doc call 15): P6 is seated by the trope graph's walk ([📐 ssot_04_trope_graph.md](📐%20ssot_04_trope_graph.md)). The fabula supplies only the event's `time` |
| P7 `reveal_content`, `reveal_type` | An event whose `gap_type` was `logged`-but-untold surfaces here as the syuzhet's reveal. UNDERSIDE_SURFACING (03) hands P7 these two fields and logs the event as `gap_type: logged`, surfacing as untold (IF catalog call 5; IF-03-04-19) |
| P9 `stakes_delta` | The chain of `cause`/`enable` edges back to the prior fabula event in sequence — this is the fix for the plot doc's own flagged gap, "P9 needs a prior unit to compare against... nothing upstream carded yet" |
| P11 `order_told`, `order_happened`, `duration_mode` | `order_happened` is this doc's `time` field on the referenced event (`time_code` and `calendar_year` included); `order_told` stays the syuzhet doc's own field, written as an 08 time code (IF catalog call 1; IF-04-08-13); the gap between them is classified as an anachrony (external, internal, or mixed analepsis; prolepsis) so the trope graph can reason about foreshadowing and reveal structure ([[BVX.0562]] does not cover this; Genette 1980: 48-53) |

**To the state architecture.** The v1.1 gap PS2 flagged becomes a patch spec, **landed in `ssot_02_character_state_architecture.md` v1.1.0 on 2026-09-24** (OPEN call 6, ruled). As applied:

1. **`origin_event` field** — a structured reference, `origin_event: "<event_id>"`, added beside the freeform `narrative_moment` text (kept as a readable tag) as the state record's structured link into this doc's registry.
2. **`state_diffs` as a named parent field** — consolidating the current separate `MODIFIED_VALUES`, `MODIFIED_DERIVED`, and `MODIFIED_FLAGS` blocks under one `state_diffs:` parent, so a state change reads explicitly as a diff caused by an event rather than three loose blocks.
3. **Event ID standardization** — the fabula assigns each event one `event_id` (this doc's `<movement>_<slug>` grammar); every state record that traces to it carries the same string in `origin_event`. Worked example: `event_id: "m1b_crash_jebb_death"` pairs to state diff `vm_m1b_post_crash`.

**To the setting.** The setting doc's Axis 4 TIME states — "a slice is the baseline; states are dated overlays keyed to ladder addresses" — read this doc's world-clock eras for their dating rather than the setting doc re-deriving its own; S7 FOUNDING, S11 VECTOR, and S5 SCAR stay the authoring surface for what happened to the place, this doc stays the authoring surface for when.

**To the readers of the world clock.** Read by 01 (IF-01-04-06): the story registry reads the universe eras 1–5 and the world clock, and each story row carries an era. Read by 05 (IF-04-05-01): a catalog entry's `origin: "<fabula event_id>"` names the event that brought the entry into being.

---

## THE INSTANCE

**Scope note:** per the ruled default on DOPE SHEET 77 (Chief's silence read as "all recs"), this wave's instance fills Tori Midnight (alias Victoria) only. Anna Colson Conway carries zero dated past events in current canon — her own node marks L7 ORIGIN, L8 IMPRINT, and the Jebb Midnight relation as author-pending (Open Questions #3, #4, #9) — so no event record is filled for her this wave; that gap is OPEN call 1 (77-C), not an omission.

The fabula's Movement 1 is the Delta Coast racing run. The PSP Fella salvage flotilla is held as lineage (F7, ruled 2026-10-11).

Facts below trace only to what PS2 quotes from `victoria-midnight.md`. No birth date, no age at the crash, and no calendar date exist in that node for any of these events; every `time.reach` below is fuzzy or movement-relative only, never a fabricated point.

```yaml
event_id: "m1b_crash_jebb_death"
transition: "Tori overrides the pace notes, calculating she knows better -> Jebb dies"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
  - actor: "Jebb Midnight"
    actant_role: object
kernel_satellite: kernel   # branches WOUND, KINSHIP_COLLAPSE, and every downstream state
time:
  movement: "M1B"
  reach: "pre-story; distance from story-present unspecified in canon"
  extent: "point (a single crash)"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "victoria-midnight.md, REORIENT; §11 vertical slice instance"
  confidence: direct_quote
causal_edges:
  - type: cause
    to: "m1b_untouchable_resolve"
```

```yaml
event_id: "m1b_untouchable_resolve"
transition: "reactive grief -> the closed resolve 'I will become untouchable'"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
kernel_satellite: kernel   # a choice point, Bal's Choice criterion — opens a new behavioral regime
time:
  movement: "M1B, immediately post-crash"
  reach: "pre-story; unspecified"
  extent: "point"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "victoria-midnight.md, REORIENT"
  confidence: direct_quote
causal_edges:
  - type: precede
    to: "m2_recruited"
```

```yaml
event_id: "m2_recruited"
transition: "outside the Academy -> recruited to the Academy"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: object
kernel_satellite: kernel   # opens the school throughline
time:
  movement: "M2 entry"
  reach: "unspecified relative to M1B beyond sequence"
  extent: "point"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "victoria-midnight.md, Where she appears"
  confidence: direct_quote
causal_edges: []   # no stated causal link to M1B beyond precedence; precedence alone is not causality (Bal 2017: 159)
```

**Call 12 addition (2026-09-24, BOLO 77 wave 3).** The five records above trace only to what PS2 quotes from `victoria-midnight.md`; the sixth below traces instead to the scene card — `oxo-scene-card-M2-row9.md`'s own commandments block — filling the gap the plot doc's OPEN call 12 named: no fabula event covered row 9's rating system, "Verified" mechanic, or reach-vs-pull-out choice.

```yaml
event_id: "m2_first_sync_verified"
transition: "the best-bad choice at her first Sync-rating session, pull out (stay grey, keep control-as-safety) or reach (take the counterfeit wholeness) -> she reaches, says 'breathe' into the gap, the Feed archives it 'Unrecognized input,' her rating climbs anyway, and she is marked 'Verified' (neon blue)"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
  - actor: "the Feed (DCUS Sync system)"
    actant_role: opponent
kernel_satellite: kernel   # Bal's Choice criterion — the CR beat is a stated best-bad choice, opens a new behavioral regime (the hook goes in)
time:
  movement: "M2"
  reach: "unspecified relative to m2_recruited beyond sequence; scene card marks it the first Sync-rating session, address q1.s3"
  extent: "point (one Sync session)"
gap_type: logged
repeat: false
location: GAP   # the Sync hall is the scene card's own invention; no 03 address (F3)
stories: [OXO]
provenance:
  source: "oxo-scene-card-M2-row9.md, THE CARD commandments block (II/TP/CR/CL/RES) and the value-turn line"
  confidence: direct_quote   # quoted verbatim from the scene card; the card itself is status draft/⧗, see its own CANON GAPS section
causal_edges:
  - type: specify
    to: "m2_grief_outbursts"   # this dated Sync session is one instance the iterative m2_grief_outbursts class stands for; the card's TP line ("Digital Puberty glitch fires mid-sync") names the same in-world dismissal
```

```yaml
event_id: "m2_grief_outbursts"
transition: "grief held -> grief surfacing as surreal outbursts, dismissed in-world as 'Digital Puberty'"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
kernel_satellite: satellite   # characterizes the ongoing state, does not itself branch the fabula
time:
  movement: "M2"
  reach: "unspecified"
  extent: "repeated across M2"
gap_type: logged
repeat: true   # Genette's iterative — one record standing for a repeated class (Genette 1980: 53)
location: GAP   # no 03 address given
stories: [OXO]
provenance:
  source: "victoria-midnight.md, Where she appears"
  confidence: direct_quote
causal_edges:
  - type: precede
    to: "m3_underground_search"
```

```yaml
event_id: "m3_underground_search"
transition: "Jebb's data unrecovered -> Tori works the transgressive underground seeking the deleted data of his death"
actors:
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
kernel_satellite: satellite   # an ongoing pursuit, no stated single-choice branch point in canon
time:
  movement: "M3"
  reach: "unspecified"
  extent: "ongoing across M3"
gap_type: logged
repeat: true
location: GAP   # the transgressive underground has no 03 address
stories: [OXO]
provenance:
  source: "victoria-midnight.md, Where she appears"
  confidence: direct_quote
causal_edges: []   # no stated causal edge to the crash's data-deletion mechanism; flagged uncertain, not invented
```

**The removal event (F8, ruled 2026-10-11).** The crash stays the believed cause of Jebb's death. The world holds a second event: the system removed him on purpose, and Tori misreads it. The fabula records what really happened. The syuzhet tells it later as a P7 reveal.

```yaml
event_id: "m1b_system_removes_jebb"
transition: "Jebb alive -> the system removes Jebb as a punitive removal; Tori reads it as her own crash"
actors:
  - actor: "the system (DCUS)"
    actant_role: opponent
  - actor: "Jebb Midnight"
    actant_role: object
  - actor: "Tori Midnight"   # alias: Victoria
    actant_role: subject
kernel_satellite: kernel   # the true cause under the believed one
time:
  movement: "M1B"
  reach: "pre-story; distance from story-present unspecified in canon"
  extent: "point"
gap_type: logged   # on record, untold until the P7 reveal
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "series bible note OB35"
  confidence: inferred
causal_edges:
  - type: cause
    to: "m1b_crash_jebb_death"
    confidence: inferred   # G2, ruled 2026-10-12; OB35: "a punitive removal, a functional act" (packet.md:1064, 1067); the crash stays the believed cause
```

**The Feed's version of an event (F9, ruled 2026-10-11).** The fabula records the true event. The Feed's account is a separate event with `source_kind: institutional`. The two do not conflict. The Miracle Glitch is the worked case, and it is not placed on a movement in canon yet. Its two ids carry the `unplaced_` prefix until Chief places the event; the prefix then becomes the era's (G1, ruled 2026-10-12).

```yaml
event_id: "unplaced_miracle_glitch_destruction"
transition: "Quinn Bishop and Riley Moss alive -> destroyed"
actors:
  - actor: "Quinn Bishop"
    actant_role: object
  - actor: "Riley Moss"
    actant_role: object
kernel_satellite: kernel
time:
  movement: null   # not placed in canon
  time_code: null
  calendar_year: null
  reach: "unspecified"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
location: GAP
stories: [OXO]
provenance:
  source: "series bible notes OB19, OB28, OB15"
  confidence: inferred
causal_edges:
  - type: cause
    to: "unplaced_miracle_glitch_feed_record"
```

```yaml
event_id: "unplaced_miracle_glitch_feed_record"
transition: "no record -> the Feed shows Quinn Bishop and Riley Moss surviving, with a Medal of Honor"
actors:
  - actor: "the Feed (DCUS Sync system)"
    actant_role: subject
  - actor: "Quinn Bishop"
    actant_role: object
  - actor: "Riley Moss"
    actant_role: object
kernel_satellite: satellite   # the official telling, not the world's truth
time:
  movement: null   # follows unplaced_miracle_glitch_destruction
  time_code: null
  calendar_year: null
  reach: "unspecified"
  extent: "point"
gap_type: logged
repeat: false
source_kind: institutional
location: GAP
stories: [OXO]
provenance:
  source: "series bible notes OB19, OB28, OB15"
  confidence: inferred
causal_edges: []
```

**A note on Tori's family origin (RULED 2026-09-29, BOLO 91).** Per Chief's ruling, Tori's family origin is **the trash zone, not Bikini Atoll** — where the trash land runs out into the ocean, a delta with room for islands; her family were holdouts there. This supersedes an earlier, discarded variant carried in the phone notes: "Ariel lived on an old army base on an island where she would race and her small community lived in peace. One day the army forcefully evacuated them....the story of the bikini atoll people" (`_PRIVATE/notes/phone-notes-2022-2023.digest.md`, §1 OXO). That Bikini-Atoll draft is now superseded, kept only as discarded history, not canon. The ruled version instead confirms the *other* line from the same source — "Her family was a 'holdout' from pre-skyfall. They own the biggest fucking Island... the 'girl who lives in the dusk,' trash girl" — as the one that stands: a trash-zone delta, not a military-island evacuation. This is background condition feeding **L7 ORIGIN**, not a dated transition, so (per the same Bal 2017: 155-156 rule the note below applies to Tori's racing career) it is not filled as its own event record. **The car crash stays her WOUND**: `m1b_crash_jebb_death` above is unchanged and remains the L5 WOUND trigger; the family-origin ruling adds birth-context color to L7, it does not touch or replace the crash.

**A note on what is left out.** Tori's pre-M1B racing career (working/criminal-adjacent origin, "salvage economy phase," feeding L7 ORIGIN) is not filled as an event record: PS2 gives it as a background condition, not a dated transition, and Bal's own definition rules a state that never changes on record out of the event schema (Bal 2017: 155-156). It stays as context for L7 ORIGIN, not a fabula event.

---

## ANNA COLSON'S ORIGIN (BOLO 91, RULED 2026-09-29)

**Scope note.** THE INSTANCE above scoped wave 1 to Tori only, leaving Anna Colson Conway's L7 ORIGIN and L8 IMPRINT author-pending (OPEN call 1, 77-C). Chief's 2026-09-29 ruling fills that gap: a dated (fuzzily-dated, pre-story) origin chain, sourced from `_PRIVATE/notes/apple-notes-2026.digest.md` §1 OXO, quoting Chief's own note verbatim: *"Colson dies in a freak ice-skating accident. Her father seeks out a scientist who says she can build her back, but better. The scientist grows too close to Colson, so the father steals her back — but what the father doesn't know is that she's made her own copy of Colson."* Five backstory events follow, using the `backstory_<slug>` grammar (v0.1.4, BOLO 90 step 7). **The copy is not a state diff on Anna Colson Conway** — per Chief's ruling it "gets her own fabula node, separate from Colson" — so the fifth event below doubles as the copy's own L7 ORIGIN moment, a distinct actor from the original.

```yaml
event_id: "backstory_colson_skating_death"
transition: "Colson skating -> Colson dies in a freak ice-skating accident"
actors:
  - actor: "Anna Colson Conway"
    actant_role: object
kernel_satellite: kernel   # opens the entire rebuild/copy chain; branches L7 ORIGIN
time:
  movement: "backstory"
  reach: "pre-story; distance from story-present unspecified"
  extent: "point (a single accident)"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "_PRIVATE/notes/apple-notes-2026.digest.md, §1 OXO — Anna Colson Conway's origin"
  confidence: direct_quote
causal_edges:
  - type: cause
    to: "backstory_colson_father_seeks_scientist"
```

```yaml
event_id: "backstory_colson_father_seeks_scientist"
transition: "Colson dead -> her father seeks out a scientist who says she can be built back, but better"
actors:
  - actor: "Colson's father"
    actant_role: subject
  - actor: "the scientist"
    actant_role: helper
  - actor: "Anna Colson Conway"
    actant_role: object
kernel_satellite: kernel   # Bal's Choice criterion — the father chooses the rebuild path
time:
  movement: "backstory"
  reach: "immediately after backstory_colson_skating_death; unspecified distance"
  extent: "point"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "_PRIVATE/notes/apple-notes-2026.digest.md, §1 OXO — Anna Colson Conway's origin"
  confidence: direct_quote
causal_edges:
  - type: enable
    to: "backstory_colson_scientist_attachment"
```

```yaml
event_id: "backstory_colson_scientist_attachment"
transition: "the rebuild proceeds as a professional project -> the scientist grows too close to Colson"
actors:
  - actor: "the scientist"
    actant_role: subject
  - actor: "Anna Colson Conway"
    actant_role: object
kernel_satellite: kernel   # the turn that provokes the father's reclaim
time:
  movement: "backstory"
  reach: "during or after the rebuild; unspecified distance"
  extent: "extended (a growing attachment, not a point) ⧗"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "_PRIVATE/notes/apple-notes-2026.digest.md, §1 OXO — Anna Colson Conway's origin"
  confidence: direct_quote
causal_edges:
  - type: cause
    to: "backstory_colson_father_reclaims"
```

```yaml
event_id: "backstory_colson_father_reclaims"
transition: "Colson in the scientist's care -> the father steals her back"
actors:
  - actor: "Colson's father"
    actant_role: subject
  - actor: "the scientist"
    actant_role: opponent
  - actor: "Anna Colson Conway"
    actant_role: object
kernel_satellite: kernel   # closes the rebuild chain for the Colson the father recovers
time:
  movement: "backstory"
  reach: "after backstory_colson_scientist_attachment; unspecified distance"
  extent: "point"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "_PRIVATE/notes/apple-notes-2026.digest.md, §1 OXO — Anna Colson Conway's origin"
  confidence: direct_quote
causal_edges:
  - type: simultaneous
    to: "backstory_colson_copy_made"   # the father does not know this happens at the same time
```

```yaml
event_id: "backstory_colson_copy_made"
transition: "one Colson exists -> the scientist secretly keeps her own copy of Colson, made without the father's knowledge — a second, distinct Colson"
actors:
  - actor: "the scientist"
    actant_role: subject
  - actor: "Anna Colson Conway (the copy)"   # NOTE: a distinct actor from "Anna Colson Conway" above — her own fabula node per Chief's ruling, not a state diff on the original
    actant_role: object
kernel_satellite: kernel   # this event is ALSO the copy's own L7 ORIGIN moment — she begins existing here; her own 02 character record points its L7 `origin_event` here (IF catalog call 5)
time:
  movement: "backstory"
  reach: "concurrent with backstory_colson_father_reclaims; unspecified distance"
  extent: "point (the copy is made)"
gap_type: logged
repeat: false
location: GAP
stories: [OXO]
provenance:
  source: "_PRIVATE/notes/apple-notes-2026.digest.md, §1 OXO — Anna Colson Conway's origin"
  confidence: direct_quote
causal_edges: []   # downstream events for the copy are not yet on record — open for a future wave
```

**The copy's own record (IF catalog call 5, ruled 2026-10-05; IF-02-04-17).** "Anna Colson Conway (the copy)" gets her own 02 character record, apart from `_CANON_NODES/anna-colson-conway.md`. That record's L7 ORIGIN names `backstory_colson_copy_made` as its `origin_event`. The five Colson events feed L7 only.

**What this does and does not settle.** This fills L7 ORIGIN's dated antecedent for Anna Colson Conway (and gives "Anna Colson Conway (the copy)" her own L7 ORIGIN event, distinct from the original). It does **not** fill L8 IMPRINT, L9 EROS, or L10 SHADOW for either Colson — those stay author-pending per the original node's Open Questions #3, #4, #9 — and it does not place either Colson's post-origin events (what either of them does afterward) on the fabula. That is future wave work, not this ruling.

---

## THE ERA SPINES (batch 3, RULED 2026-10-12, Chief: "take all recs")

Batch 3 puts the first event records into eras 1, 3 and 5. Every place gate is met (G4, G7, G11). Every `location` stays GAP until 03 gives the homestead and the station an address. No record names a person, because no source names one yet (L3). Records marked provisional rest on a provisional ruling and rise to canon on one word.

Batch 3 is closed (10/12, 'take all recs'). Still ⧗, by ruling: H10 the station's name and owner, held until the post-apocalyptic research list returns · what the first attempt loses · the first-comer people's name and customs · the ship itself.

**Era 1 · Skeeter Creek.** The first attempt fails (H2), and a first-comer people helps the founders survive (H3). The founding on the homestead follows. The three Narco Republic stages follow in their ruled order; which generation sees each stage is open. The heir of the Red Hills generation renames the place Red Hills (H4). The sale of the land comes right after the 2099 Moon Severance (H6), so the family sells into the diving economy that mines the falling wreck; it closes the family's hold and enables the rebrand.

```yaml
event_id: "skeeter_creek_backstory_first_attempt_lost"   # PROVISIONAL (H2 rec taken 10/12); what is lost ⧗
transition: "the founders hold a first holding -> the first holding is lost, and the founders start over"
actors:
  - actor: "the founding generation"   # no name yet; Chief hand-builds the people (L3)
    actant_role: subject
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "the founding years"
  extent: "point"
gap_type: logged
repeat: false
source_kind: ownership
canon_source: "H2 rec taken 10/12 ('take all recs'): A Land Remembered opens on 'a failed first attempt with a clear loss' (BVX.1276 line 180); the loss itself is Chief's"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "skeeter_creek_backstory_skeeter_creek_founding"
```

```yaml
event_id: "skeeter_creek_backstory_first_comers_ally"   # PROVISIONAL (H3 rec taken 10/12); the people's name and customs ⧗
transition: "the founders alone on the Delta Coast -> a first-comer people helps them survive"
actors:
  - actor: "the first-comer people of the Delta Coast"   # no name yet; Chief hand-builds the people (L3)
    actant_role: subject
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "the founding years"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "H3 rec taken 10/12 ('take all recs'): after the book's Seminole allies (BVX.1276 lines 169, 208, 278), translated, not transplanted (L1, L3); lineage note: Red Stick Creek, Native North Florida (digest.md:678)"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: inferred
causal_edges:
  - type: enable
    to: "skeeter_creek_backstory_skeeter_creek_founding"
```

```yaml
event_id: "skeeter_creek_backstory_skeeter_creek_founding"   # PROVISIONAL (G4)
transition: "no holding at Skeeter Creek -> the founding generation holds a scrub homestead"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: construction
canon_source: "G4 (provisional); L2; fabula doc, the world clock era 1 row"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "skeeter_creek_land_sold"
```

```yaml
event_id: "skeeter_creek_narco_republic_cartel_culo"   # working name ⧗
transition: "no Narco Republic -> the founders run a joke-named cartel"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: institutional
canon_source: "G6; Chief 10/12: 'not serious at all'"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges:
  - type: precede
    to: "skeeter_creek_narco_republic_cartel_federal"
```

```yaml
event_id: "skeeter_creek_narco_republic_cartel_federal"
transition: "Cartel Culo -> Cartel Federal"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: institutional
canon_source: "batch 2 rec taken 10/12; Pax Cartel an alias"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges:
  - type: precede
    to: "skeeter_creek_narco_republic_real_federale"
```

```yaml
event_id: "skeeter_creek_narco_republic_real_federale"
transition: "Cartel Federal -> Real Federale"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: institutional
canon_source: "G6"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges: []
```

```yaml
event_id: "skeeter_creek_backstory_red_hills_rename"
transition: "the founding name Skeeter Creek -> the name sanded to Red Hills"
actors:
  - actor: "the second generation's heir"   # no name yet; Chief hand-builds the person (L3)
    actant_role: subject
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "about a century before the Bishops arrive"
  extent: "point"
gap_type: logged
repeat: false
source_kind: rename
canon_source: "H4, Chief 10/12: 'Its heir' (the heir of the Red Hills generation renames, not the generation itself); 03 S7 FOUNDING: sanded to 'Red Hills' a century before the Bishops"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges:
  - type: precede
    to: "backstory_dcus_rebrand"
```

```yaml
event_id: "skeeter_creek_backstory_moon_colony"   # PROVISIONAL (S4 rec taken 10/12: two ids, one edge); era 1's buried secret
transition: "no one lives on the Moon -> a colony goes up on the Moon"
actors: []   # no source names the colonists; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null   # the 2050s-70s stay lineage on the Outliers clock (F4)
  reach: "before the 2099 Moon Severance"
  extent: "span"
gap_type: logged
repeat: false
source_kind: construction
canon_source: "THE WORLD CLOCK (BOLO 96): 'The Moon colony went up in the 2050s-70s and had turned hell by the 2090s'; 'the early Moon colony is era 1's buried secret'; S4 rec taken 10/12 ('take all recs')"
produces: []
scheduled: null
location: GAP   # the Moon's 03 address ⧗
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "skeeter_creek_backstory_moon_severance"
```

```yaml
event_id: "skeeter_creek_land_sold"   # the regret stays a separate record, PROVISIONAL (L4)
transition: "the family holds the Skeeter Creek land -> the last generation sells it, and it becomes the school site"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "right after the 2099 Moon Severance"
  extent: "point"
gap_type: logged
repeat: false
source_kind: ownership
canon_source: "L2 (ruled); H6, Chief 10/12, revised the same hour: 'it would probably be better after the 2099 shit happens.....right after' (the sale follows the Severance); the regret is L4, provisional"
produces: []
scheduled: null
location: GAP
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges:
  - type: enable
    to: "backstory_dcus_rebrand"
```

**Era 3 · LAKAD.** The launch opens the era with a hard break (G8). The boarding hands the welded station to every later event as its first address.

```yaml
event_id: "lakad_first_launch"
transition: "characters on Earth -> characters aboard a rocket in space"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: null   # LAKAD has no movements yet
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "G8, Chief 10/12: 'that's where Lakad picks up. It's literally that hard break'"
produces: []
scheduled: null
location: GAP
stories: [LAKAD]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges:
  - type: enable
    to: "lakad_rocket_boarded"
```

```yaml
event_id: "lakad_rocket_boarded"   # PROVISIONAL (G7)
transition: "characters aboard a rocket in flight -> characters held prisoner aboard a welded station"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: null   # LAKAD has no movements yet
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "G7 (provisional), Chief 10/12: 'we'll figure something out'"
produces: []
scheduled: null
location: GAP
stories: [LAKAD]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: direct_quote
causal_edges: []
```

**Era 5 · beyond.** A voyage needs a departure before an arrival, so the departure opens the era (G11). The exodus note's five ship stages (digest.md:680-681) stay lineage, as G11 ruled; they are candidates, not canon.

```yaml
event_id: "beyond_exodus_departure"   # PROVISIONAL (G11); the ship ⧗; the port is the Moon (rec taken 10/12)
transition: "no voyage -> a generation ship leaves the Moon for a new planet"
actors: []   # no source names the people yet; Chief hand-builds them (L3)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "G11 (provisional): 'the journey to a new planet, like a generational ship'"
produces: []
scheduled: null
location: GAP   # departs from the Moon (rec taken 10/12, provisional); the Moon's 03 address ⧗
stories: [backstory_only]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-3.md"
  confidence: inferred
causal_edges: []
```

**Era 4 · ASTRO7EX (batch 4, RULED 2026-10-12, Chief: "take all recs", each rec re-read against I4).** Era 4 runs beside era 2 on the shared 2199 clock (I4), so no record below carries a `calendar_year`. The MAXWING survivor, the heist and the queenpin belong to the separate Moon character (name ⧗), not to Vivian. Every record is provisional, and every `location` stays GAP: the 03 doc holds no Moon address yet.

**S1-S7 RULED 2026-10-12 (Chief: "take all recs").** The Aldrin Sector opens era 4 (S3, I1). Phase I, the Moon's colonization, gets two ids joined by one edge: era 1's `skeeter_creek_backstory_moon_colony` and era 4's `astro7ex_backstory_phase_one_colonized` (S4, I5). The MAXWING purge comes before the AI Collapse (S5, I10). The ASTRO7EX Severance is the AI Collapse seen from the Moon (S6, I12). Vivian finds Myrtle after the heist (S7). The 2090s births (2091, 2095) are ancestors' births, held as lineage, so no era 4 character carries those years (S2, I9 resolved as lineage). The queenpin's name goes on the name bench, BOLO 48 (S1).

Place stubs for the 03 pass (I2, I3; provisional, `location: GAP`, described only as the sources say): **the Aldrin Sector** (era 4's first place, S3; the 2091 lineage birth's place, an ancestor's by S2) · **the Babylon Strip** (the 2095 lineage birth's place, an ancestor's by S2) · **Cradle Halo** (where Fiona is raised, among "transient scientists and visiting corporate executives") · **the AN7L lab ruins** (a burned-out lab in the lunar ruinscape, "a graveyard of unfinished futures").

Held for Chief before S1-S7 (all ruled 10/12, above): I1 · I5 · I10 · I12 · the Myrtle order · I9 with the 2090s births · the queenpin's name. Still ⧗: the queenpin's name (on the bench) · the colonists, MAXWING's site and director. I8 (Vivian's 2091 birth) is void, because I4 gave the 2091 birth to the queenpin; S2 then made it an ancestor's.

```yaml
event_id: "astro7ex_backstory_phase_one_colonized"   # PROVISIONAL (S4 rec taken 10/12: two ids, one edge)
transition: "no one lives on the Moon -> the Moon is colonized as an ideological and scientific utopia"
actors: []   # no source names the colonists
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "Phase I, before AN7L's fracture"
  extent: "span"
gap_type: logged
repeat: false
source_kind: construction
canon_source: "S4 rec taken 10/12 ('take all recs'): 'Phase I: the Moon was colonized as an ideological and scientific utopia' and 'humanity moved to the Moon after an Earth collapse' (packet.md:429, 434); era 1 keeps its own id for the same colony"
produces: []
scheduled: null
location: GAP   # the Aldrin Sector opens era 4 (S3); its 03 address ⧗
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: simultaneous   # the one edge (S4): the same colony, told from era 4
    to: "skeeter_creek_backstory_moon_colony"
  - type: precede
    to: "astro7ex_backstory_an7l_fractured"
```

```yaml
event_id: "astro7ex_backstory_an7l_fractured"   # PROVISIONAL (I6 rec taken 10/12); cause open against C15
transition: "AN7L governs as one AI -> AN7L splits into fragments, and MORN weaponizes them as the MODS"
actors:
  - actor: "AN7L"
    actant_role: subject
  - actor: "MORN"
    actant_role: subject
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "unknown"
  extent: "span"
gap_type: logged
repeat: false
source_kind: construction
canon_source: "I6 rec taken 10/12 ('take all recs'): 'AN7L fractures into conflicting subroutines', and MORN's weaponized fragments birth the MODS (packet.md:431; digest.md:656); rival origin open: John Smith 'created the MODS as apostles' (C15, packet.md:648-653)"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "astro7ex_backstory_bitcoin_moon_heist"
```

```yaml
event_id: "astro7ex_backstory_maxwing_program"   # PROVISIONAL (I7 rec taken 10/12, re-read against I4); site and director ⧗
transition: "children live in the colony -> MAXWING takes children and conditions them"
actors:
  - actor: "the MAXWING program"
    actant_role: subject
  - actor: "the MAXWING children"   # the one survivor the sources follow is the queenpin (I4), name ⧗
    actant_role: object
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "before the AI Collapse"
  extent: "span"   # the start enters now; the end comes later
gap_type: logged
repeat: false
source_kind: character
canon_source: "I7 rec taken 10/12 ('take all recs'): MAXWING is Phase III; it takes children for 'psychic conditioning, physical augmentations, and ideological indoctrination' (packet.md:201, 433)"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "astro7ex_backstory_maxwing_purge"
  - type: precede
    to: "astro7ex_backstory_bitcoin_moon_heist"
```

```yaml
event_id: "astro7ex_backstory_maxwing_purge"   # PROVISIONAL (S5 rec taken 10/12: the purge comes first)
transition: "the MODS class the MAXWING survivor an adaptive asset -> the MODS reclassify her an existential threat, and she survives the purge"
actors:
  - actor: "the MODS"
    actant_role: subject
  - actor: "the queenpin"   # the MAXWING survivor is the queenpin (I4), name ⧗
    actant_role: object
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "before the AI Collapse (S5)"
  extent: "span"
gap_type: logged
repeat: false
source_kind: character
canon_source: "S5 rec taken 10/12 ('take all recs'): 'During the MAXWING purges, the MODS reclassified [her] from adaptive asset to existential threat'; she 'survives the purge' (packet.md:205, 203); I4 moves the survivor to the queenpin"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "astro7ex_backstory_ai_collapse"
  - type: precede
    to: "astro7ex_backstory_bitcoin_moon_heist"
```

```yaml
event_id: "astro7ex_backstory_ai_collapse"   # PROVISIONAL (I11 rec taken 10/12, G10); cause open between two readings (C15)
transition: "Moon and Earth linked by the recursion chain -> the chain is cut, and the Moon people turn aggressive"
actors: []   # the cause is open: John's deployment of the MAXWING children, or the world's 'refusal to change'
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "after the Deep Meridian beam"
  extent: "point"   # G10: 'it happens everywhere all at once'
gap_type: logged
repeat: false
source_kind: character
canon_source: "G10 (Chief 10/12) and I11 rec taken 10/12 ('take all recs'): on the Moon, everywhere all at once; reading 1, John 'deployed MAXWING children as encryption bombs to cut the recursion chain' (packet.md:435); reading 2, the world 'collapses not from an attack but from its refusal to change' (digest.md:652); the beam precedes it (the hinge)"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges: []   # the MAXWING purge precedes it (S5); the Moon's side of it is the ASTRO7EX Severance (S6)
```

```yaml
event_id: "astro7ex_backstory_moon_severance"   # PROVISIONAL (S6 rec taken 10/12); kept apart from era 1's Severance (G9)
transition: "the Moon is linked to Earth -> the Moon is cut off, as the Moon lives through the AI Collapse"
actors: []   # the cause stays open with the AI Collapse's (C15)
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null   # 'the Moon Severance happened in 2099 (OXO canonical year 2199 on Earth)' stays lineage (F4)
  reach: "at the AI Collapse"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "S6 rec taken 10/12 ('take all recs'): the ASTRO7EX Severance is the AI Collapse seen from the Moon; lineage: 'the Moon Severance happened in 2099 (OXO canonical year 2199 on Earth)', 'divers mine a falling Severance wreck' (digest.md:734, 732)"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: simultaneous
    to: "astro7ex_backstory_ai_collapse"
```

```yaml
event_id: "astro7ex_backstory_bitcoin_moon_heist"   # PROVISIONAL (I13 rec taken 10/12, re-read against I4); the Myrtle find follows (S7)
transition: "the cold wallet sits with MORN -> the queenpin steals it and becomes the lunar queenpin"
actors:
  - actor: "the queenpin"   # the separate Moon character (I4), name ⧗
    actant_role: subject
  - actor: "MORN"
    actant_role: opponent
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "five years before Fiona's jaded present"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "I13 rec taken 10/12 ('take all recs'): 'pulls the Bitcoin Moon heist, and becomes lunar queenpin' (packet.md:203; digest.md:298); 'steals the cold bitcoin wallet as an act of ultimate rebellion against MORN and MODS' (digest.md:884); 'five years after the heist' (packet.md:187); I4 moves the heist to the queenpin"
produces: []
scheduled: null
location: GAP
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges:
  - type: precede
    to: "astro7ex_backstory_myrtle_found"
```

```yaml
event_id: "astro7ex_backstory_myrtle_found"   # PROVISIONAL (S7 rec taken 10/12: after the heist); Myrtle's origin open against C14
transition: "Myrtle lies in a burned-out AN7L lab -> Vivian finds her"
actors:
  - actor: "Vivian"   # the source names Vivian; I4 moved the heist, not the find
    actant_role: subject
  - actor: "Myrtle"
    actant_role: object
kernel_satellite: kernel
time:
  movement: "backstory"
  time_code: null
  calendar_year: null
  reach: "after the heist (S7), after a MODS purge"
  extent: "point"
gap_type: logged
repeat: false
source_kind: character
canon_source: "S7 rec taken 10/12 ('take all recs'): Vivian finds Myrtle in 'a burned-out lab deep within the lunar ruins of the AN7L project' 'after a MODS purge' (packet.md:387); rival origin open (C14, packet.md:642)"
produces: []
scheduled: null
location: GAP   # the AN7L lab ruins stub (I3)
stories: [ASTRO7EX]
provenance:
  source: "_PRIVATE/intake/FABULA-BATCH-4.md"
  confidence: inferred
causal_edges: []
```

---

## FABULA × LIBRARY

| Source | What it gives the fabula | Cite |
|---|---|---|
| Bal, *Narratology* | The event definition (transition, Choice, Confrontation), kernel/satellite's functional test, Bremond's causal phases, the gap/silence distinction | [[BVX.0591]] |
| Chatman, *Story and Discourse* | The kernel/satellite terms themselves; the surprise-in-story/suspense-in-discourse cut that keeps suspense a syuzhet-layer query, not a fabula field | [[BVX.0167]] |
| Genette, *Narrative Discourse* | Order, duration, frequency as the three discourse axes; reach and extent as the two numbers an event carries; the anachrony taxonomy (analepsis, prolepsis) THE HANDSHAKE hands to P11 | Genette 1980 (drop; no catalog id) |
| Rimmon-Kenan, *Narrative Fiction* | The warrant for `provenance`/`confidence`: story is a reconstruction, never the text itself, so a shared-universe fabula must adjudicate rather than transcribe | Rimmon-Kenan 2002 (drop; no catalog id) |
| Wolf, *Building Imaginary Worlds* | Internarrative theory — the direct warrant for one fabula under two syuzhets; the `stories:` field | [[BVX.0562]] |
| Sternberg, "Expositional Modes and Temporal Ordering in Fiction" | Curiosity/suspense/surprise as *payoffs* of misaligning syuzhet order against fabula order, confirming these are queries against this doc, not stored fields on it | Sternberg 1978 (drop; no catalog id) |
| Propp, *Morphology of the Folktale* | The boundary case: functions are a pattern-layer above events, the trope graph's job (wave 2), explicitly not a field this doc owns | Propp 1968 (drop; no catalog id) |

---

## OPEN
**All six ruled 2026-09-24, Chief: "go on all recommendations."** Each rec below is now the rule, provisional a week like every ruling.

1. **RULED 2026-09-24 (rec taken) · 77-C — Tori-only instance** — does wave 1's filled instance stay Tori-only, leaving Anna Colson Conway's layer origins open per her own node's Open Questions? Rec: yes, matches Chief's silence-ruling on DOPE SHEET 77 and Anna Colson Conway's own node marks L7 and L8 as author-pending.
2. **RULED 2026-09-24 (rec taken) · 77-D — EVIL CHECK wave 2** — when does EVIL CHECK's own event set enter this registry, given the `stories:` field is reserved but empty for it now? Rec: wave 2, once an EVIL CHECK-side extraction exists to source-check its events the way PS2 did for Tori.
3. **RULED 2026-09-24 (rec taken) · Event ID scheme** — the digests give one worked example, `m1b_crash_jebb_death`, but no formal grammar for `event_id`; what characters and length does the state doc's v1.1 field expect? Rec: adopt `<movement>_<slug>` as the working grammar until the state doc's owner rules otherwise.
4. **RULED 2026-09-24 (rec taken) · DCUS eras vs setting arc** — should THE WORLD CLOCK re-author the Skeeter Creek to Red Hills to DCUS lattice as its own filled event rows, or only cross-reference S5, S7, and S11? Rec: cross-reference only; the setting doc stays the one authoring surface for those dated states.
5. **RULED 2026-09-24 (rec taken) · Fuzzy-date convention** — none of the theory sources gives a formal null-value convention for an unknown date; is movement-relative dating, Mn with no calendar, the Command's working answer for this wave? Rec: yes for now, revisit once a calendar exists for the world.
6. **RULED 2026-09-24 (rec taken) · State architecture v1.1 ownership** — this doc specifies the `origin_event`, `state_diffs`, and event-id patch; does `ssot_02_character_state_architecture.md` take the version bump in the same pass or a separate FRAGO? Rec: separate FRAGO to that file; this doc's HANDSHAKE section is the spec source of truth until it lands.

---

## Version history

- 10/11 · batch 1 F1–F12 ruled ('Take all recs')
- **1.6.0 — 2026-10-12.** S1-S7 recs taken ('take all recs'). S3: the Aldrin Sector opens era 4. S4: Phase I gets two ids and one `simultaneous` edge, `skeeter_creek_backstory_moon_colony` (era 1) and `astro7ex_backstory_phase_one_colonized` (era 4). S5: `astro7ex_backstory_maxwing_purge` enters before the AI Collapse; the queenpin survives it. S6: `astro7ex_backstory_moon_severance` enters as the AI Collapse seen from the Moon (G9 keeps it apart from era 1's). S7: `astro7ex_backstory_myrtle_found` enters after the heist (C14 open). S2: the 2090s births are ancestors', held as lineage; I9 closes as lineage. S1: the queenpin's name goes on the name bench (BOLO 48). All provisional.
- **1.5.0 — 2026-10-12.** Batch 4 recs taken ('take all recs'), each re-read against I4. Era 4 gets its first four records, all provisional: `astro7ex_backstory_an7l_fractured` (I6, cause open on C15), `astro7ex_backstory_maxwing_program` (I7, no child named), `astro7ex_backstory_ai_collapse` (I11, cause open), `astro7ex_backstory_bitcoin_moon_heist` (I13, moved to the queenpin). Four Moon place stubs for the 03 pass: the Aldrin Sector, the Babylon Strip, Cradle Halo, the AN7L lab ruins (I2, I3). Held for Chief: I1, I5, I10, I12, the Myrtle order, I9 with the 2090s births, the queenpin's name. I8 void.
- **1.4.0 — 2026-10-12.** I4 ruled (Chief's words + "take both"): era 4 (ASTRO7EX) runs at the same time as era 2, sharing 2199; the seam-only overlap rule gains that exception. Vivian's story ends at the jump to LAKAD. The MAXWING survivor, heist and queenpin are a separate Moon character (name ⧗) and take the 2091 Aldrin birth. The 2090s births are held ⧗ (ancestors or a century later).
- **1.3.0 — 2026-10-12.** Batch 3 closed ('take all recs'). H2: `skeeter_creek_backstory_first_attempt_lost` (provisional). H3: `skeeter_creek_backstory_first_comers_ally`, after the book's Seminole allies, name ⧗ (provisional). The era 5 ship departs the Moon (provisional). H10 held until the post-apocalyptic research list returns. Eleven era spine records.
- **1.2.2 — 2026-10-12.** H6 revised (Chief: "it would probably be better after the 2099 shit happens.....right after"): the land sale follows the 2099 Moon Severance; its precede edge to the Severance is removed, and the Severance now comes first.
- **1.2.1 — 2026-10-12.** Chief hand-built H4 ('Its heir'): `skeeter_creek_backstory_red_hills_rename` enters, the Red Hills generation's heir renames. H6 ('before'): the land sale precedes the 2099 Moon Severance. Nine era spine records.
- **1.2.0 — 2026-10-12.** Batch 3 recs taken ('take all recs'). THE ERA SPINES adds eight records: era 1's founding (provisional, G4), the three Narco Republic stages, the land sale (regret provisional, L4); era 3's first launch and the boarding (provisional, G7); era 5's departure (provisional, G11). Every location GAP. H2, H3, H4, H6, H10 and the era 5 ship stay with Chief.
- **1.1.3 — 2026-10-12.** Recs taken: Cartel Federal is the Narco Republic's middle stage (Pax Cartel an alias); the AI Collapse sits in era 4.
- **1.1.2 — 2026-10-12.** G4: a scrub homestead at Skeeter Creek is era 1's first place (provisional). G7: the rocket is boarded mid-flight; the characters are taken prisoner aboard a station made of three or four stations, Fallout 3 in feel (provisional). Batch 3's place gate is met.
- **1.1.1 — 2026-10-12.** Chief hand-built four calls. G6: Real Federale is the Narco Republic's last stage; a crude joke name (working: Cartel Culo) is the first. G8: `lakad_first_launch`, the rocket into space, opens era 3. G10: the AI Collapse happens on the Moon. G11 (provisional): era 5 is a generation ship's journey, not a landfall. G4 and G7 stay open.
- **1.1.0 — 2026-10-12.** Batch 2 ruled ('All recommendations'). `unplaced_` id prefix; the Miracle Glitch ids renamed (G1). The removal gets an inferred cause edge to the crash (G2). Places before events in eras 1, 3 and 5 (G3, G12). Seam and Severance ids kept (G5, G9). Era 5 exodus note held as lineage (G11). A Land Remembered is era 1's skeleton (L1-L4, L4 provisional). Hand-build calls G4, G6, G7, G8, G10 and G11's landfall question stay open for Chief.
- **1.0.1 — 2026-10-11** · F2 and F10 carried through (ids and prose)
- **1.0.0 — 2026-10-11.** `stories` gains ASTRO7EX, TREMOR_CULT, LAKAD (F1). Era prefix on every `event_id` outside era 2 (F2). `location` holds a 03 address or GAP (F3). 2099 and 2199 held as lineage on the Outliers clock only (F4). Beam first, then the Severance; two Severance ids (F5). Kessler age held as lineage (F6). Delta Coast racing run is M1 (F7). Removal event added (F8). The Feed's record is its own event (F9). Actor names use the ruled long forms (F10). Eras 1, 3 and 5 stay band-only (F11). Method done; instance ⧗ marks stay as marked gaps (F12).
- **0.3.0 — 2026-10-05.** BOLO 102 stage 2 (Chief: "My word"): the event record gains `source_kind`, `canon_source`, `produces` and `scheduled` (call 5); `time` carries the 08 time code and the calendar year, and the "no calendar layer" line is corrected (call 1); `story_beat` and flag `event_id` stated; the copy's 02 record named; two reader lines added (IF-01-04-06, IF-04-05-01).
- **0.2.0 — 2026-10-01 (BOLO 96, "all rec").** THE WORLD CLOCK gains its first calendar years: OXO's present **2199**, the **Moon Severance 2099** (era 1): the Moon nukes orbit into a Kessler cascade on purpose; the Outliers descend from Moon people who came back down; ASTRO7EX is Earth's return. Event `skeeter_creek_backstory_moon_severance`. Its order against the Deep Meridian beam stays open.
- **0.1.9 — 2026-09-29.** THE WORLD CLOCK gains a new era 1, **Skeeter Creek** (Chief: "era one will be the Skeeter Creek … it'll stay the same after"): the founding through the Red Hills century, ending at the Bishops' rebrand; DCUS → 2, LAKAD → 3, ASTRO7EX → 4, beyond → 5. The Narco Republic placed on the clock ⧗: rises in era 1.
- **0.1.8 — 2026-09-29.** THE WORLD CLOCK gains era 4, **beyond** (past the Moon, ⧗ unnamed), after DCUS → LAKAD (cislunar) → ASTRO7EX (the Moon); Chief: "after DCUS, there's the cislunar space, and then the moon, and then beyond."
- **0.1.7 — 2026-09-29 (BOLO 91 rulings).** Anna Colson's origin fabula-filled: five `backstory_<slug>` event records (ice-skating death → father seeks the scientist → the scientist's attachment → the father's reclaim → the scientist's own kept copy); "Anna Colson (the copy)" given her own fabula node and L7 ORIGIN moment, distinct from the original. Tori's family origin ruled the trash-zone delta, not Bikini Atoll (superseding the earlier phone-notes draft); the car crash (`m1b_crash_jebb_death`) confirmed unchanged as her L5 WOUND.
- **0.1.6 — 2026-09-29.** The hinge ruled (Chief: "number two, yes"): the Deep Meridian beam signals the quasar that reaches Vivian's time; the Moon Severance and the AI Collapse follow ⧗.
- **0.1.5 — 2026-09-29.** THE WORLD CLOCK gains the universe eras (RULED, Chief: "yes to all recommendations"): DCUS → LAKAD → ASTRO7EX, sequential with overlap at the seams; the Moon Severance + AI Collapse as the ⧗ hinge; the 2/9 "simultaneous" ruling kept as superseded history; applies_to gains LAKAD and ASTRO7EX.
- **v0.1.4 (2026-09-29):** RULED 2026-09-29, Chief: "line up the recs" (BOLO 90 step 7 trial). THE WORLD CLOCK gains a short paragraph on backstory events: deep past with no Mn carries `movement: "backstory"` and `event_id: backstory_<slug>`, additive to the existing `<movement>_<slug>` grammar. No event records changed.
- **v0.1.0 (2026-09-24):** first draft, BOLO 77 wave 1, "go 77" ruled 2026-09-24. Built from three disjoint extractions: PS1 (syuzhet-side hooks, DCUS setting facts), PS2 (the twelve-layer origin-moment rule, the state architecture v1.0 gap, Tori's dated backstory), MS-T (the fabula/syuzhet/trope-graph theory digest, Bal/Chatman/Genette/Rimmon-Kenan/Wolf/Sternberg/Propp). Instance scoped to Tori only per the ruled default; EVIL CHECK's events reserved for wave 2; the state architecture v1.1 patch spec ships inside THE HANDSHAKE rather than in the state doc itself, pending OPEN call 6.
- **v0.1.1 (2026-09-24):** all six OPEN calls ruled as recommended (Tori-only instance · EVIL CHECK in wave 2 · `<movement>_<slug>` ids · DCUS eras cross-referenced · date by movement · the v1.1 patch shipped now). The patch landed in the state architecture v1.1.0: `origin_event` field, `state_diffs` parent, additive, `narrative_moment` kept.
- **v0.1.2 (2026-09-24):** the HANDSHAKE P6 row re-pointed to the trope graph's walk (plot doc OPEN call 15, ruled).
- **v0.1.3 (2026-09-24):** BOLO 77 wave 3, plot doc OPEN call 12 executed — sixth event record added, `m2_first_sync_verified` (M2, the first Sync-rating session's reach-vs-pull-out choice and "Verified" mark), sourced from `oxo-scene-card-M2-row9.md` rather than `victoria-midnight.md`; causal edge `specify` to `m2_grief_outbursts`. Row 9's plot-card P2 DRIVER, P3 VALUE-IN, P5 VALUE-OUT, and P9 STAKES now read this event in `ssot_04_plot_system.md`.
