---
rung: handbook · NASA four, ruled 2026-09-24 (BOLO 79)
---

# CMO/CMANO Window Study → Rules for the Story Workspace

Scope: Command: Modern Operations (CMO, 2021) and predecessor CMANO (2013), plus Hearts of Iron IV, Gary Grigsby's War in the East (GGWE), and Shadow Empire as counter-examples — a model for the story workspace's window grammar: one app, three lenses (fabula timeline · trope graph · told order) over a plot system, plus character windows. Confidence HIGH/MEDIUM/LOW per claim. Extends, does not repeat, [CK3-IA-STUDY.md](CK3-IA-STUDY.md) R12 (outliner), R14 (side-by-side panels), "no modal dead-ends." Study date 2026-09-24.

## Executive summary

1. CMO's stated philosophy: present "a huge amount of information" in "discrete, manageable chunks," favoring "scalability, usability, expandability and maintainability" over a trendy but inflexible UI — the war-game density Chief wants is deliberate, not an accident [HIGH — dev blog].
2. Secondary windows persist: last position/size saved to an ini file, restored on relaunch, one "Reset positions" button returns to default [HIGH — manual].
3. One selection updates every open panel: the Unit Status Panel, its weapons summary, and an inline hyperlink that jumps into the mission editor pre-selected [HIGH — manual].
4. The message log is one filtered stream, not toasts: category-colored, unread-highlighted, click-to-recenter, short-lived on-map balloon, raw-text fallback [HIGH — dev blog, Wargamer].
5. Doctrine/ROE is a docked, tabbed window with load/save XML templates — not a blocking modal stack [HIGH/MEDIUM].
6. The 2019–21 rewrite fixed real complaints (slow map engine, "looks like MS Office," message spam, DPI scaling) with a dark reskin, full-screen toggle, rebuilt log, time-stepped sim — but 1440p+ text-size complaints persist into 2025 [HIGH/MEDIUM].
7. HOI4 is the caution against feature growth without shared grammar: "uninformative and yet cluttered," inconsistent panel design per mechanic, tooltips clipped off-screen [HIGH].
8. Shadow Empire and GGWE are the caution against density without hierarchy: "famously dense," "obscure icons and buried modifiers," most learning happens outside the game [HIGH].
9. Hover previews before commit: CMO's "mouse preview mode" ghosts a hovered, non-selected unit's datablock — inspect before select, same contract as CK3's tooltip-before-sheet [HIGH].
10. Do not copy: literal floating desktop windows (no mobile analog), timer-only pacing with no manual override, letting every new mechanic invent its own panel shape.

## 1. The frame — multi-window doctrine, not single-window

CMO kept its multi-window model through the rewrite rather than collapsing to one HUD: the goal is information in "discrete, manageable chunks" [HIGH — command.matrixgames.com/?p=4954]. Main map plus secondary windows (Unit Status, Message Log, Doctrine/ROE, Mission Editor, Recorder, Formation Editor) move and resize independently but each "remember[s] last position and size… saved on the Command.ini file," with one "Reset positions of secondary windows" button in Game Options [HIGH — manual addendum]. Secondary windows "minimize/maximize together with the main game window" and no longer "visually block other program windows"; they close uniformly "by pressing Esc, or their assigned function key (F2 etc.)" [HIGH]. The right info column "can now be tucked out of the way," trading panel space for map space [HIGH — dev blog]. The frame adapts to the OS: "Command handles the 125% desktop font setting… much more gracefully, and adjusts the dimensions of the right-column panels to compensate" [HIGH — patch notes].

## 2. Selection linking — one click, every panel

