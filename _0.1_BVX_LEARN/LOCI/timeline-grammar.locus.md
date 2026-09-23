---
locus: "editing software × the timeline as an interface × 1983–2025"
methods: [spine, container, nesting, compounding, automation, non-destructive-edit]
neighbors: [score-vs-patch, music-syllabus, watch-register]
feeds: [MUS.01, BOLO-36, the story-timeline tool]
sources: [ableton.com/en/manual, helpx.adobe.com/premiere, steakunderwater.com VFXPedia (Resolve 18.6 manual mirror), tourboxtech Pages overview]
tier: reference
---

# Timeline grammar — what a story timeline borrows from Ableton, Resolve and Premiere

**The question.** A story-timeline tool is a time series plus drag-and-drop blocks. Three editors already solved that interface. What is worth taking, and what is a trap?

| Thing | Ableton Live | DaVinci Resolve | Premiere Pro |
|---|---|---|---|
| Spine | two clocks — Arrangement in bars/beats, tempo-relative; Session has **no time axis at all** | one clock, timecode/frames — except Fairlight, which automates at sample resolution | one clock, timecode/frames, fixed per sequence |
| Containers | track · clip · scene slot | clip · **Compound Clip** (flattens, reversible) · **Nested Timeline** (embedded, updates everywhere) | clip · **Nested Sequence** (one mechanism for both jobs) |
| Two views | Session vs Arrangement; crossing is a **capture, not a toggle** | none | none |
| Continuous data | track Automation Lane (song position) + clip Envelope (travels with the clip unless *Lock Envelopes* pins it) | page-dependent resolution | keyframes on the sequence |

**The borrows, ranked.**

1. **Non-destructive shaping.** Warping never touches the source audio; warp markers are playback metadata. A story tool copies it exactly: scene text stays intact, and position, length and shaping live in a separate undoable layer. Strongest borrow because Resolve and Premiere already obey the principle by convention while Ableton names it and pushes it down to the clip.
2. **The clip-envelope split.** A per-scene curve either travels with the scene on reorder or stays pinned to a timeline position. That is the cleanest existing answer to a question a story tool must ask about every curve it carries.
3. **Resolve's compound-versus-nested split**, kept apart rather than merged as Premiere merges them — the moment the tool needs both "fold this act down for scale" and "this exact scene appears in two chapters", those are two operations, not one.
4. **Resolve's pages for scale-of-view** (a structure page, a tone page, a dialogue page over one timeline) and **Premiere's nesting for scale-of-content** (folding an act into a block).

**Do not borrow.** The Session/Arrangement split — a story has no "order not yet decided, launch live" state, and building one invents a mode nobody needs. Resolve's dual-resolution automation — a story has no equivalent to sub-frame audio precision, and faking one adds a fake-precision axis.

**Where the Command's own material lands.** Fabula, the raw chronological event set, is the fixed spine every one of these editors assumes. Sjuzhet, the arranged presentation, is what Ableton's two-view split gestures at without landing — a story tool's real second view is the discourse ordering laid over the fabula spine, not a live-launch mode. Genette's axes map onto operations already in these editors: **order** is drag-to-reorder on the fixed spine · **duration** is a compound block standing in for more or less fabula time than its width shows · **frequency** is the nested-clip reference turned around, one event told once and referenced from several places.

**Full read:** `_tools/bolostatus/work/35/HEAD-VERSION.md` §1 · extract `_tools/bolostatus/work/35/ui-read.md`
