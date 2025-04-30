```
occupation_function {
  occupation_id integer pk increments unique
  occupation_label varchar
  occupation_class varchar
  narrative_function varchar
  societal_position varchar
  allegiance_integration varchar
  combat_orientation varchar
  occupation_symbolism text
  representative_champions text
  dual_occupation_flags text
  evolution_pathways text
  real_world_inspiration text
  visual_coding text
  institutional_affiliation text
  occupation_status varchar
  occupation_mythos_tier varchar
  lore_sources text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Occupation_ID](#1_occupation_id)
- [2. Occupation_Label](#2_occupation_label)
- [3. Occupation_Class](#3_occupation_class)
- [4. Narrative_Function](#4_narrative_function)
- [5. Societal_Position](#5_societal_position)
- [6. Allegiance_Integration](#6_allegiance_integration)
- [7. Combat_Orientation](#7_combat_orientation)
- [8. Occupation_Symbolism](#8_occupation_symbolism)
- [9. Representative_Champions](#9_representative_champions)
- [10. Dual_Occupation_Flags](#10_dual_occupation_flags)
- [11. Evolution_Pathways](#11_evolution_pathways)
- [12. Real_World_Inspiration](#12_real_world_inspiration)
- [13. Visual_Coding](#13_visual_coding)
- [14. Institutional_Affiliation](#14_institutional_affiliation)
- [15. Occupation_Status](#15_occupation_status)
- [16. Occupation_Mythos_Tier](#16_occupation_mythos_tier)
- [17. Lore_Sources](#17_lore_sources)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Occupation_Function**

---

## 1. Occupation_ID

- **Definition**: Unique identifier (slug or numeric) for the occupation.
- **Examples**: `warrior`, `assassin`, `prophet`, `inventor`

---

## 2. Occupation_Label

- **Definition**: Canonical occupation name.
- **Examples**: Warrior, General, Mage, Inventor, Cultist

---

## 3. Occupation_Class

- **Definition**: Broad occupational category.
- **Values**:
  - Military
  - Magical
  - Religious
  - Political
  - Academic / Scientific
  - Criminal / Underground
  - Artisan / Engineer
  - Explorer / Adventurer
  - Divine / Mythic
  - Civilian
  - Constructed Role (e.g., Weapon, Host)

---

## 4. Narrative_Function

- **Definition**: Thematic or structural function the occupation serves in lore.
- **Examples**:
  - Enforcer of Law
  - Agent of Chaos
  - Guardian of a Realm
  - Reluctant Champion
  - Institutional Rebel
  - Avatar of a Force

---

## 5. Societal_Position

- **Definition**: Social standing or authority level in-world.
- **Values**:
  - Ruler / Head of State
  - Commander / General
  - High Priest / Seer
  - Elite Agent / Specialist
  - Commoner / Wanderer
  - Criminal / Fugitive
  - Legendary / Mythologized

---

## 6. Allegiance_Integration

- **Definition**: Whether the occupation ties into a larger faction or institution.
- **Values**:
  - Institutional (e.g., Demacian Mage Seeker)
  - Independent (e.g., Self-taught Inventor)
  - Rogue / Renegade (e.g., Ex-Kinkou)
  - Divinely Appointed
  - Created Role (e.g., Construct, Host)

---

## 7. Combat_Orientation

- **Definition**: How the occupation influences combat behavior in-universe.
- **Values**:
  - Frontline Fighter
  - Assassin / Infiltrator
  - Tactical Commander
  - Magical Artillery
  - Support / Healing
  - Noncombatant / Passive

---

## 8. Occupation_Symbolism

- **Definition**: Symbolic or archetypal meaning of the role.
- **Examples**:
  - Warrior = Valor, Duty, Sacrifice
  - Assassin = Secrecy, Revenge, Precision
  - Prophet = Vision, Madness, Revelation
  - Inventor = Progress, Hubris, Curiosity

---

## 9. Representative_Champions

- **Definition**: Champions associated with this occupation.
- **Structure**:
  - Champion_ID
  - Name
  - Notes (e.g., "Former Commander", "Self-Proclaimed Prophet")

---

## 10. Dual_Occupation_Flags

- **Definition**: Flags if a character holds more than one functional role.
- **Structure**:
  - Primary_Occupation
  - Secondary_Occupation
  - Narrative Context (e.g., “Jhin is an artist and an assassin”)

---

## 11. Evolution_Pathways

- **Definition**: Known occupational transformations within character arcs.
- **Structure**:
  - From → To
  - Trigger: (e.g., exile, death, ascension, corruption)

---

## 12. Real_World_Inspiration

- **Definition**: Historical, mythological, or pop culture inspirations for the occupation.
- **Examples**:
  - Mage = Renaissance Sorcerers, Druidic Tradition
  - General = Roman Legates, WWII Strategists
  - Inventor = Nikola Tesla, Jules Verne
  - Cultist = Lovecraftian Priesthoods, Apocalyptic Doomsday Sects

---

## 13. Visual_Coding

- **Definition**: Iconography and visual tropes used to depict the occupation.
- **Examples**:
  - Warriors = Armor, Banners, Swords
  - Mages = Staffs, Runes, Glowing Eyes
  - Criminals = Masks, Chains, Shadowy Silhouettes
  - Seers = Blindfolds, Eyes, Flame

---

## 14. Institutional_Affiliation

- **Definition**: Organization or faction tied to the occupation.
- **Structure**:
  - Institution_Name
  - Role (e.g., Agent, Leader, Former Member)

---

## 15. Occupation_Status

- **Definition**: Whether the occupation is active or former within narrative.
- **Values**:
  - Active
  - Former
  - Abandoned / Rejected
  - Forced Role
  - Unknown

---

## 16. Occupation_Mythos_Tier

- **Definition**: How culturally or cosmologically significant the occupation is.
- **Values**:
  - Mundane / Everyday
  - Notable / Skilled
  - Legendary / Revered
  - Transcendent / Divine
  - Forgotten / Forbidden

---

## 17. Lore_Sources

- **Definition**: Canonical media referencing the champion’s occupation.
- **Structure**:
  - Title
  - Media Type (Short Story, Cinematic, Game Event)
  - URL / Reference

---

## 18. Codex_Notes

- **Definition**: Internal commentary, contradictions, or unresolved occupational roles in canon.

---
