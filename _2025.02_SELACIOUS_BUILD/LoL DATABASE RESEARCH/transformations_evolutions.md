```
transformations_or_evolutions {
  transformation_id integer pk increments unique
  champion_id integer > champion.champion_id
  transformation_label varchar
  transformation_type varchar
  trigger_event text
  from_state varchar
  to_state varchar
  is_reversible varchar
  transformation_status varchar
  transformation_arc_t text
}
```

## 📘 Table of Contents

- [1. Transformation_ID](#1_transformation_id)
- [2. Champion_ID](#2_champion_id)
- [3. Transformation_Label](#3_transformation_label)
- [4. Transformation_Type](#4_transformation_type)
- [5. Trigger_Event](#5_trigger_event)
- [6. From_State](#6_from_state)
- [7. To_State](#7_to_state)
- [8. Is_Reversible](#8_is_reversible)
- [9. Transformation_Status](#9_transformation_status)
- [10. Transformation_Arc_T](#10_transformation_arc_t)

---

# **Narrative Asset Schema: Transformations_or_Evolutions**

---

## 1. Transformation_ID

- **Definition**: Unique identifier (slug or numeric) for the transformation instance.
- **Examples**: `kayn_darkin_possession`, `nasus_ascension`, `viego_ruination`

---

## 2. Champion_ID

- **Definition**: Champion who undergoes the transformation.
- **Examples**: `kayn`, `nasus`, `viego`

---

## 3. Transformation_Label

- **Definition**: Short name or phrase describing the transformation.
- **Examples**: Darkin Possession, Ascension, Ruination, Spiritual Binding

---

## 4. Transformation_Type

- **Definition**: Structural type of transformation.
- **Values**:
  - Physical / Biological
  - Magical / Supernatural
  - Ideological / Moral
  - Metaphysical / Existential
  - Psychological / Emotional
  - Multi-layered / Mythic

---

## 5. Trigger_Event

- **Definition**: Catalyst or cause of the transformation.
- **Examples**:
  - Exposure to Void
  - Betrayal by a loved one
  - Ancient ritual
  - Death and resurrection
  - Prolonged trauma
  - Acceptance of forbidden power

---

## 6. From_State

- **Definition**: Origin state before transformation.
- **Examples**:
  - Human
  - Mortal Warrior
  - Noble Protector
  - Apprentice

---

## 7. To_State

- **Definition**: Resultant form or identity after transformation.
- **Examples**:
  - Darkin Host
  - Ascended Being
  - Undead King
  - Demonic Entity
  - Enlightened Avatar

---

## 8. Is_Reversible

- **Definition**: Whether the transformation can be reversed or undone.
- **Values**:
  - Yes
  - No
  - Partially
  - Unknown

---

## 9. Transformation_Status

- **Definition**: Current state of transformation in canonical timeline.
- **Values**:
  - Active
  - Reversed
  - In Progress
  - Incomplete / Fragmented
  - Hypothetical / Prophesied

---

## 10. Transformation_Arc_T
