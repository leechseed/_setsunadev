---
title: "VSCode profiles for reading, AI data generation, and revision"
uuid: 729e6f78-b2d0-4e19-9f13-ddb6c4331392
created: 2026-02-19
updated: 2026-02-19
trunk: BLACK
messages: 16
chars: 15255
artifacts: 0
generated_files: 0
tools: [Claude in Chrome:update_plan]
source: claude.ai-export-2026-08-15
---

# VSCode profiles for reading, AI data generation, and revision

> **Conversation Overview**

The user sought help setting up three distinct VSCode profiles for different workflows: a "Read" profile for browsing and copying information with file explorer and markdown preview in a read-only environment, a "Data Gen/AI" profile with a complex three-column layout (file explorer left, split editors center for reference and scratch buffer, dual terminals right for agentic AI and Claude), and a "Revision" profile for cleanup and structuring with a similar layout but Claude-only terminal. The user demonstrated familiarity with technical terminology, referencing Emacs scratch buffers and seeking the VSCode equivalent for temporary editing spaces.

Claude clarified that VSCode profiles control UI behavior and tool configuration while workspaces manage file/folder access, and that both can work together. A key technical issue emerged where VSCode prevents opening the same folder in multiple profile windows simultaneously, collapsing back to the original window. The solution involved switching profiles within the same window rather than opening new windows. The user initially couldn't locate the profile switching UI due to their customized layout hiding the activity bar, so Claude provided the command palette approach and suggested custom keybindings for profile switching.

The conversation concluded with the user asking about window layout persistence across profile switches. Claude explained that VSCode reliably restores the last window state on startup but may not preserve complex editor group layouts when switching profiles frequently, though suggested testing the behavior before implementing more complex layout restoration solutions.

---
## 🧑 Papi  <sub>2026-02-19 00:19:49</sub>

in vscode....ok so help me setup profiles. each profile should be per action. one for reading - basically a file explorer on the left and an editor with markdown previewer enabled. here i'll browse and copy paste certain info but either thru just some sort of clever shit or just by memory i don't want to be able to move anything just reading. i need one for data generation/ai. (window will consist of left file browser explorer, center column split into two rows. top will be where i ref and browse files. the bottom editor will be an editor open to a 'scratch' pastebin ((theres a technical name for this is it like a temp layer? i think the term im looking for is from ermacs?)) this is where i basically do any prep for prompting the ai agent who access to data. and browsing. the right column will be two terminal windows stacked like the editors. the top will be my agentic ai, the bottom will be claude or just the agentic ai as one window in the right column. .) the third profile will be for revision, organization, and clean up. This window will primarily be used for structuring the data with AI. same basic format as the previous but only with claude.

---

## 🤖 Claude  <sub>2026-02-19 00:20:37</sub>

The term you're thinking of from Emacs is a **scratch buffer** — a temporary, unsaved editing space. VSCode's equivalent is an **Untitled** editor, but you can get true scratch buffer behavior with the **Scratchpad** extension or just using `workbench.action.files.newUntitledFile`.

Let me help you set up these three profiles. Here's the plan:

**Profile 1: Read** — File explorer + editor with markdown preview, read-only feel
**Profile 2: Data Gen / AI** — Explorer | split editor (ref top, scratch bottom) | split terminals (agent top, Claude bottom)
**Profile 3: Revision / Structure** — Same layout but stripped down, Claude only
```
This block is not supported on your current device yet.
```

I'll walk you through this manually since VSCode profiles are best set up through the UI + settings files. Here's the full breakdown:

---

## Setting Up the Three Profiles

Go to **File → Preferences → Profiles → Create Profile** (or the profile icon bottom-left in the activity bar).

---

### Profile 1: "Read"

**Create profile named `Read`**

In its settings (`Ctrl+Shift+P` → "Open Profile Settings (JSON)"):

