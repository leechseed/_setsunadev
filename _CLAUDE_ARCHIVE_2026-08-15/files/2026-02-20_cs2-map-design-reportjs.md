---
original_path: "/home/claude/cs2_map_design_report.js"
source_conversation: "CS2 map design philosophy overview"
created: 2026-02-20
trunk: ORANGE
kind: generated-file
---

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageBreak, PageNumber, TabStopType
} = require("docx");

const FONT = "Arial";
const PAGE_W = 12240;
const PAGE_H = 15840;
const MARGIN = 1440;
const CONTENT_W = PAGE_W - 2 * MARGIN; // 9360

const border = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 80, bottom: 80, left: 120, right: 120 };

function heading(text, level) {
  return new Paragraph({
    heading: level,
    children: [new TextRun({ text, font: FONT })],
  });
}

function para(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 200, line: 276 },
    ...opts,
    children: [new TextRun({ text, font: FONT, size: 24, ...opts.run })],
  });
}

function multiPara(runs, opts = {}) {
  return new Paragraph({
    spacing: { after: 200, line: 276 },
    ...opts,
    children: runs.map(r =>
      typeof r === "string"
        ? new TextRun({ text: r, font: FONT, size: 24 })
        : new TextRun({ font: FONT, size: 24, ...r })
    ),
  });
}

function bulletItem(text, ref = "bullets", level = 0) {
  return new Paragraph({
    numbering: { reference: ref, level },
    spacing: { after: 120, line: 276 },
    children: [new TextRun({ text, font: FONT, size: 24 })],
  });
}

function boldBullet(boldText, normalText, ref = "bullets", level = 0) {
  return new Paragraph({
    numbering: { reference: ref, level },
    spacing: { after: 120, line: 276 },
    children: [
      new TextRun({ text: boldText, font: FONT, size: 24, bold: true }),
      new TextRun({ text: normalText, font: FONT, size: 24 }),
    ],
  });
}

function tableCell(text, opts = {}) {
  return new TableCell({
    borders,
    margins: cellMargins,
    width: opts.width ? { size: opts.width, type: WidthType.DXA } : undefined,
    shading: opts.shading ? { fill: opts.shading, type: ShadingType.CLEAR } : undefined,
    children: [
      new Paragraph({
        children: [new TextRun({ text, font: FONT, size: 22, bold: !!opts.bold })],
      }),
    ],
  });
}

function headerRow(texts, widths, color = "1B3A5C") {
  return new TableRow({
    children: texts.map((t, i) =>
      tableCell(t, { width: widths[i], shading: color, bold: true })
    ),
  });
}

function dataRow(texts, widths) {
  return new TableRow({
    children: texts.map((t, i) => tableCell(t, { width: widths[i] })),
  });
}

function sectionBreak() {
  return new Paragraph({ spacing: { after: 0 }, children: [] });
}

