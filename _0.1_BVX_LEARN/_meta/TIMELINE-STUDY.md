---
rung: study · NASA four, ruled 2026-09-24 (BOLO 79)
---

# Timeline / Told-Order Interface Study → Rules for the Story Workspace

Scope: **Heaven's Vault** (inkle, 2019), **Return of the Obra Dinn** (Lucas Pope, 2018), **Her Story** (2015) / **Telling Lies** (2019, Sam Barlow), and **Outer Wilds**' ship log — a model for the story workspace's fabula timeline (world time, fuzzy/unknown dates as ranges, eras, typed causal edges) and told-order lens (syuzhet: two stacked tracks, told above world, jump lines for analepsis/prolepsis). Extends, does not repeat, [CK3-IA-STUDY.md](CK3-IA-STUDY.md)'s nested-tooltip contract (§1, R1-R5), reused not re-derived. Confidence HIGH/MEDIUM/LOW per claim. Study date 2026-09-24.

## Executive summary

1. Heaven's Vault draws unknown history as its own **named era band** ("180-350 years ago, little is known"), not blank axis — the model for T2.
2. HV's timeline zoom is one continuous control, "minute by minute" to "thousands of years," smoothly animated — one axis, not day/month/year buttons (T12).
3. HV ties translation **confidence** to repetition — a word read often enough is trusted; a wrong reading is explicitly replaced, never silently overwritten — confidence is a value that grows and can flip (T9).
4. Obra Dinn's Book of Fates was chosen **over** a prototyped "navigable timeline interface" Pope built and rejected — direct evidence a full timeline reader is not self-justifying (Do Not Copy).
5. Obra Dinn's chapter map **fills in gradually** as fates are solved — the record starts sparse and thickens; nothing is pre-drawn (T8).
6. Obra Dinn's pocket watch hands double as an address: hour = chapter, minute (5-min steps) = part — a literal dial-index into told order, the closest any studied game gets to a two-track told/world instrument (T5).
7. Her Story / Telling Lies give the player **no built-in chronology UI at all** — the database resists order, and the player's own notes are the told order; Telling Lies caps search returns at five, forcing partial, re-queried views.
8. Telling Lies' clip-scrub is explicitly non-chronological by design intent (Barlow) — "memories do not come to us in ... linear order" — a micro-scale model of analepsis/prolepsis inside one told scene.
9. Outer Wilds' ship log is **two lenses on one fact store**, switchable, never fused: Map Mode (spatial) and Rumor Mode (causal graph); unconfirmed facts get a fixed question-mark icon that flags a gap without revealing it (T7, T10).
10. Do not copy: HV's timeline popping up on trivial 3-minutes-ago pickups (players called it noise); Obra Dinn's book-over-timeline choice as a caution, not a mandate; Telling Lies' anti-chronological scrub, which serves mystery pacing, not information architecture.

## 1. Heaven's Vault — the History timeline

