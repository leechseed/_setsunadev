---
title: "PMBOK and Ricardo Vargas: Doctrine-Grade Research for Solo AI-Augmented Development"
source_conversation: "Character database system architecture with Dramatica and astrology integration"
created: 2026-02-25
trunk: BLACK
kind: artifact
---

# PMBOK and Ricardo Vargas: doctrine-grade research for solo AI-augmented development

**PMBOK 7th Edition and Ricardo Vargas's methodology offer the missing operational scaffolding for the Bold Venture Development Doctrine — a principle-based framework for value delivery that maps cleanly onto the USMC-McKinsey-DoD architecture already in place.** PMBOK 7's shift from prescriptive processes to adaptive principles mirrors exactly what a solo developer with AI needs: a rigorous but lightweight decision framework that scales from one-person sprints to full production pipelines. Vargas's "Golden Rule of 5-80%" — where humans provide the critical 5% input and final 15-20% judgment while AI handles the middle — is the closest published framework to the cooperative human-AI workflow the doctrine requires. Together, these sources fill the gap between strategic planning (McKinsey/USMC) and operational execution (DoD 5000/game pipelines) with a measurement and adaptation layer that works at every scale.

---

## PMBOK's evolution from 800-page rulebook to principle-based operating system

The PMBOK Guide underwent its most radical transformation in 2021. The **6th Edition (2017)** was an 800-page prescriptive manual organized around 10 Knowledge Areas, 5 Process Groups, and **49 discrete processes**, each with defined Inputs, Tools & Techniques, and Outputs (ITTOs). It was built for large organizations running predictive (waterfall) projects. The **7th Edition (2021)** gutted this structure entirely, replacing it with 12 Principles and 8 Performance Domains — an outcome-focused, methodology-agnostic framework roughly one-third the length. PMI made this shift after global research showed most organizations were using hybrid or agile approaches, rendering the waterfall-centric process model insufficient.

The critical insight for the Bold Venture Doctrine: PMBOK 7 is not a replacement for PMBOK 6 but an **umbrella over it**. The principles define *why* and *what*; the legacy processes (now published separately as the *Process Groups: A Practice Guide*) define *how*. This two-layer architecture — strategic principles above, tactical processes below — maps directly to how the doctrine already separates USMC commander's intent (principle-level) from DoD 5000 milestone execution (process-level). A solo developer can operate at the principle layer daily while dropping into specific processes only when rigor demands it.

The 7th Edition also explicitly positions PMBOK as a **meta-framework** that sits above Scrum, PRINCE2, Lean, Six Sigma, and SAFe. It does not compete with these methodologies but provides the governance and measurement layer they lack. For the doctrine, this means PMBOK principles can serve as the connective tissue between USMC's decision-forcing philosophy, McKinsey's analytical rigor, and the game studio's production cadence — all without forcing any single methodology.

Worth noting: **PMBOK 8th Edition** arrived in November 2025 with 40 processes (down from 49), 6 principles (condensed from 12), and an explicit AI appendix covering automation, assistance, and augmentation strategies. Vargas has already created visual materials for this edition.

---

## The 12 principles and 8 performance domains that matter for solo development

PMBOK 7's 12 Principles are behavioral guides, not process steps. They shape decision-making rather than prescribing actions. For a solo developer working with AI, they sort into three tiers of relevance:

**Tier 1 — directly operational for solo AI-augmented work:**

- **Tailoring** (Principle 7): "Just enough" process — the minimum sufficient to achieve results. This is the principle that licenses stripping PMBOK down to what works for one person. Every project has unique DNA; one-size-fits-all is explicitly rejected.
- **Value** (Principle 4): Success is measured by value delivered, not by on-time/on-budget adherence. For a solo developer, this means shipping working features that users care about, not completing tasks on a Gantt chart.
- **Risk** (Principle 10): Continuously evaluate exposure to both threats and opportunities. This maps directly to USMC's "bias for action balanced by risk awareness."
- **Adaptability and Resilience** (Principle 11): Build the capacity to accommodate change and recover from setbacks. For solo work, this means architecture decisions that allow pivoting without catastrophic rework.
- **Quality** (Principle 8): Build quality into processes and deliverables. Prevents the solo developer's temptation to cut corners when no one is reviewing.

