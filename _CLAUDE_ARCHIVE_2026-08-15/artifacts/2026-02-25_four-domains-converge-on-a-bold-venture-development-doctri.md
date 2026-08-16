---
title: "Four Domains Converge on a Bold Venture Development Doctrine"
source_conversation: "Character database system architecture with Dramatica and astrology integration"
created: 2026-02-25
trunk: BLACK
kind: artifact
---

# Four domains converge on a Bold Venture Development Doctrine

**A solo developer working with AI can build production-grade systems by fusing Marine Corps mission command, McKinsey's structural rigor, AAA game studio pipelines, and DoD acquisition gates into a single coherent lifecycle.** The research across all four domains reveals a striking consensus: every high-performing organization separates *intent* from *method*, enforces completeness through structured decomposition, uses decision gates to manage risk, and treats documentation as a living system rather than a static artifact. The differences lie in where each domain places emphasis — the Marines prioritize tempo and adaptation, McKinsey prioritizes analytical completeness, game studios prioritize creative vision, and the DoD prioritizes traceability and verification. A solo-developer doctrine can take the best of each because the constraints of working alone with AI actually mirror the conditions these frameworks were designed for: operating under uncertainty, with limited resources, against complex problems, where speed and quality must coexist.

---

## How the Marines think about building things that work under pressure

The USMC doctrinal publication series (MCDP 1–6) provides the philosophical backbone for any development doctrine. **MCDP-1 (Warfighting)** establishes maneuver warfare as the core philosophy: rather than grinding through problems by brute force (attrition), you shatter complexity by targeting gaps, maintaining tempo, and exploiting success. The doctrine's central insight — that "no plan survives first contact" — leads directly to its most powerful operational concept: **commander's intent**.

Commander's intent articulates *purpose* and *desired end state* without specifying method. When paired with mission-type orders (Auftragstaktik), it creates a system where subordinates — or in the solo-developer case, AI agents — can exercise initiative within a bounded framework. The AI doesn't need step-by-step instructions if it understands the intent. This maps directly to how a solo developer should structure prompts and delegation: define the "why" and the "what done looks like," then let the AI determine the "how."

The **OODA loop** (Observe → Orient → Decide → Act), developed by Colonel John Boyd, is the decision-making engine beneath all Marine operations. Boyd considered **Orient** the most critical phase — the cognitive engine where prior experience, analysis, cultural context, and synthesis converge to create understanding. For a developer, this means the research and analysis phase before writing code is not overhead; it is the decisive activity. The OODA loop's key competitive advantage comes from *operating inside the opponent's loop* — cycling faster than the problem's complexity can overwhelm you.

**MCDP-5 (Planning)** introduces the six-step Marine Corps Planning Process: Problem Framing → COA Development → COA War Game → COA Comparison and Decision → Orders Development → Transition. The most critical step is **Problem Framing** — the doctrine explicitly states that "no amount of subsequent planning can solve a problem insufficiently understood." Planning is treated as a *learning process*, not a deliverable-production process. It separates into three levels: conceptual (art/synthesis), functional (art + science), and detailed (science/analysis). This hierarchy maps cleanly to software development: architecture decisions are conceptual, system design is functional, and implementation is detailed.

**MCDP-6 (Command and Control)** provides the framework for human-AI collaboration: centralized command (the developer sets intent and makes key decisions) with decentralized execution (AI agents carry out tasks with initiative). The doctrine emphasizes **implicit communication through shared mental models** — when everyone shares the same doctrine, vocabulary, and mental framework, explicit coordination overhead drops dramatically. For a solo developer, this means investing in system documentation and conventions creates the "shared mental model" that allows AI to operate with minimal supervision.

