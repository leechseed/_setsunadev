---
title: "Dramatica-Astrology Interface (DAI): reference"
type: reference
for: A narrative designer looking up a derivation rule, mapping table or dignity rule
does: Lists every component and part of the DAI with its inputs, tables and rules
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_character_astrology_dai.md
source_version: 1.1.0
---

**Who it's for:** a narrative designer looking up a rule or table · **What it does:** lists every component of the DAI · **Type:** reference

# Dramatica-Astrology Interface (DAI): reference

Source: [🔮ssot_02_character_astrology_dai.md](../../../_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_character_astrology_dai.md). Concept: [1-concept.md](1-concept.md).

## How to Use This Document

Five steps. Do not skip steps. Do not reorder the sequence.

1. Open the character's locked Dramatica Ingest Template (blank form: [ssot_02_template_dramatica_ingest.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_template_dramatica_ingest.md)).
2. Follow the Derivation Sequence step by step.
3. For each planet, read the Planetary Derivation Rule and consult the Element-to-Sign Mapping Tables.
4. After all planets: derive Angles, then Aspects, then Houses, then Dignities.
5. Transfer all assignments to the Character Astrology Ingest Template (blank form: [ssot_02_template_astrology_ingest.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_template_astrology_ingest.md)).

## The Derivation Sequence

| Step | Assignment | Dramatica source | Priority |
|---|---|---|---|
| 1 | Sun Sign | MC Domain + MC Concern | Required |
| 2 | Moon Sign | MC Problem + MC Response | Required |
| 3 | Ascendant | Approach + MC Critical Flaw | Required |
| 4 | Mercury | Unique Ability + Methodology Quad | Required |
| 5 | Venus | MC Concern + Purpose Quad | Required |
| 6 | Mars | Approach + Motivation Quad | Required |
| 7 | Saturn | MC Critical Flaw + Inhibitor | Required |
| 8 | Jupiter | MC Unique Ability | Recommended |
| 9 | Uranus | MC Solution | Recommended |
| 10 | Neptune | MC Symptom | Recommended |
| 11 | Pluto | Story Outcome + Story Judgment | Recommended |
| 12 | Midheaven | Story Goal + OS Role | Recommended |
| 13 | Descendant | MC Direction | Recommended |
| 14 | IC | MC Benchmark | Recommended |
| 15 | Aspects | Tension analysis across placements | Required |
| 16 | Houses | MC Domain + environmental context | Required |
| 17 | Dignities | Sign-planet efficiency analysis | Required |
| 18 | 12th House | Submerged Dramatica functions | Recommended |

- Steps 1-7 and 15-17 are the minimum viable chart. Steps 8-14 and 18 complete the full chart.
- The Vertical Slice can proceed on the minimum viable chart.

## Element-to-Sign Mapping Tables

These are reference tables, not rigid one-to-one assignments. The designer picks the sign that best encodes the character's whole Dramatica configuration.

### Dramatica Domains to Elemental Mode

| Dramatica domain | Element | Reasoning |
|---|---|---|
| Situation (Universe) | Earth | External, fixed, material conditions. The problem is the state of things. |
| Activity (Physics) | Fire | Kinetic, process-driven. The problem is in what is being done. |
| Fixed Attitude (Mind) | Air | Internal, conceptual, ideological. The problem is a way of thinking. |
| Psychology (Psychology) | Water | Processual, internal, transformative. The problem is in how the mind works. |

### Dramatica Concerns to Modality

| Concern type | Modality | Reasoning |
|---|---|---|
| About current state (The Past, The Present, How Things Are Changing) | Fixed | The concern is what IS. Resistance to change. |
| About process (Understanding, Doing, Obtaining, Learning) | Cardinal | The concern is initiating or pursuing. |
| About evaluation (Conceptualizing, Becoming, Conceiving) | Mutable | The concern is adapting, interpreting or transforming. |

### Domain + Modality = Sign Selection Grid

