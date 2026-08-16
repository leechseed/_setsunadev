---
original_path: "/home/claude/build_plan.js"
source_conversation: "3D printing business models and market entry"
created: 2026-02-12
trunk: BLACK
kind: generated-file
---

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, PageBreak,
  TableOfContents
} = require("docx");

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0 };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
const cellMargins = { top: 80, bottom: 80, left: 120, right: 120 };

const BRAND = "PHANTOM TRACKERS"; // placeholder brand name

function heading(text, level = HeadingLevel.HEADING_1) {
  return new Paragraph({ heading: level, children: [new TextRun(text)] });
}

function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 160 },
    ...opts.pOpts,
    children: [new TextRun({ size: 22, font: "Arial", ...opts, text })],
  });
}

function bold(text, opts = {}) {
  return new TextRun({ size: 22, font: "Arial", bold: true, ...opts, text });
}

function normal(text, opts = {}) {
  return new TextRun({ size: 22, font: "Arial", ...opts, text });
}

function multiRun(runs, pOpts = {}) {
  return new Paragraph({
    spacing: { after: 160 },
    ...pOpts,
    children: runs,
  });
}

function tableHeader(text) {
  return new Paragraph({
    children: [new TextRun({ size: 20, font: "Arial", bold: true, color: "FFFFFF", text })],
  });
}

function tableCell(text, opts = {}) {
  return new Paragraph({
    children: [new TextRun({ size: 20, font: "Arial", ...opts, text })],
  });
}

function makeTable(headers, rows, colWidths) {
  const totalWidth = colWidths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: totalWidth, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [
      new TableRow({
        children: headers.map((h, i) =>
          new TableCell({
            borders,
            width: { size: colWidths[i], type: WidthType.DXA },
            shading: { fill: "1A1A2E", type: ShadingType.CLEAR },
            margins: cellMargins,
            children: [tableHeader(h)],
          })
        ),
      }),
      ...rows.map((row, ri) =>
        new TableRow({
          children: row.map((cell, ci) =>
            new TableCell({
              borders,
              width: { size: colWidths[ci], type: WidthType.DXA },
              shading: { fill: ri % 2 === 0 ? "F8F8FA" : "FFFFFF", type: ShadingType.CLEAR },
              margins: cellMargins,
              children: [tableCell(typeof cell === "string" ? cell : cell.text, cell.opts || {})],
            })
          ),
        })
      ),
    ],
  });
}