**Tier 2 — requires reinterpretation for solo context:**

- **Stewardship** (Principle 1): Responsible management of resources. For a solo developer, "resources" means personal energy, time, AI compute costs, and technical debt.
- **Systems Thinking** (Principle 5): Projects exist within larger systems. The solo developer must see their work within the ecosystem of users, platforms, dependencies, and market forces.
- **Leadership** (Principle 6): PMBOK 7 says leadership applies to everyone, not just managers. For solo work, this becomes self-leadership — maintaining discipline, making decisions without external validation.
- **Complexity** (Principle 9): Navigate complexity through knowledge, experience, and continuous learning. Solo developers face irreducible complexity in technical decisions that AI can help decompose but not eliminate.
- **Change** (Principle 12): Projects are vehicles for change. Solo developers must manage their own change resistance and scope creep impulses.

**Tier 3 — minimal applicability to solo work:**

- **Team** (Principle 2) and **Stakeholders** (Principle 3): These require significant reinterpretation. For solo AI-augmented development, the "team" is the human-AI cooperative. "Stakeholders" collapses to the developer's relationship with end users and any external dependencies.

The **8 Performance Domains** replace PMBOK 6's Knowledge Areas and describe *areas of focus* rather than process groups. Each domain is active throughout the project, not sequential. For solo development, these map as follows:

| Performance Domain | Solo Developer Application | Doctrine Phase Alignment |
|---|---|---|
| **Stakeholders** | User research, market validation, community feedback | Phase 0 (Intelligence), Phase 5 (Transition) |
| **Team** | Human-AI cooperation model, skill inventory, AI capability assessment | Continuous — defines the cooperative relationship |
| **Development Approach & Life Cycle** | Choosing predictive/adaptive/hybrid per feature or module | Phase 1 (Framing), Phase 2 (Design) |
| **Planning** | WBS decomposition, sprint planning, resource allocation | Phase 2 (Design) |
| **Project Work** | Daily execution, task management, quality adherence | Phase 3 (Build), Phase 4 (Test) |
| **Delivery** | Shipping, deployment, value realization | Phase 5 (Transition) |
| **Measurement** | EVM-lite metrics, velocity tracking, burndown | Continuous — feeds Phase 6 (AAR) |
| **Uncertainty** | Risk register, contingency planning, architectural hedging | Continuous — especially Phase 0 and Phase 1 |

---

## WBS is MECE is problem framing: the structural unity beneath three traditions

The Work Breakdown Structure is PMBOK's primary decomposition tool, defined as a "deliverable-oriented hierarchical decomposition of the total scope of work." Its governing rules are the **100% Rule** (the WBS must capture all work — no more, no less) and **mutual exclusivity** (no overlap between elements). The lowest-level elements are "work packages" from which cost and duration are estimated.

These rules are structurally identical to McKinsey's **MECE principle** (Mutually Exclusive, Collectively Exhaustive), developed by Barbara Minto in the 1960s. MECE governs issue trees, hypothesis structures, and analytical decomposition at McKinsey. WBS governs scope decomposition in PMBOK. Both enforce the same logic: **every element is distinct, and all elements together constitute the whole**. The WBS *is* a MECE tree applied to project scope rather than analytical problems.

The USMC's problem framing doctrine (MCDP 1) adds a third convergent tradition. Marine Corps planning uses **mission analysis** to decompose commander's intent into specified tasks, implied tasks, and essential tasks — a hierarchical decomposition that ensures nothing is missed and nothing overlaps. The Marine Corps' emphasis on "framing the problem before solving it" maps directly to PMBOK's insistence that scope definition (WBS) must precede schedule and cost estimation.

**For the Bold Venture Doctrine, this convergence is powerful.** All three traditions agree: decompose before you execute, ensure completeness, prevent overlap. The practical implementation is a single WBS/MECE tree that serves as the project's structural backbone — what the LEECHSEED system would call the "scope hierarchy" within the SSOT. Every task, every feature, every deliverable traces back to a node in this tree. The tree itself is the artifact that prevents scope creep (PMBOK), ensures analytical rigor (McKinsey), and maintains alignment with commander's intent (USMC).

