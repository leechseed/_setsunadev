---
title: "Bold Venture Initiative project charter planning"
uuid: 05ff65c2-e731-4a97-b14c-b114f0113a6d
created: 2026-03-19
updated: 2026-03-20
trunk: BLACK
messages: 16
chars: 38236
artifacts: 0
generated_files: 2
tools: [ask_user_input_v0, bash_tool, conversation_search, create_file, present_files, view, web_search]
source: claude.ai-export-2026-08-15
---

# Bold Venture Initiative project charter planning

> **Conversation Overview**

The person is developing the Bold Venture IP Development System (BVIPDS), also known as LEECHSEED, a methodology and toolset for producing medium-agnostic IP sourcebooks at Tolkien-legendarium scale. The project operates under the Bold Venture studio umbrella and encompasses three IPs: OVEREXITOUT (Earth), ASTRO7EX (Moon), and LAKAD (Cislunar). The person works as a solo developer at 10-20 hours per week with a moderate budget and identified emotional momentum as a key driver — stalling is a known failure mode that structured phase gates are designed to prevent. The trigger for formalizing the project charter was a combination of scope discipline needs, momentum requirements, and an unresolved four-option decision point.

The session focused on building two PMBOK 4.1 (Develop Project Charter) output documents from scratch. Claude conducted structured data gathering across four PMBOK input categories: business documents, agreements, enterprise environmental factors, and organizational process assets, drawing on prior conversation context and a series of targeted follow-up questions. Key clarifications established that the real deliverable is the system itself (not any single sourcebook), that OVEREXITOUT serves as the proving ground, that the sourcebook must be legible to a cold reader from day one, and that the scope is Tolkien-legendarium scale covering all four domains: characters, world/setting, plot architecture, and thematic framework. The person is completely solo with no collaborators or external agreements. Tools & techniques were specified as expert judgment and data gathering per PMBOK 6th Edition. Claude delivered two SSOT-compliant markdown files: the BVIPDS Project Charter (covering project purpose, 15 requirements, 7 risks, 7 milestone gates across 4 phases, budget classification, stakeholder list, and exit criteria) and the BVIPDS Assumption Log (12 open assumptions across business, environmental, process asset, and technical categories, each with validation methods tied to milestone gates).

The session concluded with a landscape of PMBOK-aligned project management software spanning open source through enterprise tiers. Claude recommended starting with GitHub Projects since the canonical workspace already exists there, then graduating to Notion or ClickUp Free if more structure was needed. The person selected ClickUp Free for its structured PM features including Gantt views and goals. Claude mapped the charter structure to ClickUp's hierarchy: Space (BVIPDS) → Folders (four phases) → Lists (milestones) → Tasks (work items) → Goals (three success criteria from the charter) → Custom Fields (risk IDs, assumption IDs, SSOT domain tags). The standing discipline established: ClickUp is the tracking layer and dashboard; the Git repository remains the canonical vault. Markdown is the canonical format per REQ-007 and no tool should become an alternative source of truth. The person's preferred working style is explicit direction before execution — Claude laid out full plans and got approval before drafting anything. The person also prefers structured button-based questions for decisions and open prose for nuanced context questions.

**Files produced**

- [bvipds_project_charter.md](../files/2026-03-19_bvipds-project-chartermd.md)
- [bvipds_assumption_log.md](../files/2026-03-19_bvipds-assumption-logmd.md)

---
## 🧑 Papi  <sub>2026-03-19 11:53:33</sub>

Ok I'm developing a project charater for the Bold Venture Initiative. I need to gather some things according to the PMBOK. I want you to pull as much as you can from this project 1. Business documents, 2. Agreeements, 3. Enterprise environmental factors, 4. Organizational process assetts. Before doing anything I need  you to go over what exactly you have planned and give me follow up quetsions that will give you exactly what you need from me

---

## 🤖 Claude  <sub>2026-03-19 11:54:43</sub>

The user wants to develop a Project Charter according to PMBOK methodology for the Bold Venture Initiative. They want me to pull from existing project context across four input categories:

1. Business Documents
2. Agreements
3. Enterprise Environmental Factors (EEFs)
4. Organizational Process Assets (OPAs)

They want me to first outline my plan and ask clarifying questions before executing. Let me search past conversations for relevant context first.Let me pull context from our past conversations to see what I can assemble before laying out a plan.
```
This block is not supported on your current device yet.
```

Let me search for more specific context about project management, PMBOK, and any existing business documentation.
```
This block is not supported on your current device yet.
```

