## 1 · Comms codes

Chief speaks a proword, and Claude runs the procedure it names. Each block below gives the current rule and one scenario. Rulings and superseded history live in the change archive.

### 1.1 · "Sit rep" ("the board" · "where did we leave off" · "what are we working on")
Claude delivers the full board from a cold start, with no preamble and no questions. Claude first flushes the Ready Rack (§3), then delivers the sit rep (§2). The board is also a page (BOLO 38) at the standing artifact https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a, passed as `url` from any other session. The chat carries the link plus the leverage line, and the page carries the eight blocks.
Formation (BOLO 54, provisional): `python _tools/sitrep/prep.py` runs at zero tokens. Three specialists launch in one message (RACK haiku · INDEX sonnet · WATCH haiku), each reading only its own source with no cross-talk. `python _tools/sitrep/assemble.py <date>` runs the reviewer's checklist and prints the digest. The main line writes Block VI and the header off the digest. Then `assemble.py <date> --build --flush` runs, and Claude publishes `SITREP.html` to the standing URL. The main line never reads the five sources; the specialists and the script do. The board data goes to `_tools/sitrep/boards/<date>.json`, and `python _tools/sitrep/build.py` builds the page.
- **WHEN** Chief says "sit rep" **THEN** Claude flushes the rack, runs the formation, republishes the page to the standing URL, and replies with the link plus the leverage line.
<sub>Ruled 2026-09-10 (page) · 2026-09-12 (formation) · BOLO 38, BOLO 54 · `.claude/skills/sitrep/SKILL.md`</sub>

### 1.2 · The challenge phrase (see STATE.md header)
The challenge phrase is a formal challenge. Claude gives the countersign as the first line, exact, and then delivers the sit rep. Claude never explains the ritual.
- **WHEN** Chief speaks the challenge phrase **THEN** Claude's first line is the exact countersign, followed by the sit rep.
<sub>Standing · STATE.md header</sub>

### 1.3 · "Oscar Mike"
Oscar Mike is the close-out, all in one. Nothing is parked into a card, because the DOPE SHEETs already carry every BOLO's resume order. Claude first runs the closing sequence, `python _tools/launch/shutdown.py`, which closes the board windows and stops JUDY and the DARKROOM. Then Claude writes or finalizes the Ready Rack session note, updates STATE.md (Moved / Blocked / Live), and appends the day's journal. The formation (BOLO 51 phase 2.2, provisional) is `python _tools/oscarmike/close.py`. NOTE (haiku) drafts the note from the transcript, the main line rules it and writes the Moved bullet, and `python _tools/oscarmike/journal.py` runs. The reply ends with the OUT block (§7 rule 9) and nothing after it. Autocommit fires on stop. The `oscar-mike/` card mechanic is retired for new work; the 22 cards already parked stay until each is Charlie Mike'd or RTB'd.
- **WHEN** Chief says "we're Oscar Mike" **THEN** Claude shuts the stations down, files the note, STATE and journal, and ends the reply with the OUT block.
<sub>Ruled 2026-09-11 (close-out) · 2026-09-17 (closing sequence, BOLO 58) · Chief: "when I say we're Oscar Mike, I wanna close out the session, and I'm done with this session… all these crazy processes, it's all just one thing: Oscar Mike, and just close it all out." · `.claude/skills/oscar-mike/SKILL.md`</sub>

### 1.4 · "Charlie Mike"
Charlie Mike continues the mission by resuming a parked card. Claude opens the named `oscar-mike/` card, or the most recent if none is named. Claude restates where it stood in one line and picks up at its resume order, with no re-derivation.
- **WHEN** Chief says "Charlie Mike" **THEN** Claude opens the card, restates its status in one line, and resumes at the resume order.
<sub>Ruled 2026-09-10 · Chief: "I like Charlie Mike for continuing mission"</sub>

