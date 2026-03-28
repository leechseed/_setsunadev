
# BVX-LEARN TEMPLATE v2

## One-Sheet Knowledge Entry Generator

---

> **What this is:** A template for turning any book, PDF, or learning resource into a single-page reference card. Feed Claude a book and say: **"BVX-LEARN this."**
> 
> **Design philosophy:** Extract the invariants (what's always true), the heuristics (decision rules), and the core concepts (the actual mechanics). Kill everything else. If it's not actionable or foundational, it doesn't make the sheet.

---

## TEMPLATE

```markdown
# [BOOK TITLE] — [Author] ([Year])
### One-Sheet Knowledge Entry | BVX-LEARN v2

---

## CORE THESIS (1 sentence)
[The entire book compressed into one sentence. What is the single 
argument the author is making? If someone only reads this line, 
what should they walk away with?]

---

## INVARIANTS
*These are the unchanging principles — true regardless of context.*

[3-8 numbered items. Each one is a principle that:
- Remains true across situations, subjects, or time periods
- Can't be "hacked around" — it's a hard constraint
- Is supported by evidence or deep logical necessity
- Format: **Bold claim.** 1-2 sentence explanation.]

1. **[Principle name.]** [Why it's always true and what it means.]
2. **[Principle name.]** [Why it's always true and what it means.]
...

---

## HEURISTICS
*Rules of thumb for real-time decision-making.*

| Situation | Do This | Not This |
|-----------|---------|----------|
| [Context] | [Correct action] | [Common wrong action] |
| [Context] | [Correct action] | [Common wrong action] |
...

[Aim for 6-10 rows. Each row is a decision point the reader 
will actually encounter. Left column = the trigger situation. 
Middle = what the book says to do. Right = what most people 
do instead (the mistake).]

---

## CORE CONCEPTS ([N])
*The essential theories, solutions, and mechanics.*

[3-8 concepts. Each one gets:]

**1. [Concept Name]**
[2-4 sentences max. What it is, how it works, why it matters. 
No fluff. If you can't explain it in 4 sentences, you don't 
understand it well enough yet.]

**2. [Concept Name]**
[2-4 sentences.]

...

---

## WHAT DOESN'T WORK (kill list)
[Single line. Comma-separated list of approaches, beliefs, or 
methods the book debunks or argues against. Quick-scan format.]

---

## QUICK SELF-CHECK (yes/no)
[6-10 checkbox items. Binary — you're either doing this or 
you're not. Ordered by priority (first item = most important). 
If a box is unchecked, that's the reader's next action.]

- [ ] [Am I doing X?]
- [ ] [Am I doing Y?]
...

*If any box is unchecked, that's your next priority — in the order listed.*

---

`BVX-LEARN v2 | [Date] | Source: [Type]`
```

---

## EXTRACTION RULES FOR CLAUDE

When processing a book/PDF with this template, follow these rules:

### Finding Invariants

Ask: "What claims in this book would remain true in any context?" These are the physics of the domain — the constraints you can't cheat. If it's situational advice, it's a heuristic, not an invariant.

### Finding Heuristics

Ask: "What decision rules does this book give for real-time situations?" Format as if-then: "When you encounter [X], do [Y] instead of [Z]." The "Not This" column is critical — it shows the common wrong path.

### Finding Core Concepts

Ask: "If I had to teach this book in 15 minutes, what are the mechanisms I'd need to explain?" Strip away stories, examples, historical context. What are the gears that make the system work?

### The Kill List

Ask: "What does this book say to stop doing?" Most useful books are as much about what NOT to do as what to do.

### The Self-Check

Ask: "What would a person who fully implemented this book be doing daily/weekly?" Turn those behaviors into yes/no checkboxes.

---

## PROMPT SHORTCUTS

- **"BVX-LEARN this"** → Generate one-sheet from book/PDF in context
- **"BVX-LEARN [book title]"** → Research the book and generate one-sheet
- **"BVX-LEARN this, heavy on heuristics"** → Expand the heuristics table
- **"BVX-LEARN this, heavy on invariants"** → Expand the invariants section