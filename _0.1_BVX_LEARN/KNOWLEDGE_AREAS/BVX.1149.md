---
id: BVX.1149
title: "Society Must Be Defended: Lectures at the Collège de France 1975-76"
author: "Michel Foucault"
year: 2003
type: distill
source_type: book
subjects: [PHI, POL]
primary_subject: PHI
trunk: BLACK
spine: [L6]
bvx_provisional: true
feeds:
  - layer: L6
    variable: controlling_idea_biopower
    strength: primary
    note: "The lecture of 17 March supplies the exact machinery of a biopower controlling idea: sovereignty's 'take life or let live' is complemented (not replaced) by a new right, 'make live and let die.' A story arguing biopower needs both registers on screen at once, the old sword-right and the new administrative one, or the argument flattens into a simple tyranny story."
  - layer: L6
    variable: theme_as_structure
    strength: primary
    note: "The 7 January method lecture models theme as a tested value, not a stated message: genealogy builds its claim ('power is not reducible to the economy or to law') by tracing a struggle across concrete cases, never by asserting it. A controlling idea should be built the same way — proven by what the plot does to the value, not announced by a character."
  - layer: L6
    variable: state_racism_mechanism
    strength: primary
    note: "Racism's two functions (17 March): first, cut the population into a part that must live and a part that may die; second, convert that cut into a formula where the death of the other makes 'me' (as species, not individual) stronger. Any plot mechanism that sorts a cast into the protected and the exposed, and frames the sorting as health rather than conquest, is running this exact function and can be named as such."
  - layer: L6
    variable: norm_as_hinge
    strength: supporting
    note: "The norm is named as the single term that runs on both registers at once — the thing that disciplines a body and regularizes a population with the same yardstick. A biopower story's scenes of measurement, screening, and classification are where the norm is doing its work; this is the connective tissue between an individual plot and a population-level stake."
  - layer: L6
    variable: death_privatized
    strength: contextual
    note: "The Franco anecdote: a sovereign killer dies inside a power that specializes in making live, and doesn't notice his own death because that power has stopped recognizing death as an event. Usable as a scene-level device — a character who wields old-style life-and-death power finds it has no purchase inside the system he built, and the system quietly outlives him."
  - layer: DRAMATICA
    variable: throughline_argument
    strength: contextual
    note: "The Course Summary's four questions (is war the primal state, does antagonism derive from it, can tactics analyze power, are war-institutions the nucleus of politics) are the same interrogation Dramatica runs on a storyform's premise before trusting it: state the claim as a question, then test whether the material actually answers it, rather than assuming the frame is self-evident."
zotero_key: ""
pdf_pages: 306
status: complete
confidence: high
date_created: 2026-09-29
---

# BVX.1149 — Society Must Be Defended — Michel Foucault (2003 English ed.)

### Knowledge Entry — Distill

Foucault's 1975-76 Collège de France course, the lecture series where "biopower" and "state racism" are coined; read for BOLO 80, the theme system, as the founding text behind the story universe's controlling idea, biopower — power that manages life itself.

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

Sovereign power took life or let live; from the nineteenth century on, a new power learned to make live and let die, managing birth, health, and population rather than commanding death. Racism is the mechanism that lets this life-making power still kill: it cuts a population into a part that must live and a part that may die, then frames the second death as the first part's health.

---

## 2 · MIND MODELS

*Required. Minimum two diagrams, maximum five.*

**Diagram 1 — the whole argument.**
Caption: *the course runs one investigation (is power war?) through two lectures worth keeping — the method lecture that licenses "history from below," and the biopower lecture that is its final payoff.*

```mermaid
mindmap
  root((Society Must<br/>Be Defended))
    Method - 7 Jan
      Subjugated knowledges
      Genealogy as antiscience
      Against economism
      Clausewitz inverted
    War as history's grid
      Race war narrative
      Nation absorbs the race war
      Class struggle inherits it
    Biopower - 17 Mar
      Sovereignty: take life or let live
      Biopower: make live and let die
      Discipline and regulation
      The norm as hinge
    State racism
      Caesura within the species
      Death of other = life of race
      Nazism as paroxysm
      Socialism's unexamined racism
```

**Diagram 2 — the central mechanism (a state change: how a life-making power still kills).**
Caption: *racism is not an attitude here, it is the load-bearing joint — remove it and a biopower state has no way to justify a single death.*

```mermaid
stateDiagram-v2
    [*] --> Sovereignty
    Sovereignty: Take life or let live
    Sovereignty --> Biopower: 18th-19th c. new right added, not swapped
    Biopower: Make live, manage population
    Biopower --> Blocked: Killing needs a justification biopower can't supply
    Blocked --> Racism: Cut population into must-live / may-die
    Racism --> Justified: Their death reads as our health
    Justified --> Biopower: Killing resumes, now as care
```