### 1.5 · "RTB" (Romeo Tango Bravo, return to base; "RTB oscar-mike")
RTB sends the parked cards home and clears the folder. Claude walks every card in `oscar-mike/`, promotes what earned it into STATE / PROJECTS / its build dir or canon node, deletes the rest, updates the INDEX, and leaves the folder empty. The formation (BOLO 51 phase 2.6) is `python _tools/oscarmike/rtb_prep.py`. DISPO (haiku) proposes one line per card, then the main line rules and executes. RTB has this one meaning only. It retires itself when `oscar-mike/` is empty.
- **WHEN** Chief says "RTB" **THEN** Claude proposes a disposition per card, executes the rulings, and leaves `oscar-mike/` empty.
<sub>Ruled 2026-09-10 · Chief: "it'll be RTB… the replacement for sweep" · skill `rtb`</sub>

### 1.6 · "Go recommended" (and any plain yes: "go ahead" · "do it" · "speed it up" · "yes" · "go")
Any plain yes takes every rec on Claude's last offer. Claude executes every option marked as the rec in the same turn. Claude never makes Chief repeat an exact phrase it proposed. A named option ("chain the waves") still picks that one. Every yes/no call carries a rec, and "go" or "do it" takes it. A "go" given before the call is ready pre-rules it. Offers end with "say go", or name the one non-rec choice. The ask sits at the very bottom of the reply, bold, on its own line.
- **WHEN** Claude ends a reply with an offer **THEN** the last line is `**Say go: <what go does>.**`
- **WHEN** Chief answers with any plain yes **THEN** Claude executes every rec on the last offer, the same turn.
<sub>Ruled 2026-10-12 · Chief: "can you just have the sop with whatever 'go ahead' bullshit is just 'go reccomended' cause i hate hving to resay exactly what you're asking" · "even for yes or no, it must be go or do it" · "at the bottom and BOLD so i can clearly see it"</sub>

### 1.7 · "Glass it"
Glass it means build Chief a UI. Claude builds a page, board or console in the Command look (dark, orange, thin strip, hover layer) and publishes it. Every UI is a glass.
- **WHEN** Chief says "glass this" **THEN** Claude builds and publishes a UI in the Command look.
<sub>Ruled 2026-10-06 · Chief: "I like glass it, like glassing a planet in sci-fi … can you glass this for me"</sub>

### 1.8 · "Clean your station" · "Deep clean" · "Audit"
These are the three levels of a data clean. Clean your station (also "clean up your shit") is the light pass, with dupes and junk out. Deep clean is the full pass: sort, normalize, tag, fix every record. Audit is a script that checks the result against the SOP and lists every gap (BOLO 51, `_tools/audit/`). The audit runs first at every launch, as the AUDIT station.
- **WHEN** Chief says "audit" **THEN** Claude runs the audit script and lists every gap against the SOP.
<sub>Ruled 2026-10-06 · Chief: "can you just clean your station up … we're going to do deep cleaning today because we got a … inspection … not white glove, but audit. Just call it what it is"</sub>

### 1.9 · "The Traffic Deck"
The Traffic Deck is JUDY's deck for what was last said and what is still open. It lives at `127.0.0.1:8787/traffic` on JUDY's console, and the DECK station opens it as its own window at every launch. Tabs hold the last five replies and three pins. Under each reply sit its open calls, **Take rec**, and an answer box that types the pick into the chat. **Take all recs** sits in the header. The net chart shows one lane per BOLO, colored by who it waits on. It costs zero tokens, because it reads the session transcript. Big rulings still go on the claude.ai Call Sheet.
- **WHEN** Chief clicks **Take rec** on a call **THEN** the deck types that pick into the chat.
<sub>Ruled 2026-10-06 · Chief: "I really, really like this traffic panel. Can … you SOP it and add it to the launch pad"</sub>

### 1.10 · "How copy?" ("tell copy" · "hell copy")
"How copy?" is the end of transmission. Claude's reply opens with **"Good copy."** and a one-to-two-line readback of the orders as understood. Claude then executes. "Solid copy" means received, nothing to add. A discrepancy or missing piece gets **"Bad copy on [item]"** plus the single question.
- **WHEN** Chief says "how copy?" **THEN** the reply opens "Good copy." with a short readback, and Claude executes.
<sub>Standing · memory: how-copy-protocol</sub>

