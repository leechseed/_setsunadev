# **Narrative Logic Schema for League of Legends Champions**

---

## 📘 Table of Contents

- [1. champion_profile_ID (Primary Key)](#1-champion_profile_id-primary-key)
- [2. Champion_ID (Foreign Key)](#2-champion_id-foreign-key)
- [3. Sex_Gender](#3-sex_gender)
- [4. Region_of_Origin](#4-region_of_origin)
- [5. Current_Allegiance](#5-current_allegiance)
- [6. Species_Race](#6-species_race)
- [7. Life_Stage](#7-life_stage)
- [8. Narrative_Archetype](#8-narrative_archetype)
- [9. Personality_Trait_Dominants](#9-personality_trait_dominants)
- [10. Narrative_Status](#10-narrative_status)
- [11. Occupation_Function](#11-occupation_function)
- [12. Motivations](#12-motivations)
- [13. Backstory_Summary](#13-backstory_summary)
- [14. Key_Relationships](#14-key_relationships)
- [15. Transformations_or_Evolutions](#15-transformations_or_evolutions)
- [16. Affiliated_Events](#16-affiliated_events)
- [17. Mythic_or_Cosmic_Role](#17-mythic_or_cosmic_role)
- [18. Thematic_Keywords](#18-thematic_keywords)
- [19. Visual_Theme](#19-visual_theme)
- [20. Cultural_Influence](#20-cultural_influence)
- [21. Quote_Lines](#21-quote_lines)
- [22. Alternate_Universe_Alignments](#22-alternate_universe_alignments)
- [23. Role_in_Crossmedia](#23-role_in_crossmedia)
- [24. Sexual_Archetype](#24-sexual_archetype)
- [25. Mental_Sexual_Theme](#25-mental_sexual_theme)
- [26. Visual_Sexual_Theme](#26-visual_sexual_theme)
- [27. Champion_Game_Logic](#27-champion_game_logic)

---

## 27. Champion_Game_Logic

### 27.1. Base_Role

- **Definition**: Strategic role within team compositions.
- **Examples**: Mage, Assassin, Tank, Fighter, Support, Marksman

### 27.2. Sub_Role

- **Definition**: Subclassification within main role.
- **Examples**: Duelist, Artillery, Enchanter, Disruptor

### 27.3. Attack_Type

- **Definition**: Nature of auto-attacks.
- **Values**: Melee, Ranged, Hybrid

### 27.4. Damage_Type

- **Definition**: Primary form of damage dealt.
- **Values**: Physical, Magical, True, Mixed

### 27.5. Resource_Type

- **Definition**: Primary resource mechanic.
- **Values**: Mana, Energy, Health, None, Unique (e.g., Heat, Grit)

### 27.6. Primary_Scaling_Stat

- **Definition**: Main stat that abilities scale with.
- **Examples**: Ability Power, Attack Damage, Max HP

### 27.7. Secondary_Scaling_Stat

- **Definition**: Optional secondary stat influencing certain abilities.
- **Examples**: Bonus Armor, Crit Chance, Missing Health

### 27.8. Gameplay_Ratings

- **Definition**: Normalized values (1–10) describing gameplay profile.
- - **Mobility_Rating**
- - **Crowd_Control_Rating**
- - **Burst_Rating**
- - **Sustain_Rating**
- - **Utility_Rating**
- - **Difficulty_Rating**

### 27.9. Base_Stats

- **Definition**: Champion’s level 1 stats.
- - Base_HP
- - Base_MP
- - Base_Attack_Damage
- - Base_Armor
- - Base_Magic_Resist
- - Base_Attack_Speed
- - Base_Move_Speed

### 27.10. Per_Level_Scaling

- **Definition**: Stat increases per level up.
- - HP_Per_Level
- - MP_Per_Level
- - Attack_Damage_Per_Level
- - Armor_Per_Level
- - Magic_Resist_Per_Level
- - Attack_Speed_Per_Level

### 27.11. Scaling_Notes

- **Definition**: Freeform description of scaling peculiarities.
- **Examples**:
  - “Spikes hard at level 6 and 11”
  - “All damage is % HP-based and ignores traditional stats”

### 27.12. Behavior_Profile

- **Definition**: Summary of play pattern, mastery curve, or AI scripting.
- **Examples**:
  - “Bait-reliant poke mage”
  - “All-in diver with forced initiation”

### 27.13. Kit_Synergy_Tags

- **Definition**: Comma-separated synergy traits.
- **Examples**: Zone Control, Execute, Empower Ally, Blink, Root Chain

### 27.14. Anti_Synergy_Tags

- **Definition**: Design weaknesses or exploitable traits.
- **Examples**: “CC Reliant”, “Immobile”, “Item Dependent”

### 27.15. Design_Flags

- **Definition**: Tags for internal dev lifecycle or meta classification.
- **Values**:
  - Legacy
  - Experimental
  - Rework Candidate
  - Tutorial Unit
  - Balance-Locked