The WBS also follows practical heuristics that translate well to solo development: the **80-hour rule** (no work package exceeds 80 hours of effort) and the **reporting period rule** (no activity longer than one reporting period). For a solo developer on weekly sprints, this means no work package should exceed one week — forcing decomposition to actionable granularity.

---

## Risk management as the common language across all four source doctrines

PMBOK 6's risk management framework contains 7 processes — the most of any knowledge area — forming a cycle: Plan Risk Management → Identify Risks → Qualitative Analysis → Quantitative Analysis → Plan Responses → Implement Responses → Monitor Risks. The core tools are the **risk register** (central document tracking all identified risks), the **probability-impact matrix** (grid for prioritization), **Monte Carlo simulation** (probabilistic modeling), and **decision trees** (expected monetary value calculations).

This framework shares deep structural DNA with the other doctrine sources:

**DoD 5000 milestone reviews** function as formalized risk gates. Each milestone (Material Solution Analysis, Technology Maturation, Engineering & Manufacturing Development, Production & Deployment, Operations & Support) requires demonstration that risks have been reduced to acceptable levels before proceeding. The DoD's approach is essentially PMBOK's risk framework institutionalized at the program level — you cannot pass a gate without proving risk mitigation.

**AAA game studio greenlight gates** (concept, pre-production, production, alpha, beta, gold master) serve the same function with different vocabulary. A game cannot move from pre-production to production without demonstrating that the core gameplay loop works and that technical risks are manageable. The "vertical slice" milestone is explicitly a risk-reduction artifact — proof that the vision is achievable.

**USMC planning** treats risk as inseparable from decision-making. The Marine Corps' "70% solution executed violently" philosophy acknowledges that perfect risk information is impossible; the goal is sufficient risk awareness to act decisively. MCDP 1's emphasis on "uncertainty as the fundamental condition of war" maps directly to PMBOK 7's Uncertainty Performance Domain.

**For the doctrine's six-phase lifecycle**, risk management is the thread that connects every phase:

- **Phase 0 (Intelligence)**: Risk identification — what could prevent success? PMBOK's "Identify Risks" process using brainstorming, checklists, and assumption analysis.
- **Phase 1 (Framing)**: Qualitative risk analysis — which risks matter most? Probability-impact matrix.
- **Phase 2 (Design)**: Risk response planning — how will we mitigate, avoid, transfer, or accept each risk?
- **Phase 3 (Build)**: Risk response implementation — executing the mitigation strategies.
- **Phase 4 (Test)**: Risk monitoring — are the mitigations working? New risks emerged?
- **Phase 5 (Transition)**: Residual risk assessment — what risks transfer to operations?
- **Phase 6 (AAR)**: Risk retrospective — which risks materialized, which didn't, what did we learn?

For solo development, **quantitative risk analysis (Monte Carlo) is unnecessary** — the overhead exceeds the value. But qualitative analysis (a simple probability-impact matrix maintained in the SSOT) is essential even for one person. Vargas explicitly supports this: his "Done is Better than Perfect" philosophy and 10-step planning process prioritize simple risk awareness over elaborate risk modeling.

---

## Ricardo Vargas: the bridge between rigor and accessibility

