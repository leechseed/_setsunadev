---
title: SOP — Standing Operating Procedure
type: doctrine
status: living document — canonical home of the verbal protocol
updated: 2026-08-22
read_first: true
read_with: STATE.md · BOLO.md · PROJECTS.md · _CACHE/
---

# SOP — THE WAY THIS OPERATION RUNS

Canonical home of every comms code and session protocol. If a code is not written here, it is not protocol. Claude's agent memory mirrors this file; **on any conflict, this file wins.** Written to the Marine Corps Doctrine Standard.

---

## 0 · SOI — the proword card

Quick reference. Full definitions in the sections below.

**Commands:** **"sit rep"** (full board) · **"Oscar Mike"** (park it, move on) · **"RTB"** (return to base — promote & clear the parked) · **"Charlie Mike"** (resume the parked card) · **"how copy?"** (end of orders → Good/Solid/Bad copy + execute) · **"boresight"** (understanding check: readback → the read → clarifying questions only; no delivery until cleared; only when spoken; **"boresight in on [target]"** aims it at a named item) · **"BOLO that" / "put that down"** (tasking captured same turn) · **"ivory tower"** (academic mode — published literature only, cited inline) · **"break-break"** (open a detour) · **"buttonhook back"** (close the detour — main thread restored unprompted) · **"run the darkroom"** (launch the DARKROOM program, no questions) · **"belay that"** (cancel the preceding order) · **"ENDEX"** (session close-out: cache note, STATE, journal) · **"status on BOLO N"** (provisional 9/10: that BOLO's status page — the five-paragraph order, next action on top) · the challenge phrase (→ countersign → sit rep)

**Board vocabulary:** **BOLO** (watchlist) · **PMCS** (operator readiness) · **Fresh Ten** (recency) · **The Ancients** (staleness tiers) · **Deep Stacks** (volume) · **Ready Rack** (`_CACHE/`) · **Magazine** (`_LOG/`) · **SOP** (this file)

---

## 1 · Comms codes

| Transmission | Meaning | Response protocol |
|---|---|---|
| **"sit rep"** (equivalents: "the board" · "where did we leave off" · "what are we working on") | Full board, cold start | Flush the Ready Rack (§3), then deliver the sit rep (§2). No preamble, no questions. **Since 2026-09-10 the board is also a page (BOLO 38):** write the board as data to `_tools/sitrep/boards/<date>.json`, run `python _tools/sitrep/build.py`, republish `SITREP.html` to the standing artifact https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a (pass it as `url` from any other session), and hand the link. The chat carries the link plus the leverage line; the page carries the eight blocks. |
| **The challenge phrase** (see STATE.md header) | Formal challenge | Countersign, first line, exact — then the sit rep. Never explain the ritual. |
| **"Oscar Mike"** | Park current work, move on | Save working state to `oscar-mike/`, update its INDEX, drop the task, take the next order. **"RTB"** (return to base, RULED 2026-09-10) sends the keepers home to their real files and clears the folder; **"Charlie Mike"** resumes a card. Repo is PUBLIC — nothing sensitive parks there. **The reply that executes a park ends with the OUT block (§7 rule 9)** — coded 2026-09-06 on Papi's order: a visible seam between what was parked and what starts next. |
| **"Charlie Mike"** — **RULED 2026-09-10** (spoken: "I like Charlie Mike for continuing mission") | Continue mission — resume a parked card | Open the named `oscar-mike/` card (the most recent if none is named), restate where it stood in one line, pick up at its resume order. No re-derivation. The park trio: Oscar Mike (park) · Charlie Mike (resume) · RTB (return to base). |
| **"RTB"** — Romeo Tango Bravo, return to base — **RULED 2026-09-10**, Papi's own coinage ("it'll be RTB… the replacement for sweep") | The parked work returns to base — every keeper in `oscar-mike/` goes home to its real file, the folder is cleared | Walk every card in `oscar-mike/`: promote what earned it into STATE / PROJECTS / its build dir or canon node, delete the rest, update the INDEX, leave the folder empty. Replaces "sweep" (retired 9/10). Spoken alone or as "RTB oscar-mike". |
| **"How copy?"** | End of transmission — acknowledge and execute | Reply opens **"Good copy."** + a one-to-two-line readback of the orders as understood, then execute. **"Solid copy"** = received, nothing to add. Discrepancy or missing piece → **"Bad copy on [item]"** + the single question. Dictation garbles of the phrase ("tell copy", "hell copy") read as "how copy". |
| **"Boresight"** — **RULED 2026-08-21.** Marksmanship: align the sight to the bore so point of aim = point of impact; nothing fires until they agree. Directed form: **"boresight in on [target]"** aims the protocol at a named item (a BOLO, a doc, a decision). Equivalents: "what are you getting from this" · "what's your read on it" | Confirm understanding **before** delivery — the mirror of "how copy". **Only when spoken, never automatic** (ruled 2026-08-21) — the standing cadence stays clean so Papi can get straight to the point | Fixed three-part reply, then hold: **(1) Readback** — the transmission as understood, in own words, nothing skipped. Proof of copy comes before anything else. **(2) The read** — assessment, relevant repo holdings, plan of attack — built answer-first per the Pyramid Principle (ratified BVX doctrine). Plan only, no delivery. **(3) Clarifying questions** — one numbered block, tied strictly to the transmission. Clarify only: no branching, no new material. Loop 1–3 until the chain is walked down; Papi then clears delivery. Rationale: catches drift and premature branching before effort is spent. |
| **A spoken tasking** ("I need to…", "remind me…", "put that down", "add that to the watchlist") | BOLO capture | Write it into [BOLO.md](BOLO.md) **in the same turn it is spoken.** No batching, no end-of-session sweep. A tasking not written down did not happen. |
| **"Ivory tower"** ("what's the ivory tower on this?") — coded 2026-08-21 | Academic mode — answer from the published literature only | Every claim carries its source inline: researcher, year, field. Peer-reviewed beats books beats everything else; pop-sci gets flagged as pop-sci. Mark established vs emerging vs contested. Name the controlling field. Still house format (§7) — the rigor is in the sourcing, never in walls of prose. |
| **"Break-break"** → **"buttonhook back"** — **RULED 2026-08-21** | Detour open / detour close | "Break-break" parks the main thread exactly where it stands and opens the detour. **"Buttonhook back"** closes it: return to the parked thread **unprompted**, restating where we were. Lineage: break-break cuts into ongoing net traffic; the buttonhook hooks off the axis and comes back onto it. |
| **"Run the darkroom"** — coded 2026-09-01. Dictation garbles ("run the black room" · "run the dark room" · "open the darkroom") read the same | Launch the DARKROOM program | Launch immediately, background, no questions: run `python _PRIVATE/taxonomy_engine/darkroom_server.py` (equivalent to the `DARKROOM.cmd` launcher in the corpus root). The server opens the browser itself; its single-instance guard means a second call just brings the live instance up — safe to speak anytime. Confirm with the serving address, one line. |
| **"Belay [that]"** (provisional 2026-09-04; spoken naturally by Papi) | Cancel the immediately preceding order | Strike the order as never given; confirm in three words or fewer; the record keeps the belay line, not the order. Naval lineage: belay = stop, make fast. |
| **"ENDEX"** (provisional 2026-08-21; "Oscar Mike" spoken at session end reads the same) | Stand down — close the session | Run the close-out: write/finalize the Ready Rack session note · update STATE.md (Moved / Blocked / Live) · append the day's journal entry. Autocommit fires on session stop. Radio equivalents: "Out" · "secure the net". |
| **"Status on BOLO N"** / "give me the status on BOLO N" / "the 411 on BOLO N" (provisional 2026-09-10, spoken; page-name bench: **FRAGO** rec — a fragmentary order updates a standing order, brief, action-first · STATUS · THE 411 · OPORD) | That one BOLO's status page — a sit rep for the BOLO, never called one | Build + publish the page: write `_tools/bolostatus/boards/<N>.json` as the **five-paragraph order** (Situation · Mission · Execution · Admin & Logistics · Command & Signal, plus the Log) with the FRAGO strip on top (mission as task + *in order to* · the next action as an order · Papi's calls with defaults that run if silent); `python _tools/bolostatus/build.py N` → `_tools/bolostatus/out/BOLO-N.html` → publish as that BOLO's own artifact (first time: new; after: pass its URL) and write the URL into the BOLO's row. **The three that govern the page (MIL.01 §4, invariant 8): SPEED — read in ten seconds, order on top · FOCUS — one main effort named, everything else supporting and short · BOLDNESS — do not wait for certainty, every call carries a default.** Same colorway, glossary and tooltip engine as the sit rep page; the big GLOSSARY button rides on it. |