Selecting a unit propagates: Unit Status "now includes a weapons summary panel for selected unit/group" [HIGH — manual]. Its mission description "is now a hyperlink. Clicking it brings up the mission editor window and selects this mission" — a cross-panel jump from inline text [HIGH — manual]. The formation editor "give[s] focus" to itself "if it is visible when selecting one of group members" — an open panel snaps to the new selection [HIGH]. Before commit, "mouse preview mode" ghosts a hovered-but-unselected unit's datablock [HIGH — patch notes]. Wargamer on the predecessor's failure: "this used to drive me nuts in CMANO where unit selection involved multiple clicks or zooming"; CMO's list-based disambiguation fixed it [HIGH]. Reference points extend the pattern to locations: selecting one or more "brings the map camera to their geographic center" [HIGH/MEDIUM].

## 3. The message/event log — a filtered stream

"Message Log 2.0" answers information overload with four moves on the same event model, not a redesign: per-unit aggregation "declutters the main message log"; a ~10-second on-map balloon surfaces the event at its location; type-based color-coding and unread highlighting organize the backlog; clicking a message auto-centers the map [HIGH — dev blog]. Wargamer confirms: messages sort by category with a toggle to "Raw text view," balloons "tied to the map location," useful for new-contact events [HIGH]. Friction persists: a v1.08 fix addressed the log showing entries "no longer in the simulation's in-memory log" [MEDIUM]; a player who popped the log into its own window got "just a window with just a close button" — the floating variant lost the docked variant's filter chrome [MEDIUM]. Lesson: filters are a property of the panel, not the event data; a spun-off view must carry them.

## 4. Doctrine/ROE and other dialogs — docked, tabbed, not modal

Doctrine/ROE is tabbed ("General," etc.) with load/save of XML templates in the same window [HIGH/MEDIUM]. It sits beside the map rather than blocking it, per CMO's non-modal convention (Esc or an F-key always returns you, §1). Function keys route straight into sub-panels: F2 Throttle+Altitude, F3 Plot Course, F9 Sensors, Ctrl+F9 Unit/Group Doctrine [MEDIUM — controls mirror, not primary-fetched]. The Recorder window is the deliberate exception to "dismissible": it "is always on-top and visible on taskbar" [HIGH] — small, single-purpose, pinned because losing it mid-recording costs more than screen space. Wargamer flags one icon near-miss: the record button's red circle reads as a stop control, and "several times in the heat of battle I found myself hitting it in the hope of stopping the simulation" [HIGH].

## 5. What the rewrite fixed, and what still breaks

The pre-rewrite complaint was performance-shaped: "its user interface, and primarily the map engine, felt slow and clunky," answered with "a complete re-write," not tweaks [HIGH]. The second was tonal: it read as "more like a 'traditional' business application like MS Office, rather than a bonafide game" [HIGH], echoed on Steam: "it looks more like an Office application than a game!" [HIGH]. CMO answered with a dark reskin (rebuilding "major elements," not recoloring) while keeping layout familiar "so existing players will feel right at home" [HIGH], plus a full-screen toggle that "persists along with the other map settings" [HIGH]. A subtler fix: "time-stepped execution" against the "runaway sim" problem (high acceleration plus muted pop-ups outrunning attention), solved with preset run intervals (15 s / 1 / 5 / 15 min) that auto-pause [HIGH]. What persists: 1440p+ users still report text too small and clipped button labels; a once-viable workaround "reportedly doesn't work in the 2025 version" [MEDIUM]. The rewrite fixed structure; scale-independent legibility is still open.

## 6. Counter-examples: sprawl without grammar, density without hierarchy

**HOI4** shows panels outrunning a shared visual language: "so uninformative and yet so cluttered," "muddy washed out colors" hinder parsing state, tooltips clip "beyond the screen's right or bottom edge" on the National Focus and Technology windows [HIGH]. Root cause is architectural: "different panel designs for various countries' mechanics in inconsistent places" — each new system got its own layout instead of reusing one [HIGH].

