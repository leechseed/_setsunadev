---
title: "Development Standard: reference"
type: reference
for: "an agent or Chief looking up a stage, rule, audit hook, or tailoring size of the loop"
does: "lists every component of the Development Standard"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_09_operations_development_standard.md
source_version: 0.1.2
---

**Who it's for:** an agent or Chief looking up a stage, rule, audit hook, or tailoring size of the loop · **What it does:** lists every component of the Development Standard · **Type:** reference

# Development Standard: reference

The source has type `ssot_standard`, category operations, version 0.1.2, last updated 2026-09-15. It applies to BOLD_VENTURE, ULTRASIN, OPERATOR. Status: working, v0.1; it promotes to canonical after two project uses (DOCTRINE 0, Invariant I). Working title: true. BOLO 53. Rung: procedure, NASA four, ruled 2026-09-15 (BOLO 50).

## Core Methodology

### A · The life-cycle read

The Command loop is **iterative-incremental development**. Five outside parents each describe a piece, in one line:

- **ISO/IEC/IEEE 12207:2017 and 15288:** life-cycle process standards. They name the iterative and incremental model as a standing process pattern.
- **The Agile Manifesto's principles and Scrum's inspect-and-adapt:** deliver on a short cycle, inspect, adapt. Transparency, inspection, and adaptation are the three pillars.
- **Deming's PDCA:** Plan, Do, Check, Act, a closed loop where the check feeds the next plan.
- **Boyd's OODA:** Observe, Orient, Decide, Act, the same cycle the project flow names as one session's shape (§F there).
- **MCDP 6:** control is the feedback returning from the action, not the orders going out.

The Command's three grains: the **increment** is one turn's delivery, which lands as a FRAGO onto the sheet. The **iteration** is one session, which Oscar Mike closes. The **release** is a project's gate, which runs inside the project flow. The read was ruled and is no longer provisional (version 0.1.1); the standard itself promotes on two uses.

### B · The loop, stage by stage

| Stage | Proword | What happens | Who | Exit event | Outside name |
|---|---|---|---|---|---|
| **Capture** | BOLO | A spoken tasking is written into BOLO.md the same turn | Chief speaks, Claude writes | The line exists on the sheet | Backlog intake |
| **Orient** | sit rep / DOPE SHEET N | The board or the BOLO's standing page delivers in fixed blocks or SMEAC order | The formation reads; the main line writes only the header | The page is read | Observe / Orient (OODA) |
| **Understanding check** | boresight | Readback, the read, clarifying questions, in that order | Claude proposes, Chief rules | Chief clears delivery | Inspection (Scrum) |
| **The order and readback** | how copy | "Good copy" plus a one-to-two-line readback, then execute | Chief closes the order, Claude reads it back | Execution begins | Decide → Act (OODA) |
| **Build** | (the formation) | Hub and spoke: gear 1 default, specialists on disjoint inputs, one script reviewer at the fan-in | Specialists plus one reviewer | The reviewer's checklist clears | Do (PDCA) |
| **Delivery and the record** | (the reply) | The reply lands in chat; the increment is pushed onto the sheet | Claude | FRAGO N merges and republishes | An increment delivered (12207/15288) |
| **Close** | Oscar Mike | Ready Rack note finalized, STATE updated, journal appended, OUT block closes the reply | Claude, ruled by Chief | The OUT block, nothing after it | Check/Act (PDCA); the AAR |
| **Resume** | Charlie Mike / RTB | A legacy card reopens at its resume order, or goes home and clears; new work resumes from its DOPE SHEET | Chief speaks, Claude executes | The card is cleared or resumed | Adaptation (Scrum) |

Three correction channels fire at any stage:

- **Abort abort abort** cancels the immediately preceding order; the record keeps the abort line, not the order.
- **Break-break / buttonhook back** parks the current stage where it stands and opens a detour. Buttonhook back returns unprompted, restating where the loop was.
- **BOLO capture** is the alarm channel: a spoken tasking interrupts any stage and is written the same turn.

### C · Nesting

The shape of MCDP 1-2 holds: turn = engagement = task. Session = operation = one OODA cycle. Project = campaign.

| Level | MCDP 1-2 term | This standard | The project flow | The SOP |
|---|---|---|---|---|
| Task | engagement | one increment (a FRAGO) | one work package inside a phase | one transmission |
| Session | operation | one iteration, one OODA cycle | a gate may fire inside it | one sit rep to one Oscar Mike |
| Project | campaign | many iterations in sequence | the six phases and their gates | many sessions |

