---
title: "Project Flow: reference"
type: reference
for: "an agent or Chief looking up a phase, brief section, gate rule, instrument, or size in the project flow"
does: "lists every component of the Project Flow"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_09_operations_project_flow.md
source_version: 0.2.0
---

**Who it's for:** an agent or Chief. They look up a phase, brief section, gate rule, instrument, or size in the project flow · **What it does:** lists every component of the Project Flow · **Type:** reference

# Project Flow: reference

The source has type `ssot_methodology`, category operations, version 0.1.1, last updated 2026-09-15. It applies to BOLD_VENTURE, ULTRASIN, OPERATOR. Status: working, v0.1; it promotes to canonical after two project uses (DOCTRINE 0, Invariant I). Working title: true. BOLO 25. Rung: procedure, NASA four, ruled 2026-09-15 (BOLO 50).

## Core Methodology

### A · The shape: campaign, operation, engagement

MCDP 1-2 supplies the levels: **campaign = project, operation = session, engagement = task**. Every project carries one **end state** (in policy terms: what the finished thing changes in the world). It carries one **intent** (the "in order to" that outlasts any task). It also carries one declared **mode**:

- **Annihilation:** finish the artifact outright; victory is simple and measurable; the build is the main effort.
- **Erosion:** raise the value of the position over time until it yields. A threshold defines victory. The main effort may sit outside the build.

A project that declares neither end state, intent, nor mode has failed before it starts.

### B · The six phases

