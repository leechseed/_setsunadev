---
original_path: "/home/claude/BVX_LEARN_SETUP_GUIDE.md"
source_conversation: "Creating study guides from books as learning templates"
created: 2026-03-28
trunk: BLACK
kind: generated-file
---

# BVX-LEARN — Project Setup Guide

---

## STEP 1: Create the Project

1. Go to **claude.ai**
2. In the left sidebar, click **Projects** (or the folder icon)
3. Click **"Create Project"**
4. Name it: `🧬 BVX-LEARN — One-Sheet Factory`
5. Hit create

## STEP 2: Add the Custom Instructions

1. Inside your new project, click the **gear icon** or **"Project Settings"**
2. Find the **"Custom Instructions"** field (also called "System Prompt" or "Project Instructions")
3. Open the file `BVX_LEARN_PROJECT_INSTRUCTIONS.md`
4. **Copy the ENTIRE contents** and paste it into the Custom Instructions field
5. Save

That's it. The agent is now loaded.

## STEP 3: Use It

**To process a book (title only — no PDF):**
1. Open your `🧬 BVX-LEARN` project
2. Start a **new conversation**
3. Type: `BVX-LEARN Make It Stick by Brown, Roediger & McDaniel`
4. The agent will research the book and generate a one-sheet
5. The YAML will say `status: draft`

**To process a book (with PDF):**
1. Start a new conversation in the project
2. Upload/attach the PDF
3. Type: `BVX-LEARN this`
4. The agent reads the PDF and generates a one-sheet
5. The YAML will say `status: complete`

**To upgrade a draft to complete:**
1. Open a new conversation
2. Upload the PDF
3. Type: `Upgrade LRN.01`

**To go deeper on a sub-topic:**
1. Type: `Branch LRN.01 on spaced repetition`
2. This creates `LRN.01a` — a focused deep-dive entry

## STEP 4: Export to Obsidian

1. After the agent generates a one-sheet, copy the full markdown output
2. In your Obsidian vault, create a new note
3. Name it using the full ID: `🧬 LRN.01 — Strategic Learning — Kamei (2021)`
4. Paste the markdown content
5. The YAML front matter, wikilinks, and tags will all work natively in Obsidian

**Tip:** If you have a dedicated folder in your vault for these, something like:
```
/Vault
  /🧬 BVX-LEARN
    🧬 LRN.01 — Strategic Learning — Kamei (2021).md
    🧬 LRN.02 — Make It Stick — Brown (2014).md
    🧬 PSY.01 — Mindset — Dweck (2006).md
```

## STEP 5: Track Your Serial Numbers

Keep a simple running list so you know what number you're on in each domain. You can keep this as a pinned note in your vault or just remember. When you start a new conversation in the project, tell the agent: "Next LRN number is 03" or it will ask you.

```
LRN: 01 (Strategic Learning)
PSY: —
SYS: —
BIZ: —
FIT: —
CRE: —
TEC: —
FIN: —
PHI: —
```

## RULES OF THUMB

- **One conversation per book.** Don't stack multiple books in one thread.
- **Title + author is enough.** You don't need the PDF. It just makes the extraction more precise.
- **Draft vs Complete.** Title-only = draft. PDF-sourced = complete. You can upgrade anytime.
- **Branching is optional.** Only branch if you want to go deep on a specific sub-topic from a book.
- **The 🧬 emoji is your brand.** Every one-sheet file starts with it. It's how you spot them in your vault at a glance.