```json
{
  "workbench.activityBar.location": "hidden",
  "workbench.statusBar.visible": false,
  "editor.readOnly": false,
  "files.readonlyInclude": {},
  "workbench.panel.defaultLocation": "bottom",
  "editor.minimap.enabled": false,
  "editor.wordWrap": "on",
  "markdown.preview.openMarkdownLinks": "inEditor",
  "workbench.editor.openSideBySideDirection": "right",
  
  // Disable anything you don't need
  "workbench.tree.enableStickyScroll": false,
  "editor.renderLineHighlight": "none",
  "editor.lineNumbers": "off",
  "editor.scrollBeyondLastLine": false
}
```

**For the soft read-only feel** — install the extension **"Read Only Indicator"** or use a workspace-level `files.readonlyInclude` glob. The cleanest approach: bind a keybinding to toggle read-only on the active file. Or, point this profile at folders by convention and use:

```json
"files.readonlyInclude": {
  "**/your-source-folder/**": true
}
```

**Layout:** Open Explorer (`Ctrl+Shift+E`), open a file, then `Ctrl+Shift+V` for Markdown preview side-by-side. Save this as your window state — VSCode remembers it per profile.

---

### Profile 2: "Data Gen"

**Create profile named `Data Gen`**

Settings:

```json
{
  "workbench.activityBar.location": "default",
  "terminal.integrated.splitTerminal": true,
  "editor.wordWrap": "on",
  "workbench.editor.showTabs": "multiple"
}
```

**Layout sequence to get your 3-column setup:**