| | Cardinal | Fixed | Mutable |
|---|---|---|---|
| Fire (Activity) | Aries | Leo | Sagittarius |
| Earth (Situation) | Capricorn | Taurus | Virgo |
| Air (Fixed Attitude) | Libra | Aquarius | Gemini |
| Water (Psychology) | Cancer | Scorpio | Pisces |

The grid produces the Sun sign (Step 1). MC Domain sets the element. MC Concern sets the modality.

### Dramatica Problem Elements to Planetary Resonance

These affinities inform sign selection for the Moon and other planets. They are guidelines.

| Element category | Planetary affinity | Signs of strength |
|---|---|---|
| Equity / Inequity | Venus / Libra axis | Libra, Taurus, Pisces, Virgo |
| Faith / Disbelief | Neptune / Jupiter axis | Pisces, Sagittarius, Cancer |
| Pursuit / Avoid | Mars axis | Aries, Scorpio, Capricorn |
| Control / Uncontrolled | Saturn / Pluto axis | Capricorn, Scorpio, Aquarius |
| Feeling / Logic | Moon / Mercury axis | Cancer, Virgo, Gemini, Pisces |
| Proaction / Reaction | Mars / Moon axis | Aries, Cancer, Capricorn |
| Certainty / Potentiality | Saturn / Uranus axis | Capricorn, Aquarius, Scorpio |
| Desire / Ability | Venus / Mars axis | Taurus, Scorpio, Aries, Libra |
| Cause / Effect | Saturn / Jupiter axis | Capricorn, Sagittarius, Virgo |
| Temptation / Conscience | Venus / Saturn axis | Taurus, Libra, Capricorn |
| Help / Hinder | Jupiter / Saturn axis | Sagittarius, Capricorn |
| Knowledge / Thought | Mercury / Uranus axis | Gemini, Virgo, Aquarius |
| Order / Chaos | Saturn / Uranus axis | Capricorn, Aquarius, Virgo |
| Actuality / Perception | Sun / Neptune axis | Leo, Pisces, Virgo |
| Proven / Unproven | Saturn / Mercury axis | Virgo, Capricorn, Gemini |
| Test / Trust | Saturn / Moon axis | Capricorn, Cancer, Scorpio |
| Result / Process | Saturn / Mars axis | Capricorn, Aries, Virgo |
| Acceptance / Non-Acceptance | Moon / Saturn axis | Cancer, Capricorn, Taurus |

## Planetary Derivation Rules

### Step 1: Sun Sign (IDENTITYAXIS)

Machine label `IDENTITY_AXIS`. Dramatica source: MC Domain + MC Concern. The Sun is what the character believes they are.

1. Identify the MC Domain. Map it to an element with the Domain-to-Element table.
2. Identify the MC Concern. Map it to a modality with the Concern-to-Modality table.
3. Cross the element and modality on the Sign Selection Grid.
4. The result is the Sun sign.

Validation: does the sign encode the self-concept the Domain and Concern define? If it feels wrong, re-examine the modality. That mapping has the most interpretive flexibility.

### Step 2: Moon Sign (INTERNALSTATE)

Machine label `INTERNAL_STATE`. Source: MC Problem + MC Response. The Moon is where the character collapses under stress.

1. Identify the MC Problem element. Consult the Problem Elements table for sign affinities.
2. Identify the MC Response element. Check for compatible or conflicting sign associations.
3. Select a Moon sign that encodes the stress-collapse pattern.
4. Place the Moon in a different element than the Sun. Break this rule only when the stress response mirrors identity. That case is rare and produces self-reinforcing loops.

Validation: under maximum stress, does the character retreat into this sign's behavior? A Moon that feels too comfortable or too rational is wrong.

### Step 3: Ascendant (CHARACTERUISKIN)

Machine label `CHARACTER_UI_SKIN`. Source: Approach (Do-er/Be-er) + MC Critical Flaw. The Ascendant is the mask.

