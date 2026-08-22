---
title: SOP — Standing Operating Procedure
type: doctrine
status: living document — canonical home of the verbal protocol
updated: 2026-08-21
read_first: true
read_with: STATE.md · BOLO.md · PROJECTS.md · _CACHE/
---

# SOP — THE WAY THIS OPERATION RUNS

Canonical home of every comms code and session protocol. If a code is not written here, it is not protocol. Claude's agent memory mirrors this file; **on any conflict, this file wins.** Written to the Marine Corps Doctrine Standard.

---

## 0 · SOI — the proword card

Quick reference. Full definitions in the sections below.

**Commands:** **"sit rep"** (full board) · **"Oscar Mike"** (park it, move on) · **"sweep"** (promote & clear the parked) · **"how copy?"** (end of orders → Good/Solid/Bad copy + execute) · **"boresight"** (understanding check: readback → the read → clarifying questions only; no delivery until cleared; only when spoken; **"boresight in on [target]"** aims it at a named item) · **"BOLO that" / "put that down"** (tasking captured same turn) · **"ivory tower"** (academic mode — published literature only, cited inline) · **"break-break"** (open a detour) · **"buttonhook back"** (close the detour — main thread restored unprompted) · **"ENDEX"** (session close-out: cache note, STATE, journal) · the challenge phrase (→ countersign → sit rep)

**Board vocabulary:** **BOLO** (watchlist) · **PMCS** (operator readiness) · **Fresh Ten** (recency) · **The Ancients** (staleness tiers) · **Deep Stacks** (volume) · **Ready Rack** (`_CACHE/`) · **Magazine** (`_LOG/`) · **SOP** (this file)

---

## 1 · Comms codes

| Transmission | Meaning | Response protocol |
|---|---|---|
| **"sit rep"** (equivalents: "the board" · "where did we leave off" · "what are we working on") | Full board, cold start | Flush the Ready Rack (§3), then deliver the sit rep (§2). No preamble, no questions. |
| **The challenge phrase** (see STATE.md header) | Formal challenge | Countersign, first line, exact — then the sit rep. Never explain the ritual. |
| **"Oscar Mike"** | Park current work, move on | Save working state to `oscar-mike/`, update its INDEX, drop the task, take the next order. **"Sweep"** promotes keepers to their real homes and clears the folder. Repo is PUBLIC — nothing sensitive parks there. |
| **"How copy?"** | End of transmission — acknowledge and execute | Reply opens **"Good copy."** + a one-to-two-line readback of the orders as understood, then execute. **"Solid copy"** = received, nothing to add. Discrepancy or missing piece → **"Bad copy on [item]"** + the single question. Dictation garbles of the phrase ("tell copy", "hell copy") read as "how copy". |
| **"Boresight"** — **RULED 2026-08-21.** Marksmanship: align the sight to the bore so point of aim = point of impact; nothing fires until they agree. Directed form: **"boresight in on [target]"** aims the protocol at a named item (a BOLO, a doc, a decision). Equivalents: "what are you getting from this" · "what's your read on it" | Confirm understanding **before** delivery — the mirror of "how copy". **Only when spoken, never automatic** (ruled 2026-08-21) — the standing cadence stays clean so Papi can get straight to the point | Fixed three-part reply, then hold: **(1) Readback** — the transmission as understood, in own words, nothing skipped. Proof of copy comes before anything else. **(2) The read** — assessment, relevant repo holdings, plan of attack — built answer-first per the Pyramid Principle (ratified BVX doctrine). Plan only, no delivery. **(3) Clarifying questions** — one numbered block, tied strictly to the transmission. Clarify only: no branching, no new material. Loop 1–3 until the chain is walked down; Papi then clears delivery. Rationale: catches drift and premature branching before effort is spent. |
| **A spoken tasking** ("I need to…", "remind me…", "put that down", "add that to the watchlist") | BOLO capture | Write it into [BOLO.md](BOLO.md) **in the same turn it is spoken.** No batching, no end-of-session sweep. A tasking not written down did not happen. |
| **"Ivory tower"** ("what's the ivory tower on this?") — coded 2026-08-21 | Academic mode — answer from the published literature only | Every claim carries its source inline: researcher, year, field. Peer-reviewed beats books beats everything else; pop-sci gets flagged as pop-sci. Mark established vs emerging vs contested. Name the controlling field. Still house format (§7) — the rigor is in the sourcing, never in walls of prose. |
| **"Break-break"** → **"buttonhook back"** — **RULED 2026-08-21** | Detour open / detour close | "Break-break" parks the main thread exactly where it stands and opens the detour. **"Buttonhook back"** closes it: return to the parked thread **unprompted**, restating where we were. Lineage: break-break cuts into ongoing net traffic; the buttonhook hooks off the axis and comes back onto it. |
| **"ENDEX"** (provisional 2026-08-21; "Oscar Mike" spoken at session end reads the same) | Stand down — close the session | Run the close-out: write/finalize the Ready Rack session note · update STATE.md (Moved / Blocked / Live) · append the day's journal entry. Autocommit fires on session stop. Radio equivalents: "Out" · "secure the net". |

---

## 2 · The sit rep — the blocks, fixed order

