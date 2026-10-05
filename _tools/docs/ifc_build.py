"""THE INTERFACE CATALOG · build (BOLO 102 stage 2, ruled "go" 10/5).

Usage:  python _tools/docs/ifc_build.py

Writes ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md from
  _tools/docs/out/ifc_candidates.json   (the six extractors' entries, merged by ifc_merge.py)
  the HEAD / CALLS / TAIL text below      (the CDR's design: what an interface is, the id scheme, the calls)
The register is generated; the truth stays in the JSON. Edit the JSON (or re-extract), then rebuild.
Each interface gets an id IF-ab-cd-nn: ab<cd is the unordered system pair, nn its row in that pair.
"""
import io
import json
import os
import re
import sys
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "out", "ifc_candidates.json")
OUT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT", "00_EPISTEMOLOGY", "📐 ssot_00_interface_catalog.md")
NAMES = {"00": "Base", "01": "Narrative frameworks", "02": "Character (LEECHSEED)", "03": "Setting", "04": "Plot",
         "05": "Worldbuilding", "06": "Theme", "07": "Style", "08": "Tracking", "09": "Operations", "ALL": "every system"}
SHORT = {"00": "Base", "01": "Narr", "02": "Char", "03": "Sett", "04": "Plot", "05": "World", "06": "Theme", "07": "Style",
         "08": "Track", "09": "Ops"}
DATE = "2026-10-05"

HEAD = """---
type: ssot_00_epistemology
category: interface_catalog
version: 0.2.0
tier: foundation
last_updated: {date}
reader: "the CDR and the writers, before touching a field another system reads; Chief, ruling the calls"
doc_type: reference
owner: "Chief (HOTLINE ACTUAL); the build script keeps the register"
state: draft
reviewed: {date}
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
trunk: BLACK
status: "v0.2.0 {date}: the ten design calls RULED (Chief: \"My word\"), source-fix batch fired; v0.1.0 {date}: BUILT from the stage 2 extraction (BOLO 102; six MS extractors, one script fan-in); {n_if} interfaces across {n_pairs} system pairs"
purpose: "The between-system map: every place one system hands another a field, an id, a record or a rule, in one register with one id per interface; the wiring findings (what one side states and the other never does); and the design calls that close the gaps."
dependencies: ["_tools/docs/ifc_build.py (the build)", "_tools/docs/out/ifc_candidates.json (the register's truth)", "_tools/docs/out/N2.md (the RECON scan)", "[[📐 ssot_00_variable_registry]]", "[[📐 ssot_00_module_architecture]]", "[[📐 ssot_00_pattern_library]]"]
sources: ["NASA Systems Engineering Handbook, interface management and the N² diagram (Zotero)", "the 58 core docs, read whole by six extractors on {date}"]
---

# 📐 ssot_00_interface_catalog — the between-system map

**Who it's for:** the CDR and the writers, before touching a field another system reads; Chief, ruling the calls · **What it does:** lists every interface between the ten systems, one id each, and the calls that close the gaps · **Type:** reference

## PURPOSE

Chief ordered this on 2026-10-04: "patterns in which possible patterns can influence and interface with each other." The systems were documented one at a time (BOLO 102 stage 1). This doc is the map of where they touch.

The register below is generated. Six extractors read the 58 core docs, one system slice each, and logged every interface from their side. A script merged the six files and numbered the rows. The truth is `_tools/docs/out/ifc_candidates.json`; this page is its printout.

## WHAT AN INTERFACE IS

An interface is a boundary where two systems exchange something (NASA SE Handbook, interface management). The register keeps three kinds apart:

| Kind | Meaning | On the page |
|---|---|---|
| **DATA** | one system produces a field, record, id or structure that another reads | a row |
| **CONTROL** | one system's rule gates, triggers or orders another | a row |
| **MENTION** | a doc cites another for a definition; nothing crosses | the "named only" line under the pair |

Each row carries **direction** (writes · reads · gates · gated_by, from the stating doc's side), the **payload** (the named thing that crosses), the **trigger**, where the stating doc says it, and a **status**: `built` (stated as working) · `parked` (the source marks it phase 2) · `proposed` (the extractor's judgment: the system needs it and the source never says so).

**The id.** `IF-ab-cd-nn`: `ab` and `cd` are the two systems, lower number first; `nn` is the row's place in that pair. A row's id never changes once published; a retired row keeps its id and says so.

**Both sides, as stated.** Each side logged what its own docs say. When A says "I write X to B" and B never says "I read X from A", both rows stand and the gap is a finding (THE WIRING FINDINGS). The catalog records the statements; it does not pretend they agree.

## THE N² GRID

Row = the system whose docs state the interface; column = the other system. Cells count DATA + CONTROL rows (proposed rows in parentheses).

{grid}

{summary}
"""

