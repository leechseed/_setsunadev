---
type: ssot_standard
category: operations
version: 0.1.2
last_updated: 2026-09-15
applies_to: [BOLD_VENTURE, ULTRASIN, OPERATOR]
status: working — v0.1; promotes to canonical after two project uses (DOCTRINE 0, Invariant I)
working_title: true
bolo: 53
rung: procedure · NASA four, ruled 2026-09-15 (BOLO 50); moved up from the provisional STANDARD rung the same day
purpose: "Defines the loop inside a session by which anything gets built, from a one-turn ask to a project, and the correction channels that keep it from stalling; governs the loop, where SOP governs the session and the project flow governs the project."
dependencies: ["[[SOP]]", "[[📐 ssot_05_operations_project_flow]]", "[[DOCTRINE-0-INVARIANTS]]", "[[standards.register]]"]
sources: "SOP.md comms codes §1, rulings 2026-08-21 to 2026-09-12 · ssot_05_operations_project_flow.md v0.1.0 (2026-09-03) · BOLO 53 row and sources.md, tabled 2026-09-12, opened 2026-09-15"
---

# 📐 ssot_05_operations_development_standard — THE DEVELOPMENT STANDARD (working title)

## Table of Contents

1. [Purpose](#purpose)
2. [Core Methodology](#core-methodology)
   - [A · The life-cycle read](#a--the-life-cycle-read)
   - [B · The loop, stage by stage](#b--the-loop-stage-by-stage)
   - [C · Nesting](#c--nesting)
   - [D · Standing rules](#d--standing-rules)
   - [E · Audit hooks](#e--audit-hooks)
   - [F · Tailoring](#f--tailoring)
   - [G · Governance](#g--governance)
3. [Implementation](#implementation)
4. [Examples](#examples)
5. [Version History](#version-history)

---

## Purpose

This document states how one exchange between Papi and Claude becomes a built thing, from a single turn to a project. It governs the **loop**. The project flow governs the project the loop runs inside; the SOP governs the session that contains it.

The loop exists to end two failure modes. The first is **the stall pattern**: a finished design blocked on one unanswered decision, then rebuilt from scratch later, because the block was never named and dated. The second is its cousin: **work built before the order was confirmed**, spending effort on a shared image that was never actually shared.

---

## Core Methodology

### A · The life-cycle read

The house loop is **iterative-incremental development**. Five outside parents already describe pieces of it, each stated in one line, no more than the record supports:

- **ISO/IEC/IEEE 12207:2017 and 15288:** the life-cycle process standards; both name the iterative and incremental life-cycle model as a standing process pattern, not an exception to a plan-driven default.
- **The Agile Manifesto's principles and Scrum's inspect-and-adapt:** deliver on a short cycle, inspect what came back, adapt the plan; transparency, inspection, and adaptation are the three pillars.
- **Deming's PDCA:** Plan, Do, Check, Act, a closed loop where the check feeds the next plan.
- **Boyd's OODA:** Observe, Orient, Decide, Act, the same cycle the project flow already names as one session's shape (§F, Cadence and control).
- **MCDP 6:** control is the feedback returning from the action, not the orders going out, the doctrine the project flow already cites for its own cadence.

The house names its own three grains. The **increment** is one turn's delivery, recorded as a FRAGO onto the sheet. The **iteration** is one session, closed by Oscar Mike. The **release** is a project's gate, run inside the project flow. Claude's working read, banked on BOLO 53 when it was tabled 2026-09-12: the boresight → how copy → build → FRAGO loop is iterative-incremental development. That read is provisional until two uses promote it, per DOCTRINE 0, Invariant I.

### B · The loop, stage by stage

| Stage | Proword | What happens | Who | Exit event | Outside name |
|---|---|---|---|---|---|
| **Capture** | BOLO | A spoken tasking is written into BOLO.md the same turn it is spoken | Papi speaks, Claude writes | The line exists on the sheet | Backlog intake |
| **Orient** | sit rep / DOPE SHEET N | The board or the BOLO's standing page delivers in fixed blocks or SMEAC order | The formation reads; the main line writes only the header | The page is read | Observe / Orient (OODA) |
| **Understanding check** | boresight | Readback, the read, clarifying questions, in that order | Claude proposes, Papi rules | Papi clears delivery | Inspection (Scrum) |
| **The order and readback** | how copy | "Good copy" plus a one-to-two-line readback, then execute | Papi closes the order, Claude reads it back | Execution begins | Decide → Act (OODA) |
| **Build** | (the formation) | Hub and spoke: gear 1 default, specialists on disjoint inputs, one script reviewer at the fan-in | Specialists plus one reviewer | The reviewer's checklist clears | Do (PDCA) |
| **Delivery and the record** | (the reply) | The reply lands in chat; the increment is pushed onto the sheet | Claude | FRAGO N merges and republishes | An increment delivered (12207/15288) |
| **Close** | Oscar Mike | Ready Rack note finalized, STATE updated, journal appended, OUT block closes the reply | Claude, ruled by Papi | The OUT block, nothing after it | Check/Act (PDCA); the AAR |
| **Resume** | Charlie Mike / RTB | A legacy card reopens at its resume order, or goes home and clears; new work resumes from its DOPE SHEET | Papi speaks, Claude executes | The card is cleared or resumed | Adaptation (Scrum) |

Three correction channels can fire at any stage, not only at the one where they are listed:

- **Abort abort abort** cancels the immediately preceding order; the record keeps the abort line, not the order.
- **Break-break / buttonhook back** parks the current stage exactly where it stands and opens a detour; buttonhook back returns unprompted, restating where the loop was.
- **BOLO capture** is the alarm channel: any stage can be interrupted by a spoken tasking, written the same turn it is spoken.

### C · Nesting

MCDP 1-2's shape holds at this altitude too: **turn = engagement = task. Session = operation = one OODA cycle. Project = campaign.**

| Level | MCDP 1-2 term | This standard | The project flow | The SOP |
|---|---|---|---|---|
| Task | engagement | one increment (a FRAGO) | one work package inside a phase | one transmission |
| Session | operation | one iteration, one OODA cycle | a gate may fire inside it | one sit rep to one Oscar Mike |
| Project | campaign | many iterations in sequence | the six phases and their gates | many sessions |

This standard is the engagement-level cycle running inside the project flow's phases. The project flow's gate (§D there) is a session-level event: it fires when a phase's event fires, which a single session may or may not reach. The SOP's blocks are this standard's orient stage, delivered as the sit rep or a DOPE SHEET.

### D · Standing rules

Numbered. Each is derived from a source read for this document; none is invented here.

1. **Nothing builds before the order is confirmed:** how copy cleared, or boresight cleared when boresight was spoken. *(SOP.md §1, the how-copy and boresight rows)*
2. **A tasking not written down did not happen: same turn.** *(SOP.md §1, BOLO capture row; DOCTRINE 0, Invariant II)*
3. **The ruling, not more structure, ends a stall; a hold carries a decider and a conversion date.** *(the project flow §D, the gate's HOLD rule; the stall pattern itself)*
4. **Defaults run if silent, marked provisional.** *(SOP.md §1: every DOPE SHEET carries a "Silence:" default line; the Gear N row runs on silence; Papi's ruling of 2026-09-10 that a call with an obvious default is made and marked provisional, never asked)*
5. **One reviewer at the fan-in, never peer checks.** *(SOP.md §1, the sit rep and Gear N rows describing the formation, BOLO 54)*
6. **The record keeps the abort line, not the order.** *(SOP.md §1, the abort abort abort row)*
7. **Every increment lands on the sheet as a FRAGO; nothing lives only in chat.** *(SOP.md §1, the DOPE SHEET / FRAGO row)*
8. **The close-out is one word and one procedure.** *(SOP.md §1, the Oscar Mike row)*
9. **House format §7 on every transmission, including this one.** *(SOP.md §7)*

### E · Audit hooks

For BOLO 51, the logistics front: how each rule's own compliance is checked, kept to the nine rules above.

| # | Rule | Evidence it was followed | Where the evidence lives |
|---|---|---|---|
| 1 | Order confirmed before build | A "Good copy" readback or a cleared boresight precedes the build turn | The transcript |
| 2 | Tasking written same turn | The BOLO line's turn matches the turn it was spoken | BOLO.md |
| 3 | Ruling ends a stall | The hold row names a decider and a conversion date, never blank | The brief's decision ledger, STATE.md |
| 4 | Defaults marked provisional | The default carries the word provisional and a date | SOP.md, this document |
| 5 | One reviewer at the fan-in | One reviewer's checklist output, no second specialist re-checking the same work | The sheet's Log, the transcript |
| 6 | Abort line kept, not the order | The struck order does not appear; only the abort line does | The transcript, the git log |
| 7 | Increment lands as a FRAGO | A FRAGO N entry exists on the sheet for the turn's delivery | The sheet's Log |
| 8 | Close-out is one word, one procedure | The OUT block closes the session; nothing follows it | The transcript, `_CACHE/` → `_LOG/` |
| 9 | House format on every transmission | Bulleted readback, bold signposts, no prose wall | The transcript |

### F · Tailoring

Mirrors the project flow's S/M/L table (§H there); this is the loop's own compression rule.

| Size | What it is | The loop |
|---|---|---|
| **S** | a one-turn ask | how copy → build → reply. No sheet. |
| **M** | a BOLO | DOPE SHEET built once; a FRAGO per increment. |
| **L** | a project | the project flow's brief and gates; this loop runs inside every session inside it. |

### G · Governance

[DOCTRINE 0](../../../../DOCTRINE-0-INVARIANTS.md) is the promotion mechanic: this standard is **v0.1 working**, promotes to canonical after two project uses, and any rule unused across those two uses is struck at the next revision. Its rung on the BOLO 50 ladder is **procedure** (NASA four, ruled 2026-09-15): it governs how the house works, not what a product measures. It moved up from the provisional STANDARD rung the day the ladder was ruled, with no content change. Revisions belong to P6 of any project that used this loop, or to a standalone FRAGO 53.

---

## Implementation

### Running one increment

1. **Capture, BOLO:** write the tasking into BOLO.md the same turn.
2. **Orient, sit rep or DOPE SHEET N:** read the current state before deciding anything.
3. **Understanding check, boresight, only if spoken:** readback, the read, clarifying questions.
4. **Order, how copy:** "Good copy" plus the readback, then execute.
5. **Build, the formation:** gear 1 default, specialists on disjoint inputs, one script reviewer at the fan-in.
6. **Deliver, the reply plus FRAGO N:** push the increment onto the sheet, not just into chat.
7. **Close, Oscar Mike:** the cache note, the STATE update, the journal, the OUT block.
8. **Resume, Charlie Mike or RTB:** for a legacy card; a new BOLO resumes straight from its DOPE SHEET.

---

## Examples

### Example 1 · the 9/15 sit rep, run as the formation

The board ran under the formation (BOLO 54): three specialists reading disjoint sources with no cross-talk, then one script reviewer at the fan-in. The reviewer's first pass stopped on three findings. Each specialist fixed its own finding, none checking another's work; the main line stripped one stray key by hand; the third pass cleared, and the board republished to its standing page. No peer cross-check ran anywhere in the sequence, per Rule 5.

### Example 2 · DOPE SHEET 53, this document's own first increment

BOLO 53 was tabled 2026-09-12 and opened today, 2026-09-15, on one spoken word: "Open 53." This document is that opening's first increment, built by one specialist (DRAFT) at gear 1, exactly as Rule 7 requires: it lands on the sheet, not only in chat. Its own next increment is a FRAGO onto DOPE SHEET 53, not a rewrite of this file.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-09-15 | Working draft on Papi's "Open 53" (2026-09-15). Life-cycle read iterative-incremental, provisional. Rung provisional pending the BOLO 50 ladder. Promotes on two uses. |
| 0.1.1 | 2026-09-15 | Papi: "Everything approved." The iterative-incremental read ruled, no longer provisional. Filing beside the project flow ruled; rung STANDARD, only the ladder (BOLO 50) still open. v0.1 accepted as working; canon on two uses. Use counter opens at the next M or L build. |
| 0.1.2 | 2026-09-15 | NASA four ruled on BOLO 50. Rung moved from STANDARD (provisional) to PROCEDURE. No rule changed. |
