---
title: 🗂️ Worked Example — Atomic Astrology + Overlay Models in Practice
updated: 2025-12-03 18:08:19Z
created: 2025-12-03 18:08:16Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---


# 🗂️ Worked Example — Atomic Astrology + Overlay Models in Practice

---

## 📑 Table of Contents

1. [Example Overview](#1-example-overview)
2. [Step 1 — Define Minimal Schema Slice](#2-step-1--define-minimal-schema-slice)
   - [2.1 Domains](#21-domains)
   - [2.2 Subsystems](#22-subsystems)
   - [2.3 Atomic Variable Definitions](#23-atomic-variable-definitions)
3. [Step 2 — Create Character & Chart](#3-step-2--create-character--chart)
   - [3.1 CHARACTER Row](#31-character-row)
   - [3.2 CHART Row](#32-chart-row)
4. [Step 3 — Define Overlay Models & Dimensions](#4-step-3--define-overlay-models--dimensions)
   - [4.1 OVERLAY_MODEL](#41-overlay_model)
   - [4.2 OVERLAY_MODEL_DIMENSION](#42-overlay_model_dimension)
5. [Step 4 — Attach Profiles to the Character](#5-step-4--attach-profiles-to-the-character)
   - [5.1 OVERLAY_MODEL_PROFILE](#51-overlay_model_profile)
   - [5.2 OVERLAY_MODEL_DIMENSION_VALUE](#52-overlay_model_dimension_value)
6. [Step 5 — Link Atomic Variables to Models](#6-step-5--link-atomic-variables-to-models)
7. [Step 6 — Fill Atomic Values for This Chart](#7-step-6--fill-atomic-values-for-this-chart)
8. [Step 7 — How It All Fits Together (Plain-Language Mental Model)](#8-step-7--how-it-all-fits-together-plain-language-mental-model)
9. [Step 8 — Example Queries / Usage](#9-step-8--example-queries--usage)

---

## 1. Example Overview

We’ll walk through a **tiny, concrete example** using:

- 1 character: **Vivian**
- 1 natal chart
- 2 subsystems: **Sun** (Identity) and **Moon** (Emotional)
- 4 atomic variables:
  - `SUN_IDENTITY_AXIS`
  - `SUN_EGO_STYLE`
  - `MOON_NEED_CORE`
  - `MOON_ATTACHMENT_PATTERN`
- 3 overlay models:
  - **Big Five** (for Sun identity/ego)
  - **Enneagram** (for Sun motivation/theme)
  - **Attachment Style** (for Moon/emotional system)

Think of it like this:

- **Astro tables** = “*Where on the sky? What is the raw setting?*”
- **Overlay tables** = “*What does that *mean* as a psychology template?*”
- **Link table** = “*Which psychology pack explains which astro variable?*”

---

## 2. Step 1 — Define Minimal Schema Slice

### 2.1 Domains

```text
DOMAIN
--------------------------------------------------------
domain_id | domain_code  | name         | description
--------- | ------------ | ------------ | -----------
1         | IDENTITY     | Identity     | Core ego, self-concept, life role
2         | EMOTIONAL    | Emotional    | Feelings, needs, attachment, wounds
````

---

### 2.2 Subsystems

```text
SUBSYSTEM
-----------------------------------------------------------------
subsystem_id | domain_id | subsystem_code | name  | description
------------ | --------- | -------------- | ----- | -----------
1            | 1         | SUN            | Sun   | Core ego & identity
2            | 2         | MOON           | Moon  | Emotional body & needs
```

---

### 2.3 Atomic Variable Definitions

We define 4 variables from your big list:

```text
ATOMIC_VARIABLE_DEF
---------------------------------------------------------------------------------------------------------------------
atomic_var_id | subsystem_id | var_code             | name                | data_type | description
------------- | -----------  | -------------------- | ------------------- | --------- | -----------
1             | 1            | SUN_IDENTITY_AXIS    | Sun Identity Axis   | text      | Core "I am..." statement
2             | 1            | SUN_EGO_STYLE        | Sun Ego Style       | text      | How ego asserts/defends
3             | 2            | MOON_NEED_CORE       | Moon Need Core      | text      | Deep emotional safety need
4             | 2            | MOON_ATTACHMENT_PATTERN | Moon Attachment Pattern | text | How they bond & panic
```

Mental model:

* **DOMAIN** = aisle in the store (Identity aisle, Emotional aisle).
* **SUBSYSTEM** = shelf (Sun shelf, Moon shelf).
* **ATOMIC_VARIABLE_DEF** = specific product slot on the shelf.

---

## 3. Step 2 — Create Character & Chart

### 3.1 CHARACTER Row

```text
CHARACTER
---------------------------------------------------------
character_id | name    | status  | notes
------------ | ------- | ------- | ----------------------
1            | Vivian  | active  | Test character
```

---

### 3.2 CHART Row

```text
CHART
------------------------------------------------------------------------------------------------------
chart_id | character_id | chart_type | datetime_utc         | location        | system    | notes
-------- | ------------ | ---------- | -------------------- | --------------- | --------- | -----
1        | 1            | natal      | 2099-05-14T03:30:00Z | "Mare Tranquil" | Tropical  | Main natal chart
```

Mental model:

* **CHARACTER** = “the person file”.
* **CHART** = “a snapshot of the sky for that person at a moment.”

---

## 4. Step 3 — Define Overlay Models & Dimensions

### 4.1 OVERLAY_MODEL

We register the three models.

```text
OVERLAY_MODEL
-----------------------------------------------------------------------------------------------------------
model_id | domain_id | model_code   | name            | model_type | description
-------- | --------- | -----------  | --------------- | ---------- | -----------
1        | 1         | BIG_FIVE     | Big Five        | trait      | OCEAN personality traits
2        | 1         | ENNEAGRAM    | Enneagram       | typology   | 9 core types + wings
3        | 2         | ATTACHMENT   | Attachment      | typology   | Bonding styles
```

---

### 4.2 OVERLAY_MODEL_DIMENSION

Now the dimensions inside each model.

```text
OVERLAY_MODEL_DIMENSION
--------------------------------------------------------------------------------------------------------------------------
dimension_id | model_id | dimension_code      | name                | data_type | enum_options
------------ | -------- | ------------------- | ------------------- | --------- | -----------
1            | 1        | O                   | Openness            | numeric   | null
2            | 1        | C                   | Conscientiousness   | numeric   | null
3            | 1        | E                   | Extraversion        | numeric   | null
4            | 1        | A                   | Agreeableness       | numeric   | null
5            | 1        | N                   | Neuroticism         | numeric   | null
6            | 2        | TYPE                | Enneagram Type      | text      | ["1","2","3","4","5","6","7","8","9"]
7            | 2        | WING                | Wing                | text      | ["1","2","3","4","5","6","7","8","9"]
8            | 3        | STYLE               | Attachment Style    | text      | ["Secure","Anxious","Avoidant","Disorganized"]
```

Mental model:

* **OVERLAY_MODEL** = “a personality test brand”.
* **OVERLAY_MODEL_DIMENSION** = “the sliders or fields *inside* that test.”

---

## 5. Step 4 — Attach Profiles to the Character

### 5.1 OVERLAY_MODEL_PROFILE

We create Vivian’s profiles for each model.

```text
OVERLAY_MODEL_PROFILE
-------------------------------------------------------------------------------------------------------------------------
profile_id | character_id | chart_id | model_id | profile_label   | notes
---------- | ------------ | -------- | -------- | --------------- | ------------------------------
1          | 1            | 1        | 1        | NATAL_DEFAULT   | Vivian's default Big Five
2          | 1            | 1        | 2        | NATAL_DEFAULT   | Vivian's default Enneagram
3          | 1            | 1        | 3        | NATAL_DEFAULT   | Vivian's default Attachment
```

---

### 5.2 OVERLAY_MODEL_DIMENSION_VALUE

Now we fill in the actual numbers/labels for Vivian.

Let’s say:

* Big Five: high O, moderate C, high E, low A, high N
* Enneagram: type 3 with 4 wing (3w4)
* Attachment: Anxious-Avoidant (we’ll just call it “Anxious” for simplicity)

```text
OVERLAY_MODEL_DIMENSION_VALUE
-----------------------------------------------------------------------------------------------------------------------------
profile_id | dimension_id | value_numeric | value_text   | notes
---------- | ------------ | ------------ | ------------ | ------------------------------
1          | 1            | 80           | null         | High Openness
1          | 2            | 55           | null         | Average Conscientiousness
1          | 3            | 75           | null         | High Extraversion
1          | 4            | 35           | null         | Low Agreeableness
1          | 5            | 85           | null         | High Neuroticism

2          | 6            | null         | "3"          | Enneagram Type 3
2          | 7            | null         | "4"          | Wing 4

3          | 8            | null         | "Anxious"    | Main attachment style
```

Mental model:

* **PROFILE** = her test result sheet.
* **DIMENSION_VALUE** = each line item on that sheet.

---

## 6. Step 5 — Link Atomic Variables to Models

Now we say which overlay models are used to interpret which atomic variables.

```text
ATOMIC_VARIABLE_OVERLAY
--------------------------------------------------------------------------------------------------------------------
atomic_var_id | model_id | role      | weight | notes
------------- | -------- | --------- | ------ | -----------------------------------------------
1             | 1        | PRIMARY   | 0.7    | SUN_IDENTITY_AXIS ← Big Five
1             | 2        | SECONDARY | 0.3    | SUN_IDENTITY_AXIS ← Enneagram
2             | 1        | PRIMARY   | 1.0    | SUN_EGO_STYLE   ← Big Five

3             | 3        | PRIMARY   | 1.0    | MOON_NEED_CORE         ← Attachment
4             | 3        | PRIMARY   | 1.0    | MOON_ATTACHMENT_PATTERN ← Attachment
```

Interpretation:

* `SUN_IDENTITY_AXIS` is driven **70%** by Big Five, **30%** by Enneagram.
* `SUN_EGO_STYLE` fully driven by Big Five.
* Moon variables are driven entirely by Attachment style in this minimal example.

Mental model:

* **ATOMIC_VARIABLE_OVERLAY** = “which test we consult for this trait, and how loud its voice is.”

---

## 7. Step 6 — Fill Atomic Values for This Chart

Now we actually generate the **atomic values** for Vivian’s chart.

### 7.1 ATOMIC_VALUE Rows

We use the overlay data + your narrative logic to write concise values.

```text
ATOMIC_VALUE
------------------------------------------------------------------------------------------------------------------------------------------------
chart_id | atomic_var_id | value_text                                         | value_numeric | notes
-------- | ------------- | -------------------------------------------------- | ------------- | -----------------------------------------------
1        | 1             | "Ambitious, performative disruptor"                | null          | From Big Five + Enneagram 3w4
1        | 2             | "Loud, risk-taking, attention-seeking ego style"  | null          | From high E, low A, high N
1        | 3             | "Needs constant proof they won't be abandoned"    | null          | From Anxious attachment
1        | 4             | "Clingy-then-withdrawing pattern in bonds"        | null          | Attachment style projected into behavior
```

What happened:

* System looked up:

  * Big Five scores (O=80, C=55, E=75, A=35, N=85)
  * Enneagram type 3w4
  * Attachment style = Anxious
* It composed narrative summaries for each atomic variable:

  * `SUN_IDENTITY_AXIS`:

    * High O + high E + high N + Enneagram 3 =
      “Ambitious, performative disruptor obsessed with being seen as exceptional.”

  * `SUN_EGO_STYLE`:

    * High E, low A, high N →
      “Loud, confrontational, sensitive to slights; overcompensates for insecurity.”

  * `MOON_NEED_CORE`:

    * Anxious attachment →
      “Needs reassurance they won’t be rejected or left.”

  * `MOON_ATTACHMENT_PATTERN`:

    * Anxious style →
      “Gets clingy when scared, then lashes out or withdraws when they feel ignored.”

Mental model:

* **ATOMIC_VALUE** = “smoothed, human-readable line” that’s generated from the **raw tests** + **sign/house/aspect logic** you’re running.

---

## 8. Step 7 — How It All Fits Together (Plain-Language Mental Model)

Think of the whole thing as:

### 8.1 Layers

1. **Character**
   → a person file.

2. **Chart**
   → timestamped sky snapshot tied to that person.

3. **Atomic Variables**
   → named sockets like `SUN_IDENTITY_AXIS`, `MOON_NEED_CORE` waiting to be filled.

4. **Overlay Models**
   → psychology packs (Big Five, Enneagram, Attachment) you can plug into those sockets.

5. **Profiles + Dimension Values**
   → the scores/results from those packs for *this* character.

6. **Overlay Links**
   → mapping: *this socket reads from these packs*.

7. **Atomic Values**
   → final, narrative-ready text/values: “ambitious disruptor”, “anxious clinger.”

---

### 8.2 Simple Mental Model: “Soundboard + Filters”

* **Charts** are like the **raw mix** of instruments.
* **Atomic variables** are **individual channels** (vocals, drums, bass).
* **Overlay models** are **effects racks** (EQ, compression, reverb) plugged into each channel.
* The **final fader output** = `ATOMIC_VALUE.value_text`: the sound you actually hear in the track.

You never edit the raw audio directly; you adjust the filters (overlay models) and the channels (atomic vars) update.

---

## 9. Step 8 — Example Queries / Usage

### 9.1 Example: “Show me Vivian’s Core Identity”

> “Explain Vivian’s core identity (Sun) using all connected models.”

**DB Logic (conceptual):**

1. Find `CHARACTER` = Vivian.
2. Find her natal `CHART`.
3. Get `ATOMIC_VALUE` where:

   * `atomic_var_id` = `SUN_IDENTITY_AXIS`, `SUN_EGO_STYLE`.
4. Optionally join through `ATOMIC_VARIABLE_OVERLAY` → `OVERLAY_MODEL` → `OVERLAY_MODEL_DIMENSION_VALUE` if you want to show the underlying trait scores.

**Result (human):**

* **Sun Identity Axis:** Ambitious, performative disruptor.
* **Sun Ego Style:** Loud, risk-taking, attention-sensitive.

You can also surface the underlying trait rows:

* Big Five: O=80, C=55, E=75, A=35, N=85
* Enneagram: Type 3w4

---

### 9.2 Example: “What breaks Vivian in relationships?”

> “Given her Moon and Attachment, where are she most likely to implode emotionally?”

**DB Logic:**

1. Look up `MOON_NEED_CORE` and `MOON_ATTACHMENT_PATTERN` `ATOMIC_VALUE` rows.
2. Optionally join to `OVERLAY_MODEL_DIMENSION_VALUE` where `model_code = ATTACHMENT`.

**Narrative Output:**

* Core need: constant proof she won’t be abandoned.
* Pattern: clings when afraid, then withdraws or attacks when she feels ignored.

**Plot usage:**
Now you know exactly what kind of scenes will reliably melt her down: delayed responses, ambiguous loyalty, perceived de-prioritization.

---

This is the whole point:

* Astro variables define **where to care**.
* Overlay models define **how to shape behavior**.
* The ERD just keeps everything modular so you can scale from this toy example into your full X:1 monstrosity without everything collapsing into spaghetti.

```
```