CALLS = """## THE DESIGN CALLS — RULED {date} (Chief: "My word", all ten as recommended)

The 115 proposed rows fell into ten calls. Chief ruled all ten as recommended on {date}. Each is now a source-fix batch (one MS per system); a row moves from `proposed` to `built` when its fix lands and the register rebuilds.

**1 · One clock.** Fourteen rows date things five different ways: the Tracking time code (`M2 · Q1 · S03 | bar.beat.tick`), the ladder address (`OXO.primary.M2.q3.s12.b4`), movement tags (`m1a`), free text (`STT.narrative_moment`), and calendar years. **Rec:** the 08 time code is the one address for anything dated in any system. 08 gains a section, "The address", that maps the ladder address onto it (movement = M, sequence = Q, scene = S, beat = bar.beat) and lists the fields that must carry it: `STT.narrative_moment`, relationship `state_history.moment`, fabula `time` (beside the calendar year), P11 `order_told`, LEDGER_DUE future states, the hook ledger, the Touchstone breach log, catalog `narrated_in`, CT5 bookends. Free text and movement tags retire as aliases.

**2 · Theme wires in.** Theme (06) names no character id, no plot field and no tracking store, yet its rails name Tori and Anna, L11 DESTINY carries the character's side of the argument, and 08 expects motif ids 06 never mints. **Rec:** 06 gains `holders:` on each rail (08 track ids, `character:tori`); mints `motif.<slug>` ids in THE MOTIFS; the scene card and the plot card both carry a theme record (`rail_tested` R1–R4 · `side_argued` · `gauge` name + step · the citation and transcript tests); 08 `subject.kind` gains `theme` and `gauge`; 02 L11 gains `rail_ref`; genre G4 `core_binary` is handed to 06 as the controlling idea's seed; the spine's L6 theme points at 06's controlling idea; Anna's reader track lives in 08 §9A and 06 cites it.

**3 · The world catalog widens.** Nineteen rows want a field the 05 entry schema lacks. **Rec:** the entry schema gains `gauge:` (value + four steps, civilizations only), `portable:`, `narrated_in:` (a time code), `founded:` and `current:` in place of the one `era:`, `motif_ref:`, `ct11_verdict:` (argues · neutral · undercuts). 08 `subject.kind` accepts 05's kinds (group · belief · custom · tech · wardrobe · architecture) plus `world`. The character's free-text world fields (`system_exposure.layers.regime`, `civic_standing`, `community_membership`, L7 `tech_level`) take a `catalog_ref:`. R8 UNIVERSE and the G8 `world_build` promise point at the catalog.

**4 · The Ownership Rule completes.** The variable registry owns every field but has no prefix for S1–S12 or P1–P12, no rows for 01, 07 or 09, no owner for REL or the storyform record, and a `touchstone` slug that cannot join the TS register. **Rec:** prefixes `SET.` and `PLT.`; rows for 01 (`feeds:`, `module_of:`, spine addresses), 07 (`voice_sheet` as consumer), 09 (front-matter keys); REL.* owned by the 02 state architecture; the storyform record owned by 04; every module variable carries the Static/Dynamic tag; L12 `touchstone` holds the TS n:m id with the slug as alias; the 139-row alias table is cited from the registry.

**5 · The plot–setting handshake.** Eleven rows are fields the fabula, the plot card and the setting slice each expect the other to hold. **Rec:** the fabula event record gains `source_kind:` (03's five categories + character), `canon_source:`, `produces:` (the state_ids it yields) and `scheduled:` (LEDGER_DUE future states). UNDERSIDE_SURFACING hands P7 `reveal_content` / `reveal_type`. P12 records the S12 Domain of a LOAD_BEARING place (`domain_ref`). S8 `witness` takes a character id. The `story_beat` type is the fabula `event_id`. PENDING and FIRED_PRE_STORY flags store their `event_id`. Anna Colson (the copy) gets her own character record.

**6 · The cards carry the checks.** P8–P10 claim every plot element passes the three checks, but only entity sheets hold the fields; hooks and breaches have no ledger. **Rec:** plot card and scene card gain `fantasy:` / `sexy:` / `aesthetic:`; 08 §9A gains a hook ledger (type · container · payoff address) beside the payoff ledger, and a Touchstone breach log (address · TS id · invalidated units); the scene card gains `focal:`; 07.1 sets the beat-boundary mark in prose so 08 can count tempo.

**7 · Style names its inputs.** 07.1 reads five things it never names. **Rec:** 07.1 lists them: the medium (01, M1 = prose) selects it; texture's T6 register and distance values are the terms it applies; 05's LNG entries are the unexplained-word list; 08's planned tempo is an input; 06's motif list routes sensory detail. The 06 citation test and 07.1's "narration never states motive" do not clash: the test runs on the scene plan, not the narrated text; one sentence in 06 says so. 07.3 names the world view page and the workspace arrangement view as pages it rules. The truth table (00) gains rows for 01 (a framework fits its text) and 07 (a voice holds: Coherence).

**8 · Base 60 and the truth check scope.** Base 60's purpose says every system; its scope says the character pipeline. **Rec:** the scope line becomes "every scaled number in any system"; S- and P-layer numerics take SC classes; time codes do not (an address is not a scale). The truth check's `checked | open` status and the checking framework sit on the claim's own record in its owning doc, not in 08.

**9 · Operations files true.** A 02 module and a 00 design system sit in 09; the flow's "vertical slice" collides with the LEECHSEED Vertical Slice; eleven 01 docs lack `rung:`. **Rec:** `ssot_00_process_illustration_character_pipeline` moves to 02; `ssot_00_bold_venture_design_system` moves to 00; the flow's P3 is renamed "proof slice"; Flow D adds the setting-state check beside the relationship check; `rung` and `trunk` join the AIP's required keys and a script backfills `rung:` on every core doc; `#ssot-candidate` promotion names its folder through the AIP table; 3A narratology output files to the 01 narratology shelf; Theme Report throughline data flows to the Dramatica ingest (02) and 06 reads the result.

**10 · One of each.** Two trope keyings, two genre tools, two "scale ladders", two 1.0 bars. **Rec:** the trope register's `register.json` is the one key store and the trope graph reads it; Ryan's nine-axis scoring is the genre-contract tool for 03 and 01 both (Baur stays as lineage); "scale ladder" is 01's R1–R8 and 05's three tiers are renamed "the reach"; the 1.0 bar is SOP §5's six (Shape · Shelf · Proof · Ruled · Wired · Store) and 06's own list retires.

**With the rulings:** the one-sided pairs in THE WIRING FINDINGS close by one line each: the silent side names the interface by its IF id. One MS per system, one pass, fired {date}.

"""

