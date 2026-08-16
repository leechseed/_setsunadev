---
original_path: "/mnt/user-data/outputs/dramatica_ingest_mission_control.jsx"
source_conversation: "Character database system architecture with Dramatica and astrology integration"
created: 2026-02-25
trunk: BLACK
kind: generated-file
---

import { useState, useEffect, useCallback } from "react";

const SECTIONS = [
  {
    id: "header",
    name: "HEADER",
    subtitle: "Identity Lock",
    fields: ["character_id", "character_name", "ip", "storyform_id", "storyform_version", "storyform_status", "completed_by", "completion_date"],
    xp: 50,
    icon: "◆",
    tier: "foundation",
  },
  {
    id: "dynamics",
    name: "STORYFORM DYNAMICS",
    subtitle: "Global Constants",
    fields: ["story_outcome", "story_judgement", "story_driver", "story_limit", "story_goal", "story_consequence", "story_cost", "story_dividend", "story_forewarnings", "story_prerequisites", "story_preconditions", "story_requirements"],
    xp: 120,
    icon: "⬡",
    tier: "critical",
  },
  {
    id: "structural_role",
    name: "STRUCTURAL ROLE",
    subtitle: "Character Binding",
    fields: ["structural_role", "dramatica_archetype", "resolve", "growth", "approach", "mental_sex"],
    xp: 80,
    icon: "◈",
    tier: "critical",
  },
  {
    id: "element_quads",
    name: "ELEMENT QUADS",
    subtitle: "Behavioral Mechanics",
    fields: ["motivation_primary", "motivation_secondary", "methodology_primary", "methodology_secondary", "evaluation_primary", "evaluation_secondary", "purpose_primary", "purpose_secondary", "structural_meaning"],
    xp: 100,
    icon: "▣",
    tier: "critical",
  },
  {
    id: "mc_throughline",
    name: "MC THROUGHLINE",
    subtitle: "Main Character Spine",
    fields: ["mc_domain", "mc_concern", "mc_issue", "mc_counterpoint", "mc_problem", "mc_solution", "mc_symptom", "mc_response", "mc_unique_ability", "mc_critical_flaw", "mc_benchmark", "mc_focus", "mc_direction", "mc_signpost_1", "mc_signpost_2", "mc_signpost_3", "mc_signpost_4"],
    xp: 180,
    icon: "◉",
    tier: "throughline",
    conditional: true,
    condition_label: "IF MC",
  },
  {
    id: "ic_throughline",
    name: "IC THROUGHLINE",
    subtitle: "Impact Character Spine",
    fields: ["ic_domain", "ic_concern", "ic_issue", "ic_counterpoint", "ic_problem", "ic_solution", "ic_symptom", "ic_response", "ic_unique_ability", "ic_critical_flaw", "ic_benchmark", "ic_focus", "ic_direction", "ic_signpost_1", "ic_signpost_2", "ic_signpost_3", "ic_signpost_4"],
    xp: 180,
    icon: "◎",
    tier: "throughline",
    conditional: true,
    condition_label: "IF IC",
  },
  {
    id: "os_throughline",
    name: "OS THROUGHLINE",
    subtitle: "Overall Story",
    fields: ["os_domain", "os_concern", "os_issue", "os_counterpoint", "os_problem", "os_solution", "os_symptom", "os_response", "os_catalyst", "os_inhibitor", "os_benchmark", "os_signpost_1", "os_signpost_2", "os_signpost_3", "os_signpost_4"],
    xp: 160,
    icon: "⬢",
    tier: "throughline",
  },
  {
    id: "rs_throughline",
    name: "RS THROUGHLINE",
    subtitle: "Relationship Story",
    fields: ["rs_domain", "rs_concern", "rs_issue", "rs_counterpoint", "rs_problem", "rs_solution", "rs_catalyst", "rs_inhibitor", "rs_benchmark", "rs_signpost_1", "rs_signpost_2", "rs_signpost_3", "rs_signpost_4", "rs_partner"],
    xp: 150,
    icon: "⬡",
    tier: "throughline",
    conditional: true,
    condition_label: "IF RS PRINCIPAL",
  },
  {
    id: "relationships",
    name: "RELATIONSHIPS",
    subtitle: "OS Character Map",
    fields: ["relationship_entries"],
    xp: 60,
    icon: "⟁",
    tier: "network",
    freeform: true,
  },
  {
    id: "invariants",
    name: "NARRATIVE INVARIANTS",
    subtitle: "Structural Laws",
    fields: ["invariant_entries"],
    xp: 100,
    icon: "⊘",
    tier: "authored",
    freeform: true,
  },
  {
    id: "handoff",
    name: "HANDOFF CHECKLIST",
    subtitle: "Lock Gate",
    fields: ["all_storyform_populated", "all_authored_completed", "structural_meaning_written", "invariants_defined", "l12_core_matches", "astrology_can_proceed", "status_locked", "placed_in_canonical"],
    xp: 200,
    icon: "⊕",
    tier: "gate",
  },
];