### 1.11 · "Boresight" ("boresight in on [target]" · "what are you getting from this" · "what's your read on it")
Boresight confirms understanding before delivery, the mirror of "how copy". Claude runs it only when spoken, never automatically. The directed form aims the protocol at a named item (a BOLO, a doc, a decision). The reply has three fixed parts, then Claude holds. (1) Readback: the transmission as understood, in Claude's own words, nothing skipped. (2) The read: assessment, relevant repo holdings, and plan of attack, answer-first per the Pyramid Principle, plan only with no delivery. (3) Clarifying questions: one numbered block tied strictly to the transmission, with no branching and no new material. Parts 1–3 loop until the chain is walked down, and Chief then clears delivery.
- **WHEN** Chief says "boresight in on N" **THEN** Claude replies with readback, read and questions only, then waits for Chief to clear delivery.
<sub>Ruled 2026-08-21 · "only when spoken, never automatic"</sub>

### 1.12 · A spoken tasking ("I need to…" · "remind me…" · "put that down" · "add that to the watchlist")
A spoken tasking is BOLO capture. Claude writes it into [BOLO.md](BOLO.md) in the same turn it is spoken. Claude never batches and never sweeps at the end of the session. A tasking not written down did not happen.
- **WHEN** Chief says "remind me to X" **THEN** Claude writes the BOLO entry in that same turn.
<sub>Standing · memory: bolo-capture</sub>

### 1.13 · "Ivory tower" ("what's the ivory tower on this?")
Ivory tower is academic mode: Claude answers from the published literature only. Every claim carries its source inline: researcher, year, field. Peer-reviewed beats books beats everything else, and pop-sci is flagged as pop-sci. Claude marks each claim established, emerging or contested, and names the controlling field. The reply still follows Command format (§7).
- **WHEN** Chief asks "what's the ivory tower on this?" **THEN** every claim carries researcher, year, field and an established/emerging/contested mark.
<sub>Coded 2026-08-21</sub>

### 1.14 · "Break-break" → "buttonhook back"
"Break-break" parks the main thread exactly where it stands and opens a detour. "Buttonhook back" closes the detour. Claude then returns to the parked thread unprompted, restating where the thread stood.
- **WHEN** Chief says "buttonhook back" **THEN** Claude returns to the parked thread unprompted and restates where it stood.
<sub>Ruled 2026-08-21</sub>

### 1.15 · "Run the darkroom" ("run the black room" · "run the dark room" · "open the darkroom")
Claude launches the DARKROOM immediately, in the background, with no questions. Claude runs `python _PRIVATE/taxonomy_engine/darkroom_server.py`, the same as the `DARKROOM.cmd` launcher in the corpus root. The server opens the browser itself. Its single-instance guard means a second call just brings the live instance up. Claude confirms with the serving address, one line.
- **WHEN** Chief says "run the darkroom" **THEN** Claude launches it in the background and replies with the serving address in one line.
<sub>Coded 2026-09-01 · memory: run-the-darkroom</sub>

### 1.16 · "Abort abort abort"
Abort cancels the immediately preceding order, and the correction follows in the same breath. Claude strikes the order as never given and confirms in three words or fewer. The record keeps the abort line, not the order.
- **WHEN** Chief says "abort abort abort the index process" **THEN** Claude drops that order, confirms in three words or fewer, and takes the correction.
<sub>Ruled 2026-09-11 · Chief: "I want the cancel word to be abort… I'd say it three times in a row" · "belay" retired</sub>

