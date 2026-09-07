---
title: LOCI — topic dossiers, navigable by neighborhood
type: convention
status: provisional — stood up 2026-09-06 on BOLO 39/41; the filing design is BOLO 41's ruling
trunk: BLACK
---

# LOCI

**What a locus is.** A one-file dossier on a *topic*, not a book. BVX-LEARN's atom (`KNOWLEDGE_AREAS/🧬 CODE.NN`) is one source distilled; a locus is one *question* answered from many sources, with its neighbors listed so the reader can step sideways. Papi's spec (9/6): *"if I'm thinking about what people eat in this area, I want to pull up everything in that locus — the edge cases, the Overton window of things related to what I'm asking — and navigate from there."*

**The file.** `<slug>.locus.md`, frontmatter:

```yaml
locus: "<place> × <meal or practice> × <era>"     # the fixed point
methods: [salt, ferment, ...]                     # from preservation.field-map.md, when food
neighbors: [<slug>, <slug>]                       # the Overton window — what borders it, in place and in method
feeds: [S3 SENSORIUM, S6 ECONOMY, S8 HABIT]       # setting-system layers (📐 ssot_03_setting_system.md)
sources: [BVX.NNNN, ...]                          # catalog ids once the books are in
tier: reference | monograph | ground              # the best tier the dossier reaches
```

**The collect method** (how a locus gets built — the Balkan breakfast is the proof case):

1. **Fix the locus.** Place × meal × era. A locus with no era drifts.
2. **Reference tier first.** The Oxford Companion to Food entries, the Cambridge World History of Food chapter. These set the vocabulary.
3. **Monograph tier.** The standard cookbook or food history of that place, in English, cited.
4. **Ground tier, flagged.** Menus, market lists, kitchen videos. Never load-bearing; useful for the tasting map.
5. **Rows, not prose.** Dish · method · what is preserved in it · when eaten · who eats it. Every method links back to the field map.
6. **Neighbors last.** What sits one step away in place (the border cuisines) and one step away in method (the same technique elsewhere). This is the navigation.

**Retrieval today:** grep the frontmatter (`locus:`, `methods:`, `neighbors:`). **Retrieval later:** the WARROOM pattern — a browser with the neighbors as links (BOLO 41).

**Files here**

- `preservation.field-map.md` — the spine: every preservation method as one tree, the cuisines that think that way, the syllabus.
- `preservation.tasting-map.md` — the original of each method and the close alternatives findable anywhere.
- `balkan-breakfast.locus.md` — the first locus, the proof of the collect method.
