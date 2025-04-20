## 📘 Table of Contents

- [1. Logic_ID](#1-logic_id)
- [2. Champion_ID](#2-champion_id)
- [3. Base_Role](#3-base_role)
- [4. Sub_Role](#4-sub_role)
- [5. Attack_Type](#5-attack_type)
- [6. Damage_Type](#6-damage_type)
- [7. Resource_Type](#7-resource_type)
- [8. Primary_Scaling_Stat](#8-primary_scaling_stat)
- [9. Secondary_Scaling_Stat](#9-secondary_scaling_stat)
- [10. Gameplay_Ratings](#10-gameplay_ratings)
- [11. Base_Stats](#11-base_stats)
- [12. Per_Level_Scaling](#12-per_level_scaling)
- [13. Scaling_Notes](#13-scaling_notes)
- [14. Behavior_Profile](#14-behavior_profile)
- [15. Kit_Synergy_Tags](#15-kit_synergy_tags)
- [16. Anti_Synergy_Tags](#16-anti_synergy_tags)
- [17. Design_Flags](#17-design_flags)

---

# **Gameplay Schema: champion_game_logic**

---

## 1. Logic_ID

- Unique identifier for each logical ruleset instance attached to a champion.

---

## 2. Champion_ID

- Foreign key linking this logic record to the champion entity.
- Structure:
  - `champion_id` (int)
  - `label`: e.g. `"Ahri"`
  - `title`: e.g. `"The Nine-Tailed Fox"`

---

## 3. Base_Role

- Primary strategic function in team compositions.
- Examples:
  - Mage
  - Assassin
  - Tank
  - Support
  - Marksman
  - Fighter

---

## 4. Sub_Role

- Further specification of role or playstyle.
- Examples:
  - Burst
  - Disruptor
  - Duelist
  - Battle Mage
  - Enchanter
  - Artillery

---

## 5. Attack_Type

- How basic attacks are delivered.
- Values:
  - Melee
  - Ranged
  - Hybrid

---

## 6. Damage_Type

- Primary form of outgoing damage.
- Values:
  - Physical
  - Magical
  - True
  - Mixed

---

## 7. Resource_Type

- Resource used to cast abilities.
- Values:
  - Mana
  - Energy
  - Health
  - None
  - Unique (e.g. Grit, Ferocity, Heat)

---

## 8. Primary_Scaling_Stat

- What stat most abilities scale with.
- Examples:
  - Ability Power
  - Attack Damage
  - Max HP

---

## 9. Secondary_Scaling_Stat

- Optional stat secondary abilities may scale with.
- Examples:
  - Crit Chance
  - Bonus Armor
  - Missing Health

---

## 10. Gameplay_Ratings

- 1–10 scale of gameplay metrics:
  - `mobility_rating`
  - `crowd_control_rating`
  - `burst_rating`
  - `sustain_rating`
  - `utility_rating`
  - `difficulty_rating`

---

## 11. Base_Stats

- Level 1 values:
  - `base_hp`
  - `base_mp`
  - `base_attack_damage`
  - `base_armor`
  - `base_magic_resist`
  - `base_attack_speed`
  - `base_move_speed`

---

## 12. Per_Level_Scaling

- Stat growth per level:
  - `hp_per_level`
  - `mp_per_level`
  - `attack_damage_per_level`
  - `armor_per_level`
  - `magic_resist_per_level`
  - `attack_speed_per_level`

---

## 13. Scaling_Notes

- Free-text field describing non-linear growth, spikes, breakpoints.

---

## 14. Behavior_Profile

- Text field for AI logic or player mastery guidance.
- Examples:
  - Hit-and-run disruptor
  - Terrain-dependent initiator

---

## 15. Kit_Synergy_Tags

- Comma-separated keywords for game logic synergy:
  - e.g. `"Zone Control, Reposition, Gap Closer"`

---

## 16. Anti_Synergy_Tags

- Weakness flags:
  - `"No Escape"`, `"Low Range"`, `"Cooldown Reliant"`

---

## 17. Design_Flags

- Development and classification metadata:
  - Legacy
  - Rework Candidate
  - Experimental
  - Tutorial
  - Balance Locked