Phases end on **events** (a decision made, an artifact shipped), never on dates. The writer plans the current phase in detail and carries only intent and two or three options for later phases. Each boundary is a gate ([D](#d--the-gate)).

| Phase | Name | Produces | Gate question |
|---|---|---|---|
| **P0** | **Problem framing** | PIRs named before research · environmental scan · problem statement · initial hypothesis · the command narrative seed | Is the problem worth a project? |
| **P1** | **Concept and intent** | The brief: end state, intent, mode, success criteria, MECE decomposition, phases and gates, sustainment line, information line, control process, exit criteria | Is the problem worth solving? Is the decomposition complete? |
| **P2** | **Design and war-gaming** | Two or three courses of action tested against time, complexity, maintenance, runway · selected approach · skeleton of every deliverable · every critical unknown named · attainability stated | Is it feasible? Are the unknowns named? Is it attainable at acceptable risk? |
| **P3** | **Proof slice** | One complete section at target quality · AAR · revised plan | Does the slice prove the system? |
| **P4** | **Production** | Sprints scoped from the decomposition · mission-type orders to the AI partner · weekly AAR · living documentation | Complete, tested, documented, meets the intent? |
| **P5** | **Transition and operate** | Shipped and monitored · continuous delivery · periodic value check against the intent | Does it still serve the intent? |
| **P6** | **AAR and doctrine revision** | What happened, why, what applies next · revisions to this flow and to the owning registries | none |

P0 and P1 are the commander's work and are not delegated. The AI partner facilitates, drafts, and challenges; the operator writes the intent line.

### C · The brief

A plan without four components is not a plan (MCDP 5): **desired outcome with intent, actions, resources, a control process**. The brief carries those four across eleven sections. It fits one page for a small project and three for a venture. It is written answer-first and passes the ten-second test (SOP §7).

| # | Section | Content | Source |
|---|---|---|---|
| 1 | **End state and intent** | End state in policy terms. One intent sentence the partner can hold in mind. Mode declared. | MCDP 1-1 · MCDP 1 · MCDP 5 |
| 2 | **Success criteria** | Measurable. What must be true for the end state to count. | BVIPDS §2 |
| 3 | **Scope** | In. Out. Boundary enforcement rule. | BVIPDS §5 |
| 4 | **Decomposition** | MECE tree of workstreams; work packages no larger than one session. | PMBOK/Vargas · McKinsey |
| 5 | **Phases and gates** | Event-gated milestones M-001..., each with gate condition and deliverables. | BVIPDS §7 · MCDP 1-2 |
| 6 | **Sustainment line** | What the project consumes (cash, energy, attention, tooling) · runway in months · the attainability statement and risk posture (avoid, accept, mitigate, transfer). One sentence plus branches for the two most likely disruptions. | MCDP 4 |
| 7 | **Assumptions and risks** | The assumption log ([E](#e--the-instruments)). Reviewed at every gate. | BVIPDS assumption log |
| 8 | **Information line** | Audiences, internal and external · the narrative, nested under the trunk narrative · the deny list (what is protected, from whom, how; what lives in `_PRIVATE/`) · the measure of narrative effect. | MCDP 8 |
| 9 | **Control process** | Sit rep cadence · decision points · the signals that trigger replanning. "The plan contains the means for changing the plan." | MCDP 5 · MCDP 6 |
| 10 | **Exit and termination** | When the project is complete. When it is killed or parked. Transition and reconstitution. | BVIPDS §10 · MCDP 1-2 |
| 11 | **Authority and the AI model** | Commander: Chief, full authority. Partner: mission-type orders, 5-80-15 split (intent, execution, judgment). The partner informs; it does not wait for permission inside the intent. | BVIPDS §11 · MCDP 1 · MCDP 6 |

### D · The gate

A gate is a decision, not a meeting. It happens when the phase event fires, fits one page, and takes under thirty minutes. Three doctrines meet in it:

- **Attainability (MCDP 4):** sufficient support exists to start the next phase at an acceptable level of risk. The gate states it and names the risk posture.
- **Ends-means reconciliation (MCDP 1-1):** when resources fall short, cut the end state or seek more. When the position is stronger than expected, expand. A gate that passes without touching either has not been run.
- **The greenlight checklist (PMBOK/DoD/studio gates):** entry criteria met · assumptions reviewed · risks named · value still present.

The gate returns one of three words:

- **GO:** the next phase opens, and resources commit inside its horizon.
- **NO-GO:** the project is killed or parked with Oscar Mike, and the reason is logged.
- **HOLD:** allowed only when it names the single blocking decision and the decider. It must also name the date the hold converts to a call. An unnamed hold is the stall pattern.

### E · The instruments

| Instrument | Lives in | Rule |
|---|---|---|
| **The brief** | the project's home (`_PRIVATE/` when it carries finances or persona internals; the domain folder otherwise) | §C, one to three pages |
| **Assumption log** | beside the brief | ID · assumption · category · impact · risk if false · validation method · status OPEN / VALIDATED / INVALIDATED / REVISED |
| **Decision ledger** | [STATE.md](../../../../STATE.md) "Blocked on you" for the operation; a `# · Decision · Blocking?` table inside the brief for the project | closed rows are struck through with the ruling date, never deleted |
| **Task register** | [BOLO.md](../../../../BOLO.md) | captured the turn it is spoken |
| **Portfolio board** | [PROJECTS.md](../../../../PROJECTS.md) | volume ranking and leverage ranking, both |
| **Backlog** | [oscar-mike/](../../../../oscar-mike/) | park with a card; sweep promotes or clears |
| **Session handoff** | `_CACHE/` → `_LOG/` | the note at ENDEX is the AAR of the session |
| **Gates sheet** | inside the brief §5 and §6 | a measured condition authorises a specific spend (lab-venture G1-G3 pattern) |
| **Status vocabulary** | everywhere | 🟢 locked · 🟡 in motion · 🔴 open decision · ⚪ parked · 📄 artifact exists, needs recovery |
| **Main effort** | [STATE.md](../../../../STATE.md) | one at any moment; a redesignation that does not move support is nominal |

### F · Cadence and control

Control is the feedback returning from the action, not the orders going out (MCDP 6). The prowords are the control system:

- **Session = one OODA cycle.** Open on the sit rep (observe, orient). Decide. Act under mission-type orders. Close on ENDEX; the cache note is the feedback that starts the next cycle from a changed situation.
- **Sit rep** is the control mechanism, in fixed blocks. Block V (blocked on you) is the decision ledger surfaced. A sit rep that shows only enabling actions for several cycles is the alarm.
- **How copy** is explicit feedback: the readback confirms the shared image before execution consumes time.
- **Boresight** is implicit understanding built before execution.
- **BOLO capture** is the alarm channel: lateral, immediate, the same turn.
- **Weekly AAR** in P4 and P5: what happened, why, what applies next. Recorded, never verbal only.
- **PIRs before research.** The operator names the two or three questions whose answers change the decision.

### G · Standing principles

Ten cross-cutting principles, each derived from a source:

1. **Commander's intent over instructions.** Purpose and end state; method left open. (MCDP 1)
2. **MECE at every level.** No gaps, no overlaps in scope, documentation, or task allocation. (McKinsey, PMBOK)
3. **Answer first.** Every document readable in thirty seconds, five minutes, and in depth. (Pyramid Principle, ratified)
4. **Proof slice before scale.** No full commitment until one complete piece proves the approach. (studio pipelines, DoD TRL) The proof slice is this flow's own gate. It is not the LEECHSEED Vertical Slice in 02 (IF catalog call 9, ruled 2026-10-05).
5. **Living documentation.** STATE.md is the plan; a plan not updated after contact is a static document. (MCDP 5)
6. **Launch with what is in hand.** The flow runs from the current repo and kit. Otherwise it is not the flow. (MCDP 3)
7. **Detail only the current horizon.** Later phases carry intent and options. (MCDP 1-2, MCDP 5)
8. **Tempo over heroics.** Simultaneous work, the next step queued, decentralized decisions inside the intent. (MCDP 1-2, MCDP 1-3)
9. **Webs, not chains.** One income source, one tool, or one file everything depends on is a chain. Audit for a second path. (MCDP 4)
10. **Tolerate mistakes of action, not inaction.** (MCDP 1, MCDP 6)

### H · Tailoring

The compressed default is **brief, gate, sit rep, ENDEX.** Everything else is expansion.

| Size | What it is | Brief | Gates | Information line | Sustainment line |
|---|---|---|---|---|---|
| **S** | a BOLO, a tool, a doc | five lines: end state · intent · scope · done · owner | one, at done | none | none |
| **M** | a system build | full brief, one page | P1 · P3 · P4 | if it ships outward | one sentence |
| **L** | a venture, an IP release | full brief, up to three pages | every phase | required | required, with runway and attainability |

### I · Governance

DOCTRINE 0, ratified 2026-09-03, is the promotion mechanic. The flow is v0.1 working and promotes to canonical after two project uses (Invariant I: earned, not declared). P6 of every project may revise it; revisions carry a version row. A rule not used in two projects is struck at the next revision.

## Implementation

### Starting a project

Seven steps:

1. **P0 in one sitting.** Name the two or three PIRs. Scan the environment against them. Write the problem statement. Form the hypothesis. Seed the command narrative. Decide: project, BOLO, or nothing.
2. **Write the brief (P1).** Use the blank below. The operator writes §1 personally. The partner drafts §3 to §9 from the holdings and the operator rules each. Declare the mode. Set milestones as events.
3. **Gate 1.** Worth solving; decomposition complete. GO opens P2 with its resources.
4. **Run sessions under the SOP.** Sit rep opens, and how copy closes orders. Boresight runs when spoken, and BOLO capture runs the same turn. ENDEX closes with the cache note and the STATE update.
5. **Gate on the event.** When the phase event fires, run the gate checklist. Record GO, NO-GO, or HOLD with its conversion date in the brief's decision ledger and in STATE.md.
6. **AAR** weekly in P4 and P5, and at every gate. Three questions, recorded.
7. **Close.** Confirm the exit criteria are true, then run the P6 AAR. Then update the registries, mark the brief complete, and sweep the project's cards from oscar-mike.

### The brief — blank

The blank is a fenced template with these headings: `# BRIEF — [project] · size [S/M/L] · mode [ANNIHILATION/EROSION] · v0.1 · [date]`. The template then holds eleven sections. Section 1 is End state and intent (End state, Intent). Section 2 is Success criteria. Section 3 is Scope (In, Out, Boundary rule). Section 4 is Decomposition (workstream to work packages of one session or less). Section 5 is Phases and gates (table M, Phase, Gate condition (event), Deliverables). Section 6 is Sustainment line (Consumes, Runway, Attainable, Disruptions planned for: two). Section 7 is Assumptions and risks (table A, Assumption, Category, Impact, Risk if false, Validation, Status). Section 8 is Information line (Audiences, Narrative, Deny list, Measure). Section 9 is Control process (Sit rep cadence, Decision points, Replan triggers). Section 10 is Exit and termination (Complete when, Killed or parked when, Transition). Section 11 is Authority and AI model (Commander: Chief, full. Partner: mission-type orders, 5-80-15), and a Decision ledger table (#, Decision, Blocking?, Ruled).

### The gate — checklist

The checklist header reads `GATE [n] — [project] — [date] — event: [what fired]`. Its six boxes:

- Entry criteria for the next phase met
- Assumption log reviewed; INVALIDATED rows have triggered their impact review
- Risks named for the next phase
- Attainability stated: support exists at acceptable risk (posture: ___)
- Ends and means reconciled: end state or resources adjusted, or confirmed unchanged with reason
- Value still present against §1

Its last line is `DECISION: GO / NO-GO / HOLD (blocker: ___ · decider: ___ · converts on: ___)`.

### The assumption — row

The row format follows. `| A-00n | [statement believed true] | Business / Environmental / Process / Technical | §[brief sections] | [what breaks] | [how and when tested] | OPEN |`.

## Examples

### Example 1 · BVIPDS, retro-fitted (2026-03-19 charter)

The BVIPDS charter is the flow's ancestor and passes as an **L-size, annihilation-mode** brief. Its M-001 to M-007 milestones are event gates keyed to artifacts. Its assumption log has twelve rows in the six-field format. The flow adds what it lacked: a declared mode and a sustainment line with runway. It also adds an information line and a hold rule with a conversion date. The April stall on the character system was a HOLD with no conversion date; the flow forbids that state.

### Example 2 · BOLO 24, the studio launch (2026-09-03, first live instance)

An **L-size** venture runs in two modes. The first is **annihilation** for the build (the persona, the season beat sheet, the launch library shipped complete). The second is **erosion** for the climb (monthly revenue gates until the exit threshold). The brief lives in `_PRIVATE/` because it carries the monthly nut and persona internals. Its gates are rent-tied attainability decisions with conservative, on-target, and ideal values. Its information line is the persona's command narrative and deny list. Its open decisions sit in the brief's ledger. The ledger records the boresight hold as a HOLD carrying a decider and a conversion date. Brief: `_PRIVATE/BOLO-24-charter.md`.

### Example 3 · BOLO 26, the dictation dictionary (S-size)

A five-line brief: end state (the recognizer stops mangling the Command lexicon) · intent (fewer misreads without slowing Chief down) · scope (one tool, one dictionary) · done (a session with zero SOP §8 catches) · owner (Claude on BUILD, Chief on INSTALL or PAY). One gate at done. Parked in oscar-mike on the route decision, a HOLD with a named decider.
