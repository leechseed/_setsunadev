# BOLO 102 batch C: proposed rules for missing procedures

Status: PROPOSALS only. No source doc is edited. Chief rules them later in one batch (ruled 10/5, "All recs go"). Gaps are in gap-number order; 24 entries.

### C2 · ssot epistemology truth verification · no cap on sources per framework and no test for which library ids qualify
**Proposed rule:** The author gives each framework one or two library ids on its Sources line. A qualifying id is a BVX number or a subject code (PSY, TEC, MIL, MSX) that names a held library file. Chief rules any third source in.
**Why:** All ten Sources lines already carry one or two ids of that kind, and Frameworks 3 and 4 say "method, no source".
**Lands in:** ssot epistemology truth verification, one rule paragraph above Framework 1, mirrored in the how-to step "Add a Sources line".

### C6 · ssot_00_base_60_number_system · no rule for rounding a converted threshold up or down
**Proposed rule:** The author rounds to the nearest valid value on the target scale and respects any divisibility constraint. When two valid values sit equally near, or the nearest breaks a constraint, Chief picks the direction by narrative need. The author records the direction and the reason.
**Why:** Rule 7 already says "nearest valid value" and "document the rounding direction"; the Truth Vulnerability case rounded down so the flag fires sooner.
**Lands in:** ssot_00_base_60_number_system, Rule 7 of the variable rules, with the same line in the how-to step "Set a flag threshold".

### C7 · ssot_00_module_architecture · the module FLAGS block names four states and defines none
**Proposed rule:** A module flag uses the four core definitions unchanged. ACTIVE means the condition is met now. PENDING means it is met at a defined narrative event. FIRED_PRE_STORY means it was met before story entry. INACTIVE means it is not met. The author of a module links to the slice's "Flag Trigger Conditions" instead of redefining them.
**Why:** The vertical slice and the setting system already define all four, and the module block copies the same four names.
**Lands in:** ssot_00_module_architecture, Computation Block, one line under `states:`.

### C8 · ssot_00_module_architecture · no rule for when a module moves from planned to draft to active
**Proposed rule:** A module moves to `planned` when its registry entry holds every field and a variable list. It moves to `draft` when the author writes the module declaration and the variable declarations under `MOD.[CODE].*`. It moves to `active` when the application can enable it and Chief rules it in. Chief rules every move.
**Why:** The Module Lifecycle already orders Creation, then Activation, and the registry parks variable lists on the module build.
**Lands in:** ssot_00_module_architecture, Registry Format, under the `status` row.

### C11 · ssot_00_module_registry · the audit names slice 3.3.1 but not who rules a module absorbed or dropped
**Proposed rule:** An MS reads the vertical slice and reports one verdict per module. Chief rules the verdict: absorbed, retired, or still planned. The author then records where each variable went in the Absorbed Modules table.
**Why:** The 10/4 audit set the verdicts from the slice, and the Absorbed Modules tables already record each variable's destination.
**Lands in:** ssot_00_module_registry, "Audit of Planned Modules", one line under the audit summary.

### C15 · ssot_00_pattern_library · no step-by-step method for stacking patterns into emergent structure
**Proposed rule:** Chief decides each stack until the sim (BOLO 101) fixes a format. The writer names the lower pattern and the upper pattern, then the scale each runs at. The writer feeds the lower cycle's change into the upper cycle as its want or its cost. Chief rules the stack in as a pattern entry.
**Why:** The source says small patterns stack, Pattern 2's change feeds the next want, and the entry format waits on BOLO 101.
**Lands in:** ssot_00_pattern_library, Open (provisional), as a "Stacking" subsection.

### C16 · ssot_00_pattern_library · no step-to-SOP mapping for the nine-step Command loop
**Proposed rule:** The Command maps the loop onto the SOP's four steps as follows. Steps 1 to 3 (Chief speaks, capture to the BOLO, recon) are RECON. Steps 4 and 5 (recs, one-word ruling) are ORDER. Steps 6 and 7 (build, script check) are EXECUTE. Steps 8 and 9 (publish, log) are CONSOLIDATE.
**Why:** The source lists the nine steps in that order and says the loop is the SOP's four steps seen as a pattern.
**Lands in:** ssot_00_pattern_library, Pattern 1, a "Maps to the SOP" table under the steps.

### C18 · ssot_00_variable_registry · the REL prefix has no variable beyond the example REL.relationship_type
**Proposed rule:** Chief decides each REL variable. The author fills all twelve Registry Format fields for it. The author checks first that no existing relational field already holds it: `T1.SOCIAL.knowledge_map`, `T3.FUNC.relational_roles` and `T2.WOUND.relational_refs`. Until Chief rules, REL stays a declared prefix with its one example.
**Why:** The registry already holds relational data in those three fields, so a new REL variable risks a duplicate.
**Lands in:** ssot_00_variable_registry, Domain Prefixes, a note under the `REL` row.