**Shadow Empire** and **GGWE** show density without a legibility ladder. Shadow Empire is "exceptionally dense," "frustratingly inconsistent," "struggles to show how the systems interact," leaning on "obscure icons and buried modifiers" [HIGH]. GGWE is "composed of a map, counters, reports, numbers, tables, pop-ups, and spreadsheets" [HIGH], its manual runs "dense blocks of text" with no enumerated breaks [MEDIUM], and it "lacks a guided, in-game tutorial," forcing play in one window against a paper tutorial in another [HIGH]. Both prove dense tables need a "why" tooltip and progressive disclosure, not just more panels.

## 7. Translation to the story workspace

**The frame.**
- W1. One fixed frame: the fabula timeline is the center map, always present; every panel — trope graph, told-order pane, character window, term store, event log — docks to a fixed slot (left rail, right rail, bottom drawer) around it. Never a floating window over the timeline. From CMO's window model (§1) filtered through this project's "no modal dead-ends" rule.
- W2. Panels remember position and open/closed state per saved layout (W7); one visible "reset to default" action undoes drift. From CMO's ini persistence and single reset button (§1).
- W3. Every panel closes two ways only: Escape, or its own dock-rail toggle — never only a corner X. From CMO's uniform Esc/F-key close (§1).

**Shared selection.**
- W4. One selection, three lenses: clicking a node in any lens sets one shared selection; all three lenses highlight it and the character window (if open) refreshes to it — the Unit-Status-plus-weapons-summary pattern (§2), not three selections to keep in sync.
- W5. Inline references are real jumps: a "used in Chapter 4" mention is a hyperlink that opens/selects the target in its own dock slot, mirroring CMO's mission-description hyperlink (§2) — not a tooltip alone, not a full navigation away.
- W6. Hover previews before selection: hovering a node shows a compact ghosted card before a click commits the full panel — CMO's mouse-preview mode (§2), the same contract as this project's CK3-derived tooltip rule.

**The event log.**
- W7. One event/change log, filtered, not per-lens: every edit, trope tag, or reorder writes to one stream; filter chips (lens, character, change type) narrow it client-side, with a raw/unfiltered fallback — CMO's Message Log 2.0 (§3).
- W8. A log row jump-centers its target lens and opens the right dock panel in one click, CMO's balloon-click (§3). If a filtered view is ever popped into its own window, the popout must carry its active filters — CMO's docked-vs-floating log divergence (§3) is the warning, not the model.

**Density and doctrine-style editors.**
- W9. Dense tables (a full character stat block, a trope-frequency matrix) live inside a panel or a drill-down, never inline in the timeline — GGWE/Shadow Empire's lesson (§6) as a boundary, not an ambition.
- W10. Every table cell a reader might doubt gets a source breakdown on hover or click, extending this project's "why" tooltip rule to numeric/graph data, the way CMO's doctrine editor exposes its ROE templates instead of hiding the logic.
- W11. Doctrine-style edit surfaces (an outliner rule, a trope definition) open as a docked, tabbed panel beside the timeline, never a blocking modal stack — CMO's Doctrine/ROE window (§4), reinforcing this project's standing "no modal dead-ends" rule.
- W12. One panel grammar for every panel type, present and future: a new lens or table reuses the same dock/tab/pin/close rules as the first three — the HOI4 failure (§6) named as the thing this rule prevents.

**Phone-width fallback (390 px).**
- W13. Below a fixed breakpoint, dock rails collapse: one lens active at a time via a bottom tab switcher (fabula / trope / told), character window and event log reachable as a swipe-up sheet — CMO's floating-window model has no mobile analog and must not be force-fit (§10).
- W14. The fabula timeline is the default lens on cold load at any width, matching W1 — every panel is reached from it, never the reverse.

