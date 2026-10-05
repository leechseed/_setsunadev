---
title: "The fabula: tutorial"
type: tutorial
for: "A new writer who wants to learn the event record by writing one from the Tori instance."
does: "Walks through writing the crash event, then linking it to its edge and its state record."
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md
source_version: 0.3.0
---

**Who it's for:** a new writer learning the event record · **What it does:** one worked event, start to finish · **Type:** tutorial

# The fabula: tutorial

You will write the first Tori event, the crash. Keep the [reference](2-reference.md) open.

1. **State the fact.** Tori overrides the pace notes, calculating she knows better. Jebb dies. That is one transition. Do not add the grief, which is a second event.
2. **Write the id.** Use `<movement>_<slug>`. The crash is pre-story, in M1B. Write `m1b_crash_jebb_death`.
3. **Write the transition.** Write `Tori overrides the pace notes, calculating she knows better -> Jebb dies`.
4. **List the actors.** Victoria Midnight (Tori) is the subject. Jebb Midnight is the object.
5. **Flag it.** This is a kernel. It branches her WOUND, the family collapse and every state downstream.
6. **Date it.** `movement: "M1B"`. The canon gives no birth date and no calendar date, so write `reach: "pre-story; distance from story-present unspecified in canon"`. Write `extent: "point (a single crash)"`. Leave `time_code` and `calendar_year` null, because canon gives neither.
7. **Set the rest.** `gap_type: logged`, `repeat: false`, `stories: [OXO]`.
8. **Cite it.** The source is victoria-midnight.md, REORIENT. The confidence is `direct_quote`.
9. **Add the edge.** The crash causes the resolve "I will become untouchable". Write `type: cause`, `to: m1b_untouchable_resolve`.
10. **Test the edge.** Ask: would the resolve have formed without the crash? No. So `cause` is right. Compare `m2_recruited`, which has no stated causal link to M1B and keeps an empty edge list.
11. **Link a state record.** Write `origin_event: "m1b_crash_jebb_death"` on the state record `vm_m1b_post_crash`.
12. **Check your work.** Your record holds one transition, no invented year and one typed edge.

Next, try the [how-to](3-how-to.md) task "Add an event record" with the five Colson backstory events, using `backstory` as the movement.

> **OPEN:** the canon gives no location for the crash, so `location` reads "unspecified in canon".
