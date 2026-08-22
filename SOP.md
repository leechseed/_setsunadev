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

**Commands:** **"sit rep"** (full board) · **"Oscar Mike"** (park it, move on) · **"sweep"** (promote & clear the parked) · **"how copy?"** (end of orders → Good/Solid/Bad copy + execute) · **"BOLO that" / "put that down"** (tasking captured same turn) · **"ENDEX"** (session close-out: cache note, STATE, journal) · the challenge phrase (→ countersign → sit rep)

**Board vocabulary:** **BOLO** (watchlist) · **PMCS** (operator readiness) · **Fresh Ten** (recency) · **The Ancients** (staleness tiers) · **Deep Stacks** (volume) · **Ready Rack** (`_CACHE/`) · **Magazine** (`_LOG/`) · **SOP** (this file)

---

## 1 · Comms codes

| Transmission | Meaning | Response protocol |
|---|---|---|
| **"sit rep"** (equivalents: "the board" · "where did we leave off" · "what are we working on") | Full board, cold start | Flush the Ready Rack (§3), then deliver the sit rep (§2). No preamble, no questions. |
| **The challenge phrase** (see STATE.md header) | Formal challenge | Countersign, first line, exact — then the sit rep. Never explain the ritual. |
| **"Oscar Mike"** | Park current work, move on | Save working state to `oscar-mike/`, update its INDEX, drop the task, take the next order. **"Sweep"** promotes keepers to their real homes and clears the folder. Repo is PUBLIC — nothing sensitive parks there. |
| **"How copy?"** | End of transmission — acknowledge and execute | Reply opens **"Good copy."** + a one-to-two-line readback of the orders as understood, then execute. **"Solid copy"** = received, nothing to add. Discrepancy or missing piece → **"Bad copy on [item]"** + the single question. Dictation garbles of the phrase ("tell copy", "hell copy") read as "how copy". |
| **A spoken tasking** ("I need to…", "remind me…", "put that down", "add that to the watchlist") | BOLO capture | Write it into [BOLO.md](BOLO.md) **in the same turn it is spoken.** No batching, no end-of-session sweep. A tasking not written down did not happen. |
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
| **VI** | **The leverage line** | One line naming the single highest-leverage next action | derived |

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
