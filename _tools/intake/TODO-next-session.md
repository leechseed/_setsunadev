# THE INTAKE QUEUE · for the next session (Fable) · BOLO 140

Spoken by Chief 10/12 ~11:15 PM, then "how copy": compile only, no analysis this session; the next session (on Fable) runs the research.

**Already done (zero tokens):** `_tools/intake/repo_scan.py` scanned all 11 repos below. Each has `_PRIVATE/intake-repos/<owner>__<repo>/scan.json` (license, stars, last push, file tree, part counts) and `README.md`. Start from those; don't re-scan.

**How to run it:** the `intake` skill (`.claude/skills/intake/SKILL.md`) for the repos: one MS per repo in parallel, `picks.json` each, the Keep/Skip glass. The articles go to one MS each with a "what do we change because of this" brief. Every deliverable lands as a glass. Never run a repo's installer, hooks or plugin.

**Scan flags to respect:** no license stated on **anthropics/skills** and **BehiSecc/awesome-claude-skills**, and "NOASSERTION" on **awesome-claude-code**: read the license terms before copying anything. **Mudlet** is GPL-3.0: ideas only, no code into our repo. **ruflo** is huge (7,794 files, 817 hook files, 57 installers): design inspiration only.

## The list (Chief's asks, in his words where it matters)

| # | Link | Chief's ask | Deliverable |
|---|---|---|---|
| 1 | https://github.com/ruvnet/ruflo (MIT · ★74K) | "I really like the animated desktop or like workflow slash desktop slash front page ... inspired by this, let's make our own stuff." | A design for our own animated Command front page (workflow / desktop view), glassed as a working mock |
| 2 | https://github.com/Mudlet/Mudlet (GPL-3.0) | "Designing a MUD around creating a character": LLM + agents, a separate environment from the chat; a conversation / questionnaire inside the MUD that outputs everything the LEECHSEED character system needs, and can edit it after. | A concept + build path for a character-creation MUD wired to LEECHSEED (input: questionnaire, output: the character tree/data), with what Mudlet gives us vs building our own |
| 3 | https://github.com/thedotmack/claude-mem (Apache-2.0 · ★100K · 25 hook files) | "How useful would this be? ... persistent context." | A verdict vs what we already run (`_CACHE` notes, STATE, the memory directory, the SessionStart digest): adopt / borrow / skip, with the token and hook cost |
| 4 | https://github.com/hesreallyhim/awesome-claude-code | "Really go through this page ... take all the coolest stuff and then a glass page for your suggestions ... on the features that we could build with this." | A glass of the coolest items + feature suggestions, each with a rec and Keep/Skip |
| 5 | https://github.com/LukeRenton/explore-claude-code (MIT) | "I really do like how clean the folder trees [are] ... our folders are thick everywhere. Is there any way we can make it clean like this ... less crazy sprawling? ... we have a bunch of ingested notes ... what are the steps?" | A target folder tree for the repo + a staged cleanup plan (what moves, what archives, what the renumber script must update), nothing moved until ruled |
| 6 | https://github.com/anthropics/skills (no license stated · ★181K) | "Really go through this one ... create an agent or an agent with subagents to create really robust agents, skills, processes, workflows ... to really start optimizing all of our stuff ... we do have a lot of bloat." | A design for a "builder" agent (with subagents) that writes and refactors our agents/skills/workflows to Anthropic's patterns, + a bloat-cut list for our current skills |
| 7 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | "Context ... was super important for us." (Chief pasted this link twice; he meant a second Anthropic article too, see #8 and #9.) | What we change in the Command because of it (session open, digests, notes, agent briefs) |
| 8 | https://www.anthropic.com/engineering/multi-agent-research-system | "Specifically, here's a research system." | What we change in our formation / research loop (BOLO 108) because of it |
| 9 | https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more | "An agent that ... first tries to understand what I'm trying to say for Claude": an intent parser in front of the work. | A design for the intent-parser agent (Chief's dictation → a clean order for the CDR), using the steering article |
| 10 | https://github.com/ThibautMelen/agentic-ai-systems (MIT) · https://aipatternbook.com/ | "More on agentic AI." | The patterns worth adopting, mapped onto our formation |
| 11 | https://github.com/hluaguo/learn-faster-kit (MIT · 4 agents, 14 commands) | "Take close attention to this one ... helping me learn ... these complex systems better. I know we tried to do it before ... we need agents specifically made for that instead of having to code it up every time." | Learning agents for the Roster, built on the teach-back loop (BOLO 95) and this kit |
| 12 | https://github.com/BehiSecc/awesome-claude-skills (no license stated) | "More Claude skills we can consider and turn into agents." | Picks into the same Keep/Skip glass as #4 |
| 13 | https://claudefa.st/blog/tools/mcp-extensions/best-addons | "MCP stuff ... help me understand it and get us on the right page." | A plain MCP guide for Chief + the 3–5 servers worth adding, each with its cost and risk |
| 14 | https://github.com/Leonxlnx/taste-skill (MIT · ★95K · 13 skills) | "Integrating taste ... not just in the visual creation, but like the word creation and the prose ... what we can take, and what systems we can build." | A taste system for glass pages AND prose (BOLO 95 doc SOP, the writing guide), what to copy, what to build |
| 15 | https://github.com/HKUDS/ClawTeam (MIT · last push 5/9 · Python) | "Explain to me what is this Claw team and what we can do to enable it." | A plain explainer + whether and how to run it here |

## Suggested order (a pick, not a ruling)

1. **Context and agents first** (#7, #8, #9, #6, #10, #3, #13, #15): they shape how everything else gets built.
2. **The catalogs** (#4, #12) into one Keep/Skip glass.
3. **Learning** (#11) and **taste** (#14): new Roster agents.
4. **The builds** (#1 front page, #2 the MUD, #5 the folder cleanup): each a glass mock or plan first.
