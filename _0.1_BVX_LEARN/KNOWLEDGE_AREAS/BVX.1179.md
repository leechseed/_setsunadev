---
id: BVX.1179
title: "Freeport: The City of Adventure"
author: "Chris Pramas (creator), with James Bell, Scott Holden, Patrick O'Duffy, Robert J. Schwalb, Todd Secord, Owen K.C. Stephens, and Christina Stiles (Green Ronin Publishing)"
year: 2014
type: distill              # distill | spine
source_type: book          # book | web | video | session | note | internal
subjects: [GAM]            # D5 taxonomy codes, ordered by relevance
primary_subject: GAM
trunk: BLACK                # BLACK | ORANGE | BOTH
spine: [SETTING]            # story-spine levels L0-L7; TEXTURE or SETTING; [] if non-story source
feeds:                      # D2 - mandatory, [] explicit if nothing to feed
  - layer: SETTING
    variable: S7_founding
    strength: primary
    note: "A full 2,000-year 'years before present' timeline load-bears every current NPC, council seat, and law: the Back Alley War explains why no single crime boss rules today, the repealed Succession Law explains the Drac bloodline's end and the live 'Orc Problem.' Present-tense history taken to book length -- the founding record and the current-events section are effectively the same document."
  - layer: SETTING
    variable: S5_scar
    strength: primary
    note: "The Serpent's Teeth archipelago IS the scar: the drowned remnant of the Valossan serpent-people empire, with the city sitting at the exact center of that fall. A second, smaller scar sits on top -- Milton Drac's Lighthouse ('Milton's Folly'), built with the plundered war-chest and secretly wired to a cult ritual. Scar layered on scar, at two different scales."
  - layer: SETTING
    variable: S6_economy
    strength: primary
    note: "Three engines run in parallel: legitimate trade/privateering (the Admiralty sells letters of marque), a triple-tier currency (lords/skulls/pennies) minted from reclaimed tariff gold, and the Salt Curse -- a three-year-old environmental crisis that turned every well to brine and handed the Rainmakers Group a citywide water monopoly. Economy here is a live crisis with a named beneficiary, not a static resource list."
  - layer: SETTING
    variable: S4_law
    strength: primary
    note: "Government is built as a conflict engine, not an org chart: the Sea Lord (absolute, unimpeachable, life tenure) is checked by a twelve-seat Captains' Council she must win eight votes from (she holds two plus the tie-break), and law enforcement is explicitly split into two competing bodies -- the militarized, human-only Sea Lord's Guard and the corrupt, open-to-everyone Freeport Watch -- so political and street tension is structural, not authored per scene."
  - layer: SETTING
    variable: S8_habit
    strength: primary
    note: "Each of the seven districts is one social class plus one danger level, given a numeric settlement stat block (Corruption/Crime/Economy/Law/Lore/Society/Danger) the way Cities of Golarion (BVX.1171) does per city; Freeport runs the same fractal at neighborhood scale inside a single city -- Merchant District wealth vs. Scurvytown squalor vs. Bloodsalt's accidental orc ghetto, each with its own belonging rules."
  - layer: SETTING
    variable: S9_allure
    strength: supporting
    note: "'Gold is king and life is cheap' -- freedom from the stifling governments of the continent, plus the promise of fortune, is the explicit recruiting pitch stated in the book's own introduction and echoed in-world by the guide-NPC Pious Pete; allure and danger are sold as the same package on purpose, never balanced against each other."
  - layer: SETTING
    variable: S10_underside
    strength: primary
    note: "A literal underside (the sewer chapter, titled 'Underside') stacks under the political one: surviving serpent people disguised among the population, the Brotherhood of the Yellow Sign cult still active in hiding, a rumored Flesh Market where the city's one truly inviolate law -- the slavery ban -- gets broken in secret. The buried layer is physical (sewers) and social (secret cult) at once."
  - layer: SETTING
    variable: S3_sensorium
    strength: supporting
    note: "A dedicated Sights and Sounds section builds the city from a repeated sensory set (seagulls, rot, rum, spice, constant wind and surf) before politics -- thinner and more compressed than Cities of Golarion's (BVX.1171) district-by-district palette method, but the same move, run once for the whole city instead of per neighborhood."
  - layer: SETTING
    variable: S11_vector
    strength: primary
    note: "The history chapter and the Current Events section both end on deliberately unresolved threads -- an empty council seat about to be filled, the still-live 'Orc Problem' in Bloodsalt, a mystery ship sinking vessels south of the city 'one year ago.' Vector is left visibly open rather than closed: a sharper, book-length version of BVX.0458's present-tense-history rule."
  - layer: SETTING
    variable: S2_weather
    strength: contextual
    note: "Hurricane season and the Great Green Fire aftermath are named as recurring threats but never built into a system (no rain-shadow or seasonal-banding method, unlike Roberts's essay in BVX.0458). Stays a thin, authorable layer here too -- the same gap DCUS already carries."
  - layer: L7
    variable: genre_setting_contract
    strength: contextual
    note: "The book states its own portability method directly: keep gods titled rather than named, keep the Continent's geography deliberately vague, keep the city compact (four islands) -- so the whole setting drops into any campaign world unmodified. A named, explicit portability technique, distinct from Baur's five-lineage realism taxonomy in BVX.0458."
