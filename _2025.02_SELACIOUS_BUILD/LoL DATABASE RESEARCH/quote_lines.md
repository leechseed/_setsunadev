```
quote_lines {
  quote_id integer pk increments unique
  champion_id integer > champion.champion_id
  quote_text text
  quote_context varchar
  thematic_tags text
  personality_trait_reflected varchar
  tone varchar
  media_source varchar
  is_iconic boolean
  notes text
}
```

## 📘 Table of Contents

- [1. Quote_ID](#1_quote_id)
- [2. Champion_ID](#2_champion_id)
- [3. Quote_Text](#3_quote_text)
- [4. Quote_Context](#4_quote_context)
- [5. Thematic_Tags](#5_thematic_tags)
- [6. Personality_Trait_Reflected](#6_personality_trait_reflected)
- [7. Tone](#7_tone)
- [8. Media_Source](#8_media_source)
- [9. Is_Iconic](#9_is_iconic)
- [10. Notes](#10_notes)

---

# **Narrative Asset Schema: Quote_Lines**

---

## 1. Quote_ID

- Unique identifier for the quote (e.g. `jhin_art_kills`, `lux_light_inside`)

## 2. Champion_ID

- The champion delivering the line.

## 3. Quote_Text

- The actual quote or voice line.

## 4. Quote_Context

- When or why the line is spoken:
  - On Spawn
  - Taunt
  - Ability Use
  - Kill Line
  - Idle Line
  - Lore (from bio or story)
  - Skin-Specific
  - Cinematic Dialogue

## 5. Thematic_Tags

- Keywords that describe the themes or emotions in the quote:
  - Vengeance, Hope, Madness, Honor, Faith, Control, Redemption

## 6. Personality_Trait_Reflected

- The trait expressed through the line:
  - Arrogant, Stoic, Vengeful, Naive, Obsessive, Conflicted

## 7. Tone

- Emotional delivery of the line:
  - Calm, Furious, Playful, Mocking, Melancholy, Exalted, Deadpan

## 8. Media_Source

- Where the line comes from:
  - In-Game
  - Short Story
  - Cinematic
  - Comic
  - Alternate Universe (Skinline)

## 9. Is_Iconic

- Boolean flag for whether the quote is widely recognized or definitive for the champion.
  - Values: `Yes`, `No`

## 10. Notes

- Any extra info: variations, dev notes, fan interpretation, or alternate delivery in skins.
