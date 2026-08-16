---
original_path: "/mnt/user-data/outputs/source-synthesis-system-spec.md"
source_conversation: "Advanced literature review of Mating in Captivity"
created: 2026-06-06
trunk: BLACK
kind: generated-file
---

---
title: "Source Synthesis System — Canonical Review + Applied Lens Pipeline"
codename: "(provisional — rename later)"
type: system-spec
version: "0.1"
status: locked-core / open-extensions
domain: [research, synthesis, knowledgebase, writing, personal-development]
tags:
  - canonical-review
  - applied-lens
  - literature-review
  - research-pipeline
  - reusable-framework
created: 2026-06-07
---

# Source Synthesis System
## Canonical Review + Applied Lens Pipeline — Spec v0.1

> A repeatable, two-tier pipeline that turns **any source** into (Tier 1) a publication-grade academic literature review, and optionally (Tier 2) one or more **full standalone rewrites** of that material through named application lenses.

**What's locked (decided):** the two-dial model, the default academic voice, the field-naming convention, the full-rewrite lens behavior, markdown as the default output format.
**What's parked (later):** storage, naming/codename, filing, and cross-linking between reviews and lenses.
**Reserved:** one additional component you've flagged but not yet named — see §5.

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. The Two Dials](#2-the-two-dials)
  - [2.1 Dial A — Register / Voice (default: locked)](#21-dial-a--register--voice-default-locked)
  - [2.2 Dial B — Application Lens (default: none)](#22-dial-b--application-lens-default-none)
- [3. Tier 1 — The Canonical Review](#3-tier-1--the-canonical-review)
  - [3.1 Input](#31-input)
  - [3.2 Process](#32-process)
  - [3.3 Voice spec — naming a primary + secondary fields](#33-voice-spec--naming-a-primary--secondary-fields)
  - [3.4 Standard structure (the repeatable skeleton)](#34-standard-structure-the-repeatable-skeleton)
  - [3.5 Output format](#35-output-format)
- [4. Tier 2 — Applied Lens](#4-tier-2--applied-lens)
  - [4.1 Definition — full rewrite through the lens](#41-definition--full-rewrite-through-the-lens)
  - [4.2 What every lens declares](#42-what-every-lens-declares)
  - [4.3 Lens Library](#43-lens-library)
- [5. Reserved Slot — the additional component](#5-reserved-slot--the-additional-component)
- [6. Invocation — how to trigger it](#6-invocation--how-to-trigger-it)
- [7. Parked / deferred decisions](#7-parked--deferred-decisions)

---

## 1. Overview

The system takes a single **source** (a book, paper, theory, body of work, even a thinker's corpus) and runs it through up to two tiers:

1. **Tier 1 — The Canonical Review.** Deep research plus synthesis, rendered as a publication-grade academic literature review. This is always the first product and the **source of truth** for everything downstream.
2. **Tier 2 — Applied Lens.** An optional, full standalone rewrite of the material through a **named perspective** (e.g., character design, personal relationship). Each lens reuses the canonical scholarship but reorganizes and re-voices it entirely around its own purpose.

The behavior of any run is set by **two independent dials** (§2). The default position of both dials produces a pure Canonical Review.

---

## 2. The Two Dials

These were previously compressed into one idea; they are independent and set separately.

### 2.1 Dial A — Register / Voice (default: locked)

*How* the document is written. **Default, every time, until overridden: publication-grade academic.** Concretely, the writer:

- writes **from inside the field**, as a scholar-participant rather than an outside explainer;
- **self-situates by naming a primary field and its secondary fields** (see §3.3), and positions the source within that primary discipline's own literature and live debates;
- carries the **citation density, hedging, qualification, and rhetorical stance** of a peer-reviewed journal article that would merit publication in the field;
- treats the source as a **contribution to a scholarly conversation**, not as standalone content to be summarized.

This dial is about *voice*, not *purpose*. It stays academic even when Dial B changes — unless explicitly told otherwise.

### 2.2 Dial B — Application Lens (default: none)

*What* the document is for. Default is **none** — pure scholarship (the Canonical Review). When set, it names a lens that triggers a Tier 2 full rewrite (§4). Lenses are reusable and named; the library lives in §4.3.

---

## 3. Tier 1 — The Canonical Review

### 3.1 Input

Any source: a single book (the current default unit), a paper, a defined theory, a thinker's body of work, or a bounded topic. The unit is declared at invocation.

### 3.2 Process

Deep research across the source and its surrounding literature, followed by synthesis. The research step is non-negotiable — the review is grounded in the field's actual scholarship (antecedents, interlocutors, critiques), not in a reading of the source alone.

### 3.3 Voice spec — naming a primary + secondary fields

Per your decision, a multi-disciplinary source is handled by **explicitly naming one primary field and its secondaries**, then writing principally from the primary while drawing on the secondaries as supporting registers. The naming is stated up front in the review so the reader knows the seat the writer is speaking from.

**Worked example — Perel, *Mating in Captivity*:**
- **Primary field:** relational psychoanalysis / contemporary couples therapy.
- **Secondary fields:** clinical sexology; family-systems theory (Bowen/Schnarch differentiation); the sociology of intimacy and modernity.
- **Resulting stance:** "Read primarily as an intervention in relational psychoanalysis, with secondary engagement from clinical sexology, systems theory, and the sociology of intimacy, Perel's argument…" — and the whole review then reasons from that seat.

### 3.4 Standard structure (the repeatable skeleton)

Every Canonical Review follows this skeleton so output is consistent across sources:

1. **Orienting précis / abstract** — what the source argues and why it matters to the field.
2. **Central thesis & argument structure** — the spine of the source's claim.
3. **Theoretical genealogy / lineage** — intellectual antecedents and the tradition it extends.
4. **Concept-by-concept exposition** — the analytical body; each major concept defined precisely, with its lineage and its stakes.
5. **Positioning within the field** — interlocutors, debates, and where the source sits among them.
6. **Original contribution vs. synthesis** — what is genuinely novel vs. repackaged.
7. **Limitations, critiques, contested points** — the honest scholarly reckoning.
8. **References / bibliography** — the field's actual literature.

### 3.5 Output format

**Clean markdown by default.** (Noted: the raw research pass is not a deliverable; the Canonical Review always is.) Default to portable markdown that renders in any reader — frontmatter, ATX headers, tables, plain blockquotes — and only use reader-specific extensions (e.g., callouts, wikilinks) when the target reader is known to support them.

---

## 4. Tier 2 — Applied Lens

### 4.1 Definition — full rewrite through the lens

Per your decision, an Applied Lens is a **complete, standalone rewrite** of the material through a named perspective — **not** an appendix, an inserted section, or a short brief. The lens document:

- stands on its own (a reader needs no prior doc to use it);
- **draws on the Canonical Review's scholarship** as its substrate, but reorganizes, re-sequences, and re-voices everything around the lens's purpose;
- is generated *after* a Canonical Review exists, so the scholarship is settled before it gets repurposed.

The Character Design document you already have is effectively a Tier 2 lens — produced before we'd separated the tiers. Going forward the order is: Canonical Review first, lens rewrites derived from it.

### 4.2 What every lens declares

So lenses stay consistent and pluggable, each one declares five things:

| Field | Meaning |
|-------|---------|
| **Name** | The handle (e.g., `Personal Relationship`). |
| **Purpose** | What the rewrite is for. |
| **Audience / addressee** | Who it speaks to (a writer, you, a clinician, etc.). |
| **Application logic** | *How* the source's concepts get redeployed for this purpose. |
| **Output shape** | The document structure the rewrite produces. |

### 4.3 Lens Library

#### 4.3.1 Lens: Character Design — *status: built*
- **Purpose:** turn the source's concepts into a toolkit for constructing fictional characters and relationships.
- **Audience:** the writer.
- **Application logic:** every concept reframed as a dial or a collision that generates dramatic tension; concepts made into pluggable, nameable modules.
- **Output shape:** concept exposition → module system → worked example → cheat sheet. (Already produced for Perel.)

#### 4.3.2 Lens: Personal Relationship — *spec*
- **Purpose:** apply the source to your own relational life, in service of becoming genuinely compelling and self-possessed (not running tactics).
- **Audience:** you.
- **Application logic:** the source's concepts become **instruments**, deployed across three parts (per your selection):
  1. **Diagnose the dynamics** — read the actual situation through the source's concepts: where the tensions sit, the attachment/differentiation picture, who is sending whom into which loops, the role of any existing partner as the "Third," the current phase, etc.
  2. **Map who to become** — the developmental target the framework itself points toward (for Perel: the differentiated, autonomous, "Radiant Other" self with a center of gravity that doesn't move). This is the growth map, and it is where holding your own footing in a precarious situation lives.
  3. **Suggest how to act** — concrete, on-framework behaviors and moves, framed strictly as *expressions of the developmental target*, never as manipulation. (This framing isn't a moral caveat tacked on — it's the framework's own logic: neediness and tactics read as anti-aphrodisiacs; autonomy and a full self are the actual draw, so the healthy version is also the effective one.)
- **Output shape:** Diagnosis → Developmental Target → Praxis, in academic voice by default.

#### 4.3.3 Lens: Custom — *template*
- **Purpose / Audience / Application logic / Output shape:** declared ad hoc at invocation, using the §4.2 fields. Use this for any `re: whatever` perspective you want on the fly; promote it into the library if it earns repeat use.

---

## 5. Reserved Slot — the additional component

You've flagged one more component as important but haven't named it yet. It is reserved here and will slot into this same two-dial / two-tier structure once defined. Name it when ready and we'll spec it without disturbing the rest.

---

## 6. Invocation — how to trigger it

Plain-language triggers (working grammar, refine later):

- **Tier 1 only:** *"Canonical Review of [source]."* → deep research + academic synthesis, default voice, markdown.
- **Tier 1 + a preset lens:** *"Canonical Review of [source], then Apply Lens: [name]."*
- **Lens on an existing review:** *"Apply Lens: [name] to the [source] review."* → full rewrite using the settled scholarship.
- **Ad-hoc lens:** *"Apply a custom lens to [source] — re: [your angle]."* → I'll ask for the §4.2 fields if they aren't obvious.
- **Override the voice:** state it explicitly (e.g., *"…in plain-language register"*), otherwise academic is assumed.

---

## 7. Parked / deferred decisions

- **Storage & filing** — where reviews and lenses live, how they're organized.
- **Naming / codename** — for the system itself and for individual artifacts.
- **Cross-linking** — how a lens references its parent review, and how reviews interlink in the knowledgebase.
- **Reader target** — whether the KB standardizes on Obsidian-flavored markdown (callouts/wikilinks) or stays portable-plain; affects formatting defaults in §3.5.
