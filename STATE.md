---
title: STATE — what is live right now
type: state
status: living document
updated: 2026-08-16
read_first: true
---

# STATE

**This is the answer to "what have we been working on."** Read this first, every session, before anything else. The ranked project board lives in [PROJECTS.md](PROJECTS.md).

> **Challenge:** *"Americans are not born. They are forged in the chaos and dysfunction of American life."*
> **Countersign:** *"The Asset is acquired. The Noise is archived. The Feed is stable."*
> → then the board. Equivalents: "set me up" · "where did we leave off" · "the board".

**Autosave is on.** A Stop hook (`_tools/autocommit.sh`) commits every change to git when a session ends. Local only — it never pushes. Run `git push` yourself when you mean to publish.

It is an **index, not a store**. Detail lives in the registries below; this file says what's live, what moved, and who's blocking. If it's not here, it isn't active.

> **The rule, inherited from the Ultrasin registry:** chats are working memory, not storage. If a decision isn't written down, it does not exist. Every session that locks a decision or builds a system ends by updating this file.

---

## 🔴 Blocked on you

Nothing moves on these until you rule. Ordered by what they unblock.

| # | Decision | Unblocks |
|---|---|---|
| 1 | **Extract the OVEREXITOUT storyform from Dramatica** (~65 fields — 9 dynamics, 2 role, 8 MC, and the entire IC/OS/RS throughlines) | Tori's pipeline locks. Every downstream character. **Highest leverage in BLACK.** |
| 2 | **Anna Colson Conway as Impact Character?** — derived via [[BVX.0064]] | 17 IC fields, the RS throughline, Movements 2–4 |
| 3 | Propagate `armor_index` · `Expressive Range` · `satisfaction_cycle_truncation` into the vertical slice SSOT | Stops the character schema forking |
| 4 | `motivation_element` — holds MC Problem (`Equity`) or Motivation quad primary (`Consider`)? | TRUTH_VULNERABILITY flag trigger |
| 5 | Name the fused school — Inner Spiral / Red Hills | Movements 2–4, i.e. most of Tori |
| 6 | BVX ↔ Ultrasin firewall structure | Public launch (Ultrasin ledger #1) |

> **Leverage check** ([PROJECTS.md](PROJECTS.md#the-same-ten-ranked-by-leverage)): #1 and #6 are the only two entries with a whole trunk behind them — #1 releases BLACK, #6 releases the money track. Neither requires building anything. **#6 is ranked last here and gates the most revenue.** The other four are propagation work that follows #1.

---

## ⛔ Do not push yet

**Two commits pending, and they contain the full claude.ai archive** — 552 files, 319 conversations, including the ~712k personal cluster. `git push` publishes all of it to a public repo.

Tabled 2026-08-16: the **pseudonymization filter**. Decision was to stay public and build it. Design constraint found — git pushes commits, not working files, so this needs a **scrubbed mirror branch** (`main` local-only as truth, generated `public` branch carries the transform), not a push-time filter. `_tools/scan_sensitive.py` is written and **unrun**; it's read-only and finds structured identifiers + codebook entity seeds across the tracked tree. Run it first when this resumes — no codebook without knowing the corpus.

Separately approved: the **pseudonym codebook as a fiction device** (roman à clef, real → in-world entities, feeding the character system). Judged on craft, not on concealment.

---

## 🟡 Live

### BLACK — creative, IP, systems

| System | State | Where |
|---|---|---|
| **OVEREXITOUT / The Outliers** | Tori node built, L9 AUTHORED, IC candidate derived. Storyform blocked. | `_CANON_NODES/` |
| **Character system** (Dramatica × astrology × 12-layer) | Validated 11/11 layers. Stalled since April on the storyform extraction. | `ShroomsQ/_CANON/_SSOT/02_*` |
| **BVX-LEARN** | v3 spec recovered + decisions locked. 1,106 sources indexed, classifier 99%. Next ID `BVX.1107`. | `_0.1_BVX_LEARN/_meta/` |
| **Leechseed Manifesto** | 🔴 **Found, not in canon.** 10 docs, May 2025, buried in imported-Joplin. | `OVER_EXIT_OUT_OBSIDIAN/.../manifesto/` |
| **L2b MORPHOLOGY** | Designed this session, unspecced. Frame → Tissue → **Condition** → Line → Archetype. | — |

### ORANGE — venture, body, sexuality

| System | State | Where |
|---|---|---|
| **Ultrasin venture** | Full registry v0.1, 32-chat sweep. 10 open decisions. | `_CLAUDE_ARCHIVE_2026-08-15/files/2026-08-05_ultrasin-master-registrymd.md` |
| **Primed Protocol** | ✅ Documented today. Ledger item 8 closed, §H 🟡→🟢. | `Desktop/ULTRASIN-primed-protocol.md` |
| **GDP-1 BOOTYCAMP** | P1 ready to run. Gate out = 60-second squeeze hold. | Registry §G |
| **Erotic Range** | ✅ Live, phone-ready, two profiles, local-only. | `Desktop/erotic-range.html` · [artifact](https://claude.ai/code/artifact/c78a1e6a-1f43-467b-a74e-7e7e66df41c1) |
| **Taxonomic-aesthetic practice** | Practice-first. Engine-vs-voice fork asked in June, never answered. | Registry §L |
| **Birthday 2026** | Space Coast run, early Oct — **Atlanta now contending** (decision 5). Transit spine locked. 5 open decisions. | [BIRTHDAY-2026.md](BIRTHDAY-2026.md) |
| **§N Interaction Economy** | ✅ Researched + distilled 2026-08-16. Principle 8 rescinded, niche selection reopened (ledger 11), practice productization tabled (ledger 12). | [ULTRASIN-interaction-economy.md](ULTRASIN-interaction-economy.md) |

---

## ✅ Moved 2026-08-16

- **BERLIN PIVOT dossier built, Gate 0 answered** — [BERLIN-PIVOT.md](BERLIN-PIVOT.md): world top-5 sexology programs ranked (UQAM · Leuven · Kinsey/IU · Curtin · Widener); Germany = the soul + field site, not the academic apex. **Bachelor's exists ([SCHOOL] multidisciplinary humanities, 2.9, ~2011 + culinary AA) — every door open.** Route E named: the Bourdain–Banksy play — literary autoethnography of the interaction economy; the empty seat next to Jones' *Camming* / Berg's *Porn Work*. Degree = tool not prerequisite. Nexus sweep parked — converges with birthday decision 5 (Atlanta).
- **Forgotten-generation thesis captured** — [ULTRASIN-forgotten-generation.md](ULTRASIN-forgotten-generation.md): the 1-in-12 bereavement cohort as §N's audience context (numbers verified — CBEM, JAMA 2024); PMV call-and-response series concept (gates on ledger 11); sexology research leads incl. Merseburg/Charité. Candidate for the empty §N naming layer.
- **PROJECTS.md leverage ranking added** — volume order vs leverage order; the two blockers releasing ~2.4M of work are both single decisions
- **BIRTHDAY-2026.md created** — Space Coast plan, transit spine locked (rail confirmed dead from [CITY]); Atlanta option opened, recon pending
- **§N Interaction Economy** — 3-agent research sweep distilled to `ULTRASIN-interaction-economy.md`; registry Principle 8 rescinded (dated strike); ledger items 11 + 12 added
- **Queued next: OSSM build consultation** — Open Source Sex Machine on the Kobra S1. Buy-vs-build fork, smooth-stroke progression ("taper," ceiling ~14"), community upgrades. Papi called the topic; research not yet run.

## ✅ Moved 2026-08-15

- **claude.ai archive recovered** — 319 conversations, 18 artifacts, 186 generated files, 12 projects → `_CLAUDE_ARCHIVE_2026-08-15/`
- **Zotero catalogued** — 1,704 attachments → 1,106 unique. 803 orphans recovered, 147 duplicate groups collapsed, 14 legacy overlaps found
- **Taxonomy derived + approved** — 17 categories, 62% → 99% coverage. Classifier is a repo tool at `_0.1_BVX_LEARN/_meta/classify.py`
- **`_INDEX.md` built** — the counter contract the spec required and never had
- **Tori L9 AUTHORED** — `armor_index` added; V-Sync identified as weaponised entrainment
- **BVX.0064 distilled** — McKee; Impact Character candidate derived
- **Primed Protocol written** — Ultrasin ledger item 8 closed
- **Erotic Range shipped**
- **Devlog resumed** after 14 months

---

## Registries — detail lives here

| Registry | Covers |
|---|---|
| `_CLAUDE_ARCHIVE_2026-08-15/INDEX.md` | Every claude.ai conversation, artifact, project |
| `_0.1_BVX_LEARN/_index/_INDEX.md` | 1,106 catalogued sources, subject + trunk |
| `_0.1_BVX_LEARN/_meta/DECISIONS.md` | BVX-LEARN locked decisions (D1–D5) |
| `.../files/2026-08-05_ultrasin-master-registrymd.md` | Ultrasin — all systems A–M, 10 open decisions |
| `_CANON_NODES/` | Canonical entity nodes |
| `_devlog/_devlog_docs/_devlog_journals/` | Daily journal, `MMDDYYYY.journal.md` |

---

## Known rot

- **`_devlog/`** is mostly a vendored copy of the vscode-journal extension repo — 464 files, 587 MB of third-party docs. Only `_devlog_docs/_devlog_journals/` is yours.
- **Six competing PKM systems on disk** — Logseq (5,194 tracked), Obsidian, Joplin ×2, ShroomsQ, claude.ai. Consolidation not started.
- **Joplin geolocation metadata** — imported vault files carry home-adjacent lat/long in a public repo. One-pass strip pending.
- **10-item review queue** — `_0.1_BVX_LEARN/_meta/REVIEW-QUEUE.md`
- `OUTLIERS_FINAL_DRAFT/outliers.fdx` is **empty**. No script pages exist.

---

## Maintenance

1. Session opens: read this file.
2. Session closes: update **Moved**, **Blocked on you**, and **Live**. Add a journal entry at `_devlog/_devlog_docs/_devlog_journals/MMDDYYYY.journal.md`.
3. Detail goes to the owning registry, never here. This file stays an index.
4. A decision that isn't written down did not happen.
