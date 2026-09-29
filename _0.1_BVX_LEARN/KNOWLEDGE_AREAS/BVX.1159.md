---
id: BVX.1159
bvx_provisional: true
title: "Dark Skies: Space Expansionism, Planetary Geopolitics, and the Ends of Humanity"
author: "Daniel Deudney"
year: 2020
type: distill
source_type: book
subjects: [POL, MIL]
primary_subject: POL
trunk: BLACK
spine: [SETTING, L6]
feeds:
  - layer: SETTING
    variable: S4_law
    strength: primary
    note: "Full geopolitical theory's triangular typology (anarchy / hierarchy / negarchy, Fig. 8.2) plus the violence-interdependence spectrum (Table 8.2) is a drop-in method for deciding what government a space faction actually runs, keyed to material context (distance, weapons volume, frontier status), not to authorial convenience."
  - layer: SETTING
    variable: S6_economy
    strength: primary
    note: "The Von Braun (military) and Tsiolkovsky (habitat) ladders name concrete dual-use tech tiers (asteroid movers, mass drivers, orbital solar power, terraforming mirrors) where the economic infrastructure and the weapon are the same object. Economy and war-fighting capacity should be designed as one line, not two."
  - layer: SETTING
    variable: S9_allure
    strength: primary
    note: "Space expansionism described as a 'science-based and technology-dependent religion': the Promethean cosmic-destiny narrative (ascent, apotheosis, species vocation) is the in-universe recruiting pitch for any expansionist faction. What it promises members is exactly what makes people want in."
  - layer: SETTING
    variable: S11_vector
    strength: primary
    note: "Table 10.1's four-stage colonization ladder (Earth-dependent outposts to galactic diaspora) is a ready-made setting arc for scaling a space polity's political maturity, population, and danger level across a campaign's Movements. Each stage is a state overlay, not a rewrite."
  - layer: SETTING
    variable: S5_scar
    strength: supporting
    note: "The 'Great Wall of Earth' / garrison-state consolidation scenario and the axial-region-capture mechanic (whoever holds the chokepoint tends toward dominance unless it is deliberately neutralized) generate erasure-lattice history at civilizational scale: a captured chokepoint becomes the founding wound of the next political order."
  - layer: L6
    variable: controlling_idea
    strength: contextual
    note: "The title's own double meaning, 'the ends of humanity' as both destiny (telos) and termination (extinction), is a ready controlling-idea spine for a space-set story's theme: does reaching for the stars fulfill the species or doom it. Institutional Prometheanism as hubris, not one character's flaw."
zotero_key: ""
pdf_pages: 425
status: complete
confidence: high
date_created: 2026-09-29
---

# BVX.1159 — Dark Skies: Space Expansionism, Planetary Geopolitics, and the Ends of Humanity — Daniel Deudney (2020)
### Knowledge Entry — Distill

A political scientist's book-length argument that space expansion is not automatically progress. Applying "full geopolitical theory" to the actual and proposed military and habitat space programs, Deudney concludes both tend toward war, garrison hierarchy, or despotic colonies: a systematic, citable machine for building a space setting's politics rather than decorating one.

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

Space expansionists treat technological ascent off Earth as destiny and salvation. Full geopolitical theory says political order is set by material context, not intention: violence interdependence, distance, and open frontiers decide whether a place lands in anarchy, hierarchy, or restrained freedom. Every rung of the space ladder trends toward war or garrison rule, rarely toward freedom.

---

## 2 · MIND MODELS

*Required. Minimum two diagrams, maximum five.*

**Diagram 1 — the whole argument.**
Caption: *the book runs one argument four times: Earth's political debates, the space environment, the two live rival programs (military and habitat), and geopolitical theory's verdict on both.*

```mermaid
mindmap
  root((Dark Skies))
    Part 1: Earth closing
      Archipelago to Planetary Earth
      Seven great debates
    Part 2: Horizons
      Astrography of near and solar space
      Feasibility and catastrophe syndromes
    Part 3: The rival programs
      Von Braun: military ladder
      Tsiolkovsky: habitat ladder
      Clarke-Sagan: planetary security critics
    Part 4: The verdict
      Full geopolitics: twelve propositions
      Earth Space: garrison or restraint
      Solar Space: the dark skies of colonization
    Conclusion
      Double NOPE
      Earth-oriented program
```

