---
title: "3D printer setup and materials guide"
uuid: 8a4147d5-a431-4fd2-9a95-9a6acca16685
created: 2026-07-15
updated: 2026-07-15
trunk: BLACK
messages: 4
chars: 22856
artifacts: 0
generated_files: 1
tools: [ask_user_input_v0, create_file, present_files, view, web_search]
source: claude.ai-export-2026-08-15
---

# 3D printer setup and materials guide

> **Conversation Overview**

The person recently acquired an Anycubic Kobra S1 (enclosed CoreXY printer) and Anycubic ACE Pro (4-slot multi-material/drying unit), and asked Claude to produce a comprehensive bill of materials for getting productively set up without having to figure things out incrementally. The person communicates via voice input, so transcriptions contain phonetic approximations of product names that Claude interpreted correctly. They explicitly requested a consultative approach with clarifying questions before Claude proceeded to the deliverable.

Claude used a structured multi-question intake to establish three key parameters: primary use case (product parts — specifically SlimeVR tracker enclosures), accessory budget ($250–500), and existing tool situation (solid collection already on hand). These answers shaped the entire document, allowing Claude to skip generic beginner items and focus the BOM on functional part production. The person is working on physical tracker components and enclosures as part of the SlimeVR project previously discussed.

Claude researched machine-specific specifications before writing — confirming the Kobra S1 uses a tool-free quick-release hotend cartridge system (incompatible with standard MK8/V6 nozzles), and that the ACE Pro's drying ceiling is 55°C (adequate for PLA/PETG but insufficient for ASA/ABS, which require a standalone dryer reaching ~70°C). Claude also surfaced a known ACE Pro compatibility issue with matte PLA causing false tangle detection. The deliverable was a tiered markdown reference document saved to outputs, structured with a table of contents covering machine facts, three budget phases (~$135 / ~$185 / ~$140), a material strategy table for enclosures, a first-72-hours commissioning sequence, and a do-not-buy list. The material strategy centers PETG for v1 prototypes and ASA for production-grade enclosures given its heat resistance, UV stability, and naturally satin-matte finish. Heat-set brass inserts (M3) are called out as the correct approach for enclosures that open repeatedly for battery access. Local climate (Florida humidity) is noted as a meaningful factor driving filament storage and drying recommendations throughout the document.

**Files produced**

- [kobra-s1-startup-bom.md](../files/2026-07-15_kobra-s1-startup-bommd.md)

---
## 🧑 Papi  <sub>2026-07-15 07:52:27</sub>

Okay. I just got an any cubic s... any cubic COBRA s one and an any cubic ace pro. Basically, that's all I have, though. That's all the hardware I have. I want a full bill of materials to actually start using this thing productively without having to, like, like, figure it out as I go. Like, give me... let's... like, what what is it that I need to to have, like, ideally and then to just get going? Um, consult and ask questions to

---

## 🤖 Claude  <sub>2026-07-15 07:53:28</sub>

Parsing the voice transcription, Papi mentioned getting an "Anycubic Kobra S1" — a CoreXY enclosed 3D printer — and an "Anycubic ACE Pro," which is the multi-color filament system and dryer box that works with it, similar to Bambu Lab's setup. So they've picked up a complete 3D printer system.

They're asking for a full bill of materials to get started productively without having to figure everything out themselves, and they explicitly want me to ask clarifying questions. Given their past research into 3D printing business opportunities — dental/orthodontic work, gaming miniatures, B2B prototyping — plus the SlimeVR tracker project that would need custom enclosures, this purchase could connect to any of those directions. But I shouldn't assume. Since they're on mobile with voice input and specifically requested consultation and questions, I should use the ask_user_input tool to understand what they're actually planning to build and what constraints matter most to them.

Now I'm thinking through what actually determines a useful BOM for the Kobra S1 Combo. The key variables are what type of prints they're targeting (functional parts versus miniatures versus props versus product enclosures), their budget for accessories, and what tools they already have access to given their food service background. For a machine like this with the ACE Pro multi-material unit, I need to know about filament types they'll need, storage and drying solutions, and whether they're planning to work with flexible materials or specialty filaments down the line.

For the consumables and maintenance side, I'm mapping out bed adhesion surfaces, spare nozzles in different sizes since the S1 has a quick-swap system, cleaning tools, lubricants for the mechanical components, and replacement parts like PTFE tubing for the feeder paths.

