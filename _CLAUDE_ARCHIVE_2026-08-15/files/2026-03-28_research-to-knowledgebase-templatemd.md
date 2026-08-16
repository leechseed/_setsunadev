---
original_path: "/mnt/user-data/outputs/RESEARCH_TO_KNOWLEDGEBASE_TEMPLATE.md"
source_conversation: "Top seduction and day game books from online communities"
created: 2026-03-28
trunk: BOTH
kind: generated-file
---

# Community-Sourced Research → Knowledgebase Synthesis
## Reusable Prompt Template for Claude / Agentic AI

**Template Version:** 1.0
**Template Type:** Research + Synthesis Pipeline
**Designed For:** Claude Projects · Agentic AI Instructions · System Prompt Injection
**Author:** Bold Venture X

---

## HOW TO USE THIS TEMPLATE

This is a two-stage pipeline template. Copy and fill in the `[BRACKETED FIELDS]` for your topic. The two stages can be run in sequence in the same conversation, or as separate agent tasks.

- **Stage 1** produces the annotated book/resource list (the raw research report)
- **Stage 2** takes that report and synthesizes it into a structured knowledgebase module

Both stages can be chained as a single agentic task with the combined prompt at the bottom of this document.

---

## ─────────────────────────────────────────────
## STAGE 1 — COMMUNITY-SOURCED RESEARCH PROMPT
## ─────────────────────────────────────────────

### What this stage does
Researches a topic across specific internet communities and returns a ranked, annotated list of the most recommended books/resources, with community-sourced tier ratings and substantive descriptions of each.

---

### STAGE 1 PROMPT (copy and customize)

```
You are a research agent. Your task is to compile a report of the top [NUMBER — e.g. 10] most recommended [RESOURCE TYPE — e.g. books / courses / frameworks / tools] on the topic of [TOPIC] as cited and discussed across the following communities and sources:

PRIMARY COMMUNITIES TO SOURCE FROM:
[LIST YOUR COMMUNITIES — e.g.]
- Reddit: r/[subreddit1], r/[subreddit2], r/[subreddit3]
- Forums: [Forum name 1], [Forum name 2]
- Aggregators: [e.g. Goodreads shelves, community polls, wiki sidebars, sticky posts]
- Curated lists: [e.g. specific blogs, reading lists, coach recommendations]

TOPIC FOCUS — the resources must specifically cover:
[LIST THE SUB-TOPICS YOU CARE ABOUT — e.g.]
- [Sub-topic 1]
- [Sub-topic 2]
- [Sub-topic 3]
- [Sub-topic 4]

FOR EACH RESOURCE, PROVIDE:
1. Title
2. Author / Creator
3. Core thesis — what is the central argument or framework?
4. Key concepts or techniques covered
5. Who it is best for (beginner / intermediate / advanced, and what type of reader)
6. Why the community recommends it — what problem does it solve for people?
7. Community tier rating — based on frequency of recommendation and consensus strength:
   - S-Tier: Unanimous, appears on every list
   - A-Tier: Widely recommended, consistent across communities
   - B-Tier: Recommended in specific contexts or by a subset of the community
   - C-Tier: Niche, polarizing, or historically significant but dated
8. Any major criticisms or caveats the community raises about it

OUTPUT FORMAT:
- Ranked list from most to least recommended (by cross-community frequency)
- Substantive descriptions (not summaries — actual analysis of the content and its application)
- Conclude with: a section on honorable mentions that nearly made the list, and a meta-analysis of what the community consensus reveals about how the field has evolved

SOURCE REQUIREMENT:
Draw from actual community discussions, forum threads, wiki sidebars, sticky posts, poll results, and recommended reading lists — not generic bestseller aggregators. Prioritize sources that reflect genuine user experience with the material.
```

---

### STAGE 1 OUTPUT STRUCTURE (what to expect)

The agent will return:

```
# [Topic] — Top [N] Community-Recommended [Resources]

## Introduction
[Meta-context: what communities were sourced, what the consensus reveals]

## 1. [Title] by [Author] — [community nickname/descriptor]
[Tier badge]
[Core thesis paragraph]
[Key concepts]
[Best for]
[Community criticism / caveats]

## 2. [Title] by [Author]...
[continues for all N resources]

## Honorable Mentions
[Resources that nearly made the list]

## Meta-Analysis: What the Consensus Reveals
[How the field has evolved / what the pattern of recommendations tells you]
```

---

