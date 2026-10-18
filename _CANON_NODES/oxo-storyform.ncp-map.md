# OXO storyform: NCP export map

[oxo-storyform.ncp.json](oxo-storyform.ncp.json) is the OXO primary storyform written in Narrative Context Protocol form. [oxo-storyform.md](oxo-storyform.md) stays the source of truth; edit it, then regenerate the JSON, never the other way round. The JSON follows storyform section 9 (the engine form, the canon per section 2).

## Mapping: canon word to NCP word

| # | Canon word | NCP word | Where it appears in the JSON |
|---|---|---|---|
| 1 | Signposts | Transits | `x_canon_transits` (appreciation `transit`, sequence 1-4) |
| 2 | Change / Steadfast | Relinquished / Maintained | NCP prose only. The schema enum still says `change` / `steadfast`, so the JSON uses those |
| 3 | Throughline | Perspective | `subtext.perspectives` |
| 4 | MC / IC / RS / OS | I / You / We / They | `pov` and `author_structural_pov` |
| 5 | MC Resolve | I-perspective resolve | dynamic `i_perspective_resolve` |
| 6 | IC Resolve | You-perspective resolve | dynamic `you_perspective_resolve` |
| 7 | Problem-Solving Style (Linear) | Narrative Alignment | dynamic `alignment` |
| 8 | Limit (Optionlock) | Narrative Fabric (Options) | dynamic `fabric`, vector `options` |
| 9 | Symptom | Focus | appreciation `focus` |
| 10 | Response | Direction | appreciation `direction` |
| 11 | Situation (domain) | Universe | method `universe` |
| 12 | Activity (domain) | Physics | method `physics` |
| 13 | Manipulation (domain) | Psychology | method `psychology` |
| 14 | Fixed Attitude (domain) | Mind | method `mind` |
| 15 | Developing a Plan | Conceptualizing | method `conceptualizing` |
| 16 | Conceiving an Idea | Conceiving | method `conceiving` |
| 17 | Playing a Role | Being | method `being` |
| 18 | Changing One's Nature | Becoming | method `becoming` |
| 19 | Gathering Information | Learning | method `learning` |
| 20 | How Things are Changing | Progress | method `progress` |
| 21 | Memories | Memory | method `memory` |
| 22 | Impulsive Responses | Preconscious | method `preconscious` |
| 23 | Innermost Desires | Subconscious | method `subconscious` |
| 24 | Contemplation | Conscious | method `conscious` |
| 25 | Do-er | do_er | dynamic `approach` |
| 26 | Story Outcome / Judgment | Ending (outcome, judgment) | dynamics `outcome`, `judgment` |

Words that match one-to-one (Equity, Inequity, Projection, Speculation, Ability, Desire, Order, Chaos, Prediction, Suspicion, Evidence, Interdiction, Senses, Circumstances, Situation as an element, Interpretation, The Past, The Present, The Future, Understanding, Doing, Obtaining) are lowercased only. NCP's Serotonin-aligned renames (Goal to Intention and so on) are not used.

## Gaps: field, and why it is left out or marked

1. `story.genre` is `""`. The storyform names no genre and the schema requires the field.
2. `story.created_at` is the export date (2026-10-17), not a canon date.
3. `players[].visual`, `players[].audio`, `players[].storytelling`, every storypoint `illustration` and `storytelling`, and every dynamic `storytelling` are `""`. The storyform has no such text; the schema requires them.
4. `subtext.storybeats` is empty. The schema requires `tones`, `illustration`, `summary` and `storytelling` on every storybeat and the storyform supplies none, so the 16 Signposts sit in `x_canon_transits` (an extension key) instead.
5. Progressions (1-16) and events (1-64) are absent. The act-by-act variation quads live in `plot_sequence.TXT` and are not transcribed.
6. Plot appreciations (Goal The Past, Consequence Memories, Cost Developing a Plan, Dividend Understanding, Requirement The Present, Prerequisite Contemplation, Precondition Conceiving an Idea, Forewarnings Gathering Information) have no value in the schema enum. They sit in `x_canon_plot_appreciations`, unmapped.
7. `storytelling.overviews` and `storytelling.moments` are empty. The episode mapping waits on plot_systems (medium line, section header), and `audience_experiential_pov` is not set.
8. Issue counterparts (the second term of "X vs. Y") share one storypoint with the issue; NCP holds one method per storypoint, so the pair is written in `summary` only.
9. The Personal Triumph ending name has no vector in the schema enum. Failure and Good are set; the name is in the `judgment` summary.
10. Conflict inside the storyform: section 2 and section 9 give Anna (IC) Manipulation / Developing a Plan, while section 4 (ruled 2026-09-23) gives her Fixed Attitude / Memories and the RS column. The export follows section 9, which section 2 names as the storyform. Needs Chief's ruling.
11. The Factions are not a Player. The storyform defines no OS character, so only Tori and Anna appear in `players`.
12. L12 fields with no NCP slot are left out: methodology Certainty, evaluation Proven, purpose Knowledge, motivation_quad Consider, narrative_invariant, dramatica_archetype beyond the Tori player summary.
13. Section 3-6 cells tagged VERIFY, ENGINE or superseded (for example os_concern Becoming, mc_issue Interdiction for Tori) are not used; section 9 replaces them.
14. Schema defects, not storyform gaps: `ncp-schema.json` is not a valid draft-07 schema (`oneOf` sits as an array inside `properties`), so `jsonschema.validate` stops at `check_schema`. The JSON was checked with `Draft7Validator(schema).iter_errors(doc)` and has zero errors. The schema also requires a `pov` key on perspectives that it never declares; the JSON carries both `pov` and `author_structural_pov`.