| Block | Name | Content | Source |
|---|---|---|---|
| **0** | **Last session** | What moved in the previous session — read from the Ready Rack before flushing it | `_CACHE/` |
| **I** | **The Fresh Ten** | Ten projects touched most recently, newest first — last-touched date, one line of context, concrete next step | STATE.md + git log |
| **II** | **The Ancients** | Longest-untouched work, tiered: true ancients → going quiet → recently parked; each with what it is waiting on | STATE.md + PROJECTS.md |
| **III** | **The Deep Stacks** | Volume ranking — content mass per project | PROJECTS.md |
| **IV** | **The BOLO board** | Active BOLOs + the PMCS readiness table | BOLO.md |
| **V** | **Blocked on you** | Numbered decisions in priority order | STATE.md |
| **VI** | **The leverage line** *(provisional rename pending: "The Main Effort" — MCDP 1's term for the one point everything else supports)* | One line naming the single highest-leverage next action | derived |

**Trunk discipline — coded 2026-08-21, non-negotiable.** Every item on every block carries its trunk: **BLACK** (creative, IP, systems) · **ORANGE** (venture, body, sexuality) · **OPERATOR** (PMCS — the operator is equipment). The board is never delivered trunk-blind. This is how Papi's head sorts; the protocol upholds it everywhere, always.

---

## 3 · The cache — Ready Rack and Magazine

Session continuity runs on ammunition-handling logic:

- **`_CACHE/` — the Ready Rack.** Rounds staged for immediate use. Every working session drops (or updates) one session note here: `YYYY-MM-DD[-n].session.md` — what moved, what was ruled, what is mid-flight. Written at session close or at any milestone worth surviving a crash.
- **The flush.** On every sit rep: read every session note in the Ready Rack, deliver Block 0 from them, then **move them** (not copy, not delete) into `_LOG/`. The Rack returns to empty. An empty Rack is the proof the handoff completed.
- **`_LOG/` — the Magazine.** Deep storage. Flushed session notes live here permanently, filename-dated, append-only. Nothing is ever deleted — it is stowed.
- The `README.md` in each folder states its own rule and never gets flushed.

STATE.md remains the **index** (what is live, what is blocked); the Ready Rack is the **wire** (what just happened). Detail still belongs to the owning registries.

---

## 4 · Session-open reading order

1. **SOP.md** — this file. The protocol itself.
2. **STATE.md** — the index.
3. **BOLO.md** — the watchlist.
4. **`_CACHE/`** — the Ready Rack (flush on sit rep).
5. **PROJECTS.md** — the volume board.

A session that answers "sit rep" without all five has not answered it.

---

## 5 · Open naming rulings on this doc

- **"BOLO"** for the watchlist — **RULED 2026-08-21.** Be On the Lookout, chosen for the bolas echo (the gaucho throwing weapon: thrown on sighting, wraps the target, holds it until you arrive). Retired bench: FRAGO · WARNO · Fire Watch.
- Ready Rack / Magazine — provisional, same session.
- **"Boresight"** for the understanding check — **RULED 2026-08-21.** Struck en route: "back-brief" (lame). Retired bench: AZIMUTH · ZERO · BACK-AZIMUTH · OVERLAY · ECHO · SQUAWK · FIVE-BY · RECON · READBACK · CONFIRMATION BRIEF. **INTEL returns to the pool** — Papi's seed, unassigned, likely future coinage.
- **"Main effort"** as a command proword — **provisional 2026-08-21.** MCDP 1's answer to "this is the main thing, focus here": the designated main effort is the one task everything else supports; all else is supporting effort. Spoken, it names or asks for the single priority. Sit rep Block VI rename to "The Main Effort" rides on the same ruling.
- **"Break-break" / "buttonhook back"** for the detour pair — **RULED 2026-08-21.** Open with break-break, close with buttonhook back. Retired bench: AS YOU WERE · DOGLEG · EXCURSION · HERRINGBONE.

---

## 6 · Lexicon doctrine — the Corps is the bootstrap

**Coded 2026-08-21.** The USMC proword and doctrine vocabulary is a **starting library, not the end-state.** It is adopted wholesale as the bootstrap; native coinages are expected to replace and extend it as the operation matures. The drift into an own language is **intended** — the lexicon is a worldbuilding asset that bleeds into the culture. The model is the Disney effect: code language plus uniform makes the separation between inside-the-operation and the rest of the world clean and total. Ten borrowed words today, ten coined words tomorrow, a house tongue eventually.

---

## 7 · House format — how transmissions are written

**Coded 2026-08-21 after the readback-wall incident.** The rhetoric stays; the formatting serves scanning. This is v0.1 — the full learning-science distill is BOLO 6.

1. **Readbacks are bulleted.** One order per bullet, bold anchor up front. Never a prose wall.
2. **One idea per paragraph, three sentences max.** Working memory holds about four items; the format respects that.
3. **Bold is a signpost, not decoration** — the first words of the point, so the bolds alone tell the story on a scan.
4. **Parallel items go in bullets or tables,** never buried in prose.
5. **Answer-first everywhere** (Pyramid Principle, ratified doctrine).
6. **The Spartan dial: trim words, not meaning.** Complete sentences, nothing ornamental — Laconic, but the message survives whole.
7. **The ten-second test:** headers plus bolds alone must carry the message. If a scan doesn't tell the story, the format failed.
