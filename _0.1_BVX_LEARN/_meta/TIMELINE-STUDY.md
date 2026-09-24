---
rung: study · NASA four, ruled 2026-09-24 (BOLO 79)
---

# Timeline / Told-Order Interface Study → Rules for the Story Workspace

Scope: **Heaven's Vault** (inkle, 2019), **Return of the Obra Dinn** (Lucas Pope, 2018), **Her Story** (2015) / **Telling Lies** (2019, Sam Barlow), and **Outer Wilds**' ship log — a model for the story workspace's fabula timeline (world time, fuzzy/unknown dates as ranges, eras, typed causal edges) and told-order lens (syuzhet: two stacked tracks, told above world, jump lines for analepsis/prolepsis). Extends [CK3-IA-STUDY.md](CK3-IA-STUDY.md)'s nested-tooltip contract (§1, R1-R5), reused not re-derived. Confidence HIGH/MEDIUM/LOW per claim. Study date 2026-09-24.

## Executive summary

1. Heaven's Vault draws unknown history as its own **named era band** ("180-350 years ago, little is known"), not blank axis — model for T2.
2. HV's timeline zoom is one continuous control, "minute by minute" to "thousands of years," smoothly animated — one axis, not day/month/year buttons (T12).
3. HV ties translation **confidence** to repetition — a word read often enough is trusted; a wrong reading is explicitly replaced, never silently overwritten (T9).
4. Obra Dinn's Book of Fates was chosen **over** a prototyped "navigable timeline interface" Pope built and rejected — evidence a full timeline reader isn't self-justifying (Do Not Copy).
5. Obra Dinn's chapter map **fills in gradually** as fates are solved — starts sparse, thickens; nothing pre-drawn (T8).
6. Obra Dinn's pocket watch hands double as an address: hour = chapter, minute (5-min steps) = part — a literal dial-index into told order, the closest any studied game gets to a two-track instrument (T5).
7. Her Story / Telling Lies give the player **no built-in chronology UI** — the database resists order, player notes are the told order; Telling Lies caps search returns at five, forcing partial views.
8. Telling Lies' clip-scrub is explicitly non-chronological by design (Barlow) — "memories do not come to us in ... linear order" — a micro model of analepsis/prolepsis inside one told scene.
9. Outer Wilds' ship log is **two lenses on one fact store**, switchable, never fused: Map Mode (spatial), Rumor Mode (causal graph); unconfirmed facts get a fixed question-mark icon flagging a gap without revealing it (T7, T10).
10. Do not copy: HV's timeline popping up on trivial 3-minutes-ago pickups (noise, per players); Obra Dinn's book-over-timeline choice as caution, not mandate; Telling Lies' anti-chronological scrub, a mystery-pacing device, not an IA pattern.

## 1. Heaven's Vault — the History timeline