Ricardo Viana Vargas is not merely a PMBOK educator — he is one of the most credentialed project management practitioners alive. **Former Chairman of the PMI Board** (first Latin American elected), **PMI Fellow** (highest individual honor), **former Director at UNOPS** managing $1.2 billion in humanitarian projects across 120+ countries, **Executive Director of the Brightline Initiative** (PMI's strategy implementation think tank), author of **16 books** (500,000+ copies, 7 languages), and host of the "5 Minutes Podcast" since 2007 with **14 million views**. He has managed over **$20 billion** in global initiatives across 27 years.

His signature contribution is the **PMBOK Process Flow** — first created in 1998 while studying for the PMP exam. This single-page visual maps all 49 PMBOK 6 processes color-coded by knowledge area, showing only the main connections between them. It transforms an 800-page guide into a scannable diagram. He produces it in four versions: Full (with all ITTOs), Simplified (process names only, A3 printable), Canvas (black-and-white build-your-own), and multilingual editions. All versions are **free under Creative Commons** — a deliberate accessibility choice.

His visual approach follows a principle he calls **"simplification without oversimplification."** The key elements of this philosophy:

- **"Done is Better than Perfect"**: Complex 100-step methodologies with 45 templates are counterproductive. He mandates that his consulting teams complete full project plans within two weeks regardless of project size.
- **"The project is complex enough — simplify management"**: Adding layers of controls and reporting to complex projects creates bureaucracy, not clarity. The management layer should be the simplest part.
- **"No Holy Grail"**: No single methodology is fail-proof. He advocates a "Swiss Army knife approach" — extracting what works from every method. He compares this to building with Lego bricks where different colored sets represent various methods.
- **The Law of Diminishing Returns in PM**: A dedicated podcast episode on how much management is worthwhile — cautioning against both over-management (bureaucracy) and under-management.

For PMBOK 7, he adapted from a process flow to an **infographic** mapping the 12 principles and 8 performance domains, showing how PMBOK 7 serves as an umbrella over all delivery methodologies. The canvas version allows practitioners to physically construct the framework, reinforcing understanding through building rather than reading.

---

## Vargas's Golden Rule of 5-80% defines the human-AI operating model

Vargas's most directly applicable framework for solo AI-augmented development is his **"Golden Rule of 5-80%"**, articulated across multiple podcast episodes and courses:

- **First 5%**: The human provides the prompt — context, specificity, intent, format. This is irreducible human work.
- **Next 75-80%**: AI generates the output — drafts, analysis, code, plans, risk assessments.
- **Final 15-20%**: The human applies intellectual judgment — analyzing, refining, deciding, validating.

This maps precisely to the doctrine's cooperative model. The solo developer is not a coder who sometimes uses AI — they are an **"AI orchestrator"** (Vargas's term) who provides intent and judgment while AI handles execution. Vargas states explicitly: "AI will not replace project managers. It will empower them to lead transformation and drive measurable results." He frames the future PM as someone who "connects the right tools" — the orchestration capability is the competitive advantage.

His **HBR article "How AI Will Transform Project Management"** (February 2023, co-authored with Antonio Nieto-Rodriguez, top-read globally for nine consecutive weeks) identifies six areas of PM disrupted by AI:

1. **Selection and prioritization**: ML-driven pattern detection for faster identification of viable projects, reduced human bias, better portfolio balance.
2. **PMO support**: Automated monitoring, anticipating problems, smarter methodology selection, compliance monitoring.
3. **Planning and reporting**: AI-assisted risk management, automated scoping, scheduling, real-time reporting replacing monthly reports.
4. **Virtual project assistants**: Context-aware bots providing instant status updates (his co-founded **PMOtto.ai** is built for this).
5. **Advanced testing**: Automated testing for early defect detection and self-correcting processes.
6. **Role transformation**: PM shifts from administrative work to soft skills, leadership, strategic thinking, coaching.

His **2025 global survey** (870 professionals, 97 countries) found that AI familiarity in PM has **doubled** in two years, over two-thirds of professionals use AI tools daily, organizations using AI execute projects **up to 25% faster**, **25% achieved over $250,000 ROI**, and **42% of organizations expect AI copilots to manage most project portfolios by 2028**.

For solo development, the practical application is clear: **every PMBOK process that involves generating, analyzing, or reporting information is a candidate for AI execution under human direction.** The developer provides the 5% (what to plan, what risks to consider, what to measure) and AI generates the 80% (the actual WBS draft, risk register, status report, code implementation), then the developer applies the final 15-20% judgment.

---

## Applying Vargas's visual simplification to the LEECHSEED SSOT

Vargas's visual approach offers a directly implementable model for the SSOT documentation system. His key design patterns:

**Color-coding by domain**: Every knowledge area in the PMBOK flow gets a unique color, enabling instant visual identification. The SSOT could apply this to doctrine sources — USMC content in one color, McKinsey in another, DoD in a third, PMBOK in a fourth — so that any document or artifact is immediately identifiable by its doctrinal lineage.

