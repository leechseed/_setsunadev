# .claude

Three terms, in our words:

- **Agent**: a specialist the CDR calls for one job on inputs it is handed; it reports and the CDR rules ([agents/README.md](agents/README.md)).
- **Skill**: a written procedure that runs when Chief says its proword ([skills/README.md](skills/README.md)).
- **Hook**: a script the harness runs on an event, with no model in the loop ([../_tools/hooks/README.md](../_tools/hooks/README.md)).

## The folder

| Path | What it holds |
|---|---|
| [agents/](agents/README.md) | the Roster (BOLO 139): one file per specialist, plus `references/` (plan template, security checklist) |
| [skills/](skills/README.md) | one folder per skill, `SKILL.md` plus optional `references/` |
| rules/ | standing rules loaded with the session |
| workflows/ | multi-step workflow scripts |
| settings.json | shared settings |
| settings.local.json | this machine's hooks and permissions (Chief edits; the proposed portable block is in [../_tools/hooks/settings.proposed.json](../_tools/hooks/settings.proposed.json)) |

Start at [../CLAUDE.md](../CLAUDE.md), then [../SOP.md](../SOP.md) section 1.