The standard is the engagement-level cycle inside the project flow's phases. The project flow's gate (§D there) is a session-level event that fires when a phase's event fires. The SOP's blocks are this standard's orient stage, delivered as the sit rep or a DOPE SHEET.

### D · Standing rules

Nine numbered rules; none is invented here.

1. **Nothing builds before the order is confirmed:** how copy cleared, or boresight cleared when spoken. (SOP.md §1)
2. **A tasking not written down did not happen: same turn.** (SOP.md §1; DOCTRINE 0, Invariant II)
3. **The ruling, not more structure, ends a stall; a hold carries a decider and a conversion date.** (project flow §D)
4. **Defaults run if silent, marked provisional.** (SOP.md §1; Chief's 2026-09-10 ruling)
5. **One reviewer at the fan-in, never peer checks.** (SOP.md §1, BOLO 54)
6. **The record keeps the abort line, not the order.** (SOP.md §1)
7. **Every increment lands on the sheet as a FRAGO; nothing lives only in chat.** (SOP.md §1)
8. **The close-out is one word and one procedure.** (SOP.md §1)
9. **Command format §7 on every transmission.** (SOP.md §7)

### E · Audit hooks

How each rule's compliance is checked, for BOLO 51:

| # | Rule | Evidence it was followed | Where the evidence lives |
|---|---|---|---|
| 1 | Order confirmed before build | A "Good copy" readback or cleared boresight precedes the build turn | The transcript |
| 2 | Tasking written same turn | The BOLO line's turn matches the turn it was spoken | BOLO.md |
| 3 | Ruling ends a stall | The hold row names a decider and a conversion date, never blank | The brief's decision ledger, STATE.md |
| 4 | Defaults marked provisional | The default carries the word provisional and a date | SOP.md, this document |
| 5 | One reviewer at the fan-in | One reviewer's checklist output, no second specialist re-checking | The sheet's Log, the transcript |
| 6 | Abort line kept, not the order | The struck order does not appear; only the abort line | The transcript, the git log |
| 7 | Increment lands as a FRAGO | A FRAGO N entry exists for the turn's delivery | The sheet's Log |
| 8 | Close-out is one word, one procedure | The OUT block closes the session; nothing follows it | The transcript, `_CACHE/` → `_LOG/` |
| 9 | Command format on every transmission | Bulleted readback, bold signposts, no prose wall | The transcript |

### F · Tailoring

| Size | What it is | The loop |
|---|---|---|
| **S** | a one-turn ask | how copy → build → reply. No sheet. |
| **M** | a BOLO | DOPE SHEET built once; a FRAGO per increment. |
| **L** | a project | the project flow's brief and gates; this loop runs inside every session inside it. |

This mirrors the project flow's S/M/L table (§H there).

### G · Governance

DOCTRINE 0 is the promotion mechanic: v0.1 working, promotes to canonical after two project uses. The next revision strikes any rule unused across those uses. The rung is **procedure** (NASA four, ruled 2026-09-15): it governs how the Command works, not what a product measures. Revisions belong to P6 of any project that used this loop, or to a standalone FRAGO 53.

## Implementation

### Running one increment

Eight steps:

1. **Capture, BOLO:** write the tasking into BOLO.md the same turn.
2. **Orient, sit rep or DOPE SHEET N:** read the current state before deciding.
3. **Understanding check, boresight, only if spoken:** readback, the read, clarifying questions.
4. **Order, how copy:** "Good copy" plus the readback, then execute.
5. **Build, the formation:** gear 1 default, specialists on disjoint inputs, one script reviewer at the fan-in.
6. **Deliver, the reply plus FRAGO N:** push the increment onto the sheet, not just into chat.
7. **Close, Oscar Mike:** the cache note, the STATE update, the journal, the OUT block.
8. **Resume, Charlie Mike or RTB:** for a legacy card; a new BOLO resumes from its DOPE SHEET.

## Examples

### Example 1 · the 9/15 sit rep, run as the formation

The board ran under the formation (BOLO 54): three specialists read disjoint sources with no cross-talk. Then one script reviewer ran at the fan-in. The reviewer's first pass stopped on three findings. Each specialist fixed its own finding, and the main line stripped one stray key by hand. The third pass cleared, and the board republished to its standing page. No peer cross-check ran, per Rule 5.

### Example 2 · DOPE SHEET 53, this document's own first increment

BOLO 53 was tabled 2026-09-12 and opened 2026-09-15 on the spoken word "Open 53". This document is that opening's first increment, built by one specialist (DRAFT) at gear 1, as Rule 7 requires. Its next increment is a FRAGO onto DOPE SHEET 53, not a rewrite of the file.