Now I'm thinking through the hand tools needed for finishing prints—flush cutters, deburring tools, files, hobby knife, metal scraper, digital calipers for calibration work, hex keys, tweezers, and pliers. I'm also considering post-processing supplies like sandpaper in various grits, super glue for assembling multi-part prints, and optional paint/primer for detailed work. The S1 appears to have an enclosed build chamber with some kind of filtration system, though I'm still clarifying the exact specs on that.

For software, I'd use Anycubic Slicer Next or OrcaSlicer (both free, with the former being their Orca-based option), and I'm moving into CAD tools next.

Now I need to decide whether to jump straight into a BOM or ask clarifying questions first — the user specifically asked me to consult and ask, so I should use the input tool to gather some key details about their setup, experience level, and what they're actually trying to print. So the real structure here is a tiered BOM: what they need on day one versus what rounds out a fully productive setup. The key variables that actually shift what I'd recommend are the primary use case (functional parts versus miniatures versus a mix), their accessory budget tier, and what tools they already have on hand.

I'm settling on three focused questions: use case as a multi-select since they might be doing multiple things, budget as a single choice, and existing tools grouped into rough categories like "basically nothing," "basic hand tools," or "solid collection" — that's cleaner than listing individual items and still captures whether I need to budget for calipers or IPA.

I'm sketching out the first question around their main printing goals, thinking through options like SlimeVR enclosures, display minis, functional prototypes — though I'm realizing some of these overlap and need tightening up.

Then I'm planning a couple follow-ups: one on accessory budget (under $100 up to "money's no object"), and another on what tools they already have at home. Once I present these questions, I'll stop and wait for their answers before moving to the actual BOM — no need to search for Kobra S1 specs yet since the questions come first.

I'm thinking the final deliverable should be a markdown document with a table of contents, matching how Papi likes things organized. But that's for next turn. Right now I'll keep the tone casual and conversational, acknowledge that the Kobra S1 and ACE Pro combo is a solid enclosed CoreXY setup with 4-color drying capability, then jump straight into the questions without over-formatting.Kobra S1 with the ACE Pro is a legit combo — enclosed CoreXY plus a 4-slot multicolor unit that doubles as a filament dryer. Good bones. What goes on the BOM shifts a lot depending on what you're actually feeding it, so let me get a read before I spec it out as a proper doc.
```
This block is not supported on your current device yet.
```

---

## 🧑 Papi  <sub>2026-07-15 07:53:52</sub>

Q: What's the main mission for this printer? (Select all that apply)
A: Product parts (SlimeVR, enclosures)

Q: Accessory budget beyond the printer itself?
A: $250–500

Q: What's your current tool situation?
A: Solid tool collection

---

## 🤖 Claude  <sub>2026-07-15 07:58:33</sub>

So Papi's clarifying the core business: SlimeVR is manufacturing physical tracker components and enclosures as of February 2026. The engineering requirements are pretty specific—dimensional precision for the housings, thermal management since the ESP32-C3 boards and 18650 batteries generate heat, and overall durability. Materials-wise, PETG and ABS/ASA are the primary candidates given the Kobra S1's enclosed design, with potential polycarbonate blends down the line.

With a $250–500 accessories budget and an already solid tool collection, I should focus the BOM on production-specific items rather than basics—digital calipers are non-negotiable for product work even if Papi has general tools. The recommendation needs to be tailored around functional part production on the Kobra S1 and ACE Pro printers.

Now I'm thinking through what I actually need to verify versus what I'm confident about with the Kobra S1's specs—the build volume, temperature limits, and capabilities matter for recommending the right materials and settings. I should verify a few hardware specifics with targeted searches before finalizing the reference doc — mainly the nozzle compatibility ecosystem and whether the ACE Pro officially supports TPU, plus bed temperature ranges for different materials on this machine. A couple of quick searches on the Kobra S1 specs and ACE Pro capabilities should give me enough confidence to build out accurate documentation for Papi.

Now I'm thinking about the deliverable format — Papi prefers markdown files structured with a table of contents in a knowledgebase style rather than Word documents. Since this is a markdown file creation task, I need to check the relevant SKILL.md file first, but I'm noticing the available skills list doesn't explicitly include a markdown skill, even though the instructions mention checking plausibly-relevant skills.

My approach: I'll quickly view the /mnt/skills/public directory to see what's actually available, then search for the Kobra S1 and ACE Pro TPU specifications online, and finally build out a markdown bill of materials with a table of contents that separates day-one essentials from the complete product setup.