Let me also search for more specific context about the system architecture, scope, and current status.
```
This block is not supported on your current device yet.
```

Let me search for more on tools, constraints, and the current development environment.
```
This block is not supported on your current device yet.
```

Now let me look at the actual project file to understand the current system state better.Good. I've pulled a substantial amount of context. Here's my plan and what I still need from you.

---

## What I Can Assemble From Existing Context

**1. Business Documents** (the "why" — business case, benefits management plan)

What I have:
- Bold Venture is the overarching studio concept wrapping the LEECHSEED IP and its methodology (BVIPDS)
- Three simultaneous IPs: OVEREXITOUT (Earth), ASTRO7EX (Moon), LAKAD (Cislunar)
- The vision is a "Bloomberg Terminal for story" — a rigorous, queryable, automated creative operating system
- The value proposition is separating methodology from content so it's replicable across IPs
- The System Architecture Map (53 components, three-layer model) establishes what the system looks like when complete

What I'm missing:
- Any formal statement of measurable objectives or success criteria
- What "done" looks like for Bold Venture as a business — is this a commercial venture, a personal creative practice, a framework you intend to license, or all three?
- A benefits management plan doesn't exist yet in any form

**2. Agreements** (contracts, MOUs, vendor relationships)

What I have:
- You're the sole developer — no external team agreements
- Tools in use include Obsidian, GitHub, Dramatica, Claude API
- Astro UXDS v7 was adopted as the design system foundation (with licensing implications)
- Creative Commons was discussed as the accessibility model for the methodology itself