### C19 · ssot_00_variable_registry · no procedure for retiring a variable
**Proposed rule:** Chief rules each retirement. The author keeps the entry, marks it retired with the date and BOLO, and names any replacement. The author keeps an alias row for the old name. The author removes the variable from every Feeds line that lists it. Character records keep their data, and the author adds a version-history row.
**Why:** The `narrative_invariant` rename kept an alias row, and module retirement leaves data in character records.
**Lands in:** ssot_00_variable_registry, Registry Format, a "Retire a variable" subsection.

### C24 · ssot_01_medium_grammars · no procedure for running the BOLO 16 research pass
**Proposed rule:** Chief finds each source and attaches it in Zotero, then says "rescan Zotero". An MS reads the held source and writes sourced grammar for one scaffold medium (M6, M7 or M8). The author replaces the scaffold bullets, cites the source, and drops the "v1 scaffold" tag. A medium with no held source keeps its scaffold. ORANGE rows carry craft grammar only.
**Why:** The queue names Vernallis, short-form sources and PMV/HMV grammar, lists zero holdings, and says the scaffolds stand until the pass runs.
**Lands in:** ssot_01_medium_grammars, the "Acquisition/research queue (BOLO 16)" paragraph.

### C29 · ssot_01_spine_house_inventory · no rule for choosing a home level when two levels tie
**Proposed rule:** Chief decides each tie. Until he does, the author gives the file the lower level number as its home. The author lists the other tied level in the Also column.
**Why:** The source orders rows by level and keeps cross-level payload in Also, so a deterministic placement keeps the table sortable.
**Lands in:** ssot_01_spine_house_inventory, the opening paragraph, one sentence on ties.

### C30 · ssot_01_story_registry · no procedure for assigning a vignette's next ID number
**Proposed rule:** The author greps the registry and `_CANON_NODES/` for the highest `VG-<nnnn>` before minting. The author takes that number plus one, padded to four digits. The author never reuses a number, even for a dropped vignette.
**Why:** The source fixes the form `VG-<nnnn>`, and a grep for the highest id before minting is the Command's existing id rule (BVX collision, 10/4).
**Lands in:** ssot_01_story_registry, VIGNETTES, a bullet under "Intake".

### C31 · ssot_01_story_spine_comparative_tree · no procedure for adding a rival model to the rival map
**Proposed rule:** Chief rules each new rival in. The author adds one row with the four columns: Model, Holdings, What it actually models, Verdict vs the spine. The author lists only held library ids and marks a missing book as not held. The author adds a missing book to the acquisition gaps line. The verdict names the spine level where the model lands.
**Why:** The map is one row per model, and every rival is mapped onto the Dramatica spine as a lens.
**Lands in:** ssot_01_story_spine_comparative_tree, THE RIVAL MAP, a line under the acquisition gaps.

### C36 · ssot_01_three_check_pass · no row numbering rule past row 12
**Proposed rule:** The author numbers a new element 13 and counts up, in expansion-queue order. The element keeps one number across all three sweeps: F13, S13, A13. The author never renumbers a row.
**Why:** Chief struck and kept lines by number (F, S, A plus row), and each of the twelve elements holds the same number in all three sweeps.
**Lands in:** ssot_01_three_check_pass, NEXT, under the sweep expansion queue.

### C37 · ssot_01_touchstones_register · the check script's command-line form and output format are not given
**Proposed rule:** The author runs `python _tools/review/touchstone_check.py` from the repo root, with no arguments. The script prints `register ids: N | citations checked: M`, then one `MISSING TS x:y  path:line` per unknown id. It ends with `PASS` or `FAIL (n unregistered)`. It exits 0 on a pass and 1 on a fail.
**Why:** The script's own header and print statements state this form and output; the source cites only its path.
**Lands in:** ssot_01_touchstones_register, the script description in the source, mirrored in the tutorial's "Step 4: check the id".

### C40 · ssot_01_trope_register · no command-line steps for fetch.py or build_register.py
**Proposed rule:** The author runs `python _tools/tropes/fetch.py --domains` to pull the indexes. The script waits one second per request, skips slugs already cached, and stores no page bodies. PS batches write the keys to `_tools/bolostatus/work/89/keys.batch*.json`. The author then runs `python _tools/tropes/build_register.py` with no arguments. It writes `register.json` and `LAYERS.md` and prints the counts table.
**Why:** Both scripts' own docstrings give these commands and outputs, and the source lists them only under `sources:`.
**Lands in:** ssot_01_trope_register, a "Rebuild the register" section before the version history.

### C60 · ssot_02_l9_eros_synthesis · the synthesis method is shown only by its output, with no formal procedure
**Proposed rule:** The formal procedure is the nine steps already read from the output. Collect and ID the distills. Read the whole shelf against L9. Build the per-distill register. List patterns that two or more sources reach. Survey the trope side. Write proposed changes with cites and a rec. Treat queer and male-male desire as first-class. List open questions undecided. Mark every change provisional. Chief orders the pass and rules each change.
**Why:** The source's own section order and its "provisional until Chief rules" line are the method, and the how-to already reads them as steps.
**Lands in:** ssot_02_l9_eros_synthesis, a "Method" section before section 1.

