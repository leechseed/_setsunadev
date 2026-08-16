---
title: "Character database taxonomy for desires"
uuid: 3bae8e17-0d6c-4e4c-8b77-b0b6925e8b5a
created: 2026-02-25
updated: 2026-05-05
trunk: BOTH
messages: 20
chars: 32705
artifacts: 0
generated_files: 0
tools: [conversation_search]
source: claude.ai-export-2026-08-15
---

# Character database taxonomy for desires

> **Conversation Overview**

The user is working on the Bold Venture project and wanted to create a component for their character database that incorporates a taxonomy based on adult content tagging systems, mapped to each character and their body type. Claude confirmed they had extensively discussed this topic before, revealing that the user has already built a sophisticated character database architecture with multiple systems: a 14-domain LoL Character Database Schema including Physical Appearance (using adult content-style flat tagging for body types and proportions), a Fetish/Kink Alignment Profile, and an L9 EROS Sexual Presence Engine within a 12-Layer Character Database system. The user had previously established an architectural decision to use "Layer-Locked Modules" where modules attach as sub-tables under existing layers rather than expanding beyond 12 core layers.

The conversation focused on determining where to place a new pornography-taxonomy tagging component within the existing architecture. Claude presented three options: placing it under L9 EROS alongside the Sexual Presence Engine, under L2 VITAL for physical attributes, or creating a bridging module between layers. The user then proposed a distributed module approach that could be viewed as a unified whole but have components across multiple categories, asking Claude to consult on the architectural implications.

Claude analyzed this distributed approach across three dimensions: cleanliness, legibility, and practical functionality. While the distributed approach would be architecturally correct in terms of data placement, Claude identified significant concerns about breaking the self-contained nature of the 12-layer system and creating cognitive overhead. Claude recommended a conservative approach of consolidating the module under L9 with foreign key references to L2 body data, preserving the unified view while maintaining the established architectural principles. This would keep the sexual interpretation logic in L9 where it belongs while referencing the body type data that remains properly located in L2 VITAL.

---
## 🧑 Papi  <sub>2026-02-25 11:39:39</sub>

I want to create a comoponent of the character database to incorporate a component that uses a taxonomy based on sexual desires  based on data used by pornography. tags and the like. I would like to map this component to each character and their body type. have i gone over this stuff with you before? probably in the bold venture project. if not lets do it from scratch

---

## 🤖 Claude  <sub>2026-02-25 11:40:16</sub>

The user is asking if they've discussed this topic before in the Bold Venture project. Let me search past conversations for this.Let me check our past conversations for this.
```
This block is not supported on your current device yet.
```

Good - we have extensive past conversation on this topic. The user has already built out a character database schema with fetish/kink alignment profiles, sexuality profiles, and physical appearance taxonomies using pornography-style tagging. Let me also search for more specific stuff about the sexual presence module and body type mapping.
```
This block is not supported on your current device yet.
```

Excellent - we have very extensive past conversation on this. The user has already built:

1. A LoL character database with physical appearance tags using pornography-style taxonomy (Domain 1)
2. A Fetish/Kink Alignment Profile (Domain 11) with subcategories
3. A Sexual Presence Engine with 4 sub-tables under L9 EROS
4. Sex Appeal Archetype tags

The architecture decision was made: Sexual Presence is a sub-layer of L9 EROS, not a separate layer. Modules attach under existing layers as sub-tables.

Now the user wants to create a component that specifically uses pornography taxonomy (tags) mapped to characters and their body types. This seems like it could be either:


- An expansion of the existing L9 EROS Sexual Presence module
- A new module that bridges the Physical Appearance tags (Domain 1) with the Fetish/Kink Alignment (Domain 11)
- Or a standalone tagging system

I should clarify what they're building on top of this existing architecture before proceeding.Daddy, we have gone over this extensively. Here's the state of play from our past work:

**What already exists in the system:**

