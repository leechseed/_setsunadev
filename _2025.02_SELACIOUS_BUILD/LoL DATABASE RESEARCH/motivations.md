```
motivations {
  motivation_id integer pk increments unique
  motivation_label varchar
  motivation_type varchar
  drive_intensity varchar
  moral_alignment varchar
  narrative_function varchar
  champion_associations text
  opposing_motivations text
  motivation_arcs text
  emotional_tone varchar
  thematic_keywords text
  cultural_influence text
  symbolic_representation text
  representative_quotes text
  motivation_complexity_score integer
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Motivation_ID](#1_motivation_id)
- [2. Motivation_Label](#2_motivation_label)
- [3. Motivation_Type](#3_motivation_type)
- [4. Drive_Intensity](#4_drive_intensity)
- [5. Moral_Alignment](#5_moral_alignment)
- [6. Narrative_Function](#6_narrative_function)
- [7. Champion_Associations](#7_champion_associations)
- [8. Opposing_Motivations](#8_opposing_motivations)
- [9. Motivation_Arcs](#9_motivation_arcs)
- [10. Emotional_Tone](#10_emotional_tone)
- [11. Thematic_Keywords](#11_thematic_keywords)
- [12. Cultural_Influence](#12_cultural_influence)
- [13. Symbolic_Representation](#13_symbolic_representation)
- [14. Representative_Quotes](#14_representative_quotes)
- [15. Motivation_Complexity_Score](#15_motivation_complexity_score)
- [16. Codex_Notes](#16_codex_notes)

---

# **Narrative Asset Schema: Motivations**

---

## 1. Motivation_ID

- **Definition**: Unique identifier (slug or numeric) for each motivation entry.
- **Examples**: `vengeance`, `redemption`, `order`, `curiosity`

---

## 2. Motivation_Label

- **Definition**: Canonical name of the motivation.
- **Examples**: Power, Revenge, Protection, Discovery, Survival, Glory

---

## 3. Motivation_Type

- **Definition**: Psychological or philosophical category.
- **Values**:
  - Emotional (e.g., Love, Anger, Guilt)
  - Ethical (e.g., Justice, Redemption)
  - Existential (e.g., Identity, Transcendence)
  - Philosophical (e.g., Freedom, Order)
  - Narrative Device (e.g., Plot Catalyst, False Belief)

---

## 4. Drive_Intensity

- **Definition**: Narrative dominance of this motivation.
- **Values**:
  - Core Drive (Primary)
  - Secondary Drive (Supporting)
  - Masked Drive (Hidden)
  - Conflicted Drive (Internal Opposition)
  - Absent / Implied

---

## 5. Moral_Alignment

- **Definition**: Ethical positioning of the motivation.
- **Values**:
  - Noble / Heroic
  - Morally Ambiguous
  - Selfish / Corrupt
  - Dual / Contextual

---

## 6. Narrative_Function

- **Definition**: Structural role the motivation plays in story development.
- **Values**:
  - Arc Catalyst
  - Arc Resolution Goal
  - Internal Conflict Generator
  - Ideological Contrast
  - Redemption Trigger
  - Motivation Misdirection

---

## 7. Champion_Associations

- **Definition**: Champions defined by or driven by this motivation.
- **Structure**:
  - Champion_ID
  - Name
  - Role: (Core / Secondary / Rejected)

---

## 8. Opposing_Motivations

- **Definition**: Narratively or thematically opposing drives.
- **Structure**:
  - Motivation_ID
  - Opposition_Type: (Ideological, Emotional, Functional)

---

## 9. Motivation_Arcs

- **Definition**: Common transformational pathways involving this motivation.
- **Structure**:
  - From → To
  - Trigger or Event
- **Examples**:
  - Vengeance → Redemption (Trigger: Truth revealed)
  - Order → Chaos (Trigger: Betrayal)

---

## 10. Emotional_Tone

- **Definition**: General affective feel of the motivation.
- **Values**:
  - Hopeful
  - Desperate
  - Violent
  - Righteous
  - Naïve
  - Obsessive

---

## 11. Thematic_Keywords

- **Definition**: Tags summarizing core themes associated with the motivation.
- **Examples**:
  - Control
  - Sacrifice
  - Liberation
  - Legacy
  - Identity
  - Loyalty
  - Madness

---

## 12. Cultural_Influence

- **Definition**: Real-world philosophical, mythological, or religious influences.
- **Examples**:
  - Greek Tragedy (e.g., Hubris, Fate)
  - Confucianism (e.g., Duty)
  - Romanticism (e.g., Passion > Reason)
  - Nietzschean Will (e.g., Power, Self-Creation)

---

## 13. Symbolic_Representation

- **Definition**: Visual or poetic motifs often linked to the motivation.
- **Examples**:
  - Power → Crown, Flame, Fist
  - Redemption → Light, Chains, Blood
  - Curiosity → Eyes, Books, Keys
  - Chaos → Masks, Fire, Shattered Glass

---

## 14. Representative_Quotes

- **Definition**: Voice lines or lore excerpts expressing the motivation.
- **Structure**:
  - Champion_ID
  - Quote
  - Context or Lore Reference

---

## 15. Motivation_Complexity_Score

- **Definition**: Depth of narrative modeling available.
- **Scale**:
  - 1 = Simple / Surface
  - 2 = Binary
  - 3 = Dual Conflict
  - 4 = Layered / Symbolic
  - 5 = Multifaceted / Thematic Pillar

---

## 16. Codex_Notes

- **Definition**: Developer commentary, contradictions, evolution notes, or lore fragmentation.

---