**Structure.** History divides into named eras measured backward from "now": roughly 0-180, 180-350, 350-580, 580-950, 950-1,670, 1,670-2,500, 2,500-3,500 years ago, the 180-350 band explicitly "very little known" [MEDIUM — aggregated search excerpt, Wikipedia/Gamer Escape wiki; wiki page 403'd on direct fetch]. The gap is a named, drawn era, not an absence.

**Scale.** "The timeline could expand to show minute by minute discoveries, and compress to show thousands of years worth of history, and all smoothly animated" [MEDIUM — search excerpt, PopMatters]. Fogknife calls it "the single most *80 Days*-esque part of the game's original UI"; every script encounter — deciphered or not — adds "a new notch," reflecting "the fractal way she sees her own lifetime... as just another fold inside an infinitely crinkly global history" [HIGH — direct fetch, fogknife.com]. Emily Short: "Aliya's backstory is presented as a series of dates on her timeline, there for you to explore if you want" [HIGH — direct fetch, emshort.blog].

**Confidence vs date.** Translation confidence is a separate, growing value: a word read often enough earns trust; a wrong reading is explicitly flagged and swapped, not silently corrected [MEDIUM — search excerpt, Steam discussion]. A PopMatters-sourced excerpt frames the system as "inference rather than completing a tick list," the deciphered past as "approximations akin to a third-person limited perspective" [MEDIUM].

**Friction.** A player, quoted directly: "what's the point of noting everything on the timeline? sure, 3000 years ago this and that happened, but me picking up a book or finding a new location 3 and 8 minutes ago seems irrelevant and annoying since the timeline thing pops up all the time" [HIGH — direct fetch, Steam thread]. World-scale and session-scale events sharing one popup channel reads as noise.

## 2. Return of the Obra Dinn — the Book of Fates

**Choice of form.** Pope considered "a much shorter logbook, a navigable timeline interface, etc" before settling on the book as "the most implicitly useful metaphor" [HIGH — direct fetch, dukope.com]. The book's job: "collect and organize the deluge of information," establish chronology, show death detail, carry identity clues [HIGH — same source]. A dedicated timeline widget was tried and set aside.

**Progressive fill.** Ten chapters, grouped by clustered deaths; Chapter VIII stays hidden until every knowable fate is solved [MEDIUM — search excerpt, fandom/GameFAQs]. Each chapter's map "gradually becomes filled in with a helpful overview of the chronology of events within a chapter" [MEDIUM — search excerpt]. The record starts sparse and thickens with play; nothing is pre-drawn.

**Draft vs confirmed.** Handwritten (editable) entries convert to typed, locked text once three fates are correctly solved in a batch [MEDIUM — search excerpt]. Two rendering states carry one meaning: draft vs confirmed, arriving in batches of three, not one at a time.

**A literal told-order dial.** The pocket watch ("Memento Mortem") freezes a death scene for exploration; its hands double as an address — hour = chapter, minute in five-minute steps = part (3:05 = ch. III pt. 1, 3:10 = pt. 2) [HIGH — search excerpt, fandom wiki + walkthrough]. Every scene has a stable two-part ID before its world-time placement. The fate record itself is a fixed schema per event — name, rank/role, cause of death, sometimes a killer — filled via dropdowns from the ship's manifest [MEDIUM — search excerpt].

## 3. Her Story / Telling Lies — the reconstructed database

**No built-in chronology.** Her Story sits the player at a period-styled desktop searching ~300 short interrogation clips; no timeline widget exists in the game — the player's own paper notes are the told order [HIGH — Wikipedia-level, confirmed by search aggregate]. The game withholds chronology by design; assembling it is the whole activity.

**Partial, re-queried views.** Telling Lies splits two callers' sides of the same conversations into separate records and caps search returns at the first five hits, "in chronological order," pushing the player to refine keywords; a hit jumps a clip to the keyword moment and timestamps its other occurrences in that clip [HIGH — search excerpt, Wireframe Magazine]. Order exists only inside a capped, re-runnable result list, never as a persistent global index.

**Scrub as anti-chronology.** Barlow, on the scrub mechanic (GameDeveloper Deep Dive, via search excerpt): it embraces "the analogue feel of *The Conversation*," and "memories do not come to us in chronological, linear order — by scrubbing backwards or forwards through a clip, the player is as likely to uncover new information" [MEDIUM — search excerpt, primary not directly fetchable]. A mystery-pacing device, not an IA pattern — flagged under Do Not Copy.

## 4. Outer Wilds — the ship log (rumor vs map mode)

**Two lenses, one store.** Map Mode groups entries by planet/structure (spatial, for picking a destination); Rumor Mode groups the same entries by causal relation, and — since discovery order differs per player — its graph layout differs per playthrough [HIGH — search aggregate, outerwildsmods.com + fandom]. Both read the same fact store; switching loses or duplicates nothing.

**A fixed icon for a known gap.** Unconfirmed/partial entries carry a colored question-mark badge (orange by default) signaling "more here" without revealing what or where it connects [MEDIUM — search excerpt, Steam guide + mod docs]. The icon marks a gap; it does not spoil the answer.

## 5. Translation to the story workspace

**Dates, ranges, unknowns (from §1, §2).**
- T1. Draw every fuzzy date as a **banded range** on the timeline axis, never a single guessed point: a translucent bar spanning the known bracket, matching HV's "180-350 years ago" era band. A caret/point mark appears only when a source states an exact date.
- T2. An unknown span is its **own labeled band** (hatched or muted fill, its own hover text), not an empty stretch of axis — HV draws the Fall-of-Iox-to-Protectorate gap as a named era rather than omitting it.
- T3. Eras render as coarser bands **underneath** individual events; the zoom control (T12) must be able to collapse to an era-only view, the way HV's seven eras read at large zoom-out before any individual date shows.
- T4. Date-precision (T1's band width) and source-confidence (T9) are **two independent axes** — never conflate a wide date range with an unconfirmed fact, or a narrow range with a trusted one. HV keeps them separate: the era bands are structural, confidence is earned by rereading.

**Told order / two-track view — extends past the source games; no studied title draws this literally.**
- T5. Give every scene a **stable two-part ID** before it has a world-time placement, the way Obra Dinn's watch hands address chapter.part — the told-order track is built from discrete scene IDs, not raw timestamps, because scenes (not seconds) are the reader's unit. [Synthesis — LOW as precedent, HIGH as an extension of a confirmed mechanic.]
- T6. A jump line is a **navigable instrument**, not a one-way annotation: clicking it scrubs both tracks to the target and back — the workspace equivalent of Telling Lies' scrub, where moving backward is as likely to surface new information as moving forward.
- T7. Keep the fabula/told-order toggle as **two saved views over one store**, switchable, never fused into a single diagram — confirming, via Outer Wilds' Map/Rumor split, the two-lens shape already ruled for this app rather than inventing a third hybrid view.

**Partial record / provenance (from §1, §2, §4).**
- T8. Don't pre-draw the full timeline for an empty or half-built project: Obra Dinn's chapter map fills in only as fates are solved. The fabula view should start sparse and visibly thicken as events are entered — a layout constraint for low-data states, not just a load animation.
- T9. Three visual states per event, not two: **draft** (HV's not-yet-confident reading / Obra Dinn's editable handwriting), **confirmed** (Obra Dinn's locked type after a batch of three), and **revised** (HV's "definitely looks wrong, replace with another possible solution" — the old value stays visible, struck or dimmed, rather than vanishing). Encode all three by weight/style, not color alone, to hold CK3 study R17's contrast rule.
- T10. A **fixed icon** marks a known gap in the fabula or trope graph, never blank space — reuse Outer Wilds' question-mark badge for "an event is referenced but not yet placed." Unlike Outer Wilds, this is a builder's tool for Chief's own project, not a mystery kept from a player: hovering the badge should name the source that referenced the gap (e.g., "referenced by BOLO 12, undated"), where Outer Wilds' badge deliberately stays silent.
- T11. Batch confirmation like Obra Dinn's three-fates-per-lock: group unresolved events sharing a source (one document, one BOLO) so ruling one nudges the reader toward its siblings, instead of leaving isolated "unverified" flags scattered with no path to closure.

**Zoom / scale (from §1).**
- T12. One continuous zoom axis, minute to millennium, smoothly animated — HV's compress/expand — not discrete day/month/year steps; the same control must carry a single scene's told-order minutes and the fabula's multi-century sweep.
- T13. Cap what "recent" (edit-time) events auto-surface at wide zoom: HV players singled out the timeline popping up for 3-minutes-ago pickups as noise. Below a chosen zoom threshold, suppress sub-scene/session-clock events by default so session recency is never mistaken for narrative weight.

**CK3 tooltip layer (extends CK3-IA-STUDY.md §1, R1-R5 — same component, new content).**
- T14. Hovering any fabula, told-order, or trope-graph marker opens the same nested-tooltip contract already ruled: bold event name, one-line description, then a breakdown row list — here, a date-range row (T1), a confidence/state row (T9), an era link (T3), and, for a told-order marker, its scene ID (T5) and jump target (T6). The depth-3 cap and lock timing from the doctrine browser study carry over unchanged; this study does not reopen that number.
- T15. A causal edge (trope graph) and an event's provenance marker (T9) live as **rows inside this one tooltip**, not as separate hover systems — one component serves all three lenses, holding CK3's rule that linking is a property of the text layer, not the widget.

**Do not copy.**
- Obra Dinn's book-over-timeline choice: Pope prototyped "a navigable timeline interface" and rejected it for the book. Treat this as a caution against assuming a full timeline reader is self-justifying — the CK3-style sheet/tab view (per CK3-IA-STUDY.md R6-R11) may still be the right home for a single event's detail, even with the timeline as the app's home screen.
- Telling Lies' anti-chronological scrub is a mystery-pacing device for an FMV thriller, not an IA pattern; T6 borrows the *mechanism* (bidirectional scrub) but not the *intent* (deliberate disorientation).
- HV's single popup channel for both world-scale and session-scale events.

## Sources

- Heaven's Vault era ranges (via search aggregate; wiki 403'd direct): https://en.wikipedia.org/wiki/Heaven%27s_Vault ; https://heavensvault.gamerescape.com/wiki/Timeline
- Emily Short, "Heaven's Vault (inkle)": https://emshort.blog/2019/07/23/heavens-vault-inkle/
- Fogknife, "I played Heaven's Vault": https://fogknife.com/2019-05-03-i-played-heavens-vault.html
- PopMatters, "Found in Translation" (via search excerpt): https://www.popmatters.com/heavens-vault-adventure-game-review
- Steam Community, Heaven's Vault discussions (popup complaint; confidence thread): https://steamcommunity.com/app/774201/discussions/0/1652169858540964705/ ; https://steamcommunity.com/app/774201/discussions/0/3570700856123387903/
- Cambridge Core academic article on Heaven's Vault (checked, no UI detail): https://www.cambridge.org/core/product/847BC3EFEF0C05C1E3D28A658D320B77/core-reader
- Lucas Pope, TIGSource devlog, Obra Dinn, June 2019 (book-vs-timeline choice): https://dukope.com/devlogs/obra-dinn/tig-37/
- Obra Dinn Wiki (Fandom), General and Pocket watch (via search excerpt): https://obradinn.fandom.com/wiki/General ; https://obradinn.fandom.com/wiki/Pocket_watch
- GameFAQs, "Solving Fates and Completing the Book" (via search excerpt): https://gamefaqs.gamespot.com/switch/272725-return-of-the-obra-dinn/faqs/78105/solving-fates-and-completing-the-book
- Game UI Database, Obra Dinn entry (blocked, HTTP 403): https://www.gameuidatabase.com/gameData.php?id=1460
- Wireframe Magazine, "Telling Lies preview": https://wireframe.raspberrypi.org/articles/telling-lies-preview-is-her-story-true
- Game Developer, "Deep Dive: Telling Lies" (via search excerpt): https://www.gamedeveloper.com/design/deep-dive-i-telling-lies-i---making-a-mechanic-out-of-scrubbing-video
- Her Story (video game), Wikipedia: https://en.wikipedia.org/wiki/Her_Story_(video_game)
- Outer Wilds mods, "Custom Ship Log Modes" / "Ship Log | New Horizons": https://outerwildsmods.com/mods/customshiplogmodes/ ; https://nh.outerwildsmods.com/guides/ship-log/
- Outer Wilds Wiki (Fandom), Computer page (blocked, HTTP 402): https://outerwilds.fandom.com/wiki/Computer
- Steam Guide, "Ship Log Completion Guide" (badge colors, via search excerpt): https://steamcommunity.com/sharedfiles/filedetails/?id=3500382207
- Mohedano, "How Outer Wilds transcends UX" (blocked, 403): https://medium.com/@claudmohe/how-outer-wilds-transcends-ux-to-become-human-experience-3ff41def8f8c
- Passi, "Outer Wilds: A UX Critique Part 2" (blocked, 403): https://ankitpassi.medium.com/outer-wilds-a-ux-critique-part-2-146abcb9a5a1

## Blocked / Unverified

- gamerescape wiki, gameuidatabase.com, outerwilds fandom, both Medium essays: all returned 403/402 on direct fetch; every claim sourced to them rests on search-excerpt aggregation only (capped MEDIUM).
- No GDC talk, dev diary, or designer-authored primary source was recovered describing Heaven's Vault's History-screen visual grammar (band colors, hover behavior) — claims trace to reviews/player threads only, capped MEDIUM.
- Jon Ingold's 2018 GDC talk ("dynamic detective story") was located by title only; the fetched Game Developer URL returned unrelated page chrome — not used as a source.
- No primary designer statement exists for the two-track told/world diagram (T5-T7); flagged as this study's own synthesis, not observed in any shipped game.

## Open questions for Chief

1. T5 proposes discrete scene IDs (chapter.part style, after Obra Dinn's watch) for the told-order track instead of a continuous timestamp axis. **Rec: discrete IDs** — scenes are the reader's unit, and Obra Dinn's own scheme is the only precedent found for a stable told-order address.
2. T4 keeps date-precision and source-confidence as two separately legible marks rather than one blended "fuzziness" bar. **Rec: keep them separate** — a scene that's firmly dated but contested, and one that's vaguely dated but certain, need to read differently on sight.
3. T10's gap icon reveals its referencing source on hover, unlike Outer Wilds' deliberately silent question mark, because this is Chief's own build tool, not a mystery kept from a player. **Rec: confirm reveal-on-hover** — the mystery-preservation logic in the source game doesn't apply here.
4. T13's recency-suppression threshold (hiding session-clock events at wide zoom) — automatic by zoom level, or a manual per-project toggle. **Rec: automatic default tied to zoom, with manual override** — BVX_LEARN projects vary widely in scene density, and no single fixed threshold will fit all of them.
5. T14 reuses the CK3 doctrine browser's depth-3 tooltip cap for causal-edge chains in the trope graph, even though edges can chain further than glossary terms did. **Rec: keep the cap at 3** and make "follow the causal chain" a click-to-open graph action instead, consistent with CK3 study R14 ("hover inspects, click opens").