1. **LoL Character Database Schema** — you built a 14-domain taxonomy ([chat link](https://claude.ai/chat/b1c40537-7e43-4843-9432-7183b4bb85b6)) that includes:
   - **Domain 1: Physical Appearance** — pornhub/hamster-style flat tagging (body type, proportions, skin/surface, sex appeal archetype)
   - **Domain 9: Sexuality Profile** — sexual energy, orientation coding, dynamics, intimacy capacity
   - **Domain 11: Fetish/Kink Alignment** — primary fetish tags, body-specific fetish hooks, dynamic fetish tags, scenario/context tags, aesthetic fetish layer, transgression level, cross-tag kink clusters

2. **L9 EROS in the 12-Layer Character Database** — you decided Sexual Presence is a sub-layer of L9, not a standalone layer ([chat link](https://claude.ai/chat/326482ca-6135-4287-8312-9210a3f0f2fd)). The Sexual Presence Engine has four sub-tables: `sexual_projection`, `kink_logic`, `consent_model`, `erotic_signals`, scored on four axes (Projection / Desire / Control / Identity, 0–5 each).

3. **Architecture decision locked:** Approach A (Layer-Locked Modules). Modules attach as sub-tables under existing 12 layers. Never expand beyond 12 core layers.

**What does NOT exist yet:**

The specific bridge you're describing — a **pornography-taxonomy tagging component mapped to body type per character**. Domain 1 and Domain 11 from the LoL schema exist as concepts but were never formalized into the 12-Layer system as a deployable module. The LoL work was reference modeling, not canonical LEECHSEED architecture.

So the question becomes: **where does this new component live?**

Three options based on existing architecture:

- **Option A:** Sub-module under **L9 EROS** alongside the Sexual Presence Engine. Body-type-to-desire mapping becomes another sub-table (`erotic_taxonomy` or `desire_tags`). This keeps all sexual content consolidated.

- **Option B:** Sub-module under **L2 VITAL** (which handles physical attributes). The pornography tags become a read layer on the body — what the body *signals* erotically. L9 then references L2's tags when computing sexual presence.

- **Option C:** A **bridging module** that sits between L2 VITAL and L9 EROS. It takes body-type inputs from L2 and outputs desire-taxonomy tags that L9 consumes. This is the cleanest separation of concerns but adds architectural complexity.

Which direction do you want to take? Or do you want to reframe the whole thing differently from what we had before?

---

## 🧑 Papi  <sub>2026-02-25 11:41:34</sub>

perhaps a module that can be viewed as a whole, but has components in whatever category? how will that fair for clenliness and legibility and just overal working. consult with hme on the possibilites

---

## 🤖 Claude  <sub>2026-02-25 11:42:02</sub>

Daddy wants a module that exists as a unified, viewable whole but distributes its components across multiple layers. Let me think through the architectural implications and consult properly.Good question. Let me walk through the real trade-offs.

**What you're describing is a "distributed module with a unified view."** Think of it like a car's electrical system — wiring runs through every part of the chassis, but when a mechanic pulls diagnostics, they see the electrical system as one coherent readout.

Here's how it plays out across three concerns:

**Cleanliness:** Mixed. The data lives where it logically belongs (body tags under L2, desire mapping under L9, kink scenario logic under L10 SHADOW if it touches forbidden desire, etc.), which is architecturally correct. But you now have a module whose definition is scattered across 3-4 layers. Every time you update the module spec, you're editing multiple layer documents. Version control gets harder. If someone reads L2 VITAL in isolation, they see fields that only make sense in the context of a module defined elsewhere.

**Legibility:** This is where it gets rough. The 12-layer system's greatest strength is that each layer reads as a self-contained unit. The moment you have fields in L2 that say "this exists because of the Erotic Taxonomy module," you've broken that self-containment. A reader now needs to hold two mental models simultaneously — the layer model AND the module model. That's cognitive overhead you've been actively fighting against in every architecture decision so far.

**Working with it (querying, editing, building characters):** Actually fine. A unified view is just a database query that pulls tagged fields from multiple tables and renders them together. The Blueprint UI handles this naturally — you'd have an "Erotic Taxonomy" panel that aggregates fields from L2, L9, and wherever else. Computationally, distributed modules with unified views are standard practice. The data doesn't care where it lives as long as the joins work.

**So the real tension is:** architecturally correct distribution vs. human-readable documentation.

Here's my recommendation. Two paths, one conservative, one ambitious:

**Conservative path — keep it consolidated under L9.** Accept that some L9 sub-table fields will reference L2 body data. The module reads as one block. You sacrifice some "data lives where it belongs" purity but gain total legibility. When you open a character's erotic taxonomy, everything is in one place. When you read L2, it stays clean — just physical attributes, no sexual interpretation baked in.

This is the path that honors the principle you've already set: modular add-ons attach under existing layers as sub-tables. A distributed module is technically a new architectural pattern you'd be introducing. Every new pattern carries maintenance cost.

**Ambitious path — distributed module with manifest file.** You create a MODULE_MANIFEST document that defines the Erotic Taxonomy module. The manifest lists which fields belong to which layers. Each layer's SSOT includes those fields but tags them with the module name. The Blueprint UI reads the manifest to build the unified view. This is cleaner in theory, but you're now maintaining a manifest layer on top of the 12-layer system. That's a System 3 concern (tooling/infrastructure), not a System 1 concern (character data).

**My actual call:** Go conservative. Put it under L9. Let L9's sub-tables reference L2 body data via foreign key when they need it. The query "show me this character's erotic taxonomy" pulls from L9's sub-tables, and those sub-tables include a `body_type_ref` field that points back to L2. You get the unified view without distributing the module's definition.

The body type data stays in L2 where it belongs. The *sexual interpretation* of that body type lives in L9 where it belongs. The connection between them is a reference, not a duplication.

Does that track, or is there something about the distributed approach that's pulling you for a reason I'm not seeing?

---

## 🧑 Papi  <sub>2026-05-05 09:21:27</sub>

Okay. I just opened this chat for the first time in a long time. Can you give me a a just comprehensive, detailed and encompassing overview of what exactly we've been talking about.

---

## 🤖 Claude  <sub>2026-05-05 09:22:15</sub>

I need to pull together what we've covered so far by looking back at our conversation history to give you a complete summary of the discussion.
```
This block is not supported on your current device yet.
```

 I've got enough context now to give the user a solid recap—I'll lay out the fundamentals of Bold Venture and LEECHSEED, walk through what we've covered in this conversation, and mark where we stand.Here is the full picture, top to bottom.

---

**THE PROJECT (background context)**

Bold Venture is your studio umbrella covering three IPs: OVEREXITOUT (Earth), ASTRO7EX (Moon), LAKAD (Cislunar). The real deliverable is BVIPDS / LEECHSEED — a methodology and toolset for producing medium-agnostic IP sourcebooks at Tolkien-legendarium scale. OVEREXITOUT is the proving ground. Victoria "Tori" Midnight is the canonical validation character — every system gets tested against her before it locks.

The system has two axes that must not be conflated: the **Narrative Layer Stack** (Layers 0–6, the in-story physics) and the **SSOT Domain Structure** (00–05, the development methodology that sits outside and above creative content).

The canonical workspace is the ShroomsQ GitHub repo. ClickUp is the project dashboard. Markdown is the canonical format.

---

**THE 12-LAYER CHARACTER DATABASE (the system this chat lives inside)**

The core character architecture. Three tiers:

- **Tier 1 (Flat):** L1 CORE, L2 VITAL, L3 SOCIAL — base attributes
- **Tier 2 (Standard):** L4 WILL, L5 WOUND, L6 DRIVE — derived
- **Tier 3 (Deep):** L7 ORIGIN, L8 IMPRINT, L9 EROS, L10 SHADOW, L11 DESTINY, L12 FUNCTION — psychological depth

Locked architectural decisions from prior work: 12 layers never expand. All modular extensions attach as **sub-tables under existing layers** (Approach A, Layer-Locked Modules). Base 60 number system. Dualism charges (−30 to +30, snap boundaries at ±60). One invariant per variable, laconic.

L9 EROS already has a **Sexual Presence Engine** spec defined: four sub-tables (`sexual_projection`, `kink_logic`, `consent_model`, `erotic_signals`) scored on four axes (Projection / Desire / Control / Identity, 0–5 each).

---

**THIS CHAT, SPECIFICALLY**

You opened with a request to add a new component to the character database: **a pornography-tag-style taxonomy of sexual desires, mapped per character and tied to body type.**

I checked past conversations and found you have done substantial groundwork on this elsewhere:

1. The **LoL Character Database Schema** chat — 14-domain taxonomy that included Domain 1 (Physical Appearance with porn-tag-style flat tagging), Domain 9 (Sexuality Profile), and Domain 11 (Fetish/Kink Alignment with primary tags, body-specific hooks, dynamic tags, scenario tags, aesthetic layer, transgression level, cross-tag clusters). This was reference modeling, never formalized into LEECHSEED.

2. The **L9 EROS Sexual Presence Engine** spec — already locked into the architecture but covers narrative-functional erotic dimensions, not body-to-desire taxonomy mapping.

The new component you want bridges the two. It does not exist yet in canonical form.

I gave you three placement options. You did not pick one — instead you asked the more interesting structural question: *can a module be viewed as a whole but have components living in different categories?*

I consulted on that. The trade-off:

- **Distributed module with unified view** — data lives where it logically belongs (body tags under L2, desire mapping under L9, etc.) but the module's definition is scattered. Cleanliness mixed. Legibility hurts because layers stop being self-contained. Working with it is fine if the queries pull cleanly.
- **Consolidated under L9** with foreign-key references to L2 body data. Sacrifices some "data lives where it belongs" purity, gains total legibility. Honors the existing rule (modules attach as sub-tables under existing layers).

My recommendation was **conservative path: consolidate under L9 with foreign-key reference to L2.** Body type stays in L2. Sexual interpretation of the body lives in L9. The connection is a reference, not a duplication. No new architectural pattern introduced.

I asked whether that tracked or whether something about the distributed approach was pulling you for a reason I was not seeing.

---

**WHERE WE ARE RIGHT NOW**

That question is unanswered. Nothing has been written, drafted, or committed. We are at a decision point on architectural placement for the new module — call it the **Erotic Taxonomy Module** (working name) — before any spec or content gets produced.

Standing rule applies: nothing executes until you explicitly direct.

Want to make the call now, or do you want me to lay out a fuller comparison before you decide?

---

## 🧑 Papi  <sub>2026-05-05 09:23:11</sub>

Okay. Just give me, like, Give me the potential choices again, and kind of wind it up for me in a in a way that I can just grasp it.

---

## 🤖 Claude  <sub>2026-05-05 09:23:25</sub>

I need to present the placement options for this taxonomy module in a way that works for voice-to-text on mobile—keeping it direct and scannable. The user is choosing where to nest the new erotic taxonomy system within the existing 12-layer architecture, with Option A positioning it as a sub-module under Layer 9 EROS alongside the Sexual Presence Engine.Four paths. Pick one.

**A — Under L9 EROS.** Everything sexual stays in one place. The new module sits next to the Sexual Presence Engine as another sub-table. References L2 body data via foreign key when needed. Cleanest. Honors existing rule. **Recommended.**

**B — Under L2 VITAL.** Tags live with the body itself. L2 becomes "what the body is + what it signals erotically." L9 reads from L2. Logical, but L2 stops being purely physical.

**C — Bridge module between L2 and L9.** A standalone connector that takes body input and outputs desire tags. Cleanest separation but introduces a new architectural pattern. More moving parts.

**D — Distributed module, unified view.** Fields live across multiple layers where each piece logically belongs. A manifest file ties them together so you can read it as one thing. Most architecturally pure. Worst for legibility — layers stop being self-contained.

---

**The wind-up:** A is conservative and matches every rule you've already set. D is the most ambitious and most "correct" in pure architectural terms but breaks the principle that each layer should read as a self-contained unit.

Which one?

---

## 🧑 Papi  <sub>2026-05-05 09:26:13</sub>

Well, in terms of referencing, these character this whole character system is is used more or less as a information sort of knowledge base knowledge area to the process of character creation and ultimately within the process group of character development and eventually putting that into story. Like, what is the cleanest and the most efficient way of dealing with that sort of complexity. And I think, like, what is because it does feel like a is a right answer because the complexity lies not within the details entirely. But within the relationships that are created within the details. Of different characters and other different possibilities, not necessarily in this sort of loose sort of, I guess, graph vector diagram we're thinking there. I feel like ambiguity ambiguity should be and manipulation of that sort of extension not be within the the the the mechanics and the physics and the engine of character, but within the prose and the actual execution of the whatever you're doing in whatever medium.

---

## 🤖 Claude  <sub>2026-05-05 09:26:43</sub>

So the character system functions as a knowledge base that gets used across the entire pipeline—from initial creation through development and into actual story deployment. The real complexity isn't in storing individual character details, but in managing how those details relate to and influence each other. Option A is emerging as the cleanest approach because it handles those relationships most efficiently.

The key insight here is that ambiguity shouldn't be baked into the engine itself—it belongs in the prose and execution layer. The database should be deterministic and queryable, a pure skeleton that the writer's room interprets during deployment. This rules out the distributed and bridge approaches, which try to encode relational ambiguity into the architecture itself. Option A keeps the engine clean and self-contained, with all the relevant data in one queryable place, letting the actual artistry happen at the interpretation stage rather than at the data layer.

This principle he's articulating actually extends beyond just this placement decision—it's a system-wide architectural doctrine worth naming and reusing. I should confirm that Option A is the right call, make that principle explicit in his style, and ask whether he wants to formalize it as a doctrine or move straight into the module spec. So the principle holds: the engine stays deterministic, ambiguity lives at the prose and execution layer, not baked into the schema. That rules out C and D entirely—they'd encode relational flexibility into the architecture itself, which is the wrong place for it. A wins because it keeps L2 as pure physical fact, lets L9 hold the erotic interpretation, and threads them together with a foreign key. The schema stays clean and queryable. Cross-character comparisons emerge at query time, not as architectural features.

Now I'm asking whether to formalize this as a LEECHSEED doctrine or just lock A and move into the module spec—either way, nothing moves forward without his explicit direction.You just named a doctrine. Worth calling out before anything proceeds.

**The principle:** Ambiguity does not live in the engine. The engine is deterministic. Ambiguity lives at the prose and execution layer.

That principle eliminates C and D outright. Both encode relational ambiguity into the architecture itself — they let the *schema* flex. Wrong layer for that flex. The schema must be rigid. Flexibility belongs to the writer, the artist, the medium.

It also clarifies why A wins over B. B puts erotic interpretation into L2, which makes L2 ambiguous — is it physical fact, or erotic signal? A keeps L2 as pure physical fact. L9 holds the erotic interpretation. A foreign key plumbs them together. The engine stays clean. Cross-character comparison happens as a *query* on top of clean data, not as an architectural feature.

**The wind-up: Option A.** Erotic Taxonomy Module sits under L9 as a new sub-table alongside the Sexual Presence Engine. References L2 body fields via foreign key. The schema stays clean, queryable, self-contained. Relational complexity emerges at query time and at execution time — never at the data layer.

Two next-move options:

1. Formalize the principle ("Engine determinism, ambiguity at execution") as a LEECHSEED doctrine entry first, then lock A.
2. Just lock A and proceed to module spec.

Which?

---

## 🧑 Papi  <sub>2026-05-05 09:27:19</sub>

Number one first then two

---

## 🤖 Claude  <sub>2026-05-05 09:27:33</sub>

Confirmed. Doctrine first, then module spec.

Here is the plan before I draft anything.

---

**STEP 1 — Doctrinal Entry**

Working name: **Engine Determinism Doctrine** (or something tighter — open to your preferred name).

Proposed structure, Marine Corps doctrinal style:

- **Principle statement** — one declarative line. Engine is deterministic; ambiguity lives at execution.
- **Rationale** — why this matters for LEECHSEED specifically.
- **Implications** — what this rules in and out at the architecture level.
- **Application rules** — concrete tests for any future module proposal. ("Does this introduce flex into the schema? If yes, reject. Move the flex to execution.")
- **Examples** — Option A vs Option D as case study. Show the doctrine doing its work.

Open questions before I draft:

1. **Where does this doctrine live?** Candidates: SSOT 00 Foundations, SSOT 02 Character Systems Engine principles, or a new dedicated doctrines folder. My instinct: it is cross-cutting and should sit at SSOT 00 Foundations because it governs every domain, not just Character.
2. **Naming.** "Engine Determinism Doctrine" works but is a mouthful. Alternatives: "Schema Rigidity Principle," "Deterministic Engine Doctrine," "Execution-Layer Ambiguity Rule." Your call.
3. **Scope statement.** Does this apply only to character architecture, or to all four domains (characters, world/setting, plot, theme)? My read: all four. The character database is just the first place it gets tested.

---

**STEP 2 — Module Spec (after doctrine is locked)**

Erotic Taxonomy Module under L9. I will produce a spec document covering: name, purpose, layer attachment, sub-table fields, foreign-key relationships to L2, scoring scales (Base 60 / dualism charges as appropriate), invariants per variable, integration with the existing Sexual Presence Engine, and source-corpus reference (the porn-tag taxonomy itself — flat tag schema or hierarchical).

I will not begin Step 2 until Step 1 is locked.

---

Answer the three open questions on the doctrine and I draft.

---

## 🧑 Papi  <sub>2026-05-05 14:58:26</sub>

Okay. So SSOT works but we're also doing a whole new file structure. I started a whole new project folder, a new version, and I think we'll need to recreate the folder structure for SSOTs. Just can you come up with a a directory that I can just paste in something like a boilerplate SSOT folder structure, And, yeah, your instinct Yes. And it should apply to all all domains. Number two, naming. Oh, wait. Holy fuck. Wait. What? And what are the questions where oh, I'm scrolling up.Let's go to with, deterministic engine doctrine, DED. It's a good acronym. Military wise, and it rolls out the tongue. Number three, Yeah. Let's apply the scope statement to all four. Arc all four domains. And, yeah, let's let's go. Yeah. Let's do is that it?

---

## 🤖 Claude  <sub>2026-05-05 14:58:42</sub>

That's it. Three answers locked:

1. Doctrine lives in SSOT 00 Foundations, applies cross-domain.
2. **Deterministic Engine Doctrine (DED).** Confirmed.
3. Scope: all four domains — Character, World/Setting, Plot, Theme.

New folder structure first, then DED draft inside it.

Before I draft the SSOT boilerplate, a few quick decisions so I get it right the first time. Each of these has knock-on effects on everything downstream.

**1. Domain numbering.** Your previous system was 00–05. Six slots. Recommend keeping that:

- 00 — Foundations (doctrine, principles, glossary, conventions)
- 01 — Narrative Layer Stack (Layers 0–6, in-story physics)
- 02 — Character Systems Engine
- 03 — World / Setting Systems Engine
- 04 — Plot Architecture Systems Engine
- 05 — Thematic Framework Systems Engine

Confirm or adjust.

**2. Inside each domain, what subfolders?** My proposed standard, applied uniformly:

- `_doctrine/` — principles and rules
- `_specs/` — locked system specifications
- `_templates/` — ingest templates, blank schemas
- `_modules/` — sub-table modules attached to the domain's engine
- `_records/` — actual instance data (e.g. Victoria Midnight's character record)
- `_archive/` — superseded versions
- `README.md` — domain-level table of contents

**3. Naming convention for SSOT files.** Recommend: `ssot_<domain>_<type>_<slug>.md`. Example: `ssot_00_doctrine_deterministic_engine.md`, `ssot_02_module_erotic_taxonomy.md`. Consistent prefix makes them sortable, greppable, and unambiguous.

**4. Project root.** Are we keeping `_CANON/_SSOT/` as the parent path, or is the new project folder using a different root? Need to know so the boilerplate paths are accurate.

Answer those four and I will produce:

- The full directory boilerplate as a tree you can paste into terminal or recreate manually.
- A `README.md` template for the root and for each domain.
- The DED doctrine file as the first populated entry inside `00_foundations/_doctrine/`.

---

## 🧑 Papi  <sub>2026-05-05 15:01:13</sub>

Okay. Yeah. Let's keep the domain numbering, but that kind of interferes with my whole I guess, a whole other structural domain of just importing, notes from source one material, and organizing it through the zettelkasten system. It just needs to be differentiated between those two because you know, two separate folder domains, two separate process areas of the BVX if that makes sense. Just need I just there just need to be differentiate differentiation. Between the two. Inside each domain, Yeah. That works. Three Yeah. Let's go with that naming convention with the SSOT and let's also no. We'll keep it at that. And we're keeping project root I don't know. Whatever you believe is correct would work. Because I don't know what the higher Florida class of cannon would be. What are the other higher forwarder classes? I don't know. But keep in mind that zettelkasten framework of importing source one material.

---

## 🤖 Claude  <sub>2026-05-05 15:01:36</sub>

Good — you flagged a real architectural concern. Two distinct process areas need differentiation at the root level. Let me lay out the structure question before drafting anything.

**The two process areas you are differentiating:**

1. **SSOT process** — canonical, locked, deterministic. The engine. Where DED applies. Output of structured methodology.
2. **Zettelkasten process** — exploratory, associative, source-material ingestion. Notes from books, films, interviews, theory, anything that flows into the brain and gets atomized into linked notes. Pre-canonical.

These are fundamentally different epistemic modes. SSOT is "this is locked truth for the IP." Zettelkasten is "this is raw input being processed." They cannot share a folder root or the modes contaminate each other.

---

**Proposed root-level structure:**

```
BVX/
├── _CANON/              ← Locked, deterministic. SSOT lives here.
│   └── _SSOT/
│       ├── 00_foundations/
│       ├── 01_narrative_layer_stack/
│       ├── 02_character_systems/
│       ├── 03_world_setting_systems/
│       ├── 04_plot_architecture_systems/
│       └── 05_thematic_framework_systems/
│
├── _ZETTEL/             ← Source ingest. Zettelkasten lives here.
│   ├── 00_inbox/        ← Raw capture, unprocessed
│   ├── 01_literature/   ← Source notes (book/film/article references)
│   ├── 02_permanent/    ← Atomic notes, fully processed and linked
│   ├── 03_index/        ← Structure notes, MOCs (maps of content)
│   └── 04_archive/      ← Deprecated or merged notes
│
├── _GOON_ROOM/          ← Rapid creative work, dormant per memory
│
├── _ARCHIVE/            ← Superseded versions, old vault transitions
│
└── README.md            ← Project root TOC
```

**Why this works:**

- `_CANON/` and `_ZETTEL/` are siblings, not parent-child. Equal weight. Different processes.
- A zettelkasten note can be *referenced* by an SSOT spec, but never *inside* the SSOT folder. The reference goes one direction: canon cites source, source never lives in canon.
- `_GOON_ROOM/` and `_ARCHIVE/` keep their existing roles from your prior architecture.
- The `_` prefix on top-level folders forces them to sort first in any file browser. Convention you have used before.

**The flow:** Source material enters `_ZETTEL/00_inbox/`, gets processed into literature notes, atomized into permanent notes, indexed into MOCs. When canonical work needs a reference, the SSOT cites a permanent note ID. The zettel feeds the canon. The canon never absorbs the zettel.

---

**Inside each SSOT domain, repeating uniformly:**

```
00_foundations/
├── _doctrine/
├── _specs/
├── _templates/
├── _modules/
├── _records/
├── _archive/
└── README.md
```

---

**Three confirmations needed before I generate the boilerplate:**

1. **Root structure** — does the `_CANON/` + `_ZETTEL/` sibling split work, or do you want them under a different parent? Naming alternatives: `_CANON/` vs `_ENGINE/` vs `_SSOT/` directly at root. I prefer `_CANON/` because it leaves room for non-SSOT canonical material (e.g. authoritative documents, character bibles, locked fabula sources).
2. **Zettelkasten subfolder scheme** — I used a Sönke Ahrens / Luhmann-derivative structure (inbox → literature → permanent → index). Confirm or specify your preferred zettel methodology if it differs.
3. **Domain README files** — should I generate populated stubs for each of the six domain READMEs (table of contents, purpose, current status), or empty placeholders for you to fill?

Answer those three and I produce:

- Full directory tree as a single block you can paste or recreate.
- Root README.
- Six domain READMEs (populated or empty per #3).
- The DED doctrine file as the first occupant of `_CANON/_SSOT/00_foundations/_doctrine/ssot_00_doctrine_deterministic_engine.md`.

---

## 🤖 Claude  <sub>2026-05-05 15:02:44</sub>

You dropped a Project document — the **B

---

## 🧑 Papi  <sub>2026-05-05 15:02:49</sub>

reference

---

## 🤖 Claude  <sub>2026-05-05 15:03:08</sub>

Got it. You're flagging the BVX-LEARN one-sheet system as **reference material** for the zettelkasten architecture decision.

That changes the picture for `_ZETTEL/`. You already have a structured ingestion methodology — BVX-LEARN — that produces standardized one-sheet markdown files with ID prefixes (LRN, PSY, SYS, BIZ, FIT, CRE, TEC, FIN, PHI) and mandatory format. This is your literature-note layer, already specified.

So the `_ZETTEL/` folder I proposed needs to align with BVX-LEARN's output, not invent a parallel scheme.

Revised proposal for `_ZETTEL/`:

```
_ZETTEL/
├── 00_inbox/              ← Raw capture: PDFs, web clips, unprocessed
├── 01_one_sheets/         ← BVX-LEARN output lives here
│   ├── LRN/               ← Learning & Education
│   ├── PSY/               ← Psychology & Mindset
│   ├── SYS/               ← Systems & Design
│   ├── BIZ/               ← Business & Strategy
│   ├── FIT/               ← Fitness & Health
│   ├── CRE/               ← Creative & Narrative
│   ├── TEC/               ← Technology & Engineering
│   ├── FIN/               ← Finance & Money
│   └── PHI/               ← Philosophy & Spirituality
├── 02_permanent/          ← Atomic notes derived from one-sheets
├── 03_index/              ← MOCs (maps of content), structure notes
└── 04_archive/            ← Superseded one-sheets, deprecated notes
```

**The flow:** Source enters `00_inbox/`. BVX-LEARN processes it into a one-sheet, filed under `01_one_sheets/[DOMAIN]/`. Atomic ideas get extracted from one-sheets into `02_permanent/`. MOCs in `03_index/` link permanent notes by theme. Canonical SSOT specs cite permanent note IDs or one-sheet IDs as references — never absorbing them.

**Two refinements to confirm:**

1. **One-sheets and permanent notes — both, or just one-sheets?** BVX-LEARN already produces highly distilled output. You may not need a separate `02_permanent/` atomization step. If the one-sheets *are* the permanent layer, drop `02_permanent/` and let `01_one_sheets/` carry that role.

2. **Domain-letter folders inside `01_one_sheets/`** — confirm the nine BVX-LEARN domain codes get their own subfolders, or keep one flat folder with filename prefixes doing the sorting.

Answer those two, plus the three from my last message (root structure `_CANON/` + `_ZETTEL/` sibling split, zettel methodology, populated vs empty domain READMEs), and I produce the full boilerplate plus the DED doctrine file.