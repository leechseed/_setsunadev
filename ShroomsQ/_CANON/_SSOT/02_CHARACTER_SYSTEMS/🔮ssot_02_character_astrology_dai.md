---

## type: ssot_02_character_systems category: character_astrology_dai version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the complete Dramatica-Astrology Interface (DAI) — the translation rules that convert locked Dramatica storyform outputs into Character Astrology planetary assignments. This is the API specification between the two systems." dependencies: ["ssot_02_character_dramatica_integration", "ssot_02_character_astrology"]
---
# 🔮 SSOT: Dramatica-Astrology Interface (DAI) Expansion

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [How to Use This Document](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#how-to-use-this-document)
3. [The Derivation Sequence](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-derivation-sequence)
4. [Element-to-Sign Mapping Tables](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#element-to-sign-mapping-tables)
5. [Planetary Derivation Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#planetary-derivation-rules)
6. [Angle Derivation Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#angle-derivation-rules)
7. [Aspect Derivation Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#aspect-derivation-rules)
8. [House Assignment Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#house-assignment-rules)
9. [Dignity Calculation Rules](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#dignity-calculation-rules)
10. [Void Variable (12th House) Assignment](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#void-variable-assignment)
11. [Tier 2 Abbreviated Derivation](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#tier-2-abbreviated-derivation)
12. [Worked Example: Victoria Midnight](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#worked-example-victoria-midnight)
13. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This document is the API specification between Dramatica and Character Astrology. It defines the exact translation rules that convert a locked Dramatica Ingest Template into a Character Astrology natal chart. Every rule traces a specific Dramatica output to a specific astrological assignment.

The narrative designer works through this document sequentially — from Sun to Pluto, then Angles, then Aspects, then Houses, then Dignities — to produce a complete character chart. The output of this process is the data that populates the Character Astrology Ingest Template (deliverable 2C).

---

## How to Use This Document

1. Open the character's locked Dramatica Ingest Template.
2. Follow the Derivation Sequence (Section 3) step by step.
3. For each planet, read the Derivation Rule (Section 5) and consult the Element-to-Sign Mapping Table (Section 4) to select the sign.
4. After all planets are placed, derive Angles (Section 6), then Aspects (Section 7), then Houses (Section 8), then Dignities (Section 9).
5. Transfer all assignments to the Character Astrology Ingest Template.

Do not skip steps. Do not reorder the sequence. Each step depends on decisions made in prior steps.

---

## The Derivation Sequence

The fixed order of operations for generating a character chart from Dramatica data:

|Step|Assignment|Dramatica Source|Priority|
|---|---|---|---|
|1|**Sun Sign**|MC Domain + MC Concern|Required|
|2|**Moon Sign**|MC Problem + MC Response|Required|
|3|**Ascendant**|Approach + MC Critical Flaw|Required|
|4|**Mercury**|Unique Ability + Methodology Quad|Required|
|5|**Venus**|MC Concern + Purpose Quad|Required|
|6|**Mars**|Approach + Motivation Quad|Required|
|7|**Saturn**|MC Critical Flaw + Inhibitor|Required|
|8|**Jupiter**|MC Unique Ability|Recommended|
|9|**Uranus**|MC Solution|Recommended|
|10|**Neptune**|MC Symptom|Recommended|
|11|**Pluto**|Story Outcome + Story Judgment|Recommended|
|12|**Midheaven**|Story Goal + OS Role|Recommended|
|13|**Descendant**|MC Direction|Recommended|
|14|**IC**|MC Benchmark|Recommended|
|15|**Aspects**|Tension analysis across placements|Required|
|16|**Houses**|MC Domain + environmental context|Required|
|17|**Dignities**|Sign-planet efficiency analysis|Required|
|18|**12th House**|Submerged Dramatica functions|Recommended|

Steps 1-7 and 15-17 constitute the **minimum viable chart**. Steps 8-14 and 18 complete the full chart. The Vertical Slice can proceed with minimum viable chart data.

---

## Element-to-Sign Mapping Tables

These tables map Dramatica structural concepts to astrological signs. They are reference tables consulted during the derivation process, not rigid one-to-one assignments. The narrative designer selects the sign that best encodes the specific Dramatica configuration for this character, using these tables as the decision space.

### Dramatica Domains to Elemental Mode

|Dramatica Domain|Astrological Element|Reasoning|
|---|---|---|
|**Situation** (Universe)|Earth|External, fixed, material conditions. The problem is the state of things.|
|**Activity** (Physics)|Fire|Kinetic, process-driven. The problem is in what is being done.|
|**Fixed Attitude** (Mind)|Air|Internal, conceptual, ideological. The problem is a way of thinking.|
|**Psychology** (Psychology)|Water|Processual, internal, transformative. The problem is in how the mind works.|

### Dramatica Concerns to Modality

|Concern Type|Astrological Modality|Reasoning|
|---|---|---|
|Concerns about **current state** (e.g., The Past, The Present, How Things Are Changing)|Fixed|The concern is about what IS. Resistance to change.|
|Concerns about **process** (e.g., Understanding, Doing, Obtaining, Learning)|Cardinal|The concern is about initiating or pursuing. Active engagement.|
|Concerns about **evaluation** (e.g., Conceptualizing, Becoming, Conceiving)|Mutable|The concern is about adapting, interpreting, or transforming.|

### Domain + Modality = Sign Selection Grid

||Cardinal|Fixed|Mutable|
|---|---|---|---|
|**Fire** (Activity)|Aries|Leo|Sagittarius|
|**Earth** (Situation)|Capricorn|Taurus|Virgo|
|**Air** (Fixed Attitude)|Libra|Aquarius|Gemini|
|**Water** (Psychology)|Cancer|Scorpio|Pisces|

This grid produces the **Sun Sign** (Step 1). The MC Domain determines the element. The MC Concern determines the modality. The intersection identifies the sign.

### Dramatica Problem Elements to Planetary Resonance

Certain Dramatica elements have natural planetary affinities that inform sign selection for the Moon and other planets:

|Element Category|Planetary Affinity|Signs of Strength|
|---|---|---|
|**Equity / Inequity**|Venus / Libra axis|Libra, Taurus, Pisces, Virgo|
|**Faith / Disbelief**|Neptune / Jupiter axis|Pisces, Sagittarius, Cancer|
|**Pursuit / Avoid**|Mars axis|Aries, Scorpio, Capricorn|
|**Control / Uncontrolled**|Saturn / Pluto axis|Capricorn, Scorpio, Aquarius|
|**Feeling / Logic**|Moon / Mercury axis|Cancer, Virgo, Gemini, Pisces|
|**Proaction / Reaction**|Mars / Moon axis|Aries, Cancer, Capricorn|
|**Certainty / Potentiality**|Saturn / Uranus axis|Capricorn, Aquarius, Scorpio|
|**Desire / Ability**|Venus / Mars axis|Taurus, Scorpio, Aries, Libra|
|**Cause / Effect**|Saturn / Jupiter axis|Capricorn, Sagittarius, Virgo|
|**Temptation / Conscience**|Venus / Saturn axis|Taurus, Libra, Capricorn|
|**Help / Hinder**|Jupiter / Saturn axis|Sagittarius, Capricorn|
|**Knowledge / Thought**|Mercury / Uranus axis|Gemini, Virgo, Aquarius|
|**Order / Chaos**|Saturn / Uranus axis|Capricorn, Aquarius, Virgo|
|**Actuality / Perception**|Sun / Neptune axis|Leo, Pisces, Virgo|
|**Proven / Unproven**|Saturn / Mercury axis|Virgo, Capricorn, Gemini|
|**Test / Trust**|Saturn / Moon axis|Capricorn, Cancer, Scorpio|
|**Result / Process**|Saturn / Mars axis|Capricorn, Aries, Virgo|
|**Acceptance / Non-Acceptance**|Moon / Saturn axis|Cancer, Capricorn, Taurus|

These affinities are guidelines. The narrative designer selects the specific sign based on the character's full Dramatica configuration, not from any single element in isolation.

---

## Planetary Derivation Rules

### Step 1: Sun Sign (`IDENTITY_AXIS`)

**Dramatica Source:** MC Domain + MC Concern

**Derivation Logic:** The Sun represents what the character believes they are. The MC Domain defines the broadest category of the character's personal problem. The MC Concern narrows that to a specific area of focus. Together they identify the character's identity axis — the thing they orient their entire self-concept around.

**Process:**

1. Identify the MC Domain. Map it to an astrological element using the Domain-to-Element table.
2. Identify the MC Concern. Map it to a modality using the Concern-to-Modality table.
3. Cross-reference element and modality on the Sign Selection Grid.
4. The resulting sign is the Sun sign.

**Validation:** Read the sign description. Does it encode the character's self-concept as defined by the MC Domain and Concern? If the sign feels wrong, re-examine the modality assignment — Concern-to-Modality mapping has the most interpretive flexibility.

### Step 2: Moon Sign (`INTERNAL_STATE`)

**Dramatica Source:** MC Problem + MC Response

**Derivation Logic:** The Moon represents the character's instinctual default — where they collapse under stress. The MC Problem is the actual source of their difficulty (often unconscious for Change characters). The MC Response is what the character does when they feel the symptoms of their problem. Together these define the emotional basement: the pattern the character falls into when their Sun-level processing fails.

**Process:**

1. Identify the MC Problem element. Consult the Problem Elements to Planetary Resonance table for sign affinities.
2. Identify the MC Response element. Check for compatible or conflicting sign associations.
3. Select a Moon sign that encodes the stress-collapse pattern — the instinctual behavior that emerges when rational processing breaks down.
4. The Moon sign should be in a different element than the Sun sign unless the character's stress response mirrors their identity (which is rare and produces a specific behavioral texture of self-reinforcing loops).

**Validation:** Under maximum stress, does this character retreat into behavior consistent with this Moon sign? If the Moon sign feels too comfortable or too rational, it is wrong — the Moon is not where the character thinks clearly, it is where they react.

### Step 3: Ascendant (`CHARACTER_UI_SKIN`)

**Dramatica Source:** Approach (Do-er/Be-er) + MC Critical Flaw

**Derivation Logic:** The Ascendant is the mask — the first thing the world sees and the style in which the character initially engages with problems. The Approach (Do-er/Be-er) determines whether the Ascendant reads as active/kinetic or receptive/adaptive. The MC Critical Flaw determines the exploit vector embedded in the mask.

**Process:**

1. If Approach = Do-er, select from Cardinal or Fire signs (active, initiating, visible energy).
2. If Approach = Be-er, select from Fixed or Water signs (receptive, adaptive, absorptive energy).
3. Within that subset, select the sign whose shadow quality aligns with the MC Critical Flaw — the Ascendant must contain the seed of the character's vulnerability in its presentation style.

**Validation:** When someone meets this character for the first time, does the Ascendant sign describe the impression they make? Does the Critical Flaw hide inside that impression like a structural weakness in an otherwise functional interface?

### Step 4: Mercury (`CODE_INTERPRETATION`)

**Dramatica Source:** Unique Ability + Methodology Quad

**Derivation Logic:** Mercury governs how the character processes information, communicates, and navigates tactical situations. The Unique Ability defines what the character can do that no other character in the story can. The Methodology quad defines how the character approaches problem-solving operationally.

**Process:**

1. Identify the Unique Ability. This is Mercury's superpower — the specific cognitive or communicative capacity that gives the character an edge.
2. Identify the Methodology elements (primary and secondary). These define the processing style — systematic vs. intuitive, certain vs. exploratory.
3. Select a Mercury sign that encodes both the superpower and the processing style.

**Note:** Mercury can only be within one sign of the Sun in astronomical reality. In Character Astrology, this constraint is relaxed — Mercury can be placed in any sign that serves the narrative. However, placing Mercury close to the Sun sign (same sign or adjacent) produces characters whose thinking and identity are tightly coupled. Placing Mercury far from the Sun produces characters whose intelligence operates independently of their self-concept. Both are valid textures.

### Step 5: Venus (`VALUE_VECTOR`)

**Dramatica Source:** MC Concern + Purpose Quad

**Derivation Logic:** Venus governs what the character values, desires, and attempts to acquire — both materially and relationally. The MC Concern defines the area of life the character is most focused on. The Purpose quad defines what the character considers meaningful and worth pursuing.

**Process:**

1. Identify the MC Concern. This defines Venus's domain — what area of life the character's desire centers on.
2. Identify the Purpose elements (primary and secondary). These define the quality of desire — knowledge-seeking, experience-seeking, control-seeking, meaning-seeking.
3. Select a Venus sign that encodes the intersection of the domain and the quality.

### Step 6: Mars (`ACTION_PROTOCOL`)

**Dramatica Source:** Approach (Do-er/Be-er) + Motivation Quad

**Derivation Logic:** Mars governs how the character acts — the style and intensity of their kinetic engagement with the world. The Approach determines the fundamental action mode. The Motivation quad defines what drives the character to move.

**Process:**

1. If Approach = Do-er, bias toward Mars in Fire or Cardinal signs (direct, initiating, physical).
2. If Approach = Be-er, bias toward Mars in Water or Fixed signs (indirect, responsive, emotionally driven).
3. Select the specific sign based on the Motivation elements — what drives this character to act? Pursuit drives Mars toward Aries/Scorpio. Consider drives Mars toward Virgo/Libra. Faith drives Mars toward Sagittarius/Pisces.

### Step 7: Saturn (`ENTROPY_LIMITER`)

**Dramatica Source:** MC Critical Flaw + Inhibitor

**Derivation Logic:** Saturn is the wall. It represents the hard-coded limit the character cannot bypass without transformation. The MC Critical Flaw is the thing that undermines the character's Unique Ability. The Inhibitor is the story-level force that slows or blocks progress.

**Process:**

1. Identify the MC Critical Flaw. This is Saturn's content — what the wall is made of.
2. Identify the Inhibitor. This is Saturn's enforcement mechanism — how the wall manifests in story events.
3. Select a Saturn sign that encodes a limit consistent with both. Saturn in Cardinal signs produces limits that block initiation. Saturn in Fixed signs produces limits that enforce endurance or rigidity. Saturn in Mutable signs produces limits that prevent adaptation or clarity.

### Steps 8-11: Outer Planets

**Jupiter** (`REDUNDANCY`): Derived from MC Unique Ability. The sign encodes where the character finds expansion and temporary safety. Select based on the quality of the Unique Ability — what kind of growth does it enable?

**Uranus** (`BREACH_PROTOCOL`): Derived from MC Solution. The sign encodes the disruption that is actually the answer. For Change characters, this is the thing they must adopt. For Steadfast characters, this is the thing they must resist while maintaining their position.

**Neptune** (`HAUNT_SIGNAL`): Derived from MC Symptom. The sign encodes the illusion — the false signal the character chases. The MC Symptom is what the character believes is their problem (as opposed to the MC Problem, which is the actual problem).

**Pluto** (`TERMINATION_CODE`): Derived from Story Outcome + Story Judgment. The sign encodes the terminal condition. Outcome: Failure + Judgment: Good produces Pluto in a sign capable of meaningful destruction (Scorpio, Capricorn, Pisces). Outcome: Success + Judgment: Bad produces Pluto in a sign of hollow victory (Leo, Aries, Gemini).

---

## Angle Derivation Rules

**Midheaven** (`CHARACTER_OUTPUT_LOG`): Derived from the Story Goal and the character's OS archetype role. The Midheaven sign encodes what the character achieves or fails to achieve in the public record. A Protagonist's Midheaven aligns with the Story Goal. An Antagonist's Midheaven opposes it.

**Descendant** (`CHARACTER_SHADOW_INTERFACE`): Derived from MC Direction. The Descendant is always the sign opposite the Ascendant, but its content is defined by the MC Direction — the thing the character moves toward in relationships. If the Ascendant is what the character shows, the Descendant is what they seek.

**IC** (`CHARACTER_ROOT_ORIGIN`): Derived from MC Benchmark. The IC is always the sign opposite the Midheaven, but its content is defined by the MC Benchmark — the hidden measurement standard against which the character unconsciously judges all progress. This is the buried origin metric.

---

## Aspect Derivation Rules

After all planets and angles are placed, aspects are derived from two sources:

### Source 1: Dramatica Tension Analysis

Examine the character's full element set (Problem, Solution, Focus, Direction, Unique Ability, Critical Flaw, Motivation, Methodology, Evaluation, Purpose). Identify pairs of elements that are in structural tension:

- **Problem / Solution pair** → The planets carrying these elements receive an **Opposition** (XOR gate). The character cannot execute both simultaneously.
- **Focus / Direction pair** → The planets carrying these elements receive a **Square** (NOT gate). The character's attention (Focus) blocks their needed trajectory (Direction).
- **Unique Ability / Critical Flaw pair** → The planets carrying these elements receive a **Conjunction** if the flaw is embedded inside the ability (they fuse), or a **Square** if the flaw undermines the ability externally.
- **Elements within the same quad that reinforce** → Corresponding planets receive a **Trine** (OR gate). Free-flowing, low-friction talent.

### Source 2: Sign Geometry

Once signs are assigned, check the geometric relationships between planet positions:

- Signs of the same element (e.g., two planets in Fire signs) naturally trine.
- Signs of the same modality but different element (e.g., Cardinal Fire and Cardinal Earth) naturally square.
- Signs in opposing positions on the zodiac wheel naturally oppose.

Where sign geometry confirms a Dramatica tension relationship, the aspect is reinforced. Where sign geometry contradicts a Dramatica tension relationship, the narrative designer must choose which takes priority. Per the narrative-first policy, the Dramatica tension governs.

---

## House Assignment Rules

House placement determines the life domain where each planet's energy operates. The MC Domain provides the primary house emphasis pattern:

|MC Domain|Primary House Emphasis|Reasoning|
|---|---|---|
|**Situation**|Angular (1, 4, 7, 10)|The problem is externally visible and immediate.|
|**Activity**|Angular + Succedent (1, 2, 5, 7, 10, 11)|The problem manifests through action and resource expenditure.|
|**Fixed Attitude**|Cadent + Succedent (3, 6, 8, 9, 12)|The problem lives in background processing and internal valuation.|
|**Psychology**|Distributed across all types|The problem is in how the mind works, which touches every domain.|

Within the emphasis pattern, specific house assignments follow the planet's narrative function:

- The **MC Problem planet** goes in an angular house (high visibility, immediate impact) or the 12th house (submerged, unconscious).
- **Saturn** goes in the house that corresponds to the life domain where the character's limit operates. Saturn in the 10th = limit is public/career. Saturn in the 4th = limit is origin/family. Saturn in the 7th = limit is relational.
- **Mars** goes in the house that corresponds to the character's primary field of action.
- **Moon** goes in the house that corresponds to the character's emotional center of gravity.

---

## Dignity Calculation Rules

After sign and house assignments are complete, calculate dignity for each planet:

1. Check each planet's sign against its traditional domicile and exaltation. If the planet is in its domicile or exaltation sign, assign **Essential Dignity**.
2. Check each planet's sign against its traditional detriment and fall. If the planet is in its detriment or fall sign, assign **Essential Debility**.
3. For planets in neither dignity nor debility, assign **Peregrine** (neutral efficiency).

**Narrative-first dignity override:** If a planet is in traditional dignity but the Dramatica data indicates the character struggles with that function, the narrative designer may override to Peregrine or Debility with a documented justification. If a planet is in traditional debility but the Dramatica data indicates the character excels at that function (albeit with emotional cost), the debility stands — debility does not mean inability, it means the function operates at internal cost. This is a feature, not a bug.

**Dignity-to-Layer feed:** Planets in dignity feed L1-L3 positive capacity justifications. Planets in debility feed L5 WOUND, L10 SHADOW, and specific behavioral texture notes. This mapping is formalized in deliverable 3A.

---

## Void Variable (12th House) Assignment

The 12th House receives planets whose Dramatica functions are **submerged** — operating beneath the character's conscious awareness.

**Primary candidate:** The planet associated with the MC Problem element, if the character is a Change character (Change characters typically do not recognize their Problem until late in the arc, meaning the Problem function operates unconsciously).

**Secondary candidates:** Any planet whose Dramatica function the character actively denies, represses, or projects. Cross-reference with L10 SHADOW content from the character's authoritative documentation.

**Rule:** A planet in the 12th House is not inert. It is active but inaccessible to the character's conscious processing (Mercury). When Mercury aspects a 12th House planet, the Hauntology Effect fires — the character experiences recursive awareness, deja vu, or the sensation of being in a pattern they cannot name.

---

## Tier 2 Abbreviated Derivation

Tier 2 characters receive a partial chart derived from their element signature (defined in the Dramatica Integration Protocol).

**Tier 2 derivation steps:**

1. **Sun Sign:** Derived from the character's primary element signature element using the Problem Elements to Planetary Resonance table. Select the sign that best encodes their dominant behavioral driver.
2. **Moon Sign:** Derived from a secondary element signature element. Select the sign that encodes their stress response.
3. **One defining aspect:** Identify the primary tension within their element signature. Assign a Square or Opposition between the Sun and Moon if the elements are in tension, or a Conjunction/Trine if they reinforce.

No house assignments, no dignity calculations, no angles, no outer planets. The Tier 2 chart is a behavioral sketch, not a full rendering.

---

## Worked Example: Victoria Midnight

**Source:** Dramatica Ingest (from authoritative document)

|Dramatica Variable|Value|
|---|---|
|MC Domain|Situation|
|MC Concern|_(to be extracted from storyform)_|
|MC Issue|Interdiction|
|MC Problem|Equity|
|MC Solution|Inequity|
|MC Focus|Desire|
|MC Direction|Ability|
|MC Unique Ability|Destiny|
|MC Critical Flaw|Truth|
|Approach|Do-er|
|Resolve|Change|
|Motivation|Consider, Pursuit|
|Methodology|Certainty, Proaction|
|Evaluation|Proven, Effect|
|Purpose|Knowledge, Actuality|
|Story Outcome|Failure|
|Story Judgment|Good|
|Limit|Optionlock|

### Step 1: Sun Sign

MC Domain = Situation → Element = Earth. MC Concern = _(pending full extraction)_. MC Issue = Interdiction, which deals with prohibition, being blocked, external constraint on action. This suggests a Fixed concern area (the problem is about what IS, resistance to change imposed from outside). Earth + Fixed = **Taurus**.

**Validation:** Taurus encodes a character whose identity axis is material, embodied, earned through labor, resistant to being moved by external force. Victoria believes she is what she has built with her own hands. Merit earns freedom. "Beauty that is earned, not curated; motion under pressure, never ornamental." Taurus confirmed.

### Step 2: Moon Sign

MC Problem = Equity → Venus/Libra axis affinity. MC Response = _(to be extracted)_. Stress collapse pattern: when her Sun-level processing fails, she defaults to Equity logic — fairness calculus, merit evaluation, weighing what is deserved versus what is given. Under maximum stress she does not rage or withdraw, she **recalculates**.

Moon in **Libra** encodes the instinctual retreat into fairness logic. When everything breaks, she weighs. When weighing fails, she freezes — the Libra Moon's paralysis state is the decision loop that fires when no option satisfies the equity requirement.

**Validation:** The crash. She overrode the pace-notes because she calculated she knew better. The Moon in Libra is the mechanism — under stress, she does not listen, she evaluates. The evaluation kills her brother.

### Step 3: Ascendant

Approach = Do-er → Cardinal or Fire signs. MC Critical Flaw = Truth → The exploit vector embedded in the mask is radical transparency. She cannot manage her signal.

Ascendant in **Aries** encodes a visible, kinetic, confrontational interface. She enters rooms like a force. The Aries mask contains Truth as its exploit: Aries does not hedge, does not perform, does not code-switch. What you see is what is actually there. In a system that rewards managed legibility, an Aries Ascendant with Truth as its flaw is maximally vulnerable.

**Validation:** Truth Exposure Index = 18. The Ascendant explains why.

### Step 4: Mercury

Unique Ability = Destiny. Methodology = Certainty, Proaction. Mercury governs how she processes information. Her unique ability is that she can see where things are going — not prediction, but pattern recognition so acute it reads as inevitability. She processes through certainty (she commits to her reading) and proaction (she moves on it before others have finished deliberating).

Mercury in **Capricorn** encodes methodical, structural, building-oriented cognition that commits to conclusions and acts on them with authority. Capricorn Mercury does not speculate — it determines.

### Step 5: Venus

MC Concern = _(pending)_, mapped through Interdiction. Purpose = Knowledge, Actuality. She values knowing what is real. She pursues actuality — the thing beneath appearances. Her desire structure is kinesthetic, earned, physical (from L9 EROS: erotic_blueprint_type = kinesthetic, intimacy_mode = parallel_presence).

Venus in **Virgo** encodes desire oriented toward precision, earned competence, and the tangible. Virgo Venus does not want to be adored — it wants to be useful, accurate, and present in the body.

### Step 6: Mars

Approach = Do-er. Motivation = Consider, Pursuit. She acts through pursuit once she has considered. She does not wait. She does not ask permission. She converts fear into action.

Mars in **Capricorn** (Exaltation) encodes disciplined, strategic, relentless kinetic energy. Mars in Capricorn does not fight emotionally — it fights structurally. This is a racing driver's Mars: precision under pressure, physical courage channeled through technique.

**Dignity note:** Mars in Capricorn = Essential Dignity (Exaltation). This is consistent — her physical execution is her highest-functioning system. VITAL = 14 in the 12-Layer system.

### Step 7: Saturn

MC Critical Flaw = Truth. Inhibitor = _(to be extracted)_. The wall is Truth itself. When she speaks truth, she desyncs her hardware and triggers systemic response. The system cannot categorize a signal it can read completely and that refuses to self-regulate.

Saturn in **Gemini** (Detriment) encodes a limit located in communication and signal management. Saturn in Gemini means the character's words are the cage — not because she speaks poorly, but because the system punishes transparent speech. Saturn in detriment means the limit is structurally inefficient: it should not function as a limit, but it does, and the character cannot fix it because fixing it would require becoming less truthful.

**Dignity note:** Saturn in Gemini = Essential Debility (Detriment). The limit is a glitch — it works against the natural function of the sign. Gemini wants to communicate freely. Saturn in Gemini says communication itself has become the boundary.

### Remaining Steps (Partial — Pending Full Storyform Data)

**Jupiter** in a sign encoding Destiny as expansion source — Sagittarius (domicile) is the direct candidate. Her ability to see where things are going is her one zone of grace.

**Uranus** encoding Inequity as the disruption-solution — Aquarius (domicile). The thing she must eventually accept is that the system is not and was never fair. This acceptance is initially experienced as threat to her entire Equity-based identity.

**Neptune** encoding Desire as the false signal — Pisces (domicile). She chases wanting as if getting what she wants will solve the problem. It will not. Desire is the symptom, not the disease.

**Pluto** encoding Failure + Good as the terminal condition — Scorpio (domicile). Total destruction that yields meaning. She loses everything and it matters.

_(Full angle, house, and remaining aspect assignments require complete storyform extraction.)_

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial DAI Expansion. Complete derivation sequence, element-to-sign mapping tables, all planetary derivation rules, angle rules, aspect rules, house assignment rules, dignity calculation rules, Void Variable assignment protocol, Tier 2 abbreviated derivation, and partial Victoria Midnight worked example.|
