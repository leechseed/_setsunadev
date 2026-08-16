---
title: "Automating PDF processing with Claude API"
uuid: 1c0f91a5-ef6c-4aa6-a91b-c631f03baf50
created: 2026-04-04
updated: 2026-04-04
trunk: BLACK
messages: 4
chars: 4188
artifacts: 0
generated_files: 0
tools: [ask_user_input_v0]
source: claude.ai-export-2026-08-15
---

# Automating PDF processing with Claude API

> **Conversation Overview**

The person is working on a project called BVX-LEARN and wants to automate the processing of PDF books into structured markdown output using Claude. The conversation began with Claude presenting three automation routes: an n8n/Make.com workflow, a Claude Code CLI script, and a raw Python script using the Anthropic API. All three approaches would use the BVX-LEARN system prompt to process PDFs and output formatted markdown files.

When asked which route to pursue, the person indicated they weren't sure what their account supported, revealing they did not yet have a separate Anthropic API key. Claude clarified that all three automation options require a paid API key distinct from a Claude.ai subscription, and proposed an alternative: a browser-based artifact that works within Claude.ai with no API key or setup required. This would allow the person to paste or upload text and receive BVX-LEARN-formatted markdown immediately, with the option to later migrate to a Python batch script once they have API access.

The person also confirmed they have not yet written the BVX-LEARN system prompt and need to build it from scratch. At the end of the conversation, Claude asked two follow-up questions to determine whether to build the browser artifact or the Python script, and what output format the BVX-LEARN system should produce—Zettelkasten atomic notes, a single structured one-sheet per book, or both. The person had not yet responded to these questions.

---
## 🧑 Papi  <sub>2026-04-04 07:22:31</sub>

Help me do this Yeah, absolutely. A few routes:
n8n or Make.com — Set up a workflow: watch a folder (Google Drive, Dropbox) → when a PDF lands, send it to the Claude API with your BVX-LEARN system prompt baked in → receive the markdown back → save it to an output folder. n8n has an Anthropic node. The main constraint is PDF size — you’d need to extract text from the PDF first (via a PDF-to-text node) before sending it to Claude, since the API has token limits.
Claude Code (CLI) — This is probably your cleanest option. Write a simple script that loops through a folder of PDFs, feeds each one to Claude with your system prompt, and writes the .md files out. You’d run it from your terminal. One command, walk away, come back to a folder full of one-sheets.
Custom Python script + Anthropic API — Same idea as Claude Code but you control everything. A few dozen lines: read PDF with pymupdf, chunk it if needed, send to claude-sonnet-4-6 with your system prompt, write the output. Most flexible, most control over error handling and retry logic.
The system prompt would just be your BVX-LEARN instructions from this project, copy-pasted in.
Want me to build you one of these? If so, which route — n8n workflow, Claude Code script, or raw Python?

---

## 🤖 Claude  <sub>2026-04-04 07:22:37</sub>

The user wants me to build one of the three options for automating BVX-LEARN book extraction. They haven't chosen yet - I should ask which route they want.
```
This block is not supported on your current device yet.
```

Waiting for user response.

---

## 🧑 Papi  <sub>2026-04-04 07:23:01</sub>

Q: Which route do you want to build?
A: Which one can I do with my account 

Q: Do you already have your BVX-LEARN system prompt written out, or do we need to build that too?
A: Need to build it

---

## 🤖 Claude  <sub>2026-04-04 07:23:19</sub>

The user wants to know which option they can do with their current setup. Let me think about this:

1. n8n/Make.com - requires a separate account/service, n8n can be self-hosted or cloud
2. Claude Code CLI - requires Claude Pro or API access, it's a CLI tool
3. Raw Python + Anthropic API - requires an Anthropic API key (paid, separate from Claude.ai subscription)

The user is talking to me on Claude.ai. The key question is whether they have an Anthropic API key. Claude Code also requires API access.


Actually, all three options need an Anthropic API key since that's separate from a Claude.ai subscription. The Python script is probably the simplest approach, but they'd still need that API access. There's also a fourth option I'm realizing—they could upload PDFs directly to a Claude project and use a system prompt there, though that wouldn't be automated. Looking at what they actually have access to, they're on Claude.ai and likely have Pro, but that doesn't automatically give them API access. Everything else requires either an API key or a separate service account.

Wait, I could actually build them an artifact right here that uses the Anthropic API through my own capabilities—they'd upload PDFs directly in the browser and get back BVX-LEARN formatted markdown without needing their own API key or any setup. That's the cleanest solution. I should suggest this approach and ask if they have an API key separately, just in case they want to explore the other options too.Honest answer: all three of those options require a **paid Anthropic API key** (separate from your Claude.ai subscription). Without one, none of them run on their own.

**But here's what I can do right now with your account:**

I can build you an **AI-powered artifact** — runs right here in the browser, no API key needed, no setup. You drag-and-drop a PDF (or paste text), it processes it through your BVX-LEARN system prompt, and spits out formatted markdown you can copy into Obsidian. It's not fully automated (you still click a button per book), but it's zero setup and works today.

If you later get an API key, we can port the same system prompt into a Python batch script and make it fully hands-off.

Two questions before I build either:
```
This block is not supported on your current device yet.
```