1. Approach = Do-er: choose from Cardinal or Fire signs.
2. Approach = Be-er: choose from Fixed or Water signs.
3. Within that subset, choose the sign whose shadow quality aligns with the MC Critical Flaw. The mask must contain the seed of the vulnerability.

Validation: does the sign describe the first impression? Does the Critical Flaw hide inside it?

### Step 4: Mercury (CODEINTERPRETATION)

Machine label `CODE_INTERPRETATION`. Source: Unique Ability + Methodology Quad.

1. Identify the Unique Ability: Mercury's superpower.
2. Identify the Methodology elements (primary and secondary): the processing style.
3. Select a Mercury sign that encodes both.

Note: the astronomical limit (Mercury within one sign of the Sun) is relaxed. Same or adjacent sign couples thinking and identity tightly. A distant sign makes intelligence independent of self-concept. Both are valid.

### Step 5: Venus (VALUEVECTOR)

Machine label `VALUE_VECTOR`. Source: MC Concern + Purpose Quad.

1. Identify the MC Concern: Venus's domain.
2. Identify the Purpose elements (primary and secondary): the quality of desire (knowledge, experience, control or meaning).
3. Select a Venus sign for the intersection.

### Step 6: Mars (ACTIONPROTOCOL)

Machine label `ACTION_PROTOCOL`. Source: Approach + Motivation Quad.

1. Do-er: bias toward Mars in Fire or Cardinal signs.
2. Be-er: bias toward Mars in Water or Fixed signs.
3. Choose the sign from the Motivation elements. Pursuit leans Aries/Scorpio. Consider leans Virgo/Libra. Faith leans Sagittarius/Pisces.

### Step 7: Saturn (ENTROPYLIMITER)

Machine label `ENTROPY_LIMITER`. Source: MC Critical Flaw + Inhibitor. Saturn is the wall.

1. The MC Critical Flaw is what the wall is made of.
2. The Inhibitor is how the wall shows up in story events.
3. Select a sign consistent with both. Cardinal blocks initiation. Fixed enforces endurance or rigidity. Mutable prevents adaptation or clarity.

### Steps 8-11: Outer Planets

| Planet | Label | Source | Rule |
|---|---|---|---|
| Jupiter | `REDUNDANCY` | MC Unique Ability | Sign encodes where the character finds expansion and temporary safety. Choose by what growth the ability enables. |
| Uranus | `BREACH_PROTOCOL` | MC Solution | Sign encodes the disruption that is the answer. Change characters must adopt it. Steadfast characters must resist it while holding position. |
| Neptune | `HAUNT_SIGNAL` | MC Symptom | Sign encodes the illusion the character chases. The Symptom is what they believe the problem is. |
| Pluto | `TERMINATION_CODE` | Story Outcome + Story Judgment | Sign encodes the terminal condition. Failure + Good: Scorpio, Capricorn, Pisces. Success + Bad (hollow victory): Leo, Aries, Gemini. |

## Angle Derivation Rules

| Angle | Label | Source | Rule |
|---|---|---|---|
| Midheaven | `CHARACTER_OUTPUT_LOG` | Story Goal + the character's OS archetype role | Encodes what the character achieves or fails to achieve in the public record. A Protagonist's aligns with the Story Goal. An Antagonist's opposes it. |
| Descendant | `CHARACTER_SHADOW_INTERFACE` | MC Direction | Always opposite the Ascendant. Content is what the character moves toward in relationships. |
| IC | `CHARACTER_ROOT_ORIGIN` | MC Benchmark | Always opposite the Midheaven. Content is the hidden measurement standard, the buried origin metric. |

## Aspect Derivation Rules

Aspects come after all planets and angles are placed, from two sources.

### Source 1: Dramatica Tension Analysis

Examine the full element set (Problem, Solution, Focus, Direction, Unique Ability, Critical Flaw, Motivation, Methodology, Evaluation, Purpose). Find pairs in structural tension.

