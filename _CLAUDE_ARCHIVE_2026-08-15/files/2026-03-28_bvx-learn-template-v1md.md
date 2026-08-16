---
original_path: "/home/claude/BVX_LEARN_TEMPLATE_v1.md"
source_conversation: "Creating study guides from books as learning templates"
created: 2026-03-28
trunk: BLACK
kind: generated-file
---

# BVX-LEARN TEMPLATE v1.0
## Strategic Learning Guide — Book/PDF Knowledge Entry Generator

---

> **PURPOSE:** Use this template when feeding Claude a book, PDF, or learning resource. Copy the structure below, replace the bracketed placeholders with the actual content, and the output will be a consistent, high-quality knowledge entry optimized for rapid comprehension and practical application.

> **HOW TO USE:** Paste this template into the conversation along with your book/PDF or book title, and tell Claude: *"Use the BVX-LEARN template to create a knowledge entry for this."*

---

## TEMPLATE START

```markdown
# [BOOK TITLE IN CAPS]
## Knowledge Entry — Study Guide & Strategic Breakdown

**Author:** [Author Name, credentials]
**Published:** [Year] · [Publisher]
**ISBN:** [ISBN if available]
**Pages:** [Page count]
**Origin:** [Context — was this a course, a research project, a personal journey?]
**Discipline Tags:** `[tag1]` · `[tag2]` · `[tag3]` · `[tag4]` · `[tag5]`

---

## TABLE OF CONTENTS

- [1. THESIS — What This Book Actually Says](#1-thesis)
- [2. CORE FRAMEWORK / MODEL](#2-core-framework--model)
- [3. KEY CONCEPTS BREAKDOWN](#3-key-concepts-breakdown)
- [4. MYTHS / MISCONCEPTIONS DESTROYED](#4-myths--misconceptions-destroyed)
- [5. ACTIONABLE TAKEAWAYS](#5-actionable-takeaways)
- [6. IMPLEMENTATION PROTOCOL](#6-implementation-protocol)
- [7. CROSS-REFERENCES & RELATED READING](#7-cross-references--related-reading)
- [8. SELF-ASSESSMENT CHECKLIST](#8-self-assessment-checklist)

---

## 1. THESIS

[2-3 paragraphs. What is the book's central argument in plain language? 
What problem does it solve? Who is it for? What makes this author's 
angle different from other books on the same topic? What's the ONE idea 
that, if you only remembered one thing, would capture the book's value?]

---

## 2. CORE FRAMEWORK / MODEL

[If the book has a central model, framework, or system, diagram it here.
Use ASCII art, tables, or step-by-step breakdowns. If the book doesn't 
have an explicit framework, construct one from the content — organize 
the book's ideas into a logical hierarchy or sequence.

Questions to answer:
- What are the major components/pillars/phases?
- How do they relate to each other?
- Is there a sequence (do X before Y)?
- Is there a hierarchy (X depends on Y)?]

```
[ASCII DIAGRAM OF THE FRAMEWORK]
```

[Explain the framework in 1-2 paragraphs after the diagram.]

---

## 3. KEY CONCEPTS BREAKDOWN

[For each major concept in the book, create a section with:]

### Concept Name
**What it is:** [1-2 sentence definition in plain language]
**Why it matters:** [1-2 sentences on practical significance]
**How it works:** [Deeper explanation — the mechanics, the research, the logic]
**Common mistake:** [How people typically get this wrong]
**Application:** [How to actually use this in practice]

[Repeat for each major concept. Aim for 4-8 concepts depending on book density.]

---

## 4. MYTHS / MISCONCEPTIONS DESTROYED

[List the false beliefs the book challenges. Format:]

### Myth: "[Common false belief]"
**Reality:** [What the evidence actually shows]
**Why this myth persists:** [Why people believe it despite the evidence]
**What to do instead:** [The correct approach]

[Repeat for each myth. Not all books have explicit myth-busting — 
if the book doesn't, reframe this as "COUNTERINTUITIVE INSIGHTS" 
and list the ideas that go against conventional wisdom.]

---

## 5. ACTIONABLE TAKEAWAYS

### The [N] Immediate Actions

[Numbered list of concrete, specific things the reader can do 
immediately after reading this entry. These should be:
- Specific (not "study better" → "close your book after 20 minutes and write everything you remember")
- Actionable (something you can do today, not a vague aspiration)
- Ordered by priority or sequence]

### The Priority Stack (In Order)
```
1. [First thing to do]     ← [Why this is first]
2. [Second thing to do]    ← [Why this follows]
3. [Third thing to do]     ← [Why this follows]
...
```

---

## 6. IMPLEMENTATION PROTOCOL

[This section is optional but high-value. Create a practical protocol 
for implementing the book's ideas. Could be:]

### Week 1: [Phase name]
- [Specific daily actions]
- [Metrics to track]
- [Milestones]

### Week 2-4: [Phase name]
- [Specific daily actions]
- [Metrics to track]  
- [Milestones]

### Ongoing: [Maintenance phase]
- [Habits to maintain]
- [Review schedule]

[Alternatively, this could be a single-page "cheat sheet" or 
"quick reference card" format for books that are more reference 
than transformation.]

---

## 7. CROSS-REFERENCES & RELATED READING

[Table format. What other books complement, extend, or challenge this one?]

| Book | Author | Relevance |
|------|--------|-----------|
| *[Title]* | [Author] | [How it connects to this book] |
| *[Title]* | [Author] | [How it connects to this book] |
| *[Title]* | [Author] | [How it connects to this book] |

[Aim for 5-8 entries. Mix complementary and contrasting perspectives.]

---

## 8. SELF-ASSESSMENT CHECKLIST

[Create a self-assessment rubric based on the book's content. 
10 items, rated 1-5.]

| # | Domain | Assessment Question | Score |
|---|--------|---------------------|-------|
| 1 | [Domain] | [Question] | /5 |
| 2 | [Domain] | [Question] | /5 |
| ... | ... | ... | /5 |
| 10 | [Domain] | [Question] | /5 |

**Scoring:**
- **40-50:** [What this level means]
- **25-39:** [What this level means]
- **Below 25:** [What this level means]

---

## META: ABOUT THIS ENTRY

- **Entry Type:** Knowledge Book Entry — [Study Guide / Reference Card / Deep Dive]
- **Source Classification:** [Published book / PDF / Course material / Research paper]
- **Confidence Level:** [High / Medium / Low — based on source quality]
- **Template Version:** BVX-LEARN-v1.0
- **Created:** [Date]
- **Last Updated:** [Date]
```

