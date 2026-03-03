---

## type: ssot_02_character_systems category: integration_mapping version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the formal mapping between Character Astrology chart variables and the 12-Layer Character Database. Specifies which astrological data feeds which layers, the translation logic for each feed, and the independence boundaries where the two systems do not overlap." dependencies: ["ssot_02_character_astrology", "ssot_02_character_astrology_dai", "ssot_03_character_systems_vertical_slice"]
---
# 🔮 SSOT: Character Astrology ↔ 12-Layer Mapping

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [Governing Principles](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#governing-principles)
3. [The Master Feed Table](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-master-feed-table)
4. [Layer-by-Layer Feed Specifications](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#layer-by-layer-feed-specifications)
5. [Independence Boundaries](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#independence-boundaries)
6. [Conflict Resolution Protocol](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#conflict-resolution-protocol)
7. [Feed Validation Checklist](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#feed-validation-checklist)
8. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

Character Astrology and the 12-Layer Character Database are parallel datasets describing the same character in different notation systems. This document is the formal interface between them. It defines exactly which astrological variables feed which layers, how the translation works, and where the two systems are independent of each other.

Without this mapping, the connection between chart data and layer values is implicit — dependent on the narrative designer's intuition rather than a documented specification. This document eliminates that dependency. When a Vertical Slice assigns a value to L8 IMPRINT, this document tells you which chart elements that value should be consistent with and how to verify the consistency.

---

## Governing Principles

**Principle 1: Feed, Not Replace.** Character Astrology feeds the 12-Layer system. It does not replace it. The 12-Layer system assigns numeric values using GURPS-derived mechanics and point-budget logic. Character Astrology provides the symbolic justification and behavioral texture that informs those numeric assignments. The number is the layer's job. The meaning behind the number is astrology's job.

**Principle 2: Consistency, Not Derivation.** Layer values are not mathematically derived from chart variables. A Sun in Taurus does not produce CORE = 13 by formula. The relationship is consistency — a Sun in Taurus is consistent with a character whose CORE reflects stubborn, material, labor-earned cognitive architecture. If the chart says one thing and the layer value says something contradictory, one of them is wrong.

**Principle 3: Not Every Layer Needs Astrology.** Some layers are fed entirely by Dramatica (L12 FUNCTION) or by authored narrative documentation (portions of L7 ORIGIN, L9 EROS). Character Astrology supplements these layers but does not govern them. The feed table marks these as partial or independent feeds.

**Principle 4: The Authoritative Document Governs Both.** When the character's authoritative document (the canonical locked character bible) contains information that conflicts with either the chart or the layer value, the authoritative document wins. Both the chart and the layers are representations of the character defined in that document. Neither representation has authority over the source.

---

## The Master Feed Table

This table provides the complete mapping at a glance. Each row identifies the 12-Layer target, the Character Astrology source(s), the feed type, and whether the feed is required for Vertical Slice completion.

|Layer|Astrology Source(s)|Feed Type|Required for Slice|
|---|---|---|---|
|**L1 CORE**|Sun sign, Sun dignity, Mercury sign, Mercury dignity|Justification + texture|Yes|
|**L2 VITAL**|Mars sign, Mars dignity, Ascendant sign|Justification + texture|Yes|
|**L3 SOCIAL**|Ascendant sign, Venus sign, 7th House contents, Venus aspects|Justification + texture|Yes|
|**L4 WILL**|Saturn sign, Saturn dignity, Sun-Saturn aspects|Justification + ceiling logic|Yes|
|**L5 WOUND**|Debilitated planets, hard aspects to Moon, 8th House contents|Texture + trigger identification|Yes|
|**L6 DRIVE**|Mars sign, Mars aspects, Jupiter sign|Justification + fuel source|Yes|
|**L7 ORIGIN**|IC sign, 4th House contents, Moon sign|Partial — supplements authored origin data|Partial|
|**L8 IMPRINT**|Moon sign, Moon aspects, Moon dignity, 8th House contents|Primary feed — attachment architecture|Yes|
|**L9 EROS**|Venus sign, Venus aspects, Mars-Venus aspect, 5th House contents, 8th House contents|Supplemental — enriches authored eros data|Partial|
|**L10 SHADOW**|12th House contents, debilitated planets, Pluto sign, Pluto aspects, hard aspects to Sun|Primary feed — repression architecture|Yes|
|**L11 DESTINY**|Jupiter sign, Uranus sign, Midheaven sign, Jupiter-Saturn aspects|Primary feed — growth vector|Yes|
|**L12 FUNCTION**|None — fed directly from Dramatica Ingest|Independent|N/A|

**Feed types defined:**

- **Justification + texture**: The chart data explains WHY the numeric value is what it is and adds behavioral detail that the number alone cannot capture.
- **Justification + ceiling logic**: The chart data constrains the plausible range of the numeric value. A Saturn in domicile justifies a higher WILL ceiling than a Saturn in fall.
- **Texture + trigger identification**: The chart data identifies specific conditions under which the layer value activates or escalates.
- **Primary feed**: The chart data is the primary source of content for this layer. Without it, the layer is thin.
- **Supplemental**: The chart data enriches content that is primarily authored from other sources.
- **Partial**: The chart provides some but not all of the layer's content.
- **Independent**: No feed relationship exists.

---

## Layer-by-Layer Feed Specifications

### L1 CORE ← Sun, Mercury

**What L1 needs:** A numeric value (default 10, GURPS IQ-equivalent) representing cognitive and psychological mass. The value must be justified by documented evidence of the character's mental capacity, problem-solving behavior, and ideological framework.

**What Character Astrology provides:**

The **Sun sign** encodes the character's identity axis — what they believe they are and how they orient their cognitive architecture. The Sun's element (Fire/Earth/Air/Water) and modality (Cardinal/Fixed/Mutable) provide the qualitative signature of the character's thinking.

- Earth Sun signs justify CORE values oriented toward practical, material, methodical cognition.
- Air Sun signs justify CORE values oriented toward abstract, conceptual, relational cognition.
- Fire Sun signs justify CORE values oriented toward intuitive, pattern-driven, visionary cognition.
- Water Sun signs justify CORE values oriented toward emotional, empathic, processual cognition.

The **Sun's dignity** informs the ceiling. A Sun in domicile or exaltation is consistent with CORE values at or above the character's tier median. A Sun in detriment or fall is consistent with CORE values that reflect cognitive capacity undermined by the sign's specific distortion — not low intelligence, but intelligence running on misaligned firmware.

**Mercury's sign** encodes the processing style. Mercury's dignity informs whether that processing runs clean or glitchy. Mercury in dignity supports high CORE; Mercury in debility supports CORE that is capable but operationally costly.

**Consistency check:** Read the Sun sign description and the Mercury sign description together. Does the character's CORE value (the number) match the cognitive portrait those two signs paint? If CORE = 13 but the Sun and Mercury both describe a character who processes slowly and struggles with abstraction, something is wrong.

---

### L2 VITAL ← Mars, Ascendant

**What L2 needs:** A numeric value (default 10, GURPS DX-equivalent) representing physical and energetic presence — body precision, endurance, reaction capacity, physical expressiveness.

**What Character Astrology provides:**

**Mars sign** encodes the kinetic style — how the character moves, fights, and engages physically.

- Mars in Fire signs justifies high VITAL with explosive, instinct-driven physicality.
- Mars in Earth signs justifies high VITAL with disciplined, endurance-oriented physicality.
- Mars in Air signs justifies moderate VITAL with technique-oriented, strategic physicality.
- Mars in Water signs justifies VITAL that is emotionally modulated — physical capacity that fluctuates with internal state.

**Mars dignity** directly informs the VITAL ceiling. Mars in exaltation (Capricorn) or domicile (Aries, Scorpio) is consistent with VITAL 12+. Mars in fall (Cancer) or detriment (Taurus, Libra) is consistent with VITAL that carries a specific physical cost or limitation.

**Ascendant sign** encodes the physical presentation — how the body reads in space. The Ascendant does not determine VITAL numerically but it determines the texture of physical expression.

**Consistency check:** Does the character's VITAL value match the physical portrait painted by Mars sign + dignity + Ascendant? A character with Mars in Capricorn (exaltation) and an Aries Ascendant who carries VITAL = 10 (average) needs a documented explanation for why their chart says "elite physical capacity" and their layer value says "average."

---

### L3 SOCIAL ← Ascendant, Venus, 7th House

**What L3 needs:** A numeric value (default 10, GURPS HT-equivalent) representing relational interface — projection into the world, reception of others, social legibility, reaction modifier math.

**What Character Astrology provides:**

**Ascendant sign** encodes the social first impression — the mask the world encounters. Cardinal Ascendants project initiating energy. Fixed Ascendants project stability or immovability. Mutable Ascendants project adaptability or elusiveness.

**Venus sign** encodes what the character values in social exchange and how they attract or repel others.

**7th House contents** (if any planets are placed there) encode the character's relational mode in one-to-one partnerships — the quality of energy they bring to direct relationship.

**Key nuance:** A low SOCIAL value does not necessarily mean social incompetence. Victoria Midnight's SOCIAL = 10 (average) with an Aries Ascendant and Virgo Venus describes a character whose social interface is accurate but unmanaged. The chart explains why SOCIAL is average despite high capability elsewhere — the Ascendant does not filter, Venus does not perform, and the social interface therefore transmits raw signal without protective encoding.

**Consistency check:** Does the SOCIAL value match the social portrait? Pay particular attention to the Ascendant-Venus relationship. If they are in harmonious signs, the social interface is coherent. If they are in tense signs, the social interface has an internal contradiction that the SOCIAL value should reflect.

---

### L4 WILL ← Saturn, Sun-Saturn Aspects

**What L4 needs:** A numeric value derived from CORE by default (WILL = CORE), buyable up or down at 5 pts per level. Represents psychological resistance to coercion, manipulation, and systemic pressure.

**What Character Astrology provides:**

**Saturn sign** encodes the nature of the character's limit — what kind of wall they face. But the same Saturn placement also encodes the character's capacity to endure that wall. Saturn in domicile (Capricorn, Aquarius) describes a character who understands structure and can sustain resistance. Saturn in fall (Aries) describes a character whose resistance is impulsive rather than structural.

**Saturn dignity** informs the buy-up/buy-down decision. Saturn in dignity justifies WILL >= CORE (the character's resistance is at least as strong as their cognition). Saturn in debility justifies WILL < CORE (the character thinks clearly but buckles under sustained pressure) or WILL > CORE with a specific fragility note (the character is stubborn beyond their intelligence, which creates its own problems).

**Sun-Saturn aspects** encode the relationship between identity and limitation:

- Sun conjunct Saturn: Identity and limitation are fused. WILL is high but rigid. The character cannot separate who they are from what constrains them.
- Sun square Saturn: Identity and limitation are in active conflict. WILL is tested constantly. The character's resolve is forged in friction.
- Sun trine Saturn: Identity and limitation flow together easily. WILL is stable but may be untested.
- Sun opposition Saturn: Identity and limitation are in binary opposition. WILL swings between extremes depending on which pole the character is operating from.

**Consistency check:** Does the WILL value match the Saturn portrait? Is the buy-up/buy-down decision consistent with the Saturn dignity?

---

### L5 WOUND ← Debilitated Planets, Hard Moon Aspects, 8th House

**What L5 needs:** A value from 0 (undamaged) to 10 (functional collapse threshold) representing accumulated psychological damage that failed to resolve. Assigned during character history entry — this is a record of what happened, not a choice.

**What Character Astrology provides:**

**Debilitated planets** identify the specific domains where the character's functioning is structurally compromised. Each debilitated planet contributes a specific wound texture:

- Mars in debility: Wound in the action/agency domain. Physical trauma, kinetic helplessness, or violence received.
- Moon in debility: Wound in the emotional/attachment domain. Neglect, abandonment, or emotional conditioning failure.
- Saturn in debility: Wound from structural failure. Institutional betrayal, authority collapse, or rule systems that harmed rather than protected.
- Venus in debility: Wound in the desire/value domain. Shame, unworthiness, or desire that was punished.

**Hard aspects to the Moon** (squares, oppositions) identify the specific stressors that activate the wound. A Moon square Saturn character's wound activates when duty and emotional need collide. A Moon opposition Pluto character's wound activates during power dynamics and loss of control.

**8th House contents** encode transformation through crisis — what the character has lost, what has been taken from them, and what resources they gained through that loss.

**Feed logic:** The number of debilitated planets and hard Moon aspects does not mechanically produce the WOUND value. The wound is authored from the character's documented history. The chart data tells you what KIND of damage the character carries and what triggers re-activation. Use the chart to validate that the WOUND value is consistent with the symbolic damage profile.

---

### L6 DRIVE ← Mars, Jupiter

**What L6 needs:** A numeric value derived from VITAL by default (DRIVE = VITAL), buyable at 3 pts per level. Represents narrative motivation fuel — spent on active goal-pursuit, recovered through narrative resolution.

**What Character Astrology provides:**

**Mars sign** encodes the fuel type — what kind of energy drives the character forward. Fire Mars runs on impulse and conviction. Earth Mars runs on discipline and material goals. Air Mars runs on ideas and strategy. Water Mars runs on emotional necessity.

**Jupiter sign** encodes the replenishment source — where the character finds expansion, temporary safety, and renewed capacity. Jupiter in a compatible element with Mars means drive replenishes naturally. Jupiter in a conflicting element means the character's expansion zone does not match their action style, creating a recovery gap.

**Mars-Jupiter aspects** (if present) encode the relationship between action and growth. Mars trine Jupiter: action naturally leads to expansion. Mars square Jupiter: action and growth are in tension — pursuing goals actively may undermine the conditions for recovery.

**Feed logic for meaning-driven vs ambition-driven:** The Vertical Slice protocol distinguishes between ambition-driven characters (DRIVE = VITAL) and meaning-driven characters (DRIVE < VITAL). The chart helps identify which type the character is. If Mars is in dignity and Jupiter is in a compatible sign, ambition-driven is consistent. If Mars is compromised or Jupiter is in tension with Mars, meaning-driven is consistent — the fuel source is already damaged or misaligned.

---

### L7 ORIGIN ← IC, 4th House, Moon

**What L7 needs:** A variable stack including origin_class, origin_stability, family_coherence, origin_wound_seed, tech_level, system_exposure. These are primarily authored from the character's documented backstory.

**What Character Astrology provides (partial feed):**

**IC sign** encodes the hidden root — the buried origin quality. IC in Earth signs points to material/class-defined origins. IC in Water signs points to emotionally-defined origins. IC in Fire signs points to ambition or conflict-defined origins. IC in Air signs points to intellectually or socially-defined origins.

**4th House contents** (planets placed in the 4th) encode the specific energies present in the character's foundational environment. Saturn in the 4th: authority was heavy in the origin. Moon in the 4th: the origin was emotionally saturated. Mars in the 4th: conflict was present at the root.

**Moon sign** encodes the emotional baseline the character carried out of their origin — the instinctual pattern they developed in response to early conditions.

**Feed logic:** L7 is primarily authored. The chart supplements but does not govern. The IC and 4th House data should be consistent with the authored origin variables. If the IC is in Cancer (emotionally saturated root) but origin_stability = 9 (highly stable), that is not necessarily a contradiction — stable environments can be emotionally intense. But the inconsistency should be noted and justified.

---

### L8 IMPRINT ← Moon (Primary)

**What L8 needs:** A variable stack including attachment_style, attachment_style_score, emotional_range, conditional_patterns, imprint_flexibility, primary_attachment_object.

**What Character Astrology provides (primary feed):**

The Moon is the primary source for L8. The Moon sign, its aspects, and its dignity encode the character's entire emotional conditioning architecture.

**Moon sign** determines the attachment style baseline:

- Moon in Water signs (Cancer, Scorpio, Pisces): High attachment intensity. Anxious or enmeshed patterns likely. Emotional range tends high.
- Moon in Earth signs (Taurus, Virgo, Capricorn): Attachment through stability and reliability. Secure or avoidant patterns likely. Emotional range tends controlled.
- Moon in Fire signs (Aries, Leo, Sagittarius): Attachment through admiration and freedom. Secure-anxious or dismissive patterns likely. Emotional range tends reactive.
- Moon in Air signs (Gemini, Libra, Aquarius): Attachment through intellectual connection and social harmony. Avoidant or secure patterns likely. Emotional range tends modulated.

**Moon aspects** modify the baseline:

- Moon conjunct Venus: Attachment and desire are fused. Strong relational bonding. Imprint flexibility may be low (patterns deeply set).
- Moon square Saturn: Attachment is tested by duty and limitation. Conditional patterns likely include duty-based love language.
- Moon opposition Pluto: Attachment is marked by power dynamics and loss. Secure attachment is difficult. Primary attachment objects may have been lost or threatening.

**Moon dignity** informs imprint_flexibility. Moon in dignity (Cancer domicile, Taurus exaltation): the emotional conditioning system is functional and relatively healthy. Moon in debility (Capricorn detriment, Scorpio fall): the emotional conditioning system is operational but structurally compromised — it works, but at cost.

---

### L9 EROS ← Venus, Mars-Venus, 5th/8th House

**What L9 needs:** A variable stack including erotic_blueprint_type, desire_vector, shame_index, intimacy_mode. Partially authored, partially inferred.

**What Character Astrology provides (supplemental feed):**

**Venus sign** encodes the desire quality — what the character finds beautiful, attractive, and worth pursuing in intimate contexts.

**Mars-Venus aspect** encodes the relationship between desire and action:

- Conjunction: "To desire is to act." Desire and pursuit are fused. Low shame index likely.
- Square: Desire and action conflict. What the character wants and what they do about it are in tension. Higher shame index likely.
- Trine: Desire flows naturally into action. Comfortable sexuality. Low friction.
- Opposition: Desire and action are split. The character may want one thing and pursue another.

**5th House contents** encode creative and romantic expression — how desire manifests in the character's expressive life.

**8th House contents** encode intimate transformation — how the character changes through deep relational and sexual experience.

**Feed logic:** L9 is the most inference-heavy layer. The chart provides the symbolic scaffolding but much of L9 is authored from the character's documented intimate history and aesthetic DNA. The chart validates authored choices rather than producing them.

---

### L10 SHADOW ← 12th House, Debilitated Planets, Pluto

**What L10 needs:** A variable stack including shadow_density, projection_tendency, regression_pattern, shadow_content.

**What Character Astrology provides (primary feed):**

**12th House contents** encode what the character has repressed — the variables operating beneath conscious access. Planets in the 12th House directly feed shadow_content.

**Debilitated planets** encode where the character's system glitches — the functions that do not run cleanly and therefore become sources of shame, denial, or projection. Each debilitated planet contributes a shadow content entry: the thing the character cannot do well and therefore cannot face.

**Pluto sign and aspects** encode the character's relationship with power, control, and destruction. Hard Pluto aspects to personal planets (Sun, Moon, Mercury, Venus, Mars) indicate intense shadow material — power dynamics, control compulsions, or destruction/rebirth patterns that the character may not consciously recognize.

**Shadow density estimation:** Count the debilitated planets, 12th House planets, and hard Pluto aspects. Higher counts are consistent with higher shadow_density values:

- 0-1: Shadow density 1-3 (light shadow, relatively integrated)
- 2-3: Shadow density 4-6 (moderate shadow, active denial or projection)
- 4+: Shadow density 7-10 (heavy shadow, significant repressed content driving behavior)

This is an estimation guideline, not a formula. The narrative designer adjusts based on the character's documented psychology.

---

### L11 DESTINY ← Jupiter, Uranus, Midheaven

**What L11 needs:** A variable stack including growth_axis, resistance_index, soul_evolution_archetype, karmic_memory, growth_requirement.

**What Character Astrology provides (primary feed):**

**Jupiter sign** encodes the growth permission — what domain of life offers the character expansion. Jupiter's sign directly informs the growth_axis.

**Uranus sign** encodes the nature of the disruption the character must accept (Change characters) or resist (Steadfast characters). Uranus directly informs the growth_requirement — the specific transformation or awakening the character's arc moves toward.

**Jupiter-Saturn aspects** encode the relationship between growth and limitation — how easily the character can access their destiny:

- Jupiter conjunct Saturn: Growth and limitation are fused. The character grows through constraint.
- Jupiter square Saturn: Growth and limitation are in active conflict. High resistance_index.
- Jupiter trine Saturn: Growth and limitation flow together. Lower resistance_index. The path is clear but may lack urgency.
- Jupiter opposition Saturn: Growth and limitation are in binary tension. The character oscillates between expansion and contraction.

**Midheaven sign** encodes the public expression of the character's destiny — what the world sees as their achievement or failure. The Midheaven informs the soul_evolution_archetype by defining what the character is building toward in the world's eyes (which may differ from what they are actually building internally).

---

### L12 FUNCTION ← No Astrology Feed

L12 is fed entirely from the Dramatica Ingest Template. Character Astrology has no feed relationship with L12. This boundary is absolute. Dramatica governs narrative function. Astrology governs symbolic character data. They do not cross at L12.

---

## Independence Boundaries

The following elements of Character Astrology have **no feed relationship** to the 12-Layer system:

|Astrology Element|Reason for Independence|
|---|---|
|**Network Topology (Unicursal Hexagram)**|Relationship-level data. Feeds relationship tables, not character records.|
|**Lifecycle Protocol (6 Movements)**|Story-structure data. Feeds plot_systems.|
|**Synastry Overlays**|Relationship-level data. Feeds relationship tables.|
|**Progressions**|State-overlay data. Feeds the character state diff system.|
|**Transits**|State-overlay data. Feeds the character state diff system.|
|**Reset Protocol**|Story-structure data. Feeds plot_systems.|
|**Sextile aspects**|Minor aspects. Documented in the chart but do not feed specific layer values.|

The following 12-Layer elements have **no feed relationship** from Character Astrology:

|Layer Element|Fed By|
|---|---|
|L1-L3 numeric values (the actual numbers)|GURPS point-budget logic and authored justification|
|L4 WILL numeric value|Derived from CORE + buy-up/down|
|L5 WOUND numeric value|Authored from character history|
|L6 DRIVE numeric value|Derived from VITAL + buy-up/down|
|L7 ORIGIN variable stack (most variables)|Authored from character backstory|
|L12 FUNCTION (entire layer)|Dramatica Ingest Template|
|All derived statistics|Computed from layer values, not from chart data|
|All flag trigger conditions|Computed from layer values and derived statistics|

**The key independence principle:** Character Astrology feeds the qualitative justification and behavioral texture of layer values. The 12-Layer system owns the quantitative values and all computation. Astrology tells you why WILL = 14 makes sense. The layer system tells you that WILL = 14 produces a Stress Threshold of 6 when combined with WOUND = 8. These are different jobs.

---

## Conflict Resolution Protocol

When the Character Astrology chart and the 12-Layer values are inconsistent:

**Step 1: Identify the conflict.** State precisely which chart element contradicts which layer value.

**Step 2: Check the authoritative document.** The character's locked canonical documentation governs both systems. If the authoritative document supports the chart, adjust the layer value. If the authoritative document supports the layer value, adjust the chart.

**Step 3: If the authoritative document is ambiguous,** the 12-Layer value takes precedence for computational purposes (derived statistics and flag triggers must remain valid) and the chart is adjusted to be consistent. Document the resolution in both the Character Astrology Ingest Template (Section 9 feed map notes) and the Vertical Slice (in the relevant layer justification prose).

**Step 4: If the conflict reveals a genuine contradiction in the authoritative document,** flag it for narrative designer review. Do not resolve it by adjusting either system. The authoritative document must be revised first, then both downstream representations are updated.

---

## Feed Validation Checklist

Run this checklist after completing both the Character Astrology Ingest Template and the Vertical Slice for a character. Every item must pass or carry a documented exception.

- [ ] Sun sign is consistent with L1 CORE justification prose
- [ ] Mars sign + dignity is consistent with L2 VITAL value and justification
- [ ] Ascendant + Venus is consistent with L3 SOCIAL value and justification
- [ ] Saturn sign + dignity is consistent with L4 WILL buy-up/down decision
- [ ] Debilitated planets and hard Moon aspects are consistent with L5 WOUND triggers
- [ ] Mars + Jupiter is consistent with L6 DRIVE derivation (ambition vs meaning driven)
- [ ] IC and 4th House are consistent with L7 ORIGIN variables (where authored)
- [ ] Moon sign + aspects + dignity are consistent with L8 IMPRINT attachment architecture
- [ ] Venus + Mars-Venus aspect are consistent with L9 EROS variables (where authored)
- [ ] 12th House + debilitated planets + Pluto are consistent with L10 SHADOW content
- [ ] Jupiter + Uranus + Midheaven are consistent with L11 DESTINY growth vector
- [ ] L12 FUNCTION has no astrology feed (confirmed independent)
- [ ] No derived statistic is contradicted by chart data
- [ ] No flag trigger condition is contradicted by chart data
- [ ] All conflicts resolved per Conflict Resolution Protocol

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial mapping specification. Complete feed table, layer-by-layer specifications for all 12 layers, independence boundaries, conflict resolution protocol, and feed validation checklist.|