zotero_key: ""
pdf_pages: 543
status: complete
confidence: high
date_created: 2026-09-29
---

# BVX.1179 — Freeport: The City of Adventure — Chris Pramas et al. (2014)
### Knowledge Entry — Distill

Green Ronin's 543-page Pathfinder-edition core book for Freeport, the "City of Adventure": a single compact city, not a region or nation, engineered from its history down to its crime table to run a whole campaign on its own.

## TABLE OF CONTENTS
- [Core Thesis](#1-core-thesis)
- [Mind Models](#2-mind-models)
- [Framework](#3-framework--structure)
- [Key Concepts](#4-key-concepts)
- [Heuristics](#5-heuristics--decision-rules)
- [Invariants](#6-invariants)
- [Pitfalls](#7-pitfalls--myths)
- [Application](#8-application)
- [Cross-References](#9-cross-references)
- [Provenance](#10-provenance--confidence)

---

## 1 · CORE THESIS

Freeport is a single compact city engineered to carry an entire campaign: a two-thousand-year secret history where every era still bites, a government built to manufacture its own political conflict, and a city whose edges are deliberately vague so it drops into any world unmodified. Depth lives at the center; the frontier is left blank on purpose.

---

## 2 · MIND MODELS

*Required. Minimum two diagrams, maximum five.*

**Diagram 1 — the whole argument.**
Caption: *six design moves, all aimed at the same target -- a city dense enough to run alone, loose enough at the edges to travel anywhere.*

```mermaid
mindmap
  root((Freeport: City<br/>of Adventure))
    Secret history as hook engine
      2000-year present-tense timeline
      Every era still bites now
      Threads left deliberately open
    Government as conflict engine
      Sea Lord vs Captains Council
      Guard vs Watch split
      Council seats keyed to factions
    Districts as class fractal
      Seven districts, one class each
      Numeric settlement stat block
    Multipolar underworld
      One guild smashed in the past
      Three rival bosses now
      Gangs and rackets beneath them
    Portability by vague edges
      Gods titled, never named
      Continent left intentionally blank
      Four-island core kept compact
    Life and culture
      Salt Curse economy
      Pirate code and customs
```

**Diagram 2 — the central mechanism (history converts into live hooks, not settled lore).**
Caption: *every past crisis resolves into a currently active faction or an unresolved tension -- the timeline is a hook generator, not a history lesson.*

```mermaid
flowchart TD
    H1["Thieves' Guild destroyed<br/>in the Back Alley War"] --> C1["No single crime<br/>lord since"]
    C1 --> P1["Three rival bosses<br/>split the underworld"]
    H2["Succession Law repealed<br/>after riots"] --> C2["Orc settlement begins<br/>via Bloodsalt"]
    C2 --> P2["The 'Orc Problem':<br/>unresolved present tension"]
    H3["Salt Curse falls,<br/>three years ago"] --> C3["Wells and rain<br/>turn to brine"]
    C3 --> P3["Rainmakers Group holds<br/>a citywide monopoly"]
    P1 --> Hooks["Every past crisis becomes<br/>a PC-usable faction or crisis"]
    P2 --> Hooks
    P3 --> Hooks
```

**Diagram 3 — mapped onto the Command's SETTING SLICE (S1-S12).**
Caption: *eleven design moves land on eight of twelve SETTING SLICE layers, and the heaviest weight falls on S11 VECTOR -- trajectory kept visibly open rather than resolved.*

```mermaid
flowchart LR
    History["2000-yr present-tense<br/>timeline"] --> S7["S7 FOUNDING"]
    History --> S5["S5 SCAR"]
    Cosmology["Yig / the fall<br/>of Valossa"] --> S5
    Government["Sea Lord vs<br/>Captains' Council"] --> S4["S4 LAW"]
    Underworld["Multipolar<br/>crime bosses"] --> S10["S10 UNDERSIDE"]
    Districts["Class-fractal<br/>districts"] --> S8["S8 HABIT"]
    SaltCurse["The Salt Curse"] --> S6["S6 ECONOMY"]
    CityLife["Sights, sounds,<br/>cuisine"] --> S3["S3 SENSORIUM"]
    Modularity["Vague continent,<br/>titled gods"] --> L7["L7 genre contract"]
    OpenThreads["Unresolved<br/>current events"] --> S11["S11 VECTOR"]
    Allure["Gold is king,<br/>freedom from home"] --> S9["S9 ALLURE"]
```

---

## 3 · FRAMEWORK / STRUCTURE

The book moves from SETTING craft outward to game crunch: a history chapter that doubles as a hook-and-timeline document; one dense city-overview chapter (districts, life, government, law, religion, underworld); ten gazetteer chapters, one per district, stacked with named locations and NPC stat blocks; then a widening lens -- the Serpent's Teeth island chain, an optional and explicitly skippable cosmology/continent chapter, a Denizens roster, races, and finally the Pathfinder-specific rules back half (classes, gear, spells, a dozen ready-to-run one-shots).

| Slot | Content | SETTING weight |
|---|---|---|
| Introduction | States the book's own design goal: portable, system-agnostic at the edges, Pathfinder-specific in the crunch | Design philosophy |
| Ch. I — History | 2,000-year present-tense timeline, ending in unresolved current events | Heaviest: S5, S7, S11 |
| Ch. II — City of Adventure | Districts, life/culture, government, law and order, religion, criminal underworld | Heaviest: S3, S4, S6, S8, S9, S10 |
| Ch. III–XII — District gazetteers | Named locations, NPC stat blocks, businesses, per district | Instances of the Ch. II framework |
| Ch. XIII — Serpent's Teeth | The wider island chain: geography, weather, the sea itself | S1, S2 |
| Ch. XIV — Beyond Freeport | Optional cosmology and continent, explicitly marked skippable | S5, L7 |
| Ch. XV–XVII, XIX–XX | Denizens, races, classes, gear, spells | Game-mechanical, not SETTING |
| Adventures (back matter) | A dozen ready-to-run one-shots keyed to named Freeport sites | Application layer |

---

## 4 · KEY CONCEPTS

| Concept | What it is | Why it matters |
|---|---|---|
| **Present-tense timeline as current-events document** | A single "years before present" table where founding-era events and last-year's events share one format | History and Current Events are not two documents -- the timeline itself is the hook list |
| **Government as conflict engine** | Sea Lord (absolute, life tenure, unimpeachable) checked by a twelve-seat Captains' Council she needs eight votes from | Political tension is wired into the org chart, not improvised per scene |
| **Guard/Watch split** | Two competing law-enforcement bodies: the militarized, human-only Sea Lord's Guard, and the corrupt, all-races Freeport Watch | "The law" is internally divided by design, so PCs can play one against the other |
| **District as class-plus-danger fractal** | Seven districts, each a numeric settlement stat block (Corruption/Crime/Economy/Law/Lore/Society/Danger) built around one class and one hazard | The same city-scale method Cities of Golarion (BVX.1171) runs across six cities, here run once at neighborhood scale |
| **Multipolar underworld** | No single crime boss since the Thieves' Guild fell in the Back Alley War; three rival bosses (Finn, Mister Wednesday, the Helkernas) plus independent gangs now split the city | A deliberately unresolved power vacuum gives PCs factions to play against each other instead of one villain to topple |
| **The Salt Curse** | A three-year-old curse turning all fresh water to brine, solved only by the Rainmakers Group's unexplained immunity | One environmental crisis threaded through economy, daily life, and a single NPC faction's monopoly |
| **Portability by vague edges** | Gods referred to by title, not name; the wider Continent kept deliberately underspecified; the city itself kept to four compact islands | The book's own stated method for dropping one dense city into any GM's existing world without contradiction |
| **The settlement stat block** | A five-to-seven-line numeric identity card (government, size, GP value, population, Corruption/Crime/Economy/Law/Lore/Society, Danger) preceding every district | Compresses a place's whole flavor to a scannable card before a word of prose, echoing Golarion's city header at neighborhood scale |
| **Deliberately unresolved current events** | An empty council seat awaiting a vote, the still-open "Orc Problem" in Bloodsalt, a mystery ship sinking vessels south of the city one year ago | The book refuses to close its own most recent threads -- vector is handed to the GM unfinished on purpose |
| **The pirate's code as legal substrate** | "Do whatever you want on the high seas, but don't go against your fellows in port" -- the informal rule the formal legal system grew out of | Explains why Freeport's law reads as improvised and personal rather than bureaucratic, even where it is codified |
| **Buried history at two scales** | Serpent-people ruins beneath the literal city (Underside chapter) sit under the political capital beneath the Old City -- physical and social undersides stacked | Two kinds of "underside" running in parallel, not one flattened into the other |

---

## 5 · HEURISTICS & DECISION RULES

| Situation | Do this | Not this |
|---|---|---|
| Writing a setting's history | Write a present-tense timeline where the most recent entries are still open questions | Write history that stops cleanly with "and so it has been ever since" |
| Designing a ruling body | Split power between a figurehead and a council that needs a real vote count to act | Give one ruler unchecked authority with no in-fiction friction |
| Building law enforcement | Split it into two competing bodies with different loyalties, recruiting rules, and reputations | Write a single unified police force with one culture |
| Building a criminal underworld | Break the last dominant syndicate in the backstory and leave several rivals splitting the wreckage | Install one crime boss who owns the whole underworld uncontested |
| Making a setting travel to other campaigns | Keep names generic at the edges (titled gods, a vague wider world) and dense at the center (the one city) | Fully name and fix every god, nation, and neighbor before anyone needs them |
| Giving a district identity fast | Assign one social class and one hazard, then give it a numeric stat-block header | List buildings and population without a class or danger throughline |
| Threading an economic crisis | Run one environmental or resource crisis through daily life, factions, and a single beneficiary faction | Treat economy as a flat price list disconnected from any character or conflict |
| Ending a history/current-events section | Stop on an unresolved vote, an open investigation, or an unexplained recent event | Stop on a tidy resolution that leaves nothing for the GM to finish |

---

## 6 · INVARIANTS

1. **A setting's history is also its hook list.** If an event from the past doesn't explain something active today, it doesn't belong in the present-tense timeline.
2. **A ruling structure without an internal check is inert.** The Sea Lord/Council split, and the Guard/Watch split beneath it, exist because unopposed authority generates no story.
3. **A criminal underworld needs more than one boss to be playable.** A single all-powerful crime lord forecloses faction play; several rivals splitting a recent power vacuum invites it.
4. **Depth at the center requires vagueness at the edge.** The city can be dense only because the wider world around it is deliberately left thin enough to bend to any GM's existing setting.
5. **A district (or any sub-unit) is a class and a danger level first, an architecture second.** The numeric stat-block header states both before a word of description follows.
6. **The most recent history should be the least resolved.** Ending on an open thread, not a closed one, is what makes "current events" different from "backstory."
7. **One crisis can carry economy, daily life, and a faction's power all at once.** The Salt Curse does the work three separate sections would otherwise need.

---

## 7 · PITFALLS / MYTHS

- Writing history that reads as complete and closed, leaving the GM nothing live to hook a session onto.
- Letting one crime boss, cult, or faction quietly own an entire underworld or opposition layer, which kills faction-vs-faction play before it starts.
- Naming and fixing every neighboring nation, deity, and border before any of them is dramatically necessary, closing off the portability the design otherwise buys.
- Treating a settlement stat block as flavor text rather than as the two-line conceit every later section has to answer to.
- Splitting law enforcement into two bodies but forgetting to give them different loyalties, cultures, and blind spots -- the split does no work if both sides behave identically.
- Resolving an environmental or economic crisis fully in the text instead of leaving its beneficiaries and losers as material for play.
- Assuming "systemless" and "portable" mean thin; Freeport is both maximally portable at its edges and maximally dense at its center, not vague throughout.

---

## 8 · APPLICATION

- **Spine level:** SETTING (non-story-spine source; keys to the entity beside the L0-L7 spine, per ssot_03's binding rule that setting is a Domain embodied, never a level)
- **12-layer character stack:** none directly -- a setting-side source; its faction-keyed council seats and named crime bosses are ready seeds if any were promoted into an actual character stack, but the entry itself does not feed a character layer
- **plot_systems:** primary candidate once `04_PLOT_SYSTEMS/` opens -- Diagram 2's history-to-hook chain (event → present consequence → live hook) is a directly reusable generator: take any past crisis in a drafted setting and force it through the same three-step chain before trusting it playable
- **Setting:** primary -- the founding SETTING-shelf entry built around a *single* city as an entire campaign's engine rather than a template run across several (BVX.1171) or a worldbuilding theory (BVX.0458)

The book's most importable move for a science-fiction setting system is the present-tense-timeline-as-current-events-document technique in Diagram 2: write a setting's backstory as a chronological table, but hold every entry to the same test -- does it explain something active right now -- and let the most recent entries stay visibly unresolved rather than wrapping up. A DCUS write-up (or any DCUS-adjacent institution) could run its own founding-through-rebrand history through exactly this test: the rename lattice (Red Stick Creek → Red Hills → DCUS) already reads as this book's Back Alley War equivalent -- a past crisis that explains a present absence (no legacy name survives cleanly) -- but the technique asks for one further step this SSOT hasn't yet taken: an explicitly *unresolved* thread at the most recent end of the timeline, the way Freeport ends on an empty council seat and an unexplained ship sinking vessels a year ago, rather than closing the history at the current Movement's state. The second importable move is the portability method itself (Diagram 3, L7): titled-not-named gods and a deliberately underspecified wider world are what let a single dense city relocate into any campaign, a genre-neutral technique for keeping a setting's core load-bearing while its context stays swappable.

---

## 9 · CROSS-REFERENCES

| Related entry | Relation |
|---|---|
| [[BVX.0458]] | Kobold Guide to Worldbuilding -- theory counterpart; Freeport is the present-tense-history rule taken to book length and given an explicit portability method (titled gods, vague continent) the theory text only gestures at |
| [[BVX.1171]] | Cities of Golarion -- template sibling; both use a numeric settlement stat block and a class-plus-danger district method, but Golarion runs one template across six shallow cities while Freeport runs the same depth into a single city built to be an entire campaign |
| [[BVX.1122]] | GURPS Hot Spots: Renaissance Venice -- single-deep-city sibling; Venice is the historical-grounding end of the single-city method, Freeport the invented-portable-pirate-city end, both worked examples at the same depth |
| [[BVX.0067]] | Collaborative Worldbuilding for Writers and Gamers -- undistilled SETTING-shelf sibling, same craft-not-theory register |

---

## 10 · PROVENANCE & CONFIDENCE

Full text, pdftotext extraction, 543pp, clean text layer with a machine-readable table of contents. Read in full: the Introduction; the complete History chapter (Chapter I, including the "A Freeport Timeline" table); the complete City of Adventure overview (Chapter II: Lay of the Land/Districts, Getting Around, Life in Freeport, Government, Sea Lord's Guard, the Admiralty, Law and Order/Freeport Watch, Crime and Punishment, Religion, Criminal Underworld); and the cosmology-and-portability-statement passages opening Chapter XIV (Beyond Freeport: "In the Beginning," "The World of Freeport," the stated design rationale for keeping the Continent deliberately vague). Sampled via targeted grep and ranged reads: the opening of the Docks gazetteer chapter (Chapter III, confirming the per-district settlement stat block format repeats). Not separately read: the remaining nine district gazetteer chapters (IV-XII, largely named-location and NPC stat-block listings), the Denizens/Races chapters (XV-XVI), the Pathfinder-specific game-mechanical chapters (Classes, Skills, Feats, Spells, Magic Items, Chapter XVII-XX), and the ready-to-run adventure back matter -- all outside this distill's SETTING-shelf scope (craft method, not game statistics or individual NPC write-ups).

The S-layer keying in frontmatter `feeds:` and Diagram 3 is this distill's synthesis against `ssot_03_setting_system.md` (PART A, the twelve-layer SETTING SLICE), read directly to confirm the S1-S12 names and the S2 WEATHER canon-thin flag already on record for DCUS. The `spine: [SETTING]` and empty character-stack application are asserted per the v4 template's binding rule (setting is an entity beside the spine, never an L0-L7 level).

## META
- Template: BVX-LEARN-v4.0
- Source classification: full-text sourcebook, deep extraction on introduction + history + city-overview chapter + cosmology opening, sampled on 1 district chapter, summarized (not extracted) on game-mechanical back matter
- Created / Updated: 2026-09-29