---

## TEMPLATE USAGE NOTES

### Prompt Patterns That Trigger This Template

When you give Claude a book, PDF, or resource, use any of these prompts to invoke this template:

- *"Use the BVX-LEARN template to create a knowledge entry for [book/PDF]"*
- *"Create a strategic learning guide for this book using the standard template"*
- *"Knowledge entry this"*  (shorthand, if template is already established in context)
- *"BVX-LEARN this"*

### Adaptation Rules

**For dense technical books:** Expand Section 3 (Key Concepts) and add code examples or formulas if relevant. Section 4 (Myths) can be converted to "Common Pitfalls."

**For narrative/story-driven books:** Section 2 (Framework) becomes "Narrative Arc & Structure." Section 3 becomes "Key Arguments & Supporting Evidence." Add a "Key Stories/Examples" section.

**For research papers/PDFs:** Compress to Sections 1, 3, 5, and 7 only. Add a "Methodology" section and a "Limitations" section.

**For self-help/personal development:** Expand Section 6 (Implementation Protocol) significantly. This is where the value lives for these books.

**For reference/technical manuals:** Replace the entire structure with a "Quick Reference Card" format — organized by task/problem, not by chapter.

### Quality Checklist

Before finalizing any entry, verify:
- [ ] Thesis is stated in 3 sentences or fewer
- [ ] Framework is visualized (ASCII, table, or diagram)
- [ ] Every concept has a "what to do" component, not just "what to know"
- [ ] Actionable takeaways are specific enough to execute today
- [ ] Cross-references include at least one contrasting/challenging perspective
- [ ] Self-assessment maps to the book's actual content domains
- [ ] Entry works as a standalone reference (doesn't require reading the book)
