---
title: "Setting state architecture: tutorial"
type: tutorial
for: "A new writer who wants to learn place state by building the DCUS rename lattice."
does: "Walks through writing the Red Hills rename checkpoint, then querying and scrubbing it."
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/🔮 ssot_03_setting_state_architecture.md
source_version: 1.3.0
---

**Who it's for:** a new writer learning place state · **What it does:** one worked checkpoint, then a query · **Type:** tutorial

# Setting state architecture: tutorial

You will write Checkpoint 2 of the Delta Coast Ultra School (DCUS) rename lattice, the first erasure. Keep the [reference](2-reference.md) open.

1. **Know the base.** The DCUS base slice is written at the current era: the Administration, the Bishops and the Feed. Its header says live name "Delta Coast Ultra School (DCUS)".
2. **Name the moment.** The founding name Skeeter Creek is sanded to Red Hills. Write `state_id: dcus_red_hills_rename` and `place_id: dcus`.
3. **Write the origin event.** No fabula record exists. Write `backstory_red_hills_rename ⏸ DCUS rename lattice fill pass (phase 2)`. Never leave it blank.
4. **Set the story fields.** `told_at: []`, because the state is true but offstage. `movement: "backstory"`. Add `state_version: "1.0"` and `base_slice_version: "1.4.1"`.
5. **Write the layer diff.** This checkpoint is earlier than the base, so it diffs backward. Add S5 entry `skeeter_creek_sanded_to_red_hills`. Set S6 to the grandfather-versus-son ownership war, pre-Bishop. Set S8 to the forming alumni-legacy bloc.
6. **Park what the source parks.** S9 and S10 values carry the `⏸` phase 2 mark. Copy that mark, not an invented value.
7. **Write the header diff.** Set `live_name: "Red Hills Academy"`, `aliases_active: ["Red Hills Academy", "The Academy"]` and `aliases_legacy: ["Skeeter Creek"]`.
8. **Handle flags.** Set `MODIFIED_FLAGS: {}` after you re-evaluate each flag trigger.
9. **Add the note.** Write 2 to 5 sentences. The founding name is sanded a century before the Bishops arrive, and the live name flips.
10. **Query it.** Load the base, load this checkpoint, apply the diffs, and read the header. The live name is "Red Hills Academy".
11. **Scrub it.** Move the timeline back past this checkpoint's moment. Check that the live name returns "Skeeter Creek" from Checkpoint 1, not "DCUS" from the base.

You have now used every block of a state record. Try the [how-to](3-how-to.md) task "Write a checkpoint" for Checkpoint 3, whose layer diff is empty.

> **OPEN:** the `origin_event` ids stay parked until the fabula registry enters them.