// ============================================================
// DOCUMENT BUILD
// ============================================================

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: "1A1A2E" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 },
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "2D2D44" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 },
      },
      {
        id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "444466" },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 },
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
        }],
      },
      {
        reference: "numbers",
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "numbersB",
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsB",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsC",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsD",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsE",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsF",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsG",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsH",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
      {
        reference: "bulletsPhases",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } },
        }],
      },
    ],
  },
  sections: [
    // ========================
    // TITLE PAGE
    // ========================
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      children: [
        new Paragraph({ spacing: { before: 3600 } }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({ size: 56, bold: true, font: "Arial", color: "1A1A2E", text: "[YOUR BRAND]" })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ size: 28, font: "Arial", color: "666688", text: "BOUTIQUE FBT TRACKER SYSTEM" })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 600 },
          children: [new TextRun({ size: 22, font: "Arial", color: "888888", text: "Product Specification & Business Plan" })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ size: 22, font: "Arial", color: "AAAAAA", text: "Prepared February 2026" })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({ size: 20, font: "Arial", color: "BBBBBB", text: "CONFIDENTIAL \u2014 FOR INTERNAL PLANNING USE" })],
        }),
        new Paragraph({
          children: [new PageBreak()],
        }),
      ],
    },
    // ========================
    // TOC + MAIN BODY
    // ========================
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [new TextRun({ size: 16, font: "Arial", color: "999999", text: "[YOUR BRAND] \u2014 Product & Business Plan" })],
          })],
        }),
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ size: 16, font: "Arial", color: "999999", text: "Page " }), new TextRun({ size: 16, font: "Arial", color: "999999", children: [PageNumber.CURRENT] })],
          })],
        }),
      },
      children: [
        heading("Table of Contents"),
        new TableOfContents("Table of Contents", {
          hyperlink: true,
          headingStyleRange: "1-3",
        }),
        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 1. EXECUTIVE SUMMARY
        // ============================================================
        heading("1. Executive Summary"),
        multiRun([
          normal("This document outlines the product specification, business model, and launch strategy for a "),
          bold("boutique, premium-tier SlimeVR-compatible full-body tracking system"),
          normal(" targeting hardcore VR enthusiasts, competitive VRChat dancers, content creators, VTubers, and motion capture professionals."),
        ]),
        multiRun([
          normal("Unlike commodity third-party sellers competing on price, this product line is positioned as the "),
          bold("highest-quality third-party FBT system available"),
          normal(" \u2014 differentiated by swappable 18650 batteries for unlimited session length, per-tracker OLED status displays, comfort-engineered enclosures, premium silicone-backed straps, rigorous quality control, and dedicated support with a real warranty."),
        ]),
        multiRun([
          normal("The business operates on a "),
          bold("limited-batch drop model"),
          normal(" inspired by Massdrop/Drop and the mechanical keyboard community. Each batch is a defined production run with a fixed number of units, sold via preorder. Each subsequent batch incorporates customer feedback and incremental improvements. This creates scarcity, community engagement, and sustainable cash flow \u2014 you only manufacture what\u2019s already sold."),
        ]),

        // ============================================================
        // 2. MARKET POSITIONING
        // ============================================================
        heading("2. Market Positioning"),
        heading("2.1 The Competitive Landscape", HeadingLevel.HEADING_2),
        makeTable(
          ["Competitor", "Price (8-10 tracker)", "Battery", "Display", "Straps", "Warranty", "Wait Time"],
          [
            ["Official SlimeVR v1.2", "$280\u2013$399", "1350mAh LiPo (20hr)", "None", "Elastic w/ velcro", "2 years", "1\u20136 months"],
            ["SlimeVR Butterfly", "$279\u2013$449+", "Built-in (days)", "None", "Clip-on", "2 years", "Ships Aug 2026+"],
            ["VyroVR (Etsy)", "$200\u2013$300", "LiPo (10\u201315hr)", "None", "Silicone-backed", "Limited", "1\u20132 weeks"],
            ["UsagiVR (Etsy)", "$150\u2013$250", "LiPo (8\u201312hr)", "None", "Cheap elastic", "None (all sales final)", "1\u20132 weeks"],
            ["Generic Etsy/eBay", "$120\u2013$200", "LiPo (6\u201312hr)", "None", "Garbage tier", "None", "Varies"],
            [{ text: "[YOUR BRAND]", opts: { bold: true, color: "1A1A2E" } }, { text: "$399\u2013$549", opts: { bold: true, color: "1A1A2E" } }, { text: "18650 hot-swap (30hr+)", opts: { bold: true } }, { text: "OLED per tracker", opts: { bold: true } }, { text: "Premium system", opts: { bold: true } }, { text: "90-day full", opts: { bold: true } }, { text: "Batch drops", opts: { bold: true } }],
          ],
          [1600, 1200, 1500, 1000, 1200, 1100, 1160]
        ),

        new Paragraph({ spacing: { after: 200 } }),
        heading("2.2 Target Customer Profiles", HeadingLevel.HEADING_2),
        multiRun([
          bold("The Marathon Dancer: "),
          normal("VRChat dancer/performer who sessions 6\u201312+ hours. Current trackers die mid-session. Hot-swap 18650s solve this permanently. Will pay premium for zero downtime."),
        ]),
        multiRun([
          bold("The Content Creator: "),
          normal("Streamer, TikToker, or YouTuber producing VR content. Needs reliable, photogenic gear. The OLED display and premium build quality become content in themselves. Unboxing videos drive organic marketing."),
        ]),
        multiRun([
          bold("The VTuber/MoCap Artist: "),
          normal("Uses FBT professionally for avatar animation or motion capture. Needs maximum uptime, drift-free performance, and the ability to monitor tracker status at a glance without alt-tabbing to the SlimeVR dashboard."),
        ]),
        multiRun([
          bold("The Collector/Enthusiast: "),
          normal("The person who buys the best version of everything. Owns a Valve Index, multiple controllers, custom faceplates. Limited batch drops with iterative improvements trigger the same psychology as mechanical keyboard group buys."),
        ]),

        heading("2.3 Why This Price Works", HeadingLevel.HEADING_2),
        multiRun([
          normal("Official SlimeVR starts at $185 for a basic 5-tracker lower-body set and goes up to $399+ for full-body with extensions. The upcoming Butterfly trackers are $279\u2013$449+. Vive trackers cost $130 EACH ($390+ for just three) plus $200+ for base stations. At $399\u2013$549 for a complete 7\u201310 tracker system with features nobody else offers, this product sits "),
          bold("below Vive pricing, above commodity SlimeVR sellers, and alongside official SlimeVR"),
          normal(" \u2014 but with tangible feature advantages that justify the premium."),
        ]),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 3. PRODUCT SPECIFICATION
        // ============================================================
        heading("3. Product Specification"),
        heading("3.1 Core Tracker Hardware", HeadingLevel.HEADING_2),

        makeTable(
          ["Component", "Specification", "Why This Choice"],
          [
            ["MCU", "ESP32-C3 SuperMini", "WiFi 4 (2.4GHz), low power, tiny footprint, SlimeVR firmware compatible, $2\u20133 each"],
            ["IMU", "TDK ICM-45686", "Same IMU as official SlimeVR v1.2. Best-in-class drift performance with open-source VQF fusion"],
            ["Magnetometer", "QMC6309", "Same as official v1.2. Enables magnetic field correction for reduced drift. Most cheap sellers skip this"],
            ["Battery", "18650 Li-Ion (Samsung 30Q or LG HG2)", "3000\u20133500mAh = 30+ hours runtime. Hot-swappable via spring contacts. Name-brand cells only"],
            ["Display", "0.91\" SSD1306 OLED (128x32)", "I2C, ultra-low power draw (~5\u201310mA). Shows battery %, tracker ID, Wi-Fi signal, drift timer, connection status"],
            ["Charging", "TP4056 USB-C module with protection", "Standard USB-C for in-case charging. But primary use is battery swap, not cable charging"],
            ["Switch", "SS12D00G3 slide switch", "Reliable, low-profile, easy to actuate"],
            ["PCB", "Custom PCB (JLCPCB)", "Integrates all components, eliminates hand-wiring, ensures consistent quality across all units"],
          ],
          [1800, 2500, 5060]
        ),

        new Paragraph({ spacing: { after: 200 } }),
        heading("3.2 Enclosure Design Philosophy", HeadingLevel.HEADING_2),
        p("Every design decision serves the hardcore user who wears these trackers for hours at a time. The enclosure is not just a box \u2014 it\u2019s part of the tracking system."),

        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("Comfort-contoured base: "), normal("Slight concave curve on the skin-contact side matches body contours. Thin silicone or EVA foam pad on contact surface prevents pressure points during long sessions.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("Rounded edges everywhere: "), normal("No sharp corners. Generous fillets on all edges. Third-party sellers ship rectangular boxes with 90-degree edges that dig into skin \u2014 this is an easy, meaningful win.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("OLED display window: "), normal("Recessed window with slight tint/contrast bezel so the display is visible at a glance but doesn\u2019t glow distractingly in dark VR rooms.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("18650 battery bay: "), normal("Spring-loaded contacts (positive and negative) in a slide-open or pop-latch compartment. Battery slides in and out in under 5 seconds. Designed to be operable by feel alone \u2014 no need to remove the headset.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("Strap integration: "), normal("Dedicated strap channel or quick-release clip mount \u2014 not just a flat surface with a slot. The strap locks to the case, the case locks to the body.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("Material: "), normal("PETG or ASA filament for impact resistance and slight flex. Not PLA (brittle, warps in heat). Matte finish to resist fingerprints and look premium.")],
        }),
        new Paragraph({
          numbering: { reference: "bullets", level: 0 },
          spacing: { after: 100 },
          children: [bold("Brand identity: "), normal("Embossed logo on the lid. Each tracker has its body-part label (CHEST, L-THIGH, R-ANKLE, etc.) both printed on the case and shown on the OLED at boot.")],
        }),

        heading("3.3 The OLED Display \u2014 Feature Breakdown", HeadingLevel.HEADING_2),
        p("This is the single most visible differentiator. No third-party seller and not even official SlimeVR puts a display on each tracker. This requires a firmware fork, but the SlimeVR firmware is open-source and designed for modification."),
        makeTable(
          ["Display State", "Information Shown", "User Benefit"],
          [
            ["Boot Screen", "Brand logo animation + tracker ID", "Immediately know which tracker you\u2019re holding. Professional first impression."],
            ["Active Tracking", "Battery % bar + hours remaining estimate", "Know exactly when to swap. No guessing, no surprise deaths mid-session."],
            ["Active Tracking", "Wi-Fi signal strength (bars)", "Instantly diagnose connection issues without opening the PC dashboard."],
            ["Active Tracking", "Drift timer (time since last reset)", "Know when a reset is coming due. Proactive, not reactive."],
            ["Low Battery", "Flashing battery icon + \u201cSWAP BATTERY\u201d text", "Unmissable warning. Even visible through peripheral vision in some HMDs."],
            ["Charging (USB-C)", "Charging animation + % fill", "Know when the 18650 is full if charging in-case."],
            ["Sleep/Standby", "Screen off (zero power draw)", "Display auto-sleeps when tracker is idle. No wasted battery."],
            ["Error State", "Error code + description", "Self-diagnosing. User can report exact error to support."],
          ],
          [2200, 3200, 3960]
        ),

        new Paragraph({ spacing: { after: 200 } }),
        heading("3.4 The Strap System", HeadingLevel.HEADING_2),
        p("Straps are the #1 complaint across all third-party SlimeVR sellers. The official SlimeVR docs themselves state that strap slipping is the most common problem. This is where \u201ccreating a system\u201d pays off \u2014 the tracker, strap, and mounting mechanism are designed as one integrated unit."),

        new Paragraph({
          numbering: { reference: "bulletsB", level: 0 },
          spacing: { after: 100 },
          children: [bold("38mm+ silicone-backed elastic: "), normal("Non-slip silicone strips on the inside surface grip skin and clothing. Will not slide during dancing, jumping, or rapid movement.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Quick-release buckle or hook system: "), normal("Not just velcro-on-velcro. A positive locking mechanism that doesn\u2019t loosen over time. Study VyroVR\u2019s quick-release hooks as a starting point and improve.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Body-part specific sizing: "), normal("Ankle straps are shorter and narrower than thigh straps. Chest/waist straps are longer with more adjustment range. Each strap is labeled and color-coded to match its tracker.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Tracker mounting tray: "), normal("3D printed tray/cradle that clips or slides onto the strap. Tracker snaps into tray. Allows quick on/off without removing the strap from your body. This is a VyroVR-inspired feature that works extremely well.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Spare strap included: "), normal("Ship one extra strap per set. Communicates confidence in the product and covers the user if one wears out or they want to experiment with placement.")],
        }),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 4. SET CONFIGURATIONS & PRICING
        // ============================================================
        heading("4. Set Configurations & Pricing"),
        p("All pricing below assumes the batch drop model. Prices include all components, straps, one set of 18650 batteries (installed), printed quick-start card, QR code to setup video, and branded packaging. Spare batteries sold separately as add-ons."),

        makeTable(
          ["Set Name", "Trackers", "Coverage", "Price", "COGS Est.", "Gross Profit"],
          [
            ["Core Set", "7 trackers", "Waist, chest, both thighs, both ankles, one foot", "$399", "$175\u2013$215", "$184\u2013$224"],
            ["Full-Body Set", "10 trackers", "Waist, chest, both thighs, both knees, both ankles, both feet", "$549", "$245\u2013$300", "$249\u2013$304"],
            ["Expansion Pack", "2 trackers", "Elbows, extra points, MoCap extensions", "$120", "$50\u2013$60", "$60\u2013$70"],
          ],
          [1800, 1400, 2400, 1000, 1400, 1360]
        ),

        new Paragraph({ spacing: { after: 200 } }),
        heading("4.1 Add-Ons & Accessories", HeadingLevel.HEADING_2),
        makeTable(
          ["Product", "Description", "Price", "COGS", "Margin"],
          [
            ["18650 Battery 2-Pack", "Samsung 30Q or LG HG2, pre-tested", "$15", "$6\u2013$8", "$7\u2013$9"],
            ["18650 Battery 5-Pack", "Full spare set for Core configuration", "$32", "$15\u2013$20", "$12\u2013$17"],
            ["Replacement Strap (any size)", "Individual strap with mounting tray", "$12", "$3\u2013$5", "$7\u2013$9"],
            ["Complete Strap Set (7-piece)", "All straps for Core Set, labeled + color-coded", "$65", "$20\u2013$30", "$35\u2013$45"],
            ["Charging Tray", "3D printed stand, holds 5\u201310 trackers upright for USB-C charging", "$25", "$5\u2013$8", "$17\u2013$20"],
            ["Dedicated 2.4GHz Router", "GL.iNet GL-SFT1200 Opal, pre-configured for SlimeVR", "$45", "$28\u2013$32", "$13\u2013$17"],
          ],
          [2000, 3000, 800, 1000, 1060]
        ),

        new Paragraph({ spacing: { after: 200 } }),
        heading("4.2 Per-Tracker Cost Breakdown (at Batch Scale)", HeadingLevel.HEADING_2),
        makeTable(
          ["Component", "Unit Cost", "Notes"],
          [
            ["ESP32-C3 SuperMini", "$2.50", "AliExpress bulk (50+ qty)"],
            ["ICM-45686 IMU module", "$8.00", "AliExpress, or direct from TDK distributor"],
            ["QMC6309 magnetometer", "$2.00", "Often bundled on breakout boards"],
            ["0.91\" SSD1306 OLED", "$1.50", "AliExpress I2C module, bulk pricing"],
            ["TP4056 USB-C charge board", "$0.50", "With protection circuit"],
            ["18650 spring contacts", "$0.30", "Battery holder springs, positive + negative"],
            ["Samsung 30Q 18650 cell", "$3.50", "Reputable source only (18650batterystore.com or similar)"],
            ["Slide switch", "$0.15", "SS12D00G3 or equivalent"],
            ["Diodes, resistors, wire", "$0.50", "Battery sense resistor divider, protection diodes"],
            ["Custom PCB (JLCPCB)", "$1.50", "Amortized across batch of 50\u2013100 boards"],
            ["3D printed enclosure", "$1.50", "PETG, ~45min print, includes lid + base + strap tray"],
            ["Silicone-backed strap", "$2.50", "38mm, sourced from strap manufacturer"],
            ["EVA foam comfort pad", "$0.25", "Thin adhesive pad for skin-contact surface"],
            ["Packaging + label + QR card", "$0.80", "Branded kraft box, printed insert, sticker"],
            [{ text: "TOTAL PER TRACKER", opts: { bold: true } }, { text: "$25.50", opts: { bold: true } }, { text: "Add ~$3\u20135 for assembly labor amortization", opts: { bold: true } }],
          ],
          [2800, 1400, 5160]
        ),
        new Paragraph({ spacing: { after: 120 } }),
        p("At $25\u201330 per tracker fully loaded, a 7-tracker Core Set costs approximately $175\u2013$210 to produce. Sold at $399, that\u2019s a gross margin of roughly 47\u201356%. A 10-tracker Full-Body Set costs $250\u2013$300, sold at $549, yielding a gross margin of 45\u201354%. These margins are healthy for a small-batch boutique operation and account for occasional warranty replacements, DOA components, and customer support time."),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 5. THE BATCH DROP MODEL
        // ============================================================
        heading("5. The Batch Drop Model"),
        p("This is the engine of the business. Instead of maintaining perpetual inventory, each production run is a defined event with a fixed quantity, sold primarily through preorder."),

        heading("5.1 How It Works", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Announce the batch: "), normal("\"Batch 03 \u2014 15 Core Sets, 8 Full-Body Sets. Preorders open [date], closes [date] or when sold out.\" Share across TikTok, Discord, X, mailing list.")],
        }),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Collect preorders with deposits or full payment: "), normal("Use Shopify, Square, or even a simple payment link. Full payment preferred \u2014 it funds component procurement for that batch.")],
        }),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Procure components for that batch: "), normal("Order exact quantities needed plus 10\u201315% overage for DOA/defects. No excess inventory sitting unsold.")],
        }),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Build, test, ship: "), normal("Assemble all units. Test every tracker for 30+ minutes. Film build process for content. Ship within stated lead time (2\u20134 weeks from close).")],
        }),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Collect feedback: "), normal("Post-delivery survey. What worked, what to improve. Fold into next batch design.")],
        }),
        new Paragraph({
          numbering: { reference: "numbers", level: 0 },
          spacing: { after: 100 },
          children: [bold("Announce next batch with improvements: "), normal("\"Batch 04 \u2014 now with updated enclosure based on your feedback, improved strap buckle, firmware v1.2.\" The iteration is the marketing.")],
        }),

        heading("5.2 Why This Model Works", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "bulletsC", level: 0 },
          spacing: { after: 100 },
          children: [bold("Zero inventory risk: "), normal("You never build more than what\u2019s sold. Cash flow is positive from day one.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsC", level: 0 },
          spacing: { after: 100 },
          children: [bold("Built-in scarcity: "), normal("Limited quantities create urgency. \"Only 15 Core Sets in Batch 03\" is more compelling than \"always in stock.\" Mechanical keyboard community proved this model drives premium pricing.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsC", level: 0 },
          spacing: { after: 100 },
          children: [bold("Community engagement: "), normal("Customers who buy Batch 01 feel ownership in the product. They give feedback that shapes Batch 02. They become evangelists. This is exactly how Massdrop built a $40M+ business.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsC", level: 0 },
          spacing: { after: 100 },
          children: [bold("Incremental improvement: "), normal("No pressure to launch with a perfect product. Batch 01 is great. Batch 02 is better. Batch 05 is extraordinary. Each batch tells a story.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsC", level: 0 },
          spacing: { after: 100 },
          children: [bold("Content goldmine: "), normal("Every batch is a content event. Announce video, build process video, shipping video, unboxing reactions, \"what changed in Batch 03\" video. Perpetual content cycle.")],
        }),

        heading("5.3 Batch Scaling Roadmap", HeadingLevel.HEADING_2),
        makeTable(
          ["Batch", "Timeline", "Quantity", "Focus", "Price"],
          [
            ["Batch 01 (Beta)", "Month 1\u20132", "5\u20138 sets (Core only)", "Validate product, gather feedback, build initial content library. Sell to engaged Discord/community members at slight discount.", "$349"],
            ["Batch 02", "Month 3\u20134", "10\u201315 sets (Core + Full-Body)", "Incorporate Batch 01 feedback. Refine enclosure, strap system. Full price launch.", "$399 / $549"],
            ["Batch 03", "Month 5\u20136", "15\u201325 sets", "Firmware improvements (OLED features expanded). Add-ons available. Growing TikTok/content presence drives demand.", "$399 / $549"],
            ["Batch 04+", "Month 7+", "25\u201340+ sets", "Custom PCBs fully dialed. Component costs dropping with larger orders. Consider expanding to Etsy/Shopify storefront with batch drops still limited.", "$399\u2013$549"],
          ],
          [1400, 1200, 1600, 3600, 1560]
        ),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 6. FINANCIAL MODEL
        // ============================================================
        heading("6. Financial Model"),
        heading("6.1 Batch 01 (Beta) \u2014 Proof of Concept", HeadingLevel.HEADING_2),
        makeTable(
          ["Line Item", "Calculation", "Amount"],
          [
            ["Revenue (5 Core Sets @ $349)", "5 x $349", "$1,745"],
            ["Revenue (add-on batteries, 3 packs)", "3 x $32", "$96"],
            ["Total Revenue", "", { text: "$1,841", opts: { bold: true } }],
            ["COGS \u2014 Tracker components (35 trackers)", "35 x $25.50", "$892"],
            ["COGS \u2014 Packaging & shipping materials", "5 sets", "$75"],
            ["COGS \u2014 Add-on battery packs", "3 x $18", "$54"],
            ["Shipping (USPS Priority, domestic)", "5 x $15 avg", "$75"],
            ["Total COGS", "", { text: "$1,096", opts: { bold: true } }],
            [{ text: "Gross Profit (Batch 01)", opts: { bold: true } }, "", { text: "$745", opts: { bold: true, color: "228B22" } }],
            [{ text: "Gross Margin", opts: { bold: true } }, "", { text: "40.5%", opts: { bold: true, color: "228B22" } }],
          ],
          [3500, 2500, 3360]
        ),
        new Paragraph({ spacing: { after: 120 } }),
        p("Note: Batch 01 is priced $50 below standard to reward early adopters and compensate for beta-level iteration. Gross margin is intentionally lower. Starting from Batch 02, standard pricing applies and margin improves to 47\u201356%."),

        heading("6.2 Batch 03 (Scaled) \u2014 Projected Steady State", HeadingLevel.HEADING_2),
        makeTable(
          ["Line Item", "Calculation", "Amount"],
          [
            ["Revenue (10 Core Sets @ $399)", "10 x $399", "$3,990"],
            ["Revenue (8 Full-Body Sets @ $549)", "8 x $549", "$4,392"],
            ["Revenue (add-ons: batteries, straps, trays)", "Estimated", "$480"],
            ["Total Revenue", "", { text: "$8,862", opts: { bold: true } }],
            ["COGS \u2014 Tracker components (150 trackers)", "150 x $23 (bulk pricing)", "$3,450"],
            ["COGS \u2014 Packaging & shipping", "18 sets", "$270"],
            ["COGS \u2014 Add-on COGS", "Estimated", "$180"],
            ["Shipping", "18 x $15", "$270"],
            ["Total COGS", "", { text: "$4,170", opts: { bold: true } }],
            [{ text: "Gross Profit (Batch 03)", opts: { bold: true } }, "", { text: "$4,692", opts: { bold: true, color: "228B22" } }],
            [{ text: "Gross Margin", opts: { bold: true } }, "", { text: "52.9%", opts: { bold: true, color: "228B22" } }],
          ],
          [3500, 2500, 3360]
        ),
        new Paragraph({ spacing: { after: 120 } }),
        p("At batch scale, per-tracker component cost drops to ~$23 with bulk AliExpress/JLCPCB pricing. If producing 18+ sets per batch on a monthly cadence, annualized gross profit reaches approximately $56,000\u2013$60,000 before operating expenses (marketing spend, tools/equipment replacement, your time). This is side-business income that can scale further."),

        heading("6.3 Startup Investment", HeadingLevel.HEADING_2),
        makeTable(
          ["Category", "Items", "Cost"],
          [
            ["3D Printers", "Bambu Lab A1 or P1S (primary) + Creality Ender 3 V3 (backup)", "$500\u2013$720"],
            ["Soldering & Assembly", "Pinecil/FNIRSI iron, multimeter, flux, tweezers, helping hands, PCB holder", "$80\u2013$120"],
            ["Batch 01 Components", "35 trackers worth of parts + 15% overage", "$1,000\u2013$1,200"],
            ["Custom PCBs (first run)", "50\u2013100 boards from JLCPCB", "$75\u2013$150"],
            ["Firmware Development", "ESP32 + OLED dev kit for firmware prototyping", "$30\u2013$50"],
            ["Marketing/Branding", "Logo, lightbox, packaging materials, Canva Pro", "$150\u2013$250"],
            ["Contingency", "10% buffer for unexpected costs", "$180\u2013$250"],
            [{ text: "TOTAL STARTUP", opts: { bold: true } }, "", { text: "$2,015\u2013$2,740", opts: { bold: true } }],
          ],
          [2500, 4000, 2860]
        ),
        new Paragraph({ spacing: { after: 120 } }),
        p("Batch 01 revenue ($1,745\u2013$1,841) nearly recovers the entire startup investment. By the end of Batch 02, the business is fully self-funding and profitable."),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 7. FIRMWARE DEVELOPMENT PLAN
        // ============================================================
        heading("7. Firmware Development Plan"),
        p("The OLED display requires modifications to the open-source SlimeVR firmware. This is the most technically complex part of the product and should be prototyped first, before committing to batch production."),

        heading("7.1 Technical Architecture", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "bulletsD", level: 0 },
          spacing: { after: 100 },
          children: [bold("I2C bus sharing: "), normal("The ICM-45686 IMU and SSD1306 OLED both use I2C. The ESP32-C3 supports one I2C bus. Both devices can coexist at different addresses (IMU typically 0x68/0x69, OLED at 0x3C). Key concern: display refresh must not block IMU polling. Solution: update display asynchronously at a low refresh rate (1\u20132 Hz) using a non-blocking timer, while IMU polls at full speed (100\u2013200Hz).")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsD", level: 0 },
          spacing: { after: 100 },
          children: [bold("Battery voltage reading: "), normal("Use a resistor voltage divider on an ADC pin to read 18650 voltage (4.2V full \u2192 3.0V empty). Map voltage to percentage using a LiPo discharge curve lookup table. Display on OLED as both percentage and a graphical bar.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsD", level: 0 },
          spacing: { after: 100 },
          children: [bold("Display library: "), normal("Use u8g2 (lighter weight than Adafruit GFX) for the SSD1306. Pre-render display buffers to minimize I2C bus time.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsD", level: 0 },
          spacing: { after: 100 },
          children: [bold("Tracker ID system: "), normal("Each tracker\u2019s body-part assignment stored in EEPROM/NVS. Set during manufacturing/provisioning. Displayed on OLED at boot and in active mode.")],
        }),

        heading("7.2 Development Phases", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "numbersB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Phase A \u2014 Prototype (Week 1\u20132): "), normal("Build one tracker with ESP32-C3 + ICM-45686 + SSD1306 on a breadboard. Verify I2C coexistence. Verify tracking quality is not degraded by display. This is the GO/NO-GO gate.")],
        }),
        new Paragraph({
          numbering: { reference: "numbersB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Phase B \u2014 Firmware Fork (Week 2\u20134): "), normal("Fork SlimeVR firmware. Add display driver module. Implement battery voltage reading. Implement boot screen, active tracking screen, low battery warning.")],
        }),
        new Paragraph({
          numbering: { reference: "numbersB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Phase C \u2014 Integration Testing (Week 4\u20135): "), normal("Build 3 complete trackers on custom PCBs. Run all 3 simultaneously for 8+ hours. Monitor for drift, Wi-Fi stability, display artifacts, battery accuracy. Compare drift performance to tracker without display.")],
        }),
        new Paragraph({
          numbering: { reference: "numbersB", level: 0 },
          spacing: { after: 100 },
          children: [bold("Phase D \u2014 Production Firmware (Week 5\u20136): "), normal("Finalize firmware. Create flashing script/tool for batch provisioning (flash firmware + set tracker ID in one step). Document firmware build process.")],
        }),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 8. QUALITY CONTROL PROTOCOL
        // ============================================================
        heading("8. Quality Control Protocol"),
        p("Every tracker ships only after passing this QC checklist. This is what separates a product from a project. Film the QC process \u2014 it\u2019s powerful content that builds trust."),

        makeTable(
          ["Test", "Criteria", "Fail Action"],
          [
            ["Visual Inspection", "No print artifacts, clean solder joints, proper component alignment, strap mechanism functional", "Rework or reject enclosure/board"],
            ["Power-On Test", "Tracker boots, OLED displays brand logo + tracker ID within 3 seconds", "Debug firmware/connections"],
            ["Wi-Fi Connection", "Connects to test router within 10 seconds, maintains stable connection", "Check antenna, re-flash firmware"],
            ["IMU Drift Test (30 min)", "Place tracker flat on desk. After 30 minutes, drift < 5 degrees. Ideally < 2 degrees.", "Recalibrate magnetometer. If persistent, replace IMU."],
            ["Battery Voltage Accuracy", "OLED battery reading within 5% of multimeter reading", "Adjust voltage divider resistors or calibration offset"],
            ["18650 Swap Test", "Battery slides in/out smoothly, spring contacts make firm connection, no intermittent power", "Adjust spring tension, widen battery bay if needed"],
            ["Full Session Test (1 per batch)", "One randomly selected tracker worn for 2+ hours of active movement. Verify no drift spikes, no disconnects.", "Investigate and fix root cause before shipping batch"],
            ["Packaging Check", "Correct tracker ID label, all accessories present, quick-start card included, QR code scannable", "Repack"],
          ],
          [2200, 3800, 3360]
        ),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 9. MARKETING & CONTENT STRATEGY
        // ============================================================
        heading("9. Marketing & Content Strategy"),
        p("Your video production skills are the moat. Nobody in this space is producing content at a professional level. This is where you outwork every competitor."),

        heading("9.1 Content Pillars", HeadingLevel.HEADING_2),

        multiRun([bold("Pillar 1 \u2014 The Build (Factory Floor): "), normal("Film every batch from component delivery through assembly, testing, and packaging. Soldering close-ups with satisfying audio. The OLED lighting up for the first time. Trackers lined up in the charging tray. This is your \u201coddly satisfying meets tech\u201d content. It builds trust \u2014 customers see exactly what they\u2019re buying.")]),
        multiRun([bold("Pillar 2 \u2014 The Before/After: "), normal("Split screen: VRChat with no FBT (stiff avatar, floating legs) vs. with your trackers (fluid, natural, expressive). This is the most powerful sell in the entire FBT market and almost nobody produces it at high quality.")]),
        multiRun([bold("Pillar 3 \u2014 The Drop Event: "), normal("Each batch announcement is a content event. Teaser video (\"Batch 03 is coming\u2026 here\u2019s what changed\"). Launch video. Sold-out announcement. Customer unboxing reactions. This creates FOMO and community momentum.")]),
        multiRun([bold("Pillar 4 \u2014 Education That Builds Authority: "), normal("\"SlimeVR vs Vive Trackers \u2014 honest comparison.\" \"How to set up FBT on Quest 3.\" \"Why most cheap SlimeVR sellers suck (and what I do differently).\" These videos rank in search and position you as the expert. After watching 3 of your videos, a potential customer already trusts you.")]),
        multiRun([bold("Pillar 5 \u2014 Community & Collaboration: "), normal("Send a free set to a VRChat dancer or content creator with 10k\u201350k followers. The cost ($175\u2013$300 in COGS) returns more value than months of Etsy ads. Their content featuring your trackers reaches exactly your target audience.")]),

        heading("9.2 Platform Strategy", HeadingLevel.HEADING_2),
        makeTable(
          ["Platform", "Content Type", "Frequency", "Purpose"],
          [
            ["TikTok", "Build process, before/after, drop teasers, education", "4\u20135x/week", "Discovery engine. Reach new audience. Viral potential."],
            ["YouTube Shorts", "Repurpose every TikTok", "4\u20135x/week", "Search discoverability. Longer shelf life than TikTok."],
            ["YouTube (long-form)", "Detailed reviews, setup guides, batch retrospectives", "2x/month", "SEO. Authority building. Deep product showcase."],
            ["SlimeVR Discord", "Active community member, marketplace listings, support", "Daily", "First sales channel. Credibility. Direct feedback."],
            ["X (Twitter)", "Drop announcements, community engagement, WIP shots", "3\u20134x/week", "SlimeVR community is active here. Conversation."],
            ["Instagram", "Product photography grid, Reels (repurposed TikToks)", "3x/week", "Visual portfolio. Professional brand presence."],
            ["Mailing List / Discord Server", "Batch announcements, early access, feedback surveys", "Per batch", "Owned audience. Not algorithm-dependent."],
          ],
          [1600, 2800, 1200, 3760]
        ),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 10. SUPPORT & WARRANTY
        // ============================================================
        heading("10. Support & Warranty"),
        p("This is where you destroy the competition by simply being a reasonable human. The bar is underground."),

        heading("10.1 Warranty Policy", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "bulletsE", level: 0 },
          spacing: { after: 100 },
          children: [bold("90-day full warranty: "), normal("Any tracker that develops excessive drift (>15 degrees in 20 minutes), fails to connect reliably, or has a hardware defect is replaced free of charge. You ship replacement, customer ships back defective unit.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsE", level: 0 },
          spacing: { after: 100 },
          children: [bold("Lifetime repair service: "), normal("Beyond 90 days, you offer repair at cost of components only ($10\u201320 + return shipping). This costs you almost nothing and builds extraordinary loyalty.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsE", level: 0 },
          spacing: { after: 100 },
          children: [bold("No hostile language: "), normal("Your warranty page does not threaten customers with chargeback disputes. It does not say \"all sales final.\" It says: \"We stand behind what we build. If something\u2019s wrong, we\u2019ll make it right.\"")],
        }),

        heading("10.2 Support Channels", HeadingLevel.HEADING_2),
        new Paragraph({
          numbering: { reference: "bulletsF", level: 0 },
          spacing: { after: 100 },
          children: [bold("Your own Discord server or channel: "), normal("Dedicated support channel. You answer personally. Response time target: <24 hours, ideally same day.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsF", level: 0 },
          spacing: { after: 100 },
          children: [bold("Setup video specific to YOUR trackers: "), normal("Not a generic SlimeVR tutorial. A video that says: \"Take the tracker labeled CHEST, attach the long strap like this, open the app, pair like this.\" QR code on the printed card links directly to this video.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsF", level: 0 },
          spacing: { after: 100 },
          children: [bold("Firmware update channel: "), normal("As you improve the firmware between batches, existing customers can flash updates. Communicate updates through Discord/mailing list.")],
        }),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 11. LAUNCH TIMELINE
        // ============================================================
        heading("11. Launch Timeline"),

        makeTable(
          ["Week", "Milestone", "Deliverables"],
          [
            ["1\u20132", "Firmware Prototype", "Build 1 tracker on breadboard with ESP32-C3 + ICM-45686 + SSD1306. Verify I2C coexistence and tracking quality. GO/NO-GO decision on OLED feature."],
            ["2\u20133", "Enclosure Design", "CAD model for 18650 case with battery bay, OLED window, strap mount. First test prints. Iterate fit and comfort."],
            ["3\u20134", "Firmware Fork", "Fork SlimeVR firmware. Implement display driver, battery reading, boot screen, active screen, low battery warning."],
            ["4\u20135", "PCB Design", "Design custom carrier PCB in KiCad. Order first run from JLCPCB (50 boards, ~$75\u2013100)."],
            ["5\u20136", "Integration Build", "Build 3\u20135 complete trackers on custom PCBs in final enclosures. Full testing protocol. Wear-test for comfort."],
            ["6\u20137", "Content Production", "Film entire build process. Create 8\u201310 TikToks. Product photography. Setup video. Etsy/Shopify listing."],
            ["7\u20138", "Batch 01 (Beta) Drop", "Announce on Discord, TikTok, X. Open preorders for 5\u20138 Core Sets at $349. Close preorders after 1 week or when sold."],
            ["8\u201310", "Build & Ship Batch 01", "Assemble all sets. Run full QC protocol. Ship. Collect feedback."],
            ["10\u201312", "Batch 02 Prep", "Incorporate feedback. Refine enclosure/firmware. Order components for Batch 02 (10\u201315 sets). Announce drop."],
          ],
          [800, 1800, 6760]
        ),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 12. RISK REGISTER
        // ============================================================
        heading("12. Risk Register"),
        makeTable(
          ["Risk", "Likelihood", "Impact", "Mitigation"],
          [
            ["OLED interferes with IMU tracking quality", "Medium", "Critical", "Prototype first (Week 1\u20132 GO/NO-GO gate). If display degrades tracking, fall back to LED-only battery indicator and save OLED for V2 after firmware optimization."],
            ["18650 makes trackers too bulky for some users", "Medium", "Moderate", "Own it in marketing. Position as \u201cbuilt for marathon sessions.\u201d Target audience cares about uptime, not miniaturization. Butterfly trackers exist for the thin crowd."],
            ["AliExpress component quality/DOA rates", "High", "Moderate", "Order 15% extra on every component. Test every IMU before soldering. Build relationships with specific sellers with good track records."],
            ["SlimeVR firmware changes break your fork", "Low", "High", "Pin to a stable firmware version. Track upstream changes. Update fork periodically between batches, not during production."],
            ["Patent/IP concerns on SlimeVR ecosystem", "Low", "High", "SlimeVR is open-source (MIT license for software, CERN-OHL for hardware). Third-party sellers are explicitly encouraged. Stay compliant with license terms."],
            ["Customer expects official SlimeVR support", "Medium", "Low", "Clear messaging: \u201cSlimeVR-compatible, independently built.\u201d Provide your own support. Link to official docs as supplementary resource."],
            ["Tariff/shipping cost increases", "Medium", "Moderate", "Domestic (US) sourcing for batteries. Buffer in pricing. Batch model allows price adjustment between drops."],
          ],
          [1800, 900, 900, 5760]
        ),

        new Paragraph({ children: [new PageBreak()] }),

        // ============================================================
        // 13. LONG-TERM VISION
        // ============================================================
        heading("13. Long-Term Vision"),
        p("The batch drop model is not just a launch strategy \u2014 it\u2019s the long-term operating model. Here\u2019s how it scales:"),

        new Paragraph({
          numbering: { reference: "bulletsPhases", level: 0 },
          spacing: { after: 120 },
          children: [bold("Months 1\u20136 (Establishment): "), normal("3\u20134 batches. Build reputation, content library, and customer base. Gross revenue: $8k\u2013$15k. Net profit after reinvestment: $3k\u2013$7k.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsPhases", level: 0 },
          spacing: { after: 120 },
          children: [bold("Months 6\u201312 (Growth): "), normal("Monthly batches of 20\u201340 sets. Add Shopify storefront. Add-on accessories become a meaningful revenue stream. Gross revenue: $40k\u2013$80k/year. Consider hiring part-time assembly help.")],
        }),
        new Paragraph({
          numbering: { reference: "bulletsPhases", level: 0 },
          spacing: { after: 120 },
          children: [bold("Year 2+ (Brand): "), normal("You\u2019re now a recognized brand in the FBT space. Batch drops sell out faster. Consider branching into adjacent products: VR accessories, custom avatars, motion capture services. The community you\u2019ve built is the asset, not just the hardware.")],
        }),

        p("The ultimate competitive moat is not the hardware \u2014 it\u2019s the combination of hardware quality, content production, community trust, and the iteration velocity of the batch model. Anyone can buy the same components. Almost nobody will build the ecosystem around them that you\u2019re planning to build."),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/home/claude/boutique_fbt_business_plan.docx", buffer);
  console.log("Document created successfully.");
});
