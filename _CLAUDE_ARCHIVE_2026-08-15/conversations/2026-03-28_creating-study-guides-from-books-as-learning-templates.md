---
title: "Creating study guides from books as learning templates"
uuid: ee1b0947-cd54-4def-b342-cce308d20bc0
created: 2026-03-28
updated: 2026-03-28
trunk: BLACK
messages: 18
chars: 27762
artifacts: 0
generated_files: 10
tools: [ask_user_input_v0, bash_tool, create_file, present_files, str_replace, web_fetch, web_search]
source: claude.ai-export-2026-08-15
---

# Creating study guides from books as learning templates

> **Conversation Overview**

The person is building a personal knowledge management system centered on rapid book extraction and is working across Claude and Obsidian. They use voice input as their primary interface (speaking into a microphone rather than typing), which became an important design constraint late in the conversation. Their goal was to create a reusable system for turning books and PDFs into concise, actionable one-sheet reference cards they can consult quickly — emphasizing fast learning, strategic distillation, and long-term queryability.

The conversation iterated through several rounds of refinement. Claude initially produced an overly long, multi-section study guide for the book "Strategic Learning: A Holistic Approach to Studying" by Robert K. Kamei, which the person rejected as too bloated. They clarified they wanted a tight one-sheet format focused on invariants (unchanging principles), heuristics (decision rules), and core concepts — not summaries. Through a structured Q&A process, the person made several key design decisions: the system would live in an Obsidian vault with YAML front matter and wikilinks, entries would be generated inside a Claude Project (one conversation per book), the naming convention would use a Zettelkasten-inspired hybrid ID system (domain code + serial number, e.g., `LRN.01`), the series brand emoji would be 🧬, and each entry would include key vocabulary and notable quotes sections in addition to the core sections. A table of contents was identified as a critical missing element and added in a later revision.

The final deliverables produced across the conversation were: the BVX-LEARN Project Instructions (a Claude Project custom instructions prompt acting as the agent), a specimen one-sheet for Strategic Learning (`🧬 LRN.01`), a setup guide for configuring the Claude Project, and a template document. The person's stated correction pattern was consistent: they pushed back on verbosity and complexity, always requesting tighter, more scannable output. The final voice trigger update replaced the awkward spoken command "BVX-LEARN" with natural spoken aliases like "Learn this," "Learn [title] by [author]," "Go deeper on [topic]," and "Upgrade this," with the project instructions updated to recognize fuzzy intent rather than exact phrasing. The person confirmed that title and author alone (no PDF) is sufficient to generate a draft entry, with PDFs used to upgrade drafts to complete status.

**Files produced**

- [strategic_learning_study_guide.md](../files/2026-03-28_strategic-learning-study-guidemd.md)
- [BVX_LEARN_TEMPLATE_v1.md](../files/2026-03-28_bvx-learn-template-v1md.md)
- [strategic_learning_onesheet.md](../files/2026-03-28_strategic-learning-onesheetmd.md)
- [BVX_LEARN_TEMPLATE_v2.md](../files/2026-03-28_bvx-learn-template-v2md.md)
- [BVX_LEARN_PROJECT_INSTRUCTIONS.md](../files/2026-03-28_bvx-learn-project-instructionsmd.md)
- [🧬 LRN.01 — Strategic Learning — Kamei (2021).md](../files/2026-03-28_lrn01-strategic-learning-kamei-2021md.md)
- [BVX_LEARN_PROJECT_INSTRUCTIONS.md](../files/2026-03-28_bvx-learn-project-instructionsmd-2.md)
- [BVX_LEARN_PROJECT_INSTRUCTIONS.md](../files/2026-03-28_bvx-learn-project-instructionsmd-3.md)
- [🧬 LRN.01 — Strategic Learning — Kamei (2021).md](../files/2026-03-28_lrn01-strategic-learning-kamei-2021md-2.md)
- [BVX_LEARN_SETUP_GUIDE.md](../files/2026-03-28_bvx-learn-setup-guidemd.md)

---
## 🧑 Papi  <sub>2026-03-28 09:34:23</sub>

