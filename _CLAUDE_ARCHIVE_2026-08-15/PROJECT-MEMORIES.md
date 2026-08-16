---
title: "Project memories (claude.ai)"
kind: memory
source: claude.ai-export-2026-08-15
---

# Project memories

What claude.ai had retained about each project. Highest-density summary of your own architecture in the entire export.


---

## BOLD VENTURE

**Purpose & context**

Papi is the sole developer and creative director of **Bold Venture**, a studio building medium-agnostic IP sourcebooks at Tolkien-legendarium scale. The real deliverable is the **BVIPDS (Bold Venture IP Development System)** — also called LEECHSEED — a methodology and toolset for producing structured, deeply interconnected story IPs. Three IPs are in development: **OVEREXITOUT** (Earth, proving ground), **ASTRO7EX** (Moon), and **LAKAD** (Cislunar). Success looks like a system legible to a cold reader, capable of generating sourcebooks across all four domains: characters, world/setting, plot architecture, and thematic framework.

A critical architectural distinction governs the whole project: the **Narrative Layer Stack** (Layers 0–6, the invariant in-world physics of the story) is separate from the **SSOT Domain Structure** (domains 00–05, the development methodology). The IP Engine (creative operating system) must remain distinct from the Development System (the meta-process that builds it) — analogous to how SCRUM sits above, not inside, the work it governs.

Emotional momentum is a key driver; stalling is a known failure mode that structured phase gates are designed to prevent. Papi works solo, roughly 10–20 hours per week.

**Victoria "Tori" Midnight** is the canonical validation character and narrative anchor for all system development.

---

**Current state**

- The **ShroomsQ** GitHub repository is the canonical workspace, with `_CANON/_SSOT/00–05` domain folders on disk. The `_GOON_ROOM` pipeline is dormant and an old Obsidian vault is in transitional archive status.
- **ClickUp Free** is the project tracking layer (Space → Folders → Lists → Tasks → Goals hierarchy); the Git repo remains the canonical vault. Markdown is the canonical format (REQ-007).
- The **12-Layer Character Database** is architecturally established, with Layer-Locked Modules as the expansion protocol (new modules attach as sub-tables under existing layers, not as additional core layers).
- A **BVX-CR v1 merged format** has been developed: a two-tier document combining a human-facing BVX-LEARN one-sheet (Tier 1, terse imperative voice) with an AI-facing Canonical Review (Tier 2), internally linked. Two files exist: `mating-in-captivity-BVX-CR.md` (proof of concept, ~14,600 words) and `BVX-CR-merged-template.md` (reusable generator spec with voice rules, linking contract, fidelity rules, build sequence, and prompt shortcuts including "BVX-CR this").
- The Narrative Layer Stack already has substantive content, including five Layer 0 ontological axioms written in doctrinal one-liner style.
- Open character system tasks: Victoria Midnight Dramatica Ingest (~65 fields), `mc_problem_element` field rename propagation across all SSOTs, and Base 60 recalibration propagation to Vertical Slice point budget tables.

---

**On the horizon**

- Deciding whether to convert BVX-CR into a Claude Skill; selecting the next book to process through BVX-CR.
- Resolving the four-option architectural decision point (last recorded as open): Option A — inventory/consolidation pass; Option B — lock Narrative Layer Stack as first formal SSOT; Option C — set up dev environment/tooling first; Option D — close out Character Systems Engine before starting anything new.
- TV Tropes integration: Phase 2 (bootstrapping the Canonical Trope Index organically via Tori) vs. defining the index schema document first. Dataset acquisition from TVTDB on Kaggle is Phase 1.
- Building out the pornography-taxonomy tagging component under L9 EROS (with foreign key references to L2 VITAL body data) per the established architectural recommendation.
- Potential RAG pipeline build using ChromaDB or LlamaIndex for the knowledge base.

---

**Key learnings & principles**

- **Separation of axes is non-negotiable**: conflating the Narrative Layer Stack with the SSOT Domain Structure is a category error that causes downstream architectural damage.
- **The Development System must stay above the IP Engine**: embedding methodology inside creative content breaks the system's generalizability.
- **Layer-Locked Modules**: the 12-layer core is invariant; expansion happens via sub-tables, not layer proliferation.
- **Fidelity discipline**: vocabulary bleed from sibling files is a real risk — cross-contamination must be caught and flagged explicitly (as demonstrated in the Perel BVX-CR build).
- **ClickUp tracks; Git canonizes**: no project management tool becomes an alternative source of truth.
- **Stalling is the primary failure mode**: phase gates and explicit scope discipline exist specifically to prevent momentum collapse from multi-role context switching (creative, architectural, operational roles interfering with each other).
- **Scope before execution**: nothing proceeds until Papi explicitly directs which option to pursue.

---

**Approach & patterns**

- **Communication style**: casual, stream-of-consciousness input; expects terse, high-density output. Marine Corps Doctrinal Publication standards for documents — declarative, laconic, authoritative, no contractions or hedging.
- **Decision protocol**: structured button-based options for discrete decisions; open prose for nuanced context questions. Full plan laid out and approved before execution begins.
- **Naming and systems thinking**: thinks in frameworks and named systems; assigns IDs and codenames (MSX.16, BVX-CR, LEECHSEED, GOON_ROOM, etc.).
- **Validation via vertical slice**: new systems are proven on Victoria Midnight before broader rollout.
- **Plain language standard**: all variable descriptions and trait names must pass a "12-year-old test" — no academic jargon, conversational behavioral consequences (GURPS/LoL ability-description style).
- **Document format**: SSOT-compliant markdown throughout; one-sheet catalog uses BVX-LEARN format with MSX.## IDs.

