# \_setsunadev

**CHEF ZAKUZOKU / U01_LEECHSEED / ggrimace**  
_Narrative engineering for the systematically creative_

A personal monorepo: story theory, tools, and the operating record of one person's operation ("the Command"). Mostly .MD files and vibed Python scripts. Read [CLAUDE.md](CLAUDE.md), then [SOP.md](SOP.md) section 1.

## The map

The ruled 12-entry root (BOLO 143, approved 10/13). "Today" says what exists now; "not yet" waits on the staged cleanup.

| # | Entry | What lives there | Today |
|---|---|---|---|
| 1 | [CLAUDE.md](CLAUDE.md) | the front door for Claude: the four steps, the skills, two rules that bite | exists |
| 2 | [SOP.md](SOP.md) | the doctrine: procedures, format rules, lexicon | exists |
| 3 | [STATE.md](STATE.md) | the live index: what is active, what is blocked | exists |
| 4 | [BOLO.md](BOLO.md) | the watchlist: every standing to-do and ruling | exists |
| 5 | [.claude/](.claude/README.md) | agents, skills, rules, hook settings | exists |
| 6 | ops/ | administration: STATE, sit rep, cache, logs, operator BOLOs | not yet (`_CACHE`, `_LOG`, `oscar-mike` hold it) |
| 7 | tools/ | every script (stations, hooks, intake, loop) | exists as [_tools/](_tools/hooks/README.md) |
| 8 | canon/ | the story's single source of truth, registers, nodes | not yet (`ShroomsQ/_CANON`, `_CANON_NODES`) |
| 9 | ventures/ | BLACK and ORANGE business work | not yet (loose files at root) |
| 10 | library/ | books, PDFs, research, reference shelves | not yet (`.AIrefLIBRARY`, Zotero side) |
| 11 | archive/ | retired builds and one-offs, index at [_ARCHIVE/INDEX.md](_ARCHIVE/INDEX.md) | exists as `_ARCHIVE` |
| 12 | private/ | health, sexual, provider and personal detail; never in public files | exists as `_PRIVATE` |

**Administration versus development (pidx-01/02).** Administration is running the operation: ops holds the sit rep, STATE, the cache, the logs, and the operator-class BOLOs, and the OPERATOR seat works there. Development is making things: tools, canon, ventures and library hold the scripts, the story, the businesses (BLACK and ORANGE) and the reading. A file goes in ops if it records what happened or what is next; it goes in a development folder if it is something that gets built, shipped or read.

## Standing rulings kept from the old README

- GUTS99 retired 2026-09-03: the twelve subsystem coinages live on in BOLO 15; the scaffold is at `_ARCHIVE/_grognard/`.
- All builds through 2025.01 live under `_ARCHIVE/` (moved 2026-09-03); `X_` or `XX_` prefix means archived, `_` prefix means active.
- Current build: `2025.02_SELACIOUS_BUILD`. Primary story project: ASTRO7EX (also ASTROSE7X).
- Naming for SSOT files: `ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐ssot_SSOT_CREATION.md`.
- Theory lives in `ShroomsQ/_CANON/_SSOT/`; the 2024 vault is archived at `_ARCHIVE/_broodengine/`.
- Maintenance schedule: whenever I feel like it. Issues: disabled. Pull requests: you're kidding, right?

The full pre-map README is in git history (the commit before the map).

## License

MIT License (2024). Do whatever you want with it. Credit where it's due.
