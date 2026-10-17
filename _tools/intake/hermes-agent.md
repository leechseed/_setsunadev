# Hermes Agent intake (2026-10-17)

Sources: [docs](https://hermes-agent.nousresearch.com/docs) · [repo](https://github.com/NousResearch/hermes-agent) · [features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)

## What it is
Hermes Agent is a self-improving agent from Nous Research, MIT license ([docs](https://hermes-agent.nousresearch.com/docs)). It runs on Nous Portal, OpenRouter, OpenAI, or any custom endpoint ([repo](https://github.com/NousResearch/hermes-agent)). You drive it from a terminal UI or one messaging gateway for Telegram, Discord, Slack, WhatsApp and Signal ([repo](https://github.com/NousResearch/hermes-agent)). Memory is agent-curated, with FTS5 session search and Honcho user modeling ([docs](https://hermes-agent.nousresearch.com/docs)). Skills follow the agentskills.io standard and the agent creates them after complex tasks ([repo](https://github.com/NousResearch/hermes-agent)). It has 60+ tools and MCP support ([docs](https://hermes-agent.nousresearch.com/docs)). Cron takes plain-English jobs and delivers results to any platform ([features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)). Seven terminal backends include local, Docker and SSH ([repo](https://github.com/NousResearch/hermes-agent)).

## What it does that Claude Code here does not
- Phone access. One gateway lets Chief message the agent from Telegram or Signal ([repo](https://github.com/NousResearch/hermes-agent)).
- Voice memo transcription through that gateway ([repo](https://github.com/NousResearch/hermes-agent)).
- Cron built into the agent, with results pushed to a chat ([features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)).
- Any model endpoint, so it can sit on a local model ([repo](https://github.com/NousResearch/hermes-agent)).
- Self-written skills and cross-session recall with no hand-kept notes ([repo](https://github.com/NousResearch/hermes-agent)).
- Checkpoints that roll back file changes with /rollback ([features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)).

## What Claude Code here already covers
- Skills, subagents, hooks and MCP all exist in Hermes too, so they are no gain ([features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)).
- Hermes reads CLAUDE.md and AGENTS.md as context files, so the doctrine carries over ([features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)).
- Memory, STATE.md, the digest and the Oscar Mike notes do the job of its learning loop by hand.
- Task Scheduler already runs the detached pipelines.
- JUDY already handles local voice.

## Fit for the Command
- Slot in: an always-on agent on the 3090 box, reached from the phone, running cron checks on the pipelines. Nothing in the docs I read says it works with Ollama, so test that first (unverified).
- Slot in: a pager. It would watch a detached run and message Chief when it stalls.
- Duplicate: skills, subagents and hooks. A second skill store would drift from `.claude/skills/`.
- Conflict: its self-written memory and skills would fight the SOP, where Chief rules what is canon.
- Conflict: it would need its own approval guard. The no-probe hook does not cover it.

## Risks
- Maturity: the repo shows about 254k stars and 55k commits ([repo](https://github.com/NousResearch/hermes-agent)). That is popular and fast-moving. I did not check release stability.
- Security: it has shell access and a chat gateway. A stranger's message or a leaked token could reach the box. The docs cover command approval, DM pairing and container isolation ([repo](https://github.com/NousResearch/hermes-agent)).
- Windows: native PowerShell install works without WSL. Defender or Bitdefender may flag the bundled uv.exe ([repo](https://github.com/NousResearch/hermes-agent)).
- Install: the PowerShell installer is a pipe-to-iex script. Read it first ([repo](https://github.com/NousResearch/hermes-agent)).
- Cost: the software is free. Cloud models cost money. A small local model may call tools badly (unverified; the docs list no caveat).
- Maintenance: one more agent to patch, and a second set of secrets.

## Verdict: TRIAL (sandboxed, one named job)
Trial it as a pager. Run it in Docker or on a spare profile with no repo write access, on a local model. Its one job is to watch a detached pipeline log and message Chief's phone when it stalls. Skip everything else.
