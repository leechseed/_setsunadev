---
id: SPEC.BVX-LEARN.decisions
title: "BVX-LEARN — Locked Decisions"
type: system-spec
status: complete
confidence: high
version: 3.1.0
implements: SPEC.BVX-LEARN.v3
created: 2026-08-15
tags: [bvx-learn, spec, locked, ingestion]
---

# BVX-LEARN — Locked Decisions

`SPEC.BVX-LEARN.v3` (2026-06-08) sat at `status: draft` for two months because §14 was never answered. These are the answers. **The spec is now `complete`.**

The v3 spec itself was recovered from the claude.ai export on 2026-08-15 — it had never existed on disk. Canonical copy now lives beside this file.

---

## D1 · ID scheme — **subject codes win**

> ⚠️ **AMENDED same day — see [D4](#d4--id-and-subject-are-decoupled-supersedes-d1s-filename-rule).** D1 was locked when the known library was 28 books. The Zotero inventory then surfaced **1,704 attachments**, which made subject-in-filename untenable. D1's *taxonomy* holds; its *filename rule* is superseded.

Existing subject taxonomy is canonical. v3's source-type prefixes (`LRN`/`MED`/`SES`/`NOTE`) are **rejected as filenames**.

| Code | Domain | Next free |
|---|---|---|
| `BIZ` | Business / economics | `BIZ.02` |
| `CRE` | Creative / literary | `CRE.02` |
| `MSX` | Sex, seduction, relationships | **`MSX.18`** |
| `PHI` | Philosophy / esoteric | `PHI.03` |
| `PSY` | Psychology / clinical | **`PSY.08`** |

- Filename stays the existing convention: `🧬 MSX.18 — Title — Author (Year).md`
- **28 entries already exist. No migration. No renaming.**
- Source type is carried in YAML as `source_type:`, not in the ID.
- `_INDEX.md` holds the next-free counter per subject code.

**Why:** subject grouping is what actually feeds a character system. Source-type grouping answers a question nobody asks.

---

## D2 · The `feeds:` field — book → character fascia

**This is the connective tissue that did not exist.** Every knowledge entry declares, in typed form, which character-system variables it is qualified to source.

```yaml
feeds:
  - layer: L9
    variable: shame_index
    strength: primary      # primary | supporting | contextual
    note: "Clinical shame taxonomy, ch. 4"
  - layer: L9
    variable: intimacy_mode
    strength: supporting
```

Rules:

- `layer` — one of `L1`–`L12`, or `DRAMATICA`, or `ASTROLOGY`
- `variable` — the exact field name as it appears in the vertical slice schema
- `strength` — `primary` (can author the value), `supporting` (can justify it), `contextual` (background only)
- A book with nothing to feed gets `feeds: []`. Explicit empty, never omitted.

**What this buys:** *"which books authored L9.shame_index"* becomes a grep, not a memory. And when a layer is marked `INFERRED`, the query *"what do I own that could author this"* is answerable in one pass.

**Reciprocal note:** the character side does *not* maintain a reverse index. `feeds:` is the single source of truth for the edge; the reverse view is derived.

---

## D3 · §7 "Application" stays

The prose section survives alongside `feeds:`. Prose carries the *why*; `feeds:` carries the *wiring*. They are not redundant — one is for you, one is for retrieval.

---

## D4 · ID and subject are decoupled *(supersedes D1's filename rule)*

**New entries use a flat serial ID.** Subject lives in YAML, not the filename.

```yaml
---
id: BVX.0431
title: "Story and Discourse: Narrative Structure in Fiction and Film"
subjects: [LIT, CRE]        # multi-valued, ordered by relevance
primary_subject: LIT
trunk: BLACK
---
```

- Filename is `BVX.####.md`. The ID never changes and never encodes meaning.
- `subjects` is a **list** — a book can be both `LIT` and `CRE`, and many are.
- The 28 existing `KNOWLEDGE_AREAS` entries **keep their current filenames**. They gain `id`/`subjects` frontmatter but are not renamed.

**Why this reversed D1:** D1 was locked against a known library of 28 books. The Zotero inventory then found **1,704 attachments**. At that scale, subject-in-filename means every misclassification is a rename plus broken links plus a burned ID — which forces the classifier to be perfect. Decoupling makes a wrong call a one-line edit, so the classifier only has to be *good*. **The best classifier is one whose mistakes are cheap.**

---

## D5 · Taxonomy — 17 categories, derived from the library

Approved 2026-08-15 from evidence across 1,359 usable items (84% rule coverage).

| Code | Trunk | Domain | Seed count |
|---|---|---|---|
| `CRE` | BLACK | Creative craft — writing & story | 281 |
| `GAM` | BLACK | Game systems & design | 213 |
| `VIS` | BLACK | Visual art, photography, cinematography | 129 |
| `LIT` | BLACK | Literary theory & scholarship | 73 |
| `TEC` | BLACK | Programming, CS, engineering | 59 |
| `POL` | BLACK | Politics, power, radicalization | 26 |
| `PSY` | BLACK | Psychology & typology | 26 |
| `PHI` | BLACK | Philosophy, esoteric, religion | 25 |
| `PRD` | BLACK | Production tooling & pipeline | 19 |
| `MIL` | BLACK | Military doctrine, tactics, firearms | 17 |
| `PRF` | BLACK | Theatre, acting, performance | 17 |
| `DSN` | BLACK | Design theory & systems | 12 |
| `BIZ` | BOTH | Business, finance, property | 50 |
| `SLF` | BOTH | Learning, self-development | 7 |
| `MSX` | ORANGE | Sex, relationships, erotic | 117 |
| `FIT` | ORANGE | Fitness, physique, sport | 32 |
| `SOC` | **ORANGE** | Social media, platforms, culture | 26 |

Two calls made explicitly:

- **`SLF` kept** despite only 7 seed items.
- **`SOC` is ORANGE, not BOTH** — the TikTok/creator-economy cluster is load-bearing venture research, not general interest.

The old five (`BIZ`/`CRE`/`MSX`/`PHI`/`PSY`) all survive; the other twelve are new. `MSX.18` and `PSY.08` remain valid for the legacy-named entries.

**Classification method:** precedence-ordered rules (first match wins) get ~85%. The remainder is classified by reading, not regex. Ambiguous cases go to a review list rather than being guessed silently.

---

## Remaining §14 items — defaulted per spec recommendation

| # | Decision | Locked as |
|---|---|---|
| §14.1 | Schema path | **C — Hybrid.** One-sheet is the default atom; spines promoted only when a topic earns depth. |
| §14.2 | Repo location | `_0.1_BVX_LEARN/` (existing vault, keeps the 28 entries in place) |
| §14.3 | Emoji ID prefixes | **On** — the 28 existing entries already use `🧬`. Consistency beats grep-purity. |
| §14.4 | Serial assignment | Index-driven counter, per subject code |
| §14.5 | Length bands | stub < 1pg · standard 1–2pg · deep-dive flagged |
| §14.6 | Application section | Keep inside the entry (see D3) |
| §14.7 | Next deliverable | Process source PDFs — build the template by using it |

---

## Pipeline, unchanged from v3

Ingest → Clean → Distill → Structure → Validate → Export → Index

Failed Validate loops back to Structure, never skips. **Index is mandatory — an unindexed entry is invisible to the next session.**

## Governing principle, unchanged

> **Distill, don't summarize.** Extract the invariants, the heuristics, the load-bearing concepts. Cut the rest. An entry is a reference card, not a second copy of the source.

---

## Open

- `_INDEX.md` does not yet exist. It must be built and backfilled with all 28 existing entries before entry #29 ships, or the counter contract is already broken.
- The 28 existing entries predate `feeds:`. They need a backfill pass to be useful to the character system.
