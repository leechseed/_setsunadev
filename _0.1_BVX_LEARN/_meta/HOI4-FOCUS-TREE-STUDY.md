---
rung: handbook · NASA four, ruled 2026-09-24 (BOLO 79)
---

# HOI4 National Focus Tree Study → Rules for the Trope Graph Rails

Scope: Hearts of Iron IV's (Paradox, 2016) national focus tree — grid layout, prerequisite/mutually-exclusive logic, available/bypass states, search-filter-zoom navigation, and the "tree too big" problem at Kaiserreich/TNO scale — as a model for the trope-graph lens of the story workspace (BOLO 79): ~135 book-derived plot nodes walked in Dramatica's fixed order of 16 signposts × 4 throughlines ("the rails"), ~1,700 TV Tropes tropes keyed to them. EU4/Imperator missions and Stellaris's card-draw tech pull in only where they sharpen a point. Confidence HIGH/MEDIUM/LOW per claim. Study date 2026-09-24.

## Executive summary

1. A focus is one node: grid position (`x`,`y` or `relative_position_id`), cost in days, `prerequisite` (AND across blocks, OR within one), optional `mutually_exclusive`, an `available` gate, a `completion_reward` — the node contract to borrow [HIGH — wiki].
2. Visual grammar is fixed: grey/brown/golden brackets = available/unavailable/completed; green vs light-blue lines = satisfied vs unsatisfied prerequisite; solid vs dotted = AND vs OR [HIGH — wiki].
3. `bypass` completes a focus with no reward when its precondition is already true elsewhere — the escape hatch keeping a fixed slot from blocking everything behind it [HIGH — wiki].
4. One small **generic** tree (five branches: Army, Aviation, Navy, Industrial, Political) serves every nation without a unique tree; unique trees are reserved for flavor-heavy majors — one skeleton, flavor layered on top [HIGH — wiki].
5. Patch 1.9 added zoom-to-cursor, a search bar, and toggleable filters because locating or exploring a focus tree "had gotten harder as trees grew" [HIGH shipped features — wiki patch notes; MEDIUM motivating quote, via search excerpt not a fetched page].
6. `search_filters = { FOCUS_FILTER_MANPOWER FOCUS_FILTER_POLITICAL }` multi-tags a focus for that search bar [HIGH — wiki].
7. Modder-scale trees (Kaiserreich ≈200 national trees; TNO's dense bespoke per-nation trees) push density into collapsed sub-branches, historical-path toggles, and the same search/filter/zoom triad rather than widening the grid [MEDIUM — community pages, no primary dev quote on technique].
8. EU4/Imperator missions share the node shape but read as advisory (skip freely, replay differently); HOI4 focuses read as committed spend. Stellaris drops the tree for a randomized card draw. The rails' fixed order sits closer to HOI4's commitment model than either [MEDIUM — community synthesis].
9. Do not copy: free-form pixel authoring (the rails are a fixed 16×4 grid, not a canvas), the political-power clock (nodes are found, not purchased), one-tree-per-case sprawl.
10. The standing CK3 nested-tooltip rule sits unchanged on top: a focus's `completion_reward` tooltip becomes the node's trope list, capped and nested per CK3 R2–R4.

## 1. The node and the grid

**Position.** `x`/`y` place a focus (≈96px/unit x, 130px/unit y; larger x right, larger y down) [HIGH — wiki, National_focus_modding]. `relative_position_id = TAG_other_focus` positions relative to another focus, so redesigning a parent cascades to children [HIGH]. `offset = { x y trigger }` moves a focus conditionally at tree-build time [HIGH].

**Prerequisites.** `prerequisite = { focus = TAG }` requires a completed focus; multiple `prerequisite` *blocks* AND together, multiple `focus` entries *inside one block* OR [HIGH — wiki]. Position and prerequisite are independent — a node's grid address need not match its causal dependency; modders wire prerequisites across the tree, not just to visual neighbors.

**Mutually exclusive.** `mutually_exclusive = { focus = TAG }` blocks a focus once its pair completes [HIGH — wiki]. A distinct connector icon marks the pair, and taking one branch can cascade-lock everything downstream of the other unless a `bypass` routes around it [MEDIUM — paraphrase, not verbatim].

**Cost and reward.** `cost = 8` sets duration (7 "points" per unit, 1 point/day default; a 70-day focus spends 70 political power at -1/day) [HIGH]. `completion_reward = { … }` fires on completion, scoped to the completing country by default [HIGH].

**Bypass.** `bypass = { … }` completes a focus with no reward once its precondition is already true by another route; `bypass_effect = { … }` runs instead [HIGH — wiki]. This keeps a fixed-position, fixed-prerequisite node from becoming a dead wall when the state it represents is already satisfied.

## 2. Visual states and the connector grammar

- **Grey** = available now; **brown** = not yet; **golden** = completed; a shine marks in-progress [HIGH — wiki, National_focus].
- **Green line** = prerequisite satisfied; **light-blue** = not yet.
- **Solid** = AND (all required); **dotted** = OR (any one suffices) [HIGH].
- Tooltip order, fixed: flavor description → requirements → bypass conditions → completion effects [HIGH].

Four states, two line colors, two line styles — six primitives cover every node from an 8-focus minor to a 130-focus major; only the grid's extent changes with tree size, never the grammar.

## 3. Generic tree vs. unique trees — scale without sprawl

Every nation without a unique tree uses the generic tree, and a nation whose unique-tree DLC is off falls back to generic too [HIGH — wiki, Generic_national_focus_tree]. The generic tree is five shallow branches — Army, Aviation, Navy, Industrial, Political Effort — reused verbatim in structure across every minor [HIGH]. Majors (base game: seven great powers plus Poland, Finland) get hand-authored unique trees; Germany's runs seven main branches plus 25 sub-branches, well over 100 focuses once the Götterdämmerung alternate-ideology paths are counted [MEDIUM — wiki synthesis, not machine-counted]. The pattern: **one skeleton, many flavor fills**, not a new skeleton per case.

## 4. The "tree too big" problem and how the field handles it

Patch 1.9 "Husky" added zoom-to-cursor, a free-text search bar over category filters, and toggleable filters (spot industry- or spirit-related focuses at a glance) because finding or exploring a focus "had gotten harder as trees grew" [HIGH shipped features — wiki patch notes; MEDIUM motivating language, search excerpt only]. `search_filters` tags drive that bar; a focus can carry several [HIGH].

At modder scale it compounds: Kaiserreich ships on the order of 200 national trees [MEDIUM — community estimate]; TNO builds dense bespoke per-nation trees with custom sub-systems [MEDIUM — no primary size count obtained]. Neither is documented (in fetchable sources) as solving scale by widening the base grid; both lean on collapsed sub-branches, historical-path toggles, and the base game's search/filter/zoom triad. The forum threads that would state this as explicit doctrine returned a bot-check wall on fetch — the feature list is HIGH, the reasoning is MEDIUM.

## 5. Two contrasts that sharpen the point

**EU4/Imperator missions** share the node-prerequisite-reward shape but read as advisory: skip freely, and replaying the same nation plays out "wildly different" as the surrounding sandbox reorders what's worth taking [MEDIUM — community synthesis]. HOI4 focuses read as a political-power spend on a path chosen in advance — a budget allocation, not a suggestion list [MEDIUM].

**Stellaris technology** drops the tree shape: three techs drawn at random per category from a weighted pool, redrawn each completion, to "de-prioritize bee-lining" [MEDIUM — community-paraphrased]. Players requesting "a proper tech tree, just like HOI4" confirm the two read as opposite philosophies: fixed-and-legible vs. randomized-and-replayable [MEDIUM].

The rails' fixed Dramatica order — walked the same way every time — sits past HOI4 on the commitment axis: HOI4 still offers OR-logic and mutually-exclusive forks inside a flexible canvas; the rails offer neither at the signpost level. Borrow HOI4's node/state/tooltip contract (§1–§2); reject its free-canvas positioning (§6, H1).

## 6. Translation to the trope graph rails

**The grid (from §1).**
- H1. The 16 signposts (fixed order) are the x-axis; the 4 throughlines are fixed swim-lanes on the y-axis. Unlike HOI4's `x`/`y`, a node's column is *determined* by which signpost it embodies, never author-placed for balance. Reject free-canvas positioning; keep the grid.
- H2. Within one signpost-cell (throughline × signpost), several book-derived nodes can coexist — HOI4's `relative_position_id` case. Cluster, don't spread: a cell with three candidates shows three stacked brackets at one address, not three cells.
- H3. Prerequisite logic is not author-drawn the way HOI4's is. Signpost order itself is the AND chain: signpost N in throughline T requires signpost N-1 in the same throughline. Author-drawn prerequisite/OR logic applies only *within* a cell, between competing nodes for the same beat.
- H4. `mutually_exclusive` maps directly: two nodes at one cell that are alternate embodiments of the same beat (different source lineages, e.g. DCUS vs. legacy Inner Spiral vocabulary) are mutually exclusive by lineage, with the same cascading lock HOI4 uses — picking one lineage at cell N locks the other's downstream nodes in that throughline unless bypassed.

**States and tooltips (from §2, plus the standing CK3 rule).**
- H5. Replace HOI4's agency states with research states: **Verified** (source confirms — golden), **Candidate** (plausible, unconfirmed — grey), **Unverified** (rail-required, no instance found — brown), **Contradicted** (a later find rules it out, a fifth state HOI4 doesn't need — struck bracket).
- H6. Connector axes carry over: green = upstream node exists, light-blue = rail requires a predecessor with none yet; solid = the fixed AND chain, dotted = in-cell lineage OR (H4).
- H7. A node's tooltip becomes its trope list: tropes keyed to that node, capped at six with "× more," full list on click — CK3 R11's pattern exactly.
- H8. That capped list is the entry point to the CK3 nested-tooltip layer: each listed trope is a term, hover opens its definition, terms inside open a second tooltip, capped at CK3's depth-3 ceiling (R3–R4). HOI4 owns the outer node/reward-list shell; CK3 owns everything nested past it — one component, one owner, resolving the CK3 study's own open question.
- H9. A rail-required cell with no confirmed node yet renders bypassed-empty (faint placeholder, no tooltip), not a blocking brown wall — the fixed order must stay walkable end to end even where research hasn't filled every cell.