| Pair | Aspect | Meaning |
|---|---|---|
| Problem / Solution | Opposition (XOR gate) | The character cannot execute both at once. |
| Focus / Direction | Square (NOT gate) | Attention blocks the needed trajectory. |
| Unique Ability / Critical Flaw | Conjunction if the flaw is inside the ability. Square if the flaw undermines it from outside. | |
| Reinforcing elements within one quad | Trine (OR gate) | Free-flowing, low-friction talent. |

### Source 2: Sign Geometry

- Same-element signs naturally trine.
- Same-modality, different-element signs naturally square.
- Signs opposite on the wheel naturally oppose.
- Where geometry confirms a Dramatica tension, the aspect is reinforced.
- Where geometry contradicts it, the designer chooses. Under the narrative-first policy, Dramatica tension governs.

## House Assignment Rules

The MC Domain gives the primary house emphasis.

| MC Domain | Primary house emphasis | Reasoning |
|---|---|---|
| Situation | Angular (1, 4, 7, 10) | The problem is externally visible and immediate. |
| Activity | Angular + Succedent (1, 2, 5, 7, 10, 11) | The problem shows through action and resource expenditure. |
| Fixed Attitude | Cadent + Succedent (3, 6, 8, 9, 12) | The problem lives in background processing and internal valuation. |
| Psychology | Distributed across all types | The problem touches every domain. |

Within the pattern:

- The MC Problem planet goes in an angular house (visible) or the 12th (submerged).
- Saturn goes where the limit operates. 10th: public/career. 4th: origin/family. 7th: relational.
- Mars goes in the primary field of action.
- Moon goes in the emotional center of gravity.

## Dignity Calculation Rules

After signs and houses, calculate dignity for each planet.

1. Planet in its domicile or exaltation sign: Essential Dignity.
2. Planet in its detriment or fall sign: Essential Debility.
3. Neither: Peregrine (neutral efficiency).

- Narrative-first override: the writer may override a planet in traditional dignity to Peregrine or Debility. Use it if the Dramatica data shows the character struggles with that function. Document the reason.
- A planet in traditional debility stands as debility if the character excels at the function at internal cost.
- Dignity-to-layer feed: dignity feeds L1-L3 positive capacity justifications. Debility feeds L5 WOUND, L10 SHADOW and behavioral texture notes.
- Connects to: [12-layer mapping](../ssot_02_character_astrology_12_layer_mapping/2-reference.md).

## Void Variable (12th House) Assignment

The 12th House receives planets whose Dramatica functions are submerged, operating below awareness.

- Primary candidate: the planet tied to the MC Problem element, if the character is a Change character.
- Secondary candidates: any planet whose function the character denies, represses or projects. Cross-reference L10 SHADOW content in the authoritative documentation.
- Rule: a 12th House planet is active but inaccessible to Mercury (conscious processing).
- When Mercury aspects a 12th House planet, the Hauntology Effect fires. The character gets recursive awareness, deja vu, or the sense of a pattern the character cannot name.

## Tier 2 Abbreviated Derivation

Tier 2 characters get a partial chart from their element signature (see the [Dramatica integration protocol](../ssot_02_dramatica_integration_protocol/2-reference.md)).

1. Sun Sign: from the primary element-signature element, via the Problem Elements to Planetary Resonance table.
2. Moon Sign: from a secondary element, encoding the stress response.
3. One defining aspect: a Square or Opposition between Sun and Moon if the elements are in tension. A Conjunction or Trine if they reinforce.

- No houses, dignities, angles or outer planets.
- Checked 2026-10-04: the mapping doc now has a Tier 2 section. The Sun feeds L1. The Moon feeds L8.

## Worked Example: Victoria Midnight

The Victoria Midnight chart moved out of this doc on 2026-10-04 (BOLO 100 C13). It is an instance, not method. It lives at [victoria-midnight-chart.md](../../../../_CANON_NODES/victoria-midnight-chart.md).

> **OPEN:** the moved chart is partial. The MC Concern is missing, flagged `⏸ VM fill pass (phase 2)`.
