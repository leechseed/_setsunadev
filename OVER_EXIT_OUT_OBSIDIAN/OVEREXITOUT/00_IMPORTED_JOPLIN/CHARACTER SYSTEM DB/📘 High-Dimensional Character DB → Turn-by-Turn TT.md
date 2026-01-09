---
title: 📘 High-Dimensional Character DB → Turn-by-Turn TTRPG / CRPG Mechanics
updated: 2025-12-03 17:42:09Z
created: 2025-12-03 17:42:08Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---

# 📘 High-Dimensional Character DB → Turn-by-Turn TTRPG / CRPG Mechanics

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Core Idea: Lore Space → Turn Space](#core-idea-lore-space--turn-space)
3. [How TTRPGs/CRPGs Typically Do It](#how-ttrpgscrpgs-typically-do-it)
   - [3.1 Core Resolution Engines](#31-core-resolution-engines)
   - [3.2 Small Set of Mechanical Axes](#32-small-set-of-mechanical-axes)
   - [3.3 Generic Turn Formula](#33-generic-turn-formula)
   - [3.4 Where “Depth” Actually Comes From](#34-where-depth-actually-comes-from)
4. [Compilation Pipeline: DB → Single-Turn Modifiers](#compilation-pipeline-db--single-turn-modifiers)
   - [4.1 Step 1 — Pick the Resolution Engine](#41-step-1--pick-the-resolution-engine)
   - [4.2 Step 2 — Compress DB into 6–8 Axes](#42-step-2--compress-db-into-68-axes)
   - [4.3 Step 3 — Build an Influence Matrix](#43-step-3--build-an-influence-matrix)
   - [4.4 Step 4 — Action → Tags → Modifiers](#44-step-4--action--tags--modifiers)
   - [4.5 Step 5 — What “Deep & Unique” Actually Means](#45-step-5--what-deep--unique-actually-means)
5. [Typical Math Patterns to Steal](#typical-math-patterns-to-steal)
6. [Mental Model: Compiler Between Lore Space and Turn Space](#mental-model-compiler-between-lore-space-and-turn-space)
7. [Concrete Examples](#concrete-examples)
   - [7.1 Example 1 — Big Five & Enneagram in a Persuasion Roll](#71-example-1--big-five--enneagram-in-a-persuasion-roll)
   - [7.2 Example 2 — Erotic Blueprint Affecting Combat](#72-example-2--erotic-blueprint-affecting-combat)
   - [7.3 Example 3 — Relationship Overlay Affecting Team Actions](#73-example-3--relationship-overlay-affecting-team-actions)
8. [Implementation Notes & Data Structure Hints](#implementation-notes--data-structure-hints)
9. [Summary](#summary)

---

## 1. Overview

You have a **high-dimensional character database**: atomic astrology, psych models, erotic blueprints, trauma schemas, etc.

At the table or in a CRPG, all of that has to compress into something like:

> `Roll [base dice] + [a few modifiers] vs [difficulty]`

This entry explains how to:

- Collapse your **insane high-D character model** into a **small mechanical profile**.
- Wire that profile into **single-turn actions** with **clear, repeatable math**.
- Preserve **depth and uniqueness** via **tags and conditional modifiers**, not massive equations.

---

## 2. Core Idea: Lore Space → Turn Space

Think in two layers:

- **Lore Space (high-dimensional)**  
  All your DB fields:
  - OCEAN (Big Five)
  - Enneagram type
  - Attachment style, Polyvagal mode
  - Erotic blueprint, Love language
  - Shadow patterns, Schemas, Nodes, etc.

- **Turn Space (low-dimensional)**  
  What actually matters on a given roll:
  - A **small set of stats** (axes like PROWESS, MOJO, NERVES…)
  - A **skill rank**
  - A **handful of conditional modifiers** that are true right now
  - The **target number / defense**

The missing piece is a **compiler**:

> A mapping layer that projects Lore Space → Turn Space.

Everything in this doc is basically:  
**“How do I design that compiler?”**

---

## 3. How TTRPGs/CRPGs Typically Do It

### 3.1 Core Resolution Engines

Most systems pick one of a few standard engines:

- **d20 + modifiers vs TN** (D&D, 5e-style, d20 clones)
- **2d6 + modifiers vs TN** (PbtA-style)
- **Dice pool vs successes** (Storyteller, Blades variants)
- **Percentile vs skill** (BRP, Call of Cthulhu)

You **must** pick one.  
All math design lives downstream of this choice.

---

### 3.2 Small Set of Mechanical Axes

Deep games do **NOT** expose all psychology directly. They boil it down to:

- **3–8 core stats** (e.g., STR/DEX/INT or Fight/Talk/Think/Weird).
- **5–20 skills**.
- A library of **binary/tiered flags**:
  - Traits, feats, perks, tags, conditions.

Your astro-psych garbage fire is **source data**.  
The sheet only shows a **small projected subset**.

---

### 3.3 Generic Turn Formula

On a single turn, for a single action:

```text
Roll = Base Dice
     + Ability Modifier (axis)
     + Skill Rank
     + Temporary Modifiers (position, tools, buffs, debuffs)
     + Trait/Feature Modifiers (if conditions met)