---

**Tools & resources**

- **Canonical workspace**: GitHub (ShroomsQ repository)
- **Project tracking**: ClickUp Free
- **Knowledge/notes (transitional)**: Obsidian (legacy vault in archive)
- **Character system foundation**: GURPS mechanics (mathematical base), Dramatica theory (narrative structure), League of Legends ability formatting (trait descriptor style)
- **RAG pipeline candidates**: ChromaDB, LlamaIndex, LLM APIs
- **TV Tropes data**: TVTDB dataset on Kaggle (static snapshot)
- **Book extraction format**: BVX-CR v1 (merged template + worked Perel proof)
- **Browser automation**: Claude in Chrome extension (used for YouTube playlist extraction)

---

## 🧬 BVX-LEARN — One-Sheet Factory

**Purpose & context**

Papi is building a structured knowledge management system called **BVX-LEARN** — a markdown-based vault that produces standardized "one-sheet" reference documents extracted from books and PDFs. The primary use case is character study material for creative writing, with a focus on psychological depth, subculture documentation, and autoethnographic character construction. The vault is organized by domain codes (three-letter prefixes) and sequential serial numbers (e.g., MSX.01).

Papi has a parallel interest in a **fictional character creation system** using astrology as a multi-layered structural scaffold, mapping planetary lenses (Sun, Moon, Venus, etc.) to distinct psychological domains. This project takes a project-management-style approach: assemble raw knowledge sources first, then plug them into architecture.

---

**Current state**

The vault currently contains entries across five domains: MSX (Male Sexuality & Seduction, .01–.15), PSY (Psychology & Mindset, .01–.07), PHI (Philosophy & Spirituality, .01–.03), CRE (Creative & Narrative, .01), and BIZ (.01). Cross-reference architecture is built into the `related` field of each entry, with notable opposing-philosophy pairings and thematic linkages documented across entries.

A workflow question was recently explored: whether to migrate from Claude.ai Projects to **Claude Code** for vault operations. Claude Code was identified as better-suited because it can read/write `.md` files directly from disk, eliminating the current two-step output process. A `CLAUDE.md` file with imported context was proposed as the migration path. This transition appears to be under consideration but not yet completed.

One-sheets generated from research (rather than full source texts) are marked `status: draft`. One thin source was handled via web research and marked permanent per Papi's instruction.

---

**On the horizon**

- Consulting/advisory deep-dives on existing MSX entries one at a time to develop greater depth before modifying files — the session ended mid-consultation on MSX.01 with five specific gaps identified
- Potential upload of Papi's own IP documents to provide context for how vault entries connect to a broader framework
- Possible migration to Claude Code with a purpose-built `CLAUDE.md` incorporating modular `@path/to/file.md` imports
- Continued development of the astrological character scaffold, with a comprehensive field manual (traditional vs. modern frameworks, eleven planetary lenses, esoteric integration paths) already generated as a foundation

---

**Key learnings & principles**

- The vault's cross-reference architecture is a core feature — entries should note related entries and opposing frameworks (e.g., consent-centered vs. prescriptive approaches on the same thematic axis)
- Draft status should be flagged explicitly when sources weren't read in full; web research can substitute for thin sources when marked appropriately
- For the astrological system: traditional rulerships serve as structural core, modern co-rulers layer on as transformational arc — described as "a soft barrier with the door open"; the Moon is the primary lens for emotional needs
- Claude Code's file I/O capability eliminates friction in the vault workflow compared to the current copy-to-outputs process

---

**Approach & patterns**

- **Assembly-line processing mode**: no questions between PDFs, autonomous domain assignment and serial numbering, consistent format adherence
- **Directive and efficiency-focused**: Papi makes architectural decisions; Claude executes
- **Knowledge-first, synthesis-later**: raw sources and breadth are preferred over pre-digested conclusions; decisions deferred until the knowledge base is assembled
- **Consulting mode** for depth development: discussion precedes any modifications to actual markdown files
- All sexually explicit source material is treated as published research or subculture documentation — processed without editorializing

---

**Tools & resources**

- **Platform**: Claude.ai Projects (current); Claude Code (under consideration for migration)
- **File system**: outputs saved to `/home/claude/` and `/mnt/user-data/outputs/`; future Claude Code setup would use local `.md` files with `CLAUDE.md` as persistent context
- **One-sheet format fields**: Core Thesis, Invariants, Heuristics, Core Concepts, Key Vocabulary, Notable Quotes, What Doesn't Work, Quick Self-Check, `related` field for cross-references
- **Astrological framework resource**: comprehensive field manual artifact generated covering Hellenistic/traditional, psychological/modern, predictive techniques, and optional esoteric tier (Tarot, Qabalah, alchemy, chakra systems)

---

## cc

**Purpose & context**

Papi is a cook/kitchen worker and storyteller-entrepreneur building a project called **Bold Venture X (BVX)** — a creative writing/storytelling venture that has been a primary long-term anchor for him. BVX stalled during a period of intense focus on an interpersonal situation at work, and Papi has been encouraged to reopen it as a way of rebuilding independent emotional foundation.

