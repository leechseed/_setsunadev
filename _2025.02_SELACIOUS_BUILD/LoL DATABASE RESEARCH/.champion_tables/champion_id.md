## 📘 Table of Contents

- [1. Champion_ID](#1_champion_id)
- [2. ID_Number](#2_id_number)
- [3. Name](#3_name)
- [4. Title](#4_title)

---

# **Narrative Asset Schema: Champion_ID**

---

## 1. Champion_ID

- **Definition**: Unique slug-based identifier used across all schema references.
- **Format**: Lowercase, underscore-separated string (e.g., `miss_fortune`, `katarina`, `lee_sin`)
- **Purpose**: Serves as the foreign key in all related tables such as Events, Profiles, Media, etc.

---

## 2. ID_Number

- **Definition**: Integer ID assigned to the champion.
- **Type**: Integer (Primary Key for indexing)
- **Usage**: Used for numeric indexing in relational systems or game data exports.

---

## 3. Name

- **Definition**: Canonical full name of the champion as shown in-game and in lore.
- **Type**: Varchar (e.g., `Aphelios`, `Seraphine`)
- **Constraints**: Must be unique across champion entries.

---

## 4. Title

- **Definition**: Narrative or lore-based epithet of the champion.
- **Type**: Text
- **Examples**: `"The Sinister Blade"`, `"The Weapon of the Faithful"`, `"The Curious Chameleon"`