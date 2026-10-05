# BOLO 102 stage 2 · the interface layer · extractor brief (MS, one per slice)

Repo root: C:\Users\U01_LEECHSEED\Desktop\_setsunadev. Write UTF-8.

Chief ordered stage 2 on 10/5 ("go"): the between-system map, "patterns in which possible patterns can influence and interface with each other". The CDR writes the interface catalog. You extract, for YOUR SLICE of systems, every interface your systems have with the other systems. You read your slice's core source docs (`ShroomsQ/_CANON/_SSOT/<system>/*.md`, top level only; not shelves, not `_history`). Nothing else.

## What an interface is (NASA Systems Engineering Handbook, interface management)

An interface is a boundary where two systems exchange something. Three kinds:

| Kind | Meaning | Example |
|---|---|---|
| **DATA** | one system produces a field, record, id or structure that another system reads | the LEECHSEED character system's `T2.WOUND.*` fields feed the plot card's seat |
| **CONTROL** | one system's rule gates, triggers or orders another | BOLO 100: no pilot writing until the fabula is built |
| **MENTION** | a doc only cites another for a definition or a cross-reference; nothing crosses | "see the texture layer for the term" |

DATA and CONTROL are interfaces. MENTION is not; log it only as `kind: MENTION` with no payload, so the CDR can tell "named" from "wired".

## Write

One file: `_tools/docs/work/ifc/<slice tag>.json`, a JSON list. One entry per interface, in this exact shape:

```json
{
 "from_sys": "02", "to_sys": "04",
 "from_doc": "ssot_02_character_systems_vertical_slice", "to_doc": "ssot_04_plot_system",
 "kind": "DATA",
 "direction": "writes",
 "payload": "T2.WOUND.wound_type, T3.DRIVE.want_vector (the seat fields the plot card reads)",
 "trigger": "when the writer builds a plot card",
 "where": "THE INSTANCE › Structured Data Block",
 "status": "built",
 "evidence": "the plot card reads the character's wound and want from the structured block",
 "note": ""
}
```

Field rules:
- `from_sys` / `to_sys`: the two-digit system numbers (00 Base · 01 Narrative · 02 Character · 03 Setting · 04 Plot · 05 Worldbuilding · 06 Theme · 07 Style · 08 Tracking · 09 Operations). `from_sys` is always a system in YOUR slice. Record the interface from your system's side only; the other side's extractor records its side.
- `direction`: `writes` (your system produces it for the other), `reads` (your system consumes the other's), or `gates` (CONTROL: your system's rule governs the other) / `gated_by` (the other's rule governs yours).
- `payload`: the named thing that crosses: field paths, id formats, record names, structures. Use the source's exact names. For CONTROL, the rule in one line. Never a vague "information".
- `trigger`: when the exchange happens, in the source's words. `""` if the source does not say.
- `where`: the section (H2 › H3) of your source doc that states it.
- `status`: `built` (the source states it as working) · `parked` (the source marks it phase 2 or ⏸) · `proposed` (your judgment: the source should consume/produce this but does not say so; see below).
- `evidence`: one quote from the source, 25 words at most, verbatim.
- `note`: anything the CDR must know (a contradiction, an alias, a renumber leftover). Usually `""`.

## The judgment part: silent needs

After the stated interfaces, add `status: "proposed"` entries where your system clearly needs something from another system (or should hand something over) and the source never says so. Ground it in the source: `evidence` quotes the line that implies the need, `note` says why. These are the gaps stage 2 exists to find. Be specific; a proposed entry with a vague payload is worth nothing.

## Rules

- Every entry comes from a line you read. No invented field names.
- Systems were renumbered 10/5 (05 Worldbuilding · 06 Theme · 07 Style · 08 Tracking · 09 Operations); some source prose may still carry old numbers. Record the NEW numbers.
- The character system is the LEECHSEED character system.
- Do not edit any doc. Do not consult other agents. Validate your JSON (run `python -c "import json;json.load(open(r'<path>',encoding='utf-8'))"`) before you reply.

## Reply

Two lines: entries written (DATA · CONTROL · MENTION · proposed) · the one interface you found most surprising.
