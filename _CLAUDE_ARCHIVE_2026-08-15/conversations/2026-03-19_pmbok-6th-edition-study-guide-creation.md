---
title: "PMBOK 6th edition study guide creation"
uuid: 70ae79b9-2168-4b06-8639-d088fd482d48
created: 2026-03-19
updated: 2026-03-19
trunk: BLACK
messages: 18
chars: 29654
artifacts: 0
generated_files: 5
tools: [ask_user_input_v0, bash_tool, create_file, present_files, str_replace, view]
source: claude.ai-export-2026-08-15
---

# PMBOK 6th edition study guide creation

> **Conversation Overview**

The person is studying the PMBOK 6th Edition using Ricardo Vargas's structured reading guide and asked Claude to help create a comprehensive markdown knowledgebase study guide based on that reading flow. They uploaded both the Vargas cheat sheet PDF and the full PMBOK 6th Edition PDF. Before executing, Claude asked clarifying questions to align on format, depth, extras, scope approach, and study goal. The person specified markdown format, deep coverage sufficient to study from without opening the PMBOK, mnemonics and memory tricks, visual process flow diagrams, and progress tracker checkboxes. They chose a step-by-step incremental build and confirmed the goal as general understanding of PM frameworks rather than PMP exam prep.

Claude built all five steps of the Vargas reading flow as separate markdown files, each with navigatable tables of contents using standard anchor link syntax compatible with Obsidian and VSCode. The five guides total 3,727 lines across approximately 624 pages of source material. Step 1 covered foundations including project definition, Process Groups, Knowledge Areas, EEFs, OPAs, PMO types, and the PMI Talent Triangle. Step 2 covered introductions to all 10 Knowledge Areas with process tables, key concepts, trends, and agile considerations. Step 3 covered Process Group structure and process flow with ASCII diagrams showing how processes connect across groups. Step 4 — the largest at 913 lines — covered all 49 processes in detail including the complete EVM formula set, risk response strategies for threats and opportunities, contract type spectrum, quality tools, Tuckman team development stages, conflict resolution techniques, and a full ITTO quick reference. Step 5 covered the optional appendices including the agile/adaptive continuum, key concepts summary per KA, tailoring considerations, the 132 tools and techniques catalog, common acronyms, and must-know glossary definitions.

Each guide follows a consistent structure: progress tracker with checkboxes, navigatable table of contents, deep content with mnemonics and ASCII diagrams, and 10–20 self-check questions at the end. The person requested the TOC be made navigatable after Step 1 was delivered, and Claude retrofitted anchor links into that guide before continuing with subsequent steps using the same pattern from the start.

**Files produced**

- [step1_warmup_study_guide.md](../files/2026-03-19_step1-warmup-study-guidemd.md)
- [step2_knowledge_areas_study_guide.md](../files/2026-03-19_step2-knowledge-areas-study-guidemd.md)
- [step3_process_groups_study_guide.md](../files/2026-03-19_step3-process-groups-study-guidemd.md)
- [step4_processes_detail_study_guide.md](../files/2026-03-19_step4-processes-detail-study-guidemd.md)
- [step5_optional_reading_study_guide.md](../files/2026-03-19_step5-optional-reading-study-guidemd.md)

---
## 🧑 Papi  <sub>2026-03-19 09:46:02</sub>

ok so i am going by a guide to read and understand the pmbok 6th edition. if i upload the guide cheat cheet (ricardo vargas) and the pmbok 6th edition will you help me create some sort of study guide  based on the how to read sheet? they're all in pdf

---

## 🤖 Claude  <sub>2026-03-19 09:46:07</sub>

Absolutely, I can help you build a study guide based on Ricardo Vargas' recommended reading flow for the PMBOK 6th Edition. Upload both PDFs — the Vargas cheat sheet and the PMBOK 6th Edition — and I'll work through them to create a structured study guide that follows his suggested reading order and highlights the key concepts at each stage.

