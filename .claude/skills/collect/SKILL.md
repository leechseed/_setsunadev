---
name: collect
description: Run a link-harvest research pass in the formation (BOLO 51 phase 2.7; the LOCI six-step collect and the standards register are its instances) — a script fetches every link to text, haiku specialists extract per batch, one sonnet specialist writes the register, a script proves every link is covered. Fires on "collect <locus>", "pull every link in …", "build the register from the harvest", "run the locus".
---

# Collect — the harvest formation

Use when a file holds a list of links (a locus, a harvest, a syllabus) and the job is to turn them into one register. Not for a single lookup.

## H0 · Fetch (zero tokens)

```
python _tools/loci/collect.py <locus.md> [--limit N] [--batch 12]
```

Every URL fetched over curl (the box's python cert store is stale) to `_tools/loci/work/<name>/<nnn>.txt` (tags stripped, capped 120 KB), plus `manifest.json` and the briefs. Dead links (403, 0) are reported, not retried by agents. If most links die behind a bot wall, stop and say so; do not send agents to fetch what the script could not.

## H1 · Fan out

Launch **EXTRACT-1 … EXTRACT-k** (haiku) in one message, each with its brief verbatim. The gear caps the count: at gear 1 launch three, then the next three when they return; never one agent per link. Each writes `extract.k.json` and reads nothing else.

## H2 · Fan in

Launch **WRITE** (sonnet) with `brief.WRITE.md`. It reads every `extract.*.json` and the locus (for the Command areas), and writes the register the locus names. One writer, so the table has one voice.

```
python _tools/loci/check.py <name> <register.md>
```

Every fetched URL must appear in the register (by URL or title); the dead ones are listed for the gaps section. A MISSING line means one extract was skipped: rerun WRITE with the finding under its brief, not a new reviewer.

## H3 · The main line

Read the check output and the register's gaps section only. Record the run in the locus frontmatter (`status:`), the BOLO row, and the session note. The reply: counts (fetched · dead · items), the register path, the three most useful findings in Papi's terms.
