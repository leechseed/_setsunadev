# CK3 Information Architecture Study → Rules for the MCDP Doctrine Browser

Scope: Crusader Kings III (Paradox, 2020) and its 2021–2025 interface updates, as a model for a single-reader, single-page browser of eleven USMC publications (MCDP 1–8 one-sheets, nine fixed sections each, shared glossary register). Confidence marked HIGH / MEDIUM / LOW per claim. Study date 2026-09-06.

## Executive summary

1. Every glossary term, wherever it appears, is a live link: hover opens a tooltip, the tooltip's own terms open further tooltips, and a tooltip locks in place by a short timer (default about two seconds) or by an explicit key — the CK3 "tooltips in tooltips" contract (DD #16).
2. Cap nesting at two or three levels, then hand off to the full glossary entry; CK3's chain is technically unbounded and Paradox had to patch infinite recursion out of it.
3. Use one semantic color grammar and nothing else: light-blue = linked concept, green = positive, red = negative, muted italic = help, bold/large = title. CK3 encodes these as text-format tags, so meaning travels with the string, not the widget.
4. Any number the reader might doubt gets a "why" tooltip: a list of icon + signed, colored value + source, summing to the shown total.
5. Lay each publication out as a character sheet: an identity block (portrait, name, title line), a traits row of square badges, a skills row of icon + value, then tabs for depth.
6. Navigate with two instruments, as CK3 does: a persistent outliner (pinned, always visible, hotkeyed) and an encyclopedia index (categorized, searchable, with search history and back/forward).
7. Hover inspects, left-click opens, right-click acts; Esc closes tooltips and panels; B/Backspace goes back; a pin key keeps a panel open.
8. No modal dead-ends: panels open beside content and stack, never over it as blocking dialogs, and every panel has a history.
9. Disclose progressively and cap overflow — CK3's tutorial team cut 67 text boxes to a third, and its war tooltip lists at most six names then "x more".
10. Do not copy the parchment-and-gold skin under body text, the game's map-first density inside the reading column, or timer-only tooltip locking without keyboard access.

## 1. Nested tooltips and game concepts

**Concept links.** Dev Diary #16 (3 March 2020, by "Matthew", a programmer): "One of the new features in CK3 is Tooltips in Tooltips, the aim of this is that relevant information can just be a mouse move away whenever you see blue highlighted text in game." [HIGH — forum thread; verbatim via search excerpts, page itself behind a browser check]. Any string becomes a concept link with `[concept_key|E]` (or `[Concept('key','custom wording')|E]` to relabel it), and the `#E` tag renders "as a game concept, light blue" [HIGH — CK3 wiki, Localization]. Linking is a property of the text layer, so the same markup works in tooltips, windows, events, and encyclopedia entries.

**Nesting.** "The behavior is nesting so you can get more and more information, so all the blue highlighted Game Concepts in tooltips can also be highlighted to explain what a Ruler is and then what a Title itself is etc." [HIGH — DD #16]. Depth is not capped by design — PCGamesN: "You can keep digging through the game's knowledgebase indefinitely" [HIGH]. Patch 1.1 had to fix encyclopedia links inside tooltips "to prevent infinite recursion" [HIGH — wiki]. Philip Ardeljan's write-up puts the sweet spot at "2 or 3 nested tooltips" and flags the cursor-precision failure ("move your cursor 1 pixel outside of the bounds") and the need for keyboard access on the web [HIGH].

**Locking.** DD #16: "There are two different modes for Tooltips in Tooltips: timer lock and action lock with the former being the default… either a timer which is configured in the settings menu or by clicking the middle mouse button to manually lock them in place." [HIGH]. By release: Timer Lock, Action Lock (middle mouse), and Mouse Tendency (locks until the cursor changes direction), plus four delay sliders — appear, lock, unlock, and when another tooltip is open [HIGH — GameWatcher]. A developer reply on Steam puts the default at hover "for two seconds" [MEDIUM — via search excerpt; page rendered only its shell]. Esc "close[s] most screens; close[s] tooltips" [HIGH — wiki Keyboard shortcuts].

**Visual grammar.** Concept links: light blue (`#E`). Positive `#P` green; negative `#N` red; `#help` "blue gray and italic"; `#T` "title, bold and large"; `#weak` "darker and italic"; `#warning` red italic; `@icon_name!` embeds an inline icon before a value [HIGH — wiki Localization; mirrored at jesec/ck3-modding-wiki]. Patch 1.9 "Added a lot of prefix icons to modifiers" [HIGH]. Tooltip anatomy — bold title line, body description, then icon-led modifier rows — follows from those tags but was not confirmed on a primary page [LOW]. Styles live in `gui/preload/textformatting.gui` [HIGH — wiki Interface]; hex values not retrievable.

**Link to the encyclopedia.** Tooltips carry encyclopedia links [HIGH — Patch 1.1], so the chain is link → tooltip → nested tooltip → full entry.

## 2. The Encyclopedia

**Arrival.** Hotkey F10 [HIGH — wiki Keyboard shortcuts]; a book-shaped button in the lower-right bottom bar next to settings and search [HIGH — gamepressure interface guide]; and from any tooltip's encyclopedia link [HIGH — Patch 1.1].

**Contents and structure.** DD #16: "The Encyclopedia includes information on Game Concepts, recaps of the guided tutorial and reactive advice, and the various types of terrains and traits present in the game and their effects." It is "fully searchable" with "a history of searches… used to scroll back and forward between searches," and pages are "automatically generated by the game from script files" [HIGH — verbatim from DD #16 via search excerpt]. GameWatcher: it "also supports highlighted words" — entries cross-link with the same concept markup [HIGH]. Launch categories: Game Concepts, tutorial lessons, terrain, traits, unit types; later patches add entries as mechanics arrive ("Level of Devotion Impact is now a game concept," 1.9) [HIGH]. Layout (category list, entry pane, search field, back/forward) is inferred, not confirmed visually [LOW].

## 3. The character window and other panels

**Character window** (lower-left, opened by left-clicking any portrait) [HIGH — gamepressure]. Order top to bottom: portrait with lifestyle/stress indicators; name, nickname, age, health; traits as "a row of square icons situated beneath their name and above their skills" [HIGH — GameWatcher]; five skills and prowess, icon + number, fixed order Diplomacy, Martial, Stewardship, Intrigue, Learning, Prowess [HIGH — wiki Attributes]; religion and culture; dynasty coat of arms; primary title and government; domain limit; lists of titles held and claims; then four tabs — family, social relations, court, vassals — of grouped portraits [HIGH — gamepressure]. Right-clicking a portrait opens the interaction ("Diplomacy") menu [HIGH — wiki Beginner's guide]. Opinion is a signed number whose tooltip lists each modifier with its value ("+10 Dynasty Legacy 'Glory'", "-1 ~ -1000 Tyranny") [HIGH — wiki Opinion]. Hovering a portrait first gives a compact character tooltip (1.5: council and court positions; 1.9: background, "to give a quick indication if a character is traveling") [HIGH] — a card before the sheet.

**Right-side menu and detail area.** Seven icons — Realm, Military, Council, Court, Intrigue, Factions, Decisions — with the outliner icon above them [HIGH — gamepressure]; the same screens sit on F1–F8 [HIGH — wiki]. The console team kept the PC model of "flicking between menus, the map and popups" while "avoiding the use of lots of fullscreen menus," adding "switching focus" between open elements [HIGH — Console DD #3, 2022-03-23].

**Back behavior and pinning.** B, Backspace, or Mouse 4 = back; N or Mouse 5 = forward; Alt+Q pins/unpins a window; Esc closes most screens [HIGH — wiki Keyboard shortcuts]. 1.5: "Decisions now support a two page setup" — paging inside a panel, not a second window [HIGH].

**Outliner.** A list of "all your armies, counties and characters that you have marked as interesting," every row interactive; Q toggles it [HIGH — gamepressure; wiki]. 1.5: hovering a holding highlights it in the outliner; 1.9: pinned rows show status icons and the outliner remembers its settings [HIGH].

**Alerts and Current Situation.** Top bar: crucial tasks are "diamond icons along the top of the screen," lesser ones "grouped into a cloverleaf shaped icon with a number inside it" [HIGH — wiki Beginner's guide]. The Current Situation widget is a "colored numbered icon" of "situational opportunities" [HIGH — gamepressure]; Tab opens "Issues / action list (suggestions based on your situation)" [HIGH — wiki]. Present by 1.3; rebuilt in 1.9 so "All entries now include icons" [HIGH].

**Progressive disclosure.** The 2024 tutorial rework (Valeska Martins, UX Design Lead; Ellinor Zetterman) cut 67 text boxes to about a third and chose to "gradually reveal information in the character panel" [HIGH — Game Developer, 2024-09-12].

## 4. Visual and typographic system

**Type.** Vanilla font files: `GitanLatin` (Regular/Bold/Italic/Bold-Italic) for UI and body text; `Fondamento-Regular` for titles; `Paradox_King_Script` for the map and logo [MEDIUM — Workshop "Easy-to-Read Fonts" via search excerpt; Nexus "Lord's UI Enhancements" names "the general content font 'Gitan'"; wiki Fonts page confirms King Script as "the map's font"]. Three faces, three jobs: a readable serif for everything dense, a calligraphic face for names only, a script face for the map.

**Palette.** Semantic text colors are the documented constant (blue link, green/red, blue-gray help, white value) [HIGH]. Panels are dark: readability mods sell "better contrast against the dark background" [MEDIUM]. Paper/parchment lives on the map and illustrated surfaces (DD #177, August 2025, Art Director Petter Lundh: a new "illustrated paper map") [MEDIUM]. Gold is the accent for frames and emphasis [LOW — not confirmed by a primary page]. Patch 1.9 added a "HUD Skin Selector" to swap cultural skins [HIGH]: the frame is a skin, the grammar underneath is fixed.

**Icons.** Every skill, resource, and modifier has an icon; `@icon!` embeds them in text; 1.9 "Assigned icons to all interactions"; 1.15 added scheme-type indicators and a "Pulsating glow" on clickable capstone traits [HIGH — wiki patch pages]. Contrast failures are patched as bugs ("no longer use white text on a light background", 1.9) [HIGH].

**Hierarchy without heading levels.** Weight, size and color tags; tabs; grouped portrait grids; paging; and hard caps with overflow ("at most 6 people on each side of the war, with the overflow listed as 'x more allies'", 1.5) [HIGH].

## 5. Interaction conventions

- Hover = inspect; left-click = open; right-click = act ("Right-clicking always goes to the county owner"; right-click portrait → interaction menu) [HIGH].
- Middle mouse = lock/unlock tooltip in Action Lock; Esc closes tooltips and screens [HIGH].
- Keyboard: F1–F10 main screens, C character finder, V title finder, Tab issues list, Q outliner, Home to capital, Alt+Q pin, B/N back/forward [HIGH].
- No modal dead-ends: side panels, focus switching, pinning, history [HIGH — Console DD #3; wiki].
- "Why" on every number: opinion breakdowns; a loot tooltip fixed to add the "missing breakdown entry … to match end value" (1.5); scheme odds in the interaction menu (1.15); legitimacy tooltips explaining obedience (1.16.2) [HIGH]. PC Gamer: the game "is much better at showing how everything is connected" [MEDIUM — page truncated].

## 6. Translation to the doctrine browser

**Terms (from §1).**
- R1. Render every glossary term as a light-blue link wherever it occurs — body, table cell, quote, tooltip. Derives from `[concept|E]`: linking belongs to the text layer.
- R2. Hover opens a tooltip: bold term, one-paragraph definition, then a row list of "appears in: MCDP n §section" with the publication's icon. Derives from the concept tooltip and the prefix-icon rule.
- R3. Terms inside a tooltip open a second tooltip; stop at depth 3 and show a "Open in glossary →" link instead. Derives from nesting plus the 1.1 recursion fix and Ardeljan's 2–3 ceiling.
- R4. Lock after ~1.5 s hover or on Space/Enter; Esc dismisses the whole stack; focus-visible keyboard path for every link. Derives from Timer/Action Lock and Esc.
- R5. Cross-reference tooltip ("this term as MCDP 1 uses it vs MCDP 5") is a breakdown list: icon + publication + one line, never prose.

**The sheet (from §3).**
- R6. Identity block = Core Thesis: a monogram (1, 1-1 … 8) as the portrait; title as the name line; thesis as the one-sentence subtitle; edition/date as the "age/health" line.
- R7. Traits row = Invariants: square badges beneath the title, each with a tooltip; badge color by kind (principle / constraint / warning).
- R8. Skills row = Heuristics table: fixed-order icon + short label + a one-word value; hover gives the "why" (source paragraph, related terms, contrary case).
- R9. Tabs = Core Concepts | Key Vocabulary | Notable Quotes | Application — the family/relations/court/vassals analog; Key Vocabulary is the glossary filtered to this publication, like traits scoped to a character.
- R10. What Doesn't Work = the red-modifier list; Quick Self-Check = a green/red checklist with a signed count at the top and the breakdown on hover.
- R11. Cap lists at six rows with "x more" and page long tabs rather than spawning a second panel.

**Navigation (from §2–3).**
- R12. Outliner: a persistent right-rail strip of the eleven sheets with Alt+1…Alt+0/– hotkeys, plus a pin area for terms and sections in current use; it remembers state.
- R13. Encyclopedia index: the glossary register with a category rail (e.g., Nature of War / Command / Planning / Logistics / Intelligence / Campaigning / Tactics, as CK3 splits Character/Realm/Religion/War), a search field, search history, B/Backspace back, N forward. Both instruments, not one.
- R14. Sheets open in a left panel, glossary entries in a right panel, side by side; nothing opens over the reading column.

**Cross-references.**
- R15. Every term shows its publication icon before the link when cited outside its home sheet; every sheet ends with a "Cited by" breakdown list.
- R16. Hovering a term highlights its row in the outliner's pin list (Patch 1.5 holding→outliner highlight).

**Palette and type (from §4).**
- R17. Keep the semantic set exactly — blue link, green positive, red negative, blue-gray italic help, bold-large title — on a neutral, high-contrast ground; light or dark, choose one and pick the tones so the four colors pass contrast in the reading column.
- R18. Three faces, three jobs: a humanist serif for body (Gitan Latin's role), a display serif for sheet titles only (Fondamento's role), a monospace for section codes and citations (King Script's map role). No script face.
- R19. One accent, one hairline: a single warm accent line for the active sheet/tab; no ornamental frames.

**Do not copy.**
- Parchment texture or gold filigree under body text; CK3 puts paper on the map, not on the numbers.
- Game density in the reading column: hold a 65–75 character measure; density belongs in tooltips and the rails.
- Timer-only locking, unbounded nesting, cultural HUD skins, toasts, and the map-first layout.

## 7. Reconcile with the Lattice Navigator

- The Navigator's ~110-term codex and this glossary register: one store with two views, or two stores? If one, which side's term IDs win, and does the Death Stranding chrome survive R17–R19?
- The Navigator is a lattice (graph-first); this app is a sheet-first reader with an encyclopedia. Is the lattice the R13 index, the R12 outliner, or a third panel — and can the reader lose one without losing the other?
- Both apps will implement nested tooltips. Which one owns the tooltip component, depth cap, and lock timing so a term behaves identically in either?

## Sources

- CK3 Dev Diary #16 (forum, 2020-03-03): https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-16-tutorials-and-tooltips-and-encyclopedias-oh-my.1345581/ — mirrors: https://store.steampowered.com/news/app/1158310/view/1719750490053071870 ; https://www.crusaderkings.com/en/pc/news/dev-diary-16-tutorials-and-tooltips-and-encyclopedias-oh-my
- CK3 wiki, Localization (concept links, format tags): https://ck3.paradoxwikis.com/Localization — mirror: https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Localization.md
- CK3 wiki, Keyboard shortcuts: https://ck3.paradoxwikis.com/Keyboard_shortcuts
- CK3 wiki, Interface (UI file structure, textformatting.gui): https://ck3.paradoxwikis.com/Interface
- CK3 wiki, Beginner's guide: https://ck3.paradoxwikis.com/Beginner%27s_guide
- CK3 wiki, Attributes: https://ck3.paradoxwikis.com/Attributes ; Opinion: https://ck3.paradoxwikis.com/Opinion ; Fonts: https://ck3.paradoxwikis.com/index.php?title=Fonts ; Category:Game concepts: https://ck3.paradoxwikis.com/Category:Game_concepts
- CK3 wiki patch notes: 1.1 https://ck3.paradoxwikis.com/Patch_1.1 ; 1.5 https://ck3.paradoxwikis.com/Patch_1.5 ; 1.9 https://ck3.paradoxwikis.com/Patch_1.9 ; 1.15 https://ck3.paradoxwikis.com/Patch_1.15 ; 1.16.X https://ck3.paradoxwikis.com/Patch_1.16.X ; 1.3 https://ck3.paradoxwikis.com/Patch_1.3
- GameWatcher, new-player experience (tooltip modes, sliders, encyclopedia): https://www.gamewatcher.com/news/crusader-kings-3-tutorials-highlighted-text-encyclopedia
- GameWatcher, traits guide (traits row placement): https://www.gamewatcher.com/crusader-kings-3-traits
- gamepressure, Interface guide: https://www.gamepressure.com/crusader-kings-3/interface-description/z2f0f6
- Game Developer, "Refreshing the Crusader Kings III tutorial mode through optimized UX" (2024-09-12): https://www.gamedeveloper.com/design/deep-dive-refreshing-the-crusader-kings-iii-tutorial-mode-through-optimized-ux
- Console Dev Diary #3, UI/UX and Controls (2022-03-23): https://www.paradoxinteractive.com/games/crusader-kings-iii/news/ck3-console-dev-diary-3-uiux-and-controls
- Philip Ardeljan, "Tooltips in tooltips": https://philip.design/blog/tooltips-in-tooltips/
- PCGamesN on Victoria 3 adopting CK3's tooltips: https://www.pcgamesn.com/victoria-3/nested-tooltip-system
- PC Gamer review: https://www.pcgamer.com/crusader-kings-3-review/
- Steam discussion with developer reply on tooltip defaults: https://steamcommunity.com/app/1158310/discussions/0/4376911779069618339/
- Steam Workshop "Easy-to-Read Fonts" (vanilla font roles): https://steamcommunity.com/sharedfiles/filedetails/?id=2918491863 ; Nexus "The Lord's UI Enhancements" (Gitan): https://www.nexusmods.com/crusaderkings3/mods/2 ; Steam Workshop "Brighter Text Colors": https://steamcommunity.com/sharedfiles/filedetails/?id=2234245906
- Dev Diary #177 "A Fresh Coat of Paint" (2025-08-12, map/paper art): https://store.steampowered.com/news/app/1158310/view/509588190910219026
- Petter Lundh, CK3 UI (ArtStation): https://www.artstation.com/artwork/WmKNaN ; ArtStation Magazine CK3 Art Blast: https://magazine.artstation.com/2023/09/paradox-interactive-crusader-kings-iii-art-blast/

## Blocked / Unverified

- forum.paradoxplaza.com (DD #16, DD #7, DD #178, DD #192, Console DD #3): returns "Validating browser" — text recovered only via search excerpts.
- Steam news/community announcement mirrors of DD #16, #177, #192: fetch returned page chrome only.
- paradoxinteractive.com DD #16 redirect: resolves to a news listing, not the article.
- ArtStation (Petter Lundh UI page) and ArtStation Magazine: HTTP 403. No primary statement of panel colors, gold usage, or frame treatment obtained — palette beyond the text-color tags is MEDIUM/LOW.
- web.archive.org: not fetchable by this tool.
- Steam Workshop pages: HTTP 429 / shell only; font roles rest on search excerpts (MEDIUM).
- Nexus Mods, smods, devtrackers.gg, Google Fonts specimen: 403 or empty.
- Game UI Database and interface-in-game.com: no CK3 entry surfaced in domain-restricted search; gameuidatabase.com returned 403 on direct fetch.
- No GDC or conference talk on CK3 UI was found; the Game Developer deep dive is the nearest designer-authored source.
- Not verified: exact hex values in textformatting.gui; in-game encyclopedia category list beyond DD #16's enumeration; tooltip header/body structure (LOW); default lock delay of two seconds (MEDIUM).
- DD #178 "A Vision in Gold" is about Coronations, not UI; DD #177 is about map art, not panels — both checked and excluded from UI claims.