**Scale (from §3–§4).**
- H10. Default view = the generic-tree pattern: show only the ~135 nodes on the 16×4 grid; the ~1,700 tropes live entirely inside each node's capped tooltip (H7). Never draw a trope as its own grid node — 135 is the tree, 1,700 is flavor.
- H11. The ruled "explore" toggle is the free-network view, playing Stellaris's role in §5: same content, fixed order relaxed, opt-in not default. Toggle, don't overlay.
- H12. Ship search + filter + zoom from day one — HOI4 shipped without them and had to retrofit at 1.9. Filter tags mirror `search_filters`: throughline, signpost, lineage (DCUS/Inner Spiral/Red Hills), TV Tropes category, multi-tag per node.
- H13. Zoom is a legibility control, not a content control: zoomed out shows bracket color only across the 16×4 grid; zoomed in reveals labels and cell clusters (H2); tooltips fire only zoomed in, matching HOI4's cursor-follow zoom.

**Do not copy.**
- Free-form pixel authoring — grid address is derived from Dramatica structure, never hand-placed.
- The political-power spend/day clock — a node's state is a research fact, not a resource spent to unlock.
- One tree per case / sprawl — 135 nodes is the whole tree; new material adds tropes inside existing nodes (H10), never grows the grid.
- Randomized card-draw as the default view — reserve randomization, if wanted at all, for a future out-of-scope mode.