The **Systems Approach to Training (SAT)** follows the ADDIE cycle (Analyze → Design → Develop → Implement → Evaluate) with continuous feedback loops. Each phase produces specific outputs that feed the next. The doctrine cycle itself — doctrine → training → execution → assessment → revision — is maintained through After-Action Reviews (AARs) structured around four questions: What was supposed to happen? What actually happened? Why the difference? What do we do better next time? The Marine Corps Center for Lessons Learned (MCCLL) institutionalizes this across the **DOTMLPF spectrum** (Doctrine, Organization, Training, Materiel, Leadership, Personnel, Facilities), ensuring improvements propagate across all dimensions rather than just one.

The Marines explicitly treat doctrine as "a philosophy for action" — a framework, not a rulebook. Every MCDP states this directly. Standardization comes from shared philosophy, common vocabulary, and performance standards. Adaptation comes from mission-type orders, decentralized execution, and the explicit expectation that subordinates will exercise initiative when conditions change.

---

## McKinsey's architecture for ensuring nothing falls through the cracks

McKinsey's contribution to a development doctrine is structural: they provide the methodology for decomposing complex systems so completely that gaps become impossible. The **MECE principle** (Mutually Exclusive, Collectively Exhaustive), developed by Barbara Minto in the late 1960s, is the fundamental tool. At every level of analysis, categories must not overlap (no double-counting, no ambiguity) and must cover 100% of the relevant space (no gaps, no unknown unknowns). Applied to system architecture, MECE means every component belongs to exactly one module, and all modules together compose the complete system.

**Issue trees** operationalize MECE into hierarchical problem decomposition. The root is the core problem framed as a question; Level 1 branches are major MECE categories; subsequent levels break down further until you reach answerable, testable questions. McKinsey consultants use four primary splitting lenses — **stakeholder, process, segment, and math** — to ensure they're decomposing problems from multiple angles. For a development doctrine, this translates directly into system decomposition: you can split a system by user-facing features, by technical components, by data domains, or by arithmetic dependencies (output A feeds input B).

**Hypothesis-driven problem solving** inverts the typical approach. Instead of researching exhaustively and then forming conclusions, McKinsey consultants form an initial hypothesis on Day 1 and then design targeted analyses to prove or disprove it. This prevents "boiling the ocean" — the trap of exploring every possible avenue instead of focusing on what matters. For development, this means: before building, state your hypothesis about what the system should do and how, then build the minimum necessary to validate or refute that hypothesis. This is remarkably similar to the game industry's vertical slice concept.

The **Pyramid Principle** structures all communication top-down: conclusion first, then supporting arguments, then evidence. The SCQA framework (Situation → Complication → Question → Answer) structures introductions. The practical implication for documentation is that any document — a technical spec, a design brief, a README — should be readable at three levels: the 30-second version (top of pyramid / executive summary), the 5-minute version (section headers and bold text), and the deep-dive version (full text with supporting data). McKinsey's "ghost deck" process — building skeleton documents with action titles before filling in content — ensures the narrative is coherent before detail work begins.

The **7-S Framework** (Strategy, Structure, Systems, Shared Values, Style, Staff, Skills) is McKinsey's systems-mapping tool. Its core insight is that **all seven elements must align** — optimizing one in isolation creates dysfunction elsewhere. For a development doctrine, this translates to ensuring that your development philosophy (shared values), your codebase architecture (structure), your tools and processes (systems), your capabilities and AI configurations (skills/staff), and your strategic objectives (strategy) are all coherent and mutually reinforcing.

McKinsey's engagement workflow follows seven steps: Problem Definition → Structure → Prioritize → Analysis Plan → Data Gathering → Synthesis → Recommendations. Quality control is built into the process through ghost deck reviews, daily flash meetings, continuous storyline refinement, and "prewiring" findings with stakeholders before final delivery. **The discipline of writing the storyline on Day 1 and refining it continuously** is perhaps the most transferable McKinsey practice — it forces clarity of thinking from the start rather than hoping coherence emerges from the work.

McKinsey invests **over $600 million annually** in knowledge management. Their Practice Development library stores all engagement artifacts in a structured, MECE-organized system. Consulting Directors serve as knowledge specialists. The culture expects rapid knowledge-sharing — colleagues return calls quickly, project artifacts are deposited for future teams, and "Practice Olympics" surface ideas from all levels. For a solo developer, the equivalent is a well-organized knowledge base (Notion, Obsidian, or similar) where every decision, pattern, and lesson learned is captured and retrievable.