For the filament strategy, PLA is just for quick prototyping iterations since it lacks heat resistance for actual shipped parts. PETG becomes the main candidate for production enclosures—it's tough, slightly flexible, handles temperatures around 75–80°C well, and works fine for 18650 battery holders since those cells stay under 60°C in normal operation.

ASA is the premium option with better UV stability and higher temperature tolerance (~95–100°C), giving a more polished matte finish that suits a boutique product, and the enclosed chamber on the S1 makes it printable without excessive warping. TPU could work for gaskets, bumpers, or battery retention clips, though it needs the external spool holder since it can't feed through the direct path.

For color, matte black ASA is the classic production choice, and there's an interesting alignment with Papi's aesthetic palette of black, OD olive, and coyote tones — Polymaker makes an army green ASA that could fit that vibe. On the brand side, Polymaker (PolyLite/PolyMax) is solid for consistency on production parts, though Bambu, eSun, Overture, and Anycubic's own filaments all work fine depending on budget.

The drying situation is tricky in Florida humidity — the ACE Pro maxes out at 55°C which is fine for PLA and PETG but ASA really wants 80–90°C, so a dedicated dryer would help ensure proper moisture removal before printing. Spare plates in smooth or satin PEI give different surface finishes for product faces, and a glue stick (Magigoo or basic PVP) protects against PETG bonding too hard to the bed while helping ASA adhesion. I'll need 91–99% IPA and microfiber cloths for maintenance, plus extra 0.4mm nozzles on hand for clog prevention.

For nozzles, a 0.6mm works well for faster drafts, and I could add a 0.2mm later if fine detail work becomes necessary—though that's not the immediate priority. If I move into carbon-fiber-filled materials like PETG-CF in phase 2, I'd need hardened steel nozzles since those materials are abrasive, but that's worth flagging as a future upgrade since PETG-CF actually gives a premium matte finish that's ideal for boutique trackers. Basic cleaning tools like nozzle needles and a brass brush should already be included.

For maintenance, I need spare PTFE tubes and a cutter since the ACE Pro's multi-path feed system will eventually wear them down, plus a good synthetic lubricant like Super Lube with PTFE for the rails and leadscrew—that's the universal solution. A spare hotend silicone sock is worth having on hand, and IPA is already accounted for.

On the calibration and QA side, digital calipers are essential if I don't already own them—something like iGaging or Neiko in the $25–35 range is solid enough, and I should flag this as mandatory for product work. Feeler gauges aren't needed since the machine has auto-leveling, and I'm planning test prints to validate everything.

For the enclosure hardware—which is honestly where most starter BOMs fall short—I need heat-set threaded inserts (M3 brass, the Voron-style kit around $15–20) and soldering iron insert tips to install them, though I should check if I actually have a soldering iron available given the SlimeVR ESP32 work. An M3 screw assortment in SHCS or BHCS is essential too, running about $15–20. Heat-set inserts are critical here since the enclosure will get opened repeatedly for things like battery swaps.

For post-processing, I'm looking at a deburring tool (maybe already owned, but worth flagging), sandpaper (probably have it), and CA glue with activator (likely on hand). Paints and finishes aren't needed.

On the environment side, I need to figure out whether the S1 has a built-in air purifier or activated carbon filter for ASA/ABS fumes—I should verify this. If not, a printable carbon filter setup would work.  Given [CITY]'s climate, ventilation during ASA runs is important. For fire safety, a smoke detector near the printer and avoiding unattended overnight prints early on are solid precautions.

Software-wise, I'm looking at free options: Anycubic Slicer Next or OrcaSlicer (which supports the Kobra S1), Fusion 360 for the CAD work since it's best for product design with parametric features and insert bosses, and Printables/MakerWorld for calibration models.

Now I'm working through the budget breakdown to tier everything out. Phase 2 covers production essentials like ASA filament, heat-set inserts, hardware, and a dedicated dryer, bringing the total to around $350–400 for core phases. Phase 3 adds optional premium materials like carbon-fiber PETG and TPU if budget allows. I should also note what typically ships in the box to prevent duplicate purchases, and add a quick primer on the first 48 hours of setup.

I need to verify some specifics about the Kobra S1 — its nozzle temperature limits, bed capacity, what's included stock, and how the nozzle swap system works — plus confirm the drying temperature for TPU on the ACE Pro.