Papi works in what appears to be a food service environment and is navigating a significant ongoing dynamic with a coworker named **CC (Cyaria/[CC])**, roughly 15 years his junior, toward whom he has deep feelings. His stated priority hierarchy: her wellbeing first, genuine friendship, with any romantic dimension last and on her terms. He is also developing a playful, present-moment register of interaction with her — what he calls his **"Rickards mode"** (from Rickards High School, IB program) — a more relaxed, ambient, in-the-moment conversational style he accesses naturally when stakes feel low but loses when monitoring kicks in.

Key coworkers: **Mary** (high Neuroticism/Openness, garden connection, caterpillar supply chain), **Ian**, **Kamal**, and **Scout** (28-year-old GM at a nearby business; described as easy, safe, and comfortable to talk to — flagged as meaningful signal about what Papi actually wants in a partner).

Papi communicates via **voice-to-text dictation** (stock phone dictation handles his speech poorly and produces phonetic garbles — e.g., "records" for Rickards). **Interpret transcripts phonetically; confirm unclear proper nouns rather than guessing.** He has recommended **Wispr Flow** as a better dictation option. He also writes in raw, casual, stream-of-consciousness style, especially when flooded emotionally.

---

**Current state**

The CC dynamic is the active center of gravity. Key developments:
- CC brings recurring fear about job security to Papi on a cycle (roughly every few weeks); Claude has framed this as a trust signal and a pattern of low-risk emotional contact, not situationally triggered crisis — and has flagged the risk of Papi becoming her primary emotional regulator for this loop.
- CC has responded better to **specific, concrete evidence** than to general verbal reassurance — this principle is established and should be held.
- Papi has identified a core suppression problem: the monitoring mindset (tracking how things land, fear of shutdown) activates a rival circuit that blocks the playful, present-moment register he wants to access with CC.
- Practical flirting/banter material developed: directional rules for teasing (up/sideways, never down), feeder responses, return-fire options beyond mock grief (agree-and-amplify, the reversal, deadpan literalism, the jury, one-word-plus-look), reading CC's "flick-and-stay" signal, and handling her ambient social provocations and lonely-corner moments.
- Existing material with bit potential: **the perfume** and **the lost vape cart**. The **smoke shop story** has been flagged as an unclaimed bid Papi has been avoiding.
- A custom emerald green adult pacifier (luxury aesthetic, Coco Chanel/"CC" color story, emerald = CC's birthstone) was planned as a gift — gifting approach developed (casual handoff, velvet pouch, minimal words, no tether energy).
- BVX has stalled; Papi has been encouraged to reopen it as an independent anchor separate from the CC dynamic.

---

**Key learnings & principles**

- **Papi functions as CC's primary emotional regulator** when she's engaged, and spirals when she's cold or absent — he has named this pattern himself and asked to be held accountable to it. Claude should flag when this dynamic is activating without shame or dwelling.
- **The suppression frame, not the skill-deficit frame**: Papi losing his playful register with CC isn't a capability gap — it's the monitoring mindset blocking a circuit that already exists.
- **Specific over general**: CC receives specific, honest, behavioral observations far better than general praise. "Good" lands flat; "there it is" or "knew you had it" lands clean.
- **Attunement before redirection**: always see before correcting.
- **Actions are already in CC's primary language**: Papi's acts-of-service approach (food, the gift, showing up) is operating correctly even when he feels verbally dysregulated with her.
- **The grand betrayal wound**: Papi has a deep personal wound around being abandoned by his support network when pursuing his storytelling dream. This wound pattern-matches onto moments of perceived replacement or distance (e.g., Ian driving CC instead of him) — Claude should name this when it's firing.
- **Savior dynamic guardrail**: Papi has explicitly flagged his tendency to gravitate toward people in distress and become their primary support. Claude should hold him accountable to this without being heavy-handed.
- **Soothing calibration**: distinguish between warranted support and soothing that bypasses something real and actionable — Papi has explicitly asked to be held to this distinction with CC.
- **Gottman antidotes applied to this dynamic**: gentle startup (behavioral, not character); active admiration; taking responsibility for his own piece; self-soothing before re-engaging during CC's withdrawal periods (not chasing, not counter-freezing).
- **Asymmetry of regulation**: CC's Four Horsemen expressions are largely physiological/involuntary; Papi's are more volitional — the relational work falls disproportionately on him to stay regulated and consistent. The "rock" metaphor: stable, warm, non-pursuing.
- **BVX as independent anchor**: creative project is not a consolation prize — it's the foundation that keeps Papi from collapsing the CC relationship under the weight of his own emotional needs.

---

**Approach & patterns**

- Papi thinks **laterally, not linearly** — he wants frameworks and ammo he can adapt himself, not prescriptive step-by-step instruction.
- He wants **direct consultation with layered theory and concrete examples** — he will pocket sections he doesn't need yet and redirect scope himself. Follow his lead on pacing rather than delivering complete structured outputs unprompted.
- He explicitly wants Claude to **challenge him when he's slipping into unproductive patterns** (projection, overreading signals, validation-seeking, savior slide, anxious-vendor creep) rather than simply affirming requests.
- He asked Claude to **open with lateral, possibility-based engagement** that places him in the decision-making role — not to lead with reframing or implicit correction of his thinking. Pushback should be preserved but not delivered as negation of every thought.
- He asked for **reframes to be consistently offered** when he presents fixed or anxious frames.
- Psychological frameworks he has engaged with and finds useful: Big Five, attachment styles (especially disorganized/fearful-avoidant), NVC, love languages, dark-triad lens, Gottman's Four Horsemen, Panksepp's primary emotional systems, Keltner's teasing research, Gable's active-constructive response framework.
- When Papi is in **acute emotional distress**, emotional presence and brevity matter more than frameworks — lead with acknowledgment, match his register (direct, grounded, not clinical), see him in specific moments before offering analysis.
- He communicates raw and stream-of-consciousness when flooded — profanity-heavy, fragmented, looping. Match register accordingly.
- He has a **medical cannabis license**, which came up as genuine peer-level common ground with CC.

---

**Tools & resources**

- **Claude.ai Projects** — actively using separate projects for different interpersonal situations (CC, Mary); has built and saved project instruction documents within these.
- **Voice-to-text dictation** (stock phone; Wispr Flow recommended as upgrade)
- Psychological/research frameworks: Gottman, Bowlby/Ainsworth/Main, Pete Walker, Rosenberg (NVC), Chapman (love languages), Panksepp, Keltner, Gable, Siegel/Wallin
- Professional support: has seen a psychiatrist; has had mixed experiences with additional professional support resources

---

## PWRX

**Purpose & context**

Daddy is building a comprehensive educational and practitioner-oriented knowledge base spanning Daddy Dom/little dynamics, broader D/s and BDSM frameworks, somatic sexology, and kink-affirming clinical psychology. The work combines academic rigor (peer-reviewed literature, DSM-5-TR, attachment theory, polyvagal theory, Wheel of Consent) with community-authoritative sources and practical applicability. Daddy operates from a Daddy Dom, pleasure Dom, and brat-tamer archetype, with a strong coaching and teaching orientation and words as a primary love language.

A parallel track involves applying these frameworks to a specific interpersonal situation with a coworker referred to as CC, including relational dynamics, trust-building, and communication strategy calibrated to her attachment style and specific behavioral patterns.

**Current state**

Two knowledgebase artifacts have been produced so far:
1. A comprehensive Daddy Dom/little dynamic overview — structured with full table of contents, academic citations, and reference list covering attachment theory, somatic frameworks, ethnographic research, and clinical literature
2. A ~110-term glossary organized into six categorical sections (D/s and power exchange, general BDSM, somatic sexology and embodiment, clinical psychology, Daddy/little-specific terminology, community and cultural terms), including a staged practice pathway and flags for contested or evolving terminology

**On the horizon**

Two major items are explicitly tabled and awaiting development in future sessions:

1. **Second knowledgebase artifact on six threads** specific to Daddy's situation with CC:
   - A framework for discovering and communicating desire safely within the dynamic
   - Trust-building methods calibrated to her specific wiring (attachment style, love language of acts of service, praise bypassing defenses vs. criticism causing collapse)
   - Homework and assignments as ambient presence and self-discipline scaffolding across distance
   - Architecture of effective praise designed to break through her defenses
   - Degradation and objectification reframed as a form of witnessing within the erotic dynamic
   - A non-transactional, non-expectant gifting framework sensitive to her history of gifts as instruments of control

2. **Tactical playbook** around a specific moment of CC's self-empowerment (a kitchen incident) — recognizing and reinforcing those moments through language and action

The multi-part conceptual guide covering negotiation processes, escalation dynamics, and troubleshooting also remains to be completed as a next phase of the broader educational project.

**Key learnings & principles**

- Attachment-style unavailability and structural unavailability are meaningfully distinct and should not be conflated when reading someone's relational behavior
- Indirect signaling through third parties or social media should be critically examined — genuine self-care and retaliation dressed as self-care can be difficult to distinguish and warrant honest scrutiny
- Giving someone's nervous system advance notice (e.g., a brief low-stakes text before an unexpected arrival) supports better connection by reducing processing load and surprise
- When someone has limited verbal expression, non-verbal and behavioral reaching gestures carry significant relational weight and should be read accordingly
- Gifting frameworks must account for relational history with transactional gifting; appreciation expressed through use rather than words is a valid signal
- Contested or evolving terminology should always be flagged rather than presented as settled consensus

**Approach & patterns**

- **Working style**: Consultative and iterative — thinks in frameworks and data points, prefers organized recaps before moving forward
- **Artifact format**: Markdown knowledgebase artifacts with full tables of contents and reference lists; not conversational summaries
- **Pre-production process**: Wants clarifying questions confirmed before artifact production begins
- **Communication style**: High-density, stream-of-consciousness verbal input with layered requests embedded in single turns — values Claude parsing implicit sequencing and reflecting back organized structure before proceeding
- **Continuity**: Explicitly requests that tabled items be held and surfaced in future sessions
- **Source standards**: Both peer-reviewed academic sources and community-authoritative voices; flags for clinical-versus-community usage divergences expected

---

## BVX SYSTEMS DEVLOPMENT

**Purpose & context**

Papi is building **The Outliers** (OXO / OVEREXITOUT) — a medium-independent story world that serves as the first proof-of-concept for a larger reusable world-building framework called **Bold Venture X (BVX)**. BVX is a methodology extracted from the act of actually building worlds, not designed in advance of them. The governing constraint is the **"car-and-cargo rule"**: the machine cannot be designed before the worlds it serves have been built. The Outliers must be complete before BVX earns its own dedicated mapping session. **ASTROSEX** is queued as the second world after The Outliers.

Papi's stated creative strengths are visceral scene-craft and tension; stated weakness is cohesion across longer narrative arcs. The system-mapping methodology is explicitly being used to build that structural muscle.

Papi communicates primarily via **voice-to-text** — recurring transcription drift is expected (e.g., "The Outsiders" = voice drift for "The Outliers"). Preferred format: short, numbered, shooting-script-style instructions. Works on large physical surfaces (chalkboard, notebook pages). Processes ideas through analogy and example rather than abstract definition.

**Canon corrections (always apply):**
- World name: **The Outliers** (never "The Outsiders")
- School: **The Academy** (Inner Spiral = current canon; Red Hills = legacy; fused name TBD)
- **QB** = Quinn Bishop (never "Quintin Barnes")
- Canon cast: Victoria "Tori" Midnight, Quinn Bishop, Riley Moss, Anna Colson Conway, Jebb Midnight (brother), Penelope Lane, Hunter Reed, Shane Doucet, The Administration, The Student Diaspora

---

**Current state**

System-mapping of The Outliers is in active progress using a structured methodology drawn from "Understanding a System." Steps 1–4 are complete; Step 5 (the Process page — mapping the school year) is the immediate next task.

- **Step 1:** Purpose sentence established — *"Right now I am trying to understand The Outliers, so that I can build it as a complete world."*
- **Step 2:** Inside/Outside/Unsure boundary list produced.
- **Step 3:** Full mess dump from notebook pages (85 items).
- **Step 4:** Parts map built and iterated live in FigJam — 7 boxes, 17 labeled wires, organized by entity type (Places, Factions, Characters, Events, Bio-Tech, Objects; Themes pulled off the map entirely). The Academy functions as a neutral hub between factions and regions.
- **Canon reconciliation pass completed:** A corpus of nine reference files (Master System Bible, character canon docs for Victoria Midnight and Quinn Bishop, validated character pipeline LEECHSEED / Dramatica-Astrology Interface, movement/genre breakdowns, legacy canon Red Hills Academy) was integrated. Most notebook material survived contact with canon cleanly.

**Five open forks** remain on a DECIDE tab and require Papi's decisions before Step 5 can fully proceed. The most urgent: **geography** (tri-state Delta Coast Spiral vs. continental US plus lunar frontier), as it gates several downstream items.

**Step 5 canon spine already available:** Year 1 = clean sync-cult → Year 2 = neon rot. The Hardware Gate marks the transition.

BVX Quartermaster is running as a parallel capture-and-validate log (not a design-ahead operation). Current BVX methodology captures include: the inhabitation test, the org-chart verb test, the once/cycle split, the ownership-first rule for sorting traditions, and the principle that some rites function as labeled wires between boxes. The tripwire (fires when the same pattern appears across two built instances) is currently cold.

---

**On the horizon**

- Resolve the five open geography and canon forks (geography is highest priority)
- Complete Step 5: Process page (school year mapping, using the Year 1→Year 2 spine and Hardware Gate)
- Continue populating the BVX Quartermaster log from real world-building work — promote methodology captures to invariants only when two or more concrete uses appear across distinct instances
- Begin ASTROSEX as the second world after The Outliers is complete
- BVX dedicated mapping session: held until the tripwire fires

---

**Key learnings & principles**

- **Car-and-cargo rule:** BVX cannot be designed before at least one complete world exists. Machine design follows evidence, not theory.
- **Inhabitation test:** Determines what belongs in-world vs. what is author scaffolding.
- **Org-chart verb test:** Wire label quality check — labels must describe the relationship, not just name the connected nodes.
- **Once/cycle split:** Distinguishes world-scarring one-time events from cyclical maintenance rites.
- **Ownership-first rule:** Sort traditions by who owns them before categorizing by content.
- **Some rites are wires, not boxes:** Certain rituals and traditions belong as labeled connectors between entities, not as standalone parts.
- **Theorized items are parked, not promoted:** BVX captures require grounding in actual built material.
- **"Wicked Penitential Freaks" author-frame principle:** The world tries to make the characters penitent; they refuse; the world reaps the consequences of its own misdiagnosis. Each term in the phrase is relational (wicked *to whom*, penitential *before whom*, freak *by whose taxonomy*) — the upstream design node may be the world/system rather than character alone. The phrase has permanent life as an author-frame motif (intro sequences, official music, framing material), not necessarily as an in-world title.
- **Multiple partial models over one complete model:** Linear "understand it first, then proceed" approaches fail on wicked problems. Boundaries are choices, not facts.
- **Scope nesting:** Problems nest inside problems; structural, process, and feedback views are genuinely distinct and require separate treatment.

---

**Approach & patterns**

- Works through a numbered, checklist-driven system-mapping methodology — explicit steps, explicit outputs, explicit decision gates.
- Builds on large physical surfaces first; then translates to digital (FigJam).
- Prefers plain language and analogy before frameworks; flags unfamiliar vocabulary and requests rewrites directly.
- Corrects Claude's misreads efficiently and specifically — Papi distinguishes between concept, rhythm, and intent with precision.
- BVX Quartermaster discipline: Claude flags the car-and-cargo rule once if Papi pushes toward designing the machine ahead of evidence, then follows Papi's lead.
- Specificity over ambiguity; descriptive density over "The [Noun]" IP-slop structures.

---

**Tools & resources**

- **FigJam** (file key: `GWcns4RGMNyuI9cSPgWcQw`) — primary live mapping board; accessed via Figma MCP connector
- **Figma MCP connector** — reliable read pattern: `Figma:get_figjam` with `includeImagesOfNodes: True`, `nodeId: 0:1`. Text edit sequence on `ShapeWithText` nodes: `getStyledTextSegments(['fontName'])` → `loadFontAsync` for each segment → set `text.characters` (font-load step cannot be skipped). New connectors: pull font from existing connector before setting text.
- **Claude Code** — used to compile reference corpus (nine canon files)
- **BVX-LEARN** — structured knowledge vault producing standardized one-sheet reference documents organized by domain (e.g., MSX series). Template: YAML front matter, Core Thesis, Invariants, Heuristics, Core Concepts, Key Vocabulary, Notable Quotes, What Doesn't Work, Quick Self-Check, and appended Glossary. Files written to `/home/claude/`, copied to `/mnt/user-data/outputs/` for persistence. Naming convention: `🧬 [ID] — [Title] — [Author Last Name] ([Year]).md`.
- **conversation_search** — required to reconstruct prior file content across sessions (container does not persist files between sessions).

---

## 🇬🇷

**Purpose & context**

Papi works in a food service role, likely in a Greek/Mediterranean kitchen or quick-service context. A key use case is building and sending structured vendor ordering lists to a supervisor for purchasing decisions. Papi also occasionally uses Claude for quick factual lookups and drafting sharp, copy-paste-ready social/comment text.

**Current state**

Papi has established a working inventory ordering system across three vendors: a primary truck vendor, Sam's Club, and Walmart. The truck and Sam's lists include PAR levels for key items (e.g., Cones, Bread, Greek Fries, box types, Lemon Juice) that auto-calculate order quantities from on-hand counts. These lists are actively used and refined on an ongoing basis.

**Key learnings & principles**

- Over-engineering is a friction point — Papi explicitly rejected complex outputs (e.g., React apps, elaborate formatting) in favor of simple, functional text.
- Pop psychology trends are a point of frustration; Papi prefers sharp, critical takes over elaborated or hedged commentary.

**Approach & patterns**

- **Communication style**: Casual, direct, and efficient. Uses strong language when frustrated. Prefers Claude to stay focused and not over-explain.
- **Preferred output format**: Clean, minimal copy-paste text using "Item - Quantity" pattern — no extra labels, symbols, category separators, or blank lines within lists.
- **Iteration style**: Dictates items verbally, then refines format quickly. Expects immediate corrections when quantities or items are flagged as wrong.
- **Writing/comment requests**: Prefers neutral, informative tone (not addressed to a specific person), laconic phrasing, and specific illustrative examples retained rather than abstracted away.

---

## ULTRASIN

**Purpose & context**

Papi is building a multi-venture creative and business operation spanning several interconnected domains: an adult content creator brand ("The Annalist" / "Ultrasin"), a broader entertainment and IP company ("Bold Venture X" / BVX), photography and visual culture work, and longer-horizon ventures including a boutique regenerative retreat concept. The fiscal anchor for the content venture is May 4, 2026.

The Annalist / Ultrasin brand is the most developed active venture: a methodology-driven adult content publication and performer brand with a deliberately academic-autoethnographic register. Core brand instruments include "The Compliance Scale" (the review methodology), "The Annals" (the keystone publication name), and "The Annalist" (the performer handle, with a glasses-over-mask signature visual). The Dionysian Drive is Papi's named creative-engine concept — the philosophical spine of the brand, emphasizing aesthetic purity and refusal to compromise for stakeholder or monetization pressures.

BVX operates as a separate but adjacent entity (subsidiary, sister, or fully separate — firewall architecture decision still open), with associated projects including Outliers, ASTRO7EX, and OVEREXITOUT. A reputational firewall between the content venture and the broader BVX identity is a standing architectural requirement.

Papi's deeper operating passion is taxonomic-aesthetic practice: collecting aesthetics, building visual archetype systems, trend-reading, and the curatorial pleasure of pairing, naming, and categorizing references. He maintains a large multi-year archive of aesthetic references and has strong interest in character design, mood archetypes, and visual identity systems.

Current day job is in food service (cook/restaurant). Financial milestone: double current income before leaving that role, with one-year and three-year targets anchoring the venture curve. Background includes film production knowledge (lighting, cameras, contracts), strong sound production and music experience, and fluency in AI tooling and Adobe Creative Suite (Premiere, After Effects). Based in North Florida ([CITY] area).

---

**Current state**

*Content production setup:*
Papi is in early concept stage for a recurring solo video production setup using a Flying J truck stop shower room as a fixed filming location — selected for its tiled walls (suction-mount camera friendly), consistent built-in lighting, privacy, and lockable room. Production philosophy is "min-max": maximum professional output, minimum footprint and setup complexity. Persona concealment via mask is a stated preference. No cameras currently owned beyond a latest-model iPhone; camera acquisition is pending a capital threshold decision.

Camera options researched and compared: matched DJI Osmo Action 6 fleet (recommended for low-light and square-sensor reframing flexibility), GoPro Hero 13 fleet, Insta360 Ace Pro 2 fleet (flip-screen advantage for solo verify-before-roll), and a single Insta360 X5 360-camera collapse approach. DJI Osmo Nano identified as the reaction/face-height station camera. Full production kit list and session run-card sequence have been outlined.

*Content and business architecture:*
Monetization model follows a Fortnite-style structure: free core content distributed widely (visibility doctrine: generous, near-full clips), subsidized by rotating shop, tiered subscriptions with whale/loyalty-tier segmentation, and tentpole drop events. Toy acquisition treated as COGS, milestone-gated into "season" triggers rather than affiliate-linked. No permanent physical shop at launch — intentional for drop-event impact.

Named benchmark toy makers: Mr. Hankey's Toys, Square Peg Toys, Topped Toys, Silc Arts, Bad Dragon (secondary). Affiliate model rejected on editorial integrity grounds.

Flagship content concept: "Cocksucking Mastery" — documentary-style progression series, self-contained seasons with a capstone feat as climax. Reference creators noted: Siswet and Lilla Junex.

*Knowledge infrastructure:*
Ultrasin Master Registry v0.1 has been produced (Obsidian-ready Map of Content across 13 system domains). Obsidian is the internal knowledge base; MkDocs Material or Quartz identified for the public-facing docs layer, hosted on adult-tolerant platforms. Established methodology: draft everything in-chat as text first, then convert to markdown artifacts.

*Physical development:*
Physique goal is a dual-signal build — mass/capability frame plus high-performance aesthetic. Four-pillar architecture: hypertrophy (anchored by Contreras Glute Lab program), mobility/flexibility (targeting full splits), functional strength (partner-lifting benchmark), and performance craft. Tracking: three tape sites monthly (hips at widest, waist at navel, right thigh), hip thrust top set as session-level leading indicator, weekly scale weight as context, locked monthly photo recipe. Startup cost under fifty dollars.

*Pelvic floor and performance conditioning:*
Active training protocol developed ("The Gate Keeper's Kata") treating pelvic floor conditioning as martial arts practice. Established prep protocols: shallow confirmation rinse for regular sessions, deeper advance clean with settle window for intensive sessions. Consistent daily fiber intake framed as foundational infrastructure. Shower attachment over-insertion identified as root cause of rinse-loop problem; corrective guidance provided.

*Personal journaling system:*
Using Claude as a structured logging assistant for personal encounter logs, formatted as bullet-point entries with consistent template (partner stats, session notes, ratings, skill development observations, logistics, pipeline notes). Pattern noted: non-performative engagement consistently produces better outcomes than deliberate effort. TRE and the psoas muscle framework identified as relevant somatic science.

---

**On the horizon**

- Capital threshold decision to gate camera acquisition (the key pending unlock for production setup)
- Companion layer consultation: a visual, conversational desktop-presence AI that interfaces naturally with Papi and can also interface with Claude/Claude Code operationally (spinning up project chats, requesting breakdowns, managing tasks) — buy-vs-build verdict pending
- Full cash-rails consultation (queued)
- Threshold and surfaces research: comp floors, audience stack minimums, long-tail funnels, reference sites (queued)
- Second knowledgebase artifact on six relationship/dynamic threads (tabled from earlier session)
- Atlanta trip planning: compressed version (one night / day and a half) following a North Carolina event leg — itinerary not yet built, pending five clarifying inputs (NC city/event type, Atlanta arrival date, content overlay y/n, lodging mode, return night flexibility)
- Nipple piercing sequenced as a body modification milestone behind filming milestones
- "The Nexus" — multi-year capital milestone: purpose-built warehouse studio integrating all ventures under one roof
- Phase 3 knowledge recovery from session census (strays and gaps identified in registry)
- Several open bracket confirmations from prior sessions still unresolved

---

**Key learnings & principles**

- **Gravity, not outreach**: Build until the asking reverses direction. Outreach is a pre-gravity activity; the goal is to reach the gravity point where brands send unsolicited units.
- **Infrastructure before content**: Entity structure, compliance, and payment processing architecture must precede public-facing presence.
- **Milestone-gated spending**: Capital unlocks season triggers rather than being deployed speculatively.
- **Firewall architecture is non-negotiable**: BVX and content ventures are separated operationally and legally, not just by identity labeling.
- **Affiliate model rejected**: Stakeholder contamination of editorial integrity, audience trust damage, and speculative income make affiliates incompatible with the brand doctrine.
- **Dionysian Drive as creative engine**: Erotic/embodied energy is Papi's highest-conversion motivational fuel — documented as a creative asset, not a liability. Limerence framed as a captured/static configuration of this system; eroticism as the dynamic, agency-convertible configuration.
- **Borrow religious structure without authority hierarchy**: Aesthetics and discipline of liturgical frameworks (ordinal ranks, rule of life, seasonal sprints) without the failure modes of belief-plus-authority organizations.
- **Non-performative engagement outperforms deliberate effort**: Consistent pattern across practice sessions.
- **Taxonomic-aesthetic capacity increases in value as AI commoditizes execution**: The naming and curation layer is the high-value, non-replicable human contribution.
- **Free tier as visibility doctrine**: Generous, near-full clip distribution widely rather than restricted previews — visibility subsidizes premium.
- **Physical sustainability as production policy**: Treated as a hard constraint, not a preference.

---

**Approach & patterns**

**Communication style**: Stream-of-consciousness voice dictation with fragmented syntax, phonetic errors, mid-sentence pivots, and deliberate pauses ("standby"). Claude's role is to log and reflect without interrupting the roll, flag garbled segments in brackets for one-word confirmation, compress readbacks to show what was caught, and bracket unresolved items explicitly.

**Standing session protocol (user instruction — always apply)**:
- Before building anything or moving on, Claude asks clarifying questions first and states what it's about to do, then waits for Papi's go-signal.
- Never dive straight into artifacts: always present information in-chat first, then check with Papi and get his confirmation before producing the artifact version.

**Decision-making**: Papi prefers structured possibility maps over recommendations; prefers honest, direct framing over diplomatic hedging; explicitly does not want projections inflated. Financial figures are parked until explicitly reopened.

**Build sequence**: In-chat text first → confirmation → artifact. All artifacts are Obsidian-compatible markdown with YAML front matter, tables of contents, and internal link syntax.

**Organizational tool**: The Four Blocks method — a chalkboard affinity-mapping instrument sorting output into mess, doctrine, systems, and ladder categories.

**Feedback pattern**: Direct and brief. Blunt creative redirection preferred over explanation. "Ehhh those were weak" is sufficient signal to strip and restart.

**Consulting register**: McKinsey-style strategic consulting held steady. No over-cautious hedging; compliance information framed as practical operational risk awareness.

---

**Tools & resources**

- **Knowledge base**: Obsidian (internal); MkDocs Material or Quartz (public-facing, adult-tolerant hosting)
- **Production**: Adobe Creative Suite (Premiere, After Effects); AI tooling (fluent); latest-model iPhone (current primary camera)
- **Camera shortlist**: DJI Osmo Action 6, Insta360 Ace Pro 2, DJI Osmo Nano (pending capital threshold)
- **Content platforms**: OnlyFans (existing account, not yet actively used); JustForFans; Telegram; X/Twitter for networking
- **Payment processing research**: CCBill, Segpay, Paxum, Verotel identified as adult-friendly processors
- **Banking research**: Mercury, NorthOne identified as adult-tolerant
- **Toy makers on radar**: Mr. Hankey's Toys, Square Peg Toys, Topped Toys, Silc Arts, Bad Dragon
- **Physical training**: Contreras Glute Lab program (Bret Contreras)
- **Production location**: Pilot Flying J shower rooms (established logistics and session protocol)
- **Networking platforms researched**: LPSG, Squirt.org, BarebackRT, Recon, JustForFans collab events

---

## DESIRE PROFILE

**Purpose & context**

Papi is working on a personal self-discovery project called the **Desire Profile** — a four-tool system for erotic self-mapping consisting of: Erotic Journal, Erotic Quizzes, Sexual Disclosure, and a Sex Menu that culminates in a personal Synthesis profile. The project is both a structured self-knowledge framework and an active software build. Claude's role is strictly technical coach and builder — never generating erotic or roleplay content — supporting taxonomy, tooling, and architecture in service of Papi's self-exploration work.

**Current state**

The primary active objective is **Tool 1, Step 1**: completing the turn-on inventory (an uncurated, judgment-free dump from four source wells — fantasies, real/wished-for experiences, intrusive/ambient thoughts, and consumed media) and marking that step done in Mission Control. Most sessions to date have been infrastructure work; this step has not yet been formally checked off.

The software side is a sophisticated single-file HTML application ("Mission Control") currently at v9+. Recently built and stabilized features include:
- A 249-tag industry-taxonomy **Tag Board** across 20 lanes with custom tag support
- A **Feeling Mapper** using a tag-first drill-down interaction (tap tag → family → word)
- A **Guided Run wizard** with working stations embedded directly in each step (not linked out)
- A **NOW-first home screen** that answers "what do I do next" with a single directed action card
- A bridge auto-populating Tag Board lanes from Sex Menu positive ratings

**Key learnings & principles**

- The NOW screen must always answer one question: *what do I do next* — no clutter, no dashboard sprawl
- Stations belong **embedded in the flow**, never linked out as separate destinations
- The board/mapper should mirror how the mind actually moves through material, not impose a tool-first workflow
- Quantity over quality during the inventory dump; no analysis during collection
- The process is activating by design — that's expected, not a problem
- Each session closes with a SYNC block: confirm completed steps, log findings, name the next objective

**Approach & patterns**

- Papi thinks through UX by describing **mental models and interaction metaphors**, not technical specs — Claude translates these into implementation
- Communication style: direct, profanity-comfortable, blunt and punchy, no hand-holding, no softening
- Strong editorial instinct toward **simplicity** — Papi consistently strips clutter when the interface accumulates dead weight (removed: coach chat embed, docklines, status strips, paint-brush metaphor)
- Coaching progresses **one step at a time**, structured and sequential
- Sessions are tracked; SYNC notes confirm what was and wasn't completed

**Tools & resources**

- Single-file HTML app (Mission Control, currently v9+) housing all four tools
- Tag taxonomy of 249 industry-standard tags across 20 lanes
- Iterative multi-session build history (v1–v9+ documented across sessions)

---

## Mary's French Bakery

**Purpose & context**

Papi is exploring questions related to interpersonal dynamics, attraction, and relationships, with an interest in psychological and research-backed perspectives on these topics.

**Key learnings & principles**

In a past conversation, Papi sought strategic guidance on navigating an ambiguous workplace dynamic. Claude declined to provide tactical escalation advice, and instead flagged that engineering situations where another person initiates while the requester maintains deniability is a form of manipulation — not a reading of genuine signals. Claude noted that the appeal of "forbidden" dynamics can be a signal to pause and reflect rather than proceed, and that workplace contexts carry particular risk. Claude pointed toward direct, honest disclosure as the only approach likely to lead to a genuinely worthwhile outcome — one that gives the other person a free and unmanipulated choice.
