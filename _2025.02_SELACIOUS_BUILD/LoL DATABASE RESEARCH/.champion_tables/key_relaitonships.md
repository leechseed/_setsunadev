```
key_relationships {
  relationship_id integer pk increments unique
  source_champion_id integer > champion.champion_id
  target_entity_id varchar
  relationship_type varchar
  emotional_dynamic varchar
  relationship_status varchar
  narrative_significance integer
  interaction_mode varchar
  historical_context text
  timeline_of_changes text
  associated_themes text
  mutuality_flag varchar
  crossmedia_representation text
  visual_symbolism text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Relationship_ID](#1_relationship_id)
- [2. Source_Champion_ID](#2_source_champion_id)
- [3. Target_Entity_ID](#3_target_entity_id)
- [4. Relationship_Type](#4_relationship_type)
- [5. Emotional_Dynamic](#5_emotional_dynamic)
- [6. Relationship_Status](#6_relationship_status)
- [7. Narrative_Significance](#7_narrative_significance)
- [8. Interaction_Mode](#8_interaction_mode)
- [9. Historical_Context](#9_historical_context)
- [10. Timeline_of_Changes](#10_timeline_of_changes)
- [11. Associated_Themes](#11_associated_themes)
- [12. Mutuality_Flag](#12_mutuality_flag)
- [13. Cross-Media_Representation](#13_crossmedia_representation)
- [14. Visual_Symbolism](#14_visual_symbolism)
- [15. Codex_Notes](#15_codex_notes)

---

# **Narrative Asset Schema: Key_Relationships**

---

## 1. Relationship_ID

- **Definition**: Unique identifier (slug or numeric) for the relationship instance.
- **Examples**: `lucian_senna`, `yasuo_yone`, `viego_isolde`

---

## 2. Source_Champion_ID

- **Definition**: Champion initiating or from whom the relationship is viewed.
- **Example**: `lucian`

---

## 3. Target_Entity_ID

- **Definition**: Target of the relationship (can be a champion, non-playable character, or faction).
- **Examples**: `senna`, `yone`, `isolde`, `kinkou_order`

---

## 4. Relationship_Type

- **Definition**: Nature of the bond.
- **Values**:
  - Romantic
  - Sibling
  - Parent / Child
  - Mentor / Student
  - Rival
  - Ally / Comrade
  - Enemy / Nemesis
  - Creator / Creation
  - Master / Servant
  - Institutional (e.g. Faction Loyalty)
  - Betrayer / Betrayed
  - Unknown / Ambiguous

---

## 5. Emotional_Dynamic

- **Definition**: Dominant emotional state or tone in the relationship.
- **Values**:
  - Love
  - Hatred
  - Loyalty
  - Obsession
  - Guilt
  - Jealousy
  - Grief
  - Fear
  - Reverence
  - Resentment
  - Duty

---

## 6. Relationship_Status

- **Definition**: Current state of the relationship in canon.
- **Values**:
  - Active
  - Broken / Estranged
  - Redeemed / Reconciled
  - One-sided / Unaware
  - Terminated (Death / Severance)
  - Complicated
  - Evolving
  - Unknown

---

## 7. Narrative_Significance

- **Definition**: How central the relationship is to the source champion’s arc.
- **Scale**:
  - 5 = Defining Motivation (e.g. Viego → Isolde)
  - 4 = Core Arc Driver (e.g. Yasuo ↔ Yone)
  - 3 = Supporting Theme (e.g. Lucian ↔ Thresh)
  - 2 = Flavor Connection (e.g. Twisted Fate ↔ Graves)
  - 1 = Minor / Referenced

---

## 8. Interaction_Mode

- **Definition**: Primary method of relationship expression.
- **Values**:
  - Lore Narrative
  - Cinematic
  - Voice Lines
  - In-Game Mechanics (e.g., Lucian + Senna synergy)
  - Backstory Only
  - Visual Symbolism (e.g., shared design motifs)

---

## 9. Historical_Context

- **Definition**: Summary of how the relationship was formed.
- **Examples**:
  - Grew up together
  - Trained under same master
  - One killed the other’s mentor
  - Were lovers before a war
  - Created by the same force
  - Betrayal during a rebellion

---

## 10. Timeline_of_Changes

- **Definition**: How the relationship has changed over time.
- **Structure**:
  - From → To
  - Trigger Event
  - Timestamp or Story Reference
- **Examples**:
  - Ally → Enemy (Trigger: Murder of a loved one)
  - Sibling → Reconciled Rival (Trigger: Reunion after death)

---

## 11. Associated_Themes

- **Definition**: Narrative themes explored through the relationship.
- **Examples**:
  - Forgiveness
  - Duality
  - Legacy
  - Love vs Duty
  - Vengeance
  - Loss of Innocence
  - Bound by Fate

---

## 12. Mutuality_Flag

- **Definition**: Whether both parties share or acknowledge the relationship similarly.
- **Values**:
  - Mutual
  - Unreciprocated
  - Unknown
  - Obsessive (One-sided fixation)
  - Contradictory Perspectives

---

## 13. Cross-Media_Representation

- **Definition**: Whether the relationship appears in external lore (Arcane, cinematics, comics).
- **Structure**:
  - Media Title
  - Medium: (Arcane, Comic, Short Story, Cinematic)
  - Representation Depth: (Primary / Secondary / Implied)

---

## 14. Visual_Symbolism

- **Definition**: Motifs or design elements that reinforce the relationship.
- **Examples**:
  - Shared weapons or marks (e.g., Yasuo/Yone’s wind)
  - Mirrored outfits
  - Inverted colors
  - Shared item references
  - Synchronized ability visuals or themes

---

## 15. Codex_Notes

- **Definition**: Commentary on unresolved tensions, lore inconsistencies, or subtextual interpretations.

---