## Sources

- HOI4 wiki, National focus modding (x/y, relative_position_id, offset, prerequisite, mutually_exclusive, available, bypass, bypass_effect, cost, completion_reward, search_filters): https://hoi4.paradoxwikis.com/National_focus_modding
- HOI4 wiki, National focus (bracket/connector grammar, tooltip order, PP cost): https://hoi4.paradoxwikis.com/National_focus
- HOI4 wiki, Generic national focus tree: https://hoi4.paradoxwikis.com/Generic_national_focus_tree
- HOI4 wiki, German national focus tree: https://hoi4.paradoxwikis.com/German_national_focus_tree
- HOI4 wiki, Patch 1.9 (zoom/search/filters shipped): https://hoi4.paradoxwikis.com/Patch_1.9
- HOI4 wiki, Category:Focus filter icons: https://hoi4.paradoxwikis.com/Category:Focus_filter_icons
- Paradox Forum, HOI4 Dev Diary — 1.8 Patch & Focus Tree Navigation (blocked on fetch, see below): https://forum.paradoxplaza.com/forum/developer-diary/hoi4-dev-diary-1-8-patch-wut-focus-tree-navigation.1279837/
- Kaiserreich (mod) — Wikipedia: https://en.wikipedia.org/wiki/Kaiserreich_(mod)
- TNO: Last Days of Europe wiki, Category:National focus trees: https://the-new-order-last-days-of-europe.fandom.com/wiki/Category:National_focus_trees
- Paradox Forum, "Why do I think National Focus trees are overrated" (via search excerpt): https://forum.paradoxplaza.com/forum/threads/why-do-i-think-national-focus-trees-are-overrated.1467006/
- PCGamesN, Stellaris tech tree explainer: https://www.pcgamesn.com/stellaris/tech-tree
- Stellaris wiki, Technology: https://stellaris.paradoxwikis.com/Technology

