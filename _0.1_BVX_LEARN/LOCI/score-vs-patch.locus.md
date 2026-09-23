---
locus: "electronic music × score versus patch × 1964–2025"
methods: [quantise, signal-flow, modulation, discrete-event, continuous-control]
neighbors: [timeline-grammar, music-syllabus]
feeds: [MUS.01, MUS.02, BOLO-36, the story-timeline tool]
sources: [Moog 1964 lineage, MIDI.org, arXiv 2010.01570, arXiv 2406.15249, Perfect Circuit (East/West Coast), Green 2002]
tier: reference
---

# Score versus patch — the two paradigms, and which layer a story tool sits on

**The question.** Chief's theory: a story-timeline tool should take its theory from electronic sound synthesis — composition as signal flow — set against conventional music theory, the score. Does that hold?

**It holds, with one correction.**

- **The score** quantises: twelve pitch steps per octave, rational fractions of a beat. Continuous phenomena get rounded onto a discrete grid before they can be written at all. Timbre barely gets notated. What that buys is transmissibility, analysis and reuse — discrete symbols compose. What it costs is exactly what was rounded away: a score is an instruction set for producing sound, not a record of it.
- **The patch** encodes signal flow — oscillators, filters, envelopes, amplifiers joined by cords, with control voltage and audio interchangeable, so modulation is not an add-on. It encodes process over time as a continuous function: a sweep, a decay, two oscillators drifting. None of that is a start-pitch-duration triple.

**The correction, and it matters.** MIDI (1983) does **not** bridge the two. It imports note-on/note-off discreteness into the electronic world, making synthesizers addressable the way a score addresses a player. Pitch-bend and CC simulate smoothness at high sample resolution; they are not a genuine continuous channel. **MIDI sits inside the score paradigm.** If a theory rests on MIDI as the bridge, the record says otherwise.

**Where the line breaks.** The axes are discrete/continuous · event/process · what-to-play/how-it-sounds · fixed/performed. Buchla's West Coast modulars rejected the keyboard, used voltage-controlled sequencers, and were built so a patch "for the most part played itself" — a patch behaving like a score. The dichotomy is a spectrum of design intent, not a wall; what differs is which unit a system treats as its default.

**Two learning pipelines.** Green (Ashgate 2002) found informal learners "acquire some or all of their skills and knowledge informally, outside school or university, and with little help from trained instrumental teachers" — choosing music they already know, learning by ear, against formal education's unfamiliar-repertoire-from-notation model. Conservatory produces reproducible performance of a fixed structure, the score's virtues. Producer training produces by-ear fluency and tolerance for iteration, the patch's virtues.

**The transfer — this dossier's own extension, not a sourced claim.** A score-shaped story tool is strong at beats and acts: discrete named units that reorder, diff and analyse. It is weak at anything that is a function rather than an event — dread rising across forty pages. A patch-shaped tool is strong at tension and character state as continuous modulatable signals, weak at producing a fixed shareable diffable object.

**Verdict.** Two layers. Beats and structure on the score layer — discrete, named, diffable, the thing handed to a collaborator. Tension, character state and thematic pressure on a patch layer underneath — continuous values that scenes modulate rather than set. MIDI's real lesson applies here: build the continuous layer for real, then expose a discretised addressable interface over it for whatever must read as an event.

**Full read:** `_tools/bolostatus/work/35/HEAD-VERSION.md` §2 · extract `_tools/bolostatus/work/35/paradigms.md`