Before I write anything, I'll check my available skills, then run those searches and build out the startup guide as a markdown file with a bill of materials table and a quick commissioning checklist. Since this is Florida humidity, I should emphasize the drying step — that's a real consideration for filament storage here. The doc will be reference-style with a table of contents, keeping the prose lean and letting the BOM table do the heavy lifting. Alright, let me run the searches now.I'm focusing the packing list on materials, drying solutions, and enclosure hardware rather than generic padding, and I'll verify some machine specifics before finalizing the documentation.
```
This block is not supported on your current device yet.
```

So the Kobra S1 uses a 320°C tool-free quick-release system where swapping nozzles actually means replacing the entire hotend unit—these are integrated units, not just tips. Anycubic offers hardened steel versions in 0.4, 0.6, and 0.8mm, with the standard 0.4mm included in the box. The TPU filament they're working with is single-color.

I still need to pin down the ACE Pro's drying temperature specs—I'm fairly confident the gen-1 maxes out around 55°C, while the newer ACE 2 Pro goes to 65°C with humidity detection. I should also verify whether the S1 comes with active carbon filtration stock or if that's an optional accessory. Let me search for the ACE Pro drying temperature specs directly to confirm.
```
This block is not supported on your current device yet.
```

So the ACE Pro gen 1 that Papi has maxes out at 55°C with dual 200W heaters and can dry while printing for up to 24 hours—it handles PLA, PETG, TPU, and PVB well, though ASA, ABS, PA, and carbon fiber are compatible but not ideal. TPU can dry in it but can't be fed through the printer itself since TPU requires single-color direct feeding. The unit comes with a mat.

There's a quirk with matte PLA where the textured finish can trigger false tangle detection, which is worth noting since matte black is such a popular colorway—for boutique parts needing that matte look, ASA or a textured plate might actually be the better route. The community also found a nice hack using PC4-M6 quick-release couplings for the ACE Pro's tube ports for around $5.

On the Kobra S1 side, it ships with a 320°C quick-release hotend in 0.4mm standard, with hardened steel options available for 0.4, 0.6, and 0.8mm sizes. The printer includes a camera and uses Anycubic Slicer Next, which is Orca-based. There's some uncertainty about whether the stock hotend is hardened steel or brass—the S1 Max FAQ mentions the Max comes with hardened 0.4 pre-installed, but Anycubic's own S1 product page just lists it as a standard 0.4mm hotend, so I should probably note that users should verify which version they have.

For ASA drying, the real constraint is temperature—ASA ideally wants around 80°C, but the ACE Pro maxes out at 55°C and most budget dryers top out around 70°C. The Sunlu FilaDryer S2 and S4 both hit that 70°C ceiling, which works fine for ASA in practice over several hours. I'll recommend a standalone dryer that reaches 70°C for production materials while the ACE Pro handles routine PLA and PETG maintenance drying.

Before I write the doc, I need to check if there's a markdown skill available in the public skills directory—it's a mandatory step before creating any file. Then I'll structure this as a knowledgebase-style reference with a table of contents, starting with the core assumptions about the Kobra S1 setup and the production mission.

Now I'm laying out the calibration and prototyping phase with a breakdown of materials needed—filament types, adhesion supplies, storage solutions, and tools—organized in a table format showing what to order, specifications, approximate cost, and the reasoning behind each item.

For Phase 2, I'm shifting toward production readiness with engineering materials like ASA, a dedicated high-temperature dryer for polymers that need more heat than the ACE can provide, heat-set inserts and fasteners for assembly, a larger nozzle for faster iteration, and various maintenance supplies like lubricant and PTFE tubing. I'm also considering whether to include a second build plate with a different texture than the stock one, trying to be precise about what ships standard rather than overstating.

Phase 3 moves into specialized territory — hardened steel hotends for abrasive materials like carbon-filled PETG and TPU, safety considerations like a smart plug and smoke detector for ASA fumes, and a printable carbon filter for ventilation. I'm starting to map out a filament strategy table that breaks down materials by their role and handling requirements.

Then there's the commissioning sequence for the first 72 hours: unboxing and firmware setup, running auto-calibration, printing a test benchy in stock PLA to verify tolerances with calipers, drying PETG for 8 hours, printing the enclosure draft in PETG, iterating on that design, and only then moving to ASA production runs. The [CITY] humidity is a factor too — ASA especially needs proper storage and drying before any serious prints. I'm also tracking a budget summary to keep the total within the $250–500 range across all phases.

