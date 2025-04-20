```
crossmedia {
  crossmedia_id integer pk increments unique
  champion_id integer > champion.champion_id
  media_title varchar
  media_type varchar
  role_in_media varchar
  canonical_weight varchar
  narrative_arc_presence varchar
  portrayal_consistency varchar
  actor_or_voice_performer varchar
  visual_design_changes text
  audience_reception_notes text
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Crossmedia_ID](#1_crossmedia_id)
- [2. Champion_ID](#2_champion_id)
- [3. Media_Title](#3_media_title)
- [4. Media_Type](#4_media_type)
- [5. Role_in_Media](#5_role_in_media)
- [6. Canonical_Weight](#6_canonical_weight)
- [7. Narrative_Arc_Presence](#7_narrative_arc_presence)
- [8. Portrayal_Consistency](#8_portrayal_consistency)
- [9. Actor_or_Voice_Performer](#9_actor_or_voice_performer)
- [10. Visual_Design_Changes](#10_visual_design_changes)
- [11. Audience_Reception_Notes](#11_audience_reception_notes)
- [12. Codex_Notes](#12_codex_notes)

---

# **Narrative Asset Schema: Role_in_Crossmedia**

---

## 1. Crossmedia_ID

- Unique identifier (slug or numeric) for the crossmedia entry.
- Examples: `arcane_s1_vi`, `ruination_novel_thresh`, `lor_card_yasuo`

## 2. Champion_ID

- The champion appearing in the media.

## 3. Media_Title

- Official title of the media.
- Examples: Arcane, Ruination, Shadow and Fortune, Kin of the Stag, Legends of Runeterra

## 4. Media_Type

- Type of media.
- Values:
  - Animated Series
  - Cinematic
  - Short Story
  - Comic
  - Novel
  - Digital Card Game
  - Artbook / Concept Feature

## 5. Role_in_Media

- The narrative function the champion serves.
- Values:
  - Main Character
  - Supporting Character
  - Antagonist
  - Flashback Subject
  - Silent Cameo
  - Visual Only (card, background art, etc.)

## 6. Canonical_Weight

- How “official” the media is considered within the main Runeterra continuity.
- Values:
  - Core Canon
  - Semi-Canon
  - Alternate Universe
  - Promotional / Stylized Non-Canon

## 7. Narrative_Arc_Presence

- Whether the champion experiences or drives a story arc.
- Values:
  - Full Arc
  - Subplot
  - Backstory Only
  - No Arc / Static

## 8. Portrayal_Consistency

- Does the characterization align with main-lore identity?
- Values:
  - Consistent
  - Alternate Interpretation
  - Inverted / Subverted
  - Unknown

## 9. Actor_or_Voice_Performer

- If applicable, name of actor or voice actor associated with portrayal.

## 10. Visual_Design_Changes

- Notable differences in appearance, costume, or age compared to in-game model.
- Examples:
  - Arcane Vi has a younger, more rugged streetfighter design.
  - LoR Yasuo features older, mentor-like artwork.

## 11. Audience_Reception_Notes

- Summary of how fans received the champion’s portrayal in this medium.
- Examples:
  - Widely acclaimed
  - Controversial redesign
  - Boosted popularity
  - Lore conflict concerns

## 12. Codex_Notes

- Any developer commentary, behind-the-scenes trivia, or cross-canon clarifications.
