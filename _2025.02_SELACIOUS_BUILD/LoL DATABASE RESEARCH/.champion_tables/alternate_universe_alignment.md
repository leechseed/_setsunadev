```
alternate_universe_alignment {
  au_id integer pk increments unique
  au_label varchar
  champion_id integer > champion.champion_id
  au_role varchar
  allegiance_faction varchar
  au_theme_type varchar
  visual_motifs text
  personality_shift text
  narrative_status_in_au varchar
  canonical_story_links text
  au_continuity varchar
  codex_notes text
}
```

## 📘 Table of Contents

- [1. AU_ID](#1_au_id)
- [2. AU_Label](#2_au_label)
- [3. Champion_ID](#3_champion_id)
- [4. AU_Role](#4_au_role)
- [5. Allegiance / Faction](#5_allegiance__faction)
- [6. AU_Theme_Type](#6_au_theme_type)
- [7. Visual_Motifs](#7_visual_motifs)
- [8. Personality_Shift](#8_personality_shift)
- [9. Narrative_Status_in_AU](#9_narrative_status_in_au)
- [10. Canonical_Story_Links](#10_canonical_story_links)
- [11. AU_Continuity](#11_au_continuity)
- [12. Codex_Notes](#12_codex_notes)

---

# **Narrative Asset Schema: Alternate_Universe_Alignment**

---

## 1. AU_ID

- Unique identifier for the alternate universe or skinline.
- Examples: `star_guardian`, `project`, `high_noon`, `spirit_blossom`

## 2. AU_Label

- Official name of the universe or skinline.
- Examples: Star Guardian, PROJECT, High Noon, Odyssey, Battle Academia

## 3. Champion_ID

- Champion assigned to this AU version.

## 4. AU_Role

- The champion’s narrative or faction role within the AU.
- Examples:
  - Guardian
  - Rebel
  - Enforcer
  - Demon
  - Commander
  - Student
  - Villain
  - Rogue Element
  - Founder / Deity

## 5. Allegiance / Faction

- Specific group or team within the AU (if applicable).
- Examples:
  - Star Guardians (Team Ahri)
  - PROJECT: Resistance
  - High Noon Church of Light
  - Spirit Blossom Festival Spirits

## 6. AU_Theme_Type

- What kind of AU this is:
  - Magical Girl / High Fantasy
  - Cyberpunk / Dystopia
  - Western / Gothic
  - School Life / Slice of Life
  - Cosmic Horror / Eldritch
  - Mythological / Spiritual
  - Military / Sci-fi

## 7. Visual_Motifs

- Summary of visual themes expressed in this AU version.
- Examples: neon armor, robes with cherry blossoms, cybernetic implants, demonic wings

## 8. Personality_Shift

- How the champion’s personality differs from canon.
- Examples:
  - More playful
  - Noble instead of selfish
  - Fully villainous
  - Enlightened / tragic

## 9. Narrative_Status_in_AU

- Role significance in the AU story.
- Values:
  - Central Protagonist
  - Team Member
  - Antagonist
  - Fallen Hero
  - Minor / Flavor Only

## 10. Canonical_Story_Links

- Short stories, cinematics, or comics tied to this AU version.
- Structure:
  - Title
  - Media Type
  - URL / Reference

## 11. AU_Continuity

- Whether the AU version is part of a coherent narrative universe.
- Values:
  - Yes (Connected narrative world)
  - No (One-off concept)
  - Semi-Connected (Loosely linked across skins)

## 12. Codex_Notes

- Commentary on visual design, lore reinterpretation, contradictions, or fan reception.

```

```
