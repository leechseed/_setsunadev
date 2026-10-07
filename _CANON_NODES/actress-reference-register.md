---
entity: "The actress reference register"
entity_id: actress_reference_register
kind: register — reference data (looks · physique · screen personality), not canon prose
ip: cross-IP (casting reference for LEECHSEED characters; OVEREXITOUT, the ORANGE trunk)
trunk: BLACK / ORANGE
status: OPENED 2026-10-06 (BOLO 113) — the card format is provisional; no cards yet, waits on Chief's first five picks
links:
  - "[[performer-register]]"
  - "[[film-register]]"
captured: 2026-10-06
---

# THE ACTRESS REFERENCE REGISTER

**What it is.** One card per actress Chief picks, used as a casting reference for LEECHSEED characters. A card describes what she brings on screen: her look, her build, her screen personality. A character can point at one card or blend several. The cards describe public screen work only. They hold no private life detail, and they never claim the actress *is* the character.

**Where the scenes come from.** Chief pulls source clips under his own accounts (Mr. Skin, streaming), the same rule as the PDFs. Claude does not scrape paid sites. A card cites a scene by film, year and timestamp; the clip itself stays in Chief's library, not in this public repo.

**Sibling registers.** The [[performer-register]] holds adult performers (BOLO 42). This register holds mainstream actresses. One person never sits in both.

## The card (provisional)

```yaml
id: AR-001                    # next free id; grep the repo for the max before minting
name: ""                      # stage name as credited
picked: 2026-10-__            # the day Chief picked her
look:                         # face, hair, coloring, signature styling, in plain words
build:                        # height and frame as publicly listed, and how she carries it on screen
screen_personality:           # the energy she plays: e.g. dry wit, menace, warmth, chaos
range_roles:                  # 2-4 roles that show the personality, film (year)
scenes:                       # citations only: film (year) · timestamp · what the scene shows
  - ""
feeds:                        # LEECHSEED characters that point here, with what they borrow
  - character: ""
    borrows: look | build | personality
chief_says: ""                # Chief's words on why she's in, verbatim
```

## Cards

*None yet.* Chief names the first five; each becomes a card on the next pass.
