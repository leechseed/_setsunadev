---
title: "Referencing projects in Claude code"
uuid: cc0fdaaf-d894-4706-9462-78fd4582094f
created: 2026-04-18
updated: 2026-04-18
trunk: BLACK
messages: 2
chars: 4145
artifacts: 0
generated_files: 0
tools: [view, web_fetch, web_search]
source: claude.ai-export-2026-08-15
---

# Referencing projects in Claude code

> **Conversation Overview**

The person asked whether a Claude.ai Project could be directly referenced or linked from Claude Code. Claude explained that no direct integration currently exists between Claude.ai Projects and Claude Code, noting there is an open feature request for this capability that has not yet shipped. Claude then outlined a practical workaround: creating a local `CLAUDE.md` file in the working directory and pasting the Project's system prompt into it, since Claude Code reads this file automatically at session start as persistent context.

The conversation revealed the person is working on a markdown-based vault system with a content factory workflow, referred to with terminology like "BVX-LEARN," "one-sheets," "assembly-line," and serial number tracking (e.g., "MSX.01"). Claude explained that Claude Code is actually better suited to this use case than Claude.ai Projects because it can read and write `.md` files directly from disk, eliminating a two-step file output process the person had been using (writing to `/home/claude/` then copying to `/mnt/user-data/outputs/`). Claude also noted that `CLAUDE.md` supports `@path/to/file.md` imports for modular organization of large system prompts.

Claude flagged one limitation: prior conversation history and accumulated session context from the Claude.ai Project would not migrate automatically, and suggested the person either finish relevant threads in the current Project or write a state-of-the-vault note into `CLAUDE.md` to carry forward context. Claude offered to draft a Claude Code-optimized version of the `CLAUDE.md` file incorporating these structural improvements.

---
## 🧑 Papi  <sub>2026-04-18 10:40:35</sub>

Okay. I have Claude code. Would you be able to I'd be able to reference this project from Claude code somehow.

---

## 🤖 Claude  <sub>2026-04-18 10:41:22</sub>

The user is asking whether they can reference a Claude Project from Claude Code, which is a question about how these Anthropic products interact. I should check the documentation to see what the current capabilities are, since this kind of product information can change.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 The user is asking whether they can reference a Claude Project from Claude Code. I'm thinking through the technical differences: Claude Code relies on local CLAUDE.md files for instructions, while Claude.ai Projects store custom instructions and knowledge in Anthropic's web app, and there's no direct integration between them.

The practical workaround would be to copy the system prompt into a CLAUDE.md file or keep the vault files locally so Claude Code can access them directly. I should check the Claude Code documentation to see if there's any project integration feature I'm missing.
```
This block is not supported on your current device yet.
```

 So there's no direct way to reference a Claude.ai Project from Claude Code since they're separate products, though there's a feature request for this. The workaround would be to copy the system prompt into a file within the project folder.

Actually, for this user's setup with a markdown-based vault, Claude Code is the better choice anyway—it can read and write the files directly without needing to re-upload anything, and a CLAUDE.md file with the extraction rules would serve the same purpose as the project's custom instructions. I should focus on giving them the concrete steps to set this up efficiently.Short answer: no direct link exists between Claude.ai Projects and Claude Code — they're separate products, and there's an open feature request for exactly this integration that hasn't shipped yet. But you can replicate the setup locally in minutes, and for your vault use case it's actually a better fit than Projects.

The Claude Code equivalent of a Project's custom instructions is a **`CLAUDE.md`** file that lives in the folder where you run Claude Code. Claude Code reads it at the start of every session and treats it as persistent context — same behavior as the system prompt you have pinned here.

**To port BVX-LEARN over:**

1. In the folder where your vault lives (or a new folder for the factory), create a file called `CLAUDE.md`.
2. Paste the entire system prompt above into it as-is. The format doesn't need to change.
3. Run `claude` in that folder. The instructions load automatically.

**Why this is actually an upgrade for your workflow:**

- Your one-sheets already live as `.md` files. Claude Code can read and write them directly — no more writing to `/home/claude/` then copying to `/mnt/user-data/outputs/`. That whole two-step ritual goes away.
- PDFs can sit in a `sources/` subfolder and get read from disk instead of re-uploaded.
- Serial number tracking gets easier because Claude Code can just `ls` the directory to see what's already taken.
- `CLAUDE.md` supports `@path/to/file.md` imports, so if the system prompt grows, you can split it (e.g., `@templates/one-sheet-template.md`, `@examples/MSX.01.md`) and keep the main file clean.

**One caveat:** the conversation history and prior chats from this Claude.ai Project don't migrate. If you want the assembly-line context (which MSX entries exist, the MSX.01 glossary retrofit state, the Pain Period / Emotional Dumping open question), you'd need to either finish that thread here or dump a brief state-of-the-vault note into `CLAUDE.md` so Claude Code picks up where you left off.

Want me to draft the `CLAUDE.md` version — stripped for Claude Code's context (e.g., swapping the `/home/claude/` → `/mnt/user-data/outputs/` bash dance for direct file writes, adding a line about running `ls` for serial tracking)?