What I'm missing:
- Whether any of the tools carry licensing constraints that affect the charter (Dramatica's license terms, for example)
- Whether there are any agreements with collaborators, beta testers, or advisors — even informal ones
- Whether the Creative Commons decision has been finalized or is still conceptual

**3. Enterprise Environmental Factors** (conditions not under your direct control)

What I have:
- Solo developer operating as line cook, menu designer, supply chain manager, and franchise architect simultaneously
- AI-augmented workflow (Vargas's 5-80-15 model referenced)
- Tool stack: Obsidian, GitHub (_setsunadev repo, ShroomsQ workspace), Dramatica, GURPS math foundation, markdown as canonical format, Python/Claude API explored for automation
- Technology choice for the command console application is unresolved (Tauri vs DearPyGui vs hybrid)
- Browser-based tools identified as a limitation — desire for native compiled application

What I'm missing:
- Time availability (hours per week you can dedicate)
- Budget constraints (subscriptions, compute costs, any hard spending limits)
- Physical workspace / hardware constraints
- External deadlines or milestones driving urgency
- Market or industry conditions that affect timing (are you building toward a pitch, a publication, a portfolio piece?)

**4. Organizational Process Assets** (internal knowledge, templates, lessons learned)

What I have:
- Bold Venture Development Doctrine (BVDP) informed by USMC MCDP 1-6, McKinsey, DoD 5000, PMBOK 7, game studio pipelines
- SSOT domain structure: 00-05 (epistemology, narrative frameworks, character systems, plot systems, style guides, operations)
- Narrative Layer Stack: Layers 0-6 (invariant story physics)
- Character Systems Engine (2.01) — partially complete, Victoria Midnight as validation character
- System Architecture Map completed (53 components, 11 undefined interfaces)
- Documentation standard: Marine Corps Doctrinal Publication style, 12-year-old test for plain language
- Lessons learned: scope creep is the recurring enemy, methodology must live outside content, nothing proceeds without explicit direction

What I'm missing:
- Whether a formal lessons-learned register exists beyond what's been discussed in conversation
- Whether there are any existing templates from previous creative projects that should carry forward
- Historical estimation data (how long past sprints/deliverables actually took vs. planned)

---

## Follow-Up Questions

These will fill the gaps I need to write a proper charter.
```
This block is not supported on your current device yet.
```

Good, I've laid out the plan and the follow-up questions. Let me also note the open-ended questions I need to ask in prose.And a few open-ended ones I can't put in buttons:

1. **Budget** — Are there any hard spending limits I should account for? (Claude API costs, tool subscriptions, potential hosting, etc.) Or is this effectively zero-budget beyond what you already pay for?

2. **Agreements/licensing** — Do you have any informal collaborators, advisors, or people you've promised access to any part of this? Even a "yeah my buddy is going to help test it" counts.

3. **What triggered this charter request now?** You've been deep in the character systems engine and the system architecture map. Something made you step back and say "I need a formal project charter." Understanding what prompted the shift helps me frame the charter correctly — is this about getting control of scope, about preparing to onboard someone (even an AI agent), or about forcing yourself through the planning discipline before the next build phase?

Answer the buttons and the three prose questions, and I'll have everything I need to draft.

---

## 🧑 Papi  <sub>2026-03-19 12:53:34</sub>

Q: What is Bold Venture's end state? What does 'success' look like?
A: An IP sourcebook. Basically the system will help me develop the entirety of an IP which can be used in creating content specific to mediums that can pull from it.  please help me develop this consult and advicse

Q: What's your realistic time commitment per week?
A: 10-20 hours/week (serious hobby)

Q: Are there any external deadlines or milestones driving urgency?
A: Emotional urgency — I need momentum or I'll stall

---

## 🤖 Claude  <sub>2026-03-19 12:54:12</sub>

The user has given me clear answers. Let me process these and also note they didn't pick from my predefined options for Q1 - they gave a custom answer that's actually more specific and useful than any of my options. They want an IP sourcebook - a comprehensive canonical reference that can feed any medium (TV, film, games, comics, etc.). This is essentially a "story bible on steroids" - the system builds the sourcebook, and the sourcebook is what gets used by creators working in specific mediums.

They also want me to consult and advise on developing this concept further.

Let me also note they haven't answered the three prose questions yet. Let me address what they gave me and follow up on the remaining gaps.That answer for Q1 is more precise than anything I had in the buttons, and it fundamentally reframes the charter. Let me make sure I understand the implications before proceeding.

An **IP sourcebook** is the deliverable. The BVIPDS (the system, the methodology, the engines) is the *machine that builds the sourcebook*. The sourcebook itself is what has value — it's the canonical, queryable, medium-agnostic reference that a screenwriter, game designer, comic artist, or showrunner could pull from to create content in their specific medium without contradicting anything else in the universe.

This means the project charter isn't for "build a creative operating system" in the abstract. It's for **"produce the OVEREXITOUT IP Sourcebook using the BVIPDS methodology."** The system is the means. The sourcebook is the end. ASTRO7EX and LAKAD get their own sourcebooks later, built by the same machine.

That distinction matters for scope. The charter scopes to the first sourcebook (OVEREXITOUT), and the system development is justified only insofar as it serves that sourcebook's completion. This is also your natural scope-creep defense — if a system component doesn't feed the sourcebook, it's out of scope for this charter.

Now, before I draft anything, I want to pressure-test this framing and fill the last gaps.
```
This block is not supported on your current device yet.
```

Good, waiting for answers. I also still need answers to the three prose questions about budget, agreements/licensing, and what triggered the charter request.And I still need the three prose questions from before when you get a chance:

1. **Budget** — any hard spending limits, or effectively zero-budget beyond existing subscriptions?
2. **Agreements** — any informal collaborators, advisors, or people you've promised access?
3. **What triggered the charter request now?** — what made you step back from building and say "I need formal project management discipline"?

These answers collectively give me everything I need to draft all four PMBOK input categories properly.

---

## 🧑 Papi  <sub>2026-03-19 12:56:20</sub>

Q: Is the charter scope the OVEREXITOUT sourcebook specifically, or the system that produces sourcebooks generally?
A: The system itself — OVEREXITOUT is the test case but the system is the real deliverable

Q: What does a 'complete' IP sourcebook contain? Which of these are essential vs. nice-to-have? (Select all that apply)
A: I want it to be encompassing. I want there to be everything. soemthing along the scale of JRR Tolkein's legendarium of sorts. the entire fabula etc.

Q: Who is the sourcebook's audience? Who pulls from it?
A: It needs to be legible to an outsider from day one

---

## 🤖 Claude  <sub>2026-03-19 12:56:50</sub>

The user has given me very clear answers. Let me synthesize:

1. The charter scope is the SYSTEM (BVIPDS) itself, with OVEREXITOUT as the test case
2. The sourcebook should be comprehensive - Tolkien's legendarium scale - the entire fabula
3. It needs to be legible to outsiders from day one

This changes the framing significantly. The deliverable isn't just "a sourcebook" - it's "a system that produces Tolkien-scale sourcebooks that outsiders can read." That's a much bigger scope statement.

I still need the three prose answers about budget, agreements, and what triggered this. Let me acknowledge what they said, update my understanding, and press for the remaining gaps.


They want all four sourcebook elements - characters, world, plot, thematic framework - and explicitly said "everything," so nothing's off the table. The charter is for BVIPDS development itself, not just the OVEREXITOUT application, which reframes this as a platform initiative. I need to lock in those three remaining questions before moving forward.Good. That sharpens everything considerably. Let me reflect back the picture so we're locked.

**The charter is for BVIPDS — the system.** OVEREXITOUT is the proving ground, not the product. The system is what you're building. The sourcebook it produces is the validation artifact that proves the system works. If the system can produce a Tolkien-legendarium-scale sourcebook for OVEREXITOUT that an outsider can pick up and understand without you in the room, the system is proven. Then ASTRO7EX and LAKAD run through the same machine.

That "legible to an outsider from day one" requirement is a major constraint. It means every SSOT, every template, every output artifact has to pass not just your 12-year-old test for plain language but also a *cold reader test* — someone with zero context about Bold Venture can orient themselves. That's a documentation standard baked into the charter as a quality requirement.

And "everything" for sourcebook scope means the system needs engines for all four domains: characters, world/setting, plot architecture, and thematic framework. Right now you have Engine 2.01 (Characters) partially built and Engine 2.02 (Plot) flagged as not built. World and thematic engines don't appear in the System Architecture Map at all yet. That's scope the charter needs to acknowledge even if those engines are later phases.

I've got enough to draft. But those three prose questions are still the difference between a solid charter and a great one. Specifically the budget and trigger questions — budget tells me about constraints, and the trigger tells me how to frame the urgency section so it actually motivates you when momentum dips.

Can you hit me with those three real quick?

1. **Budget** — any hard limits, or zero-budget beyond what you already pay for?
2. **Agreements** — anyone else involved in any capacity, even informally?
3. **What made you ask for a charter today?** What shifted?

---

## 🧑 Papi  <sub>2026-03-19 13:16:31</sub>

There are two tools & techniques that I want to add to the 4.1 intergration develop project charter 1) expert judgement 2) data gathering. the outputs will be 1) project charter 2) assumption log

