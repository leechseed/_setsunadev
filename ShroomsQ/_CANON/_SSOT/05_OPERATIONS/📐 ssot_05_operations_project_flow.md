---
type: ssot_methodology
category: operations
version: 0.1.0
last_updated: 2026-09-03
applies_to: [BOLD_VENTURE, ULTRASIN, OPERATOR]
status: working — v0.1; promotes to canonical after two project uses (DOCTRINE 0, Invariant I)
working_title: true
bolo: 25
purpose: "Defines how a project runs in this operation: the phases, the brief, the gates, the instruments, the cadence, and the tailoring rule. Governs the project; SOP.md governs the session."
dependencies: ["[[SOP]]", "[[DOCTRINE-0-INVARIANTS]]", "[[📐 ssot_05_operations_pm_holdings_inventory]]", "[[🧬 MIL.08 — MCDP 5 Planning — USMC (1997)]]", "[[🧬 MIL.09 — MCDP 6 Command and Control — USMC (1996)]]", "[[🧬 MIL.01 — MCDP 1 Warfighting — USMC (1997)]]", "[[🧬 MIL.03 — MCDP 1-2 Campaigning — USMC (1997)]]", "[[🧬 MIL.07 — MCDP 4 Logistics — USMC (2023)]]", "[[🧬 MIL.11 — MCDP 8 Information — USMC (2022)]]"]
sources: "Four-domains artifact (2026-02-25) six-phase lifecycle · PMBOK/Vargas solo mapping (2026-02-25) · BVIPDS charter + assumption log (2026-03-19) · Lab venture gates sheet (2026-08-31) · Ultrasin master registry status vocabulary · MCDP one-sheets MIL.01–MIL.11 (2026-09-03)"
---

# 📐 ssot_05_operations_project_flow — THE PROJECT FLOW (working title)

## Table of Contents