Okay. Can you take the following book I'm about to post and create a study guide for it? Or just actually explain it to me. And I wanna use it as a template to take other PDFs or other books for you to then identify it and just create these fast learning, strategic learning guide pamphlets, or knowledge book entries. Based on what I'm about to give you. Strategic Learning: A Holistic Approach to Studying 9811226652

---

## 🤖 Claude  <sub>2026-03-28 09:37:27</sub>

The user wants me to:
1. Find/get the book "Strategic Learning: A Holistic Approach to Studying" (ISBN: 9811226652)
2. Create a study guide / explanation of it
3. Use it as a template for future books/PDFs they upload

Let me search for this book to understand what it covers, then create a comprehensive study guide and a reusable template.Let me find out what this book covers so I can build you something solid.
```
This block is not supported on your current device yet.
```

Let me search for more specific content about the book's chapters and structure.
```
This block is not supported on your current device yet.
```

Let me try to find the actual table of contents or chapter structure from the World Scientific page.
```
This block is not supported on your current device yet.
```

Let me try another search to find the table of contents.
```
This block is not supported on your current device yet.
```

Let me search for a review or summary that has the actual chapter structure.
```
This block is not supported on your current device yet.
```

Now I have a good understanding of the book. Let me create the study guide as a markdown file AND a reusable template. The book's framework covers:

1. Debunking learning myths (each chapter opens with a myth)
2. Foundational pillars: health/wellness (sleep), motivation, self-discipline
3. Metacognitive cycle and self-regulatory processes
4. Evidence-based study techniques: spaced repetition, retrieval practice, interleaving
5. Holistic Learning Framework

Let me create both the study guide and the template.Good stuff — that review from Digital Senior was especially useful for understanding the internal structure. Now I have a strong picture of Kamei's framework. Let me build out both the study guide AND the reusable template for future books.
```
This block is not supported on your current device yet.
```

Now let me create the reusable template.Now let me build the reusable template you can use on any future book or PDF.
```
This block is not supported on your current device yet.
```

Now let me copy both to outputs and present them.
```
This block is not supported on your current device yet.
```

Done.
```
This block is not supported on your current device yet.
```

Done, both files delivered.Two files for you:

**File 1 — Strategic Learning Study Guide:** The full knowledge entry for Kamei's book. The book's arc moves from debunking popular myths about learning, through building metacognitive and self-regulatory understanding, to practical implementation advice. I structured it around the five-layer holistic framework — myth destruction at the base, health foundations, motivation/self-regulation, the metacognitive cycle, and then evidence-based techniques at the top. Each chapter in the original book opens with a learning myth to set up what that chapter will cover, with summaries at the end of each chapter. The guide includes a 10-point self-assessment checklist and a cross-reference table to related books.

**File 2 — BVX-LEARN Template v1.0:** Your reusable template. Next time you drop a PDF or give me a book title, just say "BVX-LEARN this" and I'll generate the same structured output. The template includes adaptation rules for different book types (technical, narrative, research papers, self-help, reference manuals) so it flexes based on what you feed it.

---

## 🧑 Papi  <sub>2026-03-28 09:40:08</sub>

Hey, dude. This doesn't really work that well, actually. I just I wanna be able to basically create a one sheet, cheat sheet, study guide for all the books that I'll post to you. One of the most important things is the idea of invariance or, heuristics. And exactly what exactly he core components or the core theories, solutions, and concepts that the book is teaching. Can you leverage that on other types of that are sort of meant to sort of meant to help people quickly learn fast and such, consult, and assess

---

## 🤖 Claude  <sub>2026-03-28 09:41:30</sub>

The user wants me to simplify and redesign the template. They want:

1. A one-sheet/cheat sheet format - concise, not a massive multi-section document
2. Focus on invariants and heuristics - the core unchanging principles/rules of thumb
3. Core theories, solutions, and concepts - the essential "what does this book actually teach"
4. Something that helps people quickly learn, consult, and assess

Let me redesign both the Strategic Learning entry AND the template to be much tighter. Think of it like a reference card, not a textbook summary.