## ─────────────────────────────────────────────
## STAGE 2 — KNOWLEDGEBASE SYNTHESIS PROMPT
## ─────────────────────────────────────────────

### What this stage does
Takes the Stage 1 research output and synthesizes it into a unified, structured knowledgebase module — a single operating document that distills the consensus across all resources into a practical framework with architecture, vocabulary, failure patterns, development progression, and source mapping.

---

### STAGE 2 PROMPT (copy and customize)

```
You are a knowledge architect. Using the research report provided [paste Stage 1 output here, or reference it if in the same conversation], synthesize all [N] resources into a single unified knowledgebase module on the topic of [TOPIC].

This document will be filed under [PARENT CATEGORY — e.g. "Male Character Architecture / Seduction"] as a personal operating reference.

DOCUMENT REQUIREMENTS:

1. TITLE AND METADATA HEADER
   - Module name, parent category, status, source note, date

2. TABLE OF CONTENTS
   - Full TOC with section numbers and anchor-ready headings

3. CORE THESIS — ONE SENTENCE
   - Distill the entire topic into a single foundational claim

4. LAYERED ARCHITECTURE
   - Organize the material into [2-4] hierarchical layers from foundational to expressive
   - Each layer should build on the previous
   - Visualize the architecture as an ASCII diagram or table
   - Label each layer with what it contains

5. ONE SECTION PER LAYER (detailed breakdown)
   For each layer, provide:
   - The key principles / beliefs that constitute this layer
   - How to build or develop this layer practically
   - What failure looks like at this layer
   - Subsections for each major concept within the layer

6. DOMAIN-SPECIFIC APPLICATION SECTIONS
   - [CONTEXT 1 — e.g. Day Game / Cold Approach]
   - [CONTEXT 2 — e.g. Social / Workplace environments]
   - [CONTEXT 3 — e.g. any other specific environment relevant to the topic]
   Each should include: what changes in this context, the specific protocol/sequence, dos and don'ts

7. TYPOLOGY / ARCHETYPE SECTION
   - If the source material identifies different types, styles, or categories (of practitioners, of targets, of approaches), present them in a reference table

8. FAILURE PATTERNS — ANTI-BEHAVIORS
   - A table of the most common mistakes, what they signal, and why they produce failure
   - Pull from across all source material

9. DEVELOPMENT PROGRESSION
   - A staged sequence from beginner to advanced
   - Each stage: what to prioritize, what to read/do, measurable milestone metric

10. CORE VOCABULARY REFERENCE
    - A glossary table of field-specific terminology
    - Term | Definition format

11. [N] IRON RULES — QUICK REFERENCE
    - Distilled from consensus across all sources
    - The non-negotiable principles of the discipline

12. SOURCE MAP
    - A table mapping specific needs/use cases to the primary and secondary source book for that need
    - Format: Need | Primary Source | Secondary Source

OUTPUT REQUIREMENTS:
- Format as a knowledgebase-style markdown document (not a report or essay)
- Use headers, subheaders, tables, and ASCII diagrams for visual clarity
- Every section should be practical, not theoretical — written for someone who will use this as an operating reference
- Maintain a consistent tone: direct, non-moralistic, informative
- Do NOT include caveats, disclaimers, or hedging language — this is a reference document, not a persuasive essay
- Length: comprehensive. Do not truncate. This is a reference document, not a summary.
```

---

### STAGE 2 OUTPUT STRUCTURE (what to expect)

```
# [TOPIC] — The Complete Framework
### A Personal Knowledgebase Module for [PARENT CATEGORY]

[Metadata block]

## Table of Contents
[Full numbered TOC]

## 1. What This Module Is
## 2. The Core Thesis — One Sentence
## 3. The [N]-Layer Architecture
   [ASCII diagram]
## 4. Layer 1 — [Foundation Layer Name]
   ### 4.1 [Concept]
   ### 4.2 [Concept]
   ### 4.3 [Concept]
## 5. Layer 2 — [Identity/Principle Layer Name]
   [subsections]
## 6. Layer 3 — [Expression/Application Layer Name]
   [subsections — the practical protocols]
## 7. [Domain-Specific Context 1]
## 8. [Domain-Specific Context 2]
## 9. [Typology / Archetype Reference]
## 10. [Communication / Mode Reference]
## 11. Failure Patterns — Anti-Behaviors to Eliminate
## 12. The Development Progression
## 13. Core Vocabulary Reference
## 14. The [N] Iron Rules — Quick Reference
## 15. Source Map
```

