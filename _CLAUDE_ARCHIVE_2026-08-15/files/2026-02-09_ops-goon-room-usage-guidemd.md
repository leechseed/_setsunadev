---
original_path: "/mnt/user-data/outputs/⚙️_ops_goon_room_usage_guide.md"
source_conversation: "MAIN SONNET"
created: 2026-02-09
trunk: BLACK
kind: generated-file
---

---
type: ssot_operations
category: operations
version: 1.0.0
last_updated: 2026-02-10
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: Defines step-by-step operational procedures for daily Goon Room workspace usage
dependencies:
  - [[⚙️_ops_goon_room_workflow]]
  - [[📐📐_ssot_writing_guide]]
---

# ⚙️ OPS: Goon Room Usage Guide

## Table of Contents
1. [Purpose](#purpose)
2. [System Overview](#system-overview)
3. [Key Terms](#key-terms)
4. [Daily Operating Procedures](#daily-operating-procedures)
5. [Tagging Protocols](#tagging-protocols)
6. [Weekly Review Procedures](#weekly-review-procedures)
7. [Canon Reference Procedures](#canon-reference-procedures)
8. [Troubleshooting](#troubleshooting)
9. [References](#references)
10. [Version History](#version-history)

---

## Purpose

This document provides operational procedures for daily Goon Room workspace usage. It establishes the practical workflow for rapid content capture, tag-based promotion, and canonical integration within the LEECHSEED narrative development system. Users follow these procedures to maintain separation between exploratory research and canonical documentation while enabling efficient promotion pathways.

---

## System Overview

### What the Goon Room Is

The **Goon Room** functions as a friction-free workspace for rapid research, ideation, and draft development. Content captured in the Goon Room requires no organizational decisions at point of creation. The workspace operates on tag-based promotion rather than manual file management.

### How the System Works

```
1. Capture → 2. Tag → 3. Auto-Stage → 4. Review → 5. Promote to Canon
```

**Capture**: Create session file, write content without structural constraints
**Tag**: Mark content quality inline during creative flow (#canon-ready, #ssot-candidate, #auth-candidate)
**Auto-Stage**: Tagged files move automatically to staging directories
**Review**: Weekly assessment of staged content
**Promote**: Move approved content to Canon with proper frontmatter

### What Makes It Different

Traditional systems require organizational decisions before capture. The Goon Room delays organization until quality assessment, eliminating capture friction while maintaining canonical rigor downstream.

---

## Key Terms

**Session File**: Timestamped markdown file created for single work session, located in `_GOON_ROOM/sessions/YYYY-MM/`

**Tagging**: Inline content classification using hashtags (#canon-ready, #ssot-candidate, #auth-candidate, #experiment)

**Auto-Staging**: Automatic file movement to staging directories triggered by tag presence

**Staging Directory**: Intermediate location (`_STAGED/`) where tagged content awaits review before canonical promotion

**Promotion**: Process of adding frontmatter and moving staged content to `_CANON/`

**Workspace**: Saved Obsidian layout configuration (Goon Room workspace vs Canon workspace)

**Bases**: Dynamic tables showing filtered vault content (Promotion Queue Base shows all tagged session content)

**Wikilink**: Internal link syntax `[[filename]]` creating bidirectional connections between files

**Graph**: Visual representation of wikilink connections between files

---

## Daily Operating Procedures

### Morning Startup

**Objective**: Begin work session in Goon Room workspace

**Procedure**:

1. **Open Obsidian vault**: Launch Obsidian, select ShroomsQ vault
2. **Switch to Goon Room workspace**: Press workspace hotkey (`Ctrl/Cmd + Shift + W`) or click workspace selector
3. **Verify workspace layout**:
   - Left pane shows Notebook Navigator with `_GOON_ROOM/` folder tree
   - Center pane ready for editing
   - Right sidebar shows Promotion Queue Base (currently empty)
4. **Create session file**: Press session creation hotkey (`Alt/Opt + Shift + N`) or manually create file in `_GOON_ROOM/sessions/2026-02/`
5. **Name session file**: Format `YYYY-MM-DD_topic_description.md`
   - Example: `2026-02-10_character_research.md`
6. **Begin capture**: Write content without organizational constraints

**Expected Duration**: 2 minutes

---

### Active Session Work

**Objective**: Capture research, ideas, and drafts during work session

**Procedure**:

1. **Write freely**: No structural requirements, no cleanup needed
2. **Link to Canon when needed**: Use wikilink syntax to reference SSOT or Authoritative documents
   - Format: `[[📐_ssot_narrative_astrology_framework]]`
   - Click link to open Canon document in new pane
   - Return to session file to continue work
3. **Tag content as quality emerges**: Apply tags inline at section level
4. **Save periodically**: Auto-staging triggers on save

**Canon Reference Example**:

```markdown
## Character Analysis

Reviewing [[📐_ssot_narrative_astrology_framework]] for Mars aspects.

Victoria's Mars conjunct Venus in 10th house creates public magnetism.
Need to verify this against [[🎯_auth_overexitout_victoria_midnight]] profile.

## New Insight #ssot-candidate

House placement modifies aspect interpretation significantly.
This should become part of the core framework.
```

**Expected Behavior**:
- Wikilinks create automatic backlinks in Canon documents
- Graph updates showing session → Canon connections
- Tagged content appears in Promotion Queue Base (right sidebar)

---

### End of Session

**Objective**: Close session and verify auto-staging

**Procedure**:

1. **Final save**: Ensure all content saved
2. **Check Promotion Queue Base**: Right sidebar shows newly tagged content
3. **Verify auto-staging**: Navigate to `_STAGED/` folders to confirm tagged files moved
   - Files with `#canon-ready` → `_STAGED/review/`
   - Files with `#ssot-candidate` → `_STAGED/ssot_candidates/`
   - Files with `#auth-candidate` → `_STAGED/authoritative_candidates/`
4. **Close Obsidian** or switch workspace if continuing with different work

**Expected Duration**: 1 minute

---

## Tagging Protocols

### Tag Definitions

**#canon-ready**
- **Use when**: Content requires no further development
- **Quality standard**: Meets SSOT or Authoritative documentation standards
- **Destination**: `_STAGED/review/`
- **Next step**: Weekend review, add frontmatter, move to Canon

**#ssot-candidate**
- **Use when**: Methodology or framework development
- **Quality standard**: Defines how systems work, applicable across all stories
- **Destination**: `_STAGED/ssot_candidates/`
- **Next step**: Verify SSOT classification, add to appropriate category

**#auth-candidate**
- **Use when**: Story-specific content development
- **Quality standard**: Character profiles, plot elements, worldbuilding for specific story
- **Destination**: `_STAGED/authoritative_candidates/`
- **Next step**: Identify SSOT dependencies, add to story directory

**#experiment**
- **Use when**: Exploratory content, hypothesis testing
- **Quality standard**: No quality requirement
- **Destination**: Remains in `_GOON_ROOM/`
- **Next step**: May evolve into candidate status later

### Tag Application

**Apply tags at section level**:

```markdown
## Section Title #tag-name

Content goes here.
Multiple paragraphs allowed.

## Another Section #different-tag

Different content with different tag.
```

**Tag priority**: If multiple tags present, Auto Note Mover uses first detected tag in this order:
1. #canon-ready (highest priority)
2. #ssot-candidate
3. #auth-candidate

**Tag modification**: Remove tag to prevent auto-staging, add tag to trigger staging on next save

---

## Weekly Review Procedures

**Objective**: Process staged content into Canon

**Frequency**: Weekly (recommended weekend)

**Procedure**:

### Step 1: Review Staged Files

1. **Open Goon Room workspace**
2. **Check Promotion Queue Base**: Right sidebar shows all staged content organized by tag
3. **Navigate to staging directories**:
   - `_STAGED/review/`
   - `_STAGED/ssot_candidates/`
   - `_STAGED/authoritative_candidates/`

### Step 2: Process SSOT Candidates

**For each file in `_STAGED/ssot_candidates/`**:

1. **Open file**
2. **Verify SSOT classification**: Content defines methodology, not story-specific application
3. **Copy SSOT frontmatter template**:

```yaml
---
type: ssot_methodology
category: [epistemology|narrative_frameworks|character_systems|plot_systems|style_guides|operations]
version: 1.0.0
last_updated: 2026-02-10
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: [One sentence description]
dependencies: []
---
```

4. **Paste at top of file**
5. **Fill in fields**:
   - Select appropriate category
   - Write purpose statement
   - List dependencies using wikilinks `[[📐_ssot_other_doc]]`
6. **Verify content follows [[📐📐_ssot_writing_guide]] standards**:
   - Table of Contents present
   - No contractions
   - Declarative language
   - Proper structure
7. **Update filename**: Add emoji prefix `📐_ssot_descriptive_name.md`
8. **Move to Canon**: Drag to `_CANON/_SSOT/[category]/`

### Step 3: Process Authoritative Candidates

**For each file in `_STAGED/authoritative_candidates/`**:

1. **Open file**
2. **Identify which SSOT documents content depends on**
3. **Copy Authoritative frontmatter template**:

```yaml
---
type: authoritative
story: [OVEREXITOUT|ASTRO7EX|LAKAD]
category: [character|plot|theme|world]
entity: [Specific character/element name]
ssot_dependencies:
  - [[📐_ssot_framework_name]]
version: 1.0.0
last_updated: 2026-02-10
status: canonical
---
```

4. **Paste at top of file**
5. **Fill in fields**:
   - Select story
   - Select category
   - Name entity
   - List all SSOT dependencies
6. **Update filename**: Add emoji prefix `🎯_auth_[story]_[entity].md`
7. **Move to Canon**: Drag to `_CANON/_AUTHORITATIVE/[STORY]/[category]/`

### Step 4: Process Canon-Ready Files

**For files in `_STAGED/review/`**:

1. **Assess whether SSOT or Authoritative**
2. **Follow appropriate process above**
3. **If unsure**: Ask "Does this define how a system works (SSOT) or apply that system to specific content (Auth)?"

### Step 5: Cleanup

1. **Delete processed files from staging**: Content now in Canon
2. **Leave unprocessed files**: Review again next week
3. **Update graph if needed**: Verify wikilinks functional

**Expected Duration**: 30-60 minutes depending on weekly output

---

## Canon Reference Procedures

### During Goon Room Work

**Objective**: Reference Canon documents while maintaining Goon Room workspace

**Procedure**:

**Method 1: Wikilink + Click**

1. Type `[[` in session file
2. Begin typing Canon document name
3. Select from autocomplete
4. Click completed wikilink
5. Canon document opens in new pane
6. Read needed information
7. Close pane or return to session file

**Method 2: Quick Switcher**

1. Press `Ctrl/Cmd + O`
2. Type Canon document name
3. Press Enter
4. Document opens
5. Press `Ctrl/Cmd + O` again, type session filename to return

**Method 3: Workspace Switch**

1. Press workspace hotkey `Ctrl/Cmd + Shift + W`
2. Switches to Canon workspace
3. Navigate folder tree to needed document
4. Read information
5. Press workspace hotkey again to return to Goon Room

**Recommended**: Method 1 (wikilink) - creates bidirectional link, updates graph, fastest

---

### Using Graph for Canon Discovery

**Objective**: Find related Canon documents

**Procedure**:

1. **Open graph view**: Click graph icon or `Ctrl/Cmd + G`
2. **Focus on current file**: Click current session file node in graph
3. **Observe connected nodes**: Canon documents you have linked appear as connected nodes
4. **Click node to navigate**: Opens that Canon document
5. **Use local graph**: Shows only immediate connections to current file

**Graph Filter** (optional):

- Show only Canon: Filter path `_CANON`
- Hide Goon Room: Exclude path `_GOON_ROOM`
- Color by folder: SSOT blue, Auth green

---

## Troubleshooting

### Issue: Auto Note Mover Not Working

**Symptoms**: Tagged file remains in `_GOON_ROOM/` after save

**Solutions**:

1. **Verify tag spelling**: Must be exact `#canon-ready` `#ssot-candidate` `#auth-candidate`
2. **Check plugin enabled**: Settings → Community Plugins → Auto Note Mover (enabled)
3. **Verify rules configured**: Settings → Auto Note Mover → check rules present
4. **Check file saved**: Trigger requires save operation
5. **Restart Obsidian**: Plugin may need reload

### Issue: Promotion Queue Base Empty

**Symptoms**: Right sidebar Base shows no content despite tagged files

**Solutions**:

1. **Verify Base filter**: Check filter set to `folder:_GOON_ROOM OR folder:_STAGED`
2. **Check tags in filter**: Verify `tags:(#canon-ready OR #ssot-candidate OR #auth-candidate)`
3. **Refresh Base**: Click refresh icon in Base view
4. **Check files actually tagged**: Open session files, verify tags present

### Issue: Wikilinks Not Creating Backlinks

**Symptoms**: Canon document backlinks pane empty despite session file links

**Solutions**:

1. **Verify link syntax**: Must be `[[filename]]` exactly
2. **Check filename matches**: Link must match actual Canon filename
3. **Wait for index**: Obsidian may need time to update backlinks
4. **Restart Obsidian**: Force backlink index refresh

### Issue: Graph Not Showing Connections

**Symptoms**: Graph shows isolated nodes instead of connections

**Solutions**:

1. **Verify wikilinks present**: Open files, check for `[[wikilink]]` syntax
2. **Check graph filters**: May be hiding certain paths or folders
3. **Zoom out**: Connections may exist but graph zoomed too far in
4. **Check local vs global**: Switch between local graph (current file) and global graph (all files)

---

## References

### Internal Dependencies
- [[⚙️_ops_goon_room_workflow]]: Complete technical specification
- [[📐📐_ssot_writing_guide]]: Documentation standards for Canon promotion

### External Documentation
- Obsidian Workspaces documentation
- Obsidian Bases plugin guide
- Auto Note Mover plugin documentation
- Obsidian Graph View usage

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial Goon Room usage guide for daily operations |