// ─── Document ───

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 24 } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: FONT, color: "1B3A5C" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 },
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: FONT, color: "2E5984" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 },
      },
      {
        id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: FONT, color: "3C6E9E" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 },
      },
    ],
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        },
        {
          level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1440, hanging: 360 } } },
        }],
      },
      {
        reference: "numbers",
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
    ],
  },
  sections: [
    // ─── TITLE PAGE ───
    {
      properties: {
        page: {
          size: { width: PAGE_W, height: PAGE_H },
          margin: { top: 3600, right: MARGIN, bottom: MARGIN, left: MARGIN },
        },
      },
      children: [
        new Paragraph({ spacing: { after: 600 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({ text: "MAP DESIGN IN", font: FONT, size: 28, color: "666666", allCaps: true, characterSpacing: 200 })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ text: "COUNTER-STRIKE 2", font: FONT, size: 64, bold: true, color: "1B3A5C" })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 600 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "E8A735", space: 1 } },
          children: [new TextRun({ text: " ", font: FONT, size: 12 })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({ text: "A Comprehensive Analysis of Level Design Philosophy,\nSpatial Architecture, and Competitive Map Theory", font: FONT, size: 26, color: "444444", italics: true })],
        }),
        new Paragraph({ spacing: { after: 1200 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ text: "February 2026", font: FONT, size: 24, color: "888888" })],
        }),
      ],
    },

    // ─── TABLE OF CONTENTS PAGE ───
    {
      properties: {
        page: {
          size: { width: PAGE_W, height: PAGE_H },
          margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
        },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ text: "Map Design in Counter-Strike 2", font: FONT, size: 18, color: "999999", italics: true })],
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ font: FONT, size: 18, color: "999999", children: [PageNumber.CURRENT] })],
          })],
        }),
      },
      children: [
        heading("Table of Contents", HeadingLevel.HEADING_1),
        para(" "),
        multiPara([{ text: "1.  ", bold: true }, "Executive Summary"]),
        multiPara([{ text: "2.  ", bold: true }, "Historical Context: From GoldSrc to Source 2"]),
        multiPara([{ text: "3.  ", bold: true }, "Core Design Philosophy"]),
        multiPara([{ text: "4.  ", bold: true }, "Spatial Grammar: The Vocabulary of CS2 Maps"]),
        multiPara([{ text: "5.  ", bold: true }, "The Bombsite Paradigm"]),
        multiPara([{ text: "6.  ", bold: true }, "Timing and Flow: The Invisible Architecture"]),
        multiPara([{ text: "7.  ", bold: true }, "Verticality and Elevation Design"]),
        multiPara([{ text: "8.  ", bold: true }, "Visibility, Sightlines, and Lighting"]),
        multiPara([{ text: "9.  ", bold: true }, "Economy of Space: Rotation and Map Control"]),
        multiPara([{ text: "10. ", bold: true }, "Utility Design: Surfaces, Skyboxes, and Physics"]),
        multiPara([{ text: "11. ", bold: true }, "Case Studies: Canonical Maps"]),
        multiPara([{ text: "12. ", bold: true }, "The Source 2 Difference: Technical Evolution"]),
        multiPara([{ text: "13. ", bold: true }, "Community Mapping and the Workshop Ecosystem"]),
        multiPara([{ text: "14. ", bold: true }, "Conclusion: Why CS2 Maps Endure"]),
        new Paragraph({ children: [new PageBreak()] }),

        // ─── 1. EXECUTIVE SUMMARY ───
        heading("1. Executive Summary", HeadingLevel.HEADING_1),
        para("Counter-Strike 2 represents the most refined iteration of competitive map design in the history of first-person shooters. Over two and a half decades, Valve and the Counter-Strike community have developed a design language for multiplayer maps that is as rigorous and internally consistent as any architectural tradition. This report provides a comprehensive analysis of every major dimension of map design in CS2, from high-level philosophy to granular technical implementation."),
        para("CS2 maps are not merely arenas; they are precision instruments designed to produce emergent strategic depth from simple, legible geometry. The genius of Counter-Strike map design lies in its ruthless economy: every corridor, every angle, every timing window exists to create meaningful decisions for both attacking and defending teams. A CS2 map is a system where spatial relationships encode tactical information, and where the geometry itself is the primary game mechanic."),
        para("This document examines the full domain of CS2 level design: the historical lineage from GoldSrc through Source to Source 2, the core design axioms that govern every competitive map, the spatial vocabulary of chokepoints, connectors, and bombsites, the invisible architecture of movement timings, the role of verticality, the design of sightlines, the integration of utility (grenades, smokes, and flashes) as a first-class design consideration, and the technical innovations that Source 2 brings to the craft. Detailed case studies of canonical maps like Dust 2, Mirage, Inferno, Nuke, Overpass, Ancient, and Anubis illustrate these principles in practice."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 2. HISTORICAL CONTEXT ───
        heading("2. Historical Context: From GoldSrc to Source 2", HeadingLevel.HEADING_1),

        heading("2.1 The GoldSrc Era (1999\u20132004)", HeadingLevel.HEADING_2),
        para("Counter-Strike began as a Half-Life mod in 1999, and its earliest maps were created by amateur level designers working within the constraints of the GoldSrc engine. Maps like de_dust (Dave Johnston, 1999) and de_inferno established foundational patterns almost by accident: the two-bombsite defusal format, the concept of chokepoints as resource-contested territory, and the idea that map geometry should force teams to commit to strategies before making contact."),
        para("GoldSrc maps were architecturally simple by necessity. Brush-based geometry, limited texture budgets, and low polygon counts meant that maps had to communicate tactical information through broad spatial relationships rather than fine detail. This constraint proved to be a virtue. Players learned to read maps as abstract tactical diagrams, and the community developed an intuitive understanding of concepts like map control, rotation timings, and trade-kill geometry long before these terms were formalized."),

        heading("2.2 The Source Engine Era (2004\u20132023)", HeadingLevel.HEADING_2),
        para("Counter-Strike: Source and later CS:GO brought significant visual and technical upgrades, but the fundamental map design grammar remained remarkably stable. The Source engine introduced displacement surfaces, improved lighting, better physics, and higher-fidelity geometry, but the competitive map pool continued to favor layouts that honored the spatial principles established in 1.6."),
        para("CS:GO in particular saw the maturation of map design as a discipline. Valve\u2019s iterative rework of maps like Inferno (the 2016 \u201CNewferno\u201D update), Nuke, Dust 2, and Cache demonstrated a design methodology: simplify sightlines, widen chokepoints slightly to reduce defender advantage, improve readability by reducing visual clutter, and ensure that every position has a counter-position. The community mapping scene, led by designers like FMPONE (Cache, Tuscan), Volcano (Overpass, Cache), and the MapCore community, contributed maps that were ultimately adopted into the competitive pool, proving that the design language was legible and reproducible beyond Valve itself."),

        heading("2.3 The Source 2 Transition (2023\u2013Present)", HeadingLevel.HEADING_2),
        para("CS2\u2019s migration to Source 2 preserved existing map layouts while overhauling rendering, lighting, physics, and audio. The most significant changes for map design were the introduction of physically-based rendering (PBR), volumetric lighting, responsive audio that reflects off surfaces dynamically, and a new smoke grenade system where smoke volumes are true 3D objects that interact with geometry and can be parted by gunfire or grenades. These changes did not alter the spatial grammar of maps but profoundly affected how players perceive and interact with space."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 3. CORE DESIGN PHILOSOPHY ───
        heading("3. Core Design Philosophy", HeadingLevel.HEADING_1),
        para("CS2 map design is governed by a set of implicit axioms that have been refined over twenty-five years of competitive play. These principles are rarely articulated formally by Valve, but they are observable in every competitive map that has survived the test of tournament play."),

        heading("3.1 Asymmetric Balance", HeadingLevel.HEADING_2),
        para("Every CS2 defusal map is fundamentally asymmetric: attackers (Terrorists) must move toward a fixed objective, while defenders (Counter-Terrorists) hold positions and react. The map must be balanced not in the sense of geometric symmetry, but in the sense of strategic equity \u2013 both teams must have approximately equal chances of winning a round at the highest level of play, with slight CT-side advantage being the historical norm (typically 52\u201355% CT win rate on well-balanced maps)."),
        para("This asymmetric balance is achieved through careful calibration of timing, information, and positional advantage. CTs arrive at bombsites first and can set up crossfires, but Ts have the advantage of choosing which site to attack and concentrating force. The map must ensure that neither advantage is overwhelming."),

        heading("3.2 Legibility and Clarity", HeadingLevel.HEADING_2),
        para("A CS2 map must be immediately legible. Players should be able to orient themselves within seconds, understand the available routes, and intuit the likely positions of enemies. This is achieved through consistent visual language (warm/cool color coding for T/CT sides of maps), distinctive landmark architecture at key decision points, clean geometry that avoids visual noise, and clear sightlines that reward good crosshair placement."),
        para("Legibility also extends to competitive spectators. A well-designed map should produce gameplay that is comprehensible to observers watching from a broadcast perspective. The spatial logic of the round should be inferable from the minimap alone."),

        heading("3.3 Meaningful Choices at Every Scale", HeadingLevel.HEADING_2),
        para("At the macro level, the T-side must choose which site to attack and which route to take. At the meso level, individual players must decide whether to push, hold, rotate, or lurk. At the micro level, every corner presents a choice of angle, every doorway a decision about timing. A great CS2 map ensures that these choices are real \u2013 that no single option dominates, and that the optimal play depends on reading the opponent\u2019s tendencies."),

        heading("3.4 Controlled Complexity", HeadingLevel.HEADING_2),
        para("CS2 maps operate in a narrow band of complexity. Too simple (a single corridor), and the game becomes mechanically trivial. Too complex (a labyrinth of interconnected rooms), and the game becomes random and unreadable. The ideal CS2 map has a small number of primary routes (typically 3\u20135 major pathways between spawn areas and bombsites), with a moderate number of secondary connectors that allow for flanking and rotation without making every position vulnerable from infinite angles."),
        para("This controlled complexity is what separates CS2 from other tactical shooters. Maps like Valorant\u2019s Bind or Ascent, while clearly influenced by Counter-Strike, tend toward greater simplicity and more explicit gating mechanisms (teleporters, one-way doors). CS2 maps achieve their strategic depth through geometry alone, without mechanical gimmicks."),

        heading("3.5 Iterative Refinement Over Revolution", HeadingLevel.HEADING_2),
        para("Competitive CS2 maps are not designed in a single pass; they are evolved over years of professional play. Dust 2 has been refined continuously since 2001. Inferno was radically reworked in 2016. Mirage\u2019s current form bears only a family resemblance to its original 2012 version. This iterative process is essential: the complexity of emergent gameplay means that design flaws only become apparent after thousands of hours of high-level play, and that small spatial changes (widening a doorway by 16 units, adding a box for cover, opening a skybox for utility) can have profound strategic consequences."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 4. SPATIAL GRAMMAR ───
        heading("4. Spatial Grammar: The Vocabulary of CS2 Maps", HeadingLevel.HEADING_1),
        para("CS2 maps are composed from a finite vocabulary of spatial elements, each of which serves a specific tactical function. Understanding this vocabulary is essential to understanding why maps work."),

        heading("4.1 Chokepoints", HeadingLevel.HEADING_2),
        para("A chokepoint is a narrow passage that attackers must traverse to reach a bombsite. Chokepoints are the primary mechanism through which maps create tactical tension. They force attackers to commit utility (smokes, flashes, molotovs) to gain passage, giving defenders information about the attack and time to rotate. Classic chokepoints include the tunnels on Dust 2 B, Banana on Inferno, and Palace/Ramp on Mirage."),
        para("The width, length, and angles of a chokepoint determine its character. A long, narrow chokepoint like Inferno Banana favors defenders who can hold with rifles at range and utility. A short, wide chokepoint like Dust 2 Long favors attackers who can burst through with speed after a single smoke. The best maps feature chokepoints of varying character to ensure diverse strategic approaches."),

        heading("4.2 Connectors", HeadingLevel.HEADING_2),
        para("Connectors are pathways that link major areas of the map without directly leading to a bombsite. They serve as rotation routes for defenders, lurking paths for attackers, and contested territory that grants map control to whichever team holds them. Mid on Mirage, Connector on Overpass, and Mid on Inferno are canonical examples."),
        para("Good connector design is subtle and critical. A connector must be valuable enough to contest but risky enough that controlling it costs resources. It should offer information about enemy positioning (through sound or sightlines) without being so exposed that it becomes a death trap."),

        heading("4.3 Bombsites", HeadingLevel.HEADING_2),
        para("Bombsites are the terminal objectives of each round. Their design is discussed in detail in Section 5, but at the level of spatial grammar, a bombsite is an open area with multiple entry points, cover positions for both attackers and defenders, and clear lines of sight that create crossfire potential."),

        heading("4.4 Mid", HeadingLevel.HEADING_2),
        para("Nearly every competitive CS2 map features a \u201Cmid\u201D area: a central zone that connects the two major routes to each bombsite. Mid control is the fundamental strategic resource of CS2. The team that controls mid gains information about rotations, the ability to split bombsites, and the flexibility to change plans mid-round. Mid areas are typically contested from the opening seconds of a round, making them the site of the game\u2019s most important early engagements."),

        heading("4.5 Spawn Areas and Approach Routes", HeadingLevel.HEADING_2),
        para("T and CT spawns are the starting positions for each team, and the routes from spawn to key map areas define the timing structure of each round. Spawn positions in CS2 are slightly randomized within a zone, meaning that the fastest player to a given position varies from round to round. This controlled randomness prevents maps from becoming entirely deterministic while still allowing teams to plan strategies around typical timings."),

        heading("4.6 Off-Angles and Novelty Positions", HeadingLevel.HEADING_2),
        para("Off-angles are positions that deviate from the standard holding spots. They exist because map geometry occasionally allows players to stand in unexpected locations \u2013 on top of boxes, in corners of irregular architecture, or in positions that exploit the gap between a player\u2019s expectation and reality. Good map design includes a moderate number of off-angles: enough to reward creativity, but not so many that clearing a site becomes impossibly tedious."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 5. BOMBSITE PARADIGM ───
        heading("5. The Bombsite Paradigm", HeadingLevel.HEADING_1),
        para("The bombsite is the gravitational center of every CS2 round. All strategy orbits the question of which site to attack, how to take it, and how to hold it. Bombsite design is therefore the most consequential element of CS2 map design."),

        heading("5.1 Entry Points and Angles", HeadingLevel.HEADING_2),
        para("Every bombsite must have at least two entry points for attackers, and ideally three or more. A site with only one entry becomes trivially defensible and produces stale gameplay. The relationship between entry points is critical: they should allow attackers to \u201Ctrade\u201D kills (if the first player entering dies, the second player can immediately refrag), create crossfires of their own, and force defenders to divide their attention."),
        para("The angles available within a bombsite determine the depth of post-plant gameplay. A site with many cover positions and angles (like Mirage A site) produces complex retake scenarios. A site that is relatively open (like Dust 2 B site) produces faster, aim-dependent engagements."),

        heading("5.2 The A/B Dynamic", HeadingLevel.HEADING_2),
        para("CS2\u2019s two-site format creates a fundamental information game. Defenders must allocate their five players between two sites without knowing where the attack will come. The standard defensive setup is a 2\u20131\u20132 or 3\u20131\u20131 split (players per site, with mid players floating). Maps must be designed so that both sites are viable attack targets \u2013 if one site is dramatically easier to take, the map collapses into a one-dimensional game."),
        para("The relationship between the two bombsites defines a map\u2019s strategic character. On some maps (Dust 2), the sites are relatively independent, and the game is primarily about executes and retakes. On others (Nuke), the sites are vertically stacked and intimately connected, creating a unique dynamic where utility and sound information flow between floors."),

        heading("5.3 Post-Plant Design", HeadingLevel.HEADING_2),
        para("Once the bomb is planted, the dynamic inverts: attackers become defenders of the bomb, and CTs must retake the site. Map design must account for this phase explicitly. The bomb plant positions, the available cover for post-plant players, the angles from which CTs can approach, and the time required to rotate all combine to determine whether post-plant situations are strategically rich or degenerate."),
        para("The best bombsite designs create interesting post-plant puzzles. Mirage A, for example, allows Ts to plant in several positions, each of which favors different post-plant setups (default plant is defensible from palace and ramp; open plant is defensible from connector and jungle). This multiplicity of viable plant positions is a hallmark of great site design."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 6. TIMING AND FLOW ───
        heading("6. Timing and Flow: The Invisible Architecture", HeadingLevel.HEADING_1),
        para("If geometry is the visible architecture of a CS2 map, timing is its invisible counterpart. The time it takes to travel from any point to any other point defines the strategic structure of the game at a level even more fundamental than the physical layout."),

        heading("6.1 First-Contact Timings", HeadingLevel.HEADING_2),
        para("The most critical timings in CS2 are the moments of first contact: when does the fastest T meet the fastest CT at each chokepoint? These timings determine who \u201Cowns\u201D a position by default. On Dust 2, CTs reach the Long Doors position about 1 second before Ts reach the other side, giving CTs the option to push out for an aggressive peek or hold the angle. On Mirage, Ts reach the B Apartments entrance before CTs can set up a full hold, creating an inherently aggressive B dynamic."),
        para("First-contact timings are calibrated in units as small as fractions of a second. A change of 64 units (about one character width) in spawn position can shift a timing enough to alter the viability of a strategy. This is why spawn randomization matters and why professional teams study specific spawn configurations."),

        heading("6.2 Rotation Timings", HeadingLevel.HEADING_2),
        para("Rotation timing is the time required for a defender to move from one bombsite to the other. This is the fundamental constraint that makes the two-site format work: if rotation were instant, defenders could always stack the attacked site; if rotation took too long, the non-attacked site\u2019s defenders would be irrelevant."),
        para("On a well-designed map, rotation from one site to the other takes approximately 10\u201315 seconds through the fastest route. This means that executing a bombsite take typically gives attackers a narrow window before rotators arrive, making the speed and efficiency of the execute critical. It also means that fake strategies (feinting at one site to draw rotations, then attacking the other) are viable but risky \u2013 the time invested in faking costs the attackers their own rotation time."),

        heading("6.3 The Pace Spectrum", HeadingLevel.HEADING_2),
        para("Different maps create different rhythms of play based on their timing structures. Dust 2 is a fast map: short rotation times, quick first-contact timings, and relatively open geometry produce an aggressive, aim-heavy style. Inferno is a slow map: long chokepoints, deliberate utility usage on Banana, and complex site architecture favor methodical play. Ancient sits in the middle, with medium timings and a balance of open and closed spaces."),
        para("This variation in pace across the map pool is itself a design goal. A healthy competitive ecosystem requires maps that reward different playstyles, and the pace spectrum ensures that teams with different strengths (aim-heavy versus strategic, aggressive versus passive) each have maps that favor them."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 7. VERTICALITY ───
        heading("7. Verticality and Elevation Design", HeadingLevel.HEADING_1),
        para("Counter-Strike has historically been a game of predominantly horizontal combat, but verticality has always played a significant role and has become more prominent in modern map design."),

        heading("7.1 Elevation as Advantage", HeadingLevel.HEADING_2),
        para("In CS2, holding an elevated position confers a significant advantage: the elevated player exposes less of their body when peeking (the \u201Chead glitch\u201D), and opponents must adjust their crosshair upward from the default head-height position. Maps exploit this by creating elevated positions at key strategic points \u2013 the window on Mirage (from CT spawn into mid), the Heaven positions on Nuke, the A site boxes on Dust 2."),
        para("Elevated positions are balanced by two mechanisms: they typically require committing to a fixed position (reducing mobility), and they can be cleared with utility (flashbangs and molotovs are especially effective against elevated players who have limited escape routes). The best elevation designs create positions that are powerful but not invincible."),

        heading("7.2 Multi-Level Maps: The Nuke Paradigm", HeadingLevel.HEADING_2),
        para("Nuke is the only map in the competitive pool with a fully stacked vertical layout, where both bombsites occupy the same footprint on different floors. This creates a unique design challenge: sound propagation between floors becomes a primary information channel, utility can be used to affect players on adjacent floors (molotovs through the floor gaps, smokes that block cross-floor sightlines), and the rotation game becomes three-dimensional."),
        para("Nuke\u2019s vertical design has been both its greatest strength and its greatest challenge. The map has been notoriously CT-sided throughout its history, largely because the vertical layout gives defenders superior information and rotation speed (dropping down is faster than climbing up). Valve\u2019s iterative reworks have addressed this through additions like the T-side outdoor area and the silo drop-down, but the fundamental asymmetry of vertical movement remains a design tension."),

        heading("7.3 Layered Verticality in Standard Maps", HeadingLevel.HEADING_2),
        para("Most maps use what might be called \u201Clayered verticality\u201D: primarily horizontal layouts with specific elevated positions. Overpass is the best example, with its canal system running beneath the main map level and multiple elevated walkways and balconies. Ancient uses cliff faces and temple architecture to create significant elevation changes around both sites. This approach adds depth without the readability challenges of full vertical stacking."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 8. VISIBILITY AND SIGHTLINES ───
        heading("8. Visibility, Sightlines, and Lighting", HeadingLevel.HEADING_1),

        heading("8.1 Sightline Design", HeadingLevel.HEADING_2),
        para("Sightlines are perhaps the single most carefully calibrated element of CS2 map design. A sightline is any unobstructed line between two positions where players can see and shoot each other. The length, width, and number of sightlines at any given position determine the skill ceiling and strategic depth of that area."),
        para("Long sightlines (like Dust 2 A Long or Mirage Mid) reward precise aim and favor AWP (sniper rifle) play. Short sightlines and close-quarter areas (like Inferno Apartments or Ancient B site) favor rifles and shotguns. Maps must balance long and short engagements across different areas to ensure that multiple weapon types are viable and that the game doesn\u2019t collapse into a single dominant playstyle."),
        para("Critically, sightlines must be counterable. Every long angle should have an alternative route that bypasses it, or a smoke lineup that neutralizes it. Every position should be vulnerable from at least two directions. The principle is that no single player should be able to lock down a large area of the map from a single position without counterplay."),

        heading("8.2 The One-Way Sightline Problem", HeadingLevel.HEADING_2),
        para("One-way sightlines \u2013 positions where one player can see another but not vice versa \u2013 are a persistent design challenge. They can arise from elevation differences, from dark textures that hide player models, or from geometric quirks that create pixel-wide gaps. CS2\u2019s improved lighting model has addressed some of these issues (consistent illumination reduces the advantage of hiding in dark corners), but one-way angles remain a concern that level designers must actively audit."),

        heading("8.3 Lighting and Readability in Source 2", HeadingLevel.HEADING_2),
        para("Source 2\u2019s physically-based rendering has fundamentally changed how lighting affects gameplay. In CS:GO, player models were often difficult to see against certain backgrounds, leading to the community term \u201Cpixel walking\u201D and persistent complaints about visibility. CS2 addresses this through more consistent ambient lighting, rim lighting on player models to separate them from backgrounds, and carefully designed surface materials that avoid both extreme brightness and extreme darkness."),
        para("The lighting design of CS2 maps follows a principle of \u201Cgameplay-first illumination\u201D: competitive areas are well-lit and high-contrast, while purely decorative areas can use more atmospheric lighting. This creates a visual hierarchy that subconsciously guides players toward relevant spaces and away from dead zones."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 9. ECONOMY OF SPACE ───
        heading("9. Economy of Space: Rotation and Map Control", HeadingLevel.HEADING_1),

        heading("9.1 Map Control as Resource", HeadingLevel.HEADING_2),
        para("In CS2, territory is not captured in the formal sense (there are no control points or zones to stand in). Map control is established informally, through the threat of violence. If a team has a player holding mid, they \u201Ccontrol\u201D mid in the sense that enemies cannot cross it without risking death. This creates an economy of spatial control: every player allocated to holding a position is a player unavailable for other tasks."),
        para("Good map design ensures that map control is contestable and meaningful. Controlling mid on Mirage provides information about rotations and enables split attacks, but it requires dedicating at least one player to the window position and one to connector. This investment creates a tradeoff: stronger mid control means weaker bombsite holds."),

        heading("9.2 Information Architecture", HeadingLevel.HEADING_2),
        para("Sound design in CS2 is a map design consideration, not merely an audio engineering concern. The material of surfaces (metal grating produces different footstep sounds than concrete), the placement of breakable objects (doors, vents), and the acoustic properties of spaces all contribute to the information available to players. A well-designed map uses sound as a deliberate information channel, creating positions where defenders can hear approaching footsteps at known distances."),
        para("Visual information is equally designed. Windows, vents, and gaps in geometry provide sightlines that may not allow shots but do allow observation. The balcony on Inferno A site, the vent on Mirage B site, and the window on Overpass Connector all serve as information-gathering positions that contribute to the strategic layer without directly enabling kills."),

        heading("9.3 Default Setups and the Opening Book", HeadingLevel.HEADING_2),
        para("Like chess, competitive CS2 has developed an \u201Copening book\u201D of standard defensive setups for each map. These defaults emerge from the map\u2019s geometry and timings: they represent the Nash equilibrium of player positioning given the map\u2019s spatial structure. A well-designed map produces diverse viable defaults, not a single dominant setup. If one setup is clearly optimal, the map becomes stale; if many setups are viable, the game remains strategically fresh even after thousands of hours of play."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 10. UTILITY DESIGN ───
        heading("10. Utility Design: Surfaces, Skyboxes, and Physics", HeadingLevel.HEADING_1),
        para("Grenade utility \u2013 smokes, flashbangs, molotovs, and HE grenades \u2013 is so central to CS2 that maps must be designed with utility usage as a first-class concern. In a real sense, the grenade meta is a design layer that sits on top of the physical map."),

        heading("10.1 Skybox Design", HeadingLevel.HEADING_2),
        para("The skybox determines which grenades can be thrown over buildings and across the map. An open skybox allows for long-range utility throws (cross-map smokes, pop flashes from behind cover), while a clipped skybox restricts utility to direct throws. The evolution of CS map design has generally trended toward more open skyboxes, as the community has discovered that long-range utility lineups add strategic depth without reducing the skill ceiling."),
        para("CS2\u2019s Inferno rework, for example, opened the skybox significantly compared to its CS:GO predecessor, allowing Ts to throw site smokes from outside chokepoints. This change alone shifted the map\u2019s meta by reducing the utility cost of bombsite executes."),

        heading("10.2 Bounce Surfaces and Lineup Culture", HeadingLevel.HEADING_2),
        para("The physical surfaces of a CS2 map are not just visual; they are gameplay surfaces that determine grenade trajectories. Specific walls, ledges, and architectural details serve as alignment points for precise grenade lineups \u2013 pre-calculated trajectories that produce consistent results. The level designer must consider which surfaces will be used as bounce points and ensure that useful lineups are possible but not trivially easy."),
        para("This is one of the most unique aspects of CS map design: the architecture serves a dual purpose as both spatial container and utility toolkit. A seemingly decorative window ledge might exist precisely because it enables a critical smoke lineup. The tension between visual design and utility function is one of the great creative challenges of CS2 level design."),

        heading("10.3 Smoke Geometry in CS2", HeadingLevel.HEADING_2),
        para("CS2\u2019s volumetric smoke system is a genuine paradigm shift for map design. Unlike CS:GO\u2019s flat, circular smoke sprites, CS2 smokes are 3D volumes that conform to geometry, fill rooms realistically, and can be disrupted by HE grenades. This means that level designers must now consider smoke behavior as a three-dimensional concern: a narrow corridor will channel smoke differently than an open area, and a doorway\u2019s exact dimensions determine whether a smoke can fully block it."),
        para("This system has also created new design considerations around the edges of smokes. In CS:GO, the hard edge of a smoke was a known quantity; in CS2, the fuzzy, volumetric edge creates uncertainty that changes how players interact with smoked-off areas. Maps must be designed so that the most important smoke positions produce clean, functional blocks even with this new system."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 11. CASE STUDIES ───
        heading("11. Case Studies: Canonical Maps", HeadingLevel.HEADING_1),

        heading("11.1 Dust 2: The Platonic Ideal", HeadingLevel.HEADING_2),
        para("Dust 2 is the most iconic map in Counter-Strike history and arguably in all of competitive gaming. Its layout is deceptively simple: two parallel lanes (Long and Short) leading to A site, a tunnel system leading to B site, and a mid area connecting everything. This simplicity is its genius."),
        para("Dust 2\u2019s design embodies every core principle of CS map design. Its chokepoints are clean and readable. Its timings are tight, producing fast-paced gameplay. Mid control is critical but contestable. Both bombsites are viable attack targets with distinct characters (A is open and aim-dependent; B is narrow and utility-dependent). The map rewards individual skill while maintaining strategic depth. Its sightlines favor AWP play on Long and Mid, rifle play on Short and B tunnels, and close-quarters combat in tunnels and site interiors."),
        para("After 25 years, Dust 2 remains in the competitive rotation. Its longevity is the strongest possible evidence that its spatial design is close to optimal for the CS format."),

        heading("11.2 Mirage: The Balanced Standard", HeadingLevel.HEADING_2),
        para("Mirage is widely considered the most balanced map in CS2, consistently hovering near 50/50 T-CT win rates at the professional level. Its three-lane structure (A Ramp and Palace, Mid, B Apartments) with a highly contested mid area creates a textbook example of the CS spatial grammar."),
        para("Mirage\u2019s A site is a masterclass in bombsite design. It features five distinct entry points (Ramp, Palace, Connector, CT, and Jungle), multiple elevation levels, and numerous cover positions. Post-plant scenarios on A site are among the most complex in the game, with viable plant positions that favor different defensive setups. B site is deliberately simpler, creating an asymmetry between sites that rewards T-side teams for reading the defense\u2019s resource allocation."),
        para("The window room overlooking mid is one of the most iconic positions in CS. It demonstrates how a single sightline can define a map\u2019s strategic structure: whoever controls the window controls mid, and whoever controls mid has the strategic initiative."),

        heading("11.3 Inferno: The Slow Burn", HeadingLevel.HEADING_2),
        para("Inferno is the map that best demonstrates the importance of chokepoint design. Its Banana approach to B site is the most analyzed chokepoint in competitive CS: a long, curving corridor with multiple intermediate positions, cover elements, and utility-dependent progression. Taking Banana is a multi-step process that requires coordinated smokes, molotovs, and flashes, making Inferno\u2019s B site the most utility-intensive objective in the game."),
        para("The 2016 rework of Inferno is a case study in iterative refinement. Valve widened critical chokepoints (Banana entrance, A site pillars), improved sightlines, and reduced visual clutter while maintaining the map\u2019s essential character. The result was a map that retained its strategic identity while becoming more balanced and readable."),

        heading("11.4 Nuke: Vertical Innovation", HeadingLevel.HEADING_2),
        para("Nuke represents the most ambitious structural experiment in the competitive pool. Its stacked bombsites, indoor/outdoor duality, and multiple vertical pathways create a map that plays unlike any other. Sound information flowing between floors is a primary strategic mechanic; utility that affects both floors simultaneously (smokes and molotovs through gaps) adds a unique dimension."),
        para("Nuke has always been polarizing. Its CT-sided nature, complex layout, and the dominance of the ramp room as a chokepoint make it challenging for casual players and less-experienced teams. But at the highest level, Nuke rewards the most sophisticated team play in the game, making it a perennial favorite of elite teams and a source of some of competitive CS\u2019s most memorable moments."),

        heading("11.5 Overpass: Connector Complexity", HeadingLevel.HEADING_2),
        para("Overpass, designed by Valve\u2019s own team, demonstrates how connector design can be elevated to a primary strategic mechanic. The map\u2019s mid area is not a simple lane but a complex, multi-level space with sightlines into both bombsite approaches. The canal system beneath the map creates a secondary movement layer that adds depth without overwhelming the core layout."),
        para("Overpass\u2019s A site (the park/bank area) is notable for its open, outdoor design and multiple approach angles, while B site is one of the most compact and utility-dependent sites in the pool. This contrast between sites \u2013 one open, one claustrophobic \u2013 is itself a design principle that ensures varied gameplay within a single map."),

        heading("11.6 Ancient and Anubis: Modern Design Philosophy", HeadingLevel.HEADING_2),
        para("Ancient and Anubis represent the most recent additions to the competitive pool and embody the current state of CS2 map design thinking. Ancient features dramatic elevation changes, a heavily contested mid area, and bombsite designs that deliberately create diverse post-plant scenarios. Anubis, with its canal and temple architecture, introduces novel spatial patterns (the mid water area, the A site\u2019s multi-level temple) while maintaining the fundamental CS grammar."),
        para("Both maps have undergone significant iteration since their introduction, with Valve making ongoing adjustments to balance, timing, and geometry based on professional play data. They demonstrate that the CS map design vocabulary is robust enough to support genuinely new layouts while preserving the strategic depth that defines the format."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 12. SOURCE 2 DIFFERENCE ───
        heading("12. The Source 2 Difference: Technical Evolution", HeadingLevel.HEADING_1),

        heading("12.1 Rendering and Material System", HeadingLevel.HEADING_2),
        para("Source 2\u2019s PBR pipeline produces more realistic and consistent material rendering, which has direct gameplay implications. Metal surfaces reflect light predictably, concrete reads as concrete, and player models are consistently visible against varied backgrounds. The material system also affects grenade physics \u2013 surfaces have defined friction and bounce properties that influence utility trajectories."),

        heading("12.2 Volumetric Lighting and Fog", HeadingLevel.HEADING_2),
        para("CS2 introduces true volumetric lighting: light shafts, atmospheric fog, and dynamic shadows that respond to time of day and environmental conditions. While primarily aesthetic, these systems affect gameplay through visibility: fog can slightly reduce effective sightline distances on outdoor maps, and volumetric light shafts can create momentary visual interference."),

        heading("12.3 Dynamic Audio Propagation", HeadingLevel.HEADING_2),
        para("Perhaps the most gameplay-significant Source 2 improvement is the audio system. Sound now propagates realistically through the environment, bouncing off surfaces and traveling through openings. Players can localize sounds more accurately, and the map\u2019s physical structure directly affects the information available through audio. This makes sound design an even more integral part of level design than before."),

        heading("12.4 The Hammer 2 Editor", HeadingLevel.HEADING_2),
        para("Source 2\u2019s Hammer editor brings significant improvements to the level design workflow: mesh-based geometry (replacing the brush system), real-time lighting preview, integrated material editing, and improved collaboration tools. These tools lower the barrier to entry for community map makers while enabling more complex and detailed environments at the professional level."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 13. COMMUNITY MAPPING ───
        heading("13. Community Mapping and the Workshop Ecosystem", HeadingLevel.HEADING_1),
        para("Counter-Strike\u2019s map design culture is inseparable from its community. Many of the game\u2019s most iconic maps were originally created by community members: Cache (FMPONE/Volcano), Tuscan (cevo_brute, later FMPONE), Season, Santorini, and others. The Steam Workshop provides a distribution platform for community maps, and Valve has historically promoted community maps into the official competitive pool based on tournament adoption and community feedback."),
        para("The community mapping ecosystem serves as both a laboratory for design innovation and a talent pipeline for professional level design. MapCore, the primary community forum for CS level designers, has produced detailed design breakdowns, tutorials, and collaborative feedback threads that constitute a body of practical knowledge about CS map design that exceeds any formal documentation."),
        para("CS2\u2019s Workshop integration continues this tradition, though the transition to Source 2 has required community mappers to learn new tools and workflows. The mapping community\u2019s ability to adapt and continue producing high-quality content is essential to the long-term health of CS2\u2019s competitive ecosystem."),

        new Paragraph({ children: [new PageBreak()] }),

        // ─── 14. CONCLUSION ───
        heading("14. Conclusion: Why CS2 Maps Endure", HeadingLevel.HEADING_1),
        para("CS2 maps endure because they are not designed as stages for action; they are designed as strategic instruments. Every wall, every doorway, every elevation change exists to create a meaningful decision for the player. The design language is minimal but expressive: from a vocabulary of chokepoints, connectors, bombsites, and mid areas, an infinite variety of strategic situations emerge."),
        para("The genius of CS map design is its economy. There are no gimmicks, no mechanics-driven level features, no teleporters or destructible walls or dynamic events. The map is pure geometry, and the depth arises from the interaction of that geometry with the movement, utility, and weapon systems. This purity is why maps like Dust 2 and Inferno have survived for over two decades, and why CS2 remains the gold standard for competitive map design in the FPS genre."),
        para("For designers working in any genre, CS2 maps offer a masterclass in the principle that constraints breed creativity, that legibility is not opposed to depth, and that the best game spaces are those where the architecture itself is the game mechanic. The map is not the arena in which Counter-Strike is played. The map is Counter-Strike."),

        // ─── APPENDIX: MAP POOL OVERVIEW TABLE ───
        new Paragraph({ children: [new PageBreak()] }),
        heading("Appendix: Competitive Map Pool Overview", HeadingLevel.HEADING_1),
        para("The following table summarizes key characteristics of the CS2 competitive map pool as of early 2026."),

        new Table({
          width: { size: CONTENT_W, type: WidthType.DXA },
          columnWidths: [1300, 1200, 1800, 1800, 1600, 1660],
          rows: [
            new TableRow({
              children: [
                tableCell("Map", { width: 1300, shading: "1B3A5C", bold: true }),
                tableCell("Era", { width: 1200, shading: "1B3A5C", bold: true }),
                tableCell("Pace", { width: 1800, shading: "1B3A5C", bold: true }),
                tableCell("Key Feature", { width: 1800, shading: "1B3A5C", bold: true }),
                tableCell("Verticality", { width: 1600, shading: "1B3A5C", bold: true }),
                tableCell("T/CT Lean", { width: 1660, shading: "1B3A5C", bold: true }),
              ],
            }),
            dataRow(["Dust 2", "2001", "Fast", "Pure aim duels", "Minimal", "Balanced"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Mirage", "2012", "Medium", "Mid control", "Low", "Balanced"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Inferno", "2001", "Slow", "Utility-heavy", "Low", "Slight CT"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Nuke", "2000", "Fast", "Vertical stacking", "Extreme", "CT-sided"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Overpass", "2013", "Medium", "Connectors", "Moderate", "Slight CT"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Ancient", "2021", "Medium", "Elevation play", "High", "Slight CT"], [1300, 1200, 1800, 1800, 1600, 1660]),
            dataRow(["Anubis", "2022", "Medium", "Water/temple", "Moderate", "Balanced"], [1300, 1200, 1800, 1800, 1600, 1660]),
          ],
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/home/claude/cs2_map_design_report.docx", buffer);
  console.log("Done.");
});