Now I'm laying out what not to buy: skip the fancy bed adhesives beyond a glue stick, avoid proprietary nozzle kits, skip filament sampler packs since we're focused, don't buy an enclosure separately since the printer comes enclosed, and hold off on third-party build plates until we understand the stock setup. For the budget math, Phase 1 covers PLA, PETG, basic maintenance supplies, and spare hotends — roughly $139. Phase 2 adds ASA, a filament dryer in the $40–90 range, inserts, iron tips, and various small parts — around $202. That puts the core setup at about $340, well within budget, with Phase 3 optional upgrades pushing toward $490 if needed.

For citations, I'll keep them in the chat response since the document itself is plain text and can't use citation tags — I'll call out the machine-specific claims like TPU compatibility, the 55°C bed temp, and matte PLA behavior with sources there. The file goes first, then a brief summary in chat to keep things lean.
```
This block is not supported on your current device yet.
```

Since markdown is Papi's preferred format and no special doc-format skill applies here, I'll create the file directly using plain markdown with a table of contents structure and BOM tables, saving it to the outputs folder.

Generating markdown document... Bed Weld or Magigoo at $18 as an alternative to the glue stick, plus IPA for cleaning. Phase 1 lands around $125–150, Phase 2 around $170–200 for the ASA workflow setup, and Phase 3 as an optional stretch at ~$140 for hardened hotends, carbon fiber materials, and monitoring upgrades—keeping the core build in the $300–350 range.

Now I'm mapping out the machine's actual capabilities: the hotend uses quick-release swaps up to 320°C with hardened variants available, the ACE Pro dries at 55°C max across four slots but isn't ideal for ASA/ABS/carbon fiber, TPU feeds direct only, and carbon or glass-filled filaments bypass the dryer entirely to avoid channel wear and require the hardened hotend.

I'm also noting the material quirks—matte PLA tends to tangle in the ACE so I'd go with ASA or a textured plate instead, cardboard spools need adapters, and the slicer is Anycubic's Orca-based version.

For the first 72 hours, the sequence is firmware update first, then full auto-calibration covering PID tuning and auto-leveling, followed by a stock test print and calibration set.

After that, I'm running a dimensional test with a 25mm cube and tolerance checks using calipers to dial in shrinkage and flow, then loading PETG into the ACE after an 8-hour dry cycle at 55°C, printing an enclosure draft to measure and refine, and saving named profiles per material. ASA comes last after PETG is dialed—it needs a longer dry at 70°C, glue stick on the plate, and ventilation. I should also practice heat-set inserts on scrap first, and skip generic nozzle packs.

Skipping the expensive stuff like enclosure kits, adhesion potions, filament samplers, and dry cabinets since the ACE and vac bags handle it. For SlimeVR enclosure shells, I'll print face-down on the textured plate for a uniform premium finish with inserts on the inside, and PETG works fine for skin temps but ASA gives better margin near charging circuits. ASA's natural matte finish ties to the brand palette—matte black or OD green options exist—so I'll note that for colorway consistency without overdoing it.

Now I'm aiming for around 180–220 lines total, then I'll present the file with a short chat message citing the key gotchas from research: TPU is single-color only, ACE has a 55°C ceiling, and matte PLA has finish issues.No markdown skill in the library — writing the doc directly.
```
This block is not supported on your current device yet.
```

I've created the file and now I'm pulling together the key facts from the search results with proper citations, keeping the summary concise.
```
This block is not supported on your current device yet.
```

Full BOM's ready — three phases, ~$135 to start printing this week, ~$320 for the productive core, ~$460 if you take every optional. Built around PETG for v1 enclosures and ASA for production grade, with heat-set inserts as the move for hot-swap battery access.

Three machine gotchas baked into the doc that would've bitten you mid-figuring-it-out: TPU can't run through the ACE Pro — it's single-color direct feed only, the ACE's drying tops out at 55°C (fine for PLA/PETG, not for ASA — hence the $45 standalone dryer in Phase 2), and matte PLA has known compatibility problems in the ACE Pro, so it's on the do-not-buy list — you get the matte look from ASA instead, which conveniently is also the production-grade material.

One thing to check when the boxes land: whether your combo shipped with a textured or smooth plate, so you know which one the Phase 3 spare should be.