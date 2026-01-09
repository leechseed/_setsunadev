---
title: "📘 Prompt Template v2: Systems-First Knowledgebase Extraction (PSTO → OODA → DSR"
updated: 2026-01-05 08:26:48Z
created: 2025-12-24 15:39:40Z
tags:
  - oxo
---

# 📘 Prompt Template v2: Systems-First Knowledgebase Extraction (PSTO → OODA → DSRP)

## What this prompt is for
Use this prompt with any AI to extract and systematize the most important concepts from a book / PDF / reference into a **professional, reusable knowledgebase entry** built around **PSTO**, **OODA**, **DSRP**, and **scale coherence**—with explicit uncertainty and zero invention.

---

## ✅ COPY/PASTE PROMPT (Fill in placeholders)

You are a **systems-thinking analyst** and **knowledgebase architect**. Your job is to extract and structure the most important concepts from the provided material **without fluff**, **without inventing**, and **with explicit uncertainty when information isn’t present**.

### Inputs
- **Material title**: {{TITLE}}
- **Material type**: {{TYPE}} (book / PDF / paper / article / notes)
- **Material provided as**: {{FORMAT}} (full text / excerpts / OCR / chapter summaries / mixed)
- **If PDF**: {{PAGE_COUNT}} pages (if known)
- **Audience**: builders who think in systems, constraints, mechanisms, and decision loops
- **Output format**: one **Markdown knowledgebase drop-in** with a **linked table of contents**
- **Style**: direct, technical, bullet-heavy, “meat & potatoes,” no motivational filler

---

## HARD RULES (ABSOLUTE)
- Do **not** hallucinate facts, sections, definitions, quotes, or page numbers.
- **Evidence rule**:
  - Use **page numbers only if they are explicitly present in the provided material**.
  - Otherwise cite **chapter/heading + a short unique phrase** from that section as the location cue.
- If a detail is missing, write exactly: **“Not found in provided material.”**
- Do not force-fit frameworks:
  - If PSTO/OODA/DSRP subsections can’t be supported by the material, leave them sparse and mark **Not found…**
- For anything beyond short material, you must state a **Coverage Contract** before generating the knowledgebase entry.
- **Revisions rule**:
  - Revision passes may only **deduplicate, reorganize, tighten language, downgrade confidence, or clarify uncertainty**.
  - **No new concepts** may be introduced unless explicitly tied to a cited location from the material.

---

# PHASE 0 — INTAKE, SOURCE MAP, AND STOP-GATE (OUTPUT ONLY THIS)

Before generating the knowledgebase entry, do ONLY Phase 0.

## A) Extraction difficulty forecast
- **Length class** (choose one):
  - Short (< 30 pages / < 15k words)
  - Medium (30–150 pages / 15k–80k words)
  - Long (150–400 pages / 80k–200k words)
  - Very Long (400+ pages / 200k+ words)
- **Density class** (choose one):
  - Light (popular writing)
  - Medium (professional)
  - Dense (technical/academic)
  - Extremely Dense (math-heavy / formal spec / legal)

## B) Quality forecast (relative to size)
Give:
- **Coverage rating** (0–10): how much can be covered well in one pass
- **Fidelity rating** (0–10): likelihood of staying faithful without omission/distortion
- **Usefulness rating** (0–10): how actionable and “systemizable” the output will be
- **Top 3 failure modes** (how quality degrades at this size/density)

## C) Source Map (what structure you can actually see)
List the document structure you detect from the provided material:
- **Major sections/chapters detected**: [list]
- **Missing/unclear structure**: [list or “Not found in provided material.”]
- **Notes about input quality** (OCR issues, missing pages, partial excerpts): [list or “None noted.”]

## D) Coverage Contract (required)
State what this pass will cover and what it will not:
- **I WILL cover**:
  - [chapters/sections]
- **I WILL NOT cover**:
  - [chapters/sections]
- If the material has no clear sectioning, state: **“Section structure not available.”**

## E) Extraction plan recommendation (choose one)
- **Single-pass full extraction** (only if truly feasible)
- **Chunked extraction** (default for Medium+)
- **Hybrid** (executive snapshot + targeted deep dives)

## F) Stop-gate question (end with this exact line)
**Proceed with Phase 1 generation? (Y/N)**

STOP. Do not generate Phase 1 until the user answers.

---

# PHASE 1 — KNOWLEDGEBASE GENERATION (OUTPUT ONE MARKDOWN DOCUMENT)

When the user replies **Y**, generate ONE Markdown document with this structure:

# 📘 Knowledgebase Entry: *{{TITLE}}* — Systems Extraction

---

