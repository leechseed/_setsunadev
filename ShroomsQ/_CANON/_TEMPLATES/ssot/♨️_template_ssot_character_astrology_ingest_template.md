---

## type: ingest_template category: character_astrology version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Canonical intake form for Character Astrology chart data per Tier 3 character. Populated by running the locked Dramatica Ingest Template through the DAI derivation sequence. Completion of this template is required before a Vertical Slice can proceed past Step 1 Source Verification." dependencies: ["ssot_02_character_astrology", "ssot_02_character_astrology_dai", "template_dramatica_ingest"]
---
# ♨️ Character Astrology Ingest Template

> **Usage:** Copy this template into the character's canonical folder. Populate all fields by running the character's locked Dramatica Ingest Template through the DAI derivation sequence (ssot_02_character_astrology_dai). Fields marked [DERIVED] are produced by the DAI rules. Fields marked [AUTHORED] require narrative designer judgment within the DAI framework. Fields marked [COMPUTED] are calculated from prior assignments in this template.
> 
> **Lock Condition:** This document is locked when all Required fields are populated, all derivation justifications are written, and the narrative designer has validated the chart against the character's authoritative documentation. Once locked, changes require a new version number and a documented reason.
> 
> **Minimum Viable Chart:** Sections 1-5 and 8-10 constitute the minimum viable chart sufficient for the Vertical Slice to proceed. Sections 6 and 7 complete the full chart.

---

## Header

|Field|Value|
|---|---|
|character_id|[CHARACTER_ID]|
|character_name|[FULL_NAME]|
|ip|[IP_NAME]|
|dramatica_ingest_ref|[path to locked Dramatica Ingest Template]|
|storyform_id|[STORYFORM_ID]|
|chart_completeness|minimum_viable / full|
|template_version|1.0.0|
|template_status|locked / draft|
|completed_by|[NAME_OR_HANDLE]|
|completion_date|[YYYY-MM-DD]|

---

## Section 1: Personal Stack (Inner Planets) — REQUIRED

Each planet entry includes the sign assignment, the Dramatica source that produced it, and a derivation justification explaining why this sign encodes this narrative truth.

### Sun (IDENTITY_AXIS)

|Field|Value|
|---|---|
|sun_sign|[DERIVED]|
|dramatica_source|MC Domain: [value] + MC Concern: [value]|
|element|[Fire / Earth / Air / Water]|
|modality|[Cardinal / Fixed / Mutable]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining why this sign encodes this character's identity axis. What does the character believe they are? How does this sign represent that belief?]_

---

### Moon (INTERNAL_STATE)

|Field|Value|
|---|---|
|moon_sign|[DERIVED]|
|dramatica_source|MC Problem: [value] + MC Response: [value]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining the stress-collapse pattern. Where does the character go when their Sun-level processing fails? Why does this sign encode that instinctual default?]_

---

### Mercury (CODE_INTERPRETATION)

|Field|Value|
|---|---|
|mercury_sign|[DERIVED]|
|dramatica_source|Unique Ability: [value] + Methodology: [primary, secondary]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining the information processing style. How does the character think, communicate, and navigate? What cognitive superpower does the Unique Ability produce through this sign?]_

---

### Venus (VALUE_VECTOR)

|Field|Value|
|---|---|
|venus_sign|[DERIVED]|
|dramatica_source|MC Concern: [value] + Purpose: [primary, secondary]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining what the character values and desires. What do they pursue? What quality of desire does this sign encode?]_

---

### Mars (ACTION_PROTOCOL)

|Field|Value|
|---|---|
|mars_sign|[DERIVED]|
|dramatica_source|Approach: [Do-er/Be-er] + Motivation: [primary, secondary]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining how the character acts. What is their kinetic style? What drives them to move?]_

---

## Section 2: Structural Stack (Outer Planets) — REQUIRED (Saturn), RECOMMENDED (Others)

### Saturn (ENTROPY_LIMITER) — REQUIRED

|Field|Value|
|---|---|
|saturn_sign|[DERIVED]|
|dramatica_source|MC Critical Flaw: [value] + Inhibitor: [value]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences explaining the wall. What is the hard-coded limit? How does this sign encode the way that limit manifests?]_

---

### Jupiter (REDUNDANCY) — RECOMMENDED

|Field|Value|
|---|---|
|jupiter_sign|[DERIVED]|
|dramatica_source|MC Unique Ability: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. Where does the character find expansion and temporary safety?]_