---

## What AAA game studios teach about shepherding creative-technical projects

Game development is the closest analog to what Bold Venture X will actually do — ship entertainment products that blend creative vision with technical execution. The three studios researched (CD Projekt Red, Rockstar, Remedy) represent three different models, all instructive.

**CD Projekt Red** provides the cautionary tale and the recovery playbook. Cyberpunk 2077's troubled launch stemmed from simultaneous engine development and game development, mid-production scope changes (third-person to first-person), and a waterfall methodology that couldn't adapt to cascading problems. Their post-launch transformation ("RED 2.0") moved to **agile with SAFe elements**: 9-week milestone planning cycles with three 3-week sprints, cross-functional teams replacing siloed departments, Miro-based collaborative planning, and a shift from proprietary engine (REDengine) to Unreal Engine 5. Their quest design methodology — particularly the **"Play, Show, Tell" hierarchy** and theme files that define tonal boundaries per region — provides a practical template for content-driven development. CDPR rejects over **90% of quest pitches**, demonstrating ruthless scope discipline.

**Rockstar Games** represents the maximum-quality, maximum-time approach. Red Dead Redemption 2 took **8+ years** with **1,600+ developers** across all global studios functioning as one team. Their methodology is iterative perfectionism: Dan Houser would "reboot, overhaul, and discard large chunks" throughout development. Character bibles documented detailed backstories for all 23 gang members — why they joined, their relationships with every other member, their life before the gang. The game contained **300,000 animations and 500,000 lines of dialogue**. Rockstar's "polish standard" means willingness to delay indefinitely and rebuild extensively. For a solo developer, the lesson is not to emulate Rockstar's scale but to understand their principle: **quality comes from willingness to cut and rebuild**, not from getting it right the first time.

**Remedy Entertainment** is the most relevant model for Bold Venture X. Alan Wake 2 was made by approximately **130 people** with a **€70 million budget** — lean by AAA standards. Sam Lake writes extensive screenplays (hundreds of pages) before and during development, making story the structural foundation. Their "Remedy Connected Universe" demonstrates long-term narrative planning across titles. Each game explicitly builds on lessons from the previous one: Alan Wake → Quantum Break → Control → Alan Wake 2, with each title evolving the studio's approach to player agency, mixed media, and narrative integration. Their adoption of **OpenUSD** for cross-tool, non-destructive workflows represents cutting-edge pipeline thinking. Remedy proves that a small team with a clear creative vision and strong technical pipeline can produce AAA-quality results.

The **vertical slice** is perhaps the single most important concept from game development for a solo developer. A vertical slice is a fully playable, polished section demonstrating ALL core elements working together at near-final quality — typically 5–30 minutes of experience. It validates the complete production pipeline before scaling to full content production. It exposes workflow breakdowns early, creates a shared definition of quality, and proves scalability. The vertical slice differs from a prototype (which proves a single mechanic works) and from an MVP (which is the minimum shippable product). **It is a proof that the full system can be built at the target quality level.**

Game development milestones follow a well-established progression: Concept → Prototype → First Playable → Vertical Slice → Pre-Alpha → Alpha (feature-complete) → Beta (content-locked) → Gold Master. The greenlight gate between pre-production and production requires proving that the core gameplay loop is fun, technically feasible, artistically defined, and realistically scoped. Modern studios have largely replaced the monolithic 100-page Game Design Document with **living wikis and modular documents** in tools like Notion and Confluence, updated in real-time as the game evolves.

**World bibles and character bibles** function as living reference systems organized in tiers: primary (essential narrative the player must experience), secondary (enriching details players may discover), and tertiary (background lore that informs design but may never surface directly). As Control lead writer Anna Megill noted, "Your bible has to accommodate changes while displaying what needs to be in there." The tension between a world bible's established rules and new creative ideas often produces the most interesting results — Control's iconic brutalist aesthetic emerged from the creative friction between "chaotic labyrinth of ever-changing rules" and a rigid architectural style.

