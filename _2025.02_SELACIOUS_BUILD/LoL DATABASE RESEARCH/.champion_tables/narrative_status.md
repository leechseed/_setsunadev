```
narrative_status {
  status_id integer pk increments unique
  status_label varchar
  champion_id integer > champion.champion_id
  lore_update_frequency varchar
  presence_in_canon_events varchar
  current_arc_activity varchar
  media_representation varchar
  narrative_weight integer
  status_change_history text
  notes text
}

```

## 📘 Table of Contents

- [1. Status_ID](#1_status_id)
- [2. Status_Label](#2_status_label)
- [3. Champion_ID](#3_champion_id)
- [4. Lore_Update_Frequency](#4_lore_update_frequency)
- [5. Presence_in_Canon_Events](#5_presence_in_canon_events)
- [6. Current_Arc_Activity](#6_current_arc_activity)
- [7. Media_Representation](#7_media_representation)
- [8. Narrative_Weight](#8_narrative_weight)
- [9. Status_Change_History (Optional)](<#9_status_change_history_(optional)>)
- [10. Notes](#10_notes)

---

# **Narrative Asset Schema: Narrative_Status**

---

## 1. Status_ID

- Unique identifier for the status type.
- Examples: `core_canon`, `supporting`, `retconned`

## 2. Status_Label

- Clear, readable label for the narrative role.
- Examples:
  - Core Canon Character
  - Supporting Character
  - Background / Lore Flavor
  - Event-Limited
  - Retconned / Deprecated
  - Dormant / Inactive

## 3. Champion_ID

- Champion the status applies to.

## 4. Lore_Update_Frequency

- How often Riot updates or expands their story.
- Values:
  - Frequent
  - Occasional
  - Rare
  - Never

## 5. Presence_in_Canon_Events

- Whether the champion plays a role in major lore arcs.
- Values:
  - Major Participant
  - Minor Participant
  - Referenced Only
  - None

## 6. Current_Arc_Activity

- Whether the champion has an active storyline.
- Values:
  - Ongoing Arc
  - Concluded Arc
  - No Arc
  - Unknown

## 7. Media_Representation

- Where they appear outside of in-game content.
- Examples:
  - Arcane
  - Cinematics
  - Comics
  - Short Stories
  - Legends of Runeterra
  - None

## 8. Narrative_Weight

- Importance of the character in the broader lore world.
- Scale:
  - 5 = Lore-Defining
  - 4 = Region-Shaping
  - 3 = Faction-Level Relevance
  - 2 = Background Depth
  - 1 = Cosmetic / AU-Only

## 9. Status_Change_History (Optional)

- Record of any status shifts over time.
- Examples:
  - Moved from Dormant → Core during Arcane
  - Retconned in 2020 visual/lore update

## 10. Notes

- Commentary on contradictions, development comments, or fan expectations.