const TIER_COLORS = {
  foundation: { bg: "#1a2332", accent: "#4a9eff", glow: "rgba(74,158,255,0.15)" },
  critical: { bg: "#1a2332", accent: "#ff6b4a", glow: "rgba(255,107,74,0.15)" },
  throughline: { bg: "#1a2332", accent: "#a78bfa", glow: "rgba(167,139,250,0.15)" },
  network: { bg: "#1a2332", accent: "#34d399", glow: "rgba(52,211,153,0.15)" },
  authored: { bg: "#1a2332", accent: "#fbbf24", glow: "rgba(251,191,36,0.15)" },
  gate: { bg: "#1a2332", accent: "#f472b6", glow: "rgba(244,114,182,0.15)" },
};

const RANK_THRESHOLDS = [
  { min: 0, label: "UNINITIALIZED", color: "#555" },
  { min: 50, label: "INTAKE STARTED", color: "#4a9eff" },
  { min: 200, label: "FOUNDATION SET", color: "#34d399" },
  { min: 500, label: "SPINE FORMING", color: "#a78bfa" },
  { min: 800, label: "THROUGHLINES MAPPED", color: "#fbbf24" },
  { min: 1100, label: "NEAR COMPLETE", color: "#ff6b4a" },
  { min: 1380, label: "LOCK READY", color: "#f472b6" },
];

function getRank(xp) {
  let rank = RANK_THRESHOLDS[0];
  for (const t of RANK_THRESHOLDS) {
    if (xp >= t.min) rank = t;
  }
  return rank;
}

function ProgressBar({ value, max, color, height = 4 }) {
  const pct = Math.min((value / max) * 100, 100);
  return (
    <div style={{ width: "100%", height, background: "#0d1117", borderRadius: 2, overflow: "hidden" }}>
      <div
        style={{
          width: `${pct}%`,
          height: "100%",
          background: `linear-gradient(90deg, ${color}, ${color}88)`,
          borderRadius: 2,
          transition: "width 0.6s cubic-bezier(0.22, 1, 0.36, 1)",
        }}
      />
    </div>
  );
}