---

### Uranus (BREACH_PROTOCOL) — RECOMMENDED

|Field|Value|
|---|---|
|uranus_sign|[DERIVED]|
|dramatica_source|MC Solution: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What disruption is actually the answer? How is it initially experienced as threat?]_

---

### Neptune (HAUNT_SIGNAL) — RECOMMENDED

|Field|Value|
|---|---|
|neptune_sign|[DERIVED]|
|dramatica_source|MC Symptom: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What false signal does the character chase? What illusion do they mistake for the real problem?]_

---

### Pluto (TERMINATION_CODE) — RECOMMENDED

|Field|Value|
|---|---|
|pluto_sign|[DERIVED]|
|dramatica_source|Story Outcome: [value] + Story Judgment: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What is the terminal condition? How does the argument end and what does that ending mean?]_

---

## Section 3: Interface Layer (Angles) — REQUIRED (Ascendant), RECOMMENDED (Others)

### Ascendant (CHARACTER_UI_SKIN) — REQUIRED

|Field|Value|
|---|---|
|ascendant_sign|[DERIVED]|
|dramatica_source|Approach: [Do-er/Be-er] + MC Critical Flaw: [value]|

**Derivation justification** [AUTHORED]:

> _[2-4 sentences. What is the mask? What impression does the character make on first contact? Where is the exploit vector hidden in that impression?]_

---

### Midheaven (CHARACTER_OUTPUT_LOG) — RECOMMENDED

|Field|Value|
|---|---|
|midheaven_sign|[DERIVED]|
|dramatica_source|Story Goal: [value] + OS Archetype Role: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What does the character achieve or fail to achieve in the public record?]_

---

### Descendant (CHARACTER_SHADOW_INTERFACE) — RECOMMENDED

|Field|Value|
|---|---|
|descendant_sign|[COMPUTED — opposite of Ascendant]|
|dramatica_source|MC Direction: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What does the character seek in others?]_

---

### IC (CHARACTER_ROOT_ORIGIN) — RECOMMENDED

|Field|Value|
|---|---|
|ic_sign|[COMPUTED — opposite of Midheaven]|
|dramatica_source|MC Benchmark: [value]|

**Derivation justification** [AUTHORED]:

> _[1-3 sentences. What is the buried origin metric? The hidden standard against which the character measures all progress?]_

---

## Section 4: Aspect Map (Logic Gates) — REQUIRED

List all significant aspects between planets. Each aspect must cite the Dramatica tension relationship that produces it.

|Planet A|Aspect|Planet B|Gate Type|Dramatica Source|Narrative Function|
|---|---|---|---|---|---|
|[PLANET]|[Conjunction / Square / Opposition / Trine / Sextile]|[PLANET]|[AND / NOT / XOR / OR]|[which Dramatica tension produces this]|[AUTHORED — 1 sentence]|
|||||||
|||||||

_(Add rows as needed. Minimum 3 aspects for a viable chart. Target 5-7 for a complete chart.)_

**Aspect derivation notes** [AUTHORED]:

> _[Optional. 2-4 sentences on the overall aspect pattern — is this chart dominated by hard aspects or soft aspects? What does the overall pattern say about the character's internal architecture?]_

---

## Section 5: House Placements — REQUIRED

Assign each planet to a house based on the MC Domain emphasis pattern and the planet's narrative function.

|Planet|House|House Type|Placement Justification|
|---|---|---|---|
|Sun|[1-12]|[Angular / Succedent / Cadent]|[AUTHORED — 1 sentence]|
|Moon|[1-12]|[type]|[justification]|
|Mercury|[1-12]|[type]|[justification]|
|Venus|[1-12]|[type]|[justification]|
|Mars|[1-12]|[type]|[justification]|
|Saturn|[1-12]|[type]|[justification]|
|Jupiter|[1-12]|[type]|[justification]|
|Uranus|[1-12]|[type]|[justification]|
|Neptune|[1-12]|[type]|[justification]|
|Pluto|[1-12]|[type]|[justification]|

**MC Domain emphasis pattern:** [Situation / Activity / Fixed Attitude / Psychology] -> [which house types are emphasized]

---

## Section 6: Dignity Assessment — REQUIRED

Evaluate each planet's efficiency in its assigned sign.

|Planet|Sign|Dignity Status|Justification|
|---|---|---|---|
|Sun|[sign]|[Domicile / Exaltation / Peregrine / Detriment / Fall]|[1 sentence]|
|Moon|[sign]|[status]|[justification]|
|Mercury|[sign]|[status]|[justification]|
|Venus|[sign]|[status]|[justification]|
|Mars|[sign]|[status]|[justification]|
|Saturn|[sign]|[status]|[justification]|
|Jupiter|[sign]|[status]|[justification]|
|Uranus|[sign]|[status]|[justification]|
|Neptune|[sign]|[status]|[justification]|
|Pluto|[sign]|[status]|[justification]|

**Dignity pattern summary** [AUTHORED]:

> _[2-3 sentences. How many planets are dignified vs debilitated? What does the overall dignity pattern say about the character?]_

---

## Section 7: Void Variable (12th House Contents) — RECOMMENDED

|Field|Value|
|---|---|
|12th_house_planets|[list of planets placed in 12th House, if any]|
|submerged_dramatica_function|[which Dramatica element operates beneath conscious awareness]|
|hauntology_trigger|[which Mercury aspect to a 12th House planet activates the Hauntology Effect]|

**Void Variable notes** [AUTHORED]:

> _[2-4 sentences. What is stored in the garbage collection folder? What deleted memories or previous-state data does this character carry without conscious access? When does the Hauntology Effect fire in the narrative?]_

---

## Section 8: Chart Summary — REQUIRED

A prose summary of the complete chart in 6-10 sentences. This summary is the human-readable interpretation of the chart as a unified system. It should answer: who is this character according to their chart, what are their primary tensions, where do they excel, where do they glitch, and what is the overall architecture of their internal system?

**Chart Summary** [AUTHORED]:

> _[6-10 sentences.]_

---

## Section 9: 12-Layer Feed Map — REQUIRED

Identify which chart elements feed which layers in the 12-Layer Vertical Slice.

|12-Layer|Chart Element(s) Feeding It|Feed Type|
|---|---|---|
|L1 CORE|Sun sign, Mercury configuration|Identity + cognitive justification|
|L2 VITAL|Mars sign + dignity, Ascendant|Physical capacity + kinetic style|
|L3 SOCIAL|Ascendant, Venus, 7th House contents|Social interface + value projection|
|L4 WILL|Saturn sign + dignity, Sun-Saturn aspects|Boundary capacity + resistance architecture|
|L5 WOUND|Debilitated planets, hard aspects to Moon|Source and texture of damage|
|L6 DRIVE|Mars sign, Jupiter placement|Action fuel + expansion capacity|
|L7 ORIGIN|IC, 4th House contents, Moon sign|Root context + emotional foundation|
|L8 IMPRINT|Moon sign + aspects, 8th House contents|Attachment architecture + conditioning|
|L9 EROS|Venus sign + aspects, Mars-Venus relationship, 5th/8th House|Desire structure + intimacy mode|
|L10 SHADOW|12th House contents, debilitated planets, Pluto aspects|Repressed content + projection patterns|
|L11 DESTINY|Jupiter, Uranus, North Node (if assigned), Midheaven|Growth vector + resistance to solution|
|L12 FUNCTION|_(fed directly from Dramatica Ingest, not from Character Astrology)_|N/A|

**Feed map notes** [AUTHORED]:

> _[Optional. 2-3 sentences on any feed relationships specific to this character that deviate from the standard mapping.]_

---

## Section 10: Downstream Handoff Checklist — REQUIRED

Before locking this template, confirm:

- [ ] All REQUIRED sections are populated
- [ ] All derivation justifications are written
- [ ] Dramatica Ingest Template is locked and referenced in header
- [ ] Sun, Moon, Mercury, Venus, Mars, Saturn, and Ascendant are assigned (minimum viable chart)
- [ ] At least 3 aspects are documented with Dramatica tension sources
- [ ] All planets have house assignments
- [ ] Dignity assessment is complete for all assigned planets
- [ ] Chart Summary is written
- [ ] 12-Layer Feed Map is completed
- [ ] Chart validated against character's authoritative documentation — no contradictions
- [ ] Template status changed to locked
- [ ] Template placed in character's canonical folder

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial template. 10 sections covering Personal Stack, Structural Stack, Interface Layer, Aspect Map, House Placements, Dignity Assessment, Void Variable, Chart Summary, 12-Layer Feed Map, and downstream handoff checklist.|