1. Open Explorer sidebar (left column ✓)
2. Open your reference file in the main editor
3. `Ctrl+\` to split editor right → this gives you the right editor column
4. In the **left editor group**: `Ctrl+K Ctrl+\` to split it horizontally (top = ref, bottom = scratch)
   - Top: open your reference doc
   - Bottom: `Ctrl+Shift+P` → **"New Untitled File"** → this is your scratch buffer
5. Open terminal (`Ctrl+\`` `) → then split it (`Ctrl+Shift+5` or the split button) to get two stacked terminals
   - Top terminal: your agentic AI (e.g., Claude Code, Cursor agent, etc.)
   - Bottom terminal: Claude CLI or secondary agent

**For the scratch buffer specifically** — the Untitled file is fine, but if you want persistence across sessions, install **"Scratchpad"** extension which gives you a persistent scratch file per workspace.

**Drag the terminal panel** to the right editor group to dock it there — right-click the terminal tab → "Move Terminal into Editor Area" then drag it to the right column.

---

### Profile 3: "Revision"

**Create profile named `Revision`**

Same layout as Data Gen but:
- Right column: single terminal (Claude only)
- Consider installing **"Todo Tree"** or **"Markdown All in One"** here since this is your cleanup/structure profile
- Disable the agentic AI extensions in this profile (VSCode profiles let you enable/disable extensions per profile — go to Extensions panel → right-click any extension → "Disable (Profile)")

Settings:
```json
{
  "editor.formatOnSave": true,
  "editor.wordWrap": "on",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 5000,
  "workbench.editor.showTabs": "multiple"
}
```

---

## Key Tips

**Saving layouts:** VSCode doesn't have a native "save layout" button, but once you set up a profile's window arrangement, it remembers the panel/editor group layout per profile automatically as long as you don't close the window erratically. You can also use **"Workbench: Save Editor Layout"** from the command palette.

**Switching profiles:** Click your profile name in the bottom-left gear area, or `Ctrl+Shift+P` → "Switch Profile". You can also assign keyboard shortcuts to profile switches.

**The scratch buffer:** The Untitled file approach works but won't survive a crash. The better Emacs-equivalent is to create a file called `scratch.md` in a hidden dot-folder (`~/.vscode-scratch/scratch.md`) and pin it to that editor slot. Then it's persistent, searchable, and you can git-ignore it.

Want me to generate the actual full `settings.json` and `keybindings.json` for each profile as files you can drop in directly?

---

## 🧑 Papi  <sub>2026-02-19 00:42:30</sub>

there isn't an open profile settings in the command thing only open user settings

---

## 🤖 Claude  <sub>2026-02-19 00:42:40</sub>

Yeah, VSCode's profile-specific settings aren't exposed as a direct JSON command the same way user settings are. Here's how to actually get to per-profile settings:

**The real way to edit profile settings:**

1. First **switch into the profile** you want to edit (bottom-left corner → your profile name → switch)
2. Then `Ctrl+Shift+P` → **"Open User Settings (JSON)"**

When you're inside a profile, "User Settings" *is* that profile's settings. The profile system essentially creates a scoped copy of user settings per profile. So whatever you set there only applies to that profile.

**To create a new profile:**

`Ctrl+Shift+P` → **"New Window with Profile"** or go to **File → Preferences → Profiles → Create Profile**

Or the quickest way — click the **gear icon** (bottom left) → **Profiles** → **Create Profile**. You can create it from scratch or copy your current settings as a starting point.

Once you're in the new profile's window, then open User Settings JSON and paste in the config for that profile.

**One thing to know:** extensions are also profile-scoped. When you create a new profile from scratch it starts with zero extensions, so you'll need to re-enable or install the ones you want for each profile. If you create from a copy of an existing profile it inherits everything.

Want to start with one of the three and I'll give you just the settings JSON to paste in?

---

## 🧑 Papi  <sub>2026-02-19 00:48:26</sub>

OK SO WHATS the difference between workspaces and profiles?

---

## 🤖 Claude  <sub>2026-02-19 00:48:38</sub>

Good question — they solve different problems and are meant to be used together.

**Profiles** are about *how VSCode looks and behaves* — your extensions, settings, keybindings, snippets, UI layout. Think of it as "what kind of work am I doing?" A profile travels with you regardless of what folder you have open. Your Read profile, Data Gen profile, Revision profile — those are profiles. You switch profiles and VSCode transforms its whole personality.

**Workspaces** are about *what files/folders you're looking at* — they're essentially a saved pointer to one or more root folders, plus any folder-specific settings. A workspace answers "what project am I in?" You can have a workspace for your SlimeVR project, one for the Florida retreat research, one for random scratch work, etc. Workspace settings override user/profile settings, so you can tune things per project on top of whatever profile you're running.

The way they interact: you can open a workspace *while in* any profile. So you might open your SlimeVR workspace in the Data Gen profile when you're doing AI work on it, then switch to the Revision profile later while keeping the same workspace open. The workspace stays, the profile swaps around it.

The practical upshot for what you're building — your three profiles define the *layouts and tools*, and if you want to you can create workspaces per project (SlimeVR, retreat, etc.) that just remember which folders to open. But honestly for your use case the profiles alone might be enough. Workspaces become most valuable when you have multi-root folder setups or project-specific extension/setting overrides.

---

## 🧑 Papi  <sub>2026-02-19 00:50:09</sub>

ok but im trying to access the same folder just with different ui front ends. and those front ends are profiles. but when i try to open up the same folder in a different profile it shits itself and sends me back to the original vscode window and closes the new one

---

## 🤖 Claude  <sub>2026-02-19 00:50:19</sub>

Yeah that's a known VSCode annoyance. A folder can only be "owned" by one window at a time — when you try to open the same folder in a second profile window, VSCode goes "nope, already got that" and collapses back to the existing window.

**The workarounds:**

**Option 1: Switch profile without reopening the folder**
Don't open the folder in the new profile — instead, while you're already in that folder's window, switch the profile on it directly. Bottom-left gear → Profiles → switch to whichever profile. The folder stays open, the profile swaps around it. This is probably the cleanest solution for your use case.

**Option 2: Use a Workspace file instead of opening the folder directly**
Create a `.code-workspace` file that points to your folder. You can have multiple `.code-workspace` files all pointing to the same underlying folder, and open each one in a different profile window. VSCode treats them as distinct "things" so it won't collapse them. Each workspace file can also carry its own settings on top of the profile.

**Option 3: `--new-window` flag**
From the terminal: `code --profile "Data Gen" --new-window /your/folder` — forces a new window. Hit or miss depending on your VSCode version.

For what you're doing, **Option 1 is probably the move** — you're not really running two profiles simultaneously, you're switching modes on the same folder. Profile switching is near-instant, so treating it like flipping between "modes" rather than separate windows is the intended workflow.

---

## 🧑 Papi  <sub>2026-02-19 00:50:55</sub>

ok so there isn't a botom left gear when i have the windows set up the way i want

---

## 🤖 Claude  <sub>2026-02-19 00:51:02</sub>

Right, because you've probably hidden the activity bar or status bar in your layout. A few ways to switch profiles without needing that gear:

**Easiest:** `Ctrl+Shift+P` → type "Switch Profile" → pick the one you want. That always works regardless of your UI setup.

**Or set a keybinding** — open `keybindings.json` and bind profile switching directly:

```json
[
  {
    "key": "ctrl+alt+1",
    "command": "workbench.action.openWindow",
    "args": { "profileName": "Read" }
  },
  {
    "key": "ctrl+alt+2", 
    "command": "workbench.action.openWindow",
    "args": { "profileName": "Data Gen" }
  },
  {
    "key": "ctrl+alt+3",
    "command": "workbench.action.openWindow",
    "args": { "profileName": "Revision" }
  }
]
```

Actually the more correct command for switching (not opening a new window) is `workbench.profiles.switchProfile` — try that in the command palette first to confirm it exists in your version, then bind it.

That way you never need the UI chrome to switch modes, just a hotkey. What version of VSCode are you on? The profile commands vary a bit between versions.

---

## 🧑 Papi  <sub>2026-02-19 00:51:23</sub>

oh i see perfect.

---

## 🤖 Claude  <sub>2026-02-19 00:51:27</sub>

Nice, yeah once you have hotkeys for it the whole thing clicks — it's basically just mode-switching on the same folder. 

Go ahead and get your three profiles created and the layouts how you want them, then set those keybindings and you're good. What do you want to tackle next — finishing the layouts, or something else?

---

## 🧑 Papi  <sub>2026-02-19 00:52:27</sub>

will the window layout stay the same

---

## 🤖 Claude  <sub>2026-02-19 00:52:35</sub>

Unfortunately no — VSCode doesn't reliably save and restore editor group layouts per profile. It'll remember some things but the specific split arrangement (your 3-column setup with stacked editors and terminals) will likely not survive switching back and forth.

The way people solve this is with an extension called **"Restore Terminals"** for the terminal side, and for editor layouts there's **"workbench.action.editorLayoutThreColumns"** type commands you can chain together in a task.

But honestly the cleanest solution is to make a **shell script or task per profile** that rebuilds the layout when you switch into it. VSCode has a command called `workbench.action.editorLayout` that accepts a JSON layout definition — you can script the whole thing.

Want me to write those layout-restore scripts for each of your three profiles? You'd just run it once after switching and it snaps everything back into place. Or if you want it fully automatic, we can hook it to a profile-switch trigger.

---

## 🧑 Papi  <sub>2026-02-19 00:52:59</sub>

well howcome vscode opens up with my windows set up the last time i opened it

---

## 🤖 Claude  <sub>2026-02-19 00:53:04</sub>

Because it remembers the last state of each *window* — but when you switch profiles on that same window, it's still the same window so it does preserve it somewhat. The issue would really only show up if you're switching profiles frequently and the layout drifts.

So honestly you might be fine — just set up each profile's layout once, switch away, switch back and see if it holds. VSCode's session restore is pretty solid for editor groups and terminals as long as you're not explicitly closing things.

Try it and see before we over-engineer a solution for a problem you might not actually have.