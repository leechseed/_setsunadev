---
title: Standards register — the harvest, organized
status: research phase · 2026-09-11
source: standards.locus.md
counts:
  harvest_links: 69
  ansi_single_standards: 36
  ansi_industry_package_lists: 19
  org_catalogs: 14
  domains_covered: 15
---

# THE STANDARDS REGISTER

One pull of Chief's 9/11 harvest (`standards.locus.md`). ANSI's webstore blocks direct fetch (403 on every `webstore.ansi.org` URL tried); those rows below are built from indexed search snippets and slug-decoding instead of a live page read — noted per row. Everything else was fetched directly where the URL is cited.

## 1. How standards bodies tier their documents

| Body | Tiers (top → bottom) | Numbering | Free or paid | URL read |
|---|---|---|---|---|
| NASA | NPD (policy) → NPR (procedural requirements) → NASA-STD / NASA-HDBK (technical) | `NPD 1000.0C` style: type + subject number + revision letter | Free, public NODIS library (266 current directives); some need internal NASA access | [nodis3.gsfc.nasa.gov](https://nodis3.gsfc.nasa.gov/Rpt_current_directives.cfm) |
| DoD (DSP/DLA) | MIL-STD (design/interface) → MIL-HDBK (guidance, non-mandatory) → MIL-SPEC/MIL-DTL (detail specs) → MIL-PRF (performance specs) | `MIL-STD-####`, letter revision (e.g. -1472H) | Free via ASSIST (116,970 documents indexed, 257,715 PDFs) | [dsp.dla.mil](https://www.dsp.dla.mil/); search via [assist.dla.mil](https://assist.dla.mil/online/faqs/overview.cfm) |
| ISO | Management-system standards (requirements, auditable — 9001, 27001, 42001) vs. guidance (9004, 10015, "Guide" docs) vs. technical specs/reports (TS, TR) | `ISO #####:YYYY`, parts `-1/-2`, joint `ISO/IEC`, `ISO/IEC/IEEE` | Paid — purchased per-document or as ANSI-webstore packages | [webstore.ansi.org/sdo/iso](https://webstore.ansi.org/sdo/iso) (indexed, not fetched — 403) |
| NATO (NSO) | STANAG (agreement to standardize, ratified) → AP/Allied Publication (the implementing doctrine text a STANAG points to) | `STANAG ####`, `AP-##` | Nominally public list at nso.nato.int; most linked documents gate behind a login/access request | [nso.nato.int/nso/nsdd/main/standards](https://nso.nato.int/nso/nsdd/main/standards) (404 on direct fetch; confirmed via search) |
| IES | RP (Recommended Practice, application-specific lighting) → LM (Light Measurement, test method) → TM (Technical Memorandum, position/explainer) | `RP-##-YY`, `LM-##-YY`, `TM-##-YY` | Paid — store.ies.org; no free tier found | confirmed via search (store.ies.org, standards.globalspec.com) |
| IEEE | Standards (normative, mandatory "shall") → Recommended Practices → Guides (informative) | `IEEE ####-YYYY` | Paid, sold through IEEE and ANSI webstore | [webstore.ansi.org](https://webstore.ansi.org/) (indexed) |
| PMI | Foundational standards (PMBOK Guide — 8th ed. shipped Q4 2025) → Practice Guides (apply the standard, e.g. Agile Practice Guide) → global/industry-extension standards | Named editions, not numbered | Free overview pages; full text requires PMI membership/purchase | [pmi.org/standards](https://www.pmi.org/standards) (403 direct; confirmed via search) |
| ESTA | ANSI E1.x standards (normative) → guidance/working-group documents (informative) | `E1.#-YYYY`, reaffirmed as `(R####)` | **Free** — TSP explicitly publishes at no cost, funded by donations | [tsp.esta.org/tsp/documents/published_docs.php](https://tsp.esta.org/tsp/documents/published_docs.php) |
| CTA | Numbered standards (`CTA-####`) across A/V, wireless power, digital health, cybersecurity, accessibility | `CTA-####` | Mixed — some public standard pages, some "member only access" | [cta.tech/resources/?type=standard](https://www.cta.tech/resources/?type=standard) |

## 2. The register

*Domain key: mgmt = management · qual = quality · infosec = information security & privacy · AI · sw/sys = software & systems engineering · light = lighting & human factors · aero = aerospace & UAS · img = imaging & print · sym = graphical symbols & identification · risk · innov = innovation · contech = consumer tech · enttech = entertainment tech · pm = project management · def = defense & space directives.*

| ID / family | Title (as decoded from source) | Body | Domain | Governs, one line | Free/paid | House area | Source |
|---|---|---|---|---|---|---|---|
| ISO/IEC 42001+42005+42006 | AI management system + AI system impact assessment + AI management-system audit/certification requirements | ISO/IEC | AI | The bundle for standing up, assessing, and certifying an AI management program | Paid | DARKROOM (taxonomy engine) · BLACK | slug decode |
| ISO/IEC 27001+42001 | Information security management + AI management, bundled | ISO/IEC | infosec/AI | Run infosec and AI management under one system | Paid | DARKROOM · OPERATOR | slug decode |
| ISO/IEC 27001+27002+9001 | Infosec requirements + infosec code of practice + quality management | ISO/IEC | infosec/qual | Cross-walks infosec controls into a QMS | Paid | OPERATOR · SOP | slug decode |
| ISO/IEC 27001+9001 | Infosec management + quality management, set | ISO/IEC | infosec/qual | Same pairing, smaller set | Paid | OPERATOR · SOP | slug decode |
| ISO/IEC 42001+27001+27002 | AI management + infosec management + infosec code of practice | ISO/IEC | AI/infosec | AI governance layered on an infosec baseline | Paid | DARKROOM · OPERATOR | slug decode |
| ISO 56000 series | Innovation management — vocabulary, guidance, tools | ISO | innov | Vocabulary and guidance for running an innovation program | Paid | BLACK (BVX) | slug decode |
| IEEE 15288-2014 | Systems and software engineering — system life cycle processes | IEEE | sw/sys | Life-cycle process model for systems engineering | Paid | OPERATOR (tooling) | slug decode |
| ISO/IEC/IEEE 12207:2026 | Software life cycle processes (next edition) | ISO/IEC/IEEE | sw/sys | Software-side twin of 15288 | Paid | OPERATOR (tooling) | slug + [blog.ansi.org](https://blog.ansi.org/ansi/iso-iec-ieee-12207-2026-software-life-cycle/) |
| ISO/IEC 12207 + IEEE 15289 + 25021 + 26531 | Software life cycle + info-product life cycle mgmt + quality measure elements + user-doc content management | Mixed | sw/sys | Software process plus the docs/quality-metric layer around it | Paid | OPERATOR (tooling) | slug decode |
| IEC 61131 | Programmable controllers | IEC | sw/sys | Industrial control programming languages/architecture | Paid | OPERATOR (reference only — no active project uses PLCs) | slug decode |
| ISO 20700:2017 | Guidelines for management consultancy services | ISO | mgmt | How a consulting engagement should be scoped and run | Paid | SOP | slug decode |
| ISO/IEC 27018:2019 | Protection of PII in public clouds acting as PII processors | ISO/IEC | infosec/privacy | Cloud-provider privacy code of practice | Paid | OPERATOR · ORANGE (any cloud-hosted personal data) | slug decode |
| ISO/IEC 27701+27001+27002+29100 | Privacy information management + infosec management + code of practice + privacy framework | ISO/IEC | infosec/privacy | Full privacy-management-system stack | Paid | OPERATOR · ORANGE | slug decode |
| ISO/IEC 17024 | Conformity assessment — requirements for bodies certifying persons | ISO/IEC | mgmt | How a "certification body" for people should be run | Paid | SOP (character/qualification systems, loose fit) | slug decode |
| ISO 9001 + ISO/TS 9002 | QMS requirements + guidelines for applying 9001 | ISO | qual | Requirements plus the "how to apply it" companion | Paid | SOP | slug decode |
| ISO 9001 (small enterprises guide) | QMS requirements, small-enterprise guidance | ISO | qual | 9001 scaled down for small orgs | Paid | SOP | slug decode |
| ISO 10015+10018+9001 | Competence/training + people engagement + QMS | ISO | qual | People-development layer on top of a QMS | Paid | SOP | slug decode |
| IES RP-24 | Recommended Practice: Lighting Sports and Recreational Areas | IES | light | Sports/rec-area lighting design targets | Paid | WARROOM (loose — long-watch venue analog) | confirmed via search |
| SAE AS264F:2016 | Aerospace Standard, AS264 family (exact current scope unconfirmed — SAE's page didn't resolve past the title in a free source) | SAE | aero | Not fully verified — flag for a direct SAE purchase-page check later | Paid | ASTRO7EX | [sae.org/standards/content/as264f](https://sae.org/standards/content/as264f) (title only) |
| IES RP-20 + RP-24 | Lighting Retail Spaces + Lighting Sports/Recreational Areas, bundled | IES | light | Two application-specific lighting practices sold together | Paid | WARROOM | confirmed via search |
| ISO/CIE 8995:2018 | Lighting of work places | ISO/CIE | light | Workplace illuminance/uniformity targets | Paid | WARROOM (long-watch UI) | slug decode |
| ISO 8995:2002 | Lighting of indoor workplaces (earlier edition) | ISO | light | Predecessor to 8995:2018/2025 | Paid | WARROOM | slug decode |
| IES RP-10-20 | Recommended Practice: Lighting Common Applications | IES | light | General-purpose interior lighting practice | Paid | WARROOM | confirmed via search |
| IES RP-23 | Recommended Practice: Lighting Hospitality Spaces | IES | light | Hospitality-venue lighting design | Paid | WARROOM (loose) | confirmed via search |
| ISO/CIE 8995:2025 | Lighting of work places (current edition) | ISO/CIE | light | Latest workplace lighting standard | Paid | WARROOM | slug decode |
| AS/NZS 1680:2006 | Interior lighting series | Standards Australia/NZ | light | Interior lighting design across space types | Paid | WARROOM | slug decode |
| AS/NZS 1680:2017 | Interior lighting series (updated) | Standards Australia/NZ | light | Update to the 2006 edition | Paid | WARROOM | slug decode |
| AIAA G-043B-2018 | Guide to the Preparation of Operational Concept Documents | AIAA | sw/sys | How to write an OpsCon document for a system | Paid | OPERATOR · ASTRO7EX | confirmed via search |
| AIAA G-082-2022 | Guide: Space Systems — Composite Overwrapped Pressure Vessels with a Plastic Liner | AIAA | aero | COPV design guidance for space hardware | Paid | ASTRO7EX | confirmed via search |
| ISO 9001:2015 (small enterprises) | QMS requirements, small-enterprise reading | ISO | qual | Same 9001, small-org lens | Paid | SOP | slug decode |
| ASTM F38 small-UAS collection | Small unmanned aircraft systems — design, terminology, flight manual, maintenance (F2908, F3298, F3341, etc.) | ASTM | aero | The working standards set behind small-drone certification | Paid | ASTRO7EX | confirmed via search |
| AIAG CQI-2021 | Effective Problem Solving (CQI series) | AIAG | qual | Structured root-cause/problem-solving method (automotive-quality lineage) | Paid | SOP | slug decode |
| ISO 25947 series | Fireworks — classification, requirements, test methods | ISO | risk (safety) | Pyrotechnic product safety/classification | Paid | No obvious house fit — reference only | slug decode |
| ISO 3864 series | Graphical symbols, safety colours and safety signs | ISO | sym | Design rules for safety signage and symbol systems | Paid | BLACK (design system) | slug decode |
| ISO/IEC 15415 + 15416 | Barcode print quality — 2D symbol print quality + linear symbol print quality | ISO/IEC | img/sym | How to grade printed barcode quality | Paid | BLACK (BVX-LEARN catalog / identification) | slug decode |
| ISO 9001 series (industry list) | Full ISO 9001 family as ANSI packages it | ISO | qual | QMS requirements across sector variants | Paid | SOP | [webstore.ansi.org/industry/.../iso-9001-series](https://webstore.ansi.org/industry/quality-management/iso-9001-series) (indexed) |
| ISO 10000 series (industry list) | Customer satisfaction + supporting QMS guidance | ISO | qual | Guidance layer around 9001 (local gov't, agriculture, automotive, etc.) | Paid | SOP | indexed |
| Additive manufacturing (ISO/ASTM 52900 series) | Vocabulary (52900), design (52910), qualification (52924), system performance (52941), material extrusion (52903) | ISO/ASTM | mfg | Common vocabulary and process rules for 3D printing | Paid | No obvious fit — reference only | indexed |
| ASTM F38 UAS list (industry page) | Same F38 committee, ANSI's listing of it | ASTM | aero | Drone standards catalog page | Paid | ASTRO7EX | indexed |
| Airport/airplane design (ASTM + SAE) | Runway pavement/lighting (ASTM), aircraft-specific systems like galleys/air conditioning (SAE) | ASTM/SAE | aero | Airport and airplane design/operation standards | Paid | ASTRO7EX | indexed |
| Metadata: content | SCTE, INCITS/ISO/IEC 11179, CTA 861.3, ISO XML metadata interchange, Dublin Core | Mixed | img/sym (metadata) | 10-category metadata taxonomy (content is one) | Paid | BLACK (BVX-LEARN catalog) | indexed |
| Metadata: education | ISO/IEC 19788 (MLR) parts 4/9, DS adoptions | ISO/IEC | metadata | Learning-resource metadata elements | Paid | BLACK (BVX-LEARN catalog) | indexed |
| Metadata: devices | ATIS-0800046, ISO JPSearch, IEC 61966 color-gamut ID | Mixed | metadata | Device/media metadata (color gamut, IPTV) | Paid | BLACK (BVX-LEARN catalog) | indexed |
| Metadata: geographic | ISO 19115-1/-2, INCITS 453 (NAP profile) | ISO/INCITS | metadata | Geographic information metadata schema | Paid | BLACK (BVX-LEARN catalog) | indexed |
| Metadata: graphic arts | SS-ISO 21812 (print product metadata for PDF) | ISO | metadata/img | Print-production workflow metadata | Paid | BLACK (BVX-LEARN catalog) | indexed |
| Software engineering package | ISO/IEC/IEEE 12207 + 15288 bundled | ISO/IEC/IEEE | sw/sys | Software + systems life-cycle processes, packaged | Paid | OPERATOR (tooling) | indexed |
| Blockchain (ISO/TC 307) | Vocabulary (22739), security mgmt (TR 23576), interoperability overview (TR 23249) | ISO | AI/sw (adjacent) | Blockchain/DLT terminology and risk | Paid | No obvious fit — reference only | indexed |
| AI package (ANSI) | ISO/IEC 42001 bundled variously with 22989, 23894, 42005, 42006 | ISO/IEC | AI | Same AI management core, different bundle partners | Paid | DARKROOM | indexed |
| Augmented reality standards | ISO/IEC 18520, 18038, 23000-13; IEEE 1589; ANSI/UL 8400 | Mixed | contech | AR/MR tracking, safety, learning-experience models | Paid | No obvious fit — reference only | indexed |
| Photography (industry list) | ISO 2720, 2721, 3664, 6846, 12232, 14524, 19262 | ISO | img | Exposure, viewing conditions, camera performance, archiving vocabulary | Paid | BLACK (BVX-LEARN catalog / imaging tooling) | indexed |
| Packages: management | Risk mgmt (ISO 31000+Guide 73+IEC 31010), environmental mgmt (ISO 14001/14004/14050/19011), IT security (ISO/IEC 27000 series) | ISO/IEC | mgmt/risk | ANSI's cross-domain management bundles | Paid | SOP · OPERATOR | indexed |
| Packages: X9 | ANSI X9.24-1/-2 + X9.143 (symmetric key management) | ASC X9 | infosec | Financial cryptographic key management | Paid | OPERATOR | indexed |
| Packages: quality management | ISO 9000/9001/9004/19011 core + 10012/10017 add-ons | ISO | qual | The full QMS starter set | Paid | SOP | indexed |
| Packages: risk management | ISO 31000:2018, Guide 73:2009, IEC 31010:2009, SME guide | ISO/IEC | risk | Enterprise risk management process and vocabulary | Paid | SOP (project risk) | indexed |
| AIAA standards program | Standards (normative) / Recommended Practices / Guides; S-series (with AIA/ASD) for integrated product support | AIAA | aero/def | Aerospace engineering and product-support standards, tiered by strength of obligation | Paid | ASTRO7EX | [arc.aiaa.org](https://arc.aiaa.org/action/showPublications?pubType=standards) (403 direct; confirmed via search) |
| Print Technologies (APTech/CGATS/B65) | CGATS: metrology, color characterization, workflow, data exchange; B65: press/bindery/finishing safety | APTech | img | US print-industry standards + secretariat to ISO/TC 130 and ICC | Not stated on page | BLACK (design system / print production) | [printtechnologies.org/standards](https://printtechnologies.org/standards/) |
| CTA standards | CTA-#### across A/V, wireless power, digital health, cybersecurity, accessibility, smart home | CTA | contech | Consumer electronics interoperability/performance | Mixed (some member-only) | OPERATOR (tooling on the box) | [cta.tech/resources/?type=standard](https://www.cta.tech/resources/?type=standard) |
| NASA NODIS directives | NPD/NPR, ~266 current | NASA | def | Agency policy and procedural requirements | Free | OPERATOR (directive-tiering model for SOP) | [nodis3.gsfc.nasa.gov](https://nodis3.gsfc.nasa.gov/Rpt_current_directives.cfm) |
| ASQ standards overview | ISO 9000 family explainer (9000/9001/9004/19011) | ASQ | qual | Plain-language guide to the QMS family, not the standards text itself | Free (overview only; standards text is paid) | SOP | confirmed via search |
| DLA Defense Standardization Program | MIL-STD/MIL-HDBK/MIL-SPEC(DTL)/MIL-PRF via ASSIST | DLA | def | DoD's standardization management and document catalog | Free (ASSIST) | WARROOM (already anchored on MIL-STD-1472) | confirmed via search |
| ESTA TSP published docs | ANSI E1.1–E1.72+ | ESTA | enttech | Entertainment-technology (lighting, rigging, stage machinery, event safety) | **Free** | WARROOM (lighting/rigging parallels long-watch UI) | [tsp.esta.org](https://tsp.esta.org/tsp/documents/published_docs.php) |
| IS&T / ISO TC42 | 200+ photography standards (via ISO) | ISO TC42 / IS&T | img | Photography and imaging science standards committee | Paid (ISO/ANSI purchase) | BLACK (BVX-LEARN catalog) | confirmed via search |
| PMI standards | PMBOK Guide (8th ed.) + Practice Guides + global standards | PMI | pm | Project/program/portfolio management body of knowledge | Free overview; full text needs membership/purchase | SOP · project flow | [pmi.org/standards](https://www.pmi.org/standards) |
| IEC technical committees | TC-organized catalog across all IEC standards | IEC | mixed | Electrotechnical standards by committee, not by tier | Paid | OPERATOR (reference) | confirmed via search (direct fetch 403/404) |
| NATO NSO standards | STANAG/AP list | NATO | def | Alliance interoperability agreements | Public list; most linked docs gate | WARROOM (already a neighbor of the WATCH register) | confirmed via search |
| EverySpec | Mirrors MIL-STD/MIL-SPEC/MIL-HDBK plus NASA family (CxP-PUBS, NASA-STD, NASA-HDBK, NPD, NPR, NPG, NRP, NSS, SP, etc.) | Aggregator | def | Free mirror of >55,000 government/military documents | **Free** | WARROOM · OPERATOR | confirmed via search |
| MIL-STD-1472H | DoD Design Criteria Standard: Human Engineering (2020) | DoD | light/human factors | Human-engineering design criteria | Free (ASSIST/EverySpec) | WARROOM (already in-house via WATCH register) | already resolved in-house |
| ASA | Acoustical Society of America (not the old ANSI name) | ASA | mixed | Acoustics/noise/bioacoustics standards (S1 acoustics, S2 shock/vibration, S3 bioacoustics, S12 noise) | Paid | No current house fit — reference only | confirmed via search |

## 3. Gaps the harvest does not cover

- **Dublin Core / schema.org** — the de-facto free metadata vocabularies; the harvest only shows the paid ISO/INCITS wrappers around them, and BVX-LEARN's catalog needs the free base layer first.
- **W3C** (HTML, CSS, WCAG, JSON-LD) — no web-standards body appears at all, despite every house artifact being a web page.
- **WCAG 2.x / 3.0** — accessibility is the single biggest gap for anything published as a page (SITREP, WARROOM, DARKROOM).
- **Unicode / CLDR** — text/character encoding underlies every system in the house; absent from the harvest.
- **ISO 8601** (dates/times) and **ISO 3166** (country/region codes) — small, free, load-bearing standards for any register or database schema the house builds.
- **SMPTE / EBU** — the actual video/broadcast technical standards bodies; APTech/CGATS covers print, not motion.
- **ISO 12647** (print process control) — sits right next to the CGATS/print harvest but wasn't pulled.
- **ISO 690** (bibliographic citation) — relevant the moment BVX-LEARN needs a citation format for its sources.
- **IEEE 830 / ISO/IEC/IEEE 29148** (requirements specification) — sits directly beside the 12207/15288 pair already in the harvest but wasn't included.
- **Dramatica theory / Save the Cat / Fountain (screenplay format)** — the de-facto "standards" for story structure and script markup; the locus explicitly frames story as needing its own standards, but no story-format body appears here.
- **2257 record-keeping / platform content-and-age-verification standards** — the direct regulatory-standard analog for ORANGE; nothing in this harvest touches it.
- **PCI DSS** — if ORANGE or any venture ever takes payment, this is the standard that gates it; adjacent to the X9/27001 material already pulled but not itself present.

## 4. Free sources

- **EverySpec** (everyspec.com) — free mirror of MIL-STD/MIL-SPEC/MIL-HDBK/MIL-PRF plus the full NASA directive family (NPD, NPR, NPG, NASA-STD, NASA-HDBK, CxP-PUBS, center-specific series). Best single free stop for defense and NASA documents.
- **NASA NODIS** (nodis3.gsfc.nasa.gov) — the live, authoritative directive index (266 current); browsable without login, some documents need internal access.
- **DLA ASSIST** (assist.dla.mil) — the official DoD specs-and-standards database; free search and PDF download for most of its 116,970 indexed documents.
- **NATO NSO public site** (nso.nato.int) — lists STANAGs/APs publicly, but most individual document links redirect to a gated access request; treat as an index, not a free-text source.
- **ESTA TSP** (tsp.esta.org) — every published ANSI E1.x entertainment-technology standard is a free PDF download; donation-supported, not paywalled.
- **IES** — confirmed **paid only**; all RP/LM/TM documents sell through store.ies.org, no free tier found despite the initial assumption.
- **ASQ** — free explainer/overview content on the ISO 9000 family, but the standards themselves are not reproduced; still useful as a free primer layer.