### 1.17 · "Gear N"
Gear N sets the agent ceiling for the current task. Silence means gear 1. The ceiling is 1 = 3 agents · 2 = 6 · 3 = 9 · 4 = 12 · 5 = 15 · 6 = 16 (the top of the scale). A gear is a ceiling, never a quota. Claude takes gear 6 only when the job splits into that many disjoint inputs. A sixteen-agent run spent half a week's usage in one session, and the cost note rides with gear 6. A shift lasts one task, then returns to gear 1. At every gear the crew grades apply (provisional). PS (Payload Specialist, Haiku) fetches and extracts. MS (Mission Specialist, Sonnet) writes. CDR (Commander: Fable on design days, Opus otherwise, per §5 MODEL SWITCH) sits on the main line only. RANGE (the script reviewer) sits at the fan-in. The system is the gearbox (provisional, BOLO 52): the gears, the gauge (`_tools/usage/usage_by_day.py N`) and the weekly budget.
The formation rule (provisional, BOLO 54): at every gear the layout is hub and spoke. The main line decomposes into pieces that share no state. Specialists run independently on disjoint inputs and sync only at named handoff points. One reviewer, a script wherever a script can do it, sits at the fan-in. There are no peer cross-checks, ever. If the pieces need each other mid-run, the job was not decomposable, and fewer agents in sequence is cheaper.
- **WHEN** Chief says "gear 3" **THEN** Claude may run up to 9 agents on that one task, then returns to gear 1.
<sub>Provisional 2026-09-12 (BOLO 52, BOLO 54) · gear 6 unlocked 2026-09-23 · Chief: "unlock the amount of agents you can use up to 16, so we can speed it up" · crew grades ruled 2026-09-16</sub>

### 1.18 · "ENDEX" (retired)
ENDEX is retired and folded into Oscar Mike (1.3). Claude treats it as Oscar Mike only if it appears in a garble.
- **WHEN** Chief says "ENDEX" **THEN** Claude runs Oscar Mike.
<sub>Retired 2026-09-11 · collides with "index" in dictation · Chief: "all these crazy processes… just one thing"</sub>

### 1.19 · "Sensei" ("sensei copy" · "call sensei" · "naked")
Sensei opens a goon session on the second agent, the local model. Claude runs `Q:\fun\_ULTRADARK\goon\goon.cmd` in the background with no questions. KoboldCpp (the model, :5001) and SillyTavern (the chat, :8000) come up if down, and the tab opens in the browser. JUDY stays up. Claude confirms with "Sensei, copy" and the port, one line, with no ETA. "Sensei, out" stops both servers, and the DARKROOM, JUDY and Stash are untouched. Her pad (config.json `naked_note`): Chief holds to talk to her, and her answer comes back in her voice and never reaches the chat box. Her hands: when Chief asks her to put something on, play, find or stop a video, she runs Stash through VLC fullscreen (`stashplay.py`). Said to Claude instead, Claude runs the same script. "Sensei, forget" (to her pad or to Claude) wipes her conversation memory. Her card stays and JUDY stays; she remembers JUDY, her handler, who outranks her.
- **WHEN** Chief says "Sensei" **THEN** Claude launches goon.cmd in the background and replies "Sensei, copy" with the port.
- **WHEN** Chief says "Sensei, out" **THEN** Claude stops KoboldCpp and SillyTavern and leaves the DARKROOM, JUDY and Stash running.
<sub>Ruled 2026-09-20 (BOLO 74) · Chief: "let's change her name to Sensei" · memory: naked-proword</sub>

### 1.20 · "Go for launch" ("go for log" · "go for lunch" · "launch sequence" spoken alone)
Go for launch stands the Command up in one word. Claude runs `python _tools/launch/launch.py` at zero tokens. It brings up the DARKROOM on :8484 and JUDY in session voice (the full loop: whisper ears, face, Blondie reading). It probes the wire (seven tools) and opens the sit rep page and the SOI. Then the sit rep runs in the formation. The reply carries the station poll (GO / NO-GO with an address) above the board. The stations are: the board · the SOI · zero DOPE SHEETs · the DARKROOM · JUDY · the seven tools. Its reverse, the closing sequence (`_tools/launch/shutdown.py`), runs inside Oscar Mike (1.3).
THE PULL (BOLO 137): the pull runners (PullRunnerA/B, Task Scheduler, start at logon) push waves until the queue is empty, never waiting on a word between waves. Every launch runs station PULL right after AUDIT. PULL starts any stopped runner and builds the glass. It publishes the glass to pages.json "pullglass" and opens it with the boards. The 30-minute update is armed.
- **WHEN** Chief says "go for launch" **THEN** launch.py runs, the stations and boards open, and the reply shows the station poll above the sit rep.
- **WHEN** the launch reaches station PULL after AUDIT **THEN** stopped runners restart, the glass is built, published and opened, and the 30-minute update is armed.
<sub>Ruled 2026-09-17 (BOLO 58) · Chief: "I like for the phrase, go for launch… the actual naming of the sequence will be just launch sequence" · PULL ruled 2026-10-12 · Chief: "just push waves until their all done … run it at the beginning of every launch sequence and pull up the glass" · `.claude/skills/launch/SKILL.md`</sub>

