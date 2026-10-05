---
type: ssot_02_character_systems
category: template_astrology_ingest
module_of: ssot_02_character_systems_vertical_slice
version: 1.0.1
tier: fabula
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "v1.0.0 2026-10-04: RULED — BOLO 100 C18"
purpose: "Blank fill-in form for the Character Astrology Ingest Template. One copy per Tier 3 character. It holds the natal chart derived from the Dramatica Ingest through the DAI rules."
dependencies: ["ssot_02_character_astrology", "ssot_02_character_astrology_dai", "ssot_02_character_astrology_12_layer_mapping", "ssot_02_template_dramatica_ingest", "ssot_02_step_1_source_verification_protocol"]
rung: standard
---
# 📐 SSOT: Template — Character Astrology Ingest

## How to use this form

1. Copy this file to the character's folder as `[CHARACTER_ID]_astrology_ingest.md`, as set out in the [Step 1 protocol](🔮ssot_02_step_1_source_verification_protocol.md).
2. Delete this section and the frontmatter above. Keep the section numbers. The Step 1 checks cite them.
3. Work in the order of the [DAI doc](🔮ssot_02_character_astrology_dai.md): planets, then angles, aspects, houses, dignities, the 12th House. The chart method is in the [astrology doc](📐%20ssot_02_character_astrology.md).
4. Every sign needs a one or two sentence derivation. Write the Dramatica input, the rule you used, and why the sign fits.
5. Leave a field empty if the storyform does not give it yet. Write `⏸` and the reason. Never guess.

**Minimum viable chart** (status `minimum_viable`): Sections 1 to 5 and 8 to 10, with the Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant signs, at least three aspects, and houses for those seven planets. Sections 6 and 7 can wait.

A Tier 2 character gets a partial chart (Sun, Moon, one defining aspect) and does not use this form.

---

## Header

```yaml
character_id: ____
ip: ____
tier: 3
dramatica_ingest_ref: ____     # path to the locked Dramatica Ingest (blank form: ssot_02_template_dramatica_ingest.md)
storyform_id: ____
storyform_version: ____
template_status: draft         # draft | minimum_viable | locked
dai_doc_version: ____
locked_on: ____
```

---

## 1. Personal Planets

|Planet (function)|Dramatica source|Sign|Derivation|
|---|---|---|---|
|Sun (`IDENTITY_AXIS`)|MC Domain + MC Concern|____|____|
|Moon (`INTERNAL_STATE`)|MC Problem + MC Response|____|____|
|Mercury (`CODE_INTERPRETATION`)|Unique Ability + Methodology quad|____|____|
|Venus (`VALUE_VECTOR`)|MC Concern + Purpose quad|____|____|
|Mars (`ACTION_PROTOCOL`)|Approach + Motivation quad|____|____|

---

## 2. Structural Planets

|Planet (function)|Dramatica source|Sign|Derivation|
|---|---|---|---|
|Saturn (`ENTROPY_LIMITER`)|MC Critical Flaw + Inhibitor|____|____|
|Jupiter (`REDUNDANCY`)|MC Unique Ability|____|____|
|Uranus (`BREACH_PROTOCOL`)|MC Solution|____|____|
|Neptune (`HAUNT_SIGNAL`)|MC Symptom|____|____|
|Pluto (`TERMINATION_CODE`)|Story Outcome + Story Judgment|____|____|

---

## 3. Angles

|Angle (function)|Dramatica source|Sign|Derivation|
|---|---|---|---|
|Ascendant (`CHARACTER_UI_SKIN`)|Approach + MC Critical Flaw|____|____|
|Midheaven (`CHARACTER_OUTPUT_LOG`)|Story Goal + OS role|____|____|
|Descendant (`CHARACTER_SHADOW_INTERFACE`)|MC Direction (opposite the Ascendant)|____|____|
|IC (`CHARACTER_ROOT_ORIGIN`)|MC Benchmark (opposite the Midheaven)|____|____|

