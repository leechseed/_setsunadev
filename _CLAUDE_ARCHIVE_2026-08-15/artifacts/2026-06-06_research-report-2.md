---
title: "Research Report"
source_conversation: "Advanced literature review of Mating in Captivity"
created: 2026-06-06
trunk: BLACK
kind: artifact
---

# The Canonical Review: A Design Theory for Self-Sufficient Reference Documents

## TL;DR
- A "Canonical Review" — a textbook-grade distillation of one source designed so a reader never needs the original — should be built by inverting current best practice into a concrete policy: **backward-design the enduring understandings, sequence by the modular logic of the source, separate the four Diátaxis modes (reference vs. explanation vs. how-to vs. tutorial), manage cognitive load à la Sweller/Mayer, and embed retrieval directly into the prose** (the Matuschak–Nielsen "mnemonic medium").
- The strongest, most decision-relevant evidence is unambiguous: **retrieval practice and spaced/distributed practice are the two highest-utility learning techniques** (Dunlosky et al., 2013); **active-learning designs raise exam/concept-inventory scores by 0.47 SD and cut average failure rates from 33.8% to 21.8%** (Freeman et al., 2014, PNAS); and **passive rereading/highlighting plus "learning styles" matching are low-value or debunked** (Pashler et al., 2008). A Canonical Review must therefore be an *active* artifact, not a passive summary.
- For the dual stakeholder (≈80% human / 20% AI), the two audiences' needs **mostly align**: explicit hierarchical headings, atomic self-contained sections, one-term-per-concept naming, a glossary, and YAML/`llms.txt`-style metadata help both human comprehension and AI retrieval. They **diverge** on engagement devices (narrative hooks, interactive widgets help humans, add little for AI) and on redundancy (humans benefit from worked recaps; AI chunking prefers non-duplicated, self-describing units).

## Key Findings

1. **There is a settled "standard now," and it converges on a few robust models.** The six evidence-based strategies (retrieval, spacing, interleaving, elaboration, concrete examples, dual coding), Cognitive Load Theory, Mayer's multimedia principles, Bloom's revised taxonomy, Backward Design/Understanding by Design, constructive alignment, and Merrill's/Gagné's instructional sequences all point to the same prescription: prioritize a few enduring ideas, align everything to them, reduce extraneous load, and force active processing.
2. **The standard is also heavily criticized**, and the criticisms are precisely the failure modes a Canonical Review must avoid: "mile-wide, inch-deep" coverage, textbook bloat and "seductive details," the ineffectiveness of passive reading, "inert knowledge," fragmentation, and the persistent learning-styles myth.
3. **The forefront is "active media."** Freeman's meta-analysis, Wieman's Science Education Initiative, the Deans for Impact "Science of Learning," the mnemonic medium (Quantum Country / Orbit), Bret Victor's explorable explanations, and 2025–26 AI tutoring/RAG knowledge artifacts all push reference material from "text to be consumed" toward "an environment to think in" (Victor) and a medium with an explicit theory of learning (Matuschak).
4. **A repeatable methodology exists** to convert a book into a Canonical Review: extract the enduring understandings, build a concept map, sequence by dependency, write atomic modular sections in the Diátaxis "reference + explanation" register, add the pedagogical apparatus (objectives, advance organizers, worked examples, embedded retrieval prompts, glossary), and compress without losing fidelity.

## Details

### PART 1 — THE STANDARD NOW

#### 1.1 The six evidence-based learning strategies (Dunlosky et al., 2013; Weinstein, Sumeracki & Caviglioli, 2018/2019)
The canonical synthesis comes from two sources. Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), *Improving Students' Learning With Effective Learning Techniques* (Psychological Science in the Public Interest), reviewed 10 techniques and rated only **two as high-utility — practice testing and distributed practice** — while rating the most popular student techniques (highlighting, rereading, summarization) as low-utility. Weinstein, Sumeracki & Madan (2018), *Teaching the science of learning* (Cognitive Research: Principles and Implications), and the Learning Scientists' book *Understanding How We Learn* (2018/2019) reframed the evidence into six teachable strategies:

- **Retrieval practice** (a.k.a. practice testing): recalling information from memory strengthens it more than restudying. *Applied:* every Canonical Review section ends with free-recall questions before the reader looks back.
- **Spaced practice** (distributed practice): spreading study over time beats massing. *Applied:* the review's review prompts are scheduled to recur, not bunched.
- **Interleaving**: mixing related topics/problem types improves discrimination and transfer. *Applied:* end-of-chapter problem sets mix concepts rather than blocking them.
- **Elaboration** (elaborative interrogation/self-explanation): asking and answering "how/why" and connecting to prior knowledge. *Applied:* margin prompts "Why does this follow?"
- **Concrete examples**: pairing abstractions with specific cases. *Applied:* every principle gets ≥1 worked example.
- **Dual coding**: combining words with visuals. *Applied:* each model gets a diagram/table.

#### 1.2 Cognitive Load Theory (Sweller, 1988) & Mayer's Cognitive Theory of Multimedia Learning
CLT (Sweller) holds that working memory is severely limited and learning = schema construction in long-term memory. Three loads: **intrinsic** (inherent complexity, a function of element interactivity and the learner's prior knowledge), **extraneous** (imposed by poor presentation — to be minimized), and **germane** (effort devoted to schema building — to be fostered). Note the theoretical caveat: recent formulations question the strict additivity of the three loads and some theorists revert to a two-part (intrinsic + extraneous) model. *Applied:* a Canonical Review minimizes extraneous load (no seductive details, clean signaling) and manages intrinsic load via sequencing and pre-training.

Mayer's Cognitive Theory of Multimedia Learning rests on three assumptions (dual channels, limited capacity, active processing) and yields **~12 principles**: coherence, signaling, redundancy, spatial contiguity, temporal contiguity, segmenting, pre-training, modality, multimedia, personalization, voice, and image. The most load-bearing for a text artifact: **coherence** (cut extraneous material), **signaling** (cue structure with headings/highlights), **spatial contiguity** (place words near corresponding graphics), **segmenting** (user-paced chunks), and **pre-training** (teach key terms first). *Applied:* glossary-first pre-training; figures captioned in place; ruthless coherence-driven cuts.

#### 1.3 Bloom's revised taxonomy (Anderson & Krathwohl, 2001)
The revision turned nouns to verbs and added a second dimension. **Cognitive process dimension:** Remember, Understand, Apply, Analyze, Evaluate, Create. **Knowledge dimension:** Factual, Conceptual, Procedural, Metacognitive. Any objective sits at the intersection of a process and a knowledge type. *Applied:* a Canonical Review tags each objective (e.g., "Apply × Conceptual") and ensures its self-check questions span lower- and higher-order processes, not just "Remember."

#### 1.4 Backward Design / Understanding by Design (Wiggins & McTighe, 1998/2005) & Constructive Alignment (Biggs)
UbD's **three stages**: (1) Identify desired results; (2) Determine acceptable evidence; (3) Plan learning experiences. Its prioritization filter sorts content into three nested rings: **"enduring understandings"** (big ideas worth retaining), **"important to know and do,"** and **"worth being familiar with."** Constructive alignment (Biggs) demands that objectives, activities, and assessment all point at the same intended outcomes. *Applied:* this is the master move for a Canonical Review — decide the enduring understandings first, then make sure every section and self-check is aligned to them; relegate trivia to "familiar with" callouts or an appendix.

#### 1.5 Merrill's First Principles of Instruction (2002) & Gagné's Nine Events
Merrill distilled instructional theories into five problem-centered principles: **problem-centered, activation** (of prior knowledge), **demonstration, application, integration.** Gagné's Nine Events: gain attention; inform objectives; stimulate recall of prior learning; present content; provide guidance; elicit performance; provide feedback; assess performance; enhance retention and transfer. *Applied:* the Canonical Review's section template mirrors this: hook/why-it-matters → objective → links to prior concept → explanation → worked example → retrieval prompt → feedback/answer → transfer task.

#### 1.6 "Considerate text" apparatus
Well-designed reference text uses: **advance organizers** (Ausubel, 1960/1968 — introductory material pitched at a higher level of abstraction that bridges prior knowledge to new content; distinct from mere overviews), stated learning objectives, signaling/headings, summaries, worked examples, glossaries, indexes, marginalia, self-check questions, and chunking. *Applied:* every chapter opens with an advance organizer and objectives, and closes with a summary and self-check.

#### 1.7 Knowledge-organization & technical-documentation frameworks
- **Diátaxis** (Daniele Procida): four documentation modes serving four needs — **tutorials** (learning-oriented, practical), **how-to guides** (task-oriented), **reference** (information-oriented, neutral facts), and **explanation** (understanding-oriented). The core thesis: these must be **kept separate** because mixing them degrades all of them. Reference and explanation are the "theory" half; a Canonical Review is principally **reference + explanation**, with how-to and tutorial elements quarantined into clearly-labeled sections.
- **Topic-based authoring / DITA / single-sourcing**: structured, modular content where each topic is self-contained and reusable; DITA adds typed topics (concept/task/reference). Information Mapping's principles — **chunking, relevance (one purpose per unit), labeling** — directly inform modular section design.
- **Networked knowledge (Zettelkasten / atomic / evergreen notes)**: Matuschak's **principle of atomicity** ("notes should be about one thing, but capture the entirety of that thing"), evergreen note titles that work "like APIs," and knowledge graphs of linked concepts. *Applied:* each Canonical Review module is an atomic, linkable unit with a precise declarative title.

### PART 2 — THE CRITICISMS

- **"Mile-wide, inch-deep."** Coined in the TIMSS analysis (William Schmidt described the U.S. curriculum this way) and applied to textbooks: AAAS Project 2061 reviewed the 10 most popular biology textbooks and found them loaded with facts to memorize but offering little explanation. As Project 2061 director George D. Nelson put it when releasing the review (Education Week, July 2000): "The important ideas are often camouflaged behind vast amounts of vocabulary and details… Not much learning of biology is going to take place while using these books." Lesson: prioritize depth on enduring ideas.
- **Textbook bloat & "seductive details."** Interesting-but-irrelevant material (the "seductive details effect," Garner et al.; Harp & Mayer) measurably harms recall and comprehension; the effect is small-to-moderate across ~35 years of studies. Lesson: coherence over color.
- **Passive reading, highlighting, rereading are low-utility** (Dunlosky 2013). Lesson: a summary that is merely read will not transfer; force retrieval.
- **"Inert knowledge"** (Whitehead) and **coverage-over-mastery**: knowledge that can be recited but not applied. Lesson: include application/transfer tasks, not just facts.
- **Fragmentation**: atomization without cohesion. Even Matuschak warns that over-fragmenting notes creates a "cohesion problem." Lesson: atomic but linked, with overview/map notes.
- **Debunked ideas to avoid**: the **learning-styles "meshing hypothesis"** has no supporting evidence (Pashler et al., 2008; Coffield et al., 2004; designated a "neuromyth"), yet the belief persists overwhelmingly — Newton & Salvi's 2020 systematic review (Frontiers in Education) found that "89.1% of 15,045 educators" across 18 countries self-reported believing that individuals learn better in their preferred style, and Dekker et al. (2012) found 93% of UK schoolteachers endorsed it. Lesson: do not build multiple "style-matched" versions; instead manage cognitive load and use dual coding for everyone.

### PART 3 — THE BLEEDING EDGE

- **Active-learning evidence base.** Freeman et al. (2014, PNAS), meta-analyzing 225 studies, found active learning raised exam/concept-inventory performance by **0.47 SD** and that the **odds ratio for failing under traditional lecturing was 1.95** — in their words, "Average failure rates were 21.8% under active learning but 33.8% under traditional lecturing." **Carl Wieman's** Science Education Initiative across 13 departments at UBC and CU-Boulder turned this into institutional practice (clickers, worksheets, peer discussion); a UBC physics study found active-learning students scored almost twice as well as a traditional-lecture section on the same material. **Deans for Impact's "Science of Learning"** translates cognitive science into teacher-facing principles.
- **The mnemonic medium** (Andy Matuschak & Michael Nielsen). *Quantum Country* (2019) embeds spaced-repetition prompts directly into narrative prose, so "memory becomes a choice"; **Orbit** generalizes it to any web text. Matuschak's *How to write good prompts* gives the craft of authoring retrieval questions. This is the single most direct precedent for a retrieval-embedded reference. Matuschak's *Why books don't work* (2019) supplies the rationale: books rest on the implied assumption that "people absorb knowledge by reading sentences," which he calls "transmissionism" and argues is "plainly false"; the readers for whom books *do* work are those who deploy effortful **metacognition** that "is unavailable to many readers and taxing for the rest."
- **Explorable explanations / reactive documents** (Bret Victor, 2011). "A reactive document allows the reader to play with the author's assumptions and analyses, and see the consequences." Goal: change "people's relationship with text. People currently think of text as information to be consumed. I want text to be used as an environment to think in."
- **Adaptive/personalized learning, AI tutoring, generative materials.** 2025–26 work points to AI tutors built on **retrieval-augmented generation (RAG)** over structured knowledge (including knowledge graphs auto-built from textbook PDFs) to reduce hallucination, plus competency/mastery-based progression. Brookings (2025) summarizes empirical gains but flags risks (accuracy, "metacognitive laziness," dependence).
- **Emerging directions:** documents authored to be consumed by AI agents/"skills" — the **llms.txt** convention (below), `skill.md` specs, and "Every page is Page One" self-contained chunking.

### PART 4 — APPLIED METHODOLOGY: Turning a Book into a Canonical Review

Running example: *Thinking, Fast and Slow* (Kahneman) — dense nonfiction with many concepts (and, notably, one of the very books Matuschak cites as failing the "absorb-by-reading" assumption).

**Step 1 — Identify enduring understandings (UbD Stage 1).** Strip to the big ideas (System 1 vs System 2; heuristics & biases; prospect theory; the two selves). Sort all other content into "important to know" (specific biases) and "worth familiar" (anecdotes). This is the antidote to mile-wide-inch-deep.

**Step 2 — Determine acceptable evidence (UbD Stage 2).** Decide what a reader must be able to *do* (e.g., identify which system a scenario engages; predict a framing effect). Write these as Bloom-tagged objectives.

**Step 3 — Build a concept map / dependency graph.** Identify prerequisite relationships; this fixes the **sequence** (pre-training before dependent ideas) and exposes which concepts are atomic modules.

**Step 4 — Write atomic, modular sections (Diátaxis reference+explanation; atomicity principle).** One concept per section, self-contained, with a precise declarative title ("API-like"). Each follows a fixed template (Gagné/Merrill): *advance organizer → objective → prior-knowledge link → definition (glossary term) → explanation → ≥1 concrete worked example → dual-coded diagram → retrieval prompt(s) → answer/feedback → transfer task.*

**Step 5 — Add the apparatus.** Front matter/metadata; advance organizers; glossary (pre-training); signaling headings; summaries; interleaved + spaced review sets; index. Quarantine any procedural "how-to" or narrative "tutorial" content into labeled blocks so the reference register stays clean.

**Step 6 — Build the explanatory/educational layer.** Convert the author's claims into elaboration prompts ("why?"), supply concrete examples where the book was abstract, and add worked examples (the **worked-example effect** reduces load for novices — with the caveat of the **expertise-reversal effect**: fade worked examples as expertise grows).

**Step 7 — Compress without losing fidelity.** Apply Mayer's coherence principle: cut seductive details, redundant anecdotes, and rhetorical padding while preserving every load-bearing claim, definition, mechanism, and caveat. Verify by checking each enduring understanding and objective is fully recoverable from the review alone (the substitution test).

### Dual-Stakeholder Design (≈80% human / 20% AI)

**Where needs ALIGN (do these — they serve both):**
- **Explicit hierarchical headings (H1>H2>H3).** Humans get signaling (Mayer); AI/RAG gets clean chunk boundaries — "Consistent heading hierarchies help AI agents understand document structure."
- **Atomic, self-contained sections.** Humans get chunking and modularity; AI gets retrievable units. Per kapa.ai's documentation guidance, AI "cannot infer unstated information"; documentation should be "explicit, self-contained, and contextually complete" — **"Every page is Page One."**
- **One term per concept.** Humans avoid confusion; AI avoids failing to link synonyms — "Pick one term for each concept and stick with it."
- **Glossary + defined terms.** Pre-training for humans; disambiguation anchors for AI.
- **Explicit naming over pronouns/anaphora.** Avoid "the method mentioned earlier"; name it. Severed anaphora breaks isolated AI chunks and also helps skimming humans.
- **Metadata / front matter.** A title-H1 + summary blockquote + sectioned links mirrors the **llms.txt** convention (Jeremy Howard / Answer.AI, published September 3, 2024): a markdown file whose only required element is an H1 name, followed by a blockquote summary and H2 link-lists. Howard's rationale: "llms.txt markdown is human and LLM readable, but is also in a precise format allowing fixed processing methods (i.e. classical programming techniques such as parsers and regex)." YAML frontmatter (semantic/graph metadata) further boosts RAG retrieval.

**Where needs DIVERGE (trade-offs):**
- **Engagement devices** (narrative hooks, motivational framing, interactive/reactive widgets, personalization voice): high value for humans (Mayer's personalization principle; Victor's explorables), low/no value for an AI consumer and can even add parsing noise. Keep them, but isolate them so they're strippable.
- **Redundancy / spaced recap**: humans benefit from spaced re-encounters and worked recaps; AI chunking prefers non-duplicated, self-describing units (duplication can pollute retrieval). Resolution: place repetition in clearly-marked "Review" blocks the AI pipeline can dedupe/skip.
- **Embedded retrieval prompts**: central for human retention (mnemonic medium); for AI they're inert unless tagged. Resolution: mark prompts with consistent syntax/metadata so they're machine-identifiable and skippable.

## Recommendations

**The Canonical Review Design Policy (named core models, ready to become a cheat-sheet):**

1. **Backward-Design First (UbD + Constructive Alignment).** Before writing, list the *enduring understandings*, the *Bloom-tagged objectives*, and the *self-check evidence*. Gate: if a passage doesn't serve an enduring understanding or an objective, it goes to "familiar-with" appendix or is cut.
2. **Diátaxis Separation.** Author primarily in **reference + explanation**; quarantine how-to and tutorial content in labeled blocks. Gate: no section mixes neutral facts with discursive "why."
3. **Atomic Modular Sections (Atomicity + Information Mapping).** One concept per section, self-contained, API-like declarative title. Gate: each section is comprehensible if retrieved alone.
4. **Load Discipline (CLT + Mayer Coherence/Signaling/Pre-training).** Glossary-first; cut seductive details; signal structure; place visuals contiguously. Gate: zero extraneous anecdotes survive the coherence pass.
5. **Active Layer (Six Strategies + Mnemonic Medium).** Every section ends with retrieval prompts; review sets are spaced and interleaved; abstractions paired with concrete examples and dual-coded visuals. Gate: no section is purely passive prose.
6. **Instructional Template (Gagné/Merrill).** Fixed per-section skeleton (organizer → objective → prior link → explain → worked example → retrieve → feedback → transfer).
7. **Dual-Stakeholder Encoding.** Hierarchical headings, one-term naming, explicit references, glossary, and llms.txt-style front matter + YAML metadata; engagement/redundancy devices isolated and machine-skippable.
8. **Fidelity/Substitution Test.** Verify the original can be set aside: every enduring understanding, mechanism, definition, and caveat is recoverable from the review alone.

**Staged rollout:** (a) Pilot on one book, measuring whether a naive reader passes the objective-based self-checks without the original. (b) If pass rates clear ~80%, codify the template and the condensed cheat-sheet. (c) Add AI-consumption metadata and test retrieval precision. **Thresholds that change the plan:** if readers fail higher-order (Apply/Analyze) checks, add more worked examples and transfer tasks; if AI retrieval returns fragmented answers, tighten chunk self-containment and naming; if the review feels bloated, re-run the coherence pass.

## Caveats
- **Evidence strength varies.** Retrieval practice, spacing, and active learning are very robustly supported; the strict additivity of CLT's three loads and the optimal "dose" of active learning are contested. Advance organizers show mixed results (only ~12 of 32 studies in one review found positive effects).
- **Context-dependence.** The worked-example effect reverses for experts (expertise-reversal effect); pre-training and prior knowledge change what counts as intrinsic load. A Canonical Review should state its assumed reader.
- **AI-design conventions are immature.** `llms.txt` is a *proposed*, non-ratified convention; claimed SEO/visibility benefits are largely vendor-reported and not independently verified. RAG failure statistics circulating in vendor blogs are often unsourced.
- **The mnemonic medium has open questions** its own authors flag (does benefit outweigh cost outside early-stage learning; adoption depends on web tooling).
- **Generative-AI tutoring carries risks** (factual errors, over-reliance/"metacognitive laziness") noted in 2025–26 literature.