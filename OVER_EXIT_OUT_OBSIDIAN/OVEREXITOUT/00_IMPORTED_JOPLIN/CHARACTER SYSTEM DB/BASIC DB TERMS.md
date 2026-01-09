---
title: BASIC DB TERMS
updated: 2025-12-03 16:22:14Z
created: 2025-12-03 16:20:47Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---

# Character Database Structure — Key Terminology

## Table-Level Classification

- Each table in the character database should be treated as an **Entity**.
- Entities represent distinct **Domains** of character information (e.g., astrology, physical traits).
- Entities act as major **Categories** or **Modules** within the overall schema.

---

### Rule of Thumb

| Database Concept | Meaning |
|-----------------|---------|
| **Entity (Table)** | A specific domain/category of character data |
| **Attribute (Field/Column)** | A single piece of information within the entity |
| **Relationship** | How entities link together (e.g., Character ↔ Astrology) |

---

### Application Examples

| Entity Name | Domain Purpose |
|------------|----------------|
| Character Astrology | Astrological profile and placement data |
| Physical Sexual Attributes | Anatomy + sexual trait modeling |
| Mental Attributes | Cognitive traits + personality markers |

> **Summary:**  
> Each table = an **Entity Domain** describing a specific slice of the character.



# Titling 

If you want a **clean, scalable naming standard** for your schema, here’s what I recommend:

---

## ✔️ Standardized File/Table Naming Format

```
[DomainCode]_[EntityName]_[Version?]
```

Where:

| Segment                   | Purpose                                          | Example                                                                |
| ------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------- |
| **DomainCode**            | Groups related tables into a high-level category | `CHR` (Character), `AST` (Astrology), `PHY` (Physical), `MEN` (Mental) |
| **EntityName**            | Short, descriptive, specific                     | `SexualAttributes`, `ZodiacProfile`                                    |
| **Version?** *(optional)* | For version tracking if schemas evolve           | `v1`, `v2`                                                             |

---

## Examples From Your Use-Case

| Table Purpose                   | Good Name                 | Why                                   |
| ------------------------------- | ------------------------- | ------------------------------------- |
| Core character details          | `CHR_Core`                | CHR = Character domain, core identity |
| Character astrology             | `AST_Profile`             | All astrology lives under AST         |
| Physical sexual attributes      | `PHY_SexualAttributes`    | PHY = Physical                        |
| Mental/cognitive attributes     | `MEN_CognitiveAttributes` | MEN = Mental                          |
| Inventory or costume sets later | `CHR_Inventory`           | Same domain grouping                  |

---

## Why This Works

* **Alphabetical grouping** keeps tables organized automatically.
* Names stay **short**, **predictable**, and **searchable**.
* Domain codes scale to **hundreds of tables** without chaos.

---

## Suggested Domain Namespace (Starter Set)

| Domain             | Code  | Examples                            |
| ------------------ | ----- | ----------------------------------- |
| Character Identity | `CHR` | CHR_Core, CHR_Backstory             |
| Astrology          | `AST` | AST_Profile, AST_Compatibility      |
| Physical Body      | `PHY` | PHY_SexualAttributes, PHY_BodyType  |
| Mind & Personality | `MEN` | MEN_Personality, MEN_StressResponse |
| Skills/Training    | `SKL` | SKL_Combat, SKL_Hacking             |

Add domains later as needed (e.g., `SOC` for social roles, `MAG` for magic if applicable).

---

## TL;DR Naming Rule

> **Code the category → name the entity → version if needed.**
> Example: `PHY_SexualAttributes_v1`

---

If you'd like, I can:

* Generate your **full naming convention document**
* Build a **starter list** of tables for your entire character system
* Output a **DDL SQL script** so you can load it straight into DBeaver

Just tell me how big you want to go (10 tables? 50? 200?).