**Multiple fidelity versions**: Full (complete detail), Simplified (titles and connections only), Canvas (build-your-own). The SSOT could maintain three views of every major artifact: a full specification, a one-page summary, and a working template. This matches how Vargas serves different audiences — detailed for practitioners, simplified for executives, interactive for learners.

**Flow-based reading**: Vargas teaches users to read PMBOK as a flow from initiation to closing, not chapter by chapter. The SSOT should present the doctrine lifecycle as a flow — Phase 0 through Phase 6 — with each phase linking to its relevant artifacts, tools, and decision points. The doctrine is read as a journey, not an encyclopedia.

**Canvas/build-your-own**: The interactive construction approach reinforces understanding through doing. For the SSOT, this means templates that a developer fills in for each new project, not pre-filled reference documents. The act of building the project charter, WBS, and risk register from templates forces engagement with the methodology.

**Creative Commons accessibility**: Vargas releases everything free for non-commercial use, maximizing adoption. The doctrine should follow this pattern — the SSOT framework itself is open, while the specific project data within it is private.

The one-page process map concept is particularly valuable. The entire Bold Venture Doctrine — all six phases, all decision gates, all key artifacts — should be expressible on a **single A3-printable visual flow** that a developer can pin above their desk. If the doctrine cannot be simplified to one page without losing its essential structure, it is too complex for solo use.

---

## What scales down and what doesn't: PMBOK for a team of one

PMI has explicitly addressed solo and small-team project management. Sandra Rowe's "Power of One" paper and Hans Marmier's "Managing Small Projects" paper establish clear guidance. Vargas has directly addressed this in podcast episodes about "managing projects where the sponsor, the project manager, and the client are the same person."

**Essential even for one person** (keep at full rigor):

- **Project charter** — even a one-page version defining scope, objectives, constraints, and success criteria. This is the doctrine's Phase 1 output.
- **Scope definition and WBS** — prevents scope creep, which is the solo developer's most dangerous enemy because there is no one else to say "that's out of scope."
- **Risk identification** — even an informal list of "what could go wrong" maintained as a living document. Qualitative probability-impact assessment is sufficient.
- **Change control** — tracking what changes and why. Without this, a solo developer cannot distinguish between strategic pivots and scope creep.
- **Closing/lessons learned** — the retrospective that feeds the next project. This is the doctrine's Phase 6 (AAR).
- **Schedule/timeline** — even a simple task list with dates and dependencies.

**Scales down cleanly** (use simplified versions):

- **Cost management** — simplified tracking, especially of AI compute costs, hosting, and tool subscriptions.
- **Quality management** — checklists and automated testing over formal audits. AI can assist with code review and quality checks.
- **Communications management** — minimal for solo work, but still document key decisions for future reference and for the SSOT.
- **Stakeholder management** — collapses to user research and community engagement.
- **EVM** — the full earned value system is overkill for solo work, but the *concept* of comparing planned vs. actual progress is essential. A simplified version tracking percentage complete vs. percentage of time elapsed captures 80% of EVM's value.

**Becomes unnecessary** (eliminate without guilt):

- **Formal resource management** — team development, RACI matrices, conflict resolution. The "team" is the developer plus AI; the operating model is defined once.
- **Procurement management** — unless the project involves significant external vendors or contractors.
- **Quantitative risk analysis** — Monte Carlo simulation and decision trees are overkill. Qualitative analysis (simple probability × impact scoring) suffices.
- **Formal communications plans** — no audience to communicate to in structured ways.
- **Detailed HR planning** — team charters and organizational charts serve no purpose for one person.

Vargas's guidance reinforces this: his "Done is Better than Perfect" philosophy and two-week maximum planning window prevent the solo developer from spending more time managing the project than doing the project. His 10-step planning process and 10-step tracking process (from his "Urgency" paper) offer a practical minimal viable PM approach.

---

## Mapping PMBOK 7 performance domains to the six-phase lifecycle