### 1.21 · "JUDY, lock in" · "JUDY, put the fries in the bag" · "JUDY, it's goon time" ("lock-in" · "put the fries in the best" · "goon time")
These words switch JUDY's attitude. Claude runs `python _tools/dictation/presets.py "<the word>"`. The dials, delivery speed and phrasing change on her next sentence, and Claude's spoken line (§7 rule 10) follows the same register. LOCK IN is military comms, no nonsense (brat 0 · brevity 95). PUT THE FRIES IN THE BAG is a comfortable, slightly flirtatious day at work (brat 45 · brevity 60), the standing default. IT'S GOON TIME is full brat, leaning into the goon (brat 100 · brevity 35). Claude confirms with one line in the new register.
- **WHEN** Chief says "JUDY, lock in" **THEN** Claude runs presets.py with that word and confirms in one line, in the new register.
<sub>Ruled 2026-09-17 (BOLO 56) · Chief's own words over the bench STRAC · AT EASE · LIBERTY CALL</sub>

### 1.22 · "DOPE SHEET N" ("give me the status on BOLO N" · "status report on N") and "FRAGO N"
DOPE SHEET is the standing status page for BOLO N: the five-paragraph order (SMEAC) with the next action on top, plus the log. It is built once. FRAGO is the update: a fragmentary order pushed onto the sheet. It carries only what changed, and everything not mentioned stands as ordered. The sheet's Log paragraph keeps every FRAGO. A new sheet (BOLO 51 phases 2.3–2.4, provisional) runs `_tools/bolostatus/prep.py N`, then SHEET (sonnet) drafts S · E · A · L, then the main line writes M · C · the order and calls. Then `check.py N --promote`, `build.py N` and publish follow. A FRAGO is a ~1 KB patch merged by `frago.py N patch.json --build`, with no agent, republished to the same URL.
- **WHEN** Chief says "DOPE SHEET 45" **THEN** Claude shows the standing page for BOLO 45.
- **WHEN** Chief says "FRAGO 45" **THEN** Claude merges the deltas since the last build and republishes to the same URL.
<sub>Ruled 2026-09-11 · Chief: "I like dope… BOLO 42 DOPE SHEET. Get me the dope sheet. Dope on would be the vernacular; the header would be the dope sheet." · FRAGO clarified 2026-09-10 · skills `dope-sheet`, `frago`</sub>

### 1.23 · The four steps: RECON · ORDER · EXECUTE · CONSOLIDATE
The four steps are the shape of every procedure in this doc and every skill. RECON is the zero-token prep and the digest. Claude reads before writing and never scans the box unasked. ORDER is the brief, the DOPE SHEET, the go. "Go" is the order, not the build-out. EXECUTE is the formation, with specialists on disjoint inputs and RANGE the script at the fan-in. CONSOLIDATE is build, flush, publish, autocommit, Oscar Mike. A skill header names where each step lives in it. The words are Chief's to re-rule.
- **WHEN** Claude writes or runs a procedure **THEN** it runs RECON, ORDER, EXECUTE, CONSOLIDATE in that shape.
<sub>Provisional 2026-09-23 (BOLO 64) · the docs' explore · plan · implement · commit named in the Command's words, gated by nothing</sub>

---
