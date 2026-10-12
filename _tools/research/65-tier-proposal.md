# BOLO 65: tier proposal (one page, proposal only)

Status: 2026-10-12. Nothing in SOP.md, STATE.md or any skill was edited. This follows the first pass in [65-lineage.md](65-lineage.md).

## What the sources say
- **Air Force.** AFDP 1 (*The Air Force*) and AFDP 1-1 (*Mission Command*) are the capstone pair. The Chief of Staff signs both. Operational publications (AFDP 2-0, 3-0, 3-01) sit below. The LeMay Center signs those. Each AFDP pairs with a joint publication. AFDP 1 itself is paywalled to my fetch (HTTP 403), so this rests on the search summary of the Smart Book, not the full text. Source: [AF Doctrine Smart Book](https://www.doctrine.af.mil/Portals/61/documents/SmartBook/AFDoctrineSmartBook.pdf).
- **Space Force.** Four levels plus a glossary: capstone, keystone, operational, tactical. *Spacepower* (2020) is the capstone. Six keystone publications follow: SDP 1-0 Personnel, 2-0 Intelligence, 3-0 Operations, 4-0 Sustainment, 6-0 Mission Command, and one more (I could not confirm SDP 5-0). Operational publications hang under a keystone (SDP 3-101 and 3-102 under 3-0). Tactical level is a set of procedure suites. Sources: [SDP 2-0](https://csps.aerospace.org/sites/default/files/2023-11/SDP%202-0%20Intelligence%20%2819%20July%202023%29_0.pdf), [SDP 3-102](https://csps.aerospace.org/sites/default/files/2025-10/USSF%20SDP%203-102%20Operations%20in%20the%20Information%20Environment%20%2821%20Jul%202025%29_0.pdf), [SDP 6-0](https://csps.aerospace.org/sites/default/files/2025-10/USSF%20SDP%206-0%20Mission%20Command%20%28Nov%202024%29.pdf), [SDP 4-0](https://csps.aerospace.org/sites/default/files/2023-11/SDP%204-0%20Sustainment%20%28Signed%29.pdf).
- **One rule they share.** Doctrine is advice. A lower tier must not contradict the tier above it.

## The four labels, plainly
- **Capstone:** why the Command exists and what it values.
- **Keystone:** how one whole function runs.
- **Operational:** how one procedure runs, start to finish.
- **Tactical:** the single page used in the moment.

## Mapping onto the Command's real files
| Tier | File | Why |
|---|---|---|
| Capstone | [CLAUDE.md](../../CLAUDE.md), [DOCTRINE-0-INVARIANTS.md](../../DOCTRINE-0-INVARIANTS.md), MCDP-CODEX | Purpose, the four steps, the invariants (Touchstones). |
| Keystone | [SOP.md](../../SOP.md), the SSOT system docs (`ssot_NN_*`, one per system) | Each runs a whole function: comms, or one story system. |
| Operational | the seven skills: sitrep, oscar-mike, dope-sheet, frago, collect, rtb, launch | Each is one named procedure. |
| Operational | DOPE SHEET N (one per BOLO) | One mission's status and order. |
| Tactical | SOI card (SOP §0), the OUT block, hooks, call sheets, prowords | Short, used in the moment. |
| Not tiered | STATE.md, BOLO.md, QUOTES.md, _LOG, _CACHE | Records, not doctrine. |

## How to label
- Add one front-matter line to each doctrine file: `tier: capstone | keystone | operational | tactical`.
- Skills get `tier: operational` in their SKILL.md header.
- A DOPE SHEET names its parent: `under: SOP §2`.
- No renames. NASA names stay (CDR, MS, PS).

## Cost and risk
- About 20 one-line edits. Zero changes to wording.
- Risk: SOP.md is one file that holds keystone and tactical content (§0 card, §8 codebook). Label by section, or leave the file keystone.
- The SSOT docs are many files across ShroomsQ; label them in one scripted pass later.

## Rec
Yes, in two steps: label only the capstone and keystone files first (about five edits), and wait to see if it helps the sit rep.