The doctrine's proposed lifecycle (Phase 0 Intelligence through Phase 6 AAR) maps onto PMBOK 7's Performance Domains not as a one-to-one correspondence but as a matrix — multiple domains are active in each phase, with varying intensity:

**Phase 0 — Intelligence (PMBOK: Stakeholders + Uncertainty)**
This is the pre-project phase where the developer gathers information, assesses the landscape, and identifies opportunities. The Stakeholders domain drives user research and market analysis. The Uncertainty domain drives initial risk scanning and environmental assessment. PMBOK 6's Initiating process group (Develop Project Charter, Identify Stakeholders) provides the tactical processes. The output is a decision: should this project exist?

**Phase 1 — Framing (PMBOK: Development Approach & Life Cycle + Planning + Uncertainty)**
Commander's intent meets project charter. This phase selects the delivery approach (predictive for well-understood features, adaptive for exploratory work, hybrid as default), defines success criteria, and creates the initial WBS. The Development Approach domain is at peak intensity here — choosing *how* to build. Planning begins with scope decomposition. Uncertainty domain continues with qualitative risk analysis and initial risk response planning.

**Phase 2 — Design (PMBOK: Planning + Measurement)**
The bulk of PMBOK 6's 24 Planning processes concentrate here. The Planning domain reaches peak intensity: detailed WBS, schedule development, cost estimation (even simplified), quality criteria definition. The Measurement domain activates as KPIs and success metrics are defined. This is where EVM baselines are set (if using EVM-lite). For a solo developer, this phase produces the sprint backlog, architectural decisions, and the risk register.

**Phase 3 — Build (PMBOK: Project Work + Delivery + Team)**
Execution. The Project Work domain governs daily task management, quality adherence, and process improvement. The Delivery domain ensures outputs connect to value. The Team domain — reinterpreted as the human-AI cooperative — governs how the developer and AI collaborate. PMBOK 6's Executing processes (Direct and Manage Project Work, Manage Quality, Manage Knowledge) provide tactical guidance. Vargas's 5-80% rule operates here: the developer directs, AI executes, the developer validates.

**Phase 4 — Test (PMBOK: Measurement + Delivery + Uncertainty)**
Validation against requirements. The Measurement domain reaches peak intensity — comparing actual results to planned baselines. The Delivery domain verifies acceptance criteria. The Uncertainty domain monitors for risks that materialized during build. PMBOK 6's Monitoring & Controlling processes (Validate Scope, Control Quality, Monitor Risks) provide the framework. This phase is analogous to the DoD's developmental test and operational test milestones.

**Phase 5 — Transition (PMBOK: Delivery + Stakeholders)**
Deployment and handoff to users/operations. The Delivery domain ensures value realization — not just "it works" but "it delivers the intended benefit." The Stakeholders domain manages user onboarding, documentation, and feedback collection. PMBOK 6's Closing process (Close Project or Phase) provides the tactical checklist.

**Phase 6 — AAR (PMBOK: Measurement + all domains in retrospect)**
After Action Review. This is PMBOK's lessons learned process expanded to a full doctrinal practice. Every performance domain is reviewed: Were stakeholders well-served? Did the human-AI team model work? Was the development approach appropriate? Was planning sufficient? Did execution stay on track? Was value delivered? Were measurements useful? Was uncertainty managed well? The AAR output feeds directly into Phase 0 of the next project, creating the continuous improvement loop that both PMBOK 7 and USMC doctrine demand.

---

## Seven integration recommendations for the Bold Venture Development Doctrine

**1. Adopt PMBOK 7's principles as the doctrine's "standing orders."** The 12 principles (especially Tailoring, Value, Risk, Adaptability, and Quality) function as the PM equivalent of USMC's warfighting philosophy. They do not tell you what to do — they tell you how to think about what to do. Embed these as the doctrine's decision-making guardrails alongside MCDP 1's maneuver warfare principles.

**2. Use the WBS as the single structural backbone connecting all doctrine sources.** The WBS/MECE tree is where McKinsey's analytical decomposition, USMC's mission analysis, PMBOK's scope management, and the game studio's milestone structure converge. Every project starts with a WBS that decomposes scope into work packages no larger than one sprint (the 80-hour rule adapted to solo cadence). This WBS lives in the SSOT and is the master artifact from which schedules, risk assessments, and progress tracking derive.

