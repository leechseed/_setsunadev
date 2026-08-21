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
> → then the board. Equivalents: "sit rep" · "where did we leave off" · "the board".

**Autosave is on.** A Stop hook (`_tools/autocommit.sh`) commits every change to git when a session ends. Local only — it never pushes. Run `git push` yourself when you mean to publish.

It is an **index, not a store**. Detail lives in the registries below; this file says what's live, what moved, and who's blocking. If it's not here, it isn't active.

> **The rule, inherited from the Ultrasin registry:** chats are working memory, not storage. If a decision isn't written down, it does not exist. Every session that locks a decision or builds a system ends by updating this file.

---

## 🔴 Blocked on you

Nothing moves on these until you rule. Ordered by what they unblock.

| # | Decision | Unblocks |
|---|---|---|
| **0** | **Public-repo exposure** — archive is live on origin/main incl. personal cluster. Flip private / strip / accept. | Nothing downstream, but it is the only item that gets worse with time |
| 1 | **Extract the OVEREXITOUT storyform from Dramatica** (~65 fields — 9 dynamics, 2 role, 8 MC, and the entire IC/OS/RS throughlines) | Tori's pipeline locks. Every downstream character. **Highest leverage in BLACK.** |
| 2 | **Anna Colson Conway as Impact Character?** — derived via [[BVX.0064]] | 17 IC fields, the RS throughline, Movements 2–4 |
| 3 | Propagate `armor_index` · `Expressive Range` · `satisfaction_cycle_truncation` into the vertical slice SSOT | Stops the character schema forking |
| 4 | `motivation_element` — holds MC Problem (`Equity`) or Motivation quad primary (`Consider`)? | TRUTH_VULNERABILITY flag trigger |
| 5 | Name the fused school — Inner Spiral / Red Hills | Movements 2–4, i.e. most of Tori |
| 6 | BVX ↔ Ultrasin firewall structure — **prepared ground now exists: [BVX-ULTRASIN-twin-track.md](BVX-ULTRASIN-twin-track.md)** (3-layer sort; §N data leans SEPARATE entities + imprint-style brand) | Public launch (Ultrasin ledger #1) |

> **Leverage check** ([PROJECTS.md](PROJECTS.md#the-same-ten-ranked-by-leverage)): #1 and #6 are the only two entries with a whole trunk behind them — #1 releases BLACK, #6 releases the money track. Neither requires building anything. **#6 is ranked last here and gates the most revenue.** The other four are propagation work that follows #1.

---

## 🩺 PMCS — Preventive Maintenance Checks & Services

**The operator is equipment.** Body, medical, and life-admin readiness — the military category is Individual Medical Readiness (IMR). Not a project; never mixes with the project board. Surfaces in every sit rep.

| Item | Status | Next action |
|---|---|---|
| **Dental** — retainer advising | 🔴 open since 8/19 | Call the orthodontist. ⚠️ Dictation has twice produced "periodontist" — confirm which specialist; if there is also a gum concern, that is a **second** appointment |
| **PCP — establish care + physical** | 🔴 open | Book the physical. Sexual-health consult sequences after it: PrEP · DoxyPEP · site-specific panel · anal Pap · pelvic-floor PT referral. Timing decoupled from October — book now |
| **Pelvic-floor PT** | ⬜ gated | Referral comes out of the PCP consult above |

> Add items here the moment they are spoken. A PMCS item that is not written down did not happen.

---

## ⚠️ ALREADY PUSHED — status corrected 2026-08-21

**The claude.ai archive is live on the public repo.** 552 files, 319 conversations, on `origin/main`. Verified: `"private": false`. This includes the personal cluster — medical, OSINT, trauma-adjacent, interpersonal.

**`_PRIVATE/` held.** Zero files on the remote. Employer, income, physical description are not exposed. The gitignore worked.

The earlier "do not push yet" warning in this file was **stale and gave false assurance** — the push happened during the 8/19–21 stretch. Corrected.

**Decision now open (see Blocked on you #0):** flip the repo private, strip the archive going forward, or accept it. Flipping private stops future indexing but retracts nothing already fetched, forked, or cached.

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
| **Birthday 2026** | 🔴 **SHELVED 2026-08-21** — Plan A cancelled (no PTO, new-job standing). Research preserved as revisit-project + **BLACK/ORANGE fiction candidate**. Plan B (off-day corridor, zero PTO) open — original Space Coast plan qualifies as-is. | [BIRTHDAY-2026.md](BIRTHDAY-2026.md) |
| **§N Interaction Economy** | ✅ Researched + distilled 2026-08-16. Principle 8 rescinded, niche selection reopened (ledger 11), practice productization tabled (ledger 12). | [ULTRASIN-interaction-economy.md](ULTRASIN-interaction-economy.md) |

---

## ✅ Moved 2026-08-21 (evening session)

- **DOCTRINE 0 drafted** — [DOCTRINE-0-INVARIANTS.md](DOCTRINE-0-INVARIANTS.md): the invariants about invariants. Seven meta-rules (earned-not-declared · written-only · names-what-it-forbids · holds-at-every-scale · names-derivation · few · dies-by-countermand), census of the existing invariant corpus (8 locations federated), rename ruling open (**Standing Order** recommended over Law / Non-Negotiable / Keel; schema fields hold until decision #3 propagates). Awaiting ratification.
- **MCDP acquisition executed** — twin-track ledger 3 approved. 4 of 11 PDFs landed in `Desktop\_BVX_INBOX\mcdp\` (Warfighting · Campaigning · Tactics · Planning, all verified); remaining 7 need a browser grab (marines.mil blocks scripts; archive.org degraded). Take ID block after BVX.1107 on catalog.
- **Sit rep format ruled** — "set me up" retired, **"sit rep"** is the trigger; board now delivers three time-sorted blocks: Fresh Ten (recency + context + next step) → **The Ancients** (staleness tiers) → Deep Stacks (volume).
- **PMCS category created** — personal readiness (medical/dental/life-admin) is its own block in STATE and in every sit rep, never mixed with projects. Seeded from the journal: dental call (retainer — specialist to confirm, ortho vs perio) + PCP physical → sexual-health consult chain. "The operator is equipment."

## ✅ Moved 2026-08-21 (close-out)

- **Gluteal morphology taxonomy specced** → [_CANON_NODES/L2b-morphology-gluteal.md](_CANON_NODES/L2b-morphology-gluteal.md). L2b MORPHOLOGY is no longer unspecced — its first module is done. Contreras's causal mechanism extracted from the 996-page *Glute Lab* text (ilium width × femoral neck × trochanter prominence = 27 cells), extended into **two sexed taxonomies, thirteen named types**, architectural naming register. Three views: character-generation, aesthetic IP, training targets. Hip dips named as a positive type (`The Corbel`) rather than a defect.
- **Push status corrected** — the archive is public; the stale warning in this file was removed. New blocker #0.
- **Multi-instance answered:** yes, multiple Claude Code sessions run concurrently; same filesystem and memory, so use git worktrees for genuinely parallel work and expect autocommit to interleave.

---

## ✅ Moved 2026-08-19/21

- **Wear/training program designed** (in-chat, distill to registry §G next): PNF session card, 4-part size-up gate + half-inch increment rule, weekly split (4 wear work-days / stretch day / prostate days / 1 hard rest day), Topped Toys shortlist verdicts (Tail Raiser = work plug · Mare Maker = stretch tool · Grip = 2nd rotation · Breaker = dildo, not wear), gym traffic-light (no plug under Valsalva). High-volume recovery architecture + PCP consult list (PrEP · DoxyPEP · site-specific panel · anal Pap · pelvic-floor PT referral).
- **Kata rename pending** — 10 candidates delivered (RINGCRAFT recommended); Papi hasn't ruled. Registry strike-through waits.
- **Germany field month ideated** — verdict: **September, Folsom Europe as anchor** (only month where the full mild→extreme ladder overlaps the international calendar); solo-contact infrastructure mapped (PlanetRomeo, Recon, Telegram, Folsom volunteering, munches); $8–10k disciplined / $12–18k definitive. FKK double-meaning trap documented. **Fold into [BERLIN-PIVOT.md](BERLIN-PIVOT.md) next session.**
- **US circuit ladder ideated** — IML Chicago (late May) = the anchor answer; the ladder: FLL Oct → MAL Jan → CLAW Apr → IML May → Folsom Europe Sept. Preference-matched alternative: Atlanta Black Pride (Labor Day). Florida-month composite (Wilton base + Key West week, Wicked Manors anchor) named best ground-only month. Leather/protocol entry: **Thebans MC (Miami, 1975) · Florida Leather Week · Mr. Eagle contest at Eagle Wilton Manors** — October trip is the doorway.
- **Leather/sling/Germany curriculum delivered in-chat** — Route E material (Rubin, Hirschfeld institute lineage, sling-as-architecture thesis). Candidate for BVX-LEARN distill.
- **Pyramid Principle audit** — book NOT in any library (0/1,106); already ratified as BVX doctrine (Feb 2026 four-domains artifact: answer-first documentation + MECE). Third recall loop closed. **Acquisition → BVX.1107 candidate.**
- **Z-lib cross-reference pipeline built** — walker script saved to [`_tools/zlib_favorites_walker.js`](_tools/zlib_favorites_walker.js); drop zone `Desktop\_BVX_INBOX\zlib\`; parser + fuzzy-diff vs catalog.json on standby. **Awaiting Papi's export run.**
- **Birthday RULED OFF (2026-08-21)** — Plan A cancelled, no PTO in new-job months. File → shelved project + **BLACK/ORANGE fiction candidate** ("the researched trip that never happened"). Plan B = off-day corridor, zero PTO; original Space Coast plan qualifies as-is.
- **Twin-Track Doctrine consolidated** — [BVX-ULTRASIN-twin-track.md](BVX-ULTRASIN-twin-track.md): three-layer sort (brand=imprint · ops=BLACK/ORANGE dual-track, already running · legal=OPEN), June 8 BVMC rediscovery, Feb 9 Marine standard confirmed canon, MCDP acquisition queue, firm-isomorphic-to-OXO rhyme recorded. **Ancient #2 now has prepared ground; ruling remains.**
- **To-do added:** orthodontist call (retainer advising).

## ✅ Moved 2026-08-19/20

- **Birthday RULED: Plan A locked** — Cabanas Guesthouse & Spa, Wilton Manors, **Mon Oct 5 → Tue Oct 13 (8 nights, gold window)**. Full-experience checklist + day grid + venue playbook in [BIRTHDAY-2026.md](BIRTHDAY-2026.md). Last gate: PTO. BBRT profile drafted in-chat (fill-ins pending).
- **Kobra S1 BOM promoted to live** — [KOBRA-S1-BOM.md](KOBRA-S1-BOM.md) (BVX-BOM-0001 v1.1, color specs locked: black/gray/OD green) + xlsx/csv twins at root. Phase 1 = $137, ready to order. SlimeVR line now has a live artifact.
- **MAsT: [CITY] pathway mapped** — 12–18 month sequence (Oct FLL recon → visit chapters → munch first → co-found → petition). Contact: membership@mast.net. Route E ethics line drawn: confidential rooms are never material.
- **Rail-month ideation banked** — Crescent line (DC→ATL→NOLA) + USA Rail Pass format, 3-tier manifest priced ($4.5k / $10k / $25k). Ideation only, per Papi.

## ✅ Moved 2026-08-16

- **Ride-gear taxonomy logged** — [ULTRASIN-ride-gear.md](ULTRASIN-ride-gear.md): 6 tiers (powered saddles → Marius stool), clear-chair/camera argument, folding-chair fixes (rug pad, zip-tied braces), taper-vs-wide resolved as two setups. Purchase order unruled; folds into OSSM consult.
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