---

## 🤖 Claude  <sub>2026-03-19 13:17:00</sub>

The user is specifying PMBOK 4.1 (Develop Project Charter) inputs, tools & techniques, and outputs. They want to add:

Tools & Techniques:
1. Expert judgment
2. Data gathering

Outputs:
1. Project charter
2. Assumption log

They still haven't answered my three prose questions, but they're moving forward with structuring the process. Let me work with this.

In PMBOK 6th Edition, section 4.1 Develop Project Charter has:

Inputs: Business documents, agreements, EEFs, OPAs (which we've been gathering)
Tools & Techniques: Expert judgment, data gathering (brainstorming, focus groups, interviews), interpersonal and team skills (conflict management, facilitation, meeting management)


Outputs: Project charter, assumption log

The user is mapping our approach onto this framework—using expert judgment and data gathering as the mechanisms to produce the charter and assumption log. I should acknowledge this methodical structure and clarify how these tools apply to our specific context, though I'm still waiting on those three prose responses.Understood. So we're running PMBOK 6th Edition 4.1 by the book. Let me lay out exactly what we have mapped and what's left.

**4.1 Develop Project Charter — Current Status**

INPUTS (what we've been gathering):
- Business documents — captured (vision, value proposition, success definition)
- Agreements — partially captured (still need your answer on collaborators/licensing)
- Enterprise environmental factors — partially captured (tools, constraints, solo developer context; missing budget, time confirmed at 10-20 hrs/week)
- Organizational process assets — captured (doctrine sources, SSOT structure, lessons learned, documentation standards)

TOOLS & TECHNIQUES (how we produce the outputs):
- Expert judgment — that's what I'm providing: PMBOK methodology, system architecture consulting, scope framing, risk identification. You're also providing expert judgment on the creative domain, Dramatica, and the IP content itself.
- Data gathering — that's the structured questioning we've been doing across this conversation. Interviews (our back-and-forth), brainstorming (your ideation on sourcebook scope), and the past-conversation mining I ran.

OUTPUTS (what we deliver):
- **Project charter** — the formal document
- **Assumption log** — every assumption we're baking into the charter gets logged separately as a living document that can be validated or invalidated as work progresses

The assumption log is smart. There are already several assumptions embedded in what we've discussed that need to be made explicit rather than silently carried. Things like "the 12-layer character model is the correct granularity," "OVEREXITOUT is a sufficient proving ground for the full system," "one person at 10-20 hours/week can produce a Tolkien-scale sourcebook system."

Before I start drafting both outputs, I need those last three answers to close out the inputs. You've been precise on everything else — these are the final gaps.
```
This block is not supported on your current device yet.
```

Good, waiting for the user's answers to these final questions before drafting.Once these come back, I'll have all four inputs closed and can begin drafting both the project charter and assumption log. Nothing starts until you say go.

---

## 🧑 Papi  <sub>2026-03-19 13:17:41</sub>

Q: Budget constraints for Bold Venture?
A: Moderate budget — willing to invest in the right tools if justified

Q: Is anyone else involved in any capacity?
A: Completely solo — no one else touches this

Q: What triggered the charter request today?
A: All of the above

---

## 🤖 Claude  <sub>2026-03-19 13:18:28</sub>

All inputs are now closed. Let me summarize what I have before drafting:

**INPUTS COMPLETE:**

1. Business Documents:
- Vision: BVIPDS — a system that produces Tolkien-legendarium-scale IP sourcebooks
- OVEREXITOUT is the test case/proving ground
- Success = system produces a sourcebook legible to outsiders from day one
- Sourcebook scope: everything (characters, world, plot, thematic framework)
- Three IPs eventually: OVEREXITOUT, ASTRO7EX, LAKAD

2. Agreements:
- Completely solo — no collaborators
- No external agreements


- Creative Commons under consideration for methodology
- Tool licenses locked in: Obsidian, GitHub, Dramatica, Claude API

3. Enterprise Environmental Factors:
- Solo developer working 10-20 hours weekly with moderate budget flexibility
- Emotional urgency driving the work — momentum is critical to prevent stalling
- Tool stack includes Obsidian, GitHub, Dramatica, GURPS, markdown, and Python/Claude API integration
- Command console technology still undecided
- Scope creep identified as primary risk

4. Organizational Process Assets:
- Drawing from USMC MCDP 1-6 and McKinsey doctrine sources

, plus DoD 5000 and PMBOK 7 frameworks alongside game studio pipeline patterns
- SSOT domain structure (00-05) with a Narrative Layer Stack (0-6) and System Architecture Map covering 53 components with 11 undefined interfaces
- Character Systems Engine partially implemented with Victoria Midnight serving as the validation test case
- Documentation follows MCDP style with the 12-year-old test and cold reader test as quality gates
- Key lessons: scope creep kills projects, methodology shouldn't overshadow content, and explicit direction prevents drift

**TOOLS & TECHNIQUES:**
- Expert judgment from myself on PM and systems, plus creative domain expertise from my father
- Structured interviews throughout this conversation for data gathering

**OUTPUTS:**
- Project charter and assumption log to formalize the plan

I've worked through the follow-up questions you asked for, examining what's actually planned across our conversation.

Now I'm ready to lay out exactly what the charter and assumption log will contain, then get your approval before I draft them.All four inputs are closed. Here is exactly what I plan to deliver, section by section, before I write a single line.

---

## Output 1: Project Charter

The charter will follow PMBOK 4.1 output structure, written in MCDP doctrinal style (declarative, no contractions, no hedging), and will cover:

**Project Purpose / Justification** — BVIPDS exists to produce medium-agnostic IP sourcebooks at Tolkien-legendarium scale. OVEREXITOUT is the proving ground. The system is the deliverable, not the story.

**Measurable Objectives and Success Criteria** — I'll define these around three axes: system completeness (all engines operational), sourcebook completeness (OVEREXITOUT sourcebook passes a cold reader test), and process maturity (the methodology is documented well enough that a second IP can run through the same machine without reinventing anything).

**High-Level Requirements** — Sourcebook must contain characters, world/setting, plot architecture, and thematic framework. System must separate methodology from content. All documentation must pass the cold reader test (outsider legible from day one). All outputs in markdown as canonical format.

**High-Level Project Description / Boundaries** — What's in scope (the system, the OVEREXITOUT proving ground, the four engine domains), what's explicitly out of scope (medium-specific adaptation like screenplays or game design documents, the ASTRO7EX and LAKAD sourcebooks, the command console application beyond prototype).

**Overall Project Risk** — Scope creep (historically the primary threat), solo-developer bottleneck (you are every role simultaneously), emotional momentum dependency (stalling is a known failure mode), and the unresolved four-option decision point that has been blocking forward progress.

**Summary Milestone Schedule** — Phased around engine completion, not calendar dates, since your time commitment is variable. Phase gates tied to the doctrine's existing lifecycle model.

**Pre-Approved Financial Resources** — Moderate budget, justified-per-tool. Current baseline: existing subscriptions (Claude, Obsidian, GitHub). Discretionary spend authorized for tools that directly accelerate sourcebook production.

**Key Stakeholder List** — You. Sole sponsor, sole PM, sole developer, sole consumer (initially). Future stakeholders noted as eventual collaborators/licensees.

**Project Exit Criteria** — What conditions must be true for the charter to be considered fulfilled.

**Assigned Project Manager and Authority Level** — You, with AI (me) functioning as consulting expert providing the 5-80-15 split per Vargas.

---

## Output 2: Assumption Log

A separate living document capturing every assumption baked into the charter. Each entry will have an ID, the assumption statement, the risk if the assumption is wrong, and a validation method. Initial entries I already know need to go in:

- The 12-layer character model is the correct granularity for sourcebook-grade character data
- OVEREXITOUT is a sufficient proving ground to validate the full system
- One person at 10-20 hrs/week can produce a system of this scope
- Markdown is sufficient as the canonical format (no database required at this stage)
- The Base 60 mathematical foundation is stable and does not require revision
- Victoria Midnight is a representative enough test case to validate new components
- The four engine domains (characters, world, plot, thematic) are MECE for sourcebook coverage
- The cold reader legibility standard can be achieved through documentation discipline alone, without a dedicated UI
- Emotional momentum is manageable through structured phase gates rather than external accountability

---

## Delivery Format

Both documents as markdown files, SSOT-compliant (YAML frontmatter, version history table, doctrinal sweep clean). The charter will be the primary file. The assumption log will be a companion file cross-referenced from the charter.
```
This block is not supported on your current device yet.
```

Waiting for the go-ahead.Nothing moves until you say.

---

## 🧑 Papi  <sub>2026-03-19 13:19:06</sub>

Q: Does this plan match what you want? Ready to draft?
A: Go — draft both documents as described

---

## 🤖 Claude  <sub>2026-03-19 13:23:18</sub>

The user wants me to draft both the Project Charter and Assumption Log as markdown files. Let me read the docx skill first to see if that's relevant, but actually they want markdown files, SSOT-compliant. Let me just draft them directly.

Let me think about the structure and content carefully before writing.

For the Project Charter, I need to follow PMBOK 4.1 output structure, written in MCDP doctrinal style. Let me draft both documents.

Let me start writing.
```
This block is not supported on your current device yet.
```

Markdown files, not docx. Let me just write them directly.
```
This block is not supported on your current device yet.
```

Now let me create the assumption log.
```
This block is not supported on your current device yet.
```

Now let me copy both to outputs and present them.
```
This block is not supported on your current device yet.
```

Let me present both files.
```
This block is not supported on your current device yet.
```

Both documents delivered. Let me give a concise summary.Both PMBOK 4.1 outputs delivered. The charter has 15 requirements, 7 risks, 7 milestones, and a four-phase plan scoped to the system (not the story). The assumption log carries 12 open assumptions, each with a specific validation method tied to a milestone gate so nothing drifts unexamined.

The default state is hold. Tell me where you want to go.

---

## 🧑 Papi  <sub>2026-03-20 05:44:04</sub>

give me a landscape of all the pmbok project management software there is from open source to premium offerings. what would work well with this project you think to sort of learn and grow as i do

---

## 🤖 Claude  <sub>2026-03-20 05:45:44</sub>

The user wants a landscape of PMBOK-aligned project management software, from open source to premium, and wants recommendations for what would work well with their specific project (solo developer, IP development system, 10-20 hrs/week, moderate budget, learning PM as they go).

Let me search for current information on this.
```
This block is not supported on your current device yet.
```

Let me search for more specific tools, especially premium ones and ones good for solo developers.
```
This block is not supported on your current device yet.
```

Let me search for a few more specific tools that would be relevant - particularly Notion, Obsidian PM plugins, and tools that integrate with GitHub/markdown workflows.
```
This block is not supported on your current device yet.
```

Let me get one more search for tools that specifically integrate with markdown/GitHub workflows, which is more relevant to this user's setup.
```
This block is not supported on your current device yet.
```

Now let me search for pricing of key tools to give a comprehensive answer.
```
This block is not supported on your current device yet.
```

I have enough information now. Let me organize this into a comprehensive landscape and provide recommendations tailored to this specific project.Here's the landscape, organized from your existing stack outward, with an honest assessment of fit for BVIPDS specifically.

---

## The Landscape

The PM software world breaks into five tiers for your purposes. I'm going to be direct about what matters and what doesn't for a solo creative developer running a markdown-based canonical system at 10-20 hours a week.

**Tier 0: What You Already Have (Free / Already Paying)**

Your current stack — Obsidian + GitHub + Claude — is already a PM system whether you've been using it that way or not. GitHub has Projects (kanban boards, table views, roadmap timelines), Issues (task tracking with labels, milestones, and assignees), and Milestones (map directly to your M-001 through M-007). Your canonical data is already in that repo. The gap isn't tools — it's that you haven't turned on the PM features of what you already own.

There's also **GitHub Projects v2**, which added timeline views, custom fields, and iteration tracking. It's free for public repos, included in your plan for private ones. The WBS lives in your markdown files. The Gantt-equivalent lives in GitHub's timeline view. The risk register and assumption log we just built are already markdown files in the repo.

Additionally, there's a tool called **WBS Markdown** (open source, npm package) that generates Work Breakdown Structure reports from markdown files, designed for software developers who manage their breakdown structure in markdown format. It produces interactive HTML reports from your existing file structure. This fits your workflow like a glove because it doesn't ask you to leave markdown.

**Tier 1: Lightweight Solo Tools (Free or < $10/month)**

**Notion** — Free for individuals. Supports project plans, timelines (Gantt), WBS, RACI, and weekly status reports. The database-centric model is flexible, and there's even a PMBOK-specific template called PMN that tracks requirements, WBS, Gantt, risks, issues, assumptions, stakeholders, costs and procurement across multiple projects simultaneously. The catch: Notion doesn't have a true Gantt chart — it has a timeline view that lacks dependency visualization, drag-and-drop scheduling, critical path analysis, and resource management. For your project this matters less because your milestones are deliverable-gated, not date-gated.

**Todoist** — Free tier is solid for daily task management. No WBS, no risk register, no PMBOK alignment. It's a to-do list, not a project management tool. Useful as a daily companion to a real PM system, not a replacement.

**Trello** — Free tier gives you kanban boards. Its card-based system appeals to visual thinkers, stripping away the learning curve. Good for simple task flow visualization. Too shallow for PMBOK-aligned work — no WBS, no risk tracking, no milestone dependencies.

**Plane** (open source) — Delivers comprehensive features without user limits and supports full self-hosting, with a modern interface and complete open-core model. Think of it as an open-source Linear/Jira hybrid. Good for sprint-based work with issue tracking, cycles, and modules.

**Tier 2: Mid-Range All-in-One ($7-15/month)**

**ClickUp** — Free plan has unlimited members and tasks, paid plans start from $7/user/month unlocking unlimited Gantt charts, integrations, and guests with permissions. The most feature-dense option in this tier. Has native time tracking, goals, dashboards, docs, whiteboards, and automations. The downside: the feature set is considerably more extensive than most competitors, which means a steep learning curve. For a solo developer already fighting scope creep, adding a tool with this much surface area is a risk.

**Airtable** — Merges the best parts of spreadsheets and databases into a project management tool. Starts free, paid at ~$15/user/month. This one is interesting for BVIPDS because your system is fundamentally database-shaped. Character records, engine specifications, interface registries — these are all structured data. Airtable could serve as both your PM tracker AND your queryable sourcebook prototype. The risk: it pulls you away from markdown as canonical format, which contradicts REQ-007 in your charter.

**Linear** — ~$11/user/month. Built for software development teams. Clean, fast, opinionated about workflow. Excellent for sprint-based development with cycles, roadmaps, and issue tracking. Less flexible than ClickUp but far less overwhelming. If you treat each engine build as a "project" and each sub-component as an "issue," Linear's model maps well to your architecture.

**Tier 3: Full PMBOK-Aligned Platforms ($15-30/month)**

**OpenProject** (open source, self-hosted free / cloud from ~$8/user/month) — Supports classic, agile, and hybrid project management with task management, Gantt charts, boards, team collaboration, and time and cost reporting. This is the closest thing to a "real" PMBOK tool in the open-source world. Has WBS support, Gantt with dependencies, risk management, cost tracking, and milestone governance. The tradeoff: it's built for teams, and the interface reflects enterprise-grade complexity.

**ProjectManager** — ~$13/user/month. Full Gantt charts with all four dependency types, critical path, baselines, resource management, and dashboards. This is what a "proper" PM tool looks like. Probably overkill for solo use but would teach you PMBOK mechanics by forcing you through them.

**Wrike** — ~$10/user/month. Provides detailed insights into project progress and status with Gantt charts to visualize project timelines and dependencies. Solid enterprise tool, but like Monday.com, it's designed for teams and charges per-seat minimums that penalize solo users.

**Monday.com** — ~$12/user/month but has a 3-seat minimum billing that makes pricing uncompetitive for solo users. Skip this one.

**Tier 4: Enterprise / Portfolio (> $30/month)**

**OpenPPM (TALAIA)** — Open source, fully PMBOK-aligned. Designed for project and portfolio management in accordance with the PMBOK guide, with EVM tracking in real-time and ISO 21500 reporting. This is the academic answer to "what tool aligns perfectly with PMBOK." The practical answer: it's built for organizations managing dozens of projects with multiple PMs. Massive overkill for solo work.

**Smartsheet, MS Project, Jira Portfolio** — Enterprise tools. Not your lane right now.

---

## My Recommendation

Given your specific situation — solo developer, markdown-canonical, 10-20 hrs/week, learning PMBOK as you go, emotional momentum dependency, moderate budget — here's what I'd actually suggest:

**Start with what you have. GitHub Projects + your markdown files.**

You already have a repo. You already have the charter and assumption log as markdown. Turn on GitHub Projects, create a board with columns mapped to your four phases, create issues for each milestone (M-001 through M-007), and label them. Your risk register lives in markdown. Your assumption log lives in markdown. Your WBS is your System Architecture Map. This costs nothing, adds no new tool to learn, and keeps everything in the canonical workspace.

**If that feels too thin after 4-6 weeks, graduate to Notion or ClickUp Free.**

Notion if you want flexibility and database-thinking (good training for how the sourcebook might eventually be structured). ClickUp Free if you want more structured PM discipline with Gantt views and goal tracking. Both are free for solo use.

**The tool I'd watch but not adopt yet: Linear.**

Linear's opinionated workflow (projects, cycles, issues, roadmaps) maps well to how your engine-building process works. But at $11/month it should be justified per REQ of your charter, and right now GitHub Projects does 80% of what Linear does for free.

**The tool I'd skip entirely: anything that requires you to duplicate your data outside of markdown/Git.** Your charter explicitly states markdown as canonical format (REQ-007). Any tool that becomes the source of truth instead of your repo is fighting your architecture.

The real answer to "what would work well to learn and grow as I do" is: **use the simplest tool that forces you through PMBOK mechanics (charter, WBS, risk register, milestone gates, change control, lessons learned) without adding overhead that competes with your creative work.** GitHub Projects does this today, for free, inside the workspace you already live in.
```
This block is not supported on your current device yet.
```

Good, I've given a comprehensive landscape with a clear recommendation. Let me wait for the user's response.No rush on this one. The charter and assumption log are delivered regardless of which tool you pick — they're markdown files that work anywhere.

---

## 🧑 Papi  <sub>2026-03-20 05:47:13</sub>

Q: Which direction resonates for PM tooling right now?
A: ClickUp Free — I want structured PM with Gantt and goals

---

## 🤖 Claude  <sub>2026-03-20 05:47:45</sub>

The user wants to go with ClickUp Free. Let me think about what would be most helpful here - they want structured PM with Gantt and goals. I should help them understand how to map their BVIPDS charter structure into ClickUp's hierarchy, and maybe offer to help them set it up or create a setup guide.Good choice. ClickUp Free gives you the structure to learn PMBOK mechanics hands-on — Gantt views, goals, milestones, dashboards — without paying anything until you outgrow it. The free tier's limits (60 Gantt chart uses, 5 Spaces, 100MB storage) won't bite you for a while since your canonical data stays in Git, not ClickUp. ClickUp is the tracking layer, not the source of truth.

Here's how your charter maps to ClickUp's hierarchy:

**ClickUp Space** = BVIPDS (the whole project)

**Folders** = Your four phases:
- Phase 1: Foundation & Character Systems
- Phase 2: Plot & World Systems
- Phase 3: Thematic Framework & Integration
- Phase 4: Validation & Process Maturity

**Lists within each Folder** = Milestone work packages (M-001, M-002, etc.)

**Tasks** = Individual work items within each milestone (e.g., "Complete Victoria Midnight Dramatica Ingest," "Propagate mc_problem_element rename," "Write BVDP-1")

**Goals** = Your three success criteria from the charter (System Completeness, Sourcebook Completeness, Process Maturity), each with measurable targets

**Custom Fields** = Risk IDs, assumption IDs, SSOT domain tags, engine references — these let you cross-reference back to your markdown canonical documents without duplicating content

The key discipline: ClickUp tracks *what you're doing and where you are*. The Git repo holds *what you've built*. Never let ClickUp become the place where canonical content lives. It's the dashboard, not the vault.
```
This block is not supported on your current device yet.
```

Waiting for user response.Either way, your charter and assumption log are done and delivered. The ClickUp setup is a configuration task, not a creative decision — it can happen whenever you're ready.