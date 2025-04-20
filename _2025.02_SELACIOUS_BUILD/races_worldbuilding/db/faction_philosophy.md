## 📘 Table of Contents

- [1. Faction_Philosophy_ID](#1_faction_philosophy_id)
- [2. Label](#2_label)
- [3. Summary](#3_summary)
- [4. Belief_System](#4_belief_system)
- [5. Regulation_Principle](#5_regulation_principle)
- [6. View_on_Sex](#6_view_on_sex)
- [7. View_on_Power](#7_view_on_power)
- [8. Conflict_Tendency](#8_conflict_tendency)
- [9. Associated_Rituals](#9_associated_rituals)
- [10. Used_By](#10_used_by)
- [11. Codex_Notes](#11_codex_notes)

---

# **Narrative Asset Schema: faction_philosophies**

---

## 1. Faction_Philosophy_ID

- Unique identifier for the faction philosophy.
- Format: integer or slug.
- Examples: `wild_mutationism`, `totem_purity_law`, `algorithmic_orgasmism`

---

## 2. Label

- Canonical name of the philosophy.
- Should be succinct but thematic.
- Examples:
  - Flesh Discipline
  - Pain Purism
  - Synthetic Harmony
  - Totemic Fidelity
  - Mutation Ecstasy

---

## 3. Summary

- One-sentence encapsulation of the philosophy’s core belief.
- Example: “Pain must be ritualized or it is meaningless.”

---

## 4. Belief_System

- Extended articulation of the philosophy's structure.
- Can include spiritual dogma, political logic, or mythic justification.
- Example: “The body is a sacred equation, and pleasure must be solved through algorithmic control.”

---

## 5. Regulation_Principle

- How sex, behavior, or identity is policed or moderated within this faction.
- Examples:
  - Moan quota enforcement
  - Prohibited climax types
  - Posture purity tracking
  - Totem-only mating permissions

---

## 6. View_on_Sex

- The faction’s conceptual framework of sex itself.
- Examples:
  - Weapon
  - Sacrament
  - Transaction
  - Ascension Mechanism
  - Glitch Interface

---

## 7. View_on_Power

- How the philosophy interprets or distributes power — especially through sexual acts.
- Examples:
  - Only through denial
  - In constant reversal
  - Through beauty and poise
  - Through biological output

---

## 8. Conflict_Tendency

- How this philosophy behaves when in contact with opposing views.
- Examples:
  - Converts outsiders violently
  - Sabotages rituals of others
  - Avoids all non-initiates
  - Encourages philosophical fusion

---

## 9. Associated_Rituals

- Rituals that arise from this belief system.
- Can link to `rituals` table or be internally stored.
- Examples:
  - Edge Ordeals
  - Nectar Suppression Weeks
  - Scar Geometry Contests

---

## 10. Used_By

- The faction(s) that follow this belief system.
- Values: faction IDs or names (e.g., "Order of Obsidian", "Totemweavers")

---

## 11. Codex_Notes

- Commentary, contradictions, memetic behavior, or design artifacts. Can also note origin within factional schism or race-wide split.