**Do not copy.**
- Literal floating, overlapping desktop windows — no mobile equivalent, and the source community still asks for bigger text after two rewrites.
- Timer-only pacing (CMO's runaway-sim fix runs on presets) without a manual override — this workspace's edits are not a live sim and should never batch-lock output.
- Icon-only controls that collide with a learned convention elsewhere (CMO's record-button red circle read as "stop") — label ambiguous controls here, don't rely on icon alone.
- Letting each new mechanic invent its own panel shape (HOI4's per-country panels) — W12 exists to block exactly this.

## Open questions for Chief

1. Selection state: does the outliner (already ruled: one outliner, R12) *own* the shared selection, or does a separate selection bus feed the outliner and all three lenses equally? **Rec:** a thin selection bus the outliner subscribes to like everything else — keeps the outliner a view, not the source of truth.
2. Event log scope: one shared stream across all three lenses (§3/W7), or a per-lens log a "combined view" merges? **Rec:** one shared stream with filter chips — three logs repeats CMO's docked-vs-floating divergence bug structurally.
3. Saved layouts: per-viewer browser storage (dies with the browser/profile) or a workspace capability that follows Chief across machines? **Rec:** localStorage for now, single-user tool — revisit only if Chief works from more than one machine.
4. Character windows: pinned dock panels beside the graph, or a full-screen sheet like CK3's character window? **Rec:** dock panel — a full-screen sheet breaks W4's "every lens stays visible" contract.
5. Phone fallback default: fabula timeline first (W14) always, or remember the last lens from desktop? **Rec:** always fabula timeline on cold load; remember last lens only within a session — a stale trope-graph deep link on a phone with no timeline context is disorienting.

## Sources

- CMO, "User interface and experience, Part I" (2019-09-30): https://command.matrixgames.com/?p=4954
- CMO, "Manual Addendum: User Interface": https://command.matrixgames.com/?page_id=2697
- CMO manual (PDF): https://ftp.matrixgames.com/pub/CommandModernOperations/CMO%20manual%20EBOOK.pdf
- Wargamer, CMO review: https://www.wargamer.com/command-modern-operations/review
- CMO patch notes via SteamDB: https://steamdb.info/app/1076160/patchnotes/ ; v1.08 log fix: https://steamdb.info/patchnotes/18808439/
- Steam Community, font-size thread: https://steamcommunity.com/app/1076160/discussions/0/3776868552305445632/
- Matrix forum, log-in-separate-window thread: http://www.matrixgames.com/forums/viewtopic.php?t=356191
- CMANO (Wikipedia): https://en.wikipedia.org/wiki/Command:_Modern_Air_Naval_Operations
- HOI4, "the UI is HORRIBLE" (Paradox forum): https://forum.paradoxplaza.com/forum/threads/hoi4-as-a-beginner-the-ui-is-horrible.1443216/
- HOI4, interface/scaling discussions: https://steamcommunity.com/app/394360/discussions/0/834997894160328529/ ; https://steamcommunity.com/app/394360/discussions/0/591765454927728587/
- PC Gamer, Shadow Empire review: https://www.pcgamer.com/shadow-empire-review/
- Turn Based Lovers, Shadow Empire review: https://turnbasedlovers.com/review/shadow-empire/
- Battle Leader, GGWE review: https://battleleader.com/gary-grigsbys-war-in-the-east-a-review/
- GGWE (Wikipedia): https://en.wikipedia.org/wiki/Gary_Grigsby's_War_in_the_East

## Blocked / Unverified

- Matrix/Steam forum threads read only via search-result excerpts, not full primary fetch; MEDIUM quotes come from those excerpts.
- The F2/F3/F9/Ctrl+F9 hotkey table came from a third-party controls mirror, not the primary manual — MEDIUM.
- No developer source compares CMO's window model to a dockable-panel framework (an unrelated Java "Modern Docking" library surfaced in search and is not part of CMO).
- Shadow Empire's and GGWE's developer commentary on interface intent was not located; both sections rest on reviewer accounts.
- HOI4 developer diaries on UI rationale were not searched this pass — the study covers community criticism only, since the order named CMO/CMANO as primary and the rest as sharpening counter-examples.