---

## The DoD acquisition lifecycle distilled for rapid development

The Department of Defense acquisition system, governed by DoDI 5000.02, provides the most rigorous lifecycle framework of any domain researched. Its five phases — Materiel Solution Analysis → Technology Maturation & Risk Reduction → Engineering & Manufacturing Development → Production & Deployment → Operations & Support — create a complete concept-to-sustainment pipeline with formal decision gates at each transition.

**Milestone reviews** are the critical mechanism. Milestone A (entry to technology maturation) requires a validated capabilities document and analysis of alternatives. Milestone B (program initiation, the critical commitment point) requires **TRL 6** for all critical technologies — meaning a fully functional prototype demonstrated in a relevant environment. Milestone C (entry to production) requires acceptable operational test results and manufacturing readiness. Each milestone demands specific documentation and specific proof before resources are committed. The discipline of "what must be true before we proceed" prevents the premature commitment that killed Cyberpunk 2077's development.

**Technology Readiness Levels (TRLs 1–9)** provide a universal maturity scale from basic principles observed (TRL 1) through operational deployment (TRL 9). For software development, the equivalent progression might be: concept validated in research (TRL 1–3), prototype working in development (TRL 4–5), system demonstrated in staging/test environment (TRL 6–7), production-deployed and battle-tested (TRL 8–9). The key insight is that TRLs are *retrospective* — they measure what has been demonstrated, not what is planned.

The **Adaptive Acquisition Framework (AAF)** revolutionized DoD acquisition by creating six distinct pathways with different speed-rigor tradeoffs. The **Software Acquisition Pathway** (DoDI 5000.87) is most relevant to Bold Venture X: it requires demonstrating viability within **one year** of first funds obligation, uses Agile/Lean methods and DevSecOps, replaces traditional requirements documents with a Capability Needs Statement, and substitutes annual Value Assessments for milestone reviews. The goal is continuous delivery — hours and days, not months and years.

The **Space Force's Space Rapid Capabilities Office (Space RCO)** demonstrates how to operate within a rigorous framework at startup speed. With ~250 people and program teams of **fewer than 12**, Space RCO delivers operational capabilities in **1–3 years** versus the traditional 7–15 year acquisition timeline. Key innovations: contracting officers with up to **$1 billion** delegated authority, JCIDS exemption (requirements driven directly by the operational commander), and "bite-sized" task orders on multi-billion-dollar IDIQ contracts. Their R2C2 program delivered working cloud-based ground control software in **14–15 months**. The philosophy: "velocity, not speed, is king" — sustained pace of delivery matters more than sprinting.

**DevSecOps** in DoD, anchored by Platform One, integrates security throughout the CI/CD pipeline rather than bolting it on at the end. The reference architecture uses containerized microservices on Kubernetes, Iron Bank (hardened container repository), and continuous Authority to Operate (cATO). Releases that previously took **3–8 months** now deploy in approximately **one week**. The principle of "security as code" — automating security checks into every build — is directly applicable to any solo developer's pipeline.

The **DoD systems engineering V-model** provides the verification-validation framework: the left side decomposes (requirements → functional analysis → design synthesis) while the right side integrates and verifies (component testing → integration testing → system verification → operational validation). The critical distinction: **verification** asks "are you building it right?" while **validation** asks "are you building the right thing?" Both questions must be answered at every level of the system.

**DoDAF** (DoD Architecture Framework) provides eight viewpoints for describing complex systems: All (overview), Capability, Data/Information, Operational, Project, Services, Standards, and Systems. While the full DoDAF is excessive for a solo developer, the principle of describing a system from multiple viewpoints — operational (what does it do?), technical (how does it work?), data (what information flows?), standards (what rules apply?) — ensures comprehensive documentation.

---

## Five patterns every high-performing system shares

Across Marines, McKinsey, game studios, and the DoD, five structural patterns recur with remarkable consistency:

**Pattern 1: Separate intent from method.** The Marines call it commander's intent with mission-type orders. McKinsey calls it the governing thought atop the pyramid. Game studios call it the creative vision document. The DoD calls it the capabilities document. In every case, the "what and why" is defined at a higher level and remains stable, while the "how" is delegated and allowed to adapt. For a solo developer with AI, this means: define clear intent documents for every system before implementation, and let AI agents determine implementation approaches within those boundaries.

**Pattern 2: Decompose exhaustively before building.** MECE issue trees, the MCPP's problem framing step, the DoD's functional analysis, and game studios' pre-production phase all insist on understanding the complete problem space before committing to solutions. Every domain has learned — often painfully — that building without complete decomposition creates gaps that compound into systemic failures.

**Pattern 3: Validate with a proof-of-concept before scaling.** The Marines war-game courses of action. McKinsey tests hypotheses before committing to recommendations. Game studios build vertical slices. The DoD requires TRL 6 at Milestone B. All four domains demand tangible proof that a concept works before investing full resources. The vertical slice / TRL 6 concept is the single most important risk-management tool across all domains.

**Pattern 4: Build feedback loops into every phase.** AARs, weekly hypothesis tree reviews, playtest cycles, and developmental testing all create structured mechanisms for learning and adaptation during execution — not just at the end. The USMC's doctrine cycle and McKinsey's continuous storyline refinement both treat the plan as a living hypothesis that must be updated as new information arrives.

