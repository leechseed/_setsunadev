---
rung: handbook · NASA four, ruled 2026-09-24 (BOLO 79)
---

# Dwarf Fortress Legends Mode Study → Rules for the Story Workspace's Fabula Lens

Scope: Dwarf Fortress Legends mode, classic (pre-2022 text-menu) and Steam/Premium (2022–, "New Legends Mode") editions, plus the community tools built to replace its browsing — Legends Viewer, LegendsViewer-Next, Legends Browser/2 — as a model for browsing a generated world's history. Caves of Qud's sultan-history generator sharpens the provenance point in §5. Confidence marked HIGH/MEDIUM/LOW. Study date 2026-09-24.

## Executive summary

1. Legends mode has one browsable unit — the **historical event** — and four doors into it: figure, site, civilization/entity, era ("Age of…"); every other view is that same event list re-sorted [HIGH].
2. An event is a one-sentence record, not a scene: typed fields (event type, year, participants, place, cause) rendered to prose at display time, not stored free text [HIGH — structural; literal wording unverified, see Blocked].
3. Figures, sites, and events cross-link by shared identity — a figure's page lists every event it's in; a site's page lists every event that happened there. Browsing is following an event's own participant list, not searching [HIGH].
4. Eras are named for whichever power dominates ("Age of Myth," "Age of Dwarves," ordinals on repeat like "Third Age of Myth"); opening an era shows "a list of all historical events in chronological order" for that span [HIGH — DF wiki].
5. Vanilla browsing is real but thin: text lists, no map-linked timeline, no cross-filter, an XML export the game itself warns can hit "a full gigabyte" [HIGH]. The 2022 Steam edition shipped a named "New Legends Mode" update with hyperlink navigation — confirmed as real, but its feature list sits behind Steam page chrome this session; MEDIUM pending a readable source.
6. The community's fix was never "patch the menu," it was **rebuild the browser as a website**: Legends Viewer and its successor LegendsViewer-Next ingest the XML export and serve entity pages with links, filters, a map, and stats the base game never computed [HIGH].
7. DFHack's `legends_plus.xml` (`exportlegends all`) is a second, richer export vanilla Legends mode never surfaces in its own UI — the tooling reads facts the game tracks but hides [HIGH].
8. Players say the pain is shape, not volume: raw output reads like "in-game notifications... loses context," a map makes history "faster to digest, more memorable" [MEDIUM — player testimony].
9. Caves of Qud's sultan histories are the counter-model: procedurally generated but not browsable — the player discovers events one at a time and the journal accretes a partial history; one event can carry two differently-toned tellings, gospel vs. tomb [HIGH — Qud wiki]. Provenance as narrative bias, not a metadata tag.
10. Do not copy: DF's menu-driven text UI, uncapped per-figure event lists, or Qud's discovery-gated non-browsable history — the fabula lens is ruled "the map," browsable from turn one.

## 1. The event as the atomic unit

**One record, four doors.** Legends mode's top-level categories are Historical Figures, Sites, Regions, Civilizations and Entities, Structures, and "The Age of…" [HIGH — DF wiki, DF2014:Legends]. None is separate content: a site page is "every event referencing this site," a figure page "every event referencing this figure," an era page "every event in this year range." The event table is the single source; every surface is a filtered view of it — the strongest, most reusable fact here.

**Event as sentence.** Exports represent each event as a typed record (event type, year, participant/place/cause fields specific to that type) [HIGH — inferred from typed-export existence and tool rendering; exact template unverified, see Blocked]. Tools generate a display sentence from the record (the wiki's own examples of what an era's list shows: a site founded, a person kidnapped, a road completed) [HIGH — DF wiki, paraphrased, not verbatim in-game strings].

**Undiscovered events.** Legends mode tracks a count of events the player-as-historian hasn't yet revealed, distinct from the full dataset — "exists in the world" vs. "known to the reader" [HIGH — DF wiki]. Maps directly onto a discovered/seeded flag per event.

## 2. Entity pages: figures, sites, civilizations

**Historical figure.** Accretes every event it's in plus relationships to other figures — "the history of every single histfig... as well as their relationships with other histfigs" [HIGH — DF wiki]. Field-by-field layout below the identity line not confirmed from a primary source (MEDIUM); the "events + relationships" core is HIGH.

**Sites.** Towns, towers, fortresses, forest retreats, caves each carry their own filtered event list — founding, sieges, occupation changes [HIGH — DF wiki].

**Civilizations and entities.** Civilizations, sub-governments, and religions are a browsable list; a specific government or religion is a distinct row even nested under one people [HIGH — DF wiki].

**Structures.** A layer below sites: named buildings (temples, shops, taverns) that accumulate their own history once tracked [HIGH — DF wiki, distinct top-level category].

**Artifacts.** Not confirmed as a distinct top-level category from a primary source (LOW placement); the figure article references named, historically-tracked artifacts [MEDIUM], and third-party tool galleries list artifact pages [MEDIUM].

## 3. Eras, timeline, map — and the rebuild

**Naming.** Ages are named for the dominant power(s) — Myth, Legends, Heroes as the default progression; ordinals on repeat ("Third Age of Myth"); bespoke names for special conditions (Age of Three Powers, Age of Dwarves, Age of Fairy Tales when mundane civs exceed 90% of the population) [HIGH — DF wiki, Calendar]. Naming is a rule evaluated over world state at each transition — derived, queryable, not fixed.

**Era as event window.** No separate timeline widget: an era view is the event table sorted and windowed by year [HIGH — DF wiki], reinforcing §1.

**Historical map.** The one place vanilla Legends mode shows simultaneous state, not sequence: toggled political/geographical (Enter), civilization/local-government territory (`c`) [HIGH — DF wiki].

**In-game linking, pre-2022.** Event→figure, figure→site navigation exists but is text-menu driven, not persistent hyperlinks [HIGH — inferred from classic version pages describing menu selection].

**The 2022 rework.** The Steam release's "New Legends Mode" update (community-tagged "Age of Hyperlink") added hyperlink-style navigation [MEDIUM — title/existence confirmed via search summaries; article body returned only page chrome on fetch, so the exact feature list is UNVERIFIED].

**Exports.** Vanilla XML dump (`x`) can reach "a full gigabyte" on a large world; `p` exports three text files plus a bitmap (world-gen settings, deities, site population) [HIGH — DF wiki]. DFHack's `legends_plus.xml` (`exportlegends info`/`all`) carries fields the vanilla export omits — a second, richer layer the base UI never shows [HIGH — LegendsBrowser2 README].

**Legends Viewer / LegendsViewer-Next.** Ingests the XML (plus `legends_plus.xml`) and rebuilds every entity as "pages with links to related objects," adds "statistics and overviews not found in the base game," filters "on a wide range of criteria," opens pages in tabs, plots on a map [HIGH — DF wiki; LegendsBrowser2 README]. LegendsViewer-Next is the maintained Steam/Premium (v50+) successor; LegendsViewer and Legends Browser are legacy, pre-Steam [HIGH — GitHub].

**Why the rebuild.** Two complaints, both shape not volume: history-browsing is disconnected from an active fortress's own world [MEDIUM]; vanilla output reads as "notifications... loses context," a map restores it [MEDIUM]. One player called the external viewer "like 70% of the fun" [MEDIUM, illustrative].

## 4. Caves of Qud's sultan histories — the counter-model

Qud generates five procedural sultans (plus one fixed, Resheph), each with 10–22 events (typically 11–14: an origin event plus eight core-life events from a pool of seventeen types) [HIGH — Qud wiki]. Not exposed as an explorable table: the player *discovers* events via shrines, engraved/painted objects, Water Ritual trading, and each discovered event lands in a **Sultan Histories** journal section [HIGH — Qud wiki]. Some events carry both a gospel account and a tomb inscription in "a different tone" — one fact, two biased retellings [HIGH]. Provenance as narrative unreliability, not a citation tag.

**The contrast that matters:** DF Legends is complete-and-browsable regardless of what the player has looked at; Qud's history is complete-in-generation but gated-by-discovery. The Command's ruling — the timeline is the map, the home screen — sides with DF: show the whole board from the start, with a discovered/known-to-reader flag layered on top, not a hidden-until-found journal as the primary mode.

## 5. Translation to the fabula lens

**Entity pages (D1–D4).**
- **D1.** One event table is the only content; every entity page (character, place, era, event) is a filtered/sorted view over it (§1). No separate storage per entity type.
- **D2.** A character page = the historical-figure page: identity line, full list of events this actor appears in (any typed role — actor, target, witness), relationships derived from co-occurrence (§2).
- **D3.** A place page = the site page: identity line, then every event with this place as its location field, chronological (§2).
- **D4.** An era/movement band page = the era view: a chronological event list windowed to the band's M-range, with the band's own label computed from dominant actor/theme (§3), not only hand-set.

**Event as sentence (D5–D7).**
- **D5.** Render every event as one generated sentence from typed fields (actor, event-type/verb, object, place, movement-date), never stored as free prose (§1). The record is the fields; the sentence is a view.
- **D6.** Keep an explicit known-to-reader flag per event, separate from exists-in-fabula, modeled on the undiscovered-event count (§1) — lets the told-order lens show what's been revealed so far without touching fabula completeness.
- **D7.** Where tellings of one event disagree, do it Qud's way: two sentences off one event record, each with its own tone/source, not two separate events (§4). That's the `provenance:` field's job, as narrative variance.

**Cause links as navigation (D8–D9).**
- **D8.** A causal edge (precede/cause/enable/embed/specify/simultaneous) is itself a click-through link — same motion as clicking a figure inside an event sentence — not a separate "related events" widget (§3).
- **D9.** Build the hyperlink-through-prose layer deliberately from day one; vanilla DF shipped without it for a decade and the community had to bolt it on (§3) — don't repeat that gap.

**Filtering by story (D10–D11).**
- **D10.** The `stories:` field is a filter over the single event table ("events where `stories:` contains X"), the same operation as DF's era/figure/site filters (§1, §3) — not a data fork.
- **D11.** Ship DF-viewer-grade filtering (actor, place, event type, era, story) from the start — exactly what vanilla lacked and outside tools had to add (§3).

**Where the CK3 tooltip layer sits (D12).**
- **D12.** CK3's tooltip-in-tooltip contract (concept link → definition → further links, capped 2–3 deep, CK3-IA-STUDY.md R1–R5) applies to *terms inside an event sentence* — actor, place, era, trope-graph term — same as glossary terms in the doctrine browser. Hovering an actor in an event sentence opens the same compact-card-first, full-page-on-click pattern CK3 uses for a portrait. Depth cap and lock behavior transfer unchanged. DF contributes no tooltip precedent of its own (no hover layer in vanilla, §3); this piece imports wholesale from CK3.

## Open questions for Chief

1. Should the event table be the *only* stored object (D1), with figure/place/era pages purely computed views — or do entities need their own persistent fields (portrait, description) beyond what events imply? **Rec:** hybrid — events are the only source of *history*, but entities keep a thin identity record (name, type, one-line description) events attach to, matching DF's figure record (§2).
2. Should the known-to-reader flag (D6) be per-event-per-story, or one global flag per event? A reveal in Story A shouldn't silently unlock Story B's telling. **Rec:** per-event-per-story, keyed off `stories:` (D10) — one more field, avoids a real leak.
3. Does provenance-as-dual-telling (D7, Qud's gospel/tomb model) replace or sit alongside a plain `provenance:` source tag? **Rec:** both — `provenance:` stays a flat citation field for real-world sourcing; dual-telling is a separate `tellings:` list for in-fiction unreliable narration, used only where a story wants competing accounts.
4. The 2022 DF hyperlink update's feature list is unverified this session (§3, Blocked) — worth a second pass reading the Steam article directly before D8/D9 lock, or is the CK3 tooltip precedent (D12) sufficient alone? **Rec:** skip the second pass; D12 already gives a fuller-specified contract than DF's own update summary would add.
5. Should era/movement labels (D4) auto-compute on every fabula edit, or only on demand? Auto-compute risks a band's name flickering mid-edit. **Rec:** on-demand relabel, with a manual override that sticks until cleared — matches DF's era names as a script-evaluated fact at world-gen, not a live recomputation.

## Sources

- DF Wiki: [Legends](https://dwarffortresswiki.org/index.php/DF2014:Legends) · [Historical figure (2014)](https://dwarffortresswiki.org/index.php/DF2014:Historical_figure) · [Historical figure](https://dwarffortresswiki.org/index.php/Historical_figure) · [Utility:Legends viewer](https://dwarffortresswiki.org/index.php/Utility:Legends_viewer) · [World History file](https://dwarffortresswiki.org/index.php/DF2014:World_History_file) · [Calendar](https://www.dwarffortresswiki.org/index.php/Calendar)
- GitHub: [LegendsBrowser2](https://github.com/robertjanetzko/LegendsBrowser2) + [README](https://github.com/robertjanetzko/LegendsBrowser2/blob/master/README.md) · [LegendsViewer-Next](https://github.com/Kromtec/LegendsViewer-Next) · [LegendsViewer](https://github.com/Kromtec/LegendsViewer) + [README](https://github.com/Kromtec/LegendsViewer/blob/master/README.md) · [LegendsBrowser](https://github.com/robertjanetzko/LegendsBrowser) · [DFHack 50.08-r2 notes](https://github.com/DFHack/dfhack/releases/tag/50.08-r2)
- Steam, "New Legends Mode" (title confirmed, body blocked): https://store.steampowered.com/news/app/975370/view/3108047224245566889 ; mirror https://steamcommunity.com/games/975370/announcements/detail/3108047224245566890
- Caves of Qud Wiki: [Sultan histories](https://wiki.cavesofqud.com/wiki/Sultan_histories) · [World generation](https://wiki.cavesofqud.com/wiki/World_generation)
- Steam Community, player testimony (map-vs-text, "70% of the fun"): https://steamcommunity.com/app/975370/discussions/0/3757725518100213402
- Reused without re-fetch (D12): CK3-IA-STUDY.md R1–R5, C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_0.1_BVX_LEARN\_meta\CK3-IA-STUDY.md

## Blocked / Unverified

- Steam news pages (store + community mirror): returned page chrome only. Title/rough claim MEDIUM via search summaries; exact feature list UNVERIFIED.
- Exact XML/`legends_plus.xml` tag names and the literal event-to-sentence template: not recovered from a primary source; rendering rule HIGH (structural), literal grammar unverified.
- Historical figure field-by-field layout: not confirmed from a primary source — MEDIUM at best.
- Artifact pages as a distinct top-level category: not directly confirmed in fetched wiki text; inferred only (MEDIUM/LOW).
- Legends Browser 2's full page inventory beyond "objects with links to related objects": not itemized in the fetched README excerpt.
- No developer-authored (Bay 12/Tarn Adams) design writeup on Legends mode's UI rationale found this session — claims rest on wiki, tool READMEs, and player testimony, not a primary designer source.
- web.archive.org not fetchable by this tool (same limitation as CK3-IA-STUDY.md).
