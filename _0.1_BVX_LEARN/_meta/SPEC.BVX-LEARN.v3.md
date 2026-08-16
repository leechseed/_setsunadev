---
original_path: "/mnt/user-data/outputs/BVX-LEARN-v3-spec.md"
source_conversation: "Building a robust markdown knowledge base system"
created: 2026-06-08
trunk: BLACK
kind: generated-file
---

---
id: SPEC.BVX-LEARN.v3
title: "BVX-LEARN v3.0 — Multi-Source Knowledge Capture & Normalization Spec"
type: system-spec
status: draft
confidence: high
version: 3.0.0
supersedes: [BVX-LEARN-v1.0, BVX-LEARN-v2]
source_type: internal
created: 2026-06-08
updated: 2026-06-08
tags: [bvx-learn, knowledge-base, ingestion, obsidian, ssot, pipeline, spec]
related: ["[[_INDEX]]", "[[OPERATOR-PROFILE]]", "[[NO-GO-LIST]]"]
aliases: ["BVX-LEARN v3", "the spec", "v-next"]
---

# BVX-LEARN v3.0 — Multi-Source Knowledge Capture & Normalization Spec

> **What this is:** The v-next specification for the BVX-LEARN system. v1.0 was a book/PDF one-sheet factory. v3 generalizes it into a **multi-source knowledge engine**: any messy input — books, web/video, chat logs, raw voice dumps — gets cleaned, distilled, and written as a consistent markdown entry into a repository that any Claude (or Claude Code) session can reliably pull from.
>
> **How to read it:** Sections 1–4 are the locked design. Section 5 is the one decision you owe me — two schema paths plus a hybrid, with a matrix to pick from. Sections 6–12 are the build detail. Section 14 lists every open decision in one place.
>
> **This file is also the reference example.** Its own front matter, TOC, and structure model what a v3 entry should look like.

---

## TABLE OF CONTENTS