1. [Purpose](#purpose)
2. [Core Methodology](#core-methodology)
   - [A · The shape: campaign, operation, engagement](#a--the-shape-campaign-operation-engagement)
   - [B · The six phases](#b--the-six-phases)
   - [C · The brief](#c--the-brief)
   - [D · The gate](#d--the-gate)
   - [E · The instruments](#e--the-instruments)
   - [F · Cadence and control](#f--cadence-and-control)
   - [G · Standing principles](#g--standing-principles)
   - [H · Tailoring](#h--tailoring)
   - [I · Governance](#i--governance)
3. [Implementation](#implementation)
4. [Examples](#examples)
5. [Version History](#version-history)

---

## Purpose

This document states how a project runs in this operation. It assembles instruments that already exist into one flow: the six-phase lifecycle of the Bold Venture Development Doctrine, the brief derived from the BVIPDS charter and MCDP 5, the gate derived from MCDP 4 attainability and the lab-venture gates sheet, the decision ledger and status vocabulary of the Ultrasin registry, and the session protocol of the SOP. The flow governs the **project**. The SOP governs the **session**. A project is complete when its exit criteria are true; a session is complete at ENDEX. The flow exists to end one failure mode above all others: **a finished design blocked on one unanswered decision, then rebuilt from scratch.**

---

## Core Methodology

### A · The shape: campaign, operation, engagement

MCDP 1-2 supplies the levels. **Campaign = project. Operation = session. Engagement = task.** Sessions accumulate tasks; without an operational design that converts them into a strategic result, the operation collects tactical victories and finishes nothing. The flow is that operational design. Every project carries one **end state** written in policy terms (what the finished thing changes in the world), one **intent** (the "in order to" that outlasts any task), and one declared **mode**: **annihilation** (finish the artifact outright; victory is simple and measurable; the build is the main effort) or **erosion** (raise the value of the position over time until it yields; victory is defined by a threshold; the main effort may sit outside the build). A project that declares neither has failed before it starts.

### B · The six phases

Phases end on **events** (a decision made, an artifact shipped), never on dates. Plan the current phase in detail; carry only intent and two or three options for later phases (MCDP 1-2 near-detailed, far-conceptual). Each boundary is a gate (§D).

| Phase | Name | Produces | Gate question |
|---|---|---|---|
| **P0** | **Problem framing** | Priority questions (PIRs) named before research · environmental scan · problem statement · initial hypothesis · the **command narrative** seed (who this is for, what story it joins) | Is the problem worth a project? |
| **P1** | **Concept and intent** | **The brief** (§C): end state, intent, mode, success criteria, MECE decomposition, phases and gates, sustainment line, information line, control process, exit criteria | Is the problem worth solving? Is the decomposition complete? |
| **P2** | **Design and war-gaming** | Two or three courses of action tested against time, complexity, maintenance, runway · selected approach · skeleton of every deliverable · every critical unknown named · **attainability** stated | Is it feasible? Are the unknowns named? Is it attainable at acceptable risk? |
| **P3** | **Vertical slice** | One complete section at target quality, proving the whole can be built · AAR · revised plan | Does the slice prove the system? |
| **P4** | **Production** | Sprints scoped from the decomposition · mission-type orders to the AI partner · weekly AAR · living documentation | Complete, tested, documented, meets the intent? |
| **P5** | **Transition and operate** | Shipped and monitored · continuous delivery · periodic value check against the intent | Does it still serve the intent? |
| **P6** | **AAR and doctrine revision** | What happened, why, what applies next · revisions to this flow and to the owning registries | — |

P0 and P1 are the commander's work and are not delegated: MCDP 5 rules that planning is done **by** the organization, not for it, and that the intent is worded by the commander personally. The AI partner facilitates, drafts, and challenges. The operator writes the intent line.

### C · The brief

MCDP 5 rules that a plan without four components is not a plan: **desired outcome with intent · actions · resources · a control process.** The brief carries those four across eleven sections. It fits on one page for a small project and three for a venture. It is written answer-first and passes the ten-second test (SOP §7).

| # | Section | Content | Source |
|---|---|---|---|
| 1 | **End state and intent** | End state in policy terms. One intent sentence the partner can hold in mind. **Mode declared.** | MCDP 1-1 · MCDP 1 · MCDP 5 |
| 2 | **Success criteria** | Measurable. What must be true for the end state to count. | BVIPDS §2 |
| 3 | **Scope** | In. Out. Boundary enforcement rule. | BVIPDS §5 |
| 4 | **Decomposition** | MECE tree of workstreams; work packages no larger than one session. | PMBOK/Vargas · McKinsey |
| 5 | **Phases and gates** | Event-gated milestones **M-001…**, each with gate condition and deliverables. Current phase detailed; later phases intent plus options. | BVIPDS §7 · MCDP 1-2 |
| 6 | **Sustainment line** | What the project consumes (cash · energy · attention · tooling) · runway in months · the **attainability** statement and risk posture (avoid / accept / mitigate / transfer). One sentence plus branches for the two most likely disruptions. | MCDP 4 |
| 7 | **Assumptions and risks** | The assumption log (§E). Reviewed at every gate. | BVIPDS assumption log |
| 8 | **Information line** | Audiences, internal and external · the narrative, nested under the trunk narrative · the **deny list** (what is protected, from whom, how; what lives in `_PRIVATE/`) · the measure of narrative effect. | MCDP 8 |
| 9 | **Control process** | Sit rep cadence · decision points · the signals that trigger replanning. "The plan contains the means for changing the plan." | MCDP 5 · MCDP 6 |
| 10 | **Exit and termination** | The conditions under which the project is complete. The conditions under which it is killed or parked. Transition and reconstitution. | BVIPDS §10 · MCDP 1-2 |
| 11 | **Authority and the AI model** | Commander: Papi, full authority. Partner: mission-type orders, 5-80-15 split (intent · execution · judgment). The partner informs; it does not wait for permission inside the intent. | BVIPDS §11 · MCDP 1 · MCDP 6 |

### D · The gate

A gate is a decision, not a meeting. It happens when the phase event fires. It fits on one page and takes under thirty minutes. Three doctrines meet in it:

- **Attainability** (MCDP 4): sufficient support exists to initiate the next phase at an acceptable level of risk. Stated explicitly, risk posture named.
- **Ends-means reconciliation** (MCDP 1-1): when resources fall short, cut the end state or seek more; when the position is stronger than expected, expand. A gate that passes without touching either has not been run.
- **The greenlight checklist** (PMBOK/DoD/studio gates): entry criteria met · assumptions reviewed · risks named · value still present.

The gate returns one of three words. **GO**: next phase opens, resources commit inside its horizon. **NO-GO**: the project is killed or parked with Oscar Mike, the reason logged. **HOLD**: permitted only with **the single blocking decision named, the decider named, and the date on which the hold converts to a call.** An unnamed hold is the stall pattern. Doctrine tolerates mistakes of action and censures inaction (MCDP 1 · MCDP 6); a hold with no conversion date is inaction.

### E · The instruments

Every instrument already exists. The flow names where each lives.

| Instrument | Lives in | Rule |
|---|---|---|
| **The brief** | the project's home (`_PRIVATE/` when it carries finances or persona internals; the domain folder otherwise) | §C, one to three pages |
| **Assumption log** | beside the brief | ID · assumption · category · impact · risk if false · validation method · status OPEN / VALIDATED / INVALIDATED / REVISED |
| **Decision ledger** | [STATE.md](../../../../STATE.md) "Blocked on you" for the operation; a `# · Decision · Blocking?` table inside the brief for the project | closed rows are struck through with the ruling date, never deleted |
| **Task register** | [BOLO.md](../../../../BOLO.md) | captured the turn it is spoken |
| **Portfolio board** | [PROJECTS.md](../../../../PROJECTS.md) | volume ranking and leverage ranking, both |
| **Backlog** | [oscar-mike/](../../../../oscar-mike/) | park with a card; sweep promotes or clears |
| **Session handoff** | `_CACHE/` → `_LOG/` | the note at ENDEX is the AAR of the session |
| **Gates sheet** | inside the brief §5 and §6 | a measured condition authorises a specific spend (lab-venture G1–G3 pattern) |
| **Status vocabulary** | everywhere | 🟢 locked · 🟡 in motion · 🔴 open decision · ⚪ parked · 📄 artifact exists, needs recovery |
| **Main effort** | [STATE.md](../../../../STATE.md) | one at any moment; a redesignation that does not move support is nominal |

### F · Cadence and control

MCDP 6 inverts the intuition: **control is the feedback returning from the action, not the orders going out.** The operation's prowords are the control system.

- **Session = one OODA cycle.** Open on the sit rep (observe, orient). Decide. Act under mission-type orders. Close on ENDEX: the cache note is the feedback that makes the next cycle start from a changed situation.
- **Sit rep** is the control mechanism, delivered in fixed blocks. Block V (blocked on you) is the decision ledger surfaced. A sit rep that shows only enabling actions for several cycles is the alarm.
- **How copy** is explicit feedback: the readback confirms the shared image before execution consumes time.
- **Boresight** is implicit understanding built before execution, so that less must be said during it.
- **BOLO capture** is the alarm channel: lateral, immediate, the same turn.
- **Weekly AAR** in P4 and P5: what happened, why, what applies next. Recorded, never verbal only.
- **PIRs before research.** The operator names the two or three questions whose answers change the decision. Research without a PIR is collection without direction.

### G · Standing principles

Cross-cutting. Each is derived; none is declared without a source.

1. **Commander's intent over instructions.** Purpose and end state; method left open. *(MCDP 1)*
2. **MECE at every level.** No gaps, no overlaps in scope, documentation, or task allocation. *(McKinsey · PMBOK)*
3. **Answer first.** Every document readable in thirty seconds, five minutes, and in depth. *(Pyramid Principle, ratified)*
4. **Vertical slice before scale.** No full commitment until one complete piece proves the approach. *(studio pipelines · DoD TRL)*
5. **Living documentation.** STATE.md is the plan; a plan not updated after contact is a static document. *(MCDP 5)*
6. **Launch with what is in hand.** Expeditionary: the flow runs from the current repo and kit, or it is not the flow. *(MCDP 3)*
7. **Detail only the current horizon.** Later phases carry intent and options. *(MCDP 1-2 · MCDP 5)*
8. **Tempo over heroics.** Simultaneous work, the next step queued, decentralized decisions inside the intent. *(MCDP 1-2 · MCDP 1-3)*
9. **Webs, not chains.** One income source, one tool, one file everything depends on is a chain. Audit for a second path. *(MCDP 4)*
10. **Tolerate mistakes of action, not inaction.** *(MCDP 1 · MCDP 6)*

### H · Tailoring

MCDP 1-1 rules that a standardized process is a departure point, not the strategy; MCDP 6 rules that the default is the simple model expanded when time allows, never the elaborate model compressed under pressure. **The compressed default is: brief · gate · sit rep · ENDEX.** Everything else is expansion.

| Size | What it is | Brief | Gates | Information line | Sustainment line |
|---|---|---|---|---|---|
| **S** | a BOLO, a tool, a doc | five lines: end state · intent · scope · done · owner | one, at done | none | none |
| **M** | a system build | full brief, one page | P1 · P3 · P4 | if it ships outward | one sentence |
| **L** | a venture, an IP release | full brief, up to three pages | every phase | required | required, with runway and attainability |

### I · Governance

[DOCTRINE 0](../../../../DOCTRINE-0-INVARIANTS.md), ratified 2026-09-03, is the promotion mechanic. This flow is **v0.1 working**. It promotes to canonical after two project uses (Invariant I: earned, not declared). P6 of every project may revise it; revisions carry a version row. A rule in this document that is not used in two projects is struck at the next revision.

---

## Implementation

### Starting a project

1. **P0 in one sitting.** Name the two or three PIRs. Scan the environment against them. Write the problem statement. Form the hypothesis. Seed the command narrative. Decide: project, BOLO, or nothing.
2. **Write the brief (P1).** Use the blank below. The operator writes §1 personally. The partner drafts §3 to §9 from the holdings and the operator rules each. Declare the mode. Set the milestones as events.
3. **Gate 1.** Worth solving; decomposition complete. GO opens P2 with its resources.
4. **Run sessions under the SOP.** Sit rep opens, how copy closes orders, boresight when spoken, BOLO capture the same turn, ENDEX closes with the cache note and the STATE update.
5. **Gate on the event.** When the phase event fires, run the gate checklist below. Record GO / NO-GO / HOLD with its conversion date in the brief's decision ledger and in STATE.md.
6. **AAR** weekly in P4 and P5, and at every gate. Three questions, recorded.
7. **Close.** Exit criteria true → P6 AAR → registries updated → the brief marked complete → the project's cards swept from oscar-mike.

### The brief — blank

```markdown
# BRIEF — [project] · size [S/M/L] · mode [ANNIHILATION/EROSION] · v0.1 · [date]

## 1 End state and intent
End state: [what the finished thing changes in the world]
Intent: [one sentence, written by the commander]

## 2 Success criteria
- [measurable]

## 3 Scope
In: · Out: · Boundary rule:

## 4 Decomposition
- [workstream] → [work packages ≤ one session]

## 5 Phases and gates
| M | Phase | Gate condition (event) | Deliverables |
| M-001 | P1 | | |

## 6 Sustainment line
Consumes: [cash · energy · attention · tooling] · Runway: [months] · Attainable: [yes/no, risk posture] · Disruptions planned for: [two]

## 7 Assumptions and risks
| A | Assumption | Category | Impact | Risk if false | Validation | Status |

## 8 Information line
Audiences: · Narrative: · Deny list: · Measure:

## 9 Control process
Sit rep cadence: · Decision points: · Replan triggers:

## 10 Exit and termination
Complete when: · Killed or parked when: · Transition:

## 11 Authority and AI model
Commander: Papi, full. Partner: mission-type orders, 5-80-15.

## Decision ledger
| # | Decision | Blocking? | Ruled |
```

### The gate — checklist

```markdown
GATE [n] — [project] — [date] — event: [what fired]
- [ ] Entry criteria for the next phase met
- [ ] Assumption log reviewed; INVALIDATED rows have triggered their impact review
- [ ] Risks named for the next phase
- [ ] Attainability stated: support exists at acceptable risk (posture: ___)
- [ ] Ends and means reconciled: end state or resources adjusted, or confirmed unchanged with reason
- [ ] Value still present against §1
DECISION: GO / NO-GO / HOLD (blocker: ___ · decider: ___ · converts on: ___)
```

### The assumption — row

`| A-00n | [statement believed true] | Business / Environmental / Process / Technical | §[brief sections] | [what breaks] | [how and when tested] | OPEN |`

---

## Examples

### Example 1 · BVIPDS, retro-fitted (2026-03-19 charter)

The BVIPDS charter is the flow's ancestor and passes as an **L-size, annihilation-mode** brief. Its M-001 to M-007 milestones are event gates keyed to artifacts. Its assumption log carries twelve rows in the six-field format. What it lacked and the flow adds: a declared mode, a sustainment line with runway, an information line, and a hold rule with a conversion date. The April stall on the character system was a HOLD with no conversion date; the flow forbids that state.

### Example 2 · BOLO 24, the studio launch (2026-09-03, first live instance)

An **L-size** venture run in two modes: **annihilation** for the build (the persona, the season beat sheet, the launch library shipped complete) and **erosion** for the climb (monthly revenue gates until the exit threshold). The brief lives in `_PRIVATE/` because it carries the monthly nut and persona internals. Its gates are rent-tied attainability decisions with conservative, on-target, and ideal values. Its information line is the persona's command narrative and deny list. Its open decisions sit in the brief's ledger with the boresight hold recorded as a HOLD carrying a decider and a conversion date. Brief: `_PRIVATE/BOLO-24-charter.md`.

### Example 3 · BOLO 26, the dictation dictionary (S-size)

Five-line brief: end state (the recognizer stops mangling the house lexicon) · intent (fewer misreads without slowing Papi down) · scope (one tool, one dictionary) · done (a session with zero SOP §8 catches) · owner (Claude on BUILD, Papi on INSTALL or PAY). One gate at done. Parked in oscar-mike on the route decision, which is a HOLD with a named decider.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-09-03 | Working assembly from finished holdings on Papi's order (BOLO 25, sequence held: PDFs → MCDP pass → template → BOLO 24). Sources named in frontmatter. Promotes on two uses. |