**3. Implement a simplified gate review system that merges PMBOK risk management with DoD milestones and game greenlight gates.** At each phase transition (0→1, 1→2, 2→3, etc.), the developer conducts a brief self-review using a standardized checklist: Have the entry criteria been met? What risks have been identified and mitigated? Is the project still delivering value? This is a "greenlight gate" requiring explicit go/no-go decision. The checklist should fit on one page and take no more than 30 minutes. Vargas's "two-week maximum planning" principle prevents these reviews from becoming bureaucratic.

**4. Apply Vargas's 5-80% rule as the doctrine's official human-AI task allocation model.** For every PMBOK process that the doctrine retains, define the split: what is the 5% human input (intent, context, constraints), what is the 80% AI execution (draft generation, analysis, code), and what is the 15-20% human judgment (validation, refinement, decision). Document this split for each major artifact (charter, WBS, risk register, status report, retrospective) so the developer has a clear playbook for AI-augmented execution.

**5. Create a one-page doctrine visual flow inspired by Vargas's PMBOK Process Flow.** The entire six-phase lifecycle, with its decision gates, key artifacts, and doctrine sources, should be expressible as a single color-coded A3-printable diagram. Use Vargas's design principles: color-code by doctrine source, show only main connections, provide Full/Simplified/Canvas versions, and release under Creative Commons. This visual becomes the doctrine's primary teaching and reference artifact.

**6. Adopt PMBOK 7's "Development Approach and Life Cycle" domain as the framework for hybrid delivery within each project.** Not every feature in a project needs the same approach. Well-understood components can use predictive planning (detailed WBS, fixed schedule). Exploratory components can use adaptive delivery (sprints, iteration, frequent pivots). The doctrine should make this explicit: at Phase 1 (Framing), each major work package in the WBS is tagged as predictive, adaptive, or hybrid, and the execution approach follows accordingly. This prevents the false binary of "waterfall vs. agile" that undermines many solo developers.

**7. Build the Measurement Performance Domain into the SSOT as an automated dashboard.** Track three metrics continuously: (a) **velocity** — work packages completed per sprint, (b) **risk burn-down** — number of open risks trending over time, and (c) **value delivery** — features shipped and user-facing outcomes achieved. These three metrics, displayed visually in the SSOT, provide the "management with the lights on" that EVM promises without the full EVM overhead. AI can automate the data collection and visualization; the developer provides the interpretation and course correction. This is Vargas's Measurement domain made operational for a team of one.

---

## Conclusion: PMBOK provides the measurement layer the doctrine was missing

The Bold Venture Doctrine already has strategic philosophy (USMC), analytical rigor (McKinsey), milestone governance (DoD 5000), and production pipeline structure (game studios). What PMBOK adds is the **measurement, adaptation, and value-delivery framework** that connects strategy to execution and execution to outcomes. PMBOK 7's principle-based approach prevents the framework from becoming bureaucratic — it scales down to solo work because it prescribes thinking patterns, not process steps. The Tailoring principle explicitly authorizes stripping everything to minimum viable rigor.

Vargas adds the **implementation bridge** — his visual simplification philosophy demonstrates that world-class methodology can fit on one page, his 5-80% rule defines how human-AI cooperation actually works in practice, and his "Done is Better than Perfect" ethos prevents the doctrine from becoming an exercise in documentation rather than development. His co-founded PMOtto.ai and AIPM certification program represent the most developed thinking on AI-augmented project management currently available from any major PM authority.

The deepest insight from this research: PMBOK's WBS, USMC's mission analysis, McKinsey's MECE trees, and Vargas's visual flows are all **the same cognitive operation** — hierarchical decomposition of complexity into actionable, non-overlapping, complete components. The Bold Venture Doctrine does not need four separate decomposition methods. It needs one decomposition discipline, informed by all four traditions, executed through a single SSOT artifact, with AI handling the 80% of generation and the developer providing the 5% of intent and 15% of judgment. That is the operating model these sources collectively describe.