1. [Purpose & Scope](#1--purpose--scope)
2. [Design Principles (the invariants)](#2--design-principles-the-invariants)
3. [The Pipeline](#3--the-pipeline)
4. [Source-Type Handling](#4--source-type-handling)
5. [Entry Schema — Two Paths + Hybrid (your pick)](#5--entry-schema--two-paths--hybrid-your-pick)
6. [The Canonical Entry Template](#6--the-canonical-entry-template)
7. [ID & Naming Convention](#7--id--naming-convention)
8. [Repository Layout (the "data lake" folder)](#8--repository-layout-the-data-lake-folder)
9. [Quality Gates (the robustness layer)](#9--quality-gates-the-robustness-layer)
10. [Trigger-Command Grammar](#10--trigger-command-grammar)
11. [Export Procedure](#11--export-procedure)
12. [Link-Readiness — designed, not built](#12--link-readiness--designed-not-built)
13. [What Changed: v1/v2 → v3](#13--what-changed-v1v2--v3)
14. [Open Decisions (lock these)](#14--open-decisions-lock-these)
15. [META: About This Entry](#15--meta-about-this-entry)

---

## 1 · Purpose & Scope

**The job.** Turn any source you throw at it into a clean, consistent, link-ready markdown entry, and land that entry in a designated repository that an LLM can read and retrieve from with zero re-orientation.

**Why v3 exists.** v1 distilled books into one-sheets — single source type, manual everything, no validation, no shared index. You now want to feed it four source types, you want it to *clean the mess* (not just summarize the clean), you want the output to live in a repository Claude pulls from, and you want it robust and efficient rather than hope-for-the-best. v3 is that.

**Design goals, in priority order:**

1. **Consistency** — every entry obeys the same schema so retrieval is predictable.
2. **Robustness** — entries can't ship malformed; quality gates enforce the format (Section 9).
3. **AI-retrievability** — the repo is structured so a fresh session primes itself in one read (Section 8).
4. **Link-readiness** — the substrate for connecting entries exists now; the graph gets built later (Section 12).
5. **Efficiency** — minimum ceremony per entry; the heavy machinery only engages when a topic earns it.

**Out of scope for v3 (deliberately):** the automation tool itself (this is the spec it would implement), the live linking/graph engine, and any cross-vault federation. All three are designed *around* so they slot in later without a rewrite.

---

## 2 · Design Principles (the invariants)

These are the rules every entry and every pipeline stage must hold. They're the things that stay true regardless of source type or schema choice.

- **One source, one canonical entry.** SSOT. A source is captured once; everything else points at it.
- **Distill, don't summarize.** Extract the invariants (what's always true), the heuristics (decision rules), the load-bearing concepts. Cut the rest. An entry is a reference card, not a second copy of the source.
- **Every entry is self-describing and self-locating.** YAML front matter tells a machine what this is; a stable ID tells it where this is. No entry relies on its filename or folder for meaning.
- **Provenance is explicit.** What came from full text vs. research vs. inference is always flagged. `status` and `confidence` are never blank.
- **Dual-mode by construction.** A human reads top-down (TOC → body). A machine reads section-level (front matter + targeted section). The same file serves both.
- **Idempotent and upgradeable.** Re-running on the same source updates in place. A `draft` entry upgrades to `complete` when better source material arrives — never a second file.
- **Format is enforced, not requested.** The quality gate is the contract. If it doesn't pass, it doesn't export.
- **Link-ready, not yet linked.** Stable IDs, a `related` field, and an index make linking trivial later. Don't build the graph now; don't foreclose it either.

---

## 3 · The Pipeline

Seven stages, each a contract with a defined input and output. This is the "run it and export it" flow expressed as a spec — a tool would implement these stages; a Claude session walks them manually.

| # | Stage | Input | Output |
|---|-------|-------|--------|
| 1 | **Ingest** | Raw source (file, URL, pasted text, chat log) | Normalized raw text + captured metadata (origin, date, type) |
| 2 | **Clean** | Normalized raw text | De-noised text: tool-call cruft, false starts, ad chrome, duplication, filler removed |
| 3 | **Distill** | Cleaned text | Invariants, heuristics, core concepts, key claims surfaced |
| 4 | **Structure** | Distilled material | Populated entry template (Section 6) with YAML + TOC + body |
| 5 | **Validate** | Populated entry | Pass/fail against the quality gate (Section 9) |
| 6 | **Export** | Validated entry | Written to `/entries/[ID].md` in the repo (Section 11) |
| 7 | **Index** | Exported entry | Row appended/updated in `_INDEX.md` |

Two rules on flow: a failed **Validate** loops back to **Structure** (never skips); **Index** is mandatory, not optional — an entry that isn't in the index is invisible to the next session.

---

## 4 · Source-Type Handling

All four types converge on the same entry schema, but each gets to the distilled material differently. The differences live in *extraction* and *what goes in the YAML*; the body structure is shared.

### 4.1 Books / PDFs  → prefix `LRN`
- **PDF present:** extract from full text. `status: complete`.
- **Title + author only:** web-research the content (reviews, chapter breakdowns, key arguments), cross-reference multiple sources. `status: draft`. Upgradeable later by dropping the PDF (`"Upgrade [ID]"`).
- **YAML extras:** `author`, `publisher`, `year`, `isbn`, `pages`.
- **Gotcha:** flag where a claim is the researcher's synthesis vs. the book's actual position.

### 4.2 Videos / Articles / Web  → prefix `MED`
- Pull transcript (video) or article body (web). Strip nav, ads, comments, related-post chrome.
- **YAML extras:** `source_url` (required), `channel_or_publication`, `retrieved` (date), `runtime_or_wordcount`.
- **Depth options:** concept-only extraction; or concepts up top + timestamped/section appendix below.
- **Gotcha:** auto-generated captions are unreliable — flag uncertain attribution/wording rather than guess. Never reproduce long verbatim passages; distill and link out.

### 4.3 Chat Logs / Claude Code Session Output  → prefix `SES`
- **Keep:** decisions reached, conclusions, final rationale, code/artifacts produced, open threads. **Cut:** the back-and-forth, abandoned branches, tool-call noise, "let me try again" loops.
- **YAML extras:** `session_date`, `tool` (Claude / Claude Code / other), `artifacts` (list of files/IDs produced), `decisions` (count or list).
- **Structure tweak:** lead the body with a **Decision Log** and an **Artifacts** block; the narrative is secondary.
- **Gotcha:** sessions ramble and self-correct — capture the *endpoint*, not the journey. If a decision was reversed mid-session, record only the final state and note it superseded an earlier call.

### 4.4 Raw Notes / Voice Dumps  → prefix `NOTE`
- De-ramble: reorder into logical structure, merge repetition, fix transcription artifacts — **without** sanding off intent or voice.
- **YAML extras:** `capture_method` (voice / typed), `raw_retained` (bool — whether the original dump is preserved in an appendix).
- **Structure tweak:** add an "Inferred vs. Stated" note wherever you reorganized or filled gaps, so future-you knows what was actually said vs. what the cleanup assumed.
- **Gotcha:** voice dumps bury the lede and contradict themselves. Surface the actual point; don't smooth a contradiction into a false consensus — flag it as an open question instead.

---

## 5 · Entry Schema — Two Paths + Hybrid (your pick)

You asked to see both. Here they are, plus the hybrid I'd actually ship. **The YAML, ID scheme, and folder conventions are identical across all three** — so this choice is reversible, and you can start with one and migrate without reformatting.

### Option A — Atomic One-Sheet (v1, evolved)
One self-contained `.md` per source. Everything about that source lives in one file.

- **Pros:** lowest overhead, fastest to produce, glanceable, dead-simple to retrieve.
- **Cons:** doesn't decompose deep topics (a 400-page book and a tweet get the same container); weak graph; cross-source synthesis has nowhere to live.
- **Best when:** most of your sources are "capture and move on."

### Option B — Vault Architecture (the richer spec)
A topic is a **spine** doc + **atomic notes** + a **decision log** + **fact files**, all under a master `_INDEX`, wired with wikilinks.

- **Pros:** scales to deep topics, rich navigable graph, AI primes in one read (index → spine → atomics), synthesis has a home.
- **Cons:** heavyweight; many docs per topic; demands discipline; overkill for a single quick source.
- **Best when:** you're doing sustained multi-source investigation on a few big themes (e.g., the venture build).

### Option C — Hybrid (recommended)
The **one-sheet is the default atom** for any single source (so capture stays cheap). The **architecture is latent**: shared IDs + `related` front matter + a live `_INDEX.md` mean any cluster of one-sheets can be promoted into a spine *when a topic earns depth* — no reformatting, just add a spine that links the atoms.

- **Pros:** cheap per entry, but the vault structure is there the moment you want it. You never pay the Option B tax until a topic justifies it.
- **Cons:** requires you to recognize when to promote a cluster (mitigated by the index making clusters visible).
- **Best when:** mixed reality — lots of quick captures, a few deep threads. **This is your actual situation.**

### Decision matrix

| Criterion | A · One-Sheet | B · Vault Arch | C · Hybrid |
|---|---|---|---|
| Overhead per entry | **Lowest** | High | Low |
| Scales to deep topics | Poor | **Excellent** | **Excellent** (on promotion) |
| Graph richness | Weak | **Rich** | Grows on demand |
| AI retrieval | Good | **Best** | **Best** (index-led) |
| Discipline required | **Minimal** | High | Low–moderate |
| Reversible / migratable | — | — | **Yes, by design** |
| Fit for your mix | OK | Overkill day-to-day | **Strong** |

> **My pick: C.** It's A's economics with B's ceiling. You start every source as a one-sheet and only build spines where depth shows up. **Tell me A, B, or C and I'll lock Section 6 to it.**

---

## 6 · The Canonical Entry Template

The v3 entry. The body adapts by source type (Section 4); the skeleton is constant. Under Hybrid (Option C) this *is* the atom; a spine is the same skeleton with the body replaced by a curated set of `related` links and synthesis.

```markdown
---
id: LRN.07
title: "Make It Stick — The Science of Successful Learning"
type: book                 # book | article | video | session | note | spine
status: complete           # complete | draft | stub
confidence: high           # high | medium | low
source_type: book          # book | web | video | session | note | internal
source_url:                # required for web/video
author: "Brown, Roediger, McDaniel"
year: 2014
retrieved:                 # date for web/video/session
created: 2026-06-08
updated: 2026-06-08
tags: [learning, memory, cognitive-science]
related: ["[[LRN.03]]", "[[NOTE.12]]"]   # link-ready (Section 12)
aliases: ["Make It Stick"]
---

# [Title]
## Knowledge Entry — [Study Guide / Capture / Session Digest / Cleaned Note]

[One-line orientation: what this is and why it's in the vault.]

## TABLE OF CONTENTS
- [section links]

## 1. Core Thesis
[The single load-bearing idea, 2–4 sentences.]

## 2. Framework / Structure
[The skeleton: how the source organizes its argument or system.]

## 3. Key Concepts
[The mechanics. Each: name → what it is → why it matters.]

## 4. Heuristics & Decision Rules
[The actionable "when X, do Y" extractions. This is where reuse value lives.]

## 5. Invariants
[What's always true regardless of context.]

## 6. Pitfalls / Myths
[Common errors the source corrects.]

## 7. Application — How This Maps to My Work
[Ties to active ventures. Kept clearly separate from source extraction.]

## 8. Cross-References & Related
[Table: related entries/sources and how they connect.]

## 9. Provenance & Confidence
[What was sourced from full text vs. research vs. inference. Source-type
notes from Section 4 land here — e.g., caption uncertainty, reversed
session decisions, inferred-vs-stated for voice dumps.]

## META: About This Entry
- Template: BVX-LEARN-v3.0
- Source classification: [ ]
- Created / Updated: [ ]
```

**Adaptation quick-reference:** `session` entries lead with a Decision Log + Artifacts block before Section 1. `note` entries add "Inferred vs. Stated." Technical books expand §3/§4; narrative books reframe §2 as "Narrative Arc." Quick captures may legitimately stop at §1–§4 — but `status` must then be `stub`, never silently thin.

---

## 7 · ID & Naming Convention

Evolves `LRN.xx` into a **type-prefixed serial** so the repo stays navigable as it grows across source types.

| Prefix | Source type | Example |
|---|---|---|
| `LRN` | Books / learning | `LRN.07` |
| `MED` | Video / article / web | `MED.14` |
| `SES` | Chat / Claude Code session | `SES.03` |
| `NOTE` | Raw / voice dump | `NOTE.21` |
| `SPINE` | Synthesis spine (Option B/C) | `SPINE.learning` |

- **Filename = `[ID].md`** (e.g., `LRN.07.md`). ID is the source of truth, not the title.
- **Serial assignment:** v3 upgrade — the **`_INDEX.md` holds the next-available number per prefix**, so you stop telling me "this is LRN.01" every time. The index is the counter. (Manual override still allowed.)
- **Emoji prefixes** (`🧬 LRN`, `🔍 MED`) from your later vault aesthetic: optional, cosmetic, off by default — flip on if you want the visual sort in Obsidian. *(Decision in §14.)*

---

## 8 · Repository Layout (the "data lake" folder)

The folder Claude pulls from. Structured so a fresh session orients in one read and so raw mess never contaminates clean entries.

```
BVX-LEARN/
├── _meta/
│   ├── SPEC.BVX-LEARN.v3.md      ← this document
│   ├── OPERATOR-PROFILE.md       ← you, fiscal year, ventures, constraints (session primer)
│   ├── NO-GO-LIST.md             ← ruled-out things, so sessions don't re-suggest them
│   └── CHANGELOG.md              ← schema/version history
├── _index/
│   ├── _INDEX.md                 ← master list: every entry, status, prefix counters
│   └── by-type/                  ← optional per-prefix index views
├── inbox/                        ← raw drops awaiting processing (the actual "data lake")
└── entries/                      ← clean, validated, canonical entries
    ├── LRN.07.md
    ├── MED.14.md
    └── ...
```

**AI-retrieval contract:** any new session is primed by reading, in order, `OPERATOR-PROFILE.md` → `_INDEX.md` → the specific entry/entries it needs. `inbox/` is staging only — nothing there is considered canonical or retrievable until it's processed into `entries/` and indexed.

---

## 9 · Quality Gates (the robustness layer)

The thing v1 didn't have. An entry cannot export until every gate passes. This is what makes v3 *robust* rather than best-effort.

- [ ] YAML present, valid, and complete (no blank `status` / `confidence` / `id`)
- [ ] `id` is unique against `_INDEX.md`
- [ ] Title and one-line orientation present
- [ ] TOC present and its anchors resolve
- [ ] Required body sections present for the declared `type` (or `status: stub` is set honestly)
- [ ] No unfilled `[bracketed placeholders]` left in the body
- [ ] Provenance flagged (full-text / research / inference) in §9
- [ ] `source_url` present when `source_type` is web/video
- [ ] `related` links are well-formed `[[wikilink]]` syntax (targets need not exist yet)
- [ ] Length within target band for the type (stub < 1 page; standard 1–2; deep dive flagged)

Fail any → loop back to **Structure** (Pipeline stage 4). A tool would assert these programmatically; a session checks them before writing.

---

## 10 · Trigger-Command Grammar

Generalizes the v1 voice commands across all source types. **Match intent — exact wording optional.** You drive by voice; these are the spoken handles.

| Intent | Spoken triggers |
|---|---|
| Capture a book (PDF or title) | "Learn this" · "Learn [title] by [author]" |
| Capture web/video | "Capture this [url]" · "Grab this video" |
| Digest a chat/Claude Code session | "Distill this session" · "Digest this log" |
| Clean a raw/voice dump | "Clean this dump" · "Tidy this note" |
| Upgrade a draft with better source | "Upgrade [ID]" · "Make this complete" |
| Expand a dimension | "More heuristics" · "More invariants" |
| Promote a cluster to a spine (Option B/C) | "Spine [topic]" · "Build a spine for [topic]" |
| Branch a sub-topic into its own entry | "Branch [ID] on [topic]" · "Go deeper on [topic]" |
| Refresh the index | "Index it" · "Update the index" |

If you drop a source with no trigger: assume a standard capture of the detected type.

---

## 11 · Export Procedure

Since v3 is a spec (not yet a tool), this is the Claude-assisted flow. The numbered steps map 1:1 to a future Claude Code script, so the spec is implementation-ready.

1. Run Pipeline stages 1–5 (ingest → validate).
2. Read `_INDEX.md`; take the next serial for the entry's prefix.
3. Write the validated entry to `entries/[ID].md`.
4. Append/update the entry's row in `_INDEX.md` and bump the prefix counter.
5. If a PDF/source file was used, note its location in `§9 Provenance` (don't copy binaries into the repo).
6. Report back: ID assigned, status, and any gates that needed a second pass.

**Future automation hook:** a `bvx-learn` CLI (Claude Code) watching `inbox/` would run 1–6 unattended — clipboard/URL/file in, validated entry + index update out. The spec is written so that tool is a transcription of these steps, not a redesign.

---

## 12 · Link-Readiness — designed, not built

You said connecting entries is "not the thing right now, but maybe build on top." Here's how v3 leaves that door wide open without building the room:

- **Stable IDs** mean a link target never breaks when a title changes.
- **`related: [[...]]`** front matter is the edge list — populated opportunistically now, harvestable into a graph later.
- **`_INDEX.md`** is the node registry — a future linker reads it to know what exists.
- **Wikilink syntax** is Obsidian-native, so the graph view already works the moment you add links manually.

**What's explicitly deferred:** automated link suggestion, backlink synthesis, and any graph-analysis layer. When you want it, it reads the substrate above — no entry needs reformatting. That's the whole point of doing the boring frontmatter discipline now.

---

## 13 · What Changed: v1/v2 → v3

| Area | v1 / v2 | v3 |
|---|---|---|
| Source types | Books / PDFs only | Books, web/video, sessions, raw notes |
| Job | Summarize clean sources | **Clean the mess**, then distill |
| Output target | Loose `.md` you file manually | Structured repo Claude pulls from |
| IDs | `LRN.xx`, you track the number | Type-prefixed, **index-driven counter** |
| Validation | None | **Quality gates** before export |
| Provenance | Implicit | Explicit `status` + `confidence` + §9 |
| Architecture | One-sheet only | **Two paths + hybrid**, reversible |
| Linking | Not addressed | **Link-ready substrate** baked in |
| Session priming | Ad hoc | `OPERATOR-PROFILE` + `_INDEX` contract |

---

## 14 · Open Decisions (lock these)

The "ask me at the end" list — the calls only you can make. My recommendation is flagged on each.

1. **Schema (§5):** A, B, or **C-hybrid (rec)**?
2. **Repo location:** a new top-level `BVX-LEARN/` vault, or nested inside an existing vault (BVX / ASTRO7EX / etc.)? Path?
3. **Emoji ID prefixes (§7):** on for visual sort, or **off (rec, cleaner for grep/retrieval)**?
4. **Serial assignment (§7):** **index-driven counter (rec)** or keep manual?
5. **Default length bands (§9):** confirm stub `<1pg` / standard `1–2pg` / deep-dive flagged, or set your own.
6. **§7 "Application" section:** keep it inside every entry, or split personal-application into separate `NOTE` entries to keep captures pure?
7. **Next deliverable after this spec:** turn §6 into a standalone copy-paste **template file**, draft the **Project Instructions** that enforce this spec, or spec the **Claude Code CLI** from Section 11?

Answer any subset; unanswered ones I'll default to the recommendation when we build.

---

## 15 · META: About This Entry

- **Entry Type:** System Specification
- **Source Classification:** Internal — synthesized from BVX-LEARN v1.0/v2 prior work + current requirements
- **Confidence Level:** High (design); decisions in §14 pending
- **Template Version:** BVX-LEARN-v3.0
- **Created:** 2026-06-08
- **Last Updated:** 2026-06-08
- **Status:** `draft` — promotes to `complete` once §14 decisions are locked
