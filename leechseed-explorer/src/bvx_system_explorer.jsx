import React, { useState, useMemo } from "react";

// ═══════════════════════════════════════════════════════════
// BOLD VENTURE DESIGN SYSTEM — TOKEN CONSTANTS
// Source: ssot_00_bold_venture_design_system
// ═══════════════════════════════════════════════════════════

const BV = {
  // Background tokens (dark theme default)
  bg: {
    base:           "#101923", // --color-background-base-default (brightblue-900)
    baseHeader:     "#172635", // --color-background-base-header (darkblue-900)
    baseHover:      "#142435", // --color-background-base-hover (brightblue-850)
    baseSelected:   "#1c3f5e", // --color-background-base-selected (darkblue-700)
    surface:        "#1b2d3e", // --color-background-surface-default (darkblue-800)
    surfaceHeader:  "#172635", // --color-background-surface-header (darkblue-900)
    surfaceHover:   "#1c3851", // --color-background-surface-hover (brightblue-800)
    surfaceSelected:"#1c3f5e", // --color-background-surface-selected (darkblue-700)
    interactive:    "#4dacff", // --color-background-interactive-default (brightblue-500)
    interactiveHov: "#92cbff", // --color-background-interactive-hover (brightblue-400)
    interactiveMut: "#2b659b", // --color-background-interactive-muted (brightblue-700)
    transparent:    "#00000000",
  },
  // Text tokens
  text: {
    primary:    "#ffffff",  // --color-text-primary (neutral-000)
    secondary:  "#d4d8dd",  // --color-text-secondary (grey-300)
    placeholder:"#a4abb6",  // --color-text-placeholder (grey-500)
    inverse:    "#080c11",  // --color-text-inverse (darkblue-950)
    interactive:"#4dacff",  // --color-text-interactive-default (brightblue-500)
    interactiveHov:"#92cbff",
    error:      "#ff3838",  // --color-text-error (red-500)
  },
  // Border tokens
  border: {
    interactive:    "#4dacff",
    interactiveHov: "#92cbff",
    interactiveMut: "#2b659b",
    error:          "#ff3838",
    focus:          "#da9ce7", // pink-200
    subtle:         "#1c3851", // brightblue-800 (used for card/row borders)
  },
  // Status colors (dark theme)
  status: {
    critical: "#ff3838",
    serious:  "#ffb302",
    caution:  "#fce83a",
    normal:   "#56f000",
    standby:  "#2dccff",
    off:      "#a4abb6",
  },
  // Data visualization
  dataViz: ["#00c7cb","#938bdb","#4dacff","#70dde0","#c9c5ed","#92cbff","#a1e9eb","#b7dcff"],
  // Tier colors mapped to data-viz + status
  tier: {
    1: "#4dacff",  // brightblue-500 (primary interactive)
    2: "#ffb302",  // status serious (orange/amber)
    3: "#938bdb",  // purple-400 (data-viz-2)
  },
  // Typography
  font: {
    sans: "'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif",
  },
  // Spacing (4px grid)
  sp: { "0":0, "025":1, "050":2, "1":4, "2":8, "3":12, "4":16, "6":24, "8":32 },
  // Border
  radius: 3,
  borderWidth: 1,
  // Shadow
  shadow: "0px 4px 4px 1px rgba(0, 0, 0, 0.45)",
  // Opacity
  disabled: 0.4,
};

// Flag state to status color mapping
const FLAG_STATUS_COLOR = {
  ACTIVE:          BV.status.critical,
  PENDING:         BV.status.serious,
  FIRED_PRE_STORY: BV.status.off,
  INACTIVE:        BV.bg.surfaceHover,
};

// Dignity to status color mapping
const DIGNITY_COLOR = {
  Domicile:    BV.status.normal,
  Exaltation:  BV.status.normal,
  Peregrine:   BV.text.placeholder,
  Detriment:   BV.status.critical,
  Fall:        BV.status.serious,
};

const ASPECT_COLOR = {
  Conjunction: BV.text.interactive,
  Square:      BV.status.critical,
  Opposition:  BV.status.serious,
  Trine:       BV.status.normal,
  Sextile:     BV.status.standby,
};

const GATE_ICON = { AND: "\u2227", NOT: "\u00AC", XOR: "\u2295", OR: "\u2228" };

// ═══════════════════════════════════════════════════════════
// VICTORIA MIDNIGHT DATA
// ═══════════════════════════════════════════════════════════

