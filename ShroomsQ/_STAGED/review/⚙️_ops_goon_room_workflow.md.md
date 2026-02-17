---

type: ssot_operations category: operations version: 1.0.0 last_updated: 2026-02-10 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: Defines the operational workflow for the Goon Room workspace within the LEECHSEED narrative development system dependencies:

- [[📐📐_ssot_writing_guide]]

---

# ⚙️ Goon Room Workflow Protocol

## Table of Contents

1. [Purpose](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#purpose)
2. [Core Concepts](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#core-concepts)
3. [Workspace Configuration](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#workspace-configuration)
4. [Session File Protocol](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#session-file-protocol)
5. [Tagging System](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#tagging-system)
6. [Auto-Staging Mechanism](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#auto-staging-mechanism)
7. [Promotion Workflow](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#promotion-workflow)
8. [Graph Visualization](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#graph-visualization)
9. [Integration Points](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#integration-points)
10. [Examples](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#examples)
11. [References](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#references)
12. [Version History](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#version-history)

---

## Purpose

The **Goon Room** establishes a friction-free workspace for rapid research, ideation, and draft development within the LEECHSEED narrative system. This document defines the operational protocols governing session file creation, content tagging, automated staging, and promotion to canonical documentation. The Goon Room operates as the primary creative workspace where chaotic exploration occurs without organizational overhead, while maintaining clear pathways to canonical integration.

---

## Core Concepts

### The Goon Room Philosophy

The Goon Room workspace operates on three foundational principles:

1. **Minimum Friction Capture**: Session files created with single hotkey activation, timestamped automatically, requiring no organizational decisions at point of capture
2. **Tag-Based Promotion**: Content quality determination occurs during creative flow through inline tagging rather than separate organizational sessions
3. **Automated Staging**: Tagged content migrates to staging directories automatically, eliminating manual file management

### Workspace Isolation

The Goon Room maintains complete separation from Canon workspace through Obsidian workspace system. This isolation prevents cross-contamination between exploratory content and established doctrine. Users switch between workspaces via dedicated hotkey, preserving distinct visual and functional contexts for different operational modes.

### Content Flow Architecture

```
Capture → Tag → Auto-Stage → Review → Promote to Canon
```

Content progresses through this pipeline with automation handling file movement and manual intervention limited to quality assessment and canonical integration decisions.

---

## Workspace Configuration

### Required Plugins

The Goon Room workspace requires the following Obsidian plugins:

- **Workspaces** (core plugin): Workspace isolation and switching
- **Bases** (core plugin): Dynamic promotion queue visualization
- **Auto Note Mover**: Tag-based automatic file staging
- **Notebook Navigator**: Dual-pane Evernote-style interface
- **Templater**: Session file template automation

### Workspace Layout

**Goon Room Workspace Structure:**

```
Left Pane: Notebook Navigator
  - Folder tree focused on _GOON_ROOM/
  - Recent files section
  - Tag management interface

Center Pane: Active Session File
  - Primary editing area
  - Full markdown support
  - Inline tagging capability

Right Sidebar: Promotion Queue Base
  - Canon Ready view (filter: #canon-ready)
  - SSOT Candidates view (filter: #ssot-candidate)
  - Auth Candidates view (filter: #auth-candidate)
  - Experiments view (filter: #experiment)
```

### Workspace Hotkey

```
Workspace Switch: Ctrl/Cmd + Shift + W
```

This hotkey toggles between Goon Room and Canon workspaces, preserving distinct layouts and contexts.

---

## Session File Protocol

### File Naming Convention

Session files follow timestamped naming:

```
Format: YYYY-MM-DD_descriptive_topic.md
Location: _GOON_ROOM/sessions/YYYY-MM/

Example: 2026-02-10_mars_aspects_research.md
```

### Session File Creation

**Hotkey:** `Alt/Opt + Shift + N` (configured via Templater)

**Process:**

1. User activates hotkey
2. Templater creates new file in current month directory
3. Filename auto-generated with current timestamp
4. Optional: User appends descriptive topic to filename
5. Template inserts basic frontmatter structure
6. File opens in center pane for immediate capture

### Session File Template

```markdown
---
created: {{date:YYYY-MM-DD HH:mm}}
tags: []
type: session
status: active
---

# Session: {{date:YYYY-MM-DD}}

## Focus


## Notes


## Links to Canon

```

This template provides minimal structure while maintaining flexibility for unstructured capture.

---

## Tagging System

### Tag Taxonomy

The Goon Room employs four primary tags for content classification:

**#canon-ready**

- Content approved for immediate canonical integration
- Requires no further development
- Quality meets SSOT or Authoritative standards
- Triggers auto-staging to `_STAGED/review/`

**#ssot-candidate**

- Methodology or framework development
- Potential Single Source of Truth documentation
- Requires review before canonical promotion
- Triggers auto-staging to `_STAGED/ssot_candidates/`

**#auth-candidate**

- Story-specific content development
- Character profiles, plot elements, worldbuilding
- Requires SSOT dependency verification
- Triggers auto-staging to `_STAGED/authoritative_candidates/`

**#experiment**

- Exploratory content
- Hypothesis testing
- May or may not reach canonical status
- No auto-staging trigger
- Remains in `_GOON_ROOM/` for reference

### Tag Application Protocol

Tags apply inline at the section or paragraph level within session files:

```markdown
## New Mars Framework #ssot-candidate

The house position modifies aspect interpretation.

Mars conjunct Venus in 10th house creates public magnetism.

## Character Concept #auth-candidate

Victoria's Mars placement drives her MORN ambition.

## Random Thought #experiment

What if we inverted the dignity system?
```

Tags attach to immediately preceding content block, allowing granular classification within single session files.

---

## Auto-Staging Mechanism

### Auto Note Mover Configuration

**Plugin:** Auto Note Mover **Trigger:** File modification (on save) **Scope:** Files in `_GOON_ROOM/` only

**Rules:**

```yaml
Rule 1:
  Tag: #canon-ready
  Destination: _STAGED/review/
  
Rule 2:
  Tag: #ssot-candidate
  Destination: _STAGED/ssot_candidates/
  
Rule 3:
  Tag: #auth-candidate
  Destination: _STAGED/authoritative_candidates/
```

### Staging Behavior

When session file saved with qualifying tag:

1. Auto Note Mover detects tag presence
2. File moves to corresponding staging directory
3. Bidirectional links remain functional
4. Graph visualization updates automatically
5. Promotion Queue Base reflects new staged content

Files containing multiple tags move to directory corresponding to first detected tag in priority order: `#canon-ready` > `#ssot-candidate` > `#auth-candidate`.

### Exclusions

The following directories excluded from Auto Note Mover:

- `_CANON/` (canonical documents never auto-move)
- `_STAGED/` (already staged, prevents loops)
- `_ARCHIVE/` (archived content remains fixed)
- `_META/` (system files protected)

---

## Promotion Workflow

### Weekly Review Ritual

**Frequency:** Weekly (recommended weekend) **Location:** `_STAGED/` directories **Process:**

1. Open Goon Room workspace
2. Check Promotion Queue Base in right sidebar
3. Review each staged file category
4. For each file:
    - Verify content quality
    - Add frontmatter (manual, following SSOT/Auth standards)
    - Add wikilinks to dependent SSOT documents
    - Move to appropriate `_CANON/` subdirectory
    - Update graph if needed

### SSOT Promotion

**Source:** `_STAGED/ssot_candidates/` **Destination:** `_CANON/_SSOT/[category]/`

**Frontmatter Template:**

```yaml
---
type: ssot_methodology
category: [appropriate category]
version: 1.0.0
last_updated: YYYY-MM-DD
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: [one sentence description]
dependencies: []
---
```

**Process:**

1. Copy SSOT frontmatter template
2. Paste at top of staged file
3. Fill category, purpose, dependencies fields
4. Verify content follows [[📐 ssot_writing_guide]] standards
5. Move to `_CANON/_SSOT/[category]/`
6. Update filename with emoji prefix: `📐_ssot_[name].md`

### Authoritative Promotion

**Source:** `_STAGED/authoritative_candidates/` **Destination:** `_CANON/_AUTHORITATIVE/[STORY]/[category]/`

**Frontmatter Template:**

```yaml
---
type: authoritative
story: [OVEREXITOUT|ASTRO7EX|LAKAD]
category: [character|plot|theme|world]
entity: [specific name]
ssot_dependencies: []
version: 1.0.0
last_updated: YYYY-MM-DD
status: canonical
---
```

**Process:**

1. Copy Authoritative frontmatter template
2. Identify which SSOT documents content depends on
3. Add wikilinks to dependencies
4. Move to appropriate story subdirectory
5. Update filename with emoji prefix: `🎯_auth_[story]_[name].md`

---

## Graph Visualization

### Graph Configuration

**Location:** Right sidebar (Canon workspace) **Purpose:** Visualize SSOT/Authoritative dependency networks

**Filter Settings:**

```yaml
Groups:
  SSOT: 
    path: _CANON/_SSOT
    color: #4A90E2 (blue)
  
  Authoritative:
    path: _CANON/_AUTHORITATIVE
    color: #50C878 (green)
  
  Goon Room:
    path: _GOON_ROOM
    color: #FFA500 (orange)

Display Filters:
  Show: _CANON, _STAGED
  Hide: _ARCHIVE, _META, _GOON_ROOM (when in Canon workspace)
```

### Graph Usage

**In Canon Workspace:**

- Local graph shows immediate dependencies for current SSOT/Auth document
- Global graph shows entire methodology network
- Click nodes to navigate between related documents

**In Goon Room Workspace:**

- Graph shows connections between session files and referenced canon
- Identifies which SSOT documents frequently referenced during research
- Reveals emerging patterns in content development

---

## Integration Points

### Bidirectional Linking

Session files link to Canon documents using standard wikilink syntax:

```markdown
Referencing the [[📐_ssot_narrative_astrology_framework]] for this analysis.

Victoria's profile ([[🎯_auth_victoria_midnight]]) demonstrates this principle.
```

These links:

- Create automatic backlinks in Canon documents
- Appear in graph visualization
- Persist after file moves to staging
- Enable Canon documents to show which sessions reference them

### Cross-Workspace Navigation

**From Goon Room to Canon:**

1. Click wikilink to Canon document
2. Document opens in new pane
3. Quick switcher (`Ctrl/Cmd + O`) returns to session file

**From Canon to Goon Room:**

1. Check backlinks pane in Canon document
2. See which session files reference current document
3. Click backlink to view research context

### Bases Integration

The Promotion Queue Base provides live query of tagged content:

```
Query Logic:
  folder:_GOON_ROOM OR folder:_STAGED
  AND tags:(#canon-ready OR #ssot-candidate OR #auth-candidate)

Update Frequency: Real-time on file save

Columns Displayed:
  - File name
  - Tags
  - Modified date
  - File path
```

This eliminates manual tracking of promotion-ready content.

---

## Examples

### Example 1: Research Session Leading to SSOT

**Session File:** `_GOON_ROOM/sessions/2026-02/2026-02-10_mars_house_research.md`

```markdown
---
created: 2026-02-10 14:30
tags: []
type: session
status: active
---

# Session: 2026-02-10

## Focus
Investigating how house placement modifies Mars aspects

## Notes

Been thinking about Mars conjunct Venus. Current framework in 
[[📐_ssot_narrative_astrology_framework]] treats it as pure passion.

Too simple.

## New Framework #ssot-candidate

Mars-Venus conjunction interpretation requires house context:

1st House: Personal magnetism, self-driven attraction
7th House: Relationship combustion, partner obsession
10th House: Public persona as seductive, career driven by desire

This creates character depth. Validates with Victoria's chart.

## Next Steps

Test against other characters.
If holds up, promote to SSOT and update Auth profiles.
```

**Auto-Staging:**

- File saved
- Auto Note Mover detects `#ssot-candidate`
- Moves to `_STAGED/ssot_candidates/2026-02-10_mars_house_research.md`
- Promotion Queue Base updates

**Promotion:**

- Weekend review
- Add SSOT frontmatter
- File becomes: `_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐_ssot_mars_aspects_house_interpretation.md`

### Example 2: Character Development Session

**Session File:** `_GOON_ROOM/sessions/2026-02/2026-02-11_victoria_rework.md`

```markdown
# Session: 2026-02-11

## Victoria Scene Draft

Writing Act 2 confrontation scene.

Victoria's Mars in 10th explains her MORN drive perfectly.

## Character Insight #auth-candidate

Victoria's public ambition (Mars 10th) conflicts with private vulnerability (Moon 12th).

This creates her core tension: powerful exterior, hidden emotional chaos.

Update character profile with this dimension.
```

**Auto-Staging:**

- Moves to `_STAGED/authoritative_candidates/`
- Ready for integration into existing Victoria profile

**Promotion:**

- Review staged file
- Open existing `🎯_auth_victoria_midnight.md`
- Integrate new insight into character psychology section
- Delete staged file (content absorbed)

---

## References

### Internal Dependencies

- [[📐 ssot_writing_guide]]: SSOT documentation standards
- [[⚙️⚙️_ops_mission_control_specification]]: Future automation framework

### External Documentation

- Obsidian Workspaces: https://help.obsidian.md/Plugins/Workspaces
- Obsidian Bases: https://help.obsidian.md/Plugins/Bases
- Auto Note Mover plugin documentation

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-02-10|Initial Goon Room workflow protocol established|