**Diagram 2 — the central mechanism.**
Caption: *both roads up the gravity well feed the same variable, violence interdependence. Past a threshold, anarchy stops being survivable, and hierarchy wins that opening far more often than restrained union does.*

```mermaid
flowchart TD
    MIL["Von Braun ladder:<br/>bombardment to orbital dominance"] --> VI
    HAB["Tsiolkovsky ladder:<br/>orbital rings to galactic diaspora"] --> VI
    VI["Violence interdependence:<br/>absent to intense"] --> GOV{"Is anarchy still survivable?"}
    GOV -->|"absent or weak"| FREE["Anarchy tolerable,<br/>freedom possible"]
    GOV -->|"intense"| EXIT["Exit from anarchy required"]
    EXIT --> WHO{"Who or what fills the exit?"}
    WHO -->|"power concentrates"| HIER["Hierarchy:<br/>empire, garrison state"]
    WHO -->|"mutual restraint holds"| NEG["Negarchy:<br/>republic, union"]
    WHO -->|"restraint fails"| WAR["War-prone anarchy persists"]
    HIER --> RARE["Freedom: rare,<br/>hard-won, easily lost"]
    NEG --> RARE
```

**Diagram 3 — the colony-government decision tool.**
Caption: *plot any faction's colony charter by two questions, how tight are survival constraints and how real is interworld war, and Deudney's four historical camps predict its government type.*

```mermaid
quadrantChart
    title Four camps on space colony government
    x-axis Situation constrained --> Situation permissive
    y-axis War discounted --> War is severe threat
    quadrant-1 Democracy by mutual vulnerability
    quadrant-2 Forced-to-be-free federation
    quadrant-3 Hierarchical collectivism
    quadrant-4 Plural freedom, war ignored
    Cole and Cox: [0.7, 0.75]
    Crawford and Baxter: [0.3, 0.8]
    Bernal and Cockell: [0.25, 0.3]
    ONeill Dyson Zubrin: [0.75, 0.2]
```

**Diagram 4 — the setting arc.**
Caption: *read as a campaign-arc ladder: each stage adds population and political reach while shrinking the mother world's relative power. Past a point, "the colony rebels" stops being a plot choice and starts being physics.*

```mermaid
stateDiagram-v2
    [*] --> StageOne
    StageOne --> StageTwo: self-sufficiency reached
    StageTwo --> StageThree: species radiation begins
    StageThree --> StageFour: interstellar ventures begin
    StageFour --> [*]
    note right of StageTwo: violence interdependence and<br/>Earth's relative power invert here
```

**Diagram 5 — mapped onto the Command's SETTING SLICE.**
Caption: *five load-bearing claims sorted onto the SETTING SLICE and the story-spine's Theme level — a setting-politics starter kit, not a footnote.*

```mermaid
flowchart LR
    VI["Violence interdependence +<br/>political order typology"] --> S4["S4 LAW"]
    LADDERS["Dual-use tech ladders<br/>(military and habitat)"] --> S6["S6 ECONOMY"]
    PROM["Promethean cosmic-destiny<br/>narrative"] --> S9["S9 ALLURE"]
    STAGES["Four-stage colonization<br/>ladder"] --> S11["S11 VECTOR"]
    WALL["Garrison consolidation,<br/>Great Wall of Earth"] --> S5["S5 SCAR"]
    ENDS["'Ends of humanity':<br/>destiny or extinction"] --> L6["L6 THEME"]
```

---

## 3 · FRAMEWORK / STRUCTURE

Ten chapters in four parts, each part answering one question in the chain. Part One ("The Earth, Technology, and Space") surveys what has actually happened in space and names seven live debates on "Planetary Earth": anarchy vs. world government, closure vs. frontier, freedom vs. technocracy, that space choices will help decide either way. Part Two ("Geographic and Technological Horizons") maps the astrography of near and solar space and audits which expansionist technologies are actually feasible. Part Three ("Space Expansionism") profiles the two live rival programs in full: military (the Von Braun ladder) and habitat (the Tsiolkovsky ladder), plus the underrecognized "planetary security" critics (arms controllers, environmentalists). Part Four ("Assessment") builds "full geopolitical theory," twelve propositions relating material context to political order, and fires it at Earth orbital space, then at solar space, then states a counter-program.

---

## 4 · KEY CONCEPTS