**Pattern 5: Documentation serves decision-making, not compliance.** Every domain struggles with the tension between documentation rigor and operational speed. The resolution is consistent: documentation must be structured for rapid comprehension (Pyramid Principle / action titles / commander's intent), organized for completeness (MECE / DOTMLPF / DoDAF viewpoints), and maintained as a living system (wiki-based, continuously updated, versioned). Static documents that nobody reads serve no one.

---

## How each domain maps systems and their relationships

Each domain has developed distinct approaches to the critical challenge of understanding how components relate to each other within larger systems:

The **USMC** uses the **warfighting functions framework** (command and control, intelligence, fires, maneuver, logistics, force protection, information) as a MECE decomposition of all military capability. The MAGTF structure integrates air, ground, and logistics under single command. Relationships are mapped through commander's intent (vertical alignment) and combined arms integration (horizontal coordination). The DOTMLPF spectrum ensures changes are tracked across all organizational dimensions.

**McKinsey** uses **MECE decomposition at every level**, the 7-S Framework for organizational mapping (with explicit interconnecting lines showing every element affects every other), and value driver trees for quantitative dependency mapping (Profit = Revenue - Cost; Revenue = Price × Volume). Their three-level process mapping (Objective → Who → How) ensures completeness at increasing granularity. The key principle: apply multiple splitting lenses (geography, product, customer, math) to cross-check completeness.

**Game studios** use **world bibles and design documents** organized in tiers of importance, with cross-references between narrative elements, gameplay systems, and technical dependencies. CDPR's theme files define boundaries per region. Remedy's "Case Board" system (built on an Entity Component System architecture) explicitly maps narrative connections. Modern studios use visual tools like Miro for dependency mapping and Confluence for cross-linked documentation.

The **DoD** uses **DoDAF's eight viewpoints** to describe the same system from operational, capability, data, services, systems, standards, and project perspectives. The V-model traces requirements down through functional decomposition and back up through integration and verification. Interface Control Documents explicitly define every connection between components. Configuration management maintains three baselines (functional, allocated, product) that track the system's definition at each stage.

For a solo developer, the optimal approach combines McKinsey's MECE decomposition for ensuring completeness, DoDAF's multi-viewpoint principle for describing systems from different angles, the game industry's tiered documentation for prioritizing what matters most, and the USMC's warfighting functions as a template for defining your own MECE functional categories.

---

## Living documentation across all four domains

All four domains have evolved toward treating documentation as a living system, though they arrive there from different starting points:

The **Marines** continuously revise doctrine through the MCCLL feedback loop. MCDP-4 (Logistics) was revised in 2023 to address great power competition — 26 years after initial publication. The T&R Manual system chains training events vertically and horizontally, creating a living web of standards. AARs feed lessons learned into doctrine, training, organization, materiel, leadership, personnel, and facilities changes simultaneously.

**McKinsey's** hypothesis trees are explicitly described as living documents, pruned and regrown weekly as evidence arrives. The ghost deck evolves continuously from Day 1 through final delivery. The Practice Development library stores and makes retrievable all engagement artifacts. Frameworks themselves evolve — the 7-S Framework has been updated to a 12-element "Organize to Value" system for volatile environments.

**Game studios** have moved decisively from static 100-page Game Design Documents to **living wikis in Notion, Confluence, and Miro**. CDPR's agile transformation uses Miro for real-time collaborative planning across 27 teams. Character and world bibles must accommodate changes while maintaining consistency. The modern GDD starts as a 1-page pitch, expands to a concept document, and grows organically as the game takes shape.

The **DoD** maintains configuration management through three evolving baselines, uses continuous Authority to Operate (cATO) to replace point-in-time security reviews, and the Software Acquisition Pathway requires continuous delivery with annual Value Assessments. The Space RCO's "bite-sized task orders" on large IDIQ contracts allow the documented scope to evolve with operational needs.

The common principle: **documentation should be modular, versioned, cross-linked, and structured so that updates in one area automatically signal what other areas need review.** The MECE principle ensures that when one module changes, you know exactly which other modules might be affected (because boundaries are explicit) and which are definitely unaffected (because categories don't overlap).

---

## A full-lifecycle doctrine for solo developer plus AI

Drawing the best from each domain, a Bold Venture Development Doctrine would structure the full lifecycle as follows:

**Phase 0 — Intelligence & Problem Framing (USMC MCDP-2 + MCDP-5 + McKinsey Problem Definition).** Before any building, conduct IPB-equivalent research: what exists in the space, what are the technical constraints, who is the audience, what are the competitive dynamics. Frame the problem using MCPP Step 1. Write a Problem Statement Worksheet (McKinsey format: specific, measurable, action-oriented, relevant, time-bound). Form an initial hypothesis about the solution. This phase produces: a problem statement, environmental scan, and initial hypothesis.

**Phase 1 — Concept & Intent (USMC Commander's Intent + McKinsey SCQA + Game Studio Vision Document).** Define the system's intent: what it must accomplish, why it matters, and what "done" looks like. Structure this using SCQA (Situation → Complication → Question → Answer). Decompose the system into MECE components using issue trees with multiple splitting lenses. Map relationships using a simplified DoDAF approach (operational view: what does it do; data view: what information flows; technical view: how will it work). This phase produces: an Intent Document, a MECE system decomposition, and a relationship map. **Decision Gate: Is the problem worth solving? Is the decomposition complete?**

**Phase 2 — Design & War-Gaming (USMC COA Development + DoD Functional Analysis + McKinsey Hypothesis Tree).** Develop 2–3 courses of action for implementation. War-game each against constraints (time, technical complexity, maintenance burden, scalability). Select the best approach or synthesize from multiple. Conduct functional analysis: decompose high-level functions into component functions, allocate to system elements. Assign TRL equivalents to each component. Write a ghost deck / skeleton document for the full system. This phase produces: selected architecture, functional allocation, component TRL assessment, and skeleton documentation. **Decision Gate (Milestone A equivalent): Is the approach technically feasible? Are all critical unknowns identified?**

**Phase 3 — Vertical Slice (Game Studio Vertical Slice + DoD TRL 6 + McKinsey Hypothesis Testing).** Build one complete, polished section of the system that demonstrates all core elements working together at near-final quality. This is not a prototype (single mechanic) or an MVP (minimum shippable). It is proof that the full system can be built at the target quality level. Test the hypothesis from Phase 1 against this working implementation. Conduct an AAR: What was supposed to happen? What actually happened? Why the difference? What changes? This phase produces: working vertical slice, validated pipeline, AAR findings, and revised plan. **Decision Gate (Milestone B equivalent): Does the vertical slice prove the system can be built? Has the core approach been validated?**

**Phase 4 — Production (CDPR Agile Sprints + DoD EMD + McKinsey Work Plan).** Scale from the vertical slice to full implementation using time-boxed sprints (3-week cycles within 9-week milestones, following CDPR's model). Each sprint has a clear scope derived from the MECE decomposition. AI agents receive mission-type orders: intent document + specific sprint objectives + quality standards, with freedom to determine implementation approach. Continuous testing validates each component against requirements (V-model right side). Weekly AARs maintain the feedback loop. Documentation updates with every sprint — the living wiki grows alongside the codebase. This phase produces: complete, tested system with full documentation. **Decision Gate (Milestone C equivalent): Is the system complete, tested, and documented? Does it meet the original intent?**

**Phase 5 — Deployment & Operations (DoD P&D + O&S + Space RCO DevSecOps).** Deploy using CI/CD pipeline with security integrated throughout (DevSecOps principle). Establish monitoring and feedback collection. Plan for continuous delivery — the system is never "done," only at a current version. Annual Value Assessments (DoD Software Pathway concept) evaluate whether the system still serves its intent or needs strategic redirection.

**Phase 6 — AAR & Doctrine Revision (USMC Doctrine Cycle + McKinsey Knowledge Management).** After each major release, conduct a formal AAR across the DOTMLPF-equivalent spectrum: Does the doctrine need updating? Does the organization of systems need restructuring? Does training/onboarding documentation need revision? Do tools need changing? Apply lessons learned to revise the doctrine itself. The doctrine is a living document that improves with every cycle.

**Cross-cutting principles that govern all phases:**
- **Commander's Intent over detailed instructions** — define purpose and end state; let AI determine method
- **MECE decomposition at every level** — no gaps, no overlaps in system architecture, documentation, or task allocation  
- **Pyramid Principle for all documentation** — answer first, supporting arguments second, evidence third; readable at 30-second, 5-minute, and deep-dive levels
- **Vertical slice before scale** — never commit full resources until the approach is validated with a working proof
- **Living documentation** — modular, versioned, cross-linked wikis that evolve with the system
- **80/20 focus** — prioritize the 20% of components that deliver 80% of value; avoid boiling the ocean
- **Tempo as competitive advantage** — operate inside the problem's OODA loop; sustained velocity over heroic sprints

---

## Conclusion: what makes this doctrine different

The Bold Venture Development Doctrine is not a process document — it is a warfighting philosophy applied to creative-technical development. Its power comes from four fused insights that no single domain provides alone.

From the Marines, it inherits the conviction that **uncertainty is permanent and adaptation is not a failure of planning but its purpose**. The developer who treats every plan as a hypothesis to be tested — not a commitment to be honored — will out-iterate any competitor clinging to a fixed roadmap.

From McKinsey, it inherits the structural guarantee that **completeness is achievable through disciplined decomposition**. MECE is not bureaucracy; it is the mathematical proof that your system architecture has no gaps. The Pyramid Principle is not a writing style; it is a thinking discipline that forces clarity before complexity.

From game studios, it inherits the understanding that **creative vision and technical execution must develop together, not sequentially**, and that the vertical slice is the single most effective risk-management tool available. Remedy's 130-person team producing AAA results proves that constraints breed quality when paired with clear vision and strong pipeline.

From the DoD, it inherits the rigor of **decision gates with explicit criteria** — the discipline of asking "what must be true before we proceed?" at every phase transition. The Space RCO proves this rigor is compatible with 14-month delivery timelines when you strip away unnecessary process and empower small teams with clear authority.

The synthesis produces something none of the four domains has alone: a doctrine that is philosophically grounded (USMC), structurally complete (McKinsey), creatively alive (game studios), and rigorously gated (DoD) — all optimized for the radical constraint and radical freedom of one person working with AI.