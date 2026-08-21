# OSCAR MIKE

Staging area. You're moving on to the next thing — park this here first.

## The verbs

**`Oscar Mike`** — park the current work here and move on. No cataloging, no filing,
no decisions. Capture is cheap.

**`sweep`** — walk what's parked, promote what earned it into the indexed system
(`STATE.md`, `PROJECTS.md`, the build dirs), delete the rest. Back to empty.

The whole point: **capture is cheap, cataloging is expensive.** Don't pay the second
cost until you know the thing survived contact.

## Rules

1. Everything gets frontmatter, so grep works.
2. Nothing here is permanent. If it matters, sweep it out.

## Frontmatter

```yaml
---
parked: YYYY-MM-DD
title: Human Readable Name
handle: kebab-case-shorthand    # what you say to pull it up
tags: [topic, topic]
status: active | parked | ready-to-sweep
open-decision: "the one thing still unresolved, if any"
---
```

## Search

PowerShell:
```powershell
Select-String -Path ".\oscar-mike\*.md" -Pattern "term"
Select-String -Path ".\oscar-mike\*.md" -Pattern "^tags:.*furniture"
```

Bash:
```bash
grep -rin "term" oscar-mike/
grep -rl "tags:.*furniture" oscar-mike/
```