Let me rebuild this as something much more compact and useful.Got it — the first version was bloated. You want something tight: the invariants, the heuristics, the core mechanics. A reference card you can glance at and immediately use, not a second book about the book. Let me redo both.
```
This block is not supported on your current device yet.
```

Now let me rebuild the template to match this tighter format.
```
This block is not supported on your current device yet.
```

Let me copy to outputs and present.
```
This block is not supported on your current device yet.
```

Good, now present.
```
This block is not supported on your current device yet.
```

Done. Let me give a concise summary.Completely rebuilt. The structure now is just six sections: thesis (one sentence), invariants (the physics of the domain — what's always true), heuristics (if-then decision table for real situations), core concepts (the actual mechanisms, 4 sentences max each), a kill list, and a yes/no self-check ordered by priority.

The template v2 also includes extraction rules so when you drop a book or PDF and say "BVX-LEARN this," I know exactly what to hunt for — invariants vs. heuristics vs. core concepts, and how to tell them apart.

---

## 🧑 Papi  <sub>2026-03-28 09:45:08</sub>

Okay. Using that template, can you create a prompt for your that I can use with an AEI agent or that I can I don't know, just have that agent be responsible for creating a learning template, One Sheets? I would also like the title for each book or something to be sort of organized and a sort of state of governance. So it's all organized in a certain way. Also, a unique emoji identifier that will be used in each title. It's the same for one sheet. For across all of them, but it needs to be unique to the One Sheets consult and ask me questions that will help you create a more detailed and on the nail on the head, giving me what I need.

---

## 🤖 Claude  <sub>2026-03-28 09:45:33</sub>

The user wants me to:

1. Create a prompt they can use with an AI agent to generate BVX-LEARN one-sheets
2. Include a governance/organizational system for naming and filing
3. Include a unique emoji identifier for the one-sheet series
4. Ask clarifying questions to nail down the details

Let me ask the right questions to get this dialed in.Before I build this out, let me ask some things that'll make or break whether this actually works for you:

**On the organizational system / governance:**
When you say "state of governance" for how they're organized — are you thinking something like a tagging taxonomy? Like each one-sheet gets categorized by domain (e.g., `LEARNING`, `BUSINESS`, `PSYCHOLOGY`, `FITNESS`, `SYSTEMS`) and then filed under that? Or more like a sequential numbering system (BVX-LEARN-001, 002, etc.)? Or both — a domain tag plus a serial number?

**On where these live:**
Are these going into your Obsidian vault? That changes how I structure the naming, YAML front matter, and linking. If it's Obsidian, I can bake in wikilinks, tags, and SSOT-compatible metadata right into the template.

**On the emoji identifier:**
Just to confirm — you want ONE specific emoji that marks every one-sheet (like a series brand icon, the way a publisher has a logo), not a different emoji per book. So every one-sheet title would look something like `⚡ STRATEGIC LEARNING — Kamei (2021)` where ⚡ is always the same across the series. Want me to propose a few options, or do you already have one in mind?

**On the agent prompt:**
When you say "AI agent" — are you planning to use this as a system prompt in the Anthropic API, paste it into Claude.ai conversations, use it in Claude Code, or feed it into something like a custom GPT / assistant? The format changes slightly depending on where it's going.

**On scope of what gets extracted:**
Right now the template pulls invariants, heuristics, and core concepts. Are there any other categories you consistently want? For example: key vocabulary/jargon definitions, notable quotes, "who is this for / not for," or anything specific to how you personally process books?
```
This block is not supported on your current device yet.
```

Waiting for the user's responses to these questions.Hit me with those answers and any other details on the emoji / extra extraction categories, and I'll build the whole thing out tight.

---

## 🧑 Papi  <sub>2026-03-28 09:47:06</sub>

Q: Where will these one-sheets live?
A: Obsidian vault (with YAML/wikilinks)

Q: What's the agent target?
A: Claude Project with custom instructions

Q: Naming format preference?
A: give me examples of each dont start yet. also help me set up a project in which all of these....actually would it be better to just have it al in one conversation or like one for each book in a project folder?

---

## 🤖 Claude  <sub>2026-03-28 09:47:30</sub>

The user wants to see examples of each naming format before choosing, and they're also asking about project organization strategy — one conversation vs. multiple conversations within a Claude Project.Good call pausing here. Let me lay out the naming examples first, then the project architecture question.

---

**Naming format examples** (using Strategic Learning as the specimen):

**Domain tag + serial number:**
`📐 LEARN-001 — Strategic Learning — Kamei (2021)`
`📐 PSYCH-003 — Mindset — Dweck (2006)`
`📐 SYS-007 — Thinking in Systems — Meadows (2008)`

Pros: sortable, scannable, you can see at a glance how many entries you have per domain. Cons: you have to maintain a registry of serial numbers.

**Domain tag + title only:**
`📐 [LEARNING] Strategic Learning — Kamei (2021)`
`📐 [PSYCHOLOGY] Mindset — Dweck (2006)`
`📐 [SYSTEMS] Thinking in Systems — Meadows (2008)`

Pros: no serial number to track, domain is right there. Cons: no ordering within a domain, could get cluttered with many entries.

**Serial number + title only:**
`📐 BVX-001 — Strategic Learning — Kamei (2021)`
`📐 BVX-002 — Mindset — Dweck (2006)`
`📐 BVX-003 — Thinking in Systems — Meadows (2008)`

Pros: clean, simple, universal numbering. Cons: you can't tell the domain from the title alone without opening it.

**Just title with emoji branding:**
`📐 Strategic Learning — Kamei (2021)`
`📐 Mindset — Dweck (2006)`
`📐 Thinking in Systems — Meadows (2008)`

Pros: cleanest, most minimal. Cons: no categorization or ordering at file-name level — you'd rely on Obsidian tags/folders instead.

---

**Now the architecture question — this one matters a lot:**

**Option A: One conversation per book inside a Claude Project**

Each book gets its own conversation thread. The Project's custom instructions contain the BVX-LEARN prompt + template. You drop a PDF or book title into a new conversation, say "BVX-LEARN this," and it generates the one-sheet. Each conversation is a self-contained record of the extraction.

Why this is better: you can go back to a specific book's conversation and ask follow-up questions ("expand the heuristics," "how does this connect to the last book I did"), the conversation history stays focused, and Claude's context isn't polluted with 15 books worth of prior output.

**Option B: One long conversation for all books**

You keep feeding books into the same thread. Everything lives in one running conversation.

Why this is worse: context window fills up fast, Claude starts losing earlier entries, you can't easily find or revisit a specific book's extraction, and if the conversation breaks or gets too long you lose your working thread.

**My recommendation: Option A — one conversation per book, inside a single Claude Project.** The Project's custom instructions hold the agent prompt, the template, your formatting preferences, and the naming convention. Every new book is a new conversation. You export each one-sheet to your Obsidian vault as a standalone `.md` file.

The Project becomes your "one-sheet factory" and your Obsidian vault becomes the library.
```
This block is not supported on your current device yet.
```

Waiting for user response.Also — for the emoji, `📐` was just a placeholder. Want me to propose a few options that feel right for "one-sheet knowledge extraction," or do you have something in mind?

---

## 🧑 Papi  <sub>2026-03-28 09:51:21</sub>

Q: Which naming format do you want?
A: ok can we kind of hacknye a on the fly agile form of zettlekasten in this phase? perhpase include it in the YAML, title, some sort of system that will be easily read from the title UX wise as well as sort of systemaltically later in terms of querying and RAG type shit does that make sense

Q: Project architecture?
A: Option A — one conversation per book in a Project

---

## 🤖 Claude  <sub>2026-03-28 09:52:05</sub>

The user wants a Zettelkasten-inspired naming/ID system that:
1. Is readable at a glance (UX)
2. Is machine-queryable (RAG/search)
3. Lives in both the filename AND YAML front matter
4. Is agile/lightweight - not a full academic Zettelkasten but borrows the good parts

Let me think about what makes Zettelkasten work for this use case:
- Unique atomic IDs
- Category/domain encoding
- Linkability
- Timestamping for sequence

A good hybrid would be something like:
- A short domain code (2-4 chars)


- A timestamp-based ID (Zettelkasten traditionally uses timestamps)
- Human-readable title

For RAG/querying, the YAML front matter is where the structured metadata lives. The filename needs to be scannable by a human. I'm proposing a system like `📐 LRN.2603 — Strategic Learning — Kamei.md` where the emoji stays consistent across all one-sheets, the three-letter domain code identifies the category, and the four-digit timestamp captures when the entry was created.

But I'm running into the issue of multiple entries in the same month—I need some way to differentiate them. A traditional Zettelkasten uses full timestamps like `202603281430`, but that's unwieldy. I could try `LRN.26A` where the letter sequences within a year, or `LRN.2603a` for monthly sequences, or just go with simple sequential IDs like `LRN.01`, `LRN.02`. The real tension is that Zettelkasten IDs are supposed to encode relationships and branching structure—like `1a`, `1a1`, `1b`—but for this use case, I'm wondering if that complexity is necessary or if a simpler sequential approach would work better.

I think the branching structure could still work here: main entries like `LRN.01`, sub-entries or deep dives as `LRN.01a`, and related concept spin-offs as `LRN.01b`. That feels clean and extensible. For the YAML metadata, I'd want to capture the ID, title, author, year, domain, tags for Obsidian integration, related entries as wikilinks, creation date, source type, and possibly a status field. Let me put together a proposal for him with this structure and see if he has feedback on the emoji usage or other details.That makes total sense — you want the ID system doing double duty: human-scannable in the sidebar AND machine-parseable for when you eventually point a RAG pipeline or Dataview queries at your vault. Here's what I'm thinking:

---

**The ID System — Agile Zettelkasten Hybrid**

Filename pattern:
```
📐 LRN.01 — Strategic Learning — Kamei (2021)
📐 LRN.02 — Make It Stick — Brown (2014)
📐 PSY.01 — Mindset — Dweck (2006)
📐 SYS.01 — Thinking in Systems — Meadows (2008)
📐 BIZ.01 — Zero to One — Thiel (2014)
📐 FIT.01 — Glute Lab — Contreras (2019)
```

The anatomy:
- `📐` — series brand emoji, constant across all one-sheets (we'll pick this together)
- `LRN.01` — 3-letter domain code + sequential number within that domain
- Title, author, year — human-readable at a glance

**Branching (the Zettelkasten part):** If you ever do a deep-dive spin-off or a follow-up entry on a sub-topic from a book, it branches:
- `LRN.01` = main entry (Strategic Learning)
- `LRN.01a` = deep dive on spaced repetition specifically
- `LRN.01b` = deep dive on metacognitive cycle
- `LRN.01-vs-02` = comparison entry between two books

This keeps the tree structure without needing a database.

**YAML front matter** (this is what makes it RAG-ready):
```yaml
---
id: LRN.01
type: one-sheet
title: Strategic Learning
author: Robert K. Kamei
year: 2021
domain: LEARNING
tags:
  - bvx-learn
  - cognitive-science
  - metacognition
  - study-techniques
  - spaced-repetition
related:
  - "[[📐 LRN.02 — Make It Stick — Brown (2014)]]"
source_type: published-book
date_created: 2026-03-28
status: complete
---
```

**Why this works for querying/RAG:**
- `id` field is unique, short, greppable
- `domain` field lets you filter all LEARNING entries, all SYSTEMS entries, etc.
- `tags` array is what Obsidian search, Dataview, and any RAG ingestion pipeline will eat
- `related` field with wikilinks creates the Zettelkasten web — cross-references between entries
- `type: one-sheet` distinguishes these from your other Obsidian note types (book summaries, SSOT entries, etc.)

**Proposed domain codes:**

| Code | Domain | Covers |
|------|--------|--------|
| LRN | Learning & Education | Study methods, pedagogy, cognitive science |
| PSY | Psychology & Mindset | Behavior, motivation, mental models |
| SYS | Systems & Design | Systems thinking, architecture, complexity |
| BIZ | Business & Strategy | Entrepreneurship, management, economics |
| FIT | Fitness & Health | Training, nutrition, body mechanics |
| CRE | Creative & Narrative | Storytelling, worldbuilding, art |
| TEC | Technology & Engineering | Programming, AI, tools |
| FIN | Finance & Money | Investing, income, financial systems |
| PHI | Philosophy & Spirituality | Metaphysics, ethics, consciousness |

You can add domains as needed — the 3-letter code just needs to be unique.
```
This block is not supported on your current device yet.
```

Waiting for user responses.Once you answer these I'll build the final Project instructions prompt, the updated template with YAML, and the Strategic Learning entry as the first specimen — all ready to drop into a Claude Project.

---

## 🧑 Papi  <sub>2026-03-28 10:01:39</sub>

Q: Series emoji — which one brands the one-sheets?
A: 🧬 (DNA — extracting the core code)

Q: Does the ID + YAML + domain code system work?
A: Yes, this ID system works

Q: Any extra sections to add to the one-sheet beyond invariants/heuristics/concepts? (Select all that apply)
A: Key vocabulary / jargon definitions, Notable quotes (1-3 max)

---

## 🤖 Claude  <sub>2026-03-28 10:03:44</sub>

The user wants me to create:

1. A Claude Project custom instructions prompt (the agent prompt)
2. The updated BVX-LEARN v2 template with YAML, emoji branding, vocabulary, quotes sections
3. The Strategic Learning one-sheet rebuilt as the first specimen using the new format

Let me build all three.Let me build all three pieces — the Project instructions, the final template, and the Strategic Learning specimen.
```
This block is not supported on your current device yet.
```

Now let me create the specimen one-sheet for Strategic Learning using the finalized format.
```
This block is not supported on your current device yet.
```

Now let me copy everything to outputs and present.
```
This block is not supported on your current device yet.
```

Good, let me present both files.
```
This block is not supported on your current device yet.
```

Done. Let me summarize what was delivered.Here's your setup:

**File 1 — Project Instructions:** Paste this into a new Claude Project's custom instructions field. It contains the full agent prompt — trigger commands (`BVX-LEARN this`, `BVX-LEARN [title]`, branching), the ID system with domain codes, the exact template structure, extraction rules for how to identify invariants vs. heuristics vs. concepts, output rules, and handling for both PDFs and title-only requests.

**File 2 — LRN.01 Specimen:** The Strategic Learning one-sheet rebuilt in the final format with YAML front matter, the 🧬 branding, vocabulary table, and quotes section. Drop this into your Obsidian vault as the first entry and the reference example.

**To get running:**
1. Create a new Claude Project
2. Paste the Project Instructions into the custom instructions
3. Each new book = new conversation in that project
4. Drop a PDF or type `BVX-LEARN [book title]` and it generates
5. Export the `.md` to your vault

One thing to keep in mind — the serial numbers (LRN.01, LRN.02, etc.) need you to tell the agent where you're at. First time in a domain just say "this is LRN.01" or let it ask. After that you'll track what number you're on.

---

## 🧑 Papi  <sub>2026-03-28 10:07:38</sub>

Okay. So the deal is I need you to fix the template for this and learn dot o one. There needs to be a table of contents. That's, like, the biggest thing. Also, can you give me short instruction afterwards on how to set up the learn project instructions and stuff and all that whole jazz things? Also, can I just get the title of the book and the author and can you pull information from that? Do you need the PDF? Because some of the books, I only I don't have the actual PDF. Yet, or I could I don't know. I mean, what do you think?

---

## 🤖 Claude  <sub>2026-03-28 10:10:58</sub>

The user wants three things:

1. Fix the template and LRN.01 to include a table of contents
2. Short instructions on how to set up the Claude Project
3. Clarification on whether they need to provide a PDF or if just a title/author works

Let me address #3 first in my response, then rebuild the files.

For the TOC - I need to add markdown anchor links to each section in both the template and the specimen.

The project instructions already handle both PDF and title-only workflows, so I just need to explain that clearly.

Let me rebuild all three files.On the PDF question — title and author is enough. The project instructions already have a workflow for that: I search the web, cross-reference reviews, chapter summaries, publisher descriptions, and academic discussions to extract the content. The YAML just gets flagged `status: draft` instead of `complete` so you know it wasn't sourced from the full text. If you later get the PDF, you can drop it in and say "upgrade this to complete" and I'll fill in any gaps.

Full PDF obviously gives a more precise extraction, but for most non-fiction books, the core invariants and heuristics are well-documented enough online that a title-only entry is 80-90% there.

Let me rebuild everything with the TOC and the setup instructions.
```
This block is not supported on your current device yet.
```

Need to use str_replace or delete and recreate. Let me just use bash to remove then recreate.
```
This block is not supported on your current device yet.
```

Let me recreate both files.
```
This block is not supported on your current device yet.
```

Now recreate the specimen with TOC.
```
This block is not supported on your current device yet.
```

Now create the setup instructions.
```
This block is not supported on your current device yet.
```

Now copy all three to outputs and present.
```
This block is not supported on your current device yet.
```

Present the files.
```
This block is not supported on your current device yet.
```

Done. Let me summarize what they got.Three files, everything you need:

**Setup Guide** — step-by-step: create project, paste instructions, how to use trigger commands, how to export to Obsidian, serial number tracking. Takes about 3 minutes to get running.

**Project Instructions** — the full agent prompt. Paste this into your Claude Project's custom instructions field. It handles both PDF uploads and title-only requests, has the full template with TOC baked in, the ID system, domain codes, extraction rules, and branching.

**LRN.01 Specimen** — Strategic Learning with the TOC added, ready to drop into your vault as the first entry.

To answer your question directly: title + author is all you need. Just type something like `BVX-LEARN Atomic Habits by James Clear` into a new conversation in the project and it'll research and generate. The YAML gets flagged `status: draft` so you know it wasn't sourced from the full text. If you get the PDF later, you drop it in and say `Upgrade LRN.02` and it fills the gaps.

---

## 🧑 Papi  <sub>2026-03-28 10:20:33</sub>

I primarily like to use the voice mechanism. Like, I'm using a mic right now. So what do I just say? BBX Learn. And then copy and paste whatever I wanna do?

---

## 🤖 Claude  <sub>2026-03-28 10:20:48</sub>

The user is asking about how to use voice input with the BVX-LEARN system. They're pointing out that saying "BVX-LEARN" via voice is awkward. I should suggest simpler, voice-friendly trigger phrases and update the project instructions accordingly.Yeah that's the issue — "BVX-LEARN" is a pain to say out loud and voice-to-text will mangle it every time. Let me give you voice-friendly triggers instead.

What would actually work well for voice:

- **"Learn this"** — when you've uploaded a PDF
- **"Learn [book title]"** — title only, no PDF
- **"Go deeper on [topic]"** — for branching
- **"Upgrade this"** — when you're adding a PDF to a draft

So your actual workflow would be: open the project, start a new conversation, and just say something like:

*"Learn Make It Stick by Brown"*

or

*"Learn Atomic Habits by James Clear"*

or if you uploaded a PDF first:

*"Learn this"*

That's it. The project instructions handle everything else behind the scenes.

Want me to update the Project Instructions file with these voice-friendly triggers so it recognizes all of them? I'll keep the typed versions too but add the short spoken ones as aliases.
```
This block is not supported on your current device yet.
```

Waiting for user response.

---

## 🧑 Papi  <sub>2026-03-28 10:20:55</sub>

Q: Update project instructions with voice-friendly triggers?
A: Yes, update the instructions with voice triggers

---

## 🤖 Claude  <sub>2026-03-28 10:21:42</sub>

Let me update the project instructions with voice-friendly triggers added as aliases.
```
This block is not supported on your current device yet.
```

Now update the setup guide too so the usage examples reflect voice triggers.Now let me update the setup guide to match.
```
This block is not supported on your current device yet.
```

Good, now copy to outputs.
```
This block is not supported on your current device yet.
```

Done.
```
This block is not supported on your current device yet.
```

Done. Updated both files.Done. Your daily workflow is now just:

1. Open the project
2. New conversation
3. Say **"Learn [book title] by [author]"**

That's it. The setup guide also has a quick cheat sheet table of all the voice commands so you can glance at it until they're muscle memory. Everything recognizes fuzzy voice input — you don't need to say any exact phrase, the instructions tell Claude to match on intent not exact wording.