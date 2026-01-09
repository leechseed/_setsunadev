---
title: 📘 Naming Schema Standard — BAS / VAR / SIM System
updated: 2025-12-03 16:33:55Z
created: 2025-12-03 16:31:21Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---


# 📘 Naming Schema Standard — BAS / VAR / SIM System

This document defines the standardized naming convention used for all database tables across the worldbuilding system. The goal is to ensure scalability, clarity, and immediate recognition of data purpose.

---

## 1️⃣ Status Layer — Data Mutability Code

Indicates whether table data is **canonical**, **changing**, or **runtime**.

| Code | Meaning | Description |
|------|---------|-------------|
| **BAS** | Baseline | Immutable, canonical data defined by the creator. Never modified by scripts or mechanics. Source-of-truth attributes. |
| **VAR** | Variable | Data that evolves permanently through progression, decisions, or narrative events. |
| **MOD** | Modifier | Temporary effects or adjustments (buffs, conditions, temporary states). |
| **SIM** | Simulation | Real-time, runtime, or computational states — not saved long-term. |

> **Summary:**  
> BAS = who/what the entity **is**  
> VAR/MOD/SIM = who/what the entity **becomes**

---

## 2️⃣ Entity Domain Layer — What Type of Thing the Data Describes

Short 3-letter codes define the **category of entity**:

| Domain | Code | Examples |
|--------|------|----------|
| Characters | **CHR** | Physical profile, astrology, mental traits |
| Factions / Organizations | **FAC** | Doctrine, hierarchies, influence |
| Buildings / Architecture | **BLD** | Blueprints, structural classifications |
| Social Groups / Cultures | **SOC** | Customs, rules, class systems |
| Technology / Gear | **TEC** | Prototypes, constraints, base stats |

> Each domain can scale independently without naming collisions.

---

## 3️⃣ Table Name Layer — Specific Data Focus

A clear noun phrase that states **what the table contains**:

| Examples |
|---------|
| `Astrology` |
| `SexualAttributes` |
| `MentalProfile` |
| `Doctrine` |
| `Blueprint` |

---

## 4️⃣ Final Naming Format

```

[Status]*[Domain]*[TableName]

```

---

### ✔ Examples

#### Character Domain

| Table | Code |
|-------|------|
| Baseline astrology | `BAS_CHR_Astrology` |
| Fixed physical/sexual anatomy | `BAS_CHR_SexualAttributes` |
| Fixed mental attributes | `BAS_CHR_MentalProfile` |

#### Faction Domain

| Table | Code |
|-------|------|
| Canon doctrine | `BAS_FAC_Doctrine` |
| Evolving influence | `VAR_FAC_InfluenceLevel` |

#### Architecture Domain

| Table | Code |
|-------|------|
| Canon building blueprint | `BAS_BLD_Blueprint` |
| Damage states over time | `VAR_BLD_DamageState` |

---

## 5️⃣ Why This System Works

- **Scales endlessly** across all worldbuilding systems
- **Readable** by humans and sortable for SQL engines
- Automatically organizes entities by:
  - Mutability
  - Domain
  - Specific purpose

> Logical and future-proof: no renaming required as systems expand.

---

### TL;DR

| Layer | You Use It To Define |
|------|---------------------|
| **BAS** | Immutable truth |
| **VAR / MOD / SIM** | Change over time |
| **CHR / FAC / BLD / SOC / TEC** | What is being described |
| **TableName** | Exact purpose of the data |

**Naming Pattern**

```

BAS_CHR_Astrology
VAR_FAC_InfluenceLevel
SIM_BLD_Occupancy

```

---

| DomainCode | TableName        | FullTableCode            | FieldName   | DataType    | Description                 | PK? | FK Reference                    |
| ---------- | ---------------- | ------------------------ | ----------- | ----------- | --------------------------- | --- | ------------------------------- |
| BAS_CHR    | CoreProfile      | BAS_CHR_CoreProfile      | CharacterID | INT         | Unique character identifier | Yes | —                               |
| BAS_CHR    | CoreProfile      | BAS_CHR_CoreProfile      | FullName    | VARCHAR(60) | Canonical name              | No  | —                               |
| BAS_CHR    | Astrology        | BAS_CHR_Astrology        | SunSign     | VARCHAR(20) | Western zodiac sun sign     | No  | BAS_CHR_CoreProfile.CharacterID |
| BAS_CHR    | SexualAttributes | BAS_CHR_SexualAttributes | GenitalType | VARCHAR(20) | Canonical primary sex organ | No  | BAS_CHR_CoreProfile.CharacterID |

---

A **Field Name** is the name of a **single piece of data** stored in a database table.

In simpler terms:

> **Field = Column**

Each field describes **one attribute** of the thing the table represents.

---

### Example

Table: `BAS_CHR_CoreProfile`

| Field Name  | Value Example |
| ----------- | ------------- |
| CharacterID | 0012          |
| FullName    | “Vivian Rao”  |
| BirthDate   | “2103-02-11”  |
| Species     | “Human”       |

Here:

* `FullName` is a **field**
* It’s a **column** in the table
* It holds **one type of information**

---

### Real-world analogy

Think of an Excel spreadsheet:

| Columns (top) | = Fields |
| Rows (side) | = Records / Entries |

So a spreadsheet with:

| Name | Height | Weight |
| ---- | ------ | ------ |

These are **field names**:

* Name
* Height
* Weight

Each person (row) fills in those fields.

---

### DB Vocabulary Cheat Sheet

| Spreadsheet Term | Database Term     |
| ---------------- | ----------------- |
| Workbook         | Database          |
| Sheet            | Table (Entity)    |
| Column           | Field (Attribute) |
| Row              | Record            |

---

### Quick Rule

> A **field** defines *what* you store.
> A **record** stores *the actual data*.

---

If you'd like, I can generate a list of recommended **field names** for the first baseline character tables (Astrology, Sexual, Mental) to make things easier and reduce decision fatigue.