---

## 2 · The sit rep — the blocks, fixed order

| Block | Name | Content | Source |
|---|---|---|---|
| **0** | **Last session** | What moved in the previous session — read from the Ready Rack before flushing it | `_CACHE/` |
| **I** | **The Fresh Ten** | Ten projects touched most recently, newest first — last-touched date, one line of context, concrete next step | STATE.md + git log |
| **II** | **The Ancients** | Longest-untouched work, tiered: true ancients → going quiet → recently parked; each with what it is waiting on | STATE.md + PROJECTS.md |
| **III** | **The Deep Stacks** | Volume ranking — content mass per project | PROJECTS.md |
| **IV** | **The BOLO board** | Active BOLOs + the PMCS readiness table | BOLO.md |
| **V** | **Blocked on you** | Numbered decisions in priority order | STATE.md |
| **VI** | **The leverage line** *(provisional rename pending: "The Main Effort" — MCDP 1's term for the one point everything else supports)* | One line naming the single highest-leverage next action | derived |
| **VII** | **The SOI card** *(added by order 2026-08-25)* | The proword shortlist closes every board — commands one-per-bullet with a clause of meaning, board nouns on one line | §0 |

**The front page — coded 2026-09-10.** The board lands as a rendered dashboard, not a scroll: one panel per block, jumped to by key; the explainer register on every panel (what we did last · what the plan was · what you did · what's next, in plain words); every board noun and item a live term with nested tooltips (the CK3 rules, depth 3). **Colorway RULED 2026-09-10 (spoken): the creator-cases explainer's palette (slate ground · white surface · orange accent `#FF5A1F` · green/red status; dark twin) is the default for every internal board and tool page from here — "the default colorway that we just keep using". The ROSE / WATCH "purple" stays with DARKROOM and public-facing, front-of-house work.** Working name for the colorway: BRIEF (unruled). Skin ruled: CK3 information architecture × Death Stranding surface. **The glossary page (ordered 9/10, "how copy"): every proword and board word on one page, reached by a big GLOSSARY button on the sit rep page (and on every BOLO status page); built from the same register the tooltips use (`_tools/sitrep/glossary.json`, 84 terms · 23 prowords, each proword marked ruled / provisional / benched). Deep link: the page URL + `#glossary`.** Pipeline and URL in §1.

**Trunk discipline — coded 2026-08-21, non-negotiable.** Every item on every block carries its trunk: **BLACK** (creative, IP, systems) · **ORANGE** (venture, body, sexuality) · **OPERATOR** (PMCS — the operator is equipment). The board is never delivered trunk-blind. **House names (spoken 2026-09-03): BLACK = Bold Venture (BVX) · ORANGE = Ultrasin.** Everything Papi makes lands in one house or the other. This is how Papi's head sorts; the protocol upholds it everywhere, always.

---

## 3 · The cache — Ready Rack and Magazine

Session continuity runs on ammunition-handling logic:

- **`_CACHE/` — the Ready Rack.** Rounds staged for immediate use. Every working session drops (or updates) one session note here: `YYYY-MM-DD[-n].session.md` — what moved, what was ruled, what is mid-flight. Written at session close or at any milestone worth surviving a crash.
- **The flush.** On every sit rep: read every session note in the Ready Rack, deliver Block 0 from them, then **move them** (not copy, not delete) into `_LOG/`. The Rack returns to empty. An empty Rack is the proof the handoff completed.
- **`_LOG/` — the Magazine.** Deep storage. Flushed session notes live here permanently, filename-dated, append-only. Nothing is ever deleted — it is stowed.
- The `README.md` in each folder states its own rule and never gets flushed.

STATE.md remains the **index** (what is live, what is blocked); the Ready Rack is the **wire** (what just happened). Detail still belongs to the owning registries.

---

## 4 · Session-open reading order

1. **SOP.md** — this file. The protocol itself.
2. **STATE.md** — the index.
3. **BOLO.md** — the watchlist.
4. **`_CACHE/`** — the Ready Rack (flush on sit rep).
5. **PROJECTS.md** — the volume board.

A session that answers "sit rep" without all five has not answered it.

---

## 5 · Open naming rulings on this doc

- **"BOLO"** for the watchlist — **RULED 2026-08-21.** Be On the Lookout, chosen for the bolas echo (the gaucho throwing weapon: thrown on sighting, wraps the target, holds it until you arrive). Retired bench: FRAGO · WARNO · Fire Watch.
- Ready Rack / Magazine — provisional, same session.
- **"Boresight"** for the understanding check — **RULED 2026-08-21.** Struck en route: "back-brief" (lame). Retired bench: AZIMUTH · ZERO · BACK-AZIMUTH · OVERLAY · ECHO · SQUAWK · FIVE-BY · RECON · READBACK · CONFIRMATION BRIEF. **INTEL returns to the pool** — Papi's seed, unassigned, likely future coinage.
- **"Main effort"** as a command proword — **provisional 2026-08-21.** MCDP 1's answer to "this is the main thing, focus here": the designated main effort is the one task everything else supports; all else is supporting effort. Spoken, it names or asks for the single priority. Sit rep Block VI rename to "The Main Effort" rides on the same ruling.
- **The proword selection loop** — **provisional 2026-09-06**, BOLO 37. Papi's order: prowords stop being ruled in-chat one at a time and go through a daily selection pass (description + five candidates, pick three ranked, ten slots a day, Claude's sealed ranking revealed after, run inside every sit rep). Name bench for the loop: **MINT** (rec) · BREVITY · SOI · CALLSIGN · LEXICON. Until it stands, the benches below wait in it, not in chat.
- **The outside-the-wire boresight + the pipeline prowords** — **provisional 2026-09-06**, spoken by Papi on BOLO 35/36 ("is there a word different than boresight… for anything that is on the web or outside of it… I want to be able to say napkin boresight"). **Boresight** stays the vault-facing form (the read draws on repo holdings). Wanted: the same three-part protocol aimed outside the wire (web + literature). Bench: **RECON** (recommended — Marine lineage, "napkin recon" scans, boresight/recon = inside/outside the wire) · **INTEL** (Papi's pooled seed; better as the noun for what recon brings back) · SCOUT · OTH (over the horizon). **NAPKIN** (modifier, provisional): back-of-the-napkin — one pass, rough numbers, no question loop, spoken as a prefix ("napkin boresight", "napkin recon"). Pipeline prowords, provisional: **SYLLABUS** ("pull the syllabus on X" = the tier-one 101 textbooks of a field, ivory tower, one per field to start) · **DISTILL** (make the BVX-LEARN one-sheet — the doctrine's own word, "distill, don't summarize") · **GRAMMAR** ("write the grammar" = derive a system's operating language from its sources). Rulings are Papi's; nothing here is on the SOI card until ruled.
- **The lessons block on every creator case (BOLO 45)** — **provisional 2026-09-10**, spoken by Papi ("yes, it needs a name… derivative of the SOP… the Corps" — dictated "the burning core", §8). The thing: section 10 of every `creator-case-<handle>` node — the one mechanic · transferable tips · does not transfer · feeds. Bench, Corps lineage per §6: **GOUGE** (recommended — Navy/Marine slang for the essential distilled information from someone who has been there, "give me the gouge"; spoken: "the gouge on Siswet"; one word, no collision; dictation risk "gauge", codebook row added) · **TTPs** (Tactics, Techniques and Procedures — the doctrinal name for how an outfit operates; forces study others' TTPs and adopt them; fits the transferable-tips part exactly, less the one-mechanic part) · **THE TAKE** (intel vernacular — the product a collection run brings back; the placeholder until tonight) · **LESSONS LEARNED** (the doctrinal name itself, Marine Corps Center for Lessons Learned; exact by definition, but two words and institutional — it names the discipline, not the block) · **HOT WASH** (the immediate after-action debrief; strong Corps flavor, but it is about one's own action, not a study of someone else's). Sealed ranking: GOUGE · TTPs · THE TAKE. INTEL withheld from this bench — it is Papi's pooled seed, better as the noun for what RECON brings back. Files carry `## 10 · GOUGE` as the provisional header until ruled; rename is one pass.
- **The word for "sweep" (promote the parked keepers to their real homes, clear `oscar-mike/`)** — **provisional 2026-09-10**, spoken by Papi ("sweep… way too generic. I need something more along the lines of Oscar Mike… very clear what it meant"). The thing: the return pass after an Oscar Mike — go back to the rally point, put every keeper where it lives, leave the area clear. Bench, Corps lineage per §6: **POLICE CALL** (recommended — the daily Corps ritual: an organized pass over an area, everything picked up and put where it belongs, area left clear; exact meaning, two crisp words, same cadence register as Oscar Mike; spoken "police call on oscar-mike") · **CONSOLIDATE** (MCDP doctrine — after seizing the objective, consolidate and reorganize: redistribute, secure, prepare; fits the promote-to-homes half more than the clear half; one word) · **RECOVER** (the post-exercise phase — account for every piece of gear and return it to where it lives; exact, but collides with everyday "recover a file") · **FIELD DAY** (Corps/Navy — the scheduled top-to-bottom cleaning of the spaces; strong flavor, but it is the clean, not the promotion; civilian sense collides) · **BREAK CAMP** (pack the bivouac, leave nothing behind; clear half only; "strike camp" collides with STRUCK). **Papi 9/10: that whole bench struck ("I don't like any of that"). CHARLIE MIKE RULED for the third movement, resume the parked card — on the §1 card.** Second bench, on his cue ("what is the word for when everybody reports at this time?"): **MUSTER** (recommended — Navy/Marine: assemble at the set time, everyone present or accounted for, then sent to their posts; as the sweep: the parked items report in, get counted, get sent to where they live, the rally point is left clear; spoken "muster oscar-mike" or just "muster"; garble "mustard", §8) · **FORMATION** (the ground-side word, "morning formation": same idea, but generic in civilian use) · **RECALL** (the summons that brings everyone in — the mechanism, not the pass itself) · **STAND-TO** (dawn and dusk, everyone on position — full alert, the wrong weight for a tidy-up) · **ALL HANDS** (Navy — everyone, but no set-time meaning). Sealed ranking: MUSTER · FORMATION · RECALL. **RULED 9/10 by Papi over both benches: RTB** — Romeo Tango Bravo, return to base, his own coinage: the parked work returns to base, meaning its real home. On the §1 card. "Sweep" retired; POLICE CALL and MUSTER benches retired.
- **"Break-break" / "buttonhook back"** for the detour pair — **RULED 2026-08-21.** Open with break-break, close with buttonhook back. Retired bench: AS YOU WERE · DOGLEG · EXCURSION · HERRINGBONE.

---

## 6 · Lexicon doctrine — the Corps is the bootstrap

**Coded 2026-08-21.** The USMC proword and doctrine vocabulary is a **starting library, not the end-state.** It is adopted wholesale as the bootstrap; native coinages are expected to replace and extend it as the operation matures. The drift into an own language is **intended** — the lexicon is a worldbuilding asset that bleeds into the culture. The model is the Disney effect: code language plus uniform makes the separation between inside-the-operation and the rest of the world clean and total. Ten borrowed words today, ten coined words tomorrow, a house tongue eventually.

---

## 7 · House format — how transmissions are written

**Coded 2026-08-21 after the readback-wall incident.** The rhetoric stays; the formatting serves scanning. This is v0.1 — the full learning-science distill is BOLO 6.

1. **Readbacks are bulleted.** One order per bullet, bold anchor up front. Never a prose wall.
2. **One idea per paragraph, three sentences max.** Working memory holds about four items; the format respects that.
3. **Bold is a signpost, not decoration** — the first words of the point, so the bolds alone tell the story on a scan.
4. **Parallel items go in bullets or tables,** never buried in prose.
5. **Answer-first everywhere** (Pyramid Principle, ratified doctrine).
6. **The Spartan dial: trim words, not meaning.** Complete sentences, nothing ornamental — Laconic, but the message survives whole.
7. **The ten-second test:** headers plus bolds alone must carry the message. If a scan doesn't tell the story, the format failed.
9. **The OUT block** — coded 2026-09-06. Every reply that executes an **Oscar Mike** (or an ENDEX) closes with the end-of-transmission block and nothing after it: a fenced block, blank line above and below the sign-off line, so the seam between the parked thread and the next order is visible at a glance. The form:

```

   OSCAR MIKE  ·  OUT  ·  OUT  ·  OUT

```

   Radio lineage: **"Out"** ends a transmission and expects no reply; repeated three times it is the house's own coinage (§6). Papi's words: "everything is very tightly and compact now, I want a break between when something's Oscar Mike'd and something else starts."

8. **One value, one block** — coded 2026-09-04. Anything Papi has to copy and paste (a path, a name, a command, an exact string) goes in its own fenced code block with nothing else in it, so the chat's copy button grabs exactly that value in one click. Inline backticks are for reading, never for pasting. Several values = several blocks, each labeled by the line above it.

---

## 8 · Dictation codebook — standing garble table

**Coded 2026-09-03.** Papi speaks; a speech-to-text layer types. Claude never hears audio. Proper nouns and numbers are what the recognizer gets wrong; common words come through clean. This table is the read-through. When a transmission contains one of these, read the right-hand column without asking. New garbles get a row the turn they are caught.

| Heard | Read as |
|---|---|
| ultrasound · AutoSun · ultra sin | **Ultrasin** |
| bold adventure · bone fracture · bold vnture | **Bold Venture** (BVX) |
| blamer · blender | **Blender** |
| Doctor NZero · doctor zero | **DOCTRINE 0** |
| SLP (in a process context) | **SOP** |
| hau copy · tell copy · hell copy | **how copy** |
| SIP rep · sip rep · sit rap · set rep · this rep · "me this it, rep" | **sit rep** — the question form ("what is the sit rep") reads as the board, not a request for a definition |
| cornstars | **porn stars** |
| AirSnova · there is nowhere · Aries Nova | **Eris Nova** (performer; spelled out by Papi 9/8) |
| variety eats all | **Variety Itsol** (performer) |
| Lina Vesper (as heard) | **Lina Vesper** (performer; spelling unverified 9/8) |
| black room · dark room | **DARKROOM** |
| bolo · polo (in a tasking context) | **BOLO** |
| break break (×2 or ×3) | **break-break** (nested detours stack) |
| ask her mic · oscar mic · Oscar Mike's | **Oscar Mike** |
| bore side · bore sight | **boresight** |
| MDCP · MDP · CDP one (in a doctrine context) | **MCDP** (MCDP 1 = Warfighting, MIL.01) |
| astrosex · ASTROSE7X | **ASTRO7EX** |
| preserved stools (food context) | preserved **foods** |
| tickling · kavas (food context) | **pickling** · **kvass** |
| standing (in a canning context) | **canning** |
| College shelf · he and (after a code) | **CUL shelf** · **S8** — the BVX-LEARN food shelf and the setting layer, ruled 9/6 |
| Braddy (a mood / attitude context) | **bratty** — spelled out by Papi 9/9 |
| desk training · death training (a UI / design context) | **Death Stranding** (the ruled skin: CK3 UX × Death Stranding UI) |
| CK three · CK-3 | **CK3** (Crusader Kings III; the information-architecture study) |
| Rebel Writer · Rebel Rider | **Rebel Rhyder** (performer — "the NASA girl", RULED 9/10; spelled out by Papi r-e-b-e-l r-h-y-d-e-r) |
| the burning core · burning core (in a naming context) | **the Corps** — SOP §6, the lexicon bootstrap; "derivative of the SOP of the Corps" = a Marine-vocabulary name |
| gauge · gouge (in a creator-case context) | **GOUGE** — the lessons block (section 10), provisional 9/10 |
| our TB · R T B · return to base · sweep (spoken by habit) | **RTB** — return to base: promote the parked keepers, clear `oscar-mike/` (RULED 9/10) |
| Charlie Mike · Charley Mike · CM (spoken alone) | **Charlie Mike** — continue mission, resume the parked card (RULED 9/10) |
| Quinton | Quinn Bishop |
| The Outsiders | **The Outliers** |
| year ranges spoken as "twenty twelve … two thousand five … twenty twenty too" | check against the doc that holds the range before reading a number |
