---
title: "Opening JSX files"
uuid: 332d3cce-7236-4446-952a-59742d1ac7df
created: 2026-07-15
updated: 2026-07-15
trunk: BOTH
messages: 7
chars: 4898
artifacts: 0
generated_files: 0
tools: [bash_tool, present_files, view]
source: claude.ai-export-2026-08-15
---

# Opening JSX files

> **Conversation Overview**

The person had pre-built JSX quiz files they wanted to open and run, starting with a general question about what program handles JSX files. Claude explained the distinction between editors (VS Code, WebStorm, Sublime Text) and the runtime environment needed to actually execute React code, recommending VS Code for editing and Vite for local development.

When the person clarified they wanted to open and run their quizzes rather than just view them, Claude offered two paths: a no-setup browser-based approach using artifacts or CodeSandbox, or a local Vite development environment. The person then uploaded two JSX files — a couples communication profiler and a relationship needs/attachment-style profiler — both styled with an olive/utility color palette and built using only React's `useState` and `useMemo` hooks with no external dependencies.

Claude used file system tools to inspect, copy, and present both files as runnable artifacts directly in the chat, confirming they were self-contained and required no additional setup. Claude noted that neither file persists data between sessions and that both include an export/summary screen at the end where output should be copied before closing. Claude also offered a follow-up option: packaging either file as a standalone HTML file for hosting or sharing with someone else to complete independently.

---
## 🧑 Papi  <sub>2026-07-15 22:23:57</sub>

what program should i open jsx files in to use

---

## 🤖 Claude  <sub>2026-07-15 22:24:02</sub>

This is a straightforward technical question about which applications can open JSX files.For .jsx files, here are the main options depending on what you're doing:

**Code editors (most common choice):**
- **VS Code** — free, most popular, great JSX/React support out of the box (syntax highlighting, IntelliSense), huge extension ecosystem
- **WebStorm** — paid, very strong JSX/React tooling, heavier IDE experience
- **Sublime Text** — lightweight, fast, needs a package for JSX highlighting

**If you're actually running/building a React project** (not just viewing the file):
- You'll want Node.js installed plus a bundler/dev server — most people scaffold with **Vite** (`npm create vite@latest`) or **Create React App** (older, less recommended now)
- The editor (like VS Code) is where you *write* the JSX; Node/Vite is what actually *runs* it in a browser

**Quick recommendation:** If you just want to open and edit a `.jsx` file right now with good syntax highlighting, VS Code is the easiest free option and works well cross-platform.

If you let me know what you're actually trying to do with the file — just view/edit it, or run a full React project — I can point you to the exact setup.

---

## 🧑 Papi  <sub>2026-07-15 22:24:19</sub>

open and run....i have like these quizzes i made

---

## 🤖 Claude  <sub>2026-07-15 22:24:25</sub>

I'd need to see the actual files to give you exact steps — but here's the general path for opening and running .jsx quiz files:

**Easiest option — no setup, just paste the code:**
If your quizzes are self-contained React components, paste the code into a Claude artifact (or a tool like CodeSandbox / StackBlitz) and it'll run immediately in the browser. This is fastest if you just want to *use* the quizzes right now.

**If you want them running locally on your machine:**
1. Install **Node.js** (if you don't have it)
2. Install **VS Code** to edit the files
3. Scaffold a React project with Vite:
   ```
   npm create vite@latest my-quizzes -- --template react
   cd my-quizzes
   npm install
   ```
4. Drop your `.jsx` files into the `src` folder, import them into `App.jsx`
5. Run it:
   ```
   npm run dev
   ```
   This starts a local dev server (usually `localhost:5173`) where you can actually click through and take the quizzes in a browser.

**Quickest for you right now:** if you upload one of the .jsx quiz files here, I can just read it and either run it directly as an artifact or tell you exactly what's missing to get it running.

Want to upload one?

---

## 🤖 Claude  <sub>2026-07-15 22:26:23</sub>

I should first check what files we're working with before executing anything.
```
This block is not supported on your current device yet.
```

This is a relationship communication tool for adults to explore preferences together—essentially a consensual checklist for discussing boundaries and interests. I'll build an interactive artifact they can use to go through the options and track their selections.
```
This block is not supported on your current device yet.
```

Both files look like self-contained React apps — good news, I can just run them directly as artifacts, no setup needed. They're a kink/limits checklist ("sex menu profiler") and a relationship needs/attachment-style profiler, both styled with that olive/coyote utility-military palette.

Let me get them running for you.
```
This block is not supported on your current device yet.
```

I'm checking the imports in both components—they only use React hooks like useState and useMemo, so no external dependencies to worry about. I'll create these as React artifacts that can render directly.Both are clean, self-contained React components — no external libraries beyond `useState`/`useMemo`, so they'll run immediately. Let me get them into the outputs folder so you can open them as live artifacts.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Both should now open as live artifacts right here in the chat — clickable, interactive, no install needed. Click into either one to run it and click through the quiz.

A couple things worth knowing since these are your two profiler tools:

- **They don't save between sessions** — both have an export/compile step at the end (a "dossier" screen), so make sure to copy that output before closing the artifact tab.
- If you ever want these portable outside Claude (e.g. running locally, or hosted for a partner to fill out remotely), the Vite setup I mentioned earlier would get you there — just drop the file into `src/App.jsx` of a fresh Vite React project.

Want me to package either one as a standalone HTML file you could host or send to someone else to fill out on their own device?