---
title: STATE — what is live right now
type: state
status: living document
updated: 2026-09-06
read_first: true
---

# STATE

**This is the answer to "what have we been working on."** Read this first, every session, before anything else. The ranked project board lives in [PROJECTS.md](PROJECTS.md).

> **Challenge:** *"Americans are not born. They are forged in the chaos and dysfunction of American life."*
> **Countersign:** *"The Asset is acquired. The Noise is archived. The Feed is stable."*
> → then the board. Equivalents: "sit rep" · "where did we leave off" · "the board".

**Session-open reading order ([SOP.md](SOP.md) §4):** SOP.md → this file → [BOLO.md](BOLO.md) (watchlist) → `_CACHE/` (Ready Rack — flush to `_LOG/` on sit rep) → [PROJECTS.md](PROJECTS.md). All comms codes (sit rep · Oscar Mike · how copy · BOLO capture · **boresight** · break-break/buttonhook back · ivory tower · ENDEX) are canonical in SOP.md, house format included (§7).

**Autosave is on.** A Stop hook (`_tools/autocommit.sh`) commits every change to git when a session ends. Local only — it never pushes. Run `git push` yourself when you mean to publish.

It is an **index, not a store**. Detail lives in the registries below; this file says what's live, what moved, and who's blocking. If it's not here, it isn't active.

> **The rule, inherited from the Ultrasin registry:** chats are working memory, not storage. If a decision isn't written down, it does not exist. Every session that locks a decision or builds a system ends by updating this file.

---

## 🔴 Blocked on you

Nothing moves on these until you rule. Ordered by what they unblock.

| # | Decision | Unblocks |
|---|---|---|
| **8** | **The 03/03 domain numbering** — `03_SETTING_SYSTEMS/` (stood up 8/25) vs pre-reserved empty `03_PLOT_SYSTEMS/`; `04_STYLE_GUIDES/` also reserved. One rename either way | plot_systems' home; clean SSOT numbering before the L4 deepening lands |
| **10** | **D-9 — the BOLO 24 boresight HOLD converted 2026-09-04 and has no call yet.** Three legal answers under the flow: clear delivery · re-hold with a date · NO-GO. D-5 nut · D-6 frame · D-7 mother/year · D-8 refs · D-10 intent · D-11 lane ride with it | the studio design pass; the flow's own hold rule (an undated hold is the stall pattern) |
| **11** | **BOLO 29 — confirm the reward-vs-risk reading and clear delivery.** Research banked `_PRIVATE/BOLO-29-research.md` | the three-way ranking 24 / 27 / 29 and the 90-day ballpark |

> **#9 (BOLO 19 history) RULED + EXECUTED 2026-09-01: re-pass + force-push, Papi's hand on the trigger** (the permission layer required it — twice-blocked classifier, by design). Scope grew on prep: the batch scan found **1,064 historical blobs** with numeric coords (vs the 193-file tree count), three formats (quoted/unquoted JSON + YAML). Blob-callback pass over all history → **verified zero** (2,686 objects) → force-pushed → remote spot-check serves `[COORD]` only, old SHAs 422. Backup: `Desktop/_setsunadev-PRE-REPASS-2026-08-31.bundle` (never commit). Runbook preserved: `_PRIVATE/repass_2026-08-31/`. **BOLO 19 closed; BOLO 8 ticket now covers both strip layers in one filing.**
>
> **R1 (strip residue — class: personal ad + city pin) RULED 2026-09-03: keep all three, accepted residue.** Found on the ancients pass: `NSA.md` (a personal ad with neighborhood, body, and role) in `_ARCHIVE/XX_2025.01_MCMARI_BUILD/` and in the active `_2025.02_SELACIOUS_BUILD/`; the `[CITY]` token defeated by county / neighborhood / university names across ~30 tracked files (Leon County 6 · Killearn 3 · FAMU 19 · Apalachee 6 · Bradfordville 3 · Maclay, Klapp-Phipps, Lake Jackson, Crowder in one); the 6/16 discreet-outdoor-spots conversation surviving the 24-conversation removal. Papi's ruling: nothing deleted, nothing redacted, no ticket-scope change. Recorded so the finding is not re-derived.
>
> **#7 (the corpus floor) RULED 2026-08-31: 512** — coverage over cut, after the quarantine walkthrough; supersedes the provisional 768 (taxonomy-engine ruling 11). Quarantines only the <512 tail (933 images, 1.4%) + 337 unreadables; keeps ~65,600. **Stage 1b–d LAUNCHED same session** (hash → dedupe-cluster → quarantine → normalize; resumable pipeline at `_PRIVATE/taxonomy_engine/stage1.py`, all checkpoints in the corpus `_pipeline/` folder). Next human touch = the Stage 3 VERDICT pass.
>
> **#3 (schema propagation) EXECUTED 2026-08-24 (engine session):** `armor_index` · `satisfaction_cycle_truncation` · `erotic_safety_precondition` · Expressive Range + the `mc_problem_element` rename written across the vertical slice, integration protocol, ingest template, and both variable registries. **The Blocked table is empty for the first time.**