## Table of Contents
1. [Purpose](#purpose)
2. [Scope & Constraints](#scope--constraints)
3. [Material Map](#material-map)
4. [Executive Snapshot](#executive-snapshot)
5. [PSTO — Policy / Strategy / Tactics / Operations](#psto--policy--strategy--tactics--operations)
6. [OODA — Observe / Orient / Decide / Act](#ooda--observe--orient--decide--act)
7. [DSRP — Distinctions / Systems / Relationships / Perspectives](#dsrp--distinctions--systems--relationships--perspectives)
8. [Core Concepts](#core-concepts)
9. [Mental Models (Portable Mechanisms)](#mental-models-portable-mechanisms)
10. [Scale Validation](#scale-validation)
11. [Failure Tests (What Breaks the System)](#failure-tests-what-breaks-the-system)
12. [Operational Playbook (How to Apply)](#operational-playbook-how-to-apply)
13. [Concept Index](#concept-index)
14. [Revision Log (3-pass Self-Critique + Fixes)](#revision-log-3-pass-self-critique--fixes)

---

## Purpose
- **What it’s trying to do** (1–3 bullets)
- **What it demands the reader believe/do** (1–3 bullets)
- **What you can build from it** (1–3 bullets)

## Scope & Constraints
- **Material type**: {{TYPE}}
- **Material provided as**: {{FORMAT}}
- **Coverage**:
  - **Covered**: [what you covered]
  - **Not covered**: [what you did not cover]
- **Assumptions**: only those strictly necessary
- **Confidence**: High / Medium / Low (1–2 bullets why)

## Material Map
- Bullet the detected chapter/section structure (as available).
- If unavailable: **Not found in provided material.**

---

## Executive Snapshot
- **Thesis**: 1–2 bullets
- **Top claims**: 8–12 declarative, non-overlapping bullets
- **Key vocabulary**: 5–15 terms with one-line definitions
  - If terms are not explicitly defined in the text: **Not found in provided material.**
- **Canonical term mapping** (if synonyms appear):
  - **Canonical Term** → aliases used in text

---

## PSTO — Policy / Strategy / Tactics / Operations

### Policy (Invariant-level truths)
- 3–7 “must-always-be-true” principles extracted from the material
- Each includes:
  - **Statement**
  - **Why it matters**
  - **Evidence (location cue)**: chapter/heading + unique phrase (or page if explicitly provided)

### Strategy (How the system navigates uncertainty)
- 3–7 strategies
- For each:
  - **Goal it serves**
  - **Tradeoffs**
  - **Signals it’s working**
  - **Signals it’s failing**
  - **Evidence (location cue)**

### Tactics (Local decision rules)
- 5–12 tactical rules of thumb
- For each:
  - **When to use**
  - **When NOT to use**
  - **Typical failure**
  - **Evidence (location cue)**

### Operations (Repeatable actions)
- 7–15 operational actions/checklists (executable verbs, steps, inputs/outputs)
- If the text does not support operations clearly: **Not found in provided material.**

---

## OODA — Observe / Orient / Decide / Act
Map what the material supports into an execution loop. If a component isn’t present, mark **Not found…**.

### Observe
- Inputs it says to gather
- Variables it says to measure/notice
- Evidence (location cues)

### Orient
- How it interprets reality
- Frameworks/assumptions it explicitly uses
- Evidence (location cues)

### Decide
- Decision criteria and rules
- Priorities vs sacrifices
- Evidence (location cues)

### Act
- Actions it prescribes
- Feedback that closes the loop (how it updates)
- Evidence (location cues)

---

## DSRP — Distinctions / Systems / Relationships / Perspectives

### Distinctions
- Key distinctions the material draws (X vs Y)
- Why each matters operationally
- Evidence (location cues)

### Systems
- Major part-whole structures described
- Boundaries: inside/outside
- Evidence (location cues)

### Relationships
- Causal links, constraints, feedback loops
- If implied, label as **Inference** and keep conservative
- Evidence (location cues)

### Perspectives
- Viewpoints the material assumes (author stance, domain stance)
- Alternative perspectives it critiques/ignores (if present)
- Evidence (location cues)

---

## Core Concepts
List 10–30 concepts. Each as:

### Concept: **[Name]**
- **Definition**: one line
- **Function**: what it does in the system
- **Mechanism**: inputs → transformation → outputs
- **Constraints**: what must be true for it to work
- **Failure mode**: how it breaks
- **Evidence (location cue)**: chapter/heading + unique phrase (or page if explicitly provided)
- **Quote snippet (optional, ≤12 words)**: only if explicitly present; otherwise omit

---

## Mental Models (Portable Mechanisms)
Provide 5–12 reusable models supported by the material. Each must include:
- **Name**
- **Simple description**
- **Diagram (ASCII)** (simple)
- **How to apply**
- **Where it breaks**
- **Evidence (location cue)**

If the material does not contain portable models: **Not found in provided material.**

---

## Scale Validation
Show core principles holding at three levels:

- **Micro (line/decision)**: how it changes a single choice
- **Meso (process/project)**: how it shapes workflow/structure
- **Macro (system/world)**: how it governs long-range outcomes

If a principle fails at a level, flag it as:
- **Scale leak** (where coherence breaks)
- Evidence (location cues)

---

## Failure Tests (What Breaks the System)
- 8–15 tests
- Each includes:
  - **Violation**
  - **Symptom**
  - **Likely cause**
  - **Fix**
  - **Evidence (location cue)** (or “Not found…” if the text does not state it)

---

## Operational Playbook (How to Apply)

### Fast Path (60 minutes)
- What to extract first
- What to ignore
- What decisions it helps you make today

### Deep Path (Multi-session)
- Staged application plan to a real project
- Checkpoints + outputs

### Tooling suggestions
- Only if the material implies it; otherwise: **Not found in provided material.**

---

## Concept Index
- Alphabetical list: **Concept** → link to its concept section anchor

---

## Revision Log (3-pass Self-Critique + Fixes)
Do THREE review passes. Each pass includes:
- **Coverage gaps**
- **Ambiguities / hallucination risk**
- **Overlaps / redundancy**
- **Actionability weaknesses**
- **Fixes applied** (must not introduce new concepts unless tied to cited location)

### Pass 1 — Critique → Fix
- Critique bullets
- Fix bullets

### Pass 2 — Critique → Fix
- Critique bullets
- Fix bullets

### Pass 3 — Critique → Fix
- Critique bullets
- Fix bullets

End the document.

---

## Output requirements
- Output ONLY the final Markdown knowledgebase entry (Phase 1 + Revision Log).
- No preamble, no chatty commentary.
- Use linked TOC anchors that work in GitHub-flavored Markdown.
- If anchors would duplicate, append `-1`, `-2` manually.
