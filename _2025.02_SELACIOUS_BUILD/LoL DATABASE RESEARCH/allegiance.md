```
allegiance {
  allegiance_id integer pk increments unique
  allegiance_name varchar
  faction_type varchar
  parent_region varchar
  founding_history text
  core_philosophy_or_creed varchar
  leadership_structure varchar
  key_members text
  champion_relationship_type varchar
  associated_events varchar
  alignment_morality varchar
  narrative_function varchar
  opposing_factions text
  visual_symbolism text
  related_skinlines_or_aus varchar
  canon_resources text
  influence_scale varchar
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Allegiance_ID](#1_allegiance_id)
- [2. Allegiance_Name](#2_allegiance_name)
- [3. Faction_Type](#3_faction_type)
- [4. Parent_Region](#4_parent_region)
- [5. Founding_History](#5_founding_history)
- [6. Core_Philosophy_or_Creed](#6_core_philosophy_or_creed)
- [7. Leadership_Structure](#7_leadership_structure)
- [8. Key_Members](#8_key_members)
- [9. Champion_Relationship_Type](#9_champion_relationship_type)
- [10. Associated_Events](#10_associated_events)
- [11. Alignment_Morality](#11_alignment_morality)
- [12. Narrative_Function](#12_narrative_function)
- [13. Opposing_Factions](#13_opposing_factions)
- [14. Visual_Symbolism](#14_visual_symbolism)
- [15. Related_Skinlines_or_AUs](#15_related_skinlines_or_aus)
- [16. Canon_Resources](#16_canon_resources)
- [17. Influence_Scale](#17_influence_scale)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Allegiance**

---

## 1. Allegiance_ID

- **Definition**: Unique identifier for the allegiance (slug or numeric).
- **Examples**: `kinkou_order`, `black_rose`, `noxian_military`

---

## 2. Allegiance_Name

- **Definition**: Full canonical name of the faction, group, or order.
- **Examples**: Kinkou Order, The Black Rose, Noxian Trifecta

---

## 3. Faction_Type

- **Definition**: Core type of organization.
- **Values**:
  - Military
  - Religious
  - Magical Order
  - Secret Society
  - Rebel Cell
  - Scientific Institution
  - Merchant Guild
  - Political Cabal
  - Cult
  - Independent Entity

---

## 4. Parent_Region

- **Definition**: The geopolitical region with which the allegiance is most associated.
- **Values**:
  - Demacia
  - Noxus
  - Ionia
  - Piltover
  - Zaun
  - Targon
  - Freljord
  - Shadow Isles
  - Shurima
  - Void (none)
  - Global / Independent

---

## 5. Founding_History

- **Definition**: Short summary of the origin, founding myth, or historical context of the group.

---

## 6. Core_Philosophy_or_Creed

- **Definition**: Summarized belief system, code, or motto.
- **Examples**:
  - “Balance above all.” (Kinkou Order)
  - “Only the strong thrive.” (Noxus)
  - “Power is meant to be wielded.” (Black Rose)

---

## 7. Leadership_Structure

- **Definition**: Organizational hierarchy.
- **Values**:
  - Single Leader (Monarch, Archmage, General, etc.)
  - Council of Equals
  - Triumvirate
  - High Priesthood
  - Shadow Figure / Puppet Master
  - Leaderless / Decentralized

---

## 8. Key_Members

- **Definition**: Notable characters belonging to the group.
- **Structure**:
  - Champion_ID
  - Name
  - Rank/Role (e.g. Master, Initiate, Enforcer, etc.)
  - Status (Active / Former / Deceased)

---

## 9. Champion_Relationship_Type

- **Definition**: Defines how a champion is aligned.
- **Values**:
  - Member
  - Leader
  - Former Member
  - Opposes
  - Created By
  - Manipulated By
  - Traitor / Defector

---

## 10. Associated_Events

- **Definition**: Canonical events or major plot arcs the group is involved in.
- **Examples**:
  - The Ruination (Sentinels of Light)
  - Freljordian Unification (Frostguard, Avarosan)
  - Arcane Conflict (Council of Piltover)

---

## 11. Alignment_Morality

- **Definition**: Alignment in narrative morality terms.
- **Values**:
  - Lawful Good
  - Chaotic Good
  - True Neutral
  - Lawful Evil
  - Chaotic Evil
  - Morally Grey

---

## 12. Narrative_Function

- **Definition**: Story role or trope function of the allegiance.
- **Values**:
  - Mentor Organization
  - Antagonistic Force
  - Secret Society
  - Fallen Institution
  - Heroic Order
  - Background Lore Anchor

---

## 13. Opposing_Factions

- **Definition**: Known rival or enemy allegiances.
- **Structure**:
  - Allegiance_ID
  - Relationship Type (War / Subversion / Competition)

---

## 14. Visual_Symbolism

- **Definition**: Key imagery or iconography tied to the faction.
- **Structure**:
  - Primary Symbol (e.g., Lotus, Raven, Mask)
  - Color Palette
  - Style Reference (e.g. Shadow Ninja, Roman Imperial, Gothic, etc.)

---

## 15. Related_Skinlines_or_AUs

- **Definition**: Alternate universes or skinlines where the allegiance is reinterpreted.
- **Examples**:
  - PROJECT (Zaunite Enforcers/Rebels)
  - Star Guardian (Magical Girl Orders)
  - High Noon (Cult Orders and Lawkeepers)

---

## 16. Canon_Resources

- **Definition**: Lore texts, cinematics, or stories where the allegiance appears.
- **Structure**:
  - Source Title
  - Media Type (Short Story, Comic, Cinematic)
  - Link/Reference

---

## 17. Influence_Scale

- **Definition**: Narrative and geopolitical power level.
- **Values**:
  - Local
  - Regional
  - Interregional
  - Global
  - Cosmic

---

## 18. Codex_Notes

- **Definition**: Developer commentary, lore inconsistencies, or editorial flags.

---

```

```