## Blocked / Unverified

- forum.paradoxplaza.com (every Paradox forum URL surfaced): "Validating browser" on direct fetch. Patch 1.9's wiki page confirms *what* shipped; the *why* is search-excerpt only — MEDIUM throughout §4 and the summary.
- Exact node counts (German tree, Kaiserreich roster, any TNO tree): no machine-countable source found; all counts are MEDIUM synthesis from wiki prose.
- Category:Focus filter icons: page confirmed as the `search_filters` tag catalog; the full tag list did not resolve via fetch (JS-rendered listing).
- No primary Paradox document states the EU4-vs-HOI4 "advisory vs. committed" framing directly; §5 is this study's synthesis of forum/community discussion.
- Stellaris's "de-prioritize bee-lining" rationale is community-paraphrased, not a verbatim developer quote from a fetched source.

## Open questions for Chief

1. **H4/H5 collision** — lineage exclusivity (H4) and research-state (H5) both want the bracket's color when a node is e.g. "DCUS-lineage" *and* "Unverified." Rec: research-state owns bracket fill (it changes with evidence); lineage shows as a corner glyph, matching CK3 R7's badge-beneath-title pattern.
2. **H9 placeholder density** — most of the 64 cells may start as bypassed-empty before research fills them, reading as mostly blank on day one. Rec: seed placeholders only where a candidate node already exists in current OXO/EVIL CHECK material; leave unattested cells off the grid until a first candidate lands.
3. **H11 explore-toggle scope** — does explore relax signpost order, lineage exclusivity (H4), or both? Rec: both — explore is the fabula's real cause-link graph (BOLO 79's free network), a strict superset of the rails view, never a different dataset.
4. **H12 filter taxonomy** — four simultaneous filter axes may overload a filter bar at 1,700-trope scale. Rec: ship throughline + signpost by default (they're also the grid axes — filtering by them is "jump to cell"); hold lineage and trope-category behind an advanced-filters disclosure, per CK3's own progressive-disclosure rule.
5. **H8 tooltip ownership** — HOI4-owns-outer / CK3-owns-nested is this study's call, not a ruling. Formalize as a BOLO decision now, or leave informal until the two studies collide in a build?