function SectionCard({ section, data, skipped, onToggleField, onToggleSkip, onUpdateFreeform, isExpanded, onToggleExpand }) {
  const tc = TIER_COLORS[section.tier];
  const isSkipped = skipped;

  let completed = 0;
  let total = section.fields.length;

  if (section.freeform) {
    const content = data[section.fields[0]] || "";
    completed = content.trim().length > 0 ? 1 : 0;
    total = 1;
  } else if (section.id === "handoff") {
    completed = section.fields.filter((f) => data[f]).length;
  } else {
    completed = section.fields.filter((f) => data[f]).length;
  }

  const pct = isSkipped ? 100 : total > 0 ? Math.round((completed / total) * 100) : 0;
  const earnedXP = isSkipped ? section.xp : Math.round((completed / total) * section.xp);
  const sectionStatus = isSkipped ? "SKIPPED" : pct === 100 ? "COMPLETE" : pct > 0 ? "IN PROGRESS" : "EMPTY";

  const statusColor =
    sectionStatus === "COMPLETE" ? "#34d399" : sectionStatus === "SKIPPED" ? "#666" : sectionStatus === "IN PROGRESS" ? tc.accent : "#333";

  return (
    <div
      style={{
        background: isSkipped ? "#0d1117" : tc.bg,
        border: `1px solid ${isSkipped ? "#1a1a1a" : pct === 100 ? tc.accent + "44" : "#1e293b"}`,
        borderRadius: 6,
        marginBottom: 8,
        opacity: isSkipped ? 0.5 : 1,
        transition: "all 0.3s ease",
        overflow: "hidden",
      }}
    >
      <div
        onClick={onToggleExpand}
        style={{
          padding: "12px 16px",
          cursor: "pointer",
          display: "flex",
          alignItems: "center",
          gap: 12,
          userSelect: "none",
        }}
      >
        <span style={{ fontSize: 18, color: tc.accent, width: 24, textAlign: "center", flexShrink: 0 }}>{section.icon}</span>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span style={{ fontFamily: "'JetBrains Mono', 'Fira Code', monospace", fontSize: 12, fontWeight: 700, color: "#e2e8f0", letterSpacing: "0.05em" }}>
              {section.name}
            </span>
            {section.conditional && (
              <span
                style={{
                  fontSize: 9,
                  padding: "1px 6px",
                  borderRadius: 3,
                  background: tc.accent + "22",
                  color: tc.accent,
                  fontFamily: "monospace",
                  letterSpacing: "0.05em",
                }}
              >
                {section.condition_label}
              </span>
            )}
          </div>
          <div style={{ fontSize: 10, color: "#64748b", fontFamily: "monospace", marginTop: 2 }}>{section.subtitle}</div>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 12, flexShrink: 0 }}>
          <span style={{ fontFamily: "monospace", fontSize: 11, color: statusColor, fontWeight: 600 }}>{sectionStatus}</span>
          <span style={{ fontFamily: "monospace", fontSize: 10, color: tc.accent + "aa" }}>+{earnedXP}xp</span>
          <div style={{ width: 60 }}>
            <ProgressBar value={completed} max={total} color={tc.accent} />
          </div>
          <span style={{ fontSize: 12, color: "#475569", transform: isExpanded ? "rotate(180deg)" : "rotate(0)", transition: "transform 0.2s" }}>▼</span>
        </div>
      </div>

      {isExpanded && (
        <div style={{ padding: "0 16px 14px 52px", borderTop: "1px solid #1e293b" }}>
          {section.conditional && (
            <div style={{ marginTop: 10, marginBottom: 8 }}>
              <label
                style={{ display: "flex", alignItems: "center", gap: 8, cursor: "pointer", fontSize: 11, color: "#94a3b8", fontFamily: "monospace" }}
              >
                <input
                  type="checkbox"
                  checked={isSkipped}
                  onChange={onToggleSkip}
                  style={{ accentColor: tc.accent }}
                />
                N/A — Character does not hold this role
              </label>
            </div>
          )}

          {!isSkipped && section.freeform && (
            <div style={{ marginTop: 10 }}>
              <textarea
                value={data[section.fields[0]] || ""}
                onChange={(e) => onUpdateFreeform(section.fields[0], e.target.value)}
                placeholder={section.id === "relationships" ? "Partner | Dynamic | Type | Notes (one per line)" : "ID | Statement | Derived From (one per line)"}
                rows={4}
                style={{
                  width: "100%",
                  background: "#0d1117",
                  border: "1px solid #1e293b",
                  borderRadius: 4,
                  color: "#e2e8f0",
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  padding: 10,
                  resize: "vertical",
                  outline: "none",
                  boxSizing: "border-box",
                }}
              />
            </div>
          )}

          {!isSkipped && !section.freeform && (
            <div style={{ marginTop: 10, display: "grid", gridTemplateColumns: "1fr 1fr", gap: "4px 16px" }}>
              {section.fields.map((field) => (
                <label
                  key={field}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 8,
                    padding: "4px 0",
                    cursor: "pointer",
                    fontSize: 11,
                    color: data[field] ? "#e2e8f0" : "#475569",
                    fontFamily: "'JetBrains Mono', monospace",
                    transition: "color 0.2s",
                  }}
                >
                  <input
                    type="checkbox"
                    checked={!!data[field]}
                    onChange={() => onToggleField(field)}
                    style={{ accentColor: tc.accent, flexShrink: 0 }}
                  />
                  <span style={{ textDecoration: data[field] ? "none" : "none", opacity: data[field] ? 1 : 0.6 }}>
                    {field}
                  </span>
                </label>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default function DramaticaIngestMissionControl() {
  const [characterName, setCharacterName] = useState("");
  const [fieldData, setFieldData] = useState({});
  const [skippedSections, setSkippedSections] = useState({});
  const [expandedSections, setExpandedSections] = useState({});
  const [loaded, setLoaded] = useState(false);
  const [showLockModal, setShowLockModal] = useState(false);
  const [isLocked, setIsLocked] = useState(false);

  // Load from storage
  useEffect(() => {
    async function load() {
      try {
        const result = await window.storage.get("dramatica-ingest-state");
        if (result && result.value) {
          const parsed = JSON.parse(result.value);
          setFieldData(parsed.fieldData || {});
          setSkippedSections(parsed.skippedSections || {});
          setCharacterName(parsed.characterName || "");
          setIsLocked(parsed.isLocked || false);
        }
      } catch (e) {
        // No saved state
      }
      setLoaded(true);
    }
    load();
  }, []);

  // Save to storage
  const save = useCallback(async (fd, ss, cn, il) => {
    try {
      await window.storage.set("dramatica-ingest-state", JSON.stringify({
        fieldData: fd,
        skippedSections: ss,
        characterName: cn,
        isLocked: il,
      }));
    } catch (e) {
      // Silent fail
    }
  }, []);

  useEffect(() => {
    if (loaded) save(fieldData, skippedSections, characterName, isLocked);
  }, [fieldData, skippedSections, characterName, isLocked, loaded, save]);

  const toggleField = (field) => {
    if (isLocked) return;
    setFieldData((prev) => ({ ...prev, [field]: !prev[field] }));
  };

  const toggleSkip = (sectionId) => {
    if (isLocked) return;
    setSkippedSections((prev) => ({ ...prev, [sectionId]: !prev[sectionId] }));
  };

  const updateFreeform = (field, value) => {
    if (isLocked) return;
    setFieldData((prev) => ({ ...prev, [field]: value }));
  };

  const toggleExpand = (sectionId) => {
    setExpandedSections((prev) => ({ ...prev, [sectionId]: !prev[sectionId] }));
  };

  // Calculate totals
  let totalXP = 0;
  let maxXP = 0;
  let completeSections = 0;
  let activeSections = 0;

  SECTIONS.forEach((s) => {
    const isSkipped = skippedSections[s.id];
    maxXP += s.xp;

    if (isSkipped) {
      totalXP += s.xp;
      completeSections++;
      activeSections++;
      return;
    }

    activeSections++;
    let completed = 0;
    let total = s.fields.length;

    if (s.freeform) {
      const content = fieldData[s.fields[0]] || "";
      completed = content.trim().length > 0 ? 1 : 0;
      total = 1;
    } else {
      completed = s.fields.filter((f) => fieldData[f]).length;
    }

    const earned = total > 0 ? Math.round((completed / total) * s.xp) : 0;
    totalXP += earned;
    if (total > 0 && completed === total) completeSections++;
  });

  const rank = getRank(totalXP);
  const overallPct = maxXP > 0 ? Math.round((totalXP / maxXP) * 100) : 0;
  const canLock = completeSections === activeSections && totalXP === maxXP;

  const handleReset = async () => {
    setFieldData({});
    setSkippedSections({});
    setCharacterName("");
    setIsLocked(false);
    setExpandedSections({});
    try { await window.storage.delete("dramatica-ingest-state"); } catch(e) {}
  };

  if (!loaded) {
    return (
      <div style={{ minHeight: "100vh", background: "#0a0e14", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <span style={{ color: "#4a9eff", fontFamily: "monospace", fontSize: 14 }}>LOADING STATE...</span>
      </div>
    );
  }

  return (
    <div style={{ minHeight: "100vh", background: "#0a0e14", color: "#e2e8f0", fontFamily: "'Segoe UI', system-ui, sans-serif", padding: "0" }}>
      {/* Header */}
      <div
        style={{
          background: "linear-gradient(180deg, #0f1520 0%, #0a0e14 100%)",
          borderBottom: "1px solid #1e293b",
          padding: "20px 24px",
          position: "sticky",
          top: 0,
          zIndex: 100,
        }}
      >
        <div style={{ maxWidth: 800, margin: "0 auto" }}>
          <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", marginBottom: 14 }}>
            <div>
              <div style={{ fontFamily: "'JetBrains Mono', 'Fira Code', monospace", fontSize: 10, color: "#4a9eff", letterSpacing: "0.15em", marginBottom: 4 }}>
                LEECHSEED // PHASE 1 // DELIVERABLE 1D
              </div>
              <h1 style={{ margin: 0, fontSize: 20, fontWeight: 800, letterSpacing: "-0.02em", color: "#f1f5f9" }}>
                DRAMATICA INGEST
              </h1>
              <div style={{ fontSize: 11, color: "#64748b", marginTop: 2, fontFamily: "monospace" }}>Mission Control — Source Verification Protocol</div>
            </div>
            <div style={{ textAlign: "right" }}>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 28,
                  fontWeight: 800,
                  color: rank.color,
                  lineHeight: 1,
                  textShadow: `0 0 20px ${rank.color}44`,
                }}
              >
                {totalXP}
                <span style={{ fontSize: 12, color: "#64748b", fontWeight: 400 }}> / {maxXP} XP</span>
              </div>
              <div
                style={{
                  fontFamily: "monospace",
                  fontSize: 10,
                  color: rank.color,
                  letterSpacing: "0.1em",
                  marginTop: 2,
                }}
              >
                {rank.label}
              </div>
            </div>
          </div>

          {/* Character Name Input */}
          <div style={{ marginBottom: 12 }}>
            <input
              type="text"
              value={characterName}
              onChange={(e) => !isLocked && setCharacterName(e.target.value)}
              placeholder="CHARACTER NAME"
              disabled={isLocked}
              style={{
                width: "100%",
                background: "#0d1117",
                border: "1px solid #1e293b",
                borderRadius: 4,
                color: "#e2e8f0",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 13,
                fontWeight: 700,
                padding: "8px 12px",
                outline: "none",
                letterSpacing: "0.05em",
                boxSizing: "border-box",
              }}
            />
          </div>

          {/* Overall Progress */}
          <ProgressBar value={totalXP} max={maxXP} color={rank.color} height={6} />
          <div style={{ display: "flex", justifyContent: "space-between", marginTop: 6 }}>
            <span style={{ fontFamily: "monospace", fontSize: 10, color: "#64748b" }}>
              {completeSections}/{activeSections} SECTIONS — {overallPct}%
            </span>
            <span style={{ fontFamily: "monospace", fontSize: 10, color: isLocked ? "#34d399" : canLock ? "#f472b6" : "#333" }}>
              {isLocked ? "◆ LOCKED" : canLock ? "◆ LOCK READY" : "◇ DRAFT"}
            </span>
          </div>
        </div>
      </div>

      {/* Sections */}
      <div style={{ maxWidth: 800, margin: "0 auto", padding: "16px 24px 100px" }}>
        {/* Tier Labels */}
        {["foundation", "critical", "throughline", "network", "authored", "gate"].map((tier) => {
          const tierSections = SECTIONS.filter((s) => s.tier === tier);
          if (tierSections.length === 0) return null;
          const tierLabels = {
            foundation: "FOUNDATION",
            critical: "CRITICAL PATH",
            throughline: "THROUGHLINES",
            network: "NETWORK",
            authored: "AUTHORED",
            gate: "LOCK GATE",
          };
          return (
            <div key={tier} style={{ marginBottom: 4 }}>
              <div
                style={{
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 9,
                  color: TIER_COLORS[tier].accent + "88",
                  letterSpacing: "0.2em",
                  marginBottom: 6,
                  marginTop: 16,
                  paddingLeft: 2,
                }}
              >
                {tierLabels[tier]}
              </div>
              {tierSections.map((section) => (
                <SectionCard
                  key={section.id}
                  section={section}
                  data={fieldData}
                  skipped={skippedSections[section.id]}
                  onToggleField={toggleField}
                  onToggleSkip={() => toggleSkip(section.id)}
                  onUpdateFreeform={updateFreeform}
                  isExpanded={expandedSections[section.id]}
                  onToggleExpand={() => toggleExpand(section.id)}
                />
              ))}
            </div>
          );
        })}

        {/* Lock / Reset Controls */}
        <div style={{ display: "flex", gap: 10, marginTop: 20 }}>
          {!isLocked && (
            <button
              onClick={() => canLock && setShowLockModal(true)}
              disabled={!canLock}
              style={{
                flex: 1,
                padding: "14px 20px",
                background: canLock ? "linear-gradient(135deg, #f472b6, #a78bfa)" : "#1a1a1a",
                border: canLock ? "1px solid #f472b6" : "1px solid #1e293b",
                borderRadius: 6,
                color: canLock ? "#0a0e14" : "#333",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 13,
                fontWeight: 800,
                letterSpacing: "0.1em",
                cursor: canLock ? "pointer" : "not-allowed",
                transition: "all 0.3s",
              }}
            >
              {canLock ? "⊕ EXECUTE LOCK PROTOCOL" : "⊘ LOCK UNAVAILABLE — SECTIONS INCOMPLETE"}
            </button>
          )}
          {isLocked && (
            <div
              style={{
                flex: 1,
                padding: "14px 20px",
                background: "#0d1117",
                border: "1px solid #34d399",
                borderRadius: 6,
                textAlign: "center",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 13,
                fontWeight: 800,
                color: "#34d399",
                letterSpacing: "0.1em",
              }}
            >
              ◆ TEMPLATE LOCKED — {characterName || "UNNAMED"} — {new Date().toISOString().split("T")[0]}
            </div>
          )}
          <button
            onClick={handleReset}
            style={{
              padding: "14px 16px",
              background: "#0d1117",
              border: "1px solid #1e293b",
              borderRadius: 6,
              color: "#475569",
              fontFamily: "monospace",
              fontSize: 10,
              cursor: "pointer",
              letterSpacing: "0.1em",
            }}
          >
            RESET
          </button>
        </div>
      </div>

      {/* Lock Confirmation Modal */}
      {showLockModal && (
        <div
          style={{
            position: "fixed",
            inset: 0,
            background: "rgba(0,0,0,0.85)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 1000,
          }}
          onClick={() => setShowLockModal(false)}
        >
          <div
            onClick={(e) => e.stopPropagation()}
            style={{
              background: "#0f1520",
              border: "1px solid #f472b6",
              borderRadius: 8,
              padding: 32,
              maxWidth: 420,
              width: "90%",
              textAlign: "center",
            }}
          >
            <div style={{ fontSize: 36, marginBottom: 12 }}>⊕</div>
            <h2 style={{ margin: "0 0 8px", fontFamily: "'JetBrains Mono', monospace", fontSize: 16, color: "#f472b6" }}>LOCK CONFIRMATION</h2>
            <p style={{ fontSize: 12, color: "#94a3b8", lineHeight: 1.6, margin: "0 0 20px", fontFamily: "monospace" }}>
              Locking {characterName || "this character"}'s Dramatica Ingest Template.
              <br />
              Once locked, this document becomes the canonical source for L12 population and Character Astrology derivation.
              <br /><br />
              Changes after lock require a new version number.
            </p>
            <div style={{ display: "flex", gap: 10 }}>
              <button
                onClick={() => setShowLockModal(false)}
                style={{
                  flex: 1,
                  padding: "10px",
                  background: "transparent",
                  border: "1px solid #1e293b",
                  borderRadius: 4,
                  color: "#64748b",
                  fontFamily: "monospace",
                  fontSize: 11,
                  cursor: "pointer",
                }}
              >
                ABORT
              </button>
              <button
                onClick={() => {
                  setIsLocked(true);
                  setShowLockModal(false);
                }}
                style={{
                  flex: 1,
                  padding: "10px",
                  background: "#f472b6",
                  border: "1px solid #f472b6",
                  borderRadius: 4,
                  color: "#0a0e14",
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                  fontWeight: 800,
                  cursor: "pointer",
                  letterSpacing: "0.05em",
                }}
              >
                CONFIRM LOCK
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
