# _setsunadev — Comprehensive Project Brief

> **Repository**: `_setsunadev`
> **Author**: CHEF ZAKUZOKU / U01_LEECHSEED / ggrimace
> **License**: MIT (2024)
> **Generated**: 2026-02-09

---

## 1. PROJECT IDENTITY

### Core Purpose & Mission

_setsunadev is a **personal creative development ecosystem** — a monorepo workspace for designing, researching, and iterating on narrative-driven media projects. It functions as a combined:

- **Story laboratory**: Where narrative structures are prototyped using formal frameworks (Dramatica, Narrative Context Protocol)
- **Personal knowledge base**: Centralizing creative theory, media influence analysis, and worldbuilding research
- **Build pipeline**: Tracking versioned iterations of story projects from pre-alpha through release candidates
- **Operational hub**: Housing SOPs, devlogs, tooling scripts, and configuration for the creator's full workflow

The unifying mission is to **systematize the creative process** — treating storytelling with the rigor of software engineering while preserving artistic intuition.

### Target Users / Audience

- **Primary**: The solo creator (CHEF ZAKUZOKU) — this is a personal workspace, not a team project
- **Secondary**: AI assistants (Claude, LLMs) ingesting the structured markdown for collaborative story development
- **Tertiary**: Future collaborators who may contribute via the Narrative Context Protocol's attribution system

### Unique Value Proposition

This is not a typical codebase. It is a **narrative engineering environment** that:

1. Applies formal story theory (Dramatica's storyform model) as a structural backbone
2. Uses unconventional creative inputs (astrology, tarot, media DNA analysis) as systematic character/plot generators
3. Maintains full version history of story iterations with codename-based releases
4. Implements the Narrative Context Protocol for AI-era authorship attribution
5. Bridges multiple knowledge management tools (Obsidian, Logseq, Joplin, Hugo) into one workspace

---

## 2. ARCHITECTURE & SYSTEMS

### Key Frameworks and Their Roles

| Framework | Role | Location(s) |
|-----------|------|-------------|
| **Dramatica** | Core story structure engine — provides the "storyform" (thematic argument, character dynamics, plot progression) | `.AIrefLIBRARY/`, `DRAMATICA V4 PROGRAM BUILDS/`, `_dramatica_OXO_builds/` |
| **Narrative Context Protocol (NCP)** | Open-source schema for structured narrative data with git-style attribution tracking | `narrative-context-protocol-main/` |
| **Krebs Cycle of Creativity / Bermuda Quadrilateral** | Meta-framework for understanding creative energy flow between Science, Engineering, Design, and Art | `_broodengine/` |
| **GUTS99** | Personal media influence analysis system — 12 subsystems cataloging aesthetic DNA across media types | `_grognard/` |
| **Hugo** | Static site generator for publishing narrative documentation | `hugo-dramatica-draft-v1/` |
| **Obsidian** | Primary knowledge management tool — vaults for research, character work, manuscripts | `logseq_2023_journals_notes/leechseed2/`, `OVER_EXIT_OUT_OBSIDIAN/`, `_devlog/LEECHSEED STUDIES/` |
| **Logseq / Joplin** | Secondary note-taking tools with sync integration | `logseq_2023_journals_notes/`, `.ASTRO7EX.SYNC.JOPLIN/` |
| **Final Draft** | Professional screenwriting software | `OUTLIERS_FINAL_DRAFT/`, `.finaldraftfiles/` |

### Versioned Builds — The Release History

The project tracks story iterations using a software-style versioning scheme with anime-inspired codenames:

| Version | Codename | Stage | Description |
|---------|----------|-------|-------------|
| `1.00` | **ASTRO7EX / DRAMATICA** | Prototype | Initial PDF test output, Dramatica framework setup |
| `1.0` | **BELLE** | Pre-Alpha | First prototype build |
| `1.01` | **EMIWU** | Alpha | Added guides, AI prompts, correspondence |
| `1.02` | **MARIMARI** | Iteration | English language version |
| `1.03` | **GOONIRU** | Iteration | Added query scripts for data exploration |
| `1.03.1` | **BUNNIRU** | RC1 | Hugo-based release candidate |
| `1.04` | **MARIMARI EN** | RC1 | English release candidate |
| `2025.01` | **MCMARI** | 2025 Build | Comprehensive restructure with character esoterics |
| `2025.02` | **SELACIOUS** | 2025 Build (Latest) | Current active build with expanded systems |

**Naming convention**: `[Status]_[Version].[Iteration]_[Codename]_BUILD`
- `X_` or `XX_` prefix = archived/deprecated
- `_` prefix = active
- RC = Release Candidate

### Core Workflows and Data Flows

```
Media Consumption → GUTS99 Analysis → Aesthetic DNA Profile
                                          ↓
Creative Theory (Bermuda Quadrilateral) → Story Premise
                                          ↓
Dramatica Storyform → Character/Plot/Theme Structure
                                          ↓
Esoteric Systems (Astrology, Tarot) → Character Personality + Plot Arcs
                                          ↓
NCP Schema → Structured Story Data (JSON/SQLite)
                                          ↓
Final Draft / Manuscript → Screenplay / Prose Output
                                          ↓
Hugo Static Site → Published Documentation
```

---

## 3. TECHNICAL STACK

### Languages & Technologies

| Technology | Usage |
|------------|-------|
| **Markdown** | Primary content format — hundreds of structured .md files with frontmatter |
| **Python** | Utility scripts (PDF/EPUB conversion, media downloading, format conversion, YouTube tools) |
| **JSON** | Configuration (Obsidian, admonitions, NCP schema, VSCode settings) |
| **SQL / SQLite** | Story data storage via NCP (`DB Lite/` contains .db and .sqbpro files) |
| **HTML/CSS** | Hugo theme templates, NCP documentation rendering |
| **TOML** | Hugo configuration (`hugo.toml`), Rust build config (`Cargo.toml`) |
| **Final Draft XML** | Screenplay files (`.fdx`) |
| **Dramatica** | Proprietary `.dsf` storyweaving files |

### Dependencies & Integrations

- **Git LFS**: Configured for 20+ media file types (images, video, audio, archives, PDFs)
- **Git Submodules**: `hugo-book` theme (alex-shpak/hugo-book)
- **Python venv**: Virtual environment at `.venv/` and within build directories
- **VS Code**: Primary editor with Journal extension, spell checker (`_cspell/`), custom settings
- **Claude CLI**: `bin/claude.exe` (231MB) — AI assistant integration
- **Obsidian Plugins**: admonition, Discord RPC, style-settings, various themes (30+)
- **CrystalDiskInfo / HD Tune**: Referenced in operational SOPs

### Build Systems

- **Hugo**: Static site generation (`hugo-dramatica-draft-v1/`)
- **Python scripts**: Batch processing for format conversion, media management
- **NCP Python module**: Schema validation and story data processing (`narrative-context-protocol-main/python/`)

---

## 4. CONTENT STRUCTURE

### Purpose of Major Directories

| Directory | Purpose |
|-----------|---------|
| `_broodengine/` | **Creative theory vault** — Core frameworks (Krebs Cycle, Bermuda Quadrilateral), style guides, naming conventions, mathematical theory, studio design notes |
| `_grognard/` | **GUTS99 media influence system** — 12 subsystems cataloging personal aesthetic DNA across film, anime, literature, games, music, art, comics, theater, web culture, and more |
| `_devlog/` | **Development journal** — Dated journal entries (2024), VS Code Journal integration guide, LEECHSEED STUDIES Obsidian vault with character/theme/setting research |
| `_operations/` | **Standard Operating Procedures** — Technical how-tos (HDD installation, file transfer) for maintaining continuity |
| `_DIRECTORY OF DIR/` | **Knowledge base index** — Subject-specific collections: narratology, game design, database systems, design patterns, metadata schemas, reference sources, writing prompts, Python scripts |
| `_cake/` | **Miscellaneous research** — Film catalog, TTRPG interests, business ideas, utility scripts |
| `_dramatica_OXO_builds/` | **Dramatica project variants** — Different story configurations |
| `.AIrefLIBRARY/` | **AI reference library** — 22 Dramatica PDF reports (theme, character, plot analyses) for LLM ingestion |
| `narrative-context-protocol-main/` | **NCP framework** — Full specification, schema, examples (Anora, Shawshank Redemption), Python implementation, SQLite databases |
| `_2025.02_SELACIOUS_BUILD/` | **Current active build** — Rapid prototyping, character esoterics (astrology, tarot), worldbuilding, plot databases |
| `XX_2025.01_MCMARI_BUILD/` | **Previous build** — Similar structure, slightly less comprehensive |
| `hugo-dramatica-draft-v1/` | **Hugo site** — Static site for publishing Dramatica-based narrative documentation |
| `logseq_2023_journals_notes/` | **Legacy knowledge base** — Logseq journals (2022-2023), Obsidian vaults, Python script archive, Foundry RPG config |
| `OUTLIERS_FINAL_DRAFT/` | **Screenplay project** — Final Draft screenplay file (outliers.fdx) |
| `WORLDBUILIDNG THROUGHLINGE/` | **Worldbuilding reference** — Civilization-scale narrative throughlines |
| `lola-sama/` | **Ollama AI framework** — Local AI model data |
| `football_qb_training/` | **Non-narrative reference** — Quarterback training methodology (likely research for writing sports scenes or personal interest) |

### Content Types & Organization Philosophy

**Content Types**:
1. **Theoretical frameworks** (`.md`) — Creative theory, narrative analysis, style guides
2. **Story data** (`.json`, `.db`, `.dsf`, `.fdx`) — Structured narrative objects
3. **Research notes** (`.md`) — Character studies, plot development, worldbuilding
4. **Journal entries** (`.md`) — Personal reflections and development logs
5. **Reference reports** (`.pdf`) — Dramatica analysis outputs
6. **Utility scripts** (`.py`) — Automation and conversion tools
7. **Configuration** (`.json`, `.toml`) — Tool and environment settings
8. **Media assets** — Images, GIFs, fonts (managed via Git LFS)

**Organization Philosophy**:
- **Underscore prefix** (`_`) for project/active directories
- **Dot prefix** (`.`) for system/hidden directories
- **`_dir` suffix** for subject-specific collections
- **Version-codename pattern** for build iterations
- **Hierarchical naming** following the style guide: `System.Subsystem.Component`
- **LLM-ready markdown** with frontmatter metadata, explicit delimiters, and standardized terminology

### Naming Conventions & Taxonomies

- **Builds**: `[Status]_[Version].[Iteration]_[Codename]_BUILD`
- **Reports**: `r[#]_PSG_[PROJECT]_[DESCRIPTION].pdf`
- **Queries**: `query_by_[PARAMETER].py`
- **GUTS99 Tags**: `#VISCERA`, `#NEOGUTS`, `#LYMPH`, `#LUDOVORE`, `#AUDIVA`, `#LUSTRA`, `#OCULON`, `#TENDRA`, `#EPOCHE`, `#PANELOS`, `#MYOFLEX`, `#VERBOMANCY`
- **Sync dirs**: `.PROJECT.SYNC.TOOL` (e.g., `.ASTRO7EX.SYNC.JOPLIN`)

---

## 5. PROJECT STATE

### Current Maturity / Stage

- **Overall**: Mid-development — the project has evolved through 9+ iterations from pre-alpha to active 2025 builds
- **Active build**: `_2025.02_SELACIOUS_BUILD` represents the current working state
- **Frameworks**: Well-established — GUTS99, Bermuda Quadrilateral, and Dramatica integration are documented but still expanding
- **NCP Integration**: Early-stage — the Narrative Context Protocol has been imported but story data population appears partial
- **Hugo Site**: Skeleton — basic configuration exists but content is minimal (single test post)
- **GUTS99**: Baseline — 1 entry per subsystem (12 total), targeting 30-40+ entries

### Active vs. Archived Components

**Active**:
- `_2025.02_SELACIOUS_BUILD/` — Current build with character esoterics, worldbuilding, plot research
- `_broodengine/` — Living theory documentation
- `_grognard/` — GUTS99 system (actively being populated)
- `_devlog/` — Development journaling
- `narrative-context-protocol-main/` — NCP framework
- `.AIrefLIBRARY/` — AI reference materials

**Archived / Deprecated** (prefix `X_` or `XX_`):
- `X_1_PRE-ALPHA_BUILD_CODENAME_BELLE/`
- `X_1.01_EMIWU_ALPHA_BUILD/`
- `x_1.02_MARIMARI_EN_BUILD/`
- `x_1.03_GOONIRU_BUILD/`
- `XX_2025.01_MCMARI_BUILD/`

**Uncertain Status**:
- `_1.03.1 RC1_BUNNIRU_BUILD_HUGO/` — May be superseded
- `_1.04 RC1_MARIMARI_EN_BUILD/` — May be superseded
- `logseq_2023_journals_notes/` — Legacy but contains valuable script archive

### Roadmap Hints from Devlog & Structure

1. **GUTS99 Expansion**: System is at baseline (12 entries) with a target of 30-40+ entries across all subsystems — significant cataloging work ahead
2. **Hugo Publication**: Hugo site skeleton exists, suggesting intent to publish narrative documentation as a static site
3. **NCP Adoption**: Full specification imported with examples — likely planning to structure all story data through NCP schema
4. **Character Esoterics Deepening**: The SELACIOUS build's astrology/tarot systems are comprehensive but appear to be research-stage, not yet applied to final characters
5. **Screenplay Development**: Final Draft files exist (OUTLIERS), suggesting active screenplay production
6. **Build Consolidation**: The shift from numeric versioning (1.x) to date-based versioning (2025.x) suggests a maturation of the release process
7. **AI Integration**: Claude CLI presence, `.AIrefLIBRARY`, and LLM-optimized markdown all indicate deepening AI-assisted creative workflow

---

## Appendix: Quick Reference for AI Assistants

### Key Entry Points

- **To understand the story theory**: Start with `_broodengine/brood.theory.bermuda.quadrilateral.md`
- **To understand the story structure**: Read `.AIrefLIBRARY/` PDF reports (r1-r22)
- **To understand the NCP schema**: Read `narrative-context-protocol-main/SPECIFICATION.md`
- **To understand the creator's aesthetic**: Read `_grognard/` GUTS99 entries
- **To understand current work**: Explore `_2025.02_SELACIOUS_BUILD/`
- **To understand naming/style conventions**: Read `_broodengine/styleguide.md`

### Story Project Codename: ASTRO7EX

The primary narrative project appears to be codenamed **ASTRO7EX** (also referenced as ASTROSE7X). This is the story being developed through the Dramatica framework, with:
- Dramatica storyweaving files (`.dsf`)
- 22 analysis reports (`.pdf`)
- NCP database entries (`.db`)
- Episode structure (`ASTRO7EX_EPISODE_1/`)

### The Creator's Methodology

CHEF ZAKUZOKU approaches narrative creation as a **systems design problem**, combining:
- Formal narrative theory (Dramatica) for structural integrity
- Esoteric systems (astrology, tarot) for character generation and plot dynamics
- Media influence analysis (GUTS99) for aesthetic coherence
- Creative energy theory (Bermuda Quadrilateral) for workflow optimization
- Software engineering practices (versioning, SOPs, build management) for process discipline