| Concept | What it is | Why it matters |
|---|---|---|
| **Space expansionism** | The dominant body of thought (Tsiolkovsky, von Braun, O'Neill, Musk, Bezos) holding that large-scale human movement off Earth is desirable, necessary, and near-inevitable | The setting's default in-universe ideology for any expansionist faction, named, sourced, and ready to be dramatized rather than invented from scratch |
| **Full geopolitics** | Arguments about how material context (geography plus technology) shapes which political arrangements are viable, especially around violence and freedom; broader than "great-power politics" | The book's actual method: a checklist for deriving a faction's plausible government from its situation instead of asserting one |
| **Violence interdependence (VI)** | The capacity of actors in a space to damage one another, independent of who has more weapons; runs absent, weak, strong, then intense | The single variable that decides whether anarchy is livable; VI rising past "intense" makes some exit from anarchy necessary for security |
| **Anarchy / hierarchy / negarchy** | A triangular typology of political order: no government; concentrated top-down rule (empire, despotism); and "negarchy," Deudney's term for republics and their unions, where power is distributed but mutually restrained | Most fictional space governments are drawn from only two of these three poles; negarchy is the hard, rare, deliberately engineered case |
| **The Von Braun ladder** | Five-step military space program, read bottom-up: ballistic missiles, then force-multiplying satellites, orbital fighting, space control, and finally planetary hegemony via an "Earth Net" | A concrete tech-tier list for a setting's military-space arc, and a warning that "defensive" orbital infrastructure is also a hegemony tool |
| **The Tsiolkovsky ladder** | Seven-step habitat program: Fuller Earth, then Ehricke-Glaser-Lewis orbital rings, Bernal-O'Neill orbital cities, Mars (Zubrin), asteroid diaspora (Cole), outer-system colonization (Dyson), and interstellar migration (Goddard) | The setting's habitat-expansion tech tree, each rung with a named real-world visionary and stated rationale, ready to reskin |
| **Ships vs. cities** | Ships are governed as hierarchical technocracies (a captain, obedience, no democracy) because catastrophic failure is instant; cities can sustain republics because proximity enables organizing | The load-bearing design question for any enclosed space habitat: will the astropolis be a ship or a city? The answer sets its whole politics |
| **Species radiation / posthuman drift** | Habitat expansionism's endpoint: genetic and cybernetic divergence produces multiple non-interbreeding "spacekind," and the ideology's beneficiary silently shifts from humanity to "life itself" | A built-in faction-generator for interspecies or post-human political blocs, plus a theme hook: the program that starts to save humanity ends by discarding it |
| **Island Earth in the Solar Archipelago** | Once colonies are large and independent, Earth becomes one polity among many, its relative power shrinking, its likely response a hierarchical "garrison state" | A late-campaign reversal: the cradle world stops being the center and starts playing catch-up or defense |
| **Catastrophic threat taxonomy** | Six named ways large-scale space expansion itself manufactures new existential risk: malefic geopolitics, natural-threat amplification, restraint reversal, hierarchy enablement, alien generation, monster multiplication | A menu of setting-level dangers that are consequences of success, not sabotage, useful for antagonist design that doesn't need a villain |
| **Double NOPE** | Deudney's counter-program: "Not On Planet Earth" (no more planet-wrecking tech) plus "Not Off Planet Earth" (no ambitious colonization) | The dissenting faction's platform: an Earth-centered, restraint-first politics to set against every expansionist power bloc |

---

## 5 · HEURISTICS & DECISION RULES

| Situation | Do this | Not this |
|---|---|---|
| Deciding a space faction's government | Run it through Diagram 3: how constrained is survival, how real is interworld war | Assign "democracy" or "empire" because it fits the faction's vibe |
| Designing a resource-extraction technology (asteroid movers, mass drivers, orbital energy) | Build in its weapon use from the start: dual-use is the default, not the exception | Write a peaceful economic technology with no military shadow |
| Writing a colony's founding charter | Show it drift under the environment's real pressure (isolation, fragility, technocratic necessity) | Assume a well-written constitution holds regardless of circumstance (the "Good Seed" fallacy) |
| Placing a frontier zone (asteroid belt, unclaimed orbit, new colony world) | Make it violent, weakly propertied, and prone to core/periphery conflict by default | Write frontiers as empty opportunity with no one fighting over them yet |
| Building an interstellar or interplanetary federation | Weight it against distance, travel-time lag, and how different the member polities have become | Assume shared origin guarantees political union (the American-founding analogy oversells) |
| Escalating danger across a campaign | Raise violence interdependence stepwise (Diagram 4's four stages), not the enemy's numbers | Keep threat flat and just add bigger ships |
| Writing an expansionist faction's ideology | Give it the Promethean register: cosmic destiny, species vocation, impatience with doubters | Write "we need resources" as the whole motive; the real sell is salvation |
| Placing a strategic chokepoint (orbital ring, wormhole, single habitable moon) | Make control of it decide the whole region's political order, unless someone deliberately neutralizes it | Let a chokepoint exist without anyone contesting or weaponizing it |
| Writing a "peaceful" orbital megastructure | Ask who it would let dominate the planet below if seized, before deciding it is benign | Treat size and utility as automatically good for everyone |

---

## 6 · INVARIANTS

1. **Political order is a function of material context, not intention.** Violence interdependence, distribution of power, and frontier status set what government is *possible*, before anyone's virtue or vice enters in.
2. **An uncontrolled axial region (chokepoint, orbital ring, single habitable world) tends toward domination unless someone deliberately neutralizes it.** Control is never neutral by default.
3. **Frontiers generate conflict by structure, not by author choice.** Weak property claims plus core/periphery power asymmetry produces violence in any open system.
4. **Enclosed, fragile habitats default to technocratic hierarchy.** The tighter the coupling between political dissent and catastrophic failure, the harder political freedom becomes to sustain.
5. **Dissimilar polities, by species, technology, or circumstance, conflict more and cooperate less.** Divergence (biological, cybernetic, or merely cultural) is itself a geopolitical fact, not set dressing.
6. **Every "solution from space" presupposes a prior definition of the Earth problem it solves.** A faction's stated space policy always reveals its politics about the home world first.
7. **Success enlarges danger faster than institutions can restrain it.** The gravest outcomes in this book come from expansion working, not from it failing.

---

## 7 · PITFALLS / MYTHS

- Treating "more space, more freedom" as automatic — the geopolitical evidence runs the other way more often than not.
- Writing a resource-moving or defensive technology with no weapon application in mind; in this book's logic, almost none exist.
- Building an interstellar senate or federation without pricing in effective distance — travel-time lag, not shared ancestry, is what breaks unions (the failed British Imperial Federation is the closer analog than the American founding).
- Confusing absolute distance with *effective* distance: what technology can traverse quickly is "close," regardless of the number of light-years.
- The "Benign Parent Model": assuming a homeworld or corporation will nurture a colony toward independence rather than keep it small, dependent, and profitable.
- Giving an expansionist ideology only material motives (resources, Lebensraum) and skipping its self-description as salvation, destiny, or evolution's next step — the seduction is the point.
- Letting a "peaceful" megastructure exist without asking who it would let dominate everyone else if captured.

---

## 8 · APPLICATION

- **Spine level:** SETTING, primary; L6 (Theme) secondary — a setting-side source whose central claim ("success breeds domination, not freedom") is also a ready-made controlling idea for a space-set story's theme.
- **12-layer character stack:** none directly load-bearing, though Table 2.1's five-position technopolitical spectrum (Promethean, Techno-Optimist, Soterian, Friend of the Earth, Luddite) is a fast way to season an individual character's or faction's stated worldview without inventing one from nothing.
- **plot_systems:** strong contextual candidate once `04_PLOT_SYSTEMS/` opens — the axial-region-capture mechanic (Diagram 2) and the four-stage colonization ladder (Diagram 4) are both ready scene- and arc-generators: "who controls the chokepoint" and "which stage is this Movement" are reusable structural questions.
- **Setting:** primary — this is a SETTING-shelf source keyed to S4 LAW, S5 SCAR, S6 ECONOMY, S9 ALLURE, and S11 VECTOR (see `feeds:` above), the first distilled source in the library to carry a systematic *method* for deriving a space-faction's politics from its material situation rather than asserting a government type by narrative fiat.

Read against the SETTING SLICE (`ssot_03_setting_system.md`), this book's real export is Diagram 2's mechanism: violence interdependence, not narrative convenience, should decide whether a space setting's polities land in anarchy, hierarchy, or the rare negarchic union. Every other tool in the book — the two expansion ladders, the colony-government typology, the colonization-stage arc, the catastrophic-threat taxonomy — is that same mechanism applied to a specific setting layer. Where the Kobold Guide ([[BVX.0458]]) supplies the terrain-first method for building a world's geography and culture, Dark Skies supplies the equivalent method for a *space* setting's politics specifically: it is the TTRPG designer's missing chapter on "how do I know what government my orbital colony has," answered with a checklist instead of a guess.

---

## 9 · CROSS-REFERENCES

| Related entry | Relation |
|---|---|
| [[BVX.0458]] | Kobold Guide to Worldbuilding — the master SETTING-shelf toolkit this entry plugs into; Kobold gives terrain-first method generally, Dark Skies gives the political-order method for space settings specifically |
| [[BVX.1122]] | GURPS Hot Spots: Renaissance Venice — direct textual convergence: Deudney names Venice as the strongest historical analog for a free "city-ship" colony, against the default expectation of shipboard hierarchy |
| [[BVX.1141]] | Stars Without Number — sci-fi TTRPG core rulebook; this entry's colony-government typology and dual-use tech ladders are a ready political layer to run underneath that system's sector generation |
| [[BVX.1142]] | Cities Without Number — sibling sci-fi TTRPG core rulebook; the ships-vs-cities distinction and garrison-state trajectory apply directly to its urban/cyberpunk settings once they go orbital |
| [[BVX.0349]] | Against Worldbuilding, and Other Provocations — counter-argument sibling; Dark Skies independently arrives at the same warning (systems built for their own sake, divorced from pressure, mislead) but from political science rather than craft criticism |

---

## 10 · PROVENANCE & CONFIDENCE

Full text, plain-text extraction from PDF (page-number and running-header artifacts throughout; a recurring ligature-stripping quirk drops "Th" at the start of words, e.g. "e Promise of Space Revisited" for "The Promise of Space Revisited" — cosmetic, does not affect the content extracted below). Read in full or substantially: the Prologue; Chapter 1 ("The Promise of Space Revisited"); Chapter 2 ("Questions, Debates, and Frameworks" — all seven Planetary Earth debates and the Technopolitical Alternatives spectrum, Table 2.1); Chapter 5 ("Absolute Weapons, Lightning Wars, and Ultimate Positions" — the Von Braun ladder and ballistic-missile-as-space-weapon argument, through Table 5.2); Chapter 6 ("Limitless Frontiers, Spaceship Earths, and Higher Humanities" — the Tsiolkovsky ladder, ships-vs-cities politics, the colony-government typology at Figure 6.4, and the species-radiation/posthuman-drift argument); Chapter 8 ("Geography, Geopolitics, and Geohistory" — full geopolitical theory's assumptions, the violence-interdependence and political-order typology at Table 8.2 and Figure 8.2, the twelve propositions at Table 8.3, and the three-Earths geohistorical test); the Earth Net / hegemony-feasibility section of Chapter 9; the bulk of Chapter 10 ("Solar Space, Island Earth, and the Ends of Humanity" — the four-stage colonization ladder at Table 10.1, the seven "Solar Geopolitics" sections, and the catastrophic-threat taxonomy at Table 10.3); and the Conclusion ("Illusions and Evasions" through the Earth-oriented program at Table C.1). Not deep-extracted: Chapter 3's astrography detail, Chapter 4's ten-threat feasibility survey, Chapter 7's arms-control critique in full, and the remainder of Chapter 9's geography-error corrections — these carry the book's technical feasibility and arms-control argument rather than its setting-political method, and were sampled via the chapter map (Ch. 2's "Map of the Chapters" section) rather than read in depth, per the brief's focus on political consequences over engineering feasibility.

The SETTING and L6 keying in frontmatter `feeds:` and Diagrams 3–5 is this distill's own synthesis against `ssot_03_setting_system.md` (the SETTING SLICE, S1–S12) and `ssot_01_story_spine_comparative_tree.md`'s definition of L6 as Theme; this is the library's first source keyed to space-political geopolitics specifically, so no prior distill anticipated this mapping. `bvx_provisional: true` and the new `id` are set per this task's instruction; the book carries no Zotero key at time of writing.

## META
- Template: BVX-LEARN-v4.0
- Source classification: full-text PDF extraction, deep extraction on 6 of 10 chapters plus Prologue and Conclusion, sampled via chapter map on the remainder
- Created / Updated: 2026-09-29