---

## ─────────────────────────────────────────────
## COMBINED SINGLE-AGENT PROMPT
## ─────────────────────────────────────────────

Use this version when you want a single agent to execute both stages end-to-end without manual handoff.

---

### COMBINED PROMPT (copy and customize)

```
You are a research and knowledge synthesis agent. Execute the following two-stage task in sequence.

═══════════════════════════════════════
STAGE 1 — COMMUNITY RESEARCH
═══════════════════════════════════════

Research and compile the top [NUMBER] most recommended [RESOURCE TYPE] on the topic of [TOPIC] as cited across the following communities:

COMMUNITIES:
[List your communities]

TOPIC FOCUS:
[List your sub-topics]

For each resource provide: title, author, core thesis, key concepts, best-for audience, why the community recommends it, community tier (S/A/B/C), and notable criticisms.

Source from actual community discussions and reading lists, not generic aggregators.
Conclude Stage 1 with honorable mentions and a meta-analysis of what the consensus reveals.

═══════════════════════════════════════
STAGE 2 — KNOWLEDGEBASE SYNTHESIS
═══════════════════════════════════════

Using your Stage 1 findings, synthesize all resources into a unified knowledgebase module on [TOPIC], to be filed under [PARENT CATEGORY].

The document must include in order:
1. Title and metadata header
2. Full table of contents
3. One-sentence core thesis
4. Layered architecture with ASCII diagram ([N] layers, foundational to expressive)
5. One detailed section per layer with subsections for each major concept
6. Domain-specific application sections for: [CONTEXT 1], [CONTEXT 2], [CONTEXT 3]
7. Typology/archetype reference table
8. Failure patterns table (behavior | why it fails)
9. Development progression (Stage 1 through Stage N with milestones)
10. Core vocabulary glossary (term | definition)
11. [N] Iron Rules as a quick-reference numbered list
12. Source map table (need | primary source | secondary source)

Format as knowledgebase-style markdown. Direct and practical. No disclaimers. Comprehensive length. Do not truncate.

Output Stage 1 first, then Stage 2 immediately after.
```

---

## ─────────────────────────────────────────────
## CONFIGURATION VARIABLES — FILL THESE IN
## ─────────────────────────────────────────────

When deploying this template, fill in the following variables before running:

| Variable | Description | Example |
|---|---|---|
| `[NUMBER]` | How many resources to find | 10 |
| `[RESOURCE TYPE]` | What kind of resource | books / courses / frameworks |
| `[TOPIC]` | The subject being researched | seduction / stoic philosophy / day trading |
| `[COMMUNITIES]` | Which communities to source from | r/seduction, SoSuave, Goodreads |
| `[SUB-TOPICS]` | Specific angles within the topic | day game, player mindset, flirting |
| `[PARENT CATEGORY]` | Where this module lives in your knowledge system | Male Character Architecture |
| `[CONTEXT 1-3]` | Specific environments for application sections | workplace, cold approach, nightlife |
| `[N] LAYERS` | How many architectural layers | 3 (Foundation / Identity / Expression) |
| `[N] IRON RULES` | How many distilled rules to produce | 10 |

---

## ─────────────────────────────────────────────
## DEPLOYMENT NOTES FOR CLAUDE PROJECTS
## ─────────────────────────────────────────────

When using this as **Claude Project Instructions**, paste the Combined Prompt into the project system prompt with your variables pre-filled. The agent will execute both stages on any conversation where the user references the topic or asks for the knowledgebase.

**Recommended project instruction format:**

```
[Paste combined prompt with all variables filled in]

Additional behavior rules:
- Always produce the full document, never truncated
- Output Stage 1 as a collapsible summary, Stage 2 as the primary deliverable
- Save all outputs as markdown files
- If asked to update or expand the knowledgebase, locate the relevant section and extend it rather than rebuilding from scratch
- Cross-reference new information against existing Iron Rules and Source Map before adding
```

**When using as an agentic task:**
- Feed Stage 1 output as context to Stage 2 agent
- Stage 1 agent: researcher role, web-search enabled
- Stage 2 agent: synthesizer role, no search needed — works from Stage 1 context only
- Handoff variable: the full Stage 1 output passed as `{{research_report}}`

---

*Template v1.0 — Bold Venture X Internal Tools*
*Designed from the Seduction Module research pipeline, March 2026*