### C77 · how_to_use_goon_room · the source does not say who reviews in _STAGED/
**Proposed rule:** Chief reviews everything in `_STAGED/`. The writer does not promote on the writer's own call. Nothing reaches `_CANON/` without Chief's ruling.
**Why:** The Command's rule is that lineage reads as canon only after Chief rules it in, as the vignette canon-status line says.
**Lands in:** how_to_use_goon_room, section "4. Weekly Review".

### C78 · how_to_use_goon_room · no promotion criteria and no review owner
**Proposed rule:** A passage qualifies when it carries `#canon-ready` and Chief rules it in. The writer checks it against the live Touchstones first. The writer then moves it to its home: a `#ssot-candidate` goes to an SSOT doc, and a `#auth-candidate` goes to `_AUTHORITATIVE/`. The writer adds a version-history row naming the date and the ruling.
**Why:** The source defines the tags and their targets, and Touchstones hold at every scale in the lattice.
**Lands in:** how_to_use_goon_room, section "4. Weekly Review", as numbered promotion steps.

### C84 · ssot_05_operations_pm_holdings_inventory · no named maintainer and no re-sweep trigger
**Proposed rule:** The Command keeps the inventory, and Chief owns it. The Command re-sweeps it when BOLO 25 (the standard PM flow) builds a step, and whenever a listed holding changes state. Chief decides any other re-sweep. The author verifies each path before listing it.
**Why:** The inventory was banked once on 2026-09-03 as a survey feeding BOLO 25, and the writing guide names "Chief; Claude keeps it" as owner.
**Lands in:** ssot_05_operations_pm_holdings_inventory, a "Keeping this inventory" paragraph after the opening finding.

### C88 · ssot_SSOT_CREATION · the emoji prefixes for _AUTHORITATIVE/ files and the name rules for 🎯 files are not stated
**Proposed rule:** The author prefixes story or project content in `_AUTHORITATIVE/` with 🎯. The author names it `🎯 auth_[ip]_[name].md`, in lowercase with underscores. Chief rules whether the existing ingests and reports that carry 📐 there move to 🎯 or keep 📐.
**Why:** The taxonomy gives 🎯 to story or project content, and the one existing 🎯 file reads `🎯 auth overexitout victoria midnight.md`.
**Lands in:** ssot_SSOT_CREATION, File Naming and Metadata, under the Emoji Taxonomy.

### C91 · ssot_ai_instruction_protocol · what the operator pastes and how the six categories map to folders are not stated
**Proposed rule:** The operator pastes the whole protocol file, then one raw concept, in a single message. The six categories map to folders as follows: epistemology to `00_EPISTEMOLOGY`, narrative_frameworks to `01_NARRATIVE_FRAMEWORKS`, character_systems to `02_CHARACTER_SYSTEMS`, plot_systems to `04_PLOT_SYSTEMS`, operations to `05_OPERATIONS`, style_guides to `06_STYLE_GUIDES`. Chief decides where content for domains 03, 07, 08 and 09 lands, because no category names them.
**Why:** The protocol's first step is "give the AI the protocol as its instruction set", and the six names match six existing `_SSOT` folders.
**Lands in:** ssot_ai_instruction_protocol, Phase 4 Execution Workflow, a "Start the run" paragraph and a category-to-folder table.

### C95 · ssot_06_2a_writing_guide · the dependency template has no field list
**Proposed rule:** The template's field list is the eight components in order: YAML frontmatter, H1 title, Table of Contents, Purpose, Core Methodology, Implementation, Examples, Version History. Its YAML keys are `type`, `category`, `version`, `last_updated`, `applies_to`, `status`, `purpose` and `dependencies`. Chief decides whether the five header fields (`reader`, `doc_type`, `owner`, `state`, `reviewed`) join the template now or at the schema pass.
**Why:** The template file already holds those components and keys, while the writing guide adds the header fields separately.
**Lands in:** ssot_06_2a_writing_guide, "The Flat-Syntax YAML Standard", a field list under the header-fields bullet.

### C99 · ssot_07_theme_system · no field-level steps for keying a trope to the rails
**Proposed rule:** The author opens the trope's record in `register.json`. The author reads its one-line `def`. The author sets `keys.theme` to the one rail (R1 to R4) whose debate the trope argues, or to null if it argues none. The author sets `conf` to low when `def` is undefined. The author runs `build_register.py`. Chief decides any trope that needs two rails.
**Why:** The register record holds "one key per domain", and the register says most unkeyed theme tropes argue none of the four rails.
**Lands in:** ssot_07_theme_system, TROPES, replacing "one or more rails" in the how-to with this procedure.