TAIL = """## VERSION HISTORY

- **0.2.0 · {date}** — RULED: all ten design calls as recommended (Chief: "My word"); the source-fix batch and the catalog's four pages fired the same turn. Two files moved under call 9: the character pipeline to 02, the design system to 00.
- **0.1.0 · {date}** — BUILT (BOLO 102 stage 2, Chief: "go"). Six extractors, {n_entries} rows, {n_if} interfaces across {n_pairs} pairs; ten design calls OPEN with recs. Built on Fable (SOP §7 rule 21, the model call).
"""


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def main():
    E = json.load(io.open(SRC, encoding="utf-8"))
    pairs = defaultdict(list)
    for e in E:
        a, b = e["from_sys"], e["to_sys"]
        key = (a, b) if b == "ALL" else tuple(sorted((a, b)))
        pairs[key].append(e)
    order = {"DATA": 0, "CONTROL": 1, "MENTION": 2}
    stat = {"built": 0, "parked": 1, "proposed": 2}
    n_if = 0
    reg = []
    for key in sorted(pairs, key=lambda k: (k[0], k[1] if k[1] != "ALL" else "99")):
        rows = sorted(pairs[key], key=lambda e: (order[e["kind"]], stat[e["status"]], e["from_sys"], e["from_doc"]))
        a, b = key
        title = f"### {a} {NAMES[a]} ↔ {b} {NAMES[b]}" if b != "ALL" else f"### {a} {NAMES[a]} → every system"
        reg.append(title + "\n")
        reg.append("| id | side | kind | payload | trigger | stated in | status |\n|---|---|---|---|---|---|---|")
        mentions = []
        taken = [int(e["id"].rsplit("-", 1)[1]) for e in rows if e.get("id")]
        nxt = max(taken) + 1 if taken else 1
        for e in rows:
            if e["kind"] == "MENTION":
                mentions.append(f"{e['from_doc']} → {e['to_doc']}")
                continue
            n_if += 1
            if not e.get("id"):            # an id never changes once published; new rows take the next number
                e["id"] = f"IF-{a}-{b}-{nxt:02d}"
                nxt += 1
            iid = e["id"]
            side = f"{e['from_sys']} {e['direction']}"
            where = f"{e['from_doc']} › {e['where']}" if e["where"] else e["from_doc"]
            note = f" *({esc(e['note'])})*" if e["note"] else ""
            reg.append(f"| `{iid}` | {side} | {e['kind']} | {esc(e['payload'])}{note} | {esc(e['trigger']) or '—'} | {esc(where)} | {e['status']} |")
        if mentions:
            reg.append(f"\nNamed only: {'; '.join(sorted(set(mentions)))}.")
        reg.append("")

    # grid
    keys = [k for k in NAMES if k != "ALL"]
    cell = defaultdict(lambda: [0, 0])
    for e in E:
        if e["kind"] == "MENTION" or e["to_sys"] == "ALL":
            continue
        c = cell[(e["from_sys"], e["to_sys"])]
        c[1 if e["status"] == "proposed" else 0] += 1
    g = ["| states → other | " + " | ".join(f"{k} {SHORT[k]}" for k in keys) + " |", "|---|" + "---|" * len(keys)]
    for r in keys:
        cells = []
        for c in keys:
            if r == c:
                cells.append("■")
            else:
                b, p = cell[(r, c)]
                cells.append(("·" if not b and not p else f"{b}" + (f" ({p})" if p else "")))
        g.append(f"| **{r} {SHORT[r]}** | " + " | ".join(cells) + " |")
    grid = "\n".join(g)

    # wiring findings
    wired = [e for e in E if e["kind"] == "DATA" and e["status"] != "proposed" and e["to_sys"] != "ALL"]
    reads = {(e["to_sys"], e["from_sys"]) for e in wired if e["direction"] == "reads"}
    writes = {(e["from_sys"], e["to_sys"]) for e in wired if e["direction"] == "writes"}
    closed = {(e["from_sys"], e["to_sys"]) for e in wired if "silent side named it" in e["note"]}   # the apply batch closed it
    closed |= {(b, a) for a, b in closed}
    one_w = sorted((writes - reads) - closed)
    one_r = sorted((reads - writes) - closed)
    n_pairs = sum(1 for k in pairs if k[1] != "ALL")
    kinds = Counter(e["kind"] for e in E)
    props = sum(1 for e in E if e["status"] == "proposed")
    summary = (f"**{len(E)} rows · {n_if} interfaces (DATA {kinds['DATA']} · CONTROL {kinds['CONTROL']}) · "
               f"{kinds['MENTION']} named-only citations · {props} proposed · {n_pairs} of 45 system pairs touch.**")

    findings = ["## THE WIRING FINDINGS", "",
                "A DATA row is one-sided when one system states it and the other never does. The silent side is the gap. "
                "A pair leaves this list when the silent side names the interface by its id (the apply batch) or logs its own row.", "",
                "**Stated as written, never stated as read** (A → B): " + ", ".join(f"{a}→{b}" for a, b in one_w) + ".", "",
                "**Stated as read, never stated as written** (B reads A): " + ", ".join(f"{a}→{b}" for a, b in one_r) + ".", "",
                "Each closes by one line on the silent side naming the IF id. The fix batch runs after the calls are ruled.", ""]

    head = HEAD.format(date=DATE, n_if=n_if, n_pairs=n_pairs, grid=grid, summary=summary)
    body = head + "\n## THE REGISTER\n\nOne subsection per system pair, lower number first. Rows: DATA then CONTROL; built, parked, then proposed.\n\n" \
        + "\n".join(reg) + "\n" + "\n".join(findings) + "\n" + CALLS.format(date=DATE) + TAIL.format(date=DATE, n_entries=len(E), n_if=n_if, n_pairs=n_pairs)
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(body)
    io.open(SRC, "w", encoding="utf-8").write(json.dumps(E, ensure_ascii=False, indent=1))   # ids written back
    print(f"interface catalog · {len(E)} rows · {n_if} interfaces · {n_pairs} pairs · {len(body)//1024} KB → {os.path.relpath(OUT, ROOT)}")
    print("one-sided writes:", len(one_w), "· one-sided reads:", len(one_r))


if __name__ == "__main__":
    main()
