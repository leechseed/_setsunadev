import React from 'react'
import { useState, useMemo } from "react";

// ═══════════════════════════════════════════════════════════
// DATA: Victoria Midnight preloaded
// ═══════════════════════════════════════════════════════════

const VICTORIA = {
  meta: { character_id: "victoria_midnight", character_name: 'Victoria "Tori" Midnight', ip: "overexitout", tier: 3, status: "locked", version: "1.0.0", storyform_id: "oxo_primary_v1" },
  layers: {
    CORE:   { base_value: 13, label: "CORE", domain: "Cognitive / Psychological Mass", tier: 1, color: "#4a9eff", cost: 60 },
    VITAL:  { base_value: 14, label: "VITAL", domain: "Physical / Energetic Presence", tier: 1, color: "#4a9eff", cost: 80 },
    SOCIAL: { base_value: 10, label: "SOCIAL", domain: "Relational Interface", tier: 1, color: "#4a9eff", cost: 0 },
    WILL:   { base_value: 14, label: "WILL", domain: "Psychological Resistance", tier: 2, color: "#ff6b4a", derivation: "CORE + 1" },
    WOUND:  { wound_score: 10, label: "WOUND", domain: "Accumulated Damage", tier: 2, color: "#ff6b4a", scale: "SC-12 even" },
    DRIVE:  { base_value: 12, label: "DRIVE", domain: "Motivation Fuel", tier: 2, color: "#ff6b4a", derivation: "VITAL - 2" },
    ORIGIN: { label: "ORIGIN", domain: "Birth Context", tier: 3, color: "#a78bfa", vars: { origin_class: "working_criminal_adjacent", origin_stability: 4, family_coherence: 8, origin_wound_seed: 7, tech_level: 7, system_exposure: "early_pre_awareness" }},
    IMPRINT:{ label: "IMPRINT", domain: "Emotional Conditioning", tier: 3, color: "#a78bfa", vars: { attachment_style: "secure_anxious", attachment_style_score: 7, emotional_range: 11, conditional_patterns: ["merit_earns_freedom","loyalty_to_kinship","distrust_of_institution"], imprint_flexibility: 4, primary_attachment_object: "brother_deceased" }},
    EROS:   { label: "EROS", domain: "Psycho-Sexual Conditioning", tier: 3, color: "#a78bfa", vars: { erotic_blueprint_type: "kinesthetic", desire_vector: 4, shame_index: 2, intimacy_mode: "parallel_presence", source_confidence: "inferred" }},
    SHADOW: { label: "SHADOW", domain: "Repressed Content", tier: 3, color: "#a78bfa", vars: { shadow_density: 8, projection_tendency: 6, regression_pattern: "control_escalation", shadow_content: ["culpability_for_brother","distrust_of_own_judgment","fear_of_being_right_and_wrong"] }},
    DESTINY:{ label: "DESTINY", domain: "Growth Vector", tier: 3, color: "#a78bfa", vars: { growth_axis: "inequity", resistance_index: 8, soul_evolution_archetype: "tactical_disruptor", karmic_memory: "meritocratic_certainty", growth_requirement: "accept_asymmetry" }},
    FUNC:   { label: "FUNCTION", domain: "Narrative Mechanics", tier: 3, color: "#a78bfa", vars: { dramatica_archetype: "Protagonist", mc_problem_element: "Equity", methodology_element: "Certainty", evaluation_element: "Proven", purpose_element: "Knowledge", narrative_invariant: "cost_and_meaning", story_outcome: "Failure", story_judgement: "Good", limit_type: "Optionlock", resolve: "Change" }},
  },
  derived: {
    basic_damage_resistance: { value: 17, formula: "(WILL×3) - (WOUND×5/2)", internal: "42 - 25 = 17" },
    social_legibility: { value: 20, formula: "(SOCIAL×3) - (proj×5/3)", internal: "30 - 10 = 20" },
    narrative_momentum: { value: 56, formula: "(DRIVE×3) + (resist×5/2)", internal: "36 + 20 = 56" },
    stress_threshold: { value: -8, formula: "(WILL×3) - (WOUND×5)", internal: "42 - 50 = -8" },
    collapse_risk: { value: 45, formula: "(WOUND×5 + shadow×5) / 2", internal: "(50+40)/2 = 45" },
    truth_exposure_index: { value: 80, formula: "(SOCIAL×3) + (12-shame)×5", internal: "30 + 50 = 80" },
  },
  flags: {
    shadow_denial: { state: "ACTIVE", trigger: "WOUND>6 AND proj>=6 AND patterns∋merit_earns_freedom" },
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
    { from: "Sun□Saturn", to: "L4 WILL", type: "texture", note: "Identity tested constantly" },
    { from: "Venus Fall", to: "L5 WOUND", type: "texture", note: "Desire crack" },
    { from: "Moon□Mars", to: "L5 WOUND", type: "trigger", note: "Crash mechanism" },
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
// STYLES
// ═══════════════════════════════════════════════════════════

const S = {
  root: { minHeight: "100vh", background: "#06080c", color: "#c9d1d9", fontFamily: "'IBM Plex Mono', 'Fira Code', 'Courier New', monospace", fontSize: 12 },
  header: { background: "linear-gradient(180deg, #0d1117 0%, #06080c 100%)", borderBottom: "1px solid #1b2230", padding: "14px 20px", position: "sticky", top: 0, zIndex: 100, display: "flex", alignItems: "center", justifyContent: "space-between" },
  brand: { fontSize: 9, letterSpacing: "0.2em", color: "#4a9eff55", marginBottom: 2 },
  title: { fontSize: 16, fontWeight: 800, color: "#e6edf3", letterSpacing: "-0.01em", margin: 0 },
  subtitle: { fontSize: 10, color: "#484f58", marginTop: 1 },
  nav: { display: "flex", gap: 2, background: "#0d1117", borderRadius: 4, padding: 2 },
  navBtn: (active) => ({ padding: "7px 14px", background: active ? "#1b2230" : "transparent", border: "none", borderRadius: 3, color: active ? "#e6edf3" : "#484f58", fontFamily: "inherit", fontSize: 10, fontWeight: active ? 700 : 400, cursor: "pointer", letterSpacing: "0.05em", transition: "all 0.2s" }),
  main: { maxWidth: 1200, margin: "0 auto", padding: "16px 20px 80px" },
  card: (color, hover) => ({ background: "#0d1117", border: `1px solid ${hover ? color + "44" : "#1b2230"}`, borderRadius: 5, padding: "12px 14px", cursor: "pointer", transition: "all 0.25s ease", position: "relative", overflow: "hidden" }),
  tierBadge: (color) => ({ display: "inline-block", fontSize: 8, fontWeight: 700, padding: "1px 6px", borderRadius: 2, background: color + "22", color: color, letterSpacing: "0.1em", marginRight: 6 }),
  sectionLabel: (color) => ({ fontSize: 9, letterSpacing: "0.18em", color: color || "#484f58", marginBottom: 8, marginTop: 20, paddingLeft: 2 }),
  tag: (color) => ({ display: "inline-block", fontSize: 9, padding: "2px 7px", borderRadius: 2, background: (color || "#484f58") + "18", color: color || "#8b949e", marginRight: 4, marginBottom: 3 }),
  statBar: (pct, color) => ({ width: "100%", height: 3, background: "#161b22", borderRadius: 2, overflow: "hidden", position: "relative" }),
  statFill: (pct, color) => ({ width: `${Math.min(Math.abs(pct), 100)}%`, height: "100%", background: color, borderRadius: 2, transition: "width 0.5s ease" }),
  flagDot: (state) => {
    const colors = { ACTIVE: "#f47067", PENDING: "#d29922", FIRED_PRE_STORY: "#8b949e", INACTIVE: "#21262d" };
    return { width: 8, height: 8, borderRadius: "50%", background: colors[state] || "#21262d", flexShrink: 0, boxShadow: state === "ACTIVE" ? `0 0 6px ${colors.ACTIVE}66` : "none" };
  },
  dignityColor: (d) => {
    const m = { Domicile: "#3fb950", Exaltation: "#56d364", Peregrine: "#8b949e", Detriment: "#f47067", Fall: "#da3633" };
    return m[d] || "#8b949e";
  },
  aspectColor: (t) => {
    const m = { Conjunction: "#4a9eff", Square: "#f47067", Opposition: "#da3633", Trine: "#3fb950", Sextile: "#56d364" };
    return m[t] || "#8b949e";
  },
  gateIcon: (g) => {
    const m = { AND: "∧", NOT: "¬", XOR: "⊕", OR: "∨" };
    return m[g] || "?";
  },
};


// ═══════════════════════════════════════════════════════════
// VIEW COMPONENTS
// ═══════════════════════════════════════════════════════════

function PipelineView() {
  const stages = [
    { id: "auth", label: "AUTHORITATIVE\nDOCUMENT", sub: "Character Bible", color: "#8b949e", icon: "◆" },
    { id: "drm", label: "DRAMATICA\nSTORYFORM", sub: "Narrative Engine", color: "#ff6b4a", icon: "⬡" },
    { id: "dit", label: "DRAMATICA\nINGEST", sub: "Template (.md)", color: "#ff6b4a", icon: "◈" },
    { id: "dai", label: "DAI\nTRANSLATION", sub: "18-Step Derivation", color: "#a78bfa", icon: "⟁" },
    { id: "ait", label: "CHARACTER\nASTROLOGY", sub: "Ingest Template (.md)", color: "#a78bfa", icon: "◉" },
    { id: "sv", label: "STEP 1\nVERIFICATION", sub: "3-Component Gate", color: "#34d399", icon: "⊕" },
    { id: "vs", label: "VERTICAL\nSLICE", sub: "12-Layer Record", color: "#34d399", icon: "▣" },
    { id: "sd", label: "STATE\nDIFFS", sub: "Narrative Overlays", color: "#fbbf24", icon: "◎" },
  ];
  const arrows = [[0,2],[1,2],[2,3],[3,4],[2,5],[4,5],[5,6],[6,7]];

  return (
    <div>
      <div style={S.sectionLabel()}>PIPELINE ARCHITECTURE</div>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 10, marginBottom: 24 }}>
        {stages.map((s, i) => (
          <div key={s.id} style={{ ...S.card(s.color, false), textAlign: "center", padding: "16px 10px" }}>
            <div style={{ fontSize: 22, color: s.color, marginBottom: 6 }}>{s.icon}</div>
            <div style={{ fontSize: 10, fontWeight: 700, color: "#e6edf3", whiteSpace: "pre-line", lineHeight: 1.3, marginBottom: 4 }}>{s.label}</div>
            <div style={{ fontSize: 9, color: "#484f58" }}>{s.sub}</div>
            <div style={{ position: "absolute", top: 4, right: 6, fontSize: 8, color: "#21262d" }}>{String(i).padStart(2, "0")}</div>
          </div>
        ))}
      </div>
      <div style={S.sectionLabel()}>FLOW SEQUENCE</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
        {[
          { id: "A", label: "Dramatica → Ingest Template", from: "Locked Storyform", to: "Dramatica Ingest (.md)", color: "#ff6b4a", steps: "8 extraction steps, 3 decision points" },
          { id: "B", label: "DAI Translation → Astrology Ingest", from: "Locked Dramatica Ingest", to: "Astrology Ingest (.md)", color: "#a78bfa", steps: "18-step derivation, 2 validation gates" },
          { id: "C", label: "Both Ingests → Vertical Slice", from: "Both Ingests + Auth Doc", to: "12-Layer Record (.md)", color: "#34d399", steps: "7 steps, 4 diagnostic checkpoints" },
          { id: "D", label: "Base Record → State Diffs", from: "Locked Base + Narrative Event", to: "State Diff Record (.md)", color: "#fbbf24", steps: "5 event categories, constraint validation" },
        ].map(f => (
          <div key={f.id} style={{ ...S.card(f.color, false), display: "flex", alignItems: "center", gap: 14, padding: "10px 14px" }}>
            <div style={{ width: 32, height: 32, borderRadius: "50%", border: `2px solid ${f.color}`, display: "flex", alignItems: "center", justifyContent: "center", color: f.color, fontWeight: 800, fontSize: 14, flexShrink: 0 }}>{f.id}</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 11, fontWeight: 700, color: "#e6edf3", marginBottom: 2 }}>{f.label}</div>
              <div style={{ fontSize: 9, color: "#484f58" }}>{f.from} → {f.to}</div>
            </div>
            <div style={{ fontSize: 9, color: f.color + "99", textAlign: "right" }}>{f.steps}</div>
          </div>
        ))}
      </div>
      <div style={{ ...S.sectionLabel(), marginTop: 24 }}>BASE 60 FOUNDATION</div>
      <div style={{ ...S.card("#4a9eff", false), padding: 14 }}>
        <div style={{ fontSize: 10, fontWeight: 700, color: "#e6edf3", marginBottom: 8 }}>DIVISOR LATTICE OF 60</div>
        <div style={{ display: "flex", justifyContent: "center", gap: 6, flexWrap: "wrap", marginBottom: 10 }}>
          {[1,2,3,4,5,6,10,12,15,20,30,60].map(d => (
            <div key={d} style={{ width: 36, height: 36, borderRadius: 3, border: `1px solid ${d === 12 ? "#4a9eff" : d === 20 ? "#ff6b4a" : "#1b2230"}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: d === 12 || d === 20 || d === 60 ? 800 : 400, color: d === 12 ? "#4a9eff" : d === 20 ? "#ff6b4a" : d === 60 ? "#34d399" : "#8b949e", background: d === 60 ? "#34d39911" : d === 12 ? "#4a9eff08" : "transparent" }}>{d}</div>
          ))}
        </div>
        <div style={{ display: "flex", gap: 12, fontSize: 9, color: "#484f58", justifyContent: "center" }}>
          <span><span style={{ color: "#4a9eff" }}>■</span> SC-12 (sub-variables)</span>
          <span><span style={{ color: "#ff6b4a" }}>■</span> SC-20 (attributes)</span>
          <span><span style={{ color: "#34d399" }}>■</span> SC-60 (internal)</span>
        </div>
      </div>
    </div>
  );
}

function LayerView({ onSelectLayer, selectedLayer }) {
  const tierGroups = [
    { tier: 1, label: "TIER 1 — FLAT", color: "#4a9eff", layers: ["CORE","VITAL","SOCIAL"] },
    { tier: 2, label: "TIER 2 — STANDARD", color: "#ff6b4a", layers: ["WILL","WOUND","DRIVE"] },
    { tier: 3, label: "TIER 3 — DEEP", color: "#a78bfa", layers: ["ORIGIN","IMPRINT","EROS","SHADOW","DESTINY","FUNC"] },
  ];

  return (
    <div>
      {tierGroups.map(tg => (
        <div key={tg.tier}>
          <div style={S.sectionLabel(tg.color)}>{tg.label}</div>
          <div style={{ display: "grid", gridTemplateColumns: tg.tier === 3 ? "repeat(3, 1fr)" : "repeat(3, 1fr)", gap: 8, marginBottom: 4 }}>
            {tg.layers.map(lk => {
              const L = VICTORIA.layers[lk];
              const isSelected = selectedLayer === lk;
              const val = L.base_value ?? L.wound_score ?? null;
              return (
                <div key={lk} onClick={() => onSelectLayer(lk)} style={{ ...S.card(tg.color, isSelected), borderColor: isSelected ? tg.color : "#1b2230" }}>
                  {isSelected && <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 2, background: tg.color }} />}
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 6 }}>
                    <div>
                      <span style={S.tierBadge(tg.color)}>T{tg.tier}</span>
                      <span style={{ fontSize: 11, fontWeight: 700, color: "#e6edf3" }}>L{tierGroups.slice(0, tg.tier - 1).reduce((a, g) => a + g.layers.length, 0) + tg.layers.indexOf(lk) + 1} {L.label}</span>
                    </div>
                    {val !== null && (
                      <div style={{ fontSize: 18, fontWeight: 800, color: tg.color, lineHeight: 1 }}>{val}</div>
                    )}
                  </div>
                  <div style={{ fontSize: 9, color: "#484f58", marginBottom: 6 }}>{L.domain}</div>
                  {val !== null && (
                    <div style={S.statBar()}>
                      <div style={S.statFill((val / (lk === "WOUND" ? 12 : 20)) * 100, tg.color)} />
                    </div>
                  )}
                  {L.vars && (
                    <div style={{ marginTop: 8, display: "flex", flexWrap: "wrap", gap: 2 }}>
                      {Object.keys(L.vars).slice(0, 4).map(k => (
                        <span key={k} style={S.tag(tg.color)}>{k}</span>
                      ))}
                      {Object.keys(L.vars).length > 4 && <span style={S.tag()}>+{Object.keys(L.vars).length - 4}</span>}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}

function LayerDetail({ layerKey }) {
  const L = VICTORIA.layers[layerKey];
  if (!L) return null;
  const tierColors = { 1: "#4a9eff", 2: "#ff6b4a", 3: "#a78bfa" };
  const color = tierColors[L.tier];
  const val = L.base_value ?? L.wound_score ?? null;
  const scale = L.tier <= 2 ? (layerKey === "WOUND" ? "SC-12" : "SC-20") : "SC-12";
  const max = layerKey === "WOUND" ? 12 : L.tier <= 2 ? 20 : 12;

  const layerFeeds = VICTORIA.feeds.filter(f => f.to.includes(L.label));
  const layerFlags = Object.entries(VICTORIA.flags).filter(([k, v]) => v.trigger.toLowerCase().includes(layerKey.toLowerCase()) || (layerKey === "WOUND" && v.trigger.includes("WOUND")) || (layerKey === "SOCIAL" && v.trigger.includes("SOCIAL")));

  return (
    <div style={{ ...S.card(color, true), borderColor: color + "44", marginTop: 12 }}>
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 2, background: color }} />
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 10 }}>
        <div>
          <span style={S.tierBadge(color)}>TIER {L.tier}</span>
          <span style={{ fontSize: 13, fontWeight: 800, color: "#e6edf3" }}>{L.label}</span>
          <div style={{ fontSize: 10, color: "#484f58", marginTop: 2 }}>{L.domain}</div>
        </div>
        {val !== null && (
          <div style={{ textAlign: "right" }}>
            <div style={{ fontSize: 28, fontWeight: 800, color, lineHeight: 1 }}>{val}</div>
            <div style={{ fontSize: 9, color: "#484f58" }}>{scale} / max {max}</div>
            {L.derivation && <div style={{ fontSize: 9, color: color + "88", marginTop: 2 }}>{L.derivation}</div>}
          </div>
        )}
      </div>

      {L.vars && (
        <>
          <div style={{ ...S.sectionLabel(color), marginTop: 12 }}>VARIABLES</div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 6 }}>
            {Object.entries(L.vars).map(([k, v]) => (
              <div key={k} style={{ background: "#161b22", borderRadius: 3, padding: "8px 10px" }}>
                <div style={{ fontSize: 9, color: color, fontWeight: 600, marginBottom: 3 }}>{k}</div>
                <div style={{ fontSize: 11, color: "#e6edf3", wordBreak: "break-word" }}>
                  {Array.isArray(v) ? v.map((item, i) => <span key={i} style={S.tag(color)}>{item}</span>) : String(v)}
                </div>
                {typeof v === "number" && (
                  <div style={{ ...S.statBar(), marginTop: 4 }}>
                    <div style={S.statFill((v / 12) * 100, color)} />
                  </div>
                )}
              </div>
            ))}
          </div>
        </>
      )}

      {layerFeeds.length > 0 && (
        <>
          <div style={{ ...S.sectionLabel("#34d399"), marginTop: 14 }}>ASTROLOGY FEEDS INTO THIS LAYER</div>
          {layerFeeds.map((f, i) => (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 8, padding: "4px 0", borderBottom: "1px solid #1b223044" }}>
              <span style={{ ...S.tag("#a78bfa"), marginBottom: 0 }}>{f.from}</span>
              <span style={{ fontSize: 9, color: "#484f58" }}>→</span>
              <span style={{ ...S.tag("#34d399"), marginBottom: 0 }}>{f.type}</span>
              <span style={{ fontSize: 9, color: "#8b949e", flex: 1 }}>{f.note}</span>
            </div>
          ))}
        </>
      )}

      {layerFlags.length > 0 && (
        <>
          <div style={{ ...S.sectionLabel("#f47067"), marginTop: 14 }}>FLAGS CONSUMING THIS LAYER</div>
          {layerFlags.map(([k, v]) => (
            <div key={k} style={{ display: "flex", alignItems: "center", gap: 8, padding: "5px 0" }}>
              <div style={S.flagDot(v.state)} />
              <span style={{ fontSize: 10, fontWeight: 600, color: "#e6edf3" }}>{k.toUpperCase()}</span>
              <span style={{ fontSize: 9, color: "#484f58" }}>{v.state}</span>
            </div>
          ))}
        </>
      )}
    </div>
  );
}

function FeedMapView() {
  const planets = ["Sun","Moon","Mercury","Venus","Mars","Saturn","Jupiter","Uranus","Neptune","Pluto","Ascendant","IC"];
  const layers = ["CORE","VITAL","SOCIAL","WILL","WOUND","DRIVE","ORIGIN","IMPRINT","EROS","SHADOW","DESTINY"];
  const planetData = {
    Sun: { sign: "Taurus", dignity: "Peregrine", color: "#fbbf24" },
    Moon: { sign: "Libra", dignity: "Peregrine", color: "#c9d1d9" },
    Mercury: { sign: "Capricorn", dignity: "Peregrine", color: "#79c0ff" },
    Venus: { sign: "Virgo", dignity: "Fall", color: "#f778ba" },
    Mars: { sign: "Capricorn", dignity: "Exaltation", color: "#f47067" },
    Saturn: { sign: "Gemini", dignity: "Detriment", color: "#8b949e" },
    Jupiter: { sign: "Sagittarius", dignity: "Domicile", color: "#d2a8ff" },
    Uranus: { sign: "Aquarius", dignity: "Domicile", color: "#39d353" },
    Neptune: { sign: "Pisces", dignity: "Domicile", color: "#6cb6ff" },
    Pluto: { sign: "Scorpio", dignity: "Domicile", color: "#f47067" },
    Ascendant: { sign: "Aries", dignity: "—", color: "#ff6b4a" },
    IC: { sign: "Cancer", dignity: "—", color: "#a78bfa" },
  };
  const layerColors = { CORE: "#4a9eff", VITAL: "#4a9eff", SOCIAL: "#4a9eff", WILL: "#ff6b4a", WOUND: "#ff6b4a", DRIVE: "#ff6b4a", ORIGIN: "#a78bfa", IMPRINT: "#a78bfa", EROS: "#a78bfa", SHADOW: "#a78bfa", DESTINY: "#a78bfa" };

  return (
    <div>
      <div style={S.sectionLabel()}>ASTROLOGY → 12-LAYER FEED MAP</div>
      <div style={{ display: "grid", gridTemplateColumns: "180px 1fr 140px", gap: 0 }}>
        <div style={{ padding: "6px 10px", fontSize: 9, color: "#484f58", borderBottom: "1px solid #1b2230", fontWeight: 700 }}>PLANET (SIGN)</div>
        <div style={{ padding: "6px 10px", fontSize: 9, color: "#484f58", borderBottom: "1px solid #1b2230", fontWeight: 700 }}>FEEDS → LAYERS</div>
        <div style={{ padding: "6px 10px", fontSize: 9, color: "#484f58", borderBottom: "1px solid #1b2230", fontWeight: 700 }}>DIGNITY</div>
        {planets.map(p => {
          const pd = planetData[p];
          const feeds = VICTORIA.feeds.filter(f => f.from.startsWith(p) || f.from.includes(p));
          return [
            <div key={p+"a"} style={{ padding: "7px 10px", borderBottom: "1px solid #0d1117", display: "flex", alignItems: "center", gap: 6 }}>
              <span style={{ color: pd.color, fontWeight: 700, fontSize: 11 }}>{p}</span>
              <span style={{ fontSize: 9, color: "#484f58" }}>{pd.sign}</span>
            </div>,
            <div key={p+"b"} style={{ padding: "7px 10px", borderBottom: "1px solid #0d1117", display: "flex", flexWrap: "wrap", gap: 3, alignItems: "center" }}>
              {feeds.map((f, i) => {
                const lk = f.to.replace(/^L\d+\s/, "");
                return (
                  <span key={i} style={{ ...S.tag(layerColors[lk] || "#484f58"), marginBottom: 0 }}>
                    {f.to} <span style={{ opacity: 0.6 }}>({f.type})</span>
                  </span>
                );
              })}
              {feeds.length === 0 && <span style={{ fontSize: 9, color: "#21262d" }}>—</span>}
            </div>,
            <div key={p+"c"} style={{ padding: "7px 10px", borderBottom: "1px solid #0d1117" }}>
              <span style={{ fontSize: 10, fontWeight: 600, color: S.dignityColor(pd.dignity) }}>{pd.dignity}</span>
            </div>
          ];
        }).flat()}
      </div>
    </div>
  );
}

function AstrologyView() {
  const A = VICTORIA.astrology;
  return (
    <div>
      <div style={S.sectionLabel("#a78bfa")}>NATAL CHART — VICTORIA MIDNIGHT</div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10, marginBottom: 16 }}>
        <div style={S.card("#a78bfa", false)}>
          <div style={{ fontSize: 10, fontWeight: 700, color: "#a78bfa", marginBottom: 8 }}>PERSONAL STACK</div>
          {Object.entries(A.personal).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0", borderBottom: "1px solid #1b223044" }}>
              <span style={{ fontWeight: 600, color: "#e6edf3", textTransform: "capitalize" }}>{k}</span>
              <div>
                <span style={{ color: "#e6edf3" }}>{v.sign}</span>
                <span style={{ marginLeft: 8, fontSize: 9, color: S.dignityColor(A.dignities[k]) }}>{A.dignities[k]}</span>
              </div>
            </div>
          ))}
        </div>
        <div style={S.card("#a78bfa", false)}>
          <div style={{ fontSize: 10, fontWeight: 700, color: "#a78bfa", marginBottom: 8 }}>STRUCTURAL STACK</div>
          {Object.entries(A.structural).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0", borderBottom: "1px solid #1b223044" }}>
              <span style={{ fontWeight: 600, color: "#e6edf3", textTransform: "capitalize" }}>{k}</span>
              <div>
                <span style={{ color: "#e6edf3" }}>{v.sign}</span>
                <span style={{ marginLeft: 8, fontSize: 9, color: S.dignityColor(A.dignities[k]) }}>{A.dignities[k]}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10, marginBottom: 16 }}>
        <div style={S.card("#ff6b4a", false)}>
          <div style={{ fontSize: 10, fontWeight: 700, color: "#ff6b4a", marginBottom: 8 }}>ANGLES</div>
          {Object.entries(A.angles).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0", borderBottom: "1px solid #1b223044" }}>
              <span style={{ fontWeight: 600, color: "#e6edf3", textTransform: "capitalize" }}>{k}</span>
              <span style={{ color: "#e6edf3" }}>{v}</span>
            </div>
          ))}
        </div>
        <div style={S.card("#34d399", false)}>
          <div style={{ fontSize: 10, fontWeight: 700, color: "#34d399", marginBottom: 8 }}>HOUSES</div>
          {Object.entries(A.houses).map(([k, v]) => (
            <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "4px 0", borderBottom: "1px solid #1b223044" }}>
              <span style={{ fontWeight: 600, color: "#e6edf3", textTransform: "capitalize" }}>{k}</span>
              <span style={{ color: "#34d399" }}>H{v} <span style={{ fontSize: 9, color: "#484f58" }}>{[1,4,7,10].includes(v) ? "angular" : [2,5,8,11].includes(v) ? "succedent" : "cadent"}</span></span>
            </div>
          ))}
        </div>
      </div>

      <div style={S.sectionLabel("#f47067")}>ASPECT MAP (LOGIC GATES)</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
        {A.aspects.map((asp, i) => (
          <div key={i} style={{ ...S.card(S.aspectColor(asp.type), false), display: "flex", alignItems: "center", gap: 10, padding: "8px 12px" }}>
            <span style={{ fontWeight: 700, color: "#e6edf3", width: 70 }}>{asp.a}</span>
            <span style={{ fontSize: 16, fontWeight: 800, color: S.aspectColor(asp.type), width: 24, textAlign: "center" }}>{S.gateIcon(asp.gate)}</span>
            <span style={{ fontWeight: 700, color: "#e6edf3", width: 70 }}>{asp.b}</span>
            <span style={{ ...S.tag(S.aspectColor(asp.type)), marginBottom: 0 }}>{asp.type}</span>
            <span style={{ ...S.tag(), marginBottom: 0 }}>{asp.gate}</span>
            <span style={{ fontSize: 9, color: "#8b949e", flex: 1 }}>{asp.fn}</span>
          </div>
        ))}
      </div>
      <div style={{ marginTop: 10, fontSize: 9, color: "#484f58", padding: "0 2px" }}>
        5 hard aspects (■ Square ■ Opposition) / 1 conjunction / 1 trine — high-friction chart. Growth is forced, not invited.
      </div>
    </div>
  );
}

function DerivedView() {
  const D = VICTORIA.derived;
  const F = VICTORIA.flags;
  const maxInternal = 60;

  return (
    <div>
      <div style={S.sectionLabel("#34d399")}>DERIVED STATISTICS (INTERNAL 0-60 SPACE)</div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, marginBottom: 20 }}>
        {Object.entries(D).map(([k, v]) => {
          const isNeg = v.value < 0;
          const isOver = v.value > 60;
          const pct = isOver ? 100 : isNeg ? 0 : (v.value / maxInternal) * 100;
          const color = isNeg ? "#f47067" : isOver ? "#d29922" : v.value > 45 ? "#3fb950" : v.value > 20 ? "#4a9eff" : "#8b949e";
          return (
            <div key={k} style={S.card(color, false)}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 6 }}>
                <div style={{ fontSize: 10, fontWeight: 700, color: "#e6edf3" }}>{k.replace(/_/g, " ").toUpperCase()}</div>
                <div style={{ fontSize: 22, fontWeight: 800, color, lineHeight: 1 }}>{v.value}</div>
              </div>
              <div style={S.statBar()}>
                <div style={S.statFill(pct, color)} />
              </div>
              <div style={{ fontSize: 9, color: "#484f58", marginTop: 6 }}>{v.formula}</div>
              <div style={{ fontSize: 9, color: color + "88", marginTop: 2 }}>{v.internal}</div>
              {isNeg && <div style={{ fontSize: 9, color: "#f47067", marginTop: 4, fontWeight: 600 }}>⚠ NEGATIVE — Operating past structural limit</div>}
              {isOver && <div style={{ fontSize: 9, color: "#d29922", marginTop: 4, fontWeight: 600 }}>⚠ EXCEEDS BASE UNIT — Signal beyond containment</div>}
            </div>
          );
        })}
      </div>

      <div style={S.sectionLabel("#f47067")}>STATUS FLAGS</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
        {Object.entries(F).map(([k, v]) => {
          const stateColors = { ACTIVE: "#f47067", PENDING: "#d29922", FIRED_PRE_STORY: "#8b949e", INACTIVE: "#21262d" };
          const sc = stateColors[v.state];
          return (
            <div key={k} style={{ ...S.card(sc, false), display: "flex", alignItems: "center", gap: 12, padding: "10px 14px" }}>
              <div style={S.flagDot(v.state)} />
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: "#e6edf3" }}>{k.replace(/_/g, " ").toUpperCase()}</div>
                <div style={{ fontSize: 9, color: "#484f58", marginTop: 2 }}>{v.trigger}</div>
              </div>
              <div style={{ fontSize: 10, fontWeight: 600, color: sc, letterSpacing: "0.05em" }}>{v.state}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}


// ═══════════════════════════════════════════════════════════
// MAIN APPLICATION
// ═══════════════════════════════════════════════════════════

export default function LeechseedExplorer() {
  const [view, setView] = useState("pipeline");
  const [selectedLayer, setSelectedLayer] = useState(null);

  const views = [
    { id: "pipeline", label: "PIPELINE" },
    { id: "layers", label: "LAYERS" },
    { id: "astrology", label: "ASTROLOGY" },
    { id: "feeds", label: "FEED MAP" },
    { id: "derived", label: "STATS & FLAGS" },
  ];

  return (
    <div style={S.root}>
      <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet" />

      <div style={S.header}>
        <div>
          <div style={S.brand}>LEECHSEED // 02_CHARACTER_SYSTEMS</div>
          <h1 style={{ ...S.title, fontFamily: "'DM Sans', sans-serif" }}>System Explorer</h1>
          <div style={S.subtitle}>Victoria "Tori" Midnight — OVEREXITOUT — v1.0.0 LOCKED</div>
        </div>
        <nav style={S.nav}>
          {views.map(v => (
            <button key={v.id} onClick={() => { setView(v.id); if (v.id !== "layers") setSelectedLayer(null); }} style={S.navBtn(view === v.id)}>
              {v.label}
            </button>
          ))}
        </nav>
      </div>

      <div style={S.main}>
        {view === "pipeline" && <PipelineView />}
        {view === "layers" && (
          <>
            <LayerView onSelectLayer={(lk) => setSelectedLayer(selectedLayer === lk ? null : lk)} selectedLayer={selectedLayer} />
            {selectedLayer && <LayerDetail layerKey={selectedLayer} />}
          </>
        )}
        {view === "astrology" && <AstrologyView />}
        {view === "feeds" && <FeedMapView />}
        {view === "derived" && <DerivedView />}
      </div>

      <div style={{ position: "fixed", bottom: 0, left: 0, right: 0, background: "linear-gradient(0deg, #06080c 0%, transparent 100%)", height: 40, pointerEvents: "none" }} />
    </div>
  );
}
