# The Command — read this, then SOP §1

This repo is the operating record of one person's operation ("the Command"). The doctrine lives in [SOP.md](SOP.md); the live index is [STATE.md](STATE.md); the watchlist is [BOLO.md](BOLO.md). Open them on demand only: the SessionStart hook prints a digest that replaces reading them.

**The four steps (BOLO 64, ruled 2026-09-23):** every procedure runs RECON (zero-token prep, read before write) · ORDER (the brief or the DOPE SHEET; "go" is the order, not the build-out) · EXECUTE (the formation: specialists on disjoint inputs, one script reviewer at the fan-in) · CONSOLIDATE (build, flush, publish, autocommit, Oscar Mike). Named, not gated.

**Skills** (`.claude/skills/`): `sitrep` · `oscar-mike` · `dope-sheet` · `frago` · `collect` · `rtb` · `launch`. Say the proword; the skill is the procedure. Format rules for every reply: SOP §7.

**Hooks** (`.claude/settings.local.json`): SessionStart → the digest · Stop → local autocommit (never pushes) · PreToolUse → the no-probing guard (`_tools/hooks/no_probe.py`).

**Two standing rules that bite:** never scan the box (processes, logs, network, configs) unless the order names it; launch stations from the Bash tool, never PowerShell. The rest is in SOP.