const VICTORIA = {
  meta: { character_id: "victoria_midnight", character_name: 'Victoria "Tori" Midnight', ip: "overexitout", tier: 3, status: "locked", version: "1.0.0", storyform_id: "oxo_primary_v1" },
  layers: {
    CORE:   { base_value: 13, label: "CORE", domain: "Cognitive / Psychological Mass", tier: 1, num: 1 },
    VITAL:  { base_value: 14, label: "VITAL", domain: "Physical / Energetic Presence", tier: 1, num: 2 },
    SOCIAL: { base_value: 10, label: "SOCIAL", domain: "Relational Interface", tier: 1, num: 3 },
    WILL:   { base_value: 14, label: "WILL", domain: "Psychological Resistance", tier: 2, num: 4, derivation: "CORE + 1" },
    WOUND:  { wound_score: 10, label: "WOUND", domain: "Accumulated Damage", tier: 2, num: 5, scale: "SC-12 even" },
    DRIVE:  { base_value: 12, label: "DRIVE", domain: "Motivation Fuel", tier: 2, num: 6, derivation: "VITAL - 2" },
    ORIGIN: { label: "ORIGIN", domain: "Birth Context", tier: 3, num: 7, vars: { origin_class: "working_criminal_adjacent", origin_stability: 4, family_coherence: 8, origin_wound_seed: 7, tech_level: 7, system_exposure: "early_pre_awareness" }},
    IMPRINT:{ label: "IMPRINT", domain: "Emotional Conditioning", tier: 3, num: 8, vars: { attachment_style: "secure_anxious", attachment_style_score: 7, emotional_range: 11, conditional_patterns: ["merit_earns_freedom","loyalty_to_kinship","distrust_of_institution"], imprint_flexibility: 4, primary_attachment_object: "brother_deceased" }},
    EROS:   { label: "EROS", domain: "Psycho-Sexual Conditioning", tier: 3, num: 9, vars: { erotic_blueprint_type: "kinesthetic", desire_vector: 4, shame_index: 2, intimacy_mode: "parallel_presence", source_confidence: "inferred" }},
    SHADOW: { label: "SHADOW", domain: "Repressed Content", tier: 3, num: 10, vars: { shadow_density: 8, projection_tendency: 6, regression_pattern: "control_escalation", shadow_content: ["culpability_for_brother","distrust_of_own_judgment","fear_of_being_right_and_wrong"] }},
    DESTINY:{ label: "DESTINY", domain: "Growth Vector", tier: 3, num: 11, vars: { growth_axis: "inequity", resistance_index: 8, soul_evolution_archetype: "tactical_disruptor", karmic_memory: "meritocratic_certainty", growth_requirement: "accept_asymmetry" }},
    FUNC:   { label: "FUNCTION", domain: "Narrative Mechanics", tier: 3, num: 12, vars: { dramatica_archetype: "Protagonist", mc_problem_element: "Equity", methodology_element: "Certainty", evaluation_element: "Proven", purpose_element: "Knowledge", narrative_invariant: "cost_and_meaning", story_outcome: "Failure", story_judgement: "Good", limit_type: "Optionlock", resolve: "Change" }},
  },
  derived: {
    basic_damage_resistance: { value: 17, formula: "(WILL\u00d73) - (WOUND\u00d75/2)", internal: "42 - 25 = 17", max: 60 },
    social_legibility: { value: 20, formula: "(SOCIAL\u00d73) - (proj\u00d75/3)", internal: "30 - 10 = 20", max: 60 },
    narrative_momentum: { value: 56, formula: "(DRIVE\u00d73) + (resist\u00d75/2)", internal: "36 + 20 = 56", max: 60 },
    stress_threshold: { value: -8, formula: "(WILL\u00d73) - (WOUND\u00d75)", internal: "42 - 50 = -8", max: 60 },
    collapse_risk: { value: 45, formula: "(WOUND\u00d75 + shadow\u00d75) / 2", internal: "(50+40)/2 = 45", max: 60 },
    truth_exposure_index: { value: 80, formula: "(SOCIAL\u00d73) + (12-shame)\u00d75", internal: "30 + 50 = 80", max: 60 },
  },
  flags: {
    shadow_denial: { state: "ACTIVE", trigger: "WOUND>6 AND proj\u22656 AND patterns\u220Bmerit_earns_freedom" },
    truth_vulnerability: { state: "ACTIVE", trigger: "SOCIAL<12 AND mc_problem=Equity AND shadow>6" },
    optionlock_progression: { state: "ACTIVE", trigger: "WOUND>8 AND resist>8 AND limit=Optionlock" },
    earned_judgement: { state: "PENDING", trigger: "archetype=Protagonist AND outcome=Failure AND WILL>10" },
    kinship_collapse: { state: "FIRED_PRE_STORY", trigger: "attach_score>6 AND attach_obj=deceased AND WOUND>8" },
  },
  astrology: {
    personal: { sun: { sign: "Taurus", element: "Earth", modality: "Fixed" }, moon: { sign: "Libra" }, mercury: { sign: "Capricorn" }, venus: { sign: "Virgo" }, mars: { sign: "Capricorn" } },
    structural: { saturn: { sign: "Gemini" }, jupiter: { sign: "Sagittarius" }, uranus: { sign: "Aquarius" }, neptune: { sign: "Pisces" }, pluto: { sign: "Scorpio" } },
    angles: { ascendant: "Aries", midheaven: "Capricorn", descendant: "Libra", ic: "Cancer" },
    dignities: { sun: "Peregrine", moon: "Peregrine", mercury: "Peregrine", venus: "Fall", mars: "Exaltation", saturn: "Detriment", jupiter: "Domicile", uranus: "Domicile", neptune: "Domicile", pluto: "Domicile" },
    aspects: [
      { a: "Sun", type: "Opposition", b: "Pluto", gate: "XOR", fn: "Identity vs terminal destruction" },
      { a: "Moon", type: "Square", b: "Mars", gate: "NOT", fn: "Equity instinct blocks disciplined action" },
      { a: "Mercury", type: "Conjunction", b: "Mars", gate: "AND", fn: "To determine is to act" },
      { a: "Venus", type: "Trine", b: "Mars", gate: "OR", fn: "Desire and action flow freely" },
      { a: "Saturn", type: "Square", b: "Sun", gate: "NOT", fn: "Truth-limit blocks identity expression" },
      { a: "Jupiter", type: "Opposition", b: "Saturn", gate: "XOR", fn: "Vision opposes limit" },
      { a: "Moon", type: "Square", b: "Pluto", gate: "NOT", fn: "Fairness blocks surrender to transformation" },
    ],
    houses: { sun: 1, moon: 7, mercury: 10, venus: 6, mars: 10, saturn: 3, jupiter: 9, uranus: 11, neptune: 12, pluto: 8 },
  },
  feeds: [
    { from: "Sun (Taurus)", to: "L1 CORE", type: "justification", note: "Earth Sun = practical cognition" },
    { from: "Mercury (Capricorn)", to: "L1 CORE", type: "justification", note: "Structural processing" },
    { from: "Mars (Cap, Exalt)", to: "L2 VITAL", type: "justification", note: "Exalted = highest physical" },
    { from: "Ascendant (Aries)", to: "L2 VITAL", type: "texture", note: "Kinetic presentation" },
    { from: "Ascendant (Aries)", to: "L3 SOCIAL", type: "justification", note: "Unfiltered interface" },
    { from: "Venus (Virgo, Fall)", to: "L3 SOCIAL", type: "texture", note: "Non-performative desire" },
    { from: "Saturn (Gemini, Det)", to: "L4 WILL", type: "ceiling", note: "Limit is glitchy but forges resistance" },
    { from: "Sun-Saturn Sq", to: "L4 WILL", type: "texture", note: "Identity tested constantly" },
    { from: "Venus Fall", to: "L5 WOUND", type: "texture", note: "Desire crack" },
    { from: "Moon-Mars Sq", to: "L5 WOUND", type: "trigger", note: "Crash mechanism" },
    { from: "Mars (Exalt)", to: "L6 DRIVE", type: "justification", note: "Max physical efficiency" },
    { from: "Jupiter (Sag)", to: "L6 DRIVE", type: "texture", note: "Incompatible element = meaning-driven" },
    { from: "IC (Cancer)", to: "L7 ORIGIN", type: "partial", note: "Family/safety root" },
    { from: "Moon (Libra)", to: "L8 IMPRINT", type: "primary", note: "Attachment through reciprocity" },
    { from: "Venus (Virgo)", to: "L9 EROS", type: "supplemental", note: "Kinesthetic blueprint" },
    { from: "Neptune 12th", to: "L10 SHADOW", type: "primary", note: "Desire buried beneath awareness" },
    { from: "Jupiter (Sag, Dom)", to: "L11 DESTINY", type: "primary", note: "Vision at full power" },
    { from: "Uranus (Aqu, Dom)", to: "L11 DESTINY", type: "primary", note: "Awakening is real" },
  ],
};


// ═══════════════════════════════════════════════════════════
// SHARED UI PRIMITIVES
// ═══════════════════════════════════════════════════════════

function ProgressBar({ value, max, color, height = 4, negative }) {
  const pct = Math.min((Math.abs(value) / max) * 100, 100);
  return (
    <div style={{ width: "100%", height, background: BV.bg.surface, borderRadius: BV.radius, overflow: "hidden" }}>
      <div style={{ width: `${pct}%`, height: "100%", background: negative ? BV.status.critical : color || BV.bg.interactive, borderRadius: BV.radius, transition: "width 0.5s ease" }} />
    </div>
  );
}

function Badge({ children, color }) {
  return (
    <span style={{ display: "inline-block", fontSize: 10, fontWeight: 700, padding: "2px 8px", borderRadius: BV.radius, background: (color || BV.text.placeholder) + "1A", color: color || BV.text.placeholder, letterSpacing: "0.08em", lineHeight: "16px" }}>
      {children}
    </span>
  );
}

function Tag({ children, color }) {
  return (
    <span style={{ display: "inline-block", fontSize: 11, padding: "2px 8px", borderRadius: 4, background: (color || BV.border.interactiveMut) + "28", color: color || BV.text.secondary, marginRight: 4, marginBottom: 3, lineHeight: "18px" }}>
      {children}
    </span>
  );
}

function StatusDot({ state }) {
  const c = FLAG_STATUS_COLOR[state] || BV.bg.surfaceHover;
  return (
    <span style={{ display: "inline-block", width: 10, height: 10, borderRadius: "50%", background: c, flexShrink: 0, boxShadow: state === "ACTIVE" ? `0 0 8px ${c}88` : "none" }} />
  );
}

function SectionLabel({ children, color }) {
  return (
    <div style={{ fontSize: 11, letterSpacing: "0.14em", color: color || BV.text.placeholder, marginBottom: BV.sp[2], marginTop: BV.sp[6], fontWeight: 500 }}>
      {children}
    </div>
  );
}

function Card({ children, color, selected, onClick, style: sx }) {
  const [hov, setHov] = useState(false);
  return (
    <div
      onClick={onClick}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        background: selected ? BV.bg.surfaceSelected : hov ? BV.bg.surfaceHover : BV.bg.surface,
        border: `${BV.borderWidth}px solid ${selected ? (color || BV.border.interactive) + "66" : hov ? BV.border.subtle : BV.bg.baseHeader}`,
        borderRadius: BV.radius,
        padding: `${BV.sp[3]}px ${BV.sp[4]}px`,
        cursor: onClick ? "pointer" : "default",
        transition: "all 0.2s ease",
        position: "relative",
        ...sx,
      }}
    >
      {selected && <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 2, background: color || BV.bg.interactive, borderRadius: `${BV.radius}px ${BV.radius}px 0 0` }} />}
      {children}
    </div>
  );
}

// ═══════════════════════════════════════════════════════════
// PIPELINE VIEW
// ═══════════════════════════════════════════════════════════