**Diagram 3 — mapped onto the Command's L6 controlling-idea layer.**
Caption: *the course hands the story universe a ready-built argument engine — plug a cast's protected/exposed line into the mechanism and the theme is already load-bearing, not decorative.*

```mermaid
flowchart LR
    SovRight["Sovereign right:<br/>take life or let live"] --> L6a["L6: the old power<br/>a character still believes in"]
    Biopower["Biopower:<br/>make live and let die"] --> L6b["L6: the system<br/>actually running the world"]
    Norm["The norm<br/>(screens, scores, thresholds)"] --> L6c["L6: scenes where the<br/>argument becomes visible"]
    Racism["State racism:<br/>the must-live/may-die cut"] --> L6d["L6: the plot mechanism<br/>that tests the controlling idea"]
```

---

## 3 · FRAMEWORK / STRUCTURE

The course runs eleven lectures (7 January to 17 March 1976) as one continuous argument, not a set of separate topics:

| Stage | Lectures | Move |
|---|---|---|
| Method | 7 January | States the whole year's method: genealogy as "insurrection of subjugated knowledges," and the two off-the-cuff hypotheses about power (Reich's repression, Nietzsche's war) that the course will test against each other. |
| War-as-history's-grid | 14 January – 4 February | Builds and interrogates a "race war" discourse (Boulainvilliers, Coke) that reads all of history as one people's war against another, prior to and beneath the law. |
| Absorption | 11 February – 3 March | Traces how the race-war discourse gets absorbed and inverted by nation-state history on one side, and by class struggle on the other — the war frame survives, its "races" don't. |
| Payoff | 10-17 March | Delivers the course's destination: state racism as the mechanism that lets a life-administering power still kill, worked through Nazism and then socialism. |

The 7 January method lecture and the 17 March payoff lecture are the two load-bearing pillars; the middle lectures are the historical scaffolding the argument is built on, useful for provenance but not required to use the payoff.

---

## 4 · KEY CONCEPTS

| Concept | What it is | Why it matters |
|---|---|---|
| **Subjugated knowledges** | Two kinds of buried knowledge: erudite historical content masked by systematizing theory, and "disqualified" local/naive knowledge (the patient's, the delinquent's) beneath official science | Genealogy's method: put the buried and the disqualified back in contact to write "a historical knowledge of struggles" — the model for building a theme from concrete instances rather than a stated moral |
| **Genealogy as antiscience** | Not a rival science, but an insurrection against the *power-effects* of any discourse that claims scientific status | Explains why a controlling idea should be demonstrated through struggle and consequence, not delivered as an authoritative pronouncement inside the story |
| **Clausewitz inverted** | "Politics is the continuation of war by other means" — peace, law, and institutions are read as war continuing by other channels, not war's opposite | The founding move of the whole course: civil order is a frozen battle, not an escape from one; every institution can be reread as a position in an ongoing struggle |
| **Sovereign right (take life or let live)** | Classical sovereignty's asymmetric right: the sovereign's power over life shows itself only in the right to kill; granting life is not symmetrically a "right" exercised | The baseline the new power modifies rather than replaces — old-style sovereign killing keeps operating underneath and inside biopower |
| **Biopower (make live and let die)** | A power targeting "man-as-species": birth rate, mortality, longevity, health, environment, aimed at a population rather than individual bodies | The nineteenth century's new technology of power; it manages a population statistically rather than commanding individual bodies |
| **Discipline vs. regulation** | Discipline individualizes (drilled bodies, surveillance, institutions); regulation is "massifying" (statistics, forecasts, homeostasis at population scale) | Two technologies that don't replace each other but interlock — a single site (a housing estate, a sexuality) can be worked by both at once |
| **The norm** | The single measure that runs through both discipline and regulation — the same standard disciplines a body and regularizes a population | The hinge concept: wherever a story stages measurement, screening, or classification, discipline and regulation are meeting at the norm |
| **State racism** | Not ordinary racial hatred, but the mechanism that (1) cuts the biological continuum into subspecies, must-live and may-die, then (2) converts "the other's death" into "my (species) life" | The course's destination concept: this is *how* a life-administering power kills without contradicting its own logic |
| **Death privatized** | Once power's business is to make live, death falls outside its reach; death stops being a public transfer of power and becomes the most shameful private fact | Explains a structural feature available to any biopower story: a sovereign-style killer inside a biopower regime can die without the regime even registering the death as an event (the Franco anecdote) |
| **Nazism as paroxysm** | The one State where absolute biopower (total disciplinary and regulatory control of the population) and absolute sovereign killing coincide exactly — "a racist State, a murderous State, and a suicidal State" | The extreme case that makes the general mechanism visible; useful as a limit-case check, not a template to imitate literally |
| **Socialism's unexamined racism** | Foucault's controversial claim: socialism never critiqued the biopower mechanism itself, only who should run it, so it reproduces the racist justification whenever it must fight a physical enemy rather than an economic one | A warning against any faction in a story that claims to oppose the biopower regime while leaving its administrative machinery, and its need to justify killing, completely intact |