---

## 4. Aspect Map

At least three aspects for the minimum viable chart. Each cites its Dramatica tension source.

|Planet A|Planet B|Aspect|Dramatica tension source|Gate|Note|
|---|---|---|---|---|---|
|____|____|____|____|____|____|

Aspect types: Opposition (Problem / Solution) · Square (Focus / Direction) · Conjunction or Square (Unique Ability / Critical Flaw) · Trine (reinforcing elements in a quad) · Sextile (flowing elements in a quad that do not conflict). Where sign geometry disagrees with the Dramatica tension, the Dramatica tension governs.

---

## 5. House Placements

MC Domain emphasis pattern: ____

|Planet|House|Justification|
|---|---|---|
|Sun|____|____|
|Moon|____|____|
|Mercury|____|____|
|Venus|____|____|
|Mars|____|____|
|Saturn|____|____|
|Ascendant|1|(fixed)|

---

## 6. Dignities

|Planet|Sign|Dignity (Essential Dignity / Essential Debility / Peregrine)|Override? Justification|
|---|---|---|---|
|____|____|____|____|

---

## 7. 12th House / Void Contents

|Planet|Submerged Dramatica function|Link to L10 SHADOW content|
|---|---|---|
|____|____|____|

---

## 8. Chart Summary

Six to ten sentences, plain words. Say what the chart says about this character and where it pulls in two directions.

> ____

---

## 9. LEECHSEED Feed Map

Fill this in against the [mapping doc](🔮ssot_02_character_astrology_12_layer_mapping.md). The chart justifies a layer value. It never sets one. Fields added in schema 2.5.0 and 3.0.0 are not chart-fed (see the mapping doc's schema-pass table).

|Layer|Chart source|Consistent with the layer value? (yes / no / exception)|Feed notes and conflict resolution|
|---|---|---|---|
|L1 CORE|Sun, Mercury|____|____|
|L2 VITAL|Mars, Ascendant|____|____|
|L3 SOCIAL|Ascendant, Venus, 7th House|____|____|
|L4 WILL|Saturn, Sun-Saturn aspects|____|____|
|L5 WOUND|Debilitated planets, hard Moon aspects, 8th House|____|____|
|L6 DRIVE|Mars, Jupiter|____|____|
|L7 ORIGIN|IC, 4th House, Moon (partial)|____|____|
|L8 IMPRINT|Moon, Moon aspects, Moon dignity|____|____|
|L9 EROS|Venus, Mars-Venus aspect, 5th and 8th House (supplemental)|____|____|
|L10 SHADOW|12th House, debilitated planets, Pluto|____|____|
|L11 DESTINY|Jupiter, Uranus, Midheaven|____|____|
|L12 FUNCTION|None (fed from the Dramatica Ingest)|n/a|n/a|

When the authoritative document is ambiguous, log the resolution in the notes column, as the mapping doc's conflict protocol says.

---

## 10. Status and Lock

- [ ] The `dramatica_ingest_ref` points to a locked Dramatica Ingest.
- [ ] Sun, Moon, Mercury, Venus, Mars, Saturn and Ascendant are assigned, each with a derivation.
- [ ] The aspect map has at least three aspects.
- [ ] Houses are assigned for the seven planets above.
- [ ] The chart summary is written.
- [ ] The feed map is complete.
- [ ] Feed Validation Checklist (mapping doc) run and passed, or exceptions logged. Needed for `locked`; not for `minimum_viable`.

`template_status`: ____ (minimum_viable passes the Step 1 gate as a yellow light; layers fed by the chart carry `[ASTROLOGY_PENDING]` until `locked`).

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-10-04|v1.0.0 2026-10-04: RULED — BOLO 100 C18. First blank form, built from the DAI doc, the astrology doc and the Step 1 checks (3.1 to 3.8).|
|1.0.1|2026-10-05|BOLO 102 batch A (Chief: "All recs go"): added Sextile to the aspect list.|