Ready when you are.

---

## 🧑 Papi  <sub>2026-03-19 09:48:01</sub>

please confirm with me with what you rplan is before executing. provide me with clarificing questions to help produce what we both want ideally

---

## 🤖 Claude  <sub>2026-03-19 09:48:23</sub>

Great, I've got both files. Let me share my plan and ask some clarifying questions so we land on exactly what you need.

**What I'm thinking:**

I'd follow the Vargas 5-step reading flow (Warm Up → Knowledge Area Intros → Process Groups & Flow → Processes in Detail → Optional Reading) and for each step, pull the relevant content from your PMBOK 6th Edition PDF to create a structured study guide. For each reading chunk, the guide would include things like key concepts/definitions, important inputs-tools-outputs (ITTOs), relationships between processes, and study tips or mnemonics where helpful.

**Format question — this is the big one:**

The output could take very different shapes depending on how you want to use it. Let me know what sounds right:
```
This block is not supported on your current device yet.
```

A couple more things I want to confirm regardless of your choices above:

**Scope check** — The PMBOK is 700+ pages. Even with the Vargas reading order, a truly comprehensive study guide would be massive. Should I tackle this step-by-step (starting with Step 1, then you come back for Step 2, etc.) or do you want me to attempt the whole thing in one go? Step-by-step would let us dial in quality before I plow through all 600+ pages of content.

**PMP exam focus?** — Are you studying for the PMP exam specifically, or more for general understanding of project management? This affects whether I emphasize exam-style traps and distinctions vs. practical application.

---

## 🧑 Papi  <sub>2026-03-19 09:49:09</sub>

Q: What format do you want the study guide in?
A: markdown knowledgebase document

Q: What depth of content per reading section?
A: Deep — comprehensive notes I could study from without opening the PMBOK

Q: Any extras you'd want included? (Select all that apply)
A: Mnemonics / memory tricks, Visual process flow diagrams, Checkboxes / progress tracker

---

## 🤖 Claude  <sub>2026-03-19 09:49:24</sub>

The user wants:
- Format: Markdown knowledgebase document
- Depth: Deep — comprehensive notes they could study from without opening the PMBOK
- Extras: Mnemonics/memory tricks, Visual process flow diagrams, Checkboxes/progress tracker

They haven't answered my two additional questions yet:
1. Step-by-step vs all at once
2. PMP exam focus vs general understanding

Let me ask those before proceeding. But actually, let me think about this more carefully. The PMBOK is 700+ pages. Even extracting text from it will be a massive undertaking. I should be realistic about what I can do in one session.


I should ask the remaining clarifying questions and propose a practical approach that acknowledges the scope constraints.Great choices. Markdown knowledgebase with deep coverage, mnemonics, flow diagrams, and progress tracking — that's going to be a substantial and genuinely useful document.

Before I dive in, I still need your take on those last two questions:
```
This block is not supported on your current device yet.
```

Waiting for user responses.Once I have these answers I'll have everything I need to start building.

---

## 🧑 Papi  <sub>2026-03-19 09:49:49</sub>

Q: Should I build this incrementally or all at once? (Deep coverage of the full PMBOK will be a very large document — step-by-step lets us nail the format first)
A: Step-by-step — start with Step 1, refine, then continue

Q: What's the goal of your study?
A: General understanding — practical knowledge of PM frameworks

---

## 🤖 Claude  <sub>2026-03-19 09:59:09</sub>

The user wants me to:

1. Build a markdown knowledgebase study guide following the Vargas reading order
2. Deep coverage - comprehensive enough to study without opening PMBOK
3. Include mnemonics, visual process flow diagrams (in mermaid?), and checkboxes/progress tracker
4. Step-by-step approach - starting with Step 1 (Warm Up)
5. Focus on general understanding / practical knowledge