---

## 5 · HEURISTICS & DECISION RULES

| Situation | Do this | Not this |
|---|---|---|
| Building a biopower antagonist or system | Give it a stated, sincere mission to make live (health, growth, optimization) that requires a justified class of exceptions | Write a system that just wants to kill or dominate — that is sovereignty, not biopower, and skips the actual argument |
| Staging the theme | Let a concrete mechanism (a screening, a quota, a classification) carry the argument, and let events test it | Have a character announce the theme ("this is about power over life") as dialogue |
| Writing the "villain" of a biopower plot | Show them believing they are curating health, purity, or fitness for the whole, not indulging cruelty | Write generic malice; the mechanism only works dramatically if the killing reads as care to the killer |
| Designing who gets protected vs. exposed | Root the cut in a measurable norm (a score, a status, a diagnosis) applied uniformly, then reveal its violence | Make the cut arbitrary or purely personal — it needs to look procedural to do the thematic work |
| Writing an opposition faction | Ask whether it has actually rejected the administrative logic of "manage life" or only wants to run the machine itself | Assume any resistance to the regime is automatically outside its logic |
| Placing a sovereign-style character inside a biopower world | Let their old life-and-death authority go unrecognized or become invisible to the new system, rather than dramatically defeated | Resolve them with a classic duel or execution that restores sovereignty as the story's real logic |
| Deciding how much lecture-history to import | Use only the mechanism (biopower + racism's two functions) as a portable engine | Import the whole race-war-to-class-struggle history as setting lore; it is scaffolding for Foucault's argument, not required furniture for a new one |

---

## 6 · INVARIANTS

1. **The new right does not replace the old one; it penetrates it.** Sovereignty's "take life or let live" keeps operating beneath and inside biopower's "make live and let die" — a biopower story still has room for an old-style sovereign killer.
2. **Biopower's object is the population, not the individual.** Its tools are forecasts, statistics, and equilibrium, not verdicts on one person.
3. **The norm is the one term that works on both scales at once.** Any single measurement standard can discipline a body and regularize a population simultaneously.
4. **A life-administering power cannot kill without a justification that does not look like conquest.** Racism (in Foucault's technical sense: a caesura plus a life-for-death exchange) is the mechanism that supplies that justification.
5. **The caesura works through two linked functions, not one.** First, fragment the population into subspecies; second, convert the death of one subspecies into the vitality of another. Both functions must be present for the mechanism to run.
6. **Once power's business is to make live, death exits the field of power and becomes private.** A political system centered on managing life has no ritual vocabulary left for death as event.
7. **Opposing a biopower regime's goals is not the same as rejecting its mechanism.** A faction can fight the regime's chosen victims while leaving its administrative logic of managing-life-by-exclusion completely intact.

---

## 7 · PITFALLS / MYTHS

- Treating biopower as simply "more surveillance" or "more control" — its distinguishing feature is the *aim* (make live) and the *scale* (population), not the intensity of oversight.
- Writing a biopower antagonist as a cartoon tyrant who enjoys killing — the mechanism only argues something if the killing is sincerely framed, by the killer, as health or care.
- Confusing state racism with interpersonal racial hatred; Foucault is explicit that this is "something much deeper than an old tradition, much deeper than a new ideology" — a technique of power, not a psychology.
- Assuming resistance movements are automatically exempt from the mechanism; the course's most uncomfortable claim is that socialism reproduced state racism whenever it had to physically fight rather than argue economics.
- Reaching for Nazism as the only usable instance — it is named as the *paroxysm*, the extreme case, not the baseline; a story's biopower system should be legible well before it reaches that limit.
- Forgetting the first half of the course: "power is war continued by other means" is the premise that makes the second half's "make live and let die" land as a *continuation* of struggle, not a benevolent correction of it.

---

## 8 · APPLICATION

- **Spine level:** L6 (the controlling idea / argument's value layer)
- **12-layer character stack:** none directly by layer number; the mechanism (state racism's must-live/may-die cut) is the plot-and-cast-level device that makes an L6 controlling idea visible in action — any character sorted by the cut, or doing the sorting, is running this concept
- **plot_systems:** primary candidate once a plot-systems layer opens — the two-function racism mechanism (fragment the population; convert the other's death into the group's vitality) is a ready-made engine for a subplot's stakes, not just background theme
- **Setting:** contextual — a biopower-run society needs visible administrative apparatus (screenings, registries, health/purity metrics) as environment, but this entry's primary use is thematic, not world-building

This is the founding text behind BOLO 80's leading controlling idea. Used correctly, biopower is not "an evil empire" theme, it is a *structure*: a system that sincerely wants to make its population live, and therefore needs a justified exception to kill anyone at all. The story's argument gets tested, not stated, when the plot forces a character who believes in the system's care to confront the cut it depends on — the moment the "make live" and the "let die" halves of the same policy meet in one scene is where the theme becomes load-bearing rather than atmospheric. The norm (a score, a screening, a status designation) is the most portable single device from the lecture: wherever the story needs the argument to become visible and concrete, put a measurement in the scene.

---

## 9 · CROSS-REFERENCES

| Related entry | Relation |
|---|---|
| Agamben, *Homo Sacer* (not yet in the library) | Direct descendant: takes sovereignty's "let live/take life" and biopower's population-management and fuses them into "bare life," the figure stripped of political status who can be killed without it counting as murder — a sharper, more usable single-character version of Foucault's must-live/may-die cut |
| Mbembe, "Necropolitics" (not yet in the library) | Direct extension: argues Foucault's "let die" undersells colonial and contemporary regimes that actively "make die" — useful correction if the story's biopower system needs an explicitly lethal edge rather than a passive-exposure one |
| Byung-Chul Han, *Psychopolitics* (not yet in the library) | Contemporary update: relocates the norm from disciplinary institutions to self-optimization and data, "make live" reframed as engineered self-exploitation rather than State administration — a model for a softer, voluntary-seeming biopower system |
| Zuboff, *The Age of Surveillance Capitalism* (not yet in the library) | Institutional update: the population-level forecasting and behavioral shaping Foucault locates in State demography relocated to corporate data extraction — a non-State biopower actor, useful if the story's system is a company or platform rather than a government |
| Arendt (not yet in the library) | Adjacent, not identical: Arendt's account of totalitarianism and the banality of administrative killing runs parallel to Foucault's Nazism case but from a different method (political theory of evil, not genealogy of power-technique) |
| Bauman (not yet in the library) | Adjacent: "modernity and the Holocaust" reads bureaucratic rationality itself as the enabling condition for mass killing, a close cousin to Foucault's claim that the norm, not hatred, is racism's real mechanism |
| Goffman (not yet in the library) | Distant cousin, useful at scene level: *Stigma*'s management of a "spoiled identity" is a micro-scale, interpersonal version of the same must-live/may-die sorting Foucault locates at the level of the State |
| [[BVX.0054]] | Lyons, *Anatomy of a Premise Line* — the L6 moral-blind-spot mechanism this entry keys to `moral_blind_spot`; a biopower character's blind spot is precisely the belief that the cut is care rather than killing |
| [[BVX.0100]] | Pavel, *Fictional Worlds* — the `argue_mode` feed (a fictional place "makes the argument in matter") is the setting-side tool for staging the norm's visible apparatus (screenings, registries) that this entry's Application section calls for |

---

## 10 · PROVENANCE & CONFIDENCE

Full text (pdftotext extraction from the 2003 Picador English edition, ~306pp). Read in full, per the brief: the lecture of 17 March 1976 ("From the power of sovereignty to power over life," the biopolitics/state-racism lecture) including its editorial footnotes, and the "Course Summary" appended after it; the lecture of 7 January 1976 (the method lecture) in full, including footnotes. The intervening nine lectures (14 January through 10 March) were read only via the table of contents and their one-line chapter descriptions to establish the course's overall arc (Framework section above); their content on the race-war discourse, its English and French variants, and its absorption into nation and class-struggle narratives is therefore reported at TOC-description depth, not full-text depth, and any finer claims about those middle lectures should be checked against the source directly.

The `feeds:` keying to L6 is this distill's synthesis for BOLO 80: Foucault's own text has no character-system vocabulary, so the mapping (controlling idea, theme-as-structure, the racism mechanism, the norm, death-privatized) is this entry's translation of the lecture's argument into the Command's story-spine terms, not a claim Foucault makes himself.

## META
- Template: BVX-LEARN-v4.0
- Source classification: full-text, deep extraction on 2 of 11 lectures (7 January, 17 March) plus the Course Summary; TOC/description-depth on the remaining 9
- Created / Updated: 2026-09-29