function PipelineView() {
  const stages = [
    { label: "AUTHORITATIVE\nDOCUMENT", sub: "Character Bible", color: BV.text.placeholder },
    { label: "DRAMATICA\nSTORYFORM", sub: "Narrative Engine", color: BV.status.serious },
    { label: "DRAMATICA\nINGEST", sub: "Template (.md)", color: BV.status.serious },
    { label: "DAI\nTRANSLATION", sub: "18-Step Derivation", color: BV.tier[3] },
    { label: "CHARACTER\nASTROLOGY", sub: "Ingest Template (.md)", color: BV.tier[3] },
    { label: "STEP 1\nVERIFICATION", sub: "3-Component Gate", color: BV.status.normal },
    { label: "VERTICAL\nSLICE", sub: "12-Layer Record", color: BV.status.normal },
    { label: "STATE\nDIFFS", sub: "Narrative Overlays", color: BV.status.caution },
  ];

  const flows = [
    { id: "A", label: "Dramatica Extraction", from: "Locked Storyform", to: "Dramatica Ingest (.md)", color: BV.status.serious, steps: "8 extraction steps" },
    { id: "B", label: "DAI Translation", from: "Locked Dramatica Ingest", to: "Astrology Ingest (.md)", color: BV.tier[3], steps: "18-step derivation" },
    { id: "C", label: "Vertical Slice Production", from: "Both Ingests + Auth Doc", to: "12-Layer Record (.md)", color: BV.status.normal, steps: "7 steps, 4 checkpoints" },
    { id: "D", label: "State Diffing", from: "Base + Narrative Event", to: "State Diff Record (.md)", color: BV.status.caution, steps: "5 event categories" },
  ];

  return (
    <div>
      <SectionLabel>PIPELINE ARCHITECTURE</SectionLabel>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: BV.sp[2] }}>
        {stages.map((s, i) => (
          <Card key={i} color={s.color} style={{ textAlign: "center", padding: `${BV.sp[4]}px ${BV.sp[3]}px` }}>
            <div style={{ fontSize: 11, fontWeight: 700, color: BV.text.primary, whiteSpace: "pre-line", lineHeight: 1.35, marginBottom: BV.sp[1] }}>{s.label}</div>
            <div style={{ fontSize: 11, color: BV.text.placeholder }}>{s.sub}</div>
            <div style={{ position: "absolute", top: BV.sp[1], right: BV.sp[2], fontSize: 10, color: BV.border.subtle }}>{String(i).padStart(2, "0")}</div>
          </Card>
        ))}
      </div>

      <SectionLabel>FLOW SEQUENCE</SectionLabel>
      <div style={{ display: "flex", flexDirection: "column", gap: BV.sp[2] }}>
        {flows.map(f => (
          <Card key={f.id} color={f.color} style={{ display: "flex", alignItems: "center", gap: BV.sp[4] }}>
            <div style={{ width: 36, height: 36, borderRadius: "50%", border: `2px solid ${f.color}`, display: "flex", alignItems: "center", justifyContent: "center", color: f.color, fontWeight: 700, fontSize: 15, flexShrink: 0 }}>{f.id}</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 13, fontWeight: 700, color: BV.text.primary, marginBottom: 2 }}>{f.label}</div>
              <div style={{ fontSize: 11, color: BV.text.placeholder }}>{f.from} &rarr; {f.to}</div>
            </div>
            <div style={{ fontSize: 11, color: f.color, opacity: 0.7, textAlign: "right" }}>{f.steps}</div>
          </Card>
        ))}
      </div>

      <SectionLabel>BASE 60 DIVISOR LATTICE</SectionLabel>
      <Card color={BV.text.interactive} style={{ padding: BV.sp[4] }}>
        <div style={{ display: "flex", justifyContent: "center", gap: BV.sp[2], flexWrap: "wrap", marginBottom: BV.sp[3] }}>
          {[1,2,3,4,5,6,10,12,15,20,30,60].map(d => {
            const isKey = d === 12 || d === 20 || d === 60;
            const c = d === 12 ? BV.text.interactive : d === 20 ? BV.status.serious : d === 60 ? BV.status.normal : BV.text.placeholder;
            return (
              <div key={d} style={{ width: 40, height: 40, borderRadius: BV.radius, border: `${BV.borderWidth}px solid ${isKey ? c : BV.border.subtle}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 13, fontWeight: isKey ? 700 : 400, color: c, background: isKey ? c + "0D" : BV.bg.transparent }}>{d}</div>
            );
          })}
        </div>
        <div style={{ display: "flex", gap: BV.sp[4], fontSize: 11, color: BV.text.placeholder, justifyContent: "center" }}>
          <span><span style={{ color: BV.text.interactive }}>&#9632;</span> SC-12 sub-variables</span>
          <span><span style={{ color: BV.status.serious }}>&#9632;</span> SC-20 attributes</span>
          <span><span style={{ color: BV.status.normal }}>&#9632;</span> SC-60 internal</span>
        </div>
      </Card>
    </div>
  );
}

// ═══════════════════════════════════════════════════════════
// LAYER VIEW + DETAIL
// ═══════════════════════════════════════════════════════════

function LayerView({ onSelectLayer, selectedLayer }) {
  const tierGroups = [
    { tier: 1, label: "TIER 1 — PRIMARY ATTRIBUTES", layers: ["CORE","VITAL","SOCIAL"] },
    { tier: 2, label: "TIER 2 — SECONDARY ATTRIBUTES", layers: ["WILL","WOUND","DRIVE"] },
    { tier: 3, label: "TIER 3 — DEEP VARIABLE STACKS", layers: ["ORIGIN","IMPRINT","EROS","SHADOW","DESTINY","FUNC"] },
  ];

  return (
    <div>
      {tierGroups.map(tg => {
        const color = BV.tier[tg.tier];
        return (
          <div key={tg.tier}>
            <SectionLabel color={color}>{tg.label}</SectionLabel>
            <div style={{ display: "grid", gridTemplateColumns: tg.tier === 3 ? "repeat(3, 1fr)" : "repeat(3, 1fr)", gap: BV.sp[2] }}>
              {tg.layers.map(lk => {
                const L = VICTORIA.layers[lk];
                const isSelected = selectedLayer === lk;
                const val = L.base_value ?? L.wound_score ?? null;
                const max = lk === "WOUND" ? 12 : 20;
                return (
                  <Card key={lk} color={color} selected={isSelected} onClick={() => onSelectLayer(lk)}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: BV.sp[2] }}>
                      <div>
                        <Badge color={color}>T{tg.tier}</Badge>
                        <span style={{ fontSize: 13, fontWeight: 700, color: BV.text.primary, marginLeft: BV.sp[2] }}>L{L.num} {L.label}</span>
                      </div>
                      {val !== null && <div style={{ fontSize: 22, fontWeight: 700, color, lineHeight: 1 }}>{val}</div>}
                    </div>
                    <div style={{ fontSize: 11, color: BV.text.placeholder, marginBottom: BV.sp[2] }}>{L.domain}</div>
                    {val !== null && <ProgressBar value={val} max={max} color={color} />}
                    {L.vars && (
                      <div style={{ marginTop: BV.sp[2], display: "flex", flexWrap: "wrap", gap: 2 }}>
                        {Object.keys(L.vars).slice(0, 3).map(k => <Tag key={k} color={color}>{k}</Tag>)}
                        {Object.keys(L.vars).length > 3 && <Tag>+{Object.keys(L.vars).length - 3}</Tag>}
                      </div>
                    )}
                  </Card>
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}

function LayerDetail({ layerKey }) {
  const L = VICTORIA.layers[layerKey];
  if (!L) return null;
  const color = BV.tier[L.tier];
  const val = L.base_value ?? L.wound_score ?? null;
  const max = layerKey === "WOUND" ? 12 : L.tier <= 2 ? 20 : 12;
  const scale = layerKey === "WOUND" ? "SC-12 (even)" : L.tier <= 2 ? "SC-20" : "SC-12";
  const layerFeeds = VICTORIA.feeds.filter(f => f.to.includes(L.label));
  const layerFlags = Object.entries(VICTORIA.flags).filter(([k, v]) =>
    v.trigger.toLowerCase().includes(layerKey.toLowerCase()) ||
    (layerKey === "WOUND" && v.trigger.includes("WOUND")) ||
    (layerKey === "SOCIAL" && v.trigger.includes("SOCIAL"))
  );

  return (
    <Card color={color} selected style={{ marginTop: BV.sp[3] }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: BV.sp[3] }}>
        <div>
          <Badge color={color}>TIER {L.tier}</Badge>
          <span style={{ fontSize: 16, fontWeight: 700, color: BV.text.primary, marginLeft: BV.sp[2] }}>{L.label}</span>
          <div style={{ fontSize: 12, color: BV.text.placeholder, marginTop: BV.sp[1] }}>{L.domain}</div>
        </div>
        {val !== null && (
          <div style={{ textAlign: "right" }}>
            <div style={{ fontSize: 32, fontWeight: 700, color, lineHeight: 1 }}>{val}</div>
            <div style={{ fontSize: 11, color: BV.text.placeholder }}>{scale} / max {max}</div>
            {L.derivation && <div style={{ fontSize: 11, color: color + "AA", marginTop: 2 }}>{L.derivation}</div>}
          </div>
        )}
      </div>

      {L.vars && (
        <>
          <SectionLabel color={color}>VARIABLE STACK</SectionLabel>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: BV.sp[2] }}>
            {Object.entries(L.vars).map(([k, v]) => (
              <div key={k} style={{ background: BV.bg.base, borderRadius: BV.radius, padding: `${BV.sp[2]}px ${BV.sp[3]}px`, border: `${BV.borderWidth}px solid ${BV.bg.baseHeader}` }}>
                <div style={{ fontSize: 11, color, fontWeight: 500, marginBottom: BV.sp[1] }}>{k}</div>
                <div style={{ fontSize: 13, color: BV.text.primary, wordBreak: "break-word" }}>
                  {Array.isArray(v) ? v.map((item, i) => <Tag key={i} color={color}>{item}</Tag>) : String(v)}
                </div>
                {typeof v === "number" && <div style={{ marginTop: BV.sp[1] }}><ProgressBar value={v} max={12} color={color} height={3} /></div>}
              </div>
            ))}
          </div>
        </>
      )}

      {layerFeeds.length > 0 && (
        <>
          <SectionLabel color={BV.status.standby}>ASTROLOGY FEEDS</SectionLabel>
          {layerFeeds.map((f, i) => (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: BV.sp[2], padding: `${BV.sp[1]}px 0`, borderBottom: `1px solid ${BV.bg.baseHeader}` }}>
              <Tag color={BV.tier[3]}>{f.from}</Tag>
              <span style={{ color: BV.text.placeholder }}>&rarr;</span>
              <Tag color={BV.status.standby}>{f.type}</Tag>
              <span style={{ fontSize: 11, color: BV.text.secondary, flex: 1 }}>{f.note}</span>
            </div>
          ))}
        </>
      )}

      {layerFlags.length > 0 && (
        <>
          <SectionLabel color={BV.status.critical}>FLAGS</SectionLabel>
          {layerFlags.map(([k, v]) => (
            <div key={k} style={{ display: "flex", alignItems: "center", gap: BV.sp[2], padding: `${BV.sp[1]}px 0` }}>
              <StatusDot state={v.state} />
              <span style={{ fontSize: 12, fontWeight: 700, color: BV.text.primary }}>{k.replace(/_/g, " ").toUpperCase()}</span>
              <span style={{ fontSize: 11, color: FLAG_STATUS_COLOR[v.state] }}>{v.state}</span>
            </div>
          ))}
        </>
      )}
    </Card>
  );
}

// ═══════════════════════════════════════════════════════════
// ASTROLOGY VIEW
// ═══════════════════════════════════════════════════════════

function AstrologyView() {
  const A = VICTORIA.astrology;
  return (
    <div>
      <SectionLabel color={BV.tier[3]}>NATAL CHART</SectionLabel>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: BV.sp[2], marginBottom: BV.sp[4] }}>
        <Card color={BV.tier[3]}>
          <div style={{ fontSize: 12, fontWeight: 700, color: BV.tier[3], marginBottom: BV.sp[2] }}>PERSONAL STACK</div>
          {Object.entries(A.personal).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: `${BV.sp[1]}px 0`, borderBottom: `1px solid ${BV.bg.baseHeader}` }}>
              <span style={{ fontWeight: 500, color: BV.text.primary, textTransform: "capitalize", fontSize: 13 }}>{k}</span>
              <div style={{ display: "flex", alignItems: "center", gap: BV.sp[2] }}>
                <span style={{ color: BV.text.primary, fontSize: 13 }}>{v.sign}</span>
                <span style={{ fontSize: 11, color: DIGNITY_COLOR[A.dignities[k]], fontWeight: 500 }}>{A.dignities[k]}</span>
              </div>
            </div>
          ))}
        </Card>
        <Card color={BV.tier[3]}>
          <div style={{ fontSize: 12, fontWeight: 700, color: BV.tier[3], marginBottom: BV.sp[2] }}>STRUCTURAL STACK</div>
          {Object.entries(A.structural).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: `${BV.sp[1]}px 0`, borderBottom: `1px solid ${BV.bg.baseHeader}` }}>
              <span style={{ fontWeight: 500, color: BV.text.primary, textTransform: "capitalize", fontSize: 13 }}>{k}</span>
              <div style={{ display: "flex", alignItems: "center", gap: BV.sp[2] }}>
                <span style={{ color: BV.text.primary, fontSize: 13 }}>{v.sign}</span>
                <span style={{ fontSize: 11, color: DIGNITY_COLOR[A.dignities[k]], fontWeight: 500 }}>{A.dignities[k]}</span>
              </div>
            </div>
          ))}
        </Card>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: BV.sp[2], marginBottom: BV.sp[4] }}>
        <Card color={BV.status.serious}>
          <div style={{ fontSize: 12, fontWeight: 700, color: BV.status.serious, marginBottom: BV.sp[2] }}>ANGLES</div>
          {Object.entries(A.angles).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: `${BV.sp[1]}px 0`, borderBottom: `1px solid ${BV.bg.baseHeader}` }}>
              <span style={{ fontWeight: 500, color: BV.text.primary, textTransform: "capitalize", fontSize: 13 }}>{k}</span>
              <span style={{ color: BV.text.primary, fontSize: 13 }}>{v}</span>
            </div>
          ))}
        </Card>
        <Card color={BV.status.normal}>
          <div style={{ fontSize: 12, fontWeight: 700, color: BV.status.normal, marginBottom: BV.sp[2] }}>HOUSES</div>
          {Object.entries(A.houses).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: `${BV.sp[1]}px 0`, borderBottom: `1px solid ${BV.bg.baseHeader}` }}>
              <span style={{ fontWeight: 500, color: BV.text.primary, textTransform: "capitalize", fontSize: 13 }}>{k}</span>
              <span style={{ color: BV.status.normal, fontSize: 13 }}>H{v} <span style={{ fontSize: 11, color: BV.text.placeholder }}>{[1,4,7,10].includes(v) ? "angular" : [2,5,8,11].includes(v) ? "succedent" : "cadent"}</span></span>
            </div>
          ))}
        </Card>
      </div>

      <SectionLabel color={BV.status.critical}>ASPECT MAP — LOGIC GATES</SectionLabel>
      <div style={{ display: "flex", flexDirection: "column", gap: BV.sp[1] }}>
        {A.aspects.map((asp, i) => (
          <Card key={i} color={ASPECT_COLOR[asp.type]} style={{ display: "flex", alignItems: "center", gap: BV.sp[3], padding: `${BV.sp[2]}px ${BV.sp[3]}px` }}>
            <span style={{ fontWeight: 700, color: BV.text.primary, width: 72, fontSize: 13 }}>{asp.a}</span>
            <span style={{ fontSize: 18, fontWeight: 700, color: ASPECT_COLOR[asp.type], width: 28, textAlign: "center" }}>{GATE_ICON[asp.gate]}</span>
            <span style={{ fontWeight: 700, color: BV.text.primary, width: 72, fontSize: 13 }}>{asp.b}</span>
            <Badge color={ASPECT_COLOR[asp.type]}>{asp.type}</Badge>
            <Badge color={BV.text.placeholder}>{asp.gate}</Badge>
            <span style={{ fontSize: 11, color: BV.text.secondary, flex: 1 }}>{asp.fn}</span>
          </Card>
        ))}
      </div>
      <div style={{ marginTop: BV.sp[2], fontSize: 11, color: BV.text.placeholder }}>
        5 hard aspects (Square + Opposition) / 1 conjunction / 1 trine. High-friction chart.
      </div>
    </div>
  );
}

// ═══════════════════════════════════════════════════════════
// FEED MAP VIEW
// ═══════════════════════════════════════════════════════════

function FeedMapView() {
  const planets = ["Sun","Moon","Mercury","Venus","Mars","Saturn","Jupiter","Uranus","Neptune","Pluto","Ascendant","IC"];
  const planetMeta = {
    Sun:{sign:"Taurus",dignity:"Peregrine",c:BV.status.caution},Moon:{sign:"Libra",dignity:"Peregrine",c:BV.text.secondary},
    Mercury:{sign:"Capricorn",dignity:"Peregrine",c:BV.status.standby},Venus:{sign:"Virgo",dignity:"Fall",c:BV.dataViz[1]},
    Mars:{sign:"Capricorn",dignity:"Exaltation",c:BV.status.critical},Saturn:{sign:"Gemini",dignity:"Detriment",c:BV.text.placeholder},
    Jupiter:{sign:"Sagittarius",dignity:"Domicile",c:BV.dataViz[1]},Uranus:{sign:"Aquarius",dignity:"Domicile",c:BV.status.normal},
    Neptune:{sign:"Pisces",dignity:"Domicile",c:BV.status.standby},Pluto:{sign:"Scorpio",dignity:"Domicile",c:BV.status.critical},
    Ascendant:{sign:"Aries",dignity:"\u2014",c:BV.status.serious},IC:{sign:"Cancer",dignity:"\u2014",c:BV.tier[3]},
  };

  return (
    <div>
      <SectionLabel>ASTROLOGY &rarr; 12-LAYER FEED MAP</SectionLabel>
      <div style={{ background: BV.bg.surface, borderRadius: BV.radius, border: `${BV.borderWidth}px solid ${BV.bg.baseHeader}`, overflow: "hidden" }}>
        <div style={{ display: "grid", gridTemplateColumns: "180px 1fr 120px", background: BV.bg.surfaceHeader, boxShadow: "0px 4px 8px 0px rgba(0,0,0,0.45)" }}>
          <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, fontSize: 11, color: BV.text.secondary, fontWeight: 700 }}>PLANET</div>
          <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, fontSize: 11, color: BV.text.secondary, fontWeight: 700 }}>FEEDS</div>
          <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, fontSize: 11, color: BV.text.secondary, fontWeight: 700 }}>DIGNITY</div>
        </div>
        {planets.map(p => {
          const pm = planetMeta[p];
          const feeds = VICTORIA.feeds.filter(f => f.from.startsWith(p) || f.from.includes(p));
          return (
            <div key={p} style={{ display: "grid", gridTemplateColumns: "180px 1fr 120px", borderBottom: `1px solid ${BV.bg.base}` }}>
              <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, display: "flex", alignItems: "center", gap: BV.sp[2] }}>
                <span style={{ color: pm.c, fontWeight: 700, fontSize: 13 }}>{p}</span>
                <span style={{ fontSize: 11, color: BV.text.placeholder }}>{pm.sign}</span>
              </div>
              <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, display: "flex", flexWrap: "wrap", gap: 3, alignItems: "center" }}>
                {feeds.map((f, i) => <Tag key={i} color={BV.tier[f.to.match(/L(\d+)/)?.[1] <= 3 ? 1 : f.to.match(/L(\d+)/)?.[1] <= 6 ? 2 : 3]}>{f.to} ({f.type})</Tag>)}
                {feeds.length === 0 && <span style={{ fontSize: 11, color: BV.border.subtle }}>&mdash;</span>}
              </div>
              <div style={{ padding: `${BV.sp[2]}px ${BV.sp[3]}px`, display: "flex", alignItems: "center" }}>
                <span style={{ fontSize: 12, fontWeight: 500, color: DIGNITY_COLOR[pm.dignity] || BV.text.placeholder }}>{pm.dignity}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

// ═══════════════════════════════════════════════════════════
// DERIVED STATS + FLAGS VIEW
// ═══════════════════════════════════════════════════════════

function DerivedView() {
  return (
    <div>
      <SectionLabel color={BV.status.standby}>DERIVED STATISTICS — INTERNAL 0-60 SPACE</SectionLabel>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: BV.sp[2], marginBottom: BV.sp[6] }}>
        {Object.entries(VICTORIA.derived).map(([k, v]) => {
          const isNeg = v.value < 0;
          const isOver = v.value > v.max;
          const color = isNeg ? BV.status.critical : isOver ? BV.status.serious : v.value > 45 ? BV.status.normal : v.value > 20 ? BV.status.standby : BV.text.placeholder;
          return (
            <Card key={k} color={color}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: BV.sp[2] }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: BV.text.primary, textTransform: "uppercase" }}>{k.replace(/_/g, " ")}</div>
                <div style={{ fontSize: 26, fontWeight: 700, color, lineHeight: 1 }}>{v.value}</div>
              </div>
              <ProgressBar value={v.value} max={v.max} color={color} negative={isNeg} />
              <div style={{ fontSize: 11, color: BV.text.placeholder, marginTop: BV.sp[2] }}>{v.formula}</div>
              <div style={{ fontSize: 11, color: color + "99", marginTop: 2 }}>{v.internal}</div>
              {isNeg && <div style={{ fontSize: 11, color: BV.status.critical, marginTop: BV.sp[1], fontWeight: 500 }}>NEGATIVE — Operating past structural limit</div>}
              {isOver && <div style={{ fontSize: 11, color: BV.status.serious, marginTop: BV.sp[1], fontWeight: 500 }}>EXCEEDS BASE UNIT — Signal beyond containment</div>}
            </Card>
          );
        })}
      </div>

      <SectionLabel color={BV.status.critical}>STATUS FLAGS</SectionLabel>
      <div style={{ display: "flex", flexDirection: "column", gap: BV.sp[2] }}>
        {Object.entries(VICTORIA.flags).map(([k, v]) => {
          const fc = FLAG_STATUS_COLOR[v.state];
          return (
            <Card key={k} color={fc} style={{ display: "flex", alignItems: "center", gap: BV.sp[3] }}>
              <StatusDot state={v.state} />
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: BV.text.primary }}>{k.replace(/_/g, " ").toUpperCase()}</div>
                <div style={{ fontSize: 11, color: BV.text.placeholder, marginTop: 2 }}>{v.trigger}</div>
              </div>
              <Badge color={fc}>{v.state}</Badge>
            </Card>
          );
        })}
      </div>
    </div>
  );
}


// ═══════════════════════════════════════════════════════════
// MAIN APPLICATION — BOLD VENTURE SYSTEM EXPLORER
// ═══════════════════════════════════════════════════════════

export default function BoldVentureExplorer() {
  const [view, setView] = useState("pipeline");
  const [selectedLayer, setSelectedLayer] = useState(null);
  const [tabHover, setTabHover] = useState(null);

  const views = [
    { id: "pipeline", label: "PIPELINE" },
    { id: "layers", label: "LAYERS" },
    { id: "astrology", label: "ASTROLOGY" },
    { id: "feeds", label: "FEED MAP" },
    { id: "derived", label: "STATS & FLAGS" },
  ];

  return (
    <div style={{
      minHeight: "100vh",
      background: BV.bg.base,
      color: BV.text.primary,
      fontFamily: BV.font.sans,
      fontSize: 14,
      lineHeight: 1.429,
      letterSpacing: "0.005em",
    }}>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet" />

      {/* ── GLOBAL STATUS BAR ── */}
      <div style={{
        background: BV.bg.surfaceHeader,
        borderBottom: `${BV.borderWidth}px solid ${BV.bg.surface}`,
        padding: `${BV.sp[3]}px ${BV.sp[6]}px`,
        position: "sticky",
        top: 0,
        zIndex: 100,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        boxShadow: "0px 4px 8px 0px rgba(0,0,0,0.45)",
      }}>
        <div>
          <div style={{ fontSize: 11, letterSpacing: "0.14em", color: BV.text.interactive, fontWeight: 500, marginBottom: 2 }}>
            BOLD VENTURE // 02_CHARACTER_SYSTEMS
          </div>
          <div style={{ fontSize: 20, fontWeight: 400, color: BV.text.primary, letterSpacing: "0.0025em", lineHeight: 1.176, margin: 0 }}>
            System Explorer
          </div>
          <div style={{ fontSize: 12, color: BV.text.placeholder, marginTop: 2, letterSpacing: "0.005em" }}>
            Victoria "Tori" Midnight &mdash; OVEREXITOUT &mdash; v1.0.0 LOCKED
          </div>
        </div>

        {/* ── TAB NAVIGATION ── */}
        <nav style={{ display: "flex", gap: 0, borderBottom: "none" }}>
          {views.map(v => {
            const isActive = view === v.id;
            const isHov = tabHover === v.id;
            return (
              <button
                key={v.id}
                onClick={() => { setView(v.id); if (v.id !== "layers") setSelectedLayer(null); }}
                onMouseEnter={() => setTabHover(v.id)}
                onMouseLeave={() => setTabHover(null)}
                style={{
                  padding: `${BV.sp[2]}px ${BV.sp[4]}px`,
                  background: BV.bg.transparent,
                  border: "none",
                  borderBottom: `4px solid ${isActive ? BV.border.interactive : BV.bg.transparent}`,
                  color: isActive ? BV.text.primary : isHov ? BV.text.interactiveHov : BV.text.interactive,
                  fontFamily: BV.font.sans,
                  fontSize: 14,
                  fontWeight: isActive ? 700 : 400,
                  cursor: "pointer",
                  transition: "all 0.15s ease",
                  letterSpacing: "0.005em",
                }}
              >
                {v.label}
              </button>
            );
          })}
        </nav>
      </div>

      {/* ── MAIN CONTENT ── */}
      <div style={{ maxWidth: 1200, margin: "0 auto", padding: `${BV.sp[4]}px ${BV.sp[6]}px ${BV.sp[24]}px` }}>
        {view === "pipeline" && <PipelineView />}
        {view === "layers" && (
          <>
            <LayerView
              onSelectLayer={(lk) => setSelectedLayer(selectedLayer === lk ? null : lk)}
              selectedLayer={selectedLayer}
            />
            {selectedLayer && <LayerDetail layerKey={selectedLayer} />}
          </>
        )}
        {view === "astrology" && <AstrologyView />}
        {view === "feeds" && <FeedMapView />}
        {view === "derived" && <DerivedView />}
      </div>
    </div>
  );
}
