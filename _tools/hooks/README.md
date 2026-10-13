# Hooks

A hook is a script the harness runs on an event, with no model in the loop. Five are wired in [.claude/settings.local.json](../../.claude/settings.local.json). A proposed portable version of the block is in [settings.proposed.json](settings.proposed.json) (Chief pastes it; nothing here edits settings).

| File | Event | What it does | Fires on |
|---|---|---|---|
| [../autocommit.sh](../autocommit.sh) | Stop | Commits the working tree locally; never pushes | every time Claude finishes a turn |
| [../sitrep/digest.py](../sitrep/digest.py) | SessionStart | Prints the ~40-line session-open digest in place of reading STATE, SOP and BOLO | `startup`, `resume`, `clear` |
| [no_probe.py](no_probe.py) | PreToolUse | The no-probing guard: blocks scan-shaped shell commands (processes, network, logs, registry) unless Chief named the box; exit 2 blocks | every Bash or PowerShell call |
| [order_hint.py](order_hint.py) | UserPromptSubmit | Prints one ORDER HINT line when the prompt holds a proword scoring 0.9 or more; never rewrites or blocks | every prompt |
| [precompact_backup.py](precompact_backup.py) | PreCompact | Copies the transcript to `_LOG/transcripts/` and notes it in the newest `_CACHE` note | before any compact |

Only no_probe.py can block. To name the box for 60 minutes: `python _tools/hooks/no_probe.py --box-named`.