> **#0 (repo exposure) RULED + EXECUTED 2026-08-24: strip in place, repo stays public.** History rewritten (all 329 commits), force-pushed same session — record in the STRIPPED IN PLACE section below. Follow-ons = BOLO 8 · 9.
>
> **#1 (the storyform) RULED 2026-08-24 — every creative decision closed in-chat:** [_CANON_NODES/oxo-storyform.md](_CANON_NODES/oxo-storyform.md). Dynamics: Change · Stop · Do-er · Linear · Action · Optionlock · **Failure/Good**. Residue = ~30-min engine-verify pass, **BOLO 7** — zero decisions in it.
>
> **#2 (Impact Character) RULED 2026-08-24: Anna Colson Conway** — BVX.0064 derivation confirmed; **RS = Tori↔Anna** in Activity.
>
> **#4 (`motivation_element`) RULED 2026-08-24: renamed `mc_problem_element`, holds the MC Problem (Equity)** — `Consider` relocates to the extended sub-table; execution rides #3.
>
> **#5 (the fused school name) RULED 2026-08-24: the Delta Coast Ultra School — "DCUS"** — cleared from this table; record in [_CANON_NODES/delta-coast-ultra-school.md](_CANON_NODES/delta-coast-ultra-school.md).
>
> **#6 (BVX↔Ultrasin firewall) RULED 2026-08-24: subsidiary** — cleared from this table; record in [BVX-ULTRASIN-twin-track.md](BVX-ULTRASIN-twin-track.md).
>
> **Leverage check** ([PROJECTS.md](PROJECTS.md#the-same-ten-ranked-by-leverage)): #1 is now the only entry with a whole trunk behind it — the BLACK release, one Dramatica afternoon. The money track's structural blocker is cleared; **launch now waits on performer handle + commentary register + legal-docs execution (Ultrasin ledger #3 · #4 · #10).** The other four are propagation work that follows #1.

---

## 📋 The watchlist → [BOLO.md](BOLO.md)

Active BOLOs + the PMCS readiness table live in their own capture-fast file. Sit rep Block IV. Protocol: [SOP.md](SOP.md) §1 — spoken taskings are written there the turn they are spoken.

---

## ✅ STRIPPED IN PLACE — #0 ruled + executed 2026-08-24

**Papi's ruling: the repo stays public, period; sensitive content stripped from the working tree and from every commit.** Executed same session — five `git filter-repo` passes over all 329 commits, force-pushed to `origin/main`. Backup of the pre-strip history: `Desktop/_setsunadev-PRE-STRIP-2026-08-24.bundle` (all refs, 214MB — **never commit or push it**).

**What came out (all four classes, ruled via manifest):**
- **Geolocation** — ~1,400 Joplin/Obsidian frontmatter lat/long/altitude lines + the home-fix coordinate + one Logseq coord pair. Zero in tree, zero in history.
- **The third party (cc)** — name redacted to `[CC]`/`[CC-HANDLE]` everywhere; **24 conversations removed** (the interpersonal set, the OSINT set, medical/substance/mental-health) plus `projects/cc/`, five cc-centric generated files, the MBFF OSINT report + its generating conversation, `godhates._.cece.txt`, and the `## cc` section of PROJECT-MEMORIES. Originals preserved locally in `_PRIVATE/stripped-2026-08-24/`.
- **Employer / school / city** — redacted to `[EMPLOYER]` / `[SCHOOL]` / `[CITY]` in content and filenames (incl. `fsu.edu` URLs → `school.edu`).
- **`_tools/scan_sensitive.py`** — removed from repo + history (its patterns necessarily contain the real names); lives on locally, gitignored.

**Verified on the remote:** removed paths 404 · old filenames 404 · STATE.md shows `[CITY]` with zero real-city hits · Joplin files carry no latitude · pre-strip commit SHAs no longer resolve via the API. Archive INDEX rebuilt (295 conversations, 11 projects), dead rows dropped.

**Accepted residue (in scope, by ruling):** the `leechseed` handle (it's the account) · "Papi" as address · ~60 emails (mostly service/own) · researched-business phone numbers · benign `fsu`/`FSU` substrings inside vendored binaries · whatever crawlers cached during the 8/19–24 public window. **Follow-ons: BOLO 8 (GitHub Support purge ticket) · BOLO 9 (Google outdated-content removal).**

The 2026-08-16 **scrubbed-mirror design is superseded** by the in-place strip. Still standing: the **pseudonym codebook as a fiction device** (roman à clef, real → in-world entities) — the `[CC]`/`[CITY]`/`[EMPLOYER]` markers are its placeholder layer, ready to be replaced with in-world names when the codebook lands.

---

## 🟡 Live

### BLACK — creative, IP, systems

| System | State | Where |
|---|---|---|
| **THE STORY LATTICE** | ✅ **Built 8/25–26, COMPLETE** — IP-agnostic story-creation system, The Outliers = test bed (ruled). Spine (comparative tree, 14 rivals) · Scale Ladder (8 rungs) · Setting System (12-layer slice mirroring the character stack; **new domain `03_SETTING_SYSTEMS/`**; DCUS instanced; SCENE CARD) · Texture (Ten Questions, TELLING PROFILE) · Medium Grammars (10 contracts) · constraint layer (invariants) wired throughout. Module 5 (collision engine) parked decision-free → BOLO 17. Rulings queue in the 8/26 session note. | `01_NARRATIVE_FRAMEWORKS/` + `03_SETTING_SYSTEMS/` |
| **OVEREXITOUT / The Outliers** | Tori node built, L9 AUTHORED. **8/24 evening: storyform CANON v2.0 (§9 rotation ruled, BOLO 7 done) · IC = Anna · school = DCUS.** Ripple: Tori node's Structure table pre-rotation, reconciliation pending. **8/26: DCUS setting slice instanced; OXO Telling Profile identified as open decision set (fires when prose opens).** **9/6: Trash Land region seed** ([oxo-trash-land-seed.md](_CANON_NODES/oxo-trash-land-seed.md)) — the Spiral's rim, seven rulings open. | `_CANON_NODES/` |
| **Character system** (Dramatica × astrology × 12-layer) | Validated 11/11 layers. **8/24 evening: BOLO 7 done + #3 propagated — the schema fork is closed.** Remaining: reconcile Tori's Dramatica cells to the §9 rotation; armor_index scale-class. | `ShroomsQ/_CANON/_SSOT/02_*` |
| **Bold Venture Design System** | ✅ **v2.0.0 — THE ROSTER RULED 2026-09-01.** The brand color layer locked: ROSE anchor #8A1F44 + FLESH (shadows through the rose) + rose-cast grounds + gold in core. Four registers: **EMBER** (all-hours ambient) · **PUNCH** (live edge, time-boxed) · **DUST** (daylight) · **NOIR** (night default). The Luminance Law (warm = light, never pigment on skin) · one-red ledger · adhesive rule + rose quota · surface map labels→buildings. 11-palette challenge bench adjudicated; 4-lens panel wf_5b0af08b-c49. Board: `Desktop/BOLD-VENTURE-PALETTE.html` | `00_EPISTEMOLOGY/📐 ssot_00_bold_venture_design_system.md` |
| **MCDP one-sheets MIL.01-MIL.11** | ✅ **BUILT 2026-09-03** from the eleven PDFs (BVX.1111-1121); each carries an APPLICATION section mapping doctrine onto the project flow and the prowords. Supersede the Dec-2025 Joplin summaries (unreliable, see Known rot) | `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/` |
| **Markdown marking SOP + VOCABULARY register** | ✅ **RULED 2026-09-06** (BOLO 32 / 31) — bold = writer · `==highlight==` = reader (load-bearing terms) · harvest tool `_tools/vocab_harvest.py` → per-source `_vocab/<ID>.vocab.md` + `_meta/VOCABULARY.md`. MIL.01 harvested (62 terms); reading resumes at HEURISTICS. End state = **BOLO 33**, the MCDP browser (CK3-derived information architecture) | `05_OPERATIONS/📐 ssot_05_operations_markdown_marking.md` |
| **BVX-LEARN** | v3 spec recovered + decisions locked. **1,120 sources indexed** (MCDP intake 9/3: `BVX.1111`–`1121`, the eleven doctrinal pubs; one-sheets `MIL.01`–`MIL.11`), classifier 99%. Next free `BVX.1122` (`1107` reserved, Pyramid Principle). | `_0.1_BVX_LEARN/_meta/` |
| **THE PROJECT FLOW** (working title) | 🟡 **v0.1 WRITTEN 2026-09-03** (BOLO 25) - how a project runs here: six event-gated phases · the eleven-section brief · the gate (GO / NO-GO / HOLD with a named blocker, decider, and conversion date) · instruments mapped to existing files · prowords as the control system · S/M/L tailoring · DOCTRINE 0 as promotion mechanic. First live instance: BOLO 24 brief. Promotes to canonical after two uses | `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_project_flow.md` |
| **The narratology shelf** | ✅ **PROMOTED 2026-09-03** (the ancients pass) — 109 framework distills (UID-keyed, Tier 1–4 × 21 competencies, 15 wicked/craft) + the UID index + 31 competency one-sheets + the General Model propositions P1–P8 + the Rulebook draft, recovered from the archived 1.04 build. **Supersedes the BOLO 18 stage-1 “craft shelf 0.6% distilled” finding.** Stage 2 keys these first (provisional `feeds: SPINE.Lx` map in the shelf index) | `01_NARRATIVE_FRAMEWORKS/_narratology_shelf/📐 ssot_01_narratology_shelf.md` |
| **Modern Poetics** (was: Leechseed Manifesto) | ✅ **CANONIZED 2026-08-31** — the oldest True Ancient integrated: 16 docs (record said 10) dispositioned 7-canonize/9-fold, ratified; **+ 3 native checks coined same session (P8 Fantasy Drive · P9 Sexy Check · P10 Aesthetic Check)**. The lattice's prescriptive half. Application pass = BOLO 21; DOCTRINE 0 entry deferred | `01_NARRATIVE_FRAMEWORKS/📐 ssot_01_modern_poetics.md` (sources stay in imported-Joplin) |
| **L2b MORPHOLOGY** | Designed this session, unspecced. Frame → Tissue → **Condition** → Line → Archetype. | — |

### ORANGE — venture, body, sexuality

| System | State | Where |
|---|---|---|
| **Zero-budget launch — 3D erotica stills (Blender × DARKROOM)** | 🔴 **CAPTURED 2026-09-03 → BOLO 24.** The Amazon job fell through; Papi unemployed as of 9/3. Start now on what is in hand — $0 base, $100–200 stretch. Design pass staged, fires on go. The "new-job standing" assumption (Birthday shelving) no longer holds. | [BOLO.md](BOLO.md) #24 |
| **ULTRA DARK (BOLO 27) + the video engine (BOLO 28)** | 🟢 **Day 1 done 9/4** — 2,499 studio scenes flagged, UD pool 2,111, kit at `Q:un\_ULTRADARK\`, THE CUT method doc. Walkthrough parked at **Block C**: Papi marks 12–16 clips → "marked" → pull → Resolve → the 12-second blurb. **The main effort.** | `oscar-mike/ultradark-walkthrough.md` · `_PRIVATE/ULTRADARK-*.md` |
| **Ultrasin venture** | Full registry v0.1, 32-chat sweep. **Firewall RULED 8/24 (subsidiary)** — launch blockers now handle · register · legal docs. | `_CLAUDE_ARCHIVE_2026-08-15/files/2026-08-05_ultrasin-master-registrymd.md` |
| **Primed Protocol** | ✅ Documented today. Ledger item 8 closed, §H 🟡→🟢. | `Desktop/ULTRASIN-primed-protocol.md` |
| **GDP-1 BOOTYCAMP** | P1 ready to run. Gate out = 60-second squeeze hold. | Registry §G |
| **Erotic Range** | ✅ Live, phone-ready, two profiles, local-only. | `Desktop/erotic-range.html` · [artifact](https://claude.ai/code/artifact/c78a1e6a-1f43-467b-a74e-7e7e66df41c1) |
| **Bongobabe** | ✅ **Stood up 2026-08-25.** NSFW clicker/idle companion (Bongo Cat × e-girl: input-reactive pet, clicks → part upgrades). Registry v0.1 written; BOLO 10 staged for v0 build; first swing = art-style test. | `Desktop\BONGOBABE\` — **outside this repo**, local git, no remote |
| **Taxonomic-aesthetic practice** | Practice-first. Engine-vs-voice fork asked in June, never answered. | Registry §L |
| **Manufacturer watchlist** | ✅ Stood up 2026-08-21. Dildo/toy makers to track, sourced via X. 11 entries — indie artisan → mass-market → machines. | [ULTRASIN-mfg-watchlist.md](ULTRASIN-mfg-watchlist.md) |
| **Resource watchlist** | ✅ Stood up 2026-08-21. Industry education/tools/advocacy, sourced via X. First entry: SexWork CEO (feeds §N). | [ULTRASIN-resource-watchlist.md](ULTRASIN-resource-watchlist.md) |
| **Physique watchlist** | ✅ Stood up 2026-08-30. Glute-dominant physique figures — stage pros → influencers → trans lane → victim files. 25 rows, X/IG verified per row (3-agent sweep); scene is IG-primary. Parent doc (glute-enhancement reference guide, professional lane + worst side) **Oscar Mike'd 2026-08-30** → [oscar-mike/glute-reference.md](oscar-mike/glute-reference.md), scope locked, zero open decisions. | [ULTRASIN-physique-watchlist.md](ULTRASIN-physique-watchlist.md) |
| **Birthday 2026** | 🔴 **SHELVED 2026-08-21** — Plan A cancelled (no PTO, new-job standing). Research preserved as revisit-project + **BLACK/ORANGE fiction candidate**. Plan B (off-day corridor, zero PTO) open — original Space Coast plan qualifies as-is. | [BIRTHDAY-2026.md](BIRTHDAY-2026.md) |
| **§N Interaction Economy** | ✅ Researched + distilled 2026-08-16. Principle 8 rescinded, niche selection reopened (ledger 11), practice productization tabled (ledger 12). | [ULTRASIN-interaction-economy.md](ULTRASIN-interaction-economy.md) |

---

## ✅ Moved 2026-09-04→06 (sit rep · the TikTok boresight · Trash Land · the verb kit · the marking SOP)

- **9/4 sit rep** on the 9/3 marathon note (flushed). DARKROOM found down at open (relaunch on proword); Stash live. Main effort named: the first ULTRA DARK blurb (Block C "marked"). **D-9 came due** → Blocked #10.
- **BOLO 29 captured + boresighted** — the SFW TikTok channel: owned Fortnite skins doing the emotes (the TikTok dances), faceless, **BLACK**. Ruled on the loop: 60 s+ stitched for Creator Rewards · 90-day horizon · rank vs 24/27 on reward-vs-risk · audio = Claude's call. Research banked `_PRIVATE/BOLO-29-research.md` (rights green w/ caveats · Replay mode over UEFN Sequencer · CRP a day-60–90 unlock · creator code the early lever · lane crowded · 90-day money LOW-confidence). **HELD** → Blocked #11.
- **BOLO 30 Trash Land** — region seed for the ASTRO7EX / Outliers world: the man-made trash DMZ between the southern and northern US, mountain-range scale → [_CANON_NODES/oxo-trash-land-seed.md](_CANON_NODES/oxo-trash-land-seed.md), full 12-layer setting slice (instance #2 after DCUS). Read: the rim of the Spiral; the archive of Noise. Name bench (recommend *The Midden*); seven rulings open (who built it · what the North is · what is in the pits).
- **The verb kit** (Oscar Mike'd): argument-structure KB v2 · the 3-question tree + Mermaid · the quiz artifact *Transitive or Not* (24 items, TRANSITIVE / INTRANSITIVE). Lesson to memory: Papi-facing learning tools are the sentence and the buttons.
- **BOLO 31 + 32 DONE, 33 seeded.** MIL.01 read-through: 63 reader bolds → `==marks==` (template bolds untouched), harvested by `_tools/vocab_harvest.py` → `KNOWLEDGE_AREAS/_vocab/MIL.01.vocab.md` (62 terms, sense-in-source + sentence) + `_meta/VOCABULARY.md` (register). **📐 markdown marking SOP v1.0.0 RULED** (bold = writer · `==highlight==` = reader · `_italic_` = captions · `[[wikilink]]` = promoted; Prettier-safe); writing-guide pointer added. **BOLO 33** = the MCDP browser, MIL.01–11 with CK3-derived information architecture (seed, Lattice Navigator lineage). Read-through parked at HEURISTICS → `oscar-mike/mil01-readthrough.md`.
- **Discord intros** parked 9/4 (four drafts, none sent). SOP: "belay that" provisional; §7 rule 8 one-value-one-block (9/4).

## ✅ Moved 2026-09-03 (the ancients pass — archive-or-keep RULED, R1–R5)

- **Later 9/3 — the unemployment session.** Amazon fell through → **BOLO 24** (zero-budget ORANGE launch: 3D erotica stills, Ultrasin as the studio, first-signing persona) boresighted over four transmissions; walked state in `_PRIVATE/BOLO-24-studio-launch.md`, benchmark research banked beside it, **delivery held**. **BOLO 25** (the standard PM flow) captured; PM holdings survey banked (`05_OPERATIONS/📐 ssot_05_operations_pm_holdings_inventory.md`) — finding: the six-phase lifecycle already exists (Feb-2026 four-domains artifact) and all 11 MCDP summaries exist in the Joplin import. **Papi RULED: hold his order** (PDFs → MCDP project → template → BOLO 24); home = 05_OPERATIONS. **DOCTRINE 0 RATIFIED** (rename still open). SOP gained §2 house names (BLACK = Bold Venture · ORANGE = Ultrasin) and **§8 the dictation codebook**. PMCS: Employment row added.
- **Late 9/3 → 9/4, the same session (ran to ~03:00).** **BOLO 25 stages 1–4 DONE:** all 11 MCDP PDFs landed + catalogued `BVX.1111`–`1121` (BOLO 1 closed) · **one-sheets MIL.01–MIL.11** built from the PDFs (the Dec-2025 Joplin summaries proved unreliable → Known rot) · **THE PROJECT FLOW v0.1** written (`05_OPERATIONS/📐 ssot_05_operations_project_flow.md`) · applied to BOLO 24 as `_PRIVATE/BOLO-24-charter.md` (ledger D-1..D-11; boresight = D-9 HOLD converting at next sit rep) · parked (Oscar Mike). **BOLO 26** (dictation dictionary) parked on the route ruling. **BOLO 27 boresighted + RULED:** the gooner curation account runs as **ULTRA DARK**, an imprint under Ultrasin — the studio's credited taste-layer *funnel*, never the asset (§N + registry §E rulings surfaced); rating scale + written line on every post; commissioned edits = first-dollar line; bridge both lanes; personal content stays on its own account. **BOLO 28 DAY 1 DONE:** the video engine inside Stash (15,492 scenes / 6.9 TB) — 399 dupe groups tagged, **2,499 StashDB-matched scenes tagged `⛔ studio-content`, 416 studios named**, saved filter `UD pool` = 2,111 clean five-stars. **Production kit built:** `Q:\fun\_ULTRADARK\` tree · THE CUT method doc · Stash→Resolve pipeline (pull script + in-Resolve timeline builder + bpm tool). **Walkthrough:** Blocks A (Resolve) + B (the song, 123 BPM) done; **parked at Block C** → `oscar-mike/ultradark-walkthrough.md`. SOP: "belay that" provisional · §7 rule 8 one-value-one-block. DARKROOM launched on proword (still serving at close).

- **`_ARCHIVE/` stood up at root** ([INDEX](_ARCHIVE/INDEX.md) · README carries the rule: archaeology only, promote-then-park, nothing deleted). **Seventeen folders moved in** (R4 · R5): the seven-build lineage BELLE → EMIWU → MARIMARI → GOONIRU → BUNNIRU → 1.04 → MCMARI · `_broodengine` · `_grognard` · `_cake` · `_operations` · `football_qb_training` · `WORLDBUILIDNG THROUGHLINGE` · `split_files` · `hugo-dramatica-draft-v1` (submodule path updated in `.gitmodules`) · `_dramatica_OXO_builds` · `_DIRECTORY OF DIR`. 1,982 tracked files, 39 MB. The `X_`/`XX_` prefix convention is superseded by the folder. README + PROJECT_BRIEF re-pointed.
- **The hash pass on the lineage:** cumulative through 1.04, then MCMARI restarted; six of seven builds carry nothing the next lacks. **R3: 1.04 stands alone** — UID coverage check found 0 frameworks unique to BELLE/EMIWU/1.02, 16 unique to 1.04.
- **THE NARRATOLOGY SHELF PROMOTED** (see Live) — the recovered 2024 curriculum, 165 files / 2.1 MB, at `01_NARRATIVE_FRAMEWORKS/_narratology_shelf/`. The house already held ~110 finished framework distills under an archived prefix; the 0.6% craft-shelf stat is superseded.
- **Four more keepers promoted:** the three Bermuda Quadrilateral / Krebs Cycle essays → **BVX.1108–1110** (`DSN`; next free `BVX.1111`, `1107` reserved for the Pyramid Principle earmark) · the 2024 styleguide + naming conventions → `05_OPERATIONS/📐 ssot_05_operations_legacy_styleguide_2024.md` · the two film lists (2023 FUZZ + 2024 `_cake`) merged → [`_CANON_NODES/film-register.md`](_CANON_NODES/film-register.md) (123 titles, **40 on both lists = the stable core**) · the moon-societies list + the Civ V table → [`_CANON_NODES/moon-saga-seed.md`](_CANON_NODES/moon-saga-seed.md) (a separate IP, MOON/SAGA, not The Outliers; fabula in the archived `_g-on_dir`).
- **R2: GUTS99 RETIRED.** Ten unfilled stubs since Jul 2025; the twelve subsystem coinages carried into BOLO 15 as the media-type register. For design time: the three source docs disagree (10 vs 12 subsystems; LUSTRA = porn vs visual art). 2024's “GUTS99” was the doc-site name for the narratology curriculum — a different thing under the same name.
- **R1: the strip residue ruled** (see the Blocked notes) — keep, accept, no scope change.
- **Housekeeping surfaced, not acted on:** `yolov8n.pt` (6.5 MB) committed at the public repo root 8/31, duplicate of the gitignored copy in `_PRIVATE/taxonomy_engine/`. → Known rot.

## ✅ Moved 2026-08-26→31 (the post-lattice stretch — collision · sweeps · the leak · the census)

- **THE COLLISION ENGINE BUILT** (BOLO 17 ✅, same day it parked) — `📐 ssot_01_collision_engine.md`: four classes, contact vocabulary, **Tori×DCUS twelve-row proof** (7 hot rows = the M2–4 scene menu; the L9×S9 trine-as-trap; row 6 re-derived the economic-tracker beat; S2 gap surfaced). Next proof: Tori×Anna, needs Anna's chart.
- **THE LATTICE NAVIGATOR + CODEX shipped** — one artifact, four versions; ruled skin: CK3 UX × Death Stranding UI; ~110-term searchable Codex. `LATTICE-NAVIGATOR.html` at root. Parked.
- **The spine breadth pass** — SETTING TOUCHPOINT MAP (entity-stays ruling, explained elementary) + THE BRANCHES (8 levels × first sub-layer × starter shelves) in the spine doc; **BOLO 18 stage 1 ✅** (house inventory doc; findings: the 03/03 collision → decision #8; craft shelf 0.6% distilled).
- **⚠️ Strip remnant found + tree-fixed (BOLO 19)** — 194 longitudes + 6 full coordinate pairs survived 8/24 in Joplin sync metadata; all redacted 8/26, repo-wide verify zero. History/push = decision #9.
- **The Drop captured** — `_CANON_NODES/oxo-the-drop-seed.md`; **tone RULED: 007/Kojima blockbuster sincerity**. The 2023 **FUZZ intertext tree found** (films + anime lists = the tone register's canon); promotion unruled.
- **The corpus pipeline** — BOLO 13 ✅ (pull done 8/27: 24,310) · `_manual\` intake conventions ruled by use · **BOLO 14 FIRED 8/30: Stage 1a census done — corpus 66,892 images**, 9.2% below floor → **decision #7 gates Stage 1b**.

## ✅ Moved 2026-08-25/26 (the lattice session — the story system built end to end)

- **THE STORY LATTICE BUILT AND COMPLETE** — five canonical docs delivered on walked-down boresight chains, all IP-agnostic (**test-bed doctrine ruled: the lattice creates ANY story; The Outliers is the guinea pig**): the **Spine** (comparative tree — Dramatica canonical, 14 rivals mapped to BVX holdings, `feeds: SPINE.Lx` keying) · the **Scale Ladder** (beat→universe, completion tests, containers-vs-threads, 4 series patterns) · the **Setting System** (**`03_SETTING_SYSTEMS/` stood up**; 12-layer SETTING SLICE mirroring the character stack layer-for-layer; SCENE CARD; **DCUS instanced as proof** — one gap: S2 WEATHER) · the **Texture Layer** (Ten Questions of the Telling; TELLING PROFILE; finding: OXO has none yet) · the **Medium Grammars** (10 channel contracts; M6–M8 scaffolds await BOLO 16).
- **The constraint layer wired** (Papi's break-break catch): narrative invariants = the prescriptive register over the whole lattice; enforcement rides the ladder's completion tests; S12 + scene card carry invariant fields. **Flagged: DOCTRINE 0 still awaits ratification; the Tenet/Ethos rename gate is OPEN (was gated on #3, which executed 8/24).**
- **The Collision Engine designed + parked decision-free** (Oscar Mike → `oscar-mike/collision-engine.md`, **BOLO 17**): generalized synastry — C×C (Cat 11 exists, unrun) · **C×S via the Lx↔Sx mirror diagonal** (new; Tori×DCUS proof staged) · C×Situation (Cat 13 transits) · C×Group. Architecture ruled: layer above entities, feeds back as overlays, time keyed to ladder addresses.
- **BOLO 13 rescued twice:** relaunched at sit rep, then **detached to Windows Task Scheduler** (`BVX_corpus_pull`) so it survives session close. **36,916 files in** (18,458 images) after ~22h of unnoticed runtime; remaining unknowable until the list end.
- **BOLOs 15–17 captured** (multimedia ingestion seed w/ TV Tropes distill ruling · medium-grammar research pass · collision engine). Full rulings queue + resume order: `_CACHE/2026-08-26.session.md` → `_LOG/` after next sit rep.

## ✅ Moved 2026-08-25 (the h-game session — Bongobabe stood up)

- **Bongobabe RULED + stood up as a total project** — the NSFW clicker/idle companion: Bongo Cat × e-girl, input-reactive pet, clicks → upgrades (toy-size ladder · act tracks · cosmetics). Name ruled (retired bench: Bongoguner · BongoWifu). Home: `Desktop\BONGOBABE\` — **outside the public repo**, local git, no remote. Registry v0.1 carries concept, loop, paper-doll chibi art doctrine, browser-v0/desktop-pet-v1 fork, six-item open-decisions ledger. **BOLO 10 staged** for the v0 build.
- **The h-game ideation board banked — eleven concepts, one ruled.** The other ten (BOOTYCAMP · The Trip That Never Happened · Circuit · The Field Guide · Rig · The Workshop · The Review Desk · Inheritance · The Archive · Field Month, bench: MAsT chapter sim) recorded in the session note, keepers unruled.

## ✅ Moved 2026-08-24 (the engine session — BOLO 7 · the rotation ruling · #3 executed)

- **BOLO 7 RUN — the engine resolved to ONE storyform**, every cell transcribed: [oxo-storyform.md](_CANON_NODES/oxo-storyform.md) §9. Exports archived beside it (`oxo-storyform-engine.dsf` + two report TXTs). **`mc_concern` corrected to The Past** — the chart nests Interdiction under Past; Interdiction vs. Prediction meaning untouched.
- **THE ROTATION RULED CANON — flag struck same session.** The form as entered rotates the morning's four domain assignments: **OS = Situation/The Past · MC (Tori) = Activity/Understanding · IC (Anna) = Manipulation/Developing a Plan · RS = Fixed Attitude/Memories.** Supersedes the morning domain ruling; storyform doc now v2.0. Engine's own poetry: Goal = The Past, Consequence = Memories. **Ripple pending:** victoria-midnight.md's Structure table still shows the pre-rotation frame (flagged in its frontmatter); the authoritative Dramatica ingest + handoff sources likewise historical.
- **#3 EXECUTED — the schema propagation, the last blocker cleared.** L9 v2 fields (`armor_index` 8 · `satisfaction_cycle_truncation` reach · `erotic_safety_precondition` control) + `Expressive Range` derived stat (Tori: 2) + the `mc_problem_element` rename, written across: vertical slice v1.1.0 · integration protocol v1.1.0 · ingest template v1.1.0 · both variable registries v1.1.0 (they already carried the rename from Phase 4). TRUTH_VULNERABILITY fires off `mc_problem_element` everywhere. Residue, minor: armor_index Base-60 scale-class assignment pending. Note: the vertical slice file carries a **read-only flag** — cleared for the edit, restored after.

## ✅ Moved 2026-08-24 (the strip session — #0 ruled + executed)

- **Blocker #0 RULED: strip in place, stay public — and EXECUTED same session.** Scanner run first per standing order (21,040 hits triaged; the critical kinds all false positives; the real leak was the home-fix coordinate ×~1,400 files + the cc identity lattice). Manifest locked at all four classes; five filter-repo passes; force-pushed; remote verified clean. Full record in the STRIPPED IN PLACE section above. **The Blocked table is down to #3 — the last standing decision.**
- **Execution intel worth keeping:** `--replace-text` skips binary-detected blobs (the Logseq `index.html` carriers) — a `--blob-callback` pass catches them; regex `\b` word-boundaries died in the callback command path (backslash mangling) — plain-bytes `replace()` or file-based rules are the robust forms; filter-repo hard-resets the working tree, so **uncommitted edits do not survive a pass** (bit us once: the scanner briefly got committed; caught pre-push, soft-reset, redone clean).

## ✅ Moved 2026-08-24 (the rulings session — firewall · school · storyform)

- **Blockers #1, #2, #4 RULED — the storyform session, the April stall broken.** Every creative decision in the OXO storyform closed in-chat: [_CANON_NODES/oxo-storyform.md](_CANON_NODES/oxo-storyform.md). Dynamics locked: Change · **Stop** · Do-er · **Linear** · **Action** · Optionlock · Failure/Good — the Personal Triumph shape. All four domains forced by the model: MC Situation · IC Fixed Attitude · OS Manipulation · RS Activity. MC Concern corrected to **The Future** (Interdiction vs. Prediction — "the system forecasts her; she intervenes"). **IC = Anna Colson Conway** (#2 closed); **RS = Tori↔Anna**, the rivalry as Activity. **`motivation_element` → `mc_problem_element` = Equity** (#4 closed; execution rides #3). Residue = **BOLO 7**, the ~30-min engine-verify pass.
- **Blocker #5 RULED — the fused school is the Delta Coast Ultra School ("DCUS").** Papi's directive: "Ultra School" in the title, Southern Gothic register; Delta Coast pick off an 8-name bench (bench retired in the node). "Ultra School" is canon by deliberate ruling — supersedes the old "UltraSchool isn't a repo term" correction, which stands for pre-ruling sources. Node stood up: [_CANON_NODES/delta-coast-ultra-school.md](_CANON_NODES/delta-coast-ultra-school.md). Provisional tissue recorded, unruled: Red Hills → DCUS as Bishop-acquisition rebrand · "Inner Spiral" reverts to geography · Ultra-School-as-class · Red Stick Creek stratum. Tori's remaining blocks: storyform (#1) + IC (#2).
- **Blocker #6 RULED — BVX↔Ultrasin firewall: SUBSIDIARY.** Ultrasin as child entity of BVX. Ruled against the §N lean (fully separate) with the ownership-chain exposure explicitly on the table — **risk accepted, not overlooked.** Brand layer stays imprint (no visible bridge); operational stays BLACK/ORANGE dual-track. **BVMC ruled doctrine-name only** — internal/fictional conglomerate frame, no legal entity carries it. Propagated: [BVX-ULTRASIN-twin-track.md](BVX-ULTRASIN-twin-track.md) (status + legal row + spawned decisions 1–2 closed) · registry §A 🔴→🟢 + ledger #1 struck · this file. **Launch chain now waits on:** performer handle (ledger #3) · commentary register (ledger #4) · FL LLC + attorney consult that papers the subsidiary (ledger #10).

## ✅ Moved 2026-08-21 (night session — watchlists)

- **Both ORANGE watchlists stood up** — [ULTRASIN-mfg-watchlist.md](ULTRASIN-mfg-watchlist.md) (26 makers, indie artisan → mass-market → machines/e-stim/prostate, X handles verified per row) + [ULTRASIN-resource-watchlist.md](ULTRASIN-resource-watchlist.md) (industry education/advocacy; SexWork CEO → §N). Sorting rule for mixed drops ruled; retailer/novelty entries flagged in-row. Notable intel: Funkit migrated to Bluesky; Bad Dragon's X is @bad_dragon not @BadDragonToys; four sites are fetch-opaque — X is the watch channel.

## ✅ Moved 2026-08-21→22 (night session — the lexicon session)

- **BORESIGHT ruled** — the understanding-check proword ([SOP.md](SOP.md) §1): readback → the read → clarifying questions only, no delivery until cleared, **only when spoken**. "Back-brief" struck; INTEL returned to the pool. Directed form: "boresight in on [target]".
- **Detour pair ruled** — **break-break** opens, **buttonhook back** closes; main thread restored unprompted.
- **"Ivory tower" coded** — academic mode: published literature only, cited inline, established vs contested marked.
- **House format coded** — SOP §7, after the readback-wall callout: bulleted readbacks · one-idea paragraphs · bold signposts · ten-second scan test. Grounded in the literature (NN/g F-pattern scanning, Cowan chunking, Mayer signaling/segmenting, Sweller load).
- **Trunk discipline coded** — SOP §2: every board item carries **BLACK / ORANGE / OPERATOR**; the board is never delivered trunk-blind.
- **Lexicon doctrine coded** — SOP §6: USMC vocabulary is the bootstrap library; native coinage intended; the house tongue bleeds into the culture. "Main effort" provisional (MCDP 1), Block VI rename rides its ruling.
- **BOLOs 4–6 captured** — **Focus doctrine** [OPERATOR] (staged: science + snap-in protocol + training; "The Zone" already in MSX.11/12/14; goalie layer own section; **fires on go**) · **Papi↔Claude interface** (docs are Claude's retrieval layer, conversation is the interface, prioritize speed) · **Transmission pedagogy** (v0.1 live as §7).
- **z-lib drop zone created** — `Desktop\_BVX_INBOX\zlib\` was missing despite the standby note; walker verified; parser fresh-builds at go. BOLO 2 still waits on the browser export run.

## ✅ Moved 2026-08-21 (evening session)

- **DOCTRINE 0 drafted** — [DOCTRINE-0-INVARIANTS.md](DOCTRINE-0-INVARIANTS.md): the invariants about invariants. Seven meta-rules (earned-not-declared · written-only · names-what-it-forbids · holds-at-every-scale · names-derivation · few · dies-by-countermand), census of the existing invariant corpus (8 locations federated), rename ruling open (**Standing Order** recommended over Law / Non-Negotiable / Keel; schema fields hold until decision #3 propagates). Awaiting ratification.
- **MCDP acquisition executed** — twin-track ledger 3 approved. 4 of 11 PDFs landed in `Desktop\_BVX_INBOX\mcdp\` (Warfighting · Campaigning · Tactics · Planning, all verified); remaining 7 need a browser grab (marines.mil blocks scripts; archive.org degraded). Take ID block after BVX.1107 on catalog.
- **Sit rep format ruled** — "set me up" retired, **"sit rep"** is the trigger; board now delivers three time-sorted blocks: Fresh Ten (recency + context + next step) → **The Ancients** (staleness tiers) → Deep Stacks (volume).
- **PMCS category created** — personal readiness (medical/dental/life-admin), never mixed with projects. Seeded from the journal: dental call (retainer — specialist to confirm, ortho vs perio) + PCP physical → sexual-health consult chain. "The operator is equipment."
- **SOP stood up** — [SOP.md](SOP.md): canonical comms codes (sit rep · Oscar Mike · **how copy** ack protocol · BOLO capture), seven-block sit rep order, cache doctrine. Agent memory mirrors it; the file wins on conflict.
- **BOLO board stood up** — [BOLO.md](BOLO.md): the watchlist (3 active BOLOs + PMCS moved in from this file). Name **RULED**: BOLO — Be On the Lookout, for the bolas echo (thrown on sighting, wraps, holds). Retired bench: FRAGO / WARNO / Fire Watch.
- **Ready Rack / Magazine built** — `_CACHE/` session notes flush to `_LOG/` on every sit rep; first session note staged. Sit rep now opens with Block 0 "last session" from the Rack.
- **SOI proword card pinned** — SOP §0: every comms code and board noun on one glance. **"ENDEX"** coded provisionally as the session close-out proword ("Out" / "secure the net" on the bench).

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
| `_CANON_NODES/` | Canonical entity nodes + registers (film register · moon-saga seed) |
| `_ARCHIVE/INDEX.md` | The ancients — seventeen archived folders, what each was, what was promoted out and to where |
| `_devlog/_devlog_docs/_devlog_journals/` | Daily journal, `MMDDYYYY.journal.md` |

---

## Known rot

- **`_devlog/`** is mostly a vendored copy of the vscode-journal extension repo — 464 files, 587 MB of third-party docs. Only `_devlog_docs/_devlog_journals/` is yours.
- **Six competing PKM systems on disk** — Logseq (5,194 tracked), Obsidian, Joplin ×2, ShroomsQ, claude.ai. Consolidation not started.
- ~~**Joplin geolocation metadata** — imported vault files carry home-adjacent lat/long in a public repo.~~ **Stripped 2026-08-24** (tree + full history).
- **10-item review queue** — `_0.1_BVX_LEARN/_meta/REVIEW-QUEUE.md`
- `OUTLIERS_FINAL_DRAFT/outliers.fdx` is **empty**. No script pages exist.
- **`yolov8n.pt` (6.5 MB) sits at the public repo root** (committed 8/31 by the cast pre-pass); the working copy is the gitignored one in `_PRIVATE/taxonomy_engine/`. Candidate for tree removal + `.gitignore` entry — not ruled.
- **The Dec-2025 Joplin MCDP summaries are unreliable** — 9/3 repair pass proved the 4 and 8 files were generated from filenames (retagged UNVERIFIED, real summaries regenerated) and found MCDP 7's chapters do not match the book. The other nine are unaudited. The MIL.01–MIL.11 one-sheets (from the PDFs) are the citable layer.
- **`_ARCHIVE/_DIRECTORY OF DIR/`** (823 files) was archived uninventoried; `_narratology_dir` and `_wicked_figures_dir` may hold more distills.

---

## Maintenance

1. Session opens: read this file.
2. Session closes: update **Moved**, **Blocked on you**, and **Live**. Add a journal entry at `_devlog/_devlog_docs/_devlog_journals/MMDDYYYY.journal.md`.
3. Detail goes to the owning registry, never here. This file stays an index.
4. A decision that isn't written down did not happen.
