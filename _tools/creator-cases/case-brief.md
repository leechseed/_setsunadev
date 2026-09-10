# CREATOR CASE — shared agent instructions (BOLO 45 wave one, 2026-09-10)

You are researching and writing ONE business-side creator case study for a public GitHub repo. Working directory: `C:\Users\U01_LEECHSEED\Desktop\_setsunadev` (Windows; the Bash tool is Git Bash). Today is 2026-09-10. Your prompt names the SUBJECT, the output SLUG, and the register row with Papi's own note from 2023 or 2025.

## What the file is
A study of how one creator started, how they run their content, and how they get paid. Public-record sources only. Business side only. It sits beside the performer register as public canon under trunk ORANGE.

## Format — copy the template exactly
Read `_CANON_NODES/creator-case-variety-itsol.md` FIRST (the template) and `_CANON_NODES/creator-case-natasha-teen.md` SECOND (the newest file, which already carries the tenth section). Reproduce the structure:

- YAML frontmatter: `entity`, `entity_id`, `kind`, `ip`, `trunk: ORANGE`, `status: DELIVERED 2026-09-10 — BOLO 45 wave one (lane C), researched on Papi's order; every claim sourced; confidence labeled`, `register_row` (quote the row facts from your prompt), `pronouns`, `links` (`[[performer-register]]` plus any sibling case you cite), `captured: 2026-09-10`, `updated: 2026-09-10`.
- `# CREATOR CASE — <NAME>`
- `**Bottom line.**` one paragraph · `**Papi's context.**` one paragraph built from the register row and his note, verbatim where he wrote one · `**Confidence.**` one paragraph.
- `## 1 · Identity + verified handles` (table: Platform | Handle / URL | How verified; a "Collisions excluded" line)
- `## 2 · Timeline` (dated bullets; a growth series table from Wayback snapshots if any exist)
- `## 3 · How they run it` (model · platform mix by era · formats, named at category level only · collab vs solo · cadence · positioning in their own words · production setup)
- `## 4 · Monetization` (table: Platform | Price | Gated | Source; an earnings-on-record line; contest or award line)
- `## 5 · Growth tactics (observed)`
- `## 6 · Quotes (verbatim, with URLs and dates)`
- `## 7 · Interviews / studies found` (numbered with URLs; then a "None found:" line listing what you checked)
- `## 8 · Not known / conflicting`
- `## 9 · Sources` (every URL used)
- `## 10 · GOUGE` — **the header is provisional; Papi is ruling the name tonight; write it exactly as `## 10 · GOUGE` and do not invent another.** Four labeled parts, in this order:
  - **The one mechanic.** The single business thing this creator does that is worth studying. One paragraph.
  - **Transferable tips.** Three to five imperative bullets for a small operator starting a studio or creator venture from zero, on a zero budget. Concrete, not generic.
  - **Does not transfer.** What in this path does not carry to a zero-budget operator running a disclosed rendered persona, and why. One paragraph.
  - **Feeds.** Which of these it informs, one line each where relevant: the studio launch (BOLO 24) · the curation funnel (BOLO 27, ULTRA DARK) · the masked-performer Lab venture · the manager/agency path.

## Rules (hard)
- Public-record sources only. Never describe the sexual content of any media; name categories or titles only where a business fact needs them (a price list, a catalog count).
- No private information beyond the public professional identity: no legal names unless the creator uses one publicly, no addresses, nothing about family unless they have said it in press.
- Pronouns: use what the creator's own bios state. If unstated, use the register's Sex column (M = he/him, F = she/her, F+M = they as a pair). If the column is a dash, use they/them. Never infer from a name.
- Every claim carries a source URL. Label confidence HIGH / MEDIUM / LOW. Mark EST on any rate you derive. Mark "aggregator" or "bio farm" on figures from those sources and weight them LOW.
- **The thin-record rule.** Several of these names are tube channels from 2023 with no press and possibly no live presence. If the record is thin, the file is thin and says so in §8 and the bottom line. Kirenes is the precedent: an honest short file beats an invented long one. Do not spend more than about 25 tool calls chasing a dead handle; write what exists and stop.
- Name collisions are the norm. State what you excluded and why.
- **Do NOT edit `_CANON_NODES/performer-register.md`.** Eleven agents run at once and the file would be clobbered. Instead, end your report with a line beginning `REGISTER NOTE:` giving the exact text to append to the row's note column (one line, under 60 words, ending with the link `[creator-case-<slug>](creator-case-<slug>.md)`), and a line beginning `X HANDLE:` with the verified handle or `—`. The parent session applies them.

## Tooling notes (learned on this box)
- WebSearch works. WebFetch is BLOCKED on x.com, pornhub.com, onlyfans.com, reddit.com, web.archive.org and clips4sale.com.
- Workarounds that WORK: `https://api.fxtwitter.com/<handle>` (X profile JSON: bio, followers, join date, verified); `https://apiv3.fansly.com/api/v1/account?usernames=<handle>` (Fansly public API; prices are thousandths of a dollar, 11990 = $11.99); plain `curl -s` for Wayback — `https://web.archive.org/cdx/search/cdx?url=pornhub.com/model/<slug>&output=json` (also `/pornstar/<slug>`, `/channels/<slug>`, `/users/<slug>`) then `https://web.archive.org/web/<stamp>id_/<url>`; raw snapshots may be gzip, pipe through `gzip -dc`; `curl` also reaches clips4sale.com and manyvids.com. StashDB, ThePornDB, IAFD, Freeones and Boobpedia help with career dates and studio credits. unlockd.me, linktr.ee, allmylinks and beacons pages fetch normally.
- Long heredocs die in Git Bash here. Write any multi-line script to the scratchpad directory `C:\Users\U01_LE~1\AppData\Local\Temp\claude\c--Users-U01-LEECHSEED-Desktop--setsunadev\3a7d1b5a-70a8-414f-b14d-2a2df63ef37f\scratchpad` and run it. Do not write scrape dumps into the repo root; keep them in the scratchpad.
- Write the final markdown with the Write tool to `_CANON_NODES/creator-case-<slug>.md`.

## Report back (under 250 words)
The bottom line in two sentences · the one mechanic · confidence picture · what could not be fetched · then the `REGISTER NOTE:` line and the `X HANDLE:` line.
