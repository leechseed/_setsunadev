---
name: collect
description: Run a link-harvest research pass in the formation (BOLO 51 phase 2.7; the LOCI six-step collect and the standards register are its instances) — a script fetches every link to text, Payload Specialists (PS, haiku) extract per batch, one Mission Specialist (MS, sonnet) writes the register, a script proves every link is covered. Fires on "collect the locus", "pull every link in …", "build the register from the harvest", "run the locus".
---

# Collect — the harvest formation

**Steps (BOLO 64, provisional 9/23):** RECON = the script fetches every link to text · ORDER = the PS batches · EXECUTE = PS extract, one MS writes the register · CONSOLIDATE = the script proves every link covered.

Use when a file holds a list of links (a locus, a harvest, a syllabus) and the job is to turn them into one register. Not for a single lookup.

## H0 · Fetch (zero tokens)

```
python _tools/loci/collect.py <locus.md> [--limit N] [--batch N] [--gear N] [--resume] [--check] [--wide] [--narrow 3,7,12]
```

Every URL fetched over curl (the box's python cert store is stale) to `_tools/loci/work/<name>/<nnn>.txt` (tags stripped, capped 120 KB), plus `manifest.json` and the briefs. Dead links (403, 0) are reported, not retried by agents. If most links die behind a bot wall, stop and say so; do not send agents to fetch what the script could not.

**Effort table (mar-02).** 12 links or fewer: one PS, no fan-out. 13 to 36: up to three PS. More: the script prints "gear call needed: N links" and stops. Pass `--gear N` once Chief rules it. The digest line names the chosen effort.

**Check first (aas-07).** `--check` validates the locus file, counts the links, prints the effort row it would take and a cost floor (links times the per-link constants in the `COST` dict at the top of `collect.py`), then exits without fetching. Every real run appends one line per step to `work/<name>/trace.jsonl` (time, step, batches, links, files written, seconds).

**Wide, then narrow (mar-08).** `--wide` has the PS batches extract only title, one-line abstract and source quality per link into `wide.k.json`; once they land, rerun `--wide` and the script prints a numbered list and stops. The order is wide, then the CDR marks the numbers worth a full read, then `--narrow 3,7,12`, which reuses the fetch, reruns the full extract on only those links (`extract.nK.json`) and writes the register brief.

**Plan file (mar-03).** The script writes `plan.md` in the work folder: the question, the batch split, the stop rule, the time. On a rerun it prints "resuming plan from <time>".

**Briefs (mar-01, mar-05).** Every brief has four parts: OBJECTIVE, OUTPUT, SOURCES AND TOOLS, BOUNDARY. Each also carries a turn cap and a hand-back cap (150 words). The PS brief prefers primary sources and marks SEO farms, listicles and reposts `quality: low`.

## H1 · Fan out

Launch **EXTRACT-1 … EXTRACT-k** (haiku) in one message, each with its brief verbatim. The effort table sets the count; the gear caps it. Never one agent per link.

With `--lead`, collect.py prints one brief for collect-lead instead of three PS briefs (it writes `brief.LEAD.md`). The CDR launches the lead alone; the lead launches the PS and writes the register (depth 2, SOP §1.17).

After a failure, rerun with `--resume`. It refetches nothing, skips every batch whose extract is present and non-empty, and prints what it skipped. Launch only the briefs it names. Each writes `extract.k.json` and reads nothing else. If any batch extract is still missing or empty, `--resume` prints the pending batches and exits 2 without writing the register brief (aas-06).

## H2 · Fan in

Launch **WRITE** (sonnet) with `brief.WRITE.md`. It reads every `extract.*.json` and the locus (for the Command areas), and writes the register the locus names. One writer, so the table has one voice.

```
python _tools/loci/check.py <name> <register.md>
```

Every fetched URL must appear in the register (by URL or title); the dead ones are listed for the gaps section. Claim lines (bullets and table rows) with a URL missing from the manifest are errors (mar-04). Lines with no URL are listed as "unsourced lines", an advisory count. `check.py` also stamps one line in the locus frontmatter, `run: <date> · agents N · batches N · links N · dead N · ~tokens N`, adding a minimal frontmatter if the locus has none (mar-07). **Provenance columns (sas-11).** The register table carries three columns per link: `source url` · `fetched at` (the manifest date) · `quality` (high, medium or low, from the extract). `check.py` requires all three in the register header when the header names any of them. A MISSING line means one extract was skipped: rerun WRITE with the finding under its brief, not a new reviewer.

## H3 · The main line

Read the check output and the register's gaps section only. Record the run in the locus frontmatter (`status:`), the BOLO row, and the session note. The reply: counts (fetched · dead · items), the register path, the three most useful findings in Chief's terms.

Frames for the register and the briefs (source tiers, two-source rule, conclusion first, the one-paragraph brief): `references/research-frames.md`.

<sub>Provenance idea: sickn33/agentic-awesome-skills skills/wiki-builder (dair-ai/dair-academy-plugins), MIT. BOLO 140.</sub>