Step 1 (Warm Up) covers:
- Part 1, Chapter 1: Introduction (pages 1-35)
- Part 1, Chapter 2: The Environment in Which Projects Operate (pages 37-49)


- Part 1, Chapter 3: The Role of the Project Manager (pages 51-68)
- Part 2, Chapter 1: Introduction (pages 541-559)

That's 85 pages total, about 14% of the PMBOK. I need to extract and synthesize the content from these sections to build out the study guide.Perfect — Step 1 (Warm Up) it is. Let me first read the relevant PMBOK sections for Step 1, then I'll build the guide.

Step 1 covers 85 pages across four sections. Let me extract the content now.
```
This block is not supported on your current device yet.
```

579 pages. Let me extract text from the relevant page ranges. The PMBOK page numbers in the cheat sheet refer to the book's internal page numbering, which may differ from PDF page numbers. Let me extract text and figure out the offset.
```
This block is not supported on your current device yet.
```

Let me find the offset. The book pages start at some PDF page. Let me search for "Chapter 1" or "INTRODUCTION" to find where page 1 of the book starts.
```
This block is not supported on your current device yet.
```

So PDF page 29 seems to be the start of Part 1. Let me check pages 30-32 to find where Chapter 1/page 1 of the book starts.
```
This block is not supported on your current device yet.
```

So PDF page 30 = Book page 1 (Chapter 1 Introduction). The offset is 29. So book page N = PDF page N + 29.

Let me verify: Book pages 1-35 = PDF pages 30-64. Let me check page 64.
```
This block is not supported on your current device yet.
```

Let me check: PDF page 66 = "THE ROLE OF THE PROJECT MANAGER" which is Chapter 3, starting at book page 51. So 66 - 51 = 15... wait that doesn't match. Let me recalculate.

PDF page 30 = Book page 1 → offset = 29
PDF page 66 = Book page 66-29 = 37... but Chapter 3 starts at book page 51.

Hmm, that's not right. Let me check more carefully. Let me look for the actual page numbers printed on the pages.

Actually wait - the cheat sheet says:
- Chapter 2: pages 37 to 49


- Chapter 3: pages 51 to 68

So if PDF page 66 shows Chapter 3 content that corresponds to book page 51, the offset would be 15, but that contradicts my earlier calculation of offset 29 from the front matter. The page numbering must shift between the front matter and the actual book content. Let me trace through what's between PDF pages 30 and 66 to figure out where this transition happens.

Looking at the chapter breakdown from the sheet, Chapter 1 spans 35 pages, Chapter 2 spans 13 pages, and Chapter 3 spans 18 pages. If Chapter 1 starts at PDF page 30, it should end around PDF page 64, which would put Chapter 2 starting at PDF page 65 and Chapter 3 at PDF page 78. But PDF page 66 is clearly showing Chapter 3 content, so something's off with my offset calculation.

Let me try searching for the chapter headings directly in the PDF instead of relying on the page number mapping.
```
This block is not supported on your current device yet.
```

Now I can map:
- Chapter 1 (Introduction): PDF page 30, book page 1 → offset = 29
- Chapter 2 (Environment): PDF page 56, book page 37 → offset = 19
- Chapter 3 (Role of PM): PDF page 66, book page 51 → offset = 15
- Chapter 4 (Integration): PDF page 80, book page 69 → offset = 11

The offset keeps changing. The PDF must not have consistent page numbering, or there are unnumbered pages. Let me just find the exact PDF pages for each section I need.

For Step 1 (Warm Up):


- Chapter 1 spans PDF pages 30-55, Chapter 2 spans 56-65, and Chapter 3 spans 66-79. Now I need to locate Part 2, Chapter 1 which starts at book page 541.
```
This block is not supported on your current device yet.
```

Part 2 starts at PDF page 421. Let me find where Part 2 Chapter 1 (Introduction) is, which should be around PDF page 422-423.
```
This block is not supported on your current device yet.
```

