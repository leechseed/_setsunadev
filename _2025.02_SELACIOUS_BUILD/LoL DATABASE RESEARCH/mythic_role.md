```
mythic_role {
  mythic_role_id integer pk increments unique
  champion_id integer > champion.champion_id
  mythic_role_label varchar
  role_tier varchar
  role_function text
  associated_cosmology varchar
  binding_force_or_artifact varchar
  transformation_link text
  opposing_mythic_force text
  narrative_theme text
  mythic_symbolism text
  mythic_lineage_or_origin text
  impact_on_lore_canon integer
  mythic_arc_status varchar
  crossmedia_presence text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Mythic_Role_ID](#1_mythic_role_id)
- [2. Champion_ID](#2_champion_id)
- [3. Mythic_Role_Label](#3_mythic_role_label)
- [4. Role_Tier](#4_role_tier)
- [5. Role_Function](#5_role_function)
- [6. Associated_Cosmology](#6_associated_cosmology)
- [7. Binding_Force_or_Artifact](#7_binding_force_or_artifact)
- [8. Transformation_Link](#8_transformation_link)
- [9. Opposing_Mythic_Force](#9_opposing_mythic_force)
- [10. Narrative_Theme](#10_narrative_theme)
- [11. Mythic_Symbolism](#11_mythic_symbolism)
- [12. Mythic_Lineage_or_Origin](#12_mythic_lineage_or_origin)
- [13. Impact_on_Lore_Canon](#13_impact_on_lore_canon)
- [14. Mythic_Arc_Status](#14_mythic_arc_status)
- [15. Cross-Media_Presence](#15_crossmedia_presence)
- [16. Codex_Notes](#16_codex_notes)

---

# **Narrative Asset Schema: Mythic_Role**

---

## 1. Mythic_Role_ID

- **Definition**: Unique identifier (slug or numeric) for the mythic role instance.
- **Examples**: `avatar_of_aspect`, `herald_of_void`, `cosmic_fragment`

---

## 2. Champion_ID

- **Definition**: The champion to which this mythic role is assigned.
- **Examples**: `aatrox`, `pantheon`, `lillia`

---

## 3. Mythic_Role_Label

- **Definition**: Canonical title or description of the mythic role.
- **Examples**: Aspect Host, Ruined King, Void Herald, Spirit Dreamwalker, Living Weapon

---

## 4. Role_Tier

- **Definition**: Scale of influence and mythic importance.
- **Values**:
  - Mortal Echo
  - Regional Myth
  - World-Shaper
  - Cosmic Entity
  - Primordial Force

---

## 5. Role_Function

- **Definition**: Core symbolic or metaphysical function.
- **Examples**:
  - Avatar of a Celestial Force
  - Bearer of a Forbidden Weapon
  - Embodiment of Death, War, or Dream
  - Catalyst of Apocalypse
  - Spirit Guide / Psychopomp
  - Lost God / Fallen Champion

---

## 6. Associated_Cosmology

- **Definition**: The metaphysical system or domain the mythic role belongs to.
- **Examples**:
  - Targon (Celestial Pantheon)
  - The Void
  - Shadow Isles
  - Spirit Realm / Ionia
  - Shuriman Ascended Order
  - World Runes / Elemental Forces

---

## 7. Binding_Force_or_Artifact

- **Definition**: The object or power that connects the champion to the mythic role.
- **Examples**:
  - Rhaast (Kayn)
  - Aspect of War (Pantheon)
  - Sun Disc (Renekton, Nasus)
  - Dream Tree (Lillia)
  - Ruined Blade (Viego)

---

## 8. Transformation_Link

- **Definition**: Whether the mythic role was attained through a known transformation.
- **Structure**:
  - From: Mortal Role
  - To: Mythic Role
  - Trigger Event

---

## 9. Opposing_Mythic_Force

- **Definition**: Antagonistic or cosmologically opposed force.
- **Examples**:
  - Light vs Void (Lux ↔ Vel'Koz)
  - Order vs Chaos (Karma ↔ Jhin)
  - Ascended vs Darkin (Nasus ↔ Aatrox)
  - Life vs Death (Kindred ↔ Mordekaiser)

---

## 10. Narrative_Theme

- **Definition**: Central metaphysical or philosophical theme expressed by the role.
- **Examples**:
  - Death and Rebirth
  - Memory and Oblivion
  - War and Resistance
  - Hubris and Fall
  - Protection vs Control
  - Sacrifice and Transcendence

---

## 11. Mythic_Symbolism

- **Definition**: Visual or symbolic motifs reinforcing the role.
- **Examples**:
  - Halo, Wings, Eclipse, Chains, Mirrors, Masks, Stars, Blossoms, Ruins

---

## 12. Mythic_Lineage_or_Origin

- **Definition**: Source of the mythic status in lore history.
- **Examples**:
  - Chosen by Celestial Deity
  - Artificially Created Weapon
  - Corrupted Ascended
  - Born of Void Rift
  - Inherited Mythic Mantle

---

## 13. Impact_on_Lore_Canon

- **Definition**: Degree of influence on worldbuilding and cosmology.
- **Scale**:
  - 5 = Foundation of a Realm (e.g. Ornn, Aurelion Sol)
  - 4 = Catalyst for Global Event (e.g. Viego, Xerath)
  - 3 = Localized Mythological Force (e.g. Lillia, Kindred)
  - 2 = Hidden or Forgotten Entity
  - 1 = Subtextual / Implied

---

## 14. Mythic_Arc_Status

- **Definition**: Current narrative state of the mythic role.
- **Values**:
  - Active
  - Dormant / Suppressed
  - Sealed / Bound
  - Fragmented
  - Reawakened
  - Unknown

---

## 15. Cross-Media_Presence

- **Definition**: Mythic role depiction in other Riot media.
- **Structure**:
  - Media Title
  - Medium: (Cinematic, Short Story, Comic, Legends of Runeterra)
  - Depth of Role: (Explicit / Implied / Retconned)

---

## 16. Codex_Notes

- **Definition**: Commentary on contradictions, retcons, or symbolic theory interpretations of the mythic role.

---