**Structure.** History divides into named eras measured backward from "now": roughly 0-180, 180-350, 350-580, 580-950, 950-1,670, 1,670-2,500, 2,500-3,500 years ago, the 180-350 band explicitly "very little known" [MEDIUM — aggregated search excerpt; wiki page 403'd on direct fetch]. The gap is a named, drawn era, not an absence.

**Scale.** "The timeline could expand to show minute by minute discoveries, and compress to show thousands of years worth of history, and all smoothly animated" [MEDIUM — search excerpt, PopMatters]. Fogknife calls it "the single most *80 Days*-esque part of the game's original UI"; every script encounter — deciphered or not — adds "a new notch," reflecting "the fractal way she sees her own lifetime... as just another fold inside an infinitely crinkly global history" [HIGH — direct fetch]. Emily Short: "Aliya's backstory is presented as a series of dates on her timeline, there for you to explore if you want" [HIGH — direct fetch].

**Confidence vs date.** Translation confidence is a separate, growing value: a word read often enough earns trust; a wrong reading is explicitly flagged and swapped, not silently corrected [MEDIUM — search excerpt]. The deciphered past reads as "approximations akin to a third-person limited perspective" [MEDIUM].

**Friction.** A player, quoted directly: "what's the point of noting everything on the timeline? sure, 3000 years ago this and that happened, but me picking up a book or finding a new location 3 and 8 minutes ago seems irrelevant and annoying since the timeline thing pops up all the time" [HIGH — direct fetch]. World-scale and session-scale events on one popup channel reads as noise.

## 2. Return of the Obra Dinn — the Book of Fates

**Choice of form.** Pope considered "a much shorter logbook, a navigable timeline interface, etc" before settling on the book as "the most implicitly useful metaphor" [HIGH — direct fetch]. Its job: "collect and organize the deluge of information," establish chronology, show death detail, carry identity clues [HIGH — same source]. A timeline widget was tried and set aside.

**Progressive fill.** Ten chapters, grouped by clustered deaths; Chapter VIII stays hidden until every knowable fate is solved [MEDIUM — search excerpt]. Each chapter's map "gradually becomes filled in with a helpful overview of the chronology of events within a chapter" [MEDIUM — search excerpt]. The record starts sparse and thickens with play; nothing is pre-drawn.

**Draft vs confirmed.** Handwritten (editable) entries convert to typed, locked text once three fates are correctly solved in a batch [MEDIUM — search excerpt]. Two rendering states carry one meaning: draft vs confirmed, arriving in batches of three.

**A literal told-order dial.** The pocket watch ("Memento Mortem") freezes a death scene for exploration; its hands double as an address — hour = chapter, minute in five-minute steps = part (3:05 = ch. III pt. 1, 3:10 = pt. 2) [HIGH — search excerpt]. Every scene has a stable two-part ID before its world-time placement. The fate record is a fixed schema per event — name, rank/role, cause of death, sometimes a killer — filled via dropdowns from the ship's manifest [MEDIUM — search excerpt].

## 3. Her Story / Telling Lies — the reconstructed database

**No built-in chronology.** Her Story sits the player at a period-styled desktop searching ~300 short interrogation clips; no timeline widget exists — the player's own paper notes are the told order [HIGH — Wikipedia-level, confirmed by search aggregate]. The game withholds chronology by design; assembling it is the activity.

**Partial, re-queried views.** Telling Lies splits two callers' sides of a conversation into separate records and caps search returns at five hits, "in chronological order," pushing the player to refine keywords; a hit jumps a clip to the keyword moment and timestamps its other occurrences [HIGH — search excerpt]. Order exists only inside a capped, re-runnable result list, never a persistent global index.

**Scrub as anti-chronology.** Barlow, on the scrub mechanic (via search excerpt): it embraces "the analogue feel of *The Conversation*," and "memories do not come to us in chronological, linear order — by scrubbing backwards or forwards through a clip, the player is as likely to uncover new information" [MEDIUM — primary not fetchable]. A mystery-pacing device, not an IA pattern — flagged under Do Not Copy.

## 4. Outer Wilds — the ship log (rumor vs map mode)

**Two lenses, one store.** Map Mode groups entries by planet/structure (spatial, for picking a destination); Rumor Mode groups the same entries by causal relation, and since discovery order differs per player, its graph layout differs per playthrough [HIGH — search aggregate]. Both read the same fact store; switching loses nothing.

**A fixed icon for a known gap.** Unconfirmed/partial entries carry a colored question-mark badge (orange by default) signaling "more here" without revealing what or where it connects [MEDIUM — search excerpt]. The icon marks a gap; it doesn't spoil the answer.

## 5. Translation to the story workspace

**Dates, ranges, unknowns (§1, §2).**
- T1. Draw every fuzzy date as a **banded range**, never a single guessed point: a translucent bar over the known bracket, matching HV's "180-350 years ago" era band. A point mark appears only when a source states an exact date.
- T2. An unknown span is its **own labeled band** (hatched/muted fill, own hover text), not empty axis — HV draws the Fall-of-Iox gap as a named era, not an omission.
- T3. Eras render as coarser bands **underneath** individual events; the zoom control (T12) must collapse to an era-only view, as HV's seven eras read at zoom-out before any single date shows.
- T4. Date-precision (T1) and source-confidence (T9) are **two independent axes** — never conflate a wide range with an unconfirmed fact. HV keeps them separate: eras are structural, confidence is earned by rereading.

**Told order / two-track view — extends past the source games; no studied title draws this literally.**
- T5. Give every scene a **stable two-part ID** before its world-time placement, as Obra Dinn's watch hands address chapter.part — discrete scene IDs, not raw timestamps, since scenes (not seconds) are the reader's unit. [Synthesis — LOW as precedent, HIGH as extension of a confirmed mechanic.]
- T6. A jump line is a **navigable instrument**, not a one-way annotation: clicking scrubs both tracks to the target and back — the workspace equivalent of Telling Lies' scrub, backward as likely to surface new information as forward.
- T7. Keep the fabula/told-order toggle as **two saved views over one store**, switchable, never fused — confirming, via Outer Wilds' Map/Rumor split, the two-lens shape already ruled rather than inventing a hybrid.

**Partial record / provenance (§1, §2, §4).**
- T8. Don't pre-draw the full timeline for an empty/half-built project: Obra Dinn's chapter map fills in only as fates are solved. The fabula view starts sparse and visibly thickens as events are entered.
- T9. Three visual states per event: **draft** (HV's not-yet-confident reading / Obra Dinn's editable handwriting), **confirmed** (Obra Dinn's locked type after a batch of three), **revised** (HV's "definitely looks wrong, replace with another" — old value stays visible, struck/dimmed, not deleted). Encode by weight/style, not color alone, per CK3 study R17.
- T10. A **fixed icon** marks a known gap in fabula or trope graph, never blank space — reuse Outer Wilds' question-mark badge for "referenced but not placed." Unlike Outer Wilds, this is a builder's tool, not a kept mystery: hovering names the referencing source ("referenced by BOLO 12, undated"), where Outer Wilds' badge stays silent.
- T11. Batch confirmation like Obra Dinn's three-fates-per-lock: group unresolved events sharing a source (one document, one BOLO) so ruling one nudges the reader toward its siblings, instead of scattered lone "unverified" flags.

**Zoom / scale (§1).**
- T12. One continuous zoom axis, minute to millennium, smoothly animated — HV's compress/expand — not discrete day/month/year steps; one control carries both a scene's told-order minutes and the fabula's century sweep.
- T13. Cap what "recent" (edit-time) events auto-surface at wide zoom: HV players called the timeline popping up for 3-minutes-ago pickups noise. Below a chosen zoom, suppress sub-scene/session-clock events by default.

**CK3 tooltip layer (extends CK3-IA-STUDY.md §1, R1-R5 — same component, new content).**
- T14. Hovering any fabula, told-order, or trope-graph marker opens the same nested-tooltip contract already ruled: bold name, one-line description, breakdown rows — a date-range row (T1), confidence/state row (T9), era link (T3), and, for a told-order marker, scene ID (T5) and jump target (T6). Depth-3 cap and lock timing carry over unchanged; not reopened here.
- T15. A causal edge (trope graph) and an event's provenance marker (T9) live as **rows inside this one tooltip**, not separate hover systems — one component serves all three lenses, per CK3's rule that linking is a property of the text layer, not the widget.

**Do not copy.**
- Obra Dinn's book-over-timeline choice: Pope prototyped a "navigable timeline interface" and rejected it — a caution against assuming a full timeline reader is self-justifying; a CK3-style sheet/tab view (R6-R11) may still be the right home for one event's detail.
- Telling Lies' anti-chronological scrub is a mystery-pacing device, not an IA pattern; T6 borrows the mechanism, not the intent.
- HV's single popup channel for both world-scale and session-scale events.

## Sources

- HV era ranges (search aggregate, wiki 403'd): https://en.wikipedia.org/wiki/Heaven%27s_Vault ; https://heavensvault.gamerescape.com/wiki/Timeline
- Short, "Heaven's Vault (inkle)": https://emshort.blog/2019/07/23/heavens-vault-inkle/
- Fogknife, "I played HV": https://fogknife.com/2019-05-03-i-played-heavens-vault.html
- PopMatters, "Found in Translation" (search excerpt): https://www.popmatters.com/heavens-vault-adventure-game-review
- Steam, HV discussions: https://steamcommunity.com/app/774201/discussions/0/1652169858540964705/ ; https://steamcommunity.com/app/774201/discussions/0/3570700856123387903/
- Cambridge Core article on HV (checked, no UI detail): https://www.cambridge.org/core/product/847BC3EFEF0C05C1E3D28A658D320B77/core-reader
- Pope, TIGSource devlog, Obra Dinn: https://dukope.com/devlogs/obra-dinn/tig-37/
- Obra Dinn Wiki, General + Pocket watch: https://obradinn.fandom.com/wiki/General ; https://obradinn.fandom.com/wiki/Pocket_watch
- GameFAQs, "Solving Fates and Completing the Book": https://gamefaqs.gamespot.com/switch/272725-return-of-the-obra-dinn/faqs/78105/solving-fates-and-completing-the-book
- Game UI DB, Obra Dinn (blocked, 403): https://www.gameuidatabase.com/gameData.php?id=1460
- Wireframe Magazine, "Telling Lies preview": https://wireframe.raspberrypi.org/articles/telling-lies-preview-is-her-story-true
- Game Developer, "Deep Dive: Telling Lies" (search excerpt): https://www.gamedeveloper.com/design/deep-dive-i-telling-lies-i---making-a-mechanic-out-of-scrubbing-video
- Her Story, Wikipedia: https://en.wikipedia.org/wiki/Her_Story_(video_game)
- Outer Wilds mods, ship-log mode docs: https://outerwildsmods.com/mods/customshiplogmodes/ ; https://nh.outerwildsmods.com/guides/ship-log/
- Outer Wilds Wiki, Computer page (blocked, 402): https://outerwilds.fandom.com/wiki/Computer
- Steam Guide, "Ship Log Completion Guide" (badge colors, search excerpt): https://steamcommunity.com/sharedfiles/filedetails/?id=3500382207
- Mohedano (blocked, 403): https://medium.com/@claudmohe/how-outer-wilds-transcends-ux-to-become-human-experience-3ff41def8f8c ; Passi (blocked, 403): https://ankitpassi.medium.com/outer-wilds-a-ux-critique-part-2-146abcb9a5a1

## Blocked / Unverified

- gamerescape wiki, gameuidatabase.com, outerwilds fandom, both Medium essays: 403/402 on direct fetch; claims from them rest on search-excerpt aggregation only (capped MEDIUM).
- No GDC talk, dev diary, or designer source describes HV's History-screen visual grammar (band colors, hover behavior) — claims trace to reviews/player threads only, capped MEDIUM.
- Jon Ingold's 2018 GDC talk located by title only, page chrome not talk content — not used as a source. No designer statement exists for the two-track told/world diagram (T5-T7); flagged as this study's own synthesis.

## Open questions for Chief

1. T5 proposes discrete scene IDs (chapter.part, after Obra Dinn's watch) for the told-order track instead of a continuous timestamp axis. **Rec: discrete IDs** — scenes are the reader's unit; Obra Dinn's scheme is the only precedent found.
2. T4 keeps date-precision and source-confidence as two separately legible marks rather than one blended "fuzziness" bar. **Rec: keep separate** — firmly-dated-but-contested and vaguely-dated-but-certain must read differently.
3. T10's gap icon reveals its referencing source on hover, unlike Outer Wilds' silent question mark, since this is Chief's own build tool, not a kept mystery. **Rec: confirm reveal-on-hover.**
4. T13's recency-suppression threshold — automatic by zoom level, or a manual per-project toggle. **Rec: automatic default tied to zoom, with override** — BVX_LEARN projects vary widely in scene density.
5. T14 reuses the CK3 browser's depth-3 tooltip cap for causal-edge chains, though edges can chain further than glossary terms. **Rec: keep the cap at 3**; make "follow the causal chain" a click-to-open action, per CK3 study R14.