Now I have the PDF page mappings:

Step 1 - Warm Up sections:
1. Chapter 1 (Introduction): PDF pages 30-55 (book pages 1-35ish)
2. Chapter 2 (Environment): PDF pages 56-65 (book pages 37-49)
3. Chapter 3 (Role of PM): PDF pages 66-79 (book pages 51-68)
4. Part 2, Chapter 1 (Introduction to The Standard): PDF pages 422-434 (book pages 541-559)

Let me extract all this text now.
```
This block is not supported on your current device yet.
```

Good, I have all the text extracted. Now let me read through each section to build the study guide. Let me start by reading each file.
```
This block is not supported on your current device yet.
```

Good, I have Chapter 1. Now let me read Chapter 2 and 3.
```
This block is not supported on your current device yet.
```

Good, let me now read Chapter 3 and Part 2 Chapter 1.
```
This block is not supported on your current device yet.
```

Now let me read Part 2 Chapter 1.
```
This block is not supported on your current device yet.
```

Now I have all the content for Step 1. Let me now build the comprehensive study guide markdown file. I need to read the skill for creating markdown or documents, but since this is a markdown file, let me just create it directly.

Let me structure the study guide following the Vargas reading order for Step 1. I'll create it as a comprehensive markdown document with:
- Progress tracking checkboxes
- Deep notes organized by chapter
- Mnemonics
- Visual flow diagrams (using mermaid)
- Key terms and definitions

Let me build this now.Now I have all the content. Let me build the Step 1 study guide. This is going to be a substantial document — let me craft it properly.
```
This block is not supported on your current device yet.
```

Now let me copy it to outputs and present it.
```
This block is not supported on your current device yet.
```

Let me present the file.
```
This block is not supported on your current device yet.
```

Great, the file is ready. Let me provide a concise summary.Here's your Step 1 — Warm Up study guide. It covers all four reading sections (about 800 lines of content) and includes:

- **Progress tracker** with checkboxes for each reading chunk
- **Deep coverage** of all key concepts from Chapters 1, 2, 3, and Part 2 Chapter 1
- **Mnemonics** throughout (TUC for project traits, PI-I-AH for life cycles, I Prefer Eating Mom's Cookies for Process Groups, and many more)
- **Visual diagrams** in ASCII/text format showing the portfolio hierarchy, PM spheres of influence, data flow, Talent Triangle, etc.
- **Comparison tables** for org structures, leadership styles, power types, life cycle types
- **15 self-check questions** at the end to test yourself before moving to Step 2

Take a look through it and let me know if you want me to adjust anything — the depth, the tone, more/fewer mnemonics, different formatting, etc. Once you're happy with the format, I'll build Step 2 (Knowledge Area Introductions) using the same template.

---

## 🧑 Papi  <sub>2026-03-19 10:00:23</sub>

please. insert a table of contents that is navigatable in .md like in obsidian or vscode

---

## 🤖 Claude  <sub>2026-03-19 10:01:07</sub>

The user wants me to add a navigatable table of contents to the markdown file. In Obsidian and VSCode, markdown headers automatically create anchors that can be linked to using `[text](#header-slug)` format. I need to create a TOC that links to all the major sections.
```
This block is not supported on your current device yet.
```

I need to insert a table of contents after the progress tracker section and before the Chapter 1 content. Let me build the TOC with proper markdown anchor links.
```
This block is not supported on your current device yet.
```

Now copy to outputs and present.
```
This block is not supported on your current device yet.
```

Done, let me present the file.
```
This block is not supported on your current device yet.
```

Done. The TOC uses standard markdown anchor links that work in Obsidian, VSCode, and most markdown renderers.Done — the TOC is now right after the Progress Tracker. All links use standard markdown anchor syntax (`#header-slug`) so they'll be clickable in Obsidian, VSCode preview, GitHub, and most markdown renderers.

When you're ready, just say the word and I'll build Step 2 (Knowledge Area Introductions) in the same format.

---

## 🧑 Papi  <sub>2026-03-19 10:05:46</sub>

ok go for next step

---

## 🤖 Claude  <sub>2026-03-19 10:13:24</sub>

The user wants me to build Step 2 of the study guide. Step 2 covers the Introduction sections of all 10 Knowledge Areas (Chapters 4-13). Let me extract those pages from the PMBOK PDF.

From the Vargas cheat sheet:
- Ch 4: Project Integration Management (Introduction) - Pages 69-74
- Ch 5: Project Scope Management (Introduction) - Pages 129-133
- Ch 6: Project Schedule Management (Introduction) - Pages 173-178
- Ch 7: Project Cost Management (Introduction) - Pages 231-234
- Ch 8: Project Quality Management (Introduction) - Pages 271-276


- Ch 9: Project Resource Management (Introduction) - Pages 307-311
- Ch 10: Project Communications Management (Introduction) - Pages 359-365
- Ch 11: Project Risk Management (Introduction) - Pages 395-400
- Ch 12: Project Procurement Management (Introduction) - Pages 459-465
- Ch 13: Project Stakeholder Management (Introduction) - Pages 503-506

I need to figure out the PDF page offset. From earlier exploration, Book page 1 (Chapter 1 Introduction) maps to PDF page 30, so the offset is approximately 29. Now I'll extract each Introduction section using this offset to convert book pages to PDF pages.Let me extract all 10 Knowledge Area introduction sections from the PMBOK.
```
This block is not supported on your current device yet.
```

Good, let me read each section now.
```
This block is not supported on your current device yet.
```

That seems to have gone past the introduction section. Let me check - the Vargas sheet says Ch4 Introduction is pages 69-74. Let me verify what's actually at those pages.
```
This block is not supported on your current device yet.
```

The offset is wrong. Let me recalculate. Chapter 4 should start at book page 69, but the content at PDF page 98 is mid-chapter (section 4.3). Let me find where Chapter 4 actually starts in the PDF.
```
This block is not supported on your current device yet.
```

So Chapter 4 starts at PDF page 80. Book page should be around 69. So offset is 80 - 69 = 11. Wait, that doesn't match what I found earlier. Let me check - earlier I found Chapter 1 starts at PDF page 30, which would be book page 1, so offset = 29. But that doesn't work for Chapter 4.

Wait - the book has different numbering. The PMBOK uses roman numerals for front matter, then restarts at page 1 for the actual content. But the PDF page numbers might be off because of additional pages. Let me just find the actual PDF pages for each chapter intro and extract directly from those.


Now I'm seeing the Vargas sheet lists Chapter 4 Introduction at pages 69-74, which maps to PDF page 80 - that's an offset of 11. But Chapter 1 had an offset of 29, which doesn't align. The discrepancy suggests the PDF and physical book have different pagination, possibly due to front matter or blank pages affecting the numbering differently across sections. I should just search for the actual PDF pages directly rather than trying to calculate offsets.
```
This block is not supported on your current device yet.
```

Now I need to figure out how many pages the "introduction" section of each chapter is. Based on the Vargas sheet, the intro sections are:
- Ch4: 6 pages
- Ch5: 5 pages
- Ch6: 6 pages
- Ch7: 4 pages
- Ch8: 6 pages
- Ch9: 5 pages
- Ch10: 7 pages
- Ch11: 6 pages
- Ch12: 7 pages
- Ch13: 4 pages

So I should extract from each chapter start PDF page for the specified number of pages.
```
This block is not supported on your current device yet.
```

Good. Now let me read all of them.
```
This block is not supported on your current device yet.
```

OK, I've got the integration chapter intro. Let me now read the other chapters quickly.
```
This block is not supported on your current device yet.
```

Let me get the remaining chapters.
```
This block is not supported on your current device yet.
```

OK, I now have all the content I need. Let me create the Step 2 study guide. This covers the introductions to all 10 Knowledge Areas. For each one, the intro sections include:
- Overview and process listing
- Key concepts
- Trends and emerging practices
- Tailoring considerations
- Agile/adaptive considerations

Let me write a comprehensive study guide following the same format as Step 1.Now I have all 10 Knowledge Area introductions. Let me build the Step 2 guide.
```
This block is not supported on your current device yet.
```

Let me copy to outputs and present.
```
This block is not supported on your current device yet.
```

Good, 756 lines. Let me present it.
```
This block is not supported on your current device yet.
```

Done. Let me give a quick summary.Here's your Step 2 guide — 756 lines covering all 10 Knowledge Area introductions. It follows the same format as Step 1 with:

- **Navigatable Table of Contents** with anchor links for every section
- **Progress tracker** with checkboxes for all 10 chapters
- **Process tables** for each KA showing process name, Process Group, and what it does
- **Mnemonics** for process orders and key concepts (5Cs, COQ tree, quality levels, etc.)
- **ASCII diagrams** for the quality flow, scope validation pipeline, and schedule model pipeline
- **Master summary** at the end including a 49-process count table, quick-reference comparison, and the agile vs. predictive pattern that runs through all KAs
- **15 self-check questions**

Take a look and let me know if you want any adjustments. When you're ready, I'll tackle Step 3 (Process Groups and PMBOK Process Flow — the 74-page deep dive into Part 2, Sections 2–6).

---

## 🧑 Papi  <sub>2026-03-19 10:20:47</sub>

step 3 go

---

## 🤖 Claude  <sub>2026-03-19 10:24:48</sub>

The user wants me to create Step 3 of the study guide. Step 3 covers Process Groups and PMBOK Process Flow (Part 2, Sections 2-6), which is 74 pages covering pages 561-635 of the book. Let me extract those sections.Let me extract the Process Groups content from Part 2.
```
This block is not supported on your current device yet.
```

So the sections are:
- Section 2 (Initiating): PDF 435-438
- Section 3 (Planning): PDF 439-463
- Section 4 (Executing): PDF 464-477
- Section 5 (M&C): PDF 478-494
- Section 6 (Closing): PDF 495-497 (or so)
```
This block is not supported on your current device yet.
```

Good. Let me read through each section now.
```
This block is not supported on your current device yet.
```

Let me read the rest of the sections.
```
This block is not supported on your current device yet.
```

Let me also read the executing, monitoring, and closing sections.
```
This block is not supported on your current device yet.
```

Now I have all the content. Let me build the Step 3 study guide. This step is about the Process Groups and the flow of processes. I need to focus on the overall structure, the 49 processes organized by Process Group, and the flow/interactions between them.Now I have all the content. Let me build the Step 3 guide.
```
This block is not supported on your current device yet.
```

Let me copy to outputs and present it.
```
This block is not supported on your current device yet.
```

Good, 722 lines. Let me present it.
```
This block is not supported on your current device yet.
```

Done. Let me give a summary.Here's your Step 3 guide — 722 lines covering the Process Groups and PMBOK Process Flow. Highlights:

- **The complete 49-process map** (the single most important table in the PMBOK) organized by Knowledge Area × Process Group
- **ASCII flow diagrams** for each Process Group showing how processes connect and feed into each other
- **The Planning process flow** showing the logical sequence: Scope → Schedule → Cost → Quality/Resource/Comms → Risk → Procurement/Stakeholder
- **The full Executing and M&C process tables** with key benefits and frequency
- **Cross-group flow analysis** — what documents and outputs flow between Process Groups
- **The three baselines** and how they form the performance measurement baseline
- **Process frequency summary** — which processes run once, periodically, or continuously
- **Most-connected documents** (risk register, lessons learned register, assumption log, stakeholder register)
- **15 self-check questions**

Now, Step 4 is the monster — 409 pages covering 65% of the PMBOK. It's the full detailed content for all 10 Knowledge Areas. Want me to tackle it Knowledge Area by Knowledge Area (starting with Integration, then Scope, etc.), or do you want to take a different approach given the sheer size?

---

## 🧑 Papi  <sub>2026-03-19 10:25:56</sub>

ok go for next step

---

## 🤖 Claude  <sub>2026-03-19 10:31:09</sub>

Step 4 is massive - 409 pages covering all 10 Knowledge Areas in detail. Let me extract the content systematically. I'll need to pull each Knowledge Area's detailed process content (excluding the intro sections we already covered in Step 2).

From the Vargas cheat sheet, Step 4 covers:
- Ch 4 Integration: pp 75-128 (54 pages)
- Ch 5 Scope: pp 134-171 (38 pages)
- Ch 6 Schedule: pp 179-230 (52 pages)
- Ch 7 Cost: pp 235-270 (36 pages)


- Ch 8 Quality: pp 277-306 (30 pages)
- Ch 9 Resource: pp 312-358 (47 pages)
- Ch 10 Communications: pp 366-393 (28 pages)
- Ch 11 Risk: pp 401-458 (58 pages)
- Ch 12 Procurement: pp 466-501 (36 pages)
- Ch 13 Stakeholder: pp 507-536 (30 pages)

This is a massive amount of material to work through. I need to be strategic about extracting the key process details from each Knowledge Area while respecting the context window limitations.Step 4 is the big one — 409 pages, 65% of the PMBOK. I'll extract all 10 Knowledge Areas and build the guide. This will take several extractions given the volume.
```
This block is not supported on your current device yet.
```

That's 743,841 characters total - way too much to read all at once. I need to be strategic. Let me read each chapter and extract the key information: processes, ITTOs, important tools & techniques, and key concepts. I'll read them in chunks and build the guide as I go.

Let me read each chapter focusing on the process-level detail - specifically the tools & techniques sections which are the most valuable study content.
```
This block is not supported on your current device yet.
```

This is a massive amount of content. Let me read the key sections from each chapter to extract the most important tools & techniques and concepts. I'll focus on what's most study-worthy rather than trying to capture every detail.

Given the size, I'll create a comprehensive but focused study guide that covers:
1. Each process with its complete ITTO summary
2. Key tools & techniques explained (not just listed)
3. Important concepts and distinctions
4. Critical formulas (EVM, etc.)

Let me read the most important sections from each chapter.
```
This block is not supported on your current device yet.
```

OK, I have a good sense of the content. Given the massive volume (409 pages), I need to create a comprehensive study guide that captures the essential study-worthy content from each Knowledge Area without trying to reproduce the entire PMBOK. Let me focus on:

1. Complete ITTO tables for all 49 processes
2. Key tools & techniques explained
3. Important formulas (especially EVM)
4. Critical distinctions and concepts
5. Contract types for procurement

Let me read a few more key sections and then build the guide.
```
This block is not supported on your current device yet.
```

Let me get the risk response strategies and procurement contract types, then build the guide.
```
This block is not supported on your current device yet.
```

Now let me get the contract types detail.
```
This block is not supported on your current device yet.
```

Now I have enough material to build a comprehensive Step 4 study guide. Given the massive volume (409 pages), I need to focus on the most study-worthy content:

1. ITTO summaries for all 49 processes
2. Key tools & techniques explained (estimating techniques, EVM formulas, risk strategies, contract types, etc.)
3. Critical concepts and distinctions
4. Important formulas

Let me build this now. It's going to be a large document.Now I have all the key content. Let me build the Step 4 guide — this will be the largest one.
```
This block is not supported on your current device yet.
```

Let me copy this to outputs and present it.
```
This block is not supported on your current device yet.
```

913 lines - that's a substantial document. Let me present it.
```
This block is not supported on your current device yet.
```

Done. Let me summarize what's in this guide.Here's your Step 4 guide — 913 lines distilling 409 pages of PMBOK detail into the essential study-worthy content. The big highlights:

**Formulas & Calculations:**
- Complete EVM formula set (PV, EV, AC, SV, CV, SPI, CPI, EAC variants, ETC, TCPI, VAC)
- Three-point estimating (triangular and PERT/Beta)
- Communication channels formula
- EMV for decision trees
- Self-check answers with worked examples

**Key Frameworks:**
- All risk response strategies for threats (EATMA) and opportunities (EESEA)
- Complete contract type spectrum (FFP → FPIF → FPEPA → T&M → CPIF → CPFF → CPAF) with risk allocation
- Tuckman team development stages
- Five conflict resolution techniques
- Seven basic quality tools
- Stakeholder engagement assessment matrix
- Power/Interest grid strategies

**Reference Tables:**
- Complete ITTO quick reference for all 49 processes (organized by Process Group)
- Project charter contents checklist
- PM plan components (10 subsidiary plans, 4 baselines, additional components)
- Budget component hierarchy (work packages → contingency reserves → management reserves)
- Data flow diagram across the project

**20 self-check questions** with calculation answers provided.

That completes the core study guide (Steps 1–4 = 100% of the PMBOK). Step 5 is optional reading (appendices on Agile, key concept summaries, tools reference, glossary). Want me to build that too, or would you like to refine any of the existing guides first?

---

## 🧑 Papi  <sub>2026-03-19 10:32:08</sub>

build step 5 as well

---

## 🤖 Claude  <sub>2026-03-19 10:35:42</sub>

Let me extract the Step 5 optional reading sections from the PMBOK.
```
This block is not supported on your current device yet.
```

Now let me extract all the Step 5 content.
```
This block is not supported on your current device yet.
```

Let me read the content of each section.
```
This block is not supported on your current device yet.
```

Good, now let me read X4 and X6.
```
This block is not supported on your current device yet.
```

Now let me read X6 and a sample of the glossary.
```
This block is not supported on your current device yet.
```

Good, I have all the content I need. Now let me build the Step 5 guide.Now I have everything. Let me build the Step 5 guide.
```
This block is not supported on your current device yet.
```

Done, now copy to outputs and present.
```
This block is not supported on your current device yet.
```

Let me also count the total lines across all 5 guides.
```
This block is not supported on your current device yet.
```

Great, that's a comprehensive study guide. Let me present the final file.
```
This block is not supported on your current device yet.
```

Done. Let me give a summary.Step 5 is done — and with it, the entire study guide is complete. Here's what you now have:

| Guide | Lines | Key Content |
|---|---|---|
| **Step 1** — Warm Up | 872 | Foundations, project definition, Process Groups, Knowledge Areas, EEFs/OPAs, PMO types, Talent Triangle |
| **Step 2** — KA Introductions | 756 | All 10 Knowledge Area overviews, key concepts, trends, agile considerations, 49-process map |
| **Step 3** — Process Groups | 722 | Process flow diagrams, Planning sequence, Executing/M&C process tables, cross-group data flows, baselines |
| **Step 4** — Processes in Detail | 913 | EVM formulas, risk response strategies, contract types, quality tools, Tuckman stages, conflict management, complete ITTO reference |
| **Step 5** — Optional Reading | 464 | Agile continuum, key concepts summary, tailoring checklist, 132 T&T catalog, acronyms, glossary |
| **TOTAL** | **3,727 lines** | |

That's 3,727 lines of navigatable markdown distilling the entire 624-page PMBOK 6th Edition following the Ricardo Vargas reading flow. Every guide has a clickable table of contents, progress checkboxes, mnemonics, ASCII diagrams, and self-check questions.

Let me know if you'd like any refinements or if there's anything else you'd like to build from this foundation.