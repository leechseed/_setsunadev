# INTERNAL SYSTEMS TRANSFER REPORT

**Subject**: Narrative Chemistry Engine – Phase 0 Progress Dossier  
**Prepared by**: Narrative Systems Lead (Outgoing), FLUBBERGLAM OPS  
**Date**: 2025-04-12  
**Purpose**: Orientation brief for incoming systems architect

---

## 🧠 Project Summary

The **Narrative Chemistry Engine (NCE)** is an internal, non-commercial simulation system designed to support a multidisciplinary creator’s long-form intellectual property projects. It simulates character psychology, emotional chemistry, and social dynamics with the goal of generating scene events, relationship shifts, and markdown-based narrative logs.

This engine is a **creative infrastructure platform**, not a game. It is meant to become a modular narrative OS, eventually interfacing with future systems for plot arcs, dialogue engines, and world simulation tools.

---

## 🧩 System Design Philosophy

- **Creator-Centric**: Built for authors, not engineers
- **Narrative-First**: Characters are defined by emotion, memory, motive—not just stats
- **Simulation-Based**: The engine "ticks" through relationship changes, emotional states, and scene triggers
- **Extensible**: Designed like a DAW, with plugins/modules (e.g., character editor, scene generator)
- **Portable**: SQLite-powered for local control; markdown logs for long-term creative archival

---

## ✅ Phase 0 Progress Checklist

| Phase                         | Description                                                                 | Status         |
| ----------------------------- | --------------------------------------------------------------------------- | -------------- |
| 0.1 – Vision Statement        | Project goal and reason for existence defined                               | ✅ Complete    |
| 0.2 – User Archetype          | Identified primary user as a cross-platform IP developer                    | ✅ Complete    |
| 0.3 – Competitive Rejection   | Audited and rejected existing tooling (Obsidian, Notion, World Anvil, etc.) | ✅ Complete    |
| 0.4 – System Framing (Part 1) | Drafted Character entity schema; awaiting final field confirmation          | 🟡 In Progress |

---

## 🔍 Current Character Entity (Draft)

| Field             | Type       | Notes                                   |
| ----------------- | ---------- | --------------------------------------- |
| `id`              | INTEGER    | Primary key                             |
| `name`            | TEXT       | Character’s name                        |
| `age`             | INTEGER    | Can be approximate or precise           |
| `traits`          | TEXT (CSV) | ["jealous", "loyal", "ambitious"]       |
| `emotional_state` | TEXT       | Current mood (e.g., "angry", "hopeful") |
| `tags`            | TEXT (CSV) | ["main character", "rebel", "undead"]   |
| `notes`           | TEXT       | Freeform notes or biography             |

> Incoming lead should confirm this structure before moving on to Traits and Relationship systems.

---

## 🔮 Next Steps for Incoming Systems Lead

### 1. **Finalize Character Entity**

- Confirm or adjust schema
- Define whether traits will be stored as CSV, JSON, or a join table (see “Trait Management” note below)

### 2. **Begin Trait System**

- Define Trait structure:
  - `id`, `name`, `category`, `modifier_value`, `duration`, etc.
- Decide on permanent vs. temporary traits
- Establish trait influence rules (what they modify or trigger)

### 3. **Design Relationship Model**

- Suggested fields:
  - `id`, `source_id`, `target_id`, `type`, `trust`, `tension`, `intimacy`, `history_log`
- Plan for relationship mutation via event triggers

### 4. **Set Up Schema in SQLite**

- Create `characters`, `traits`, `relationships` tables
- Optional: Set up foreign key structure if using join tables for many-to-many links

### 5. **Godot Integration Phase 0**

- Install **Godot 4.x**
- Install **godot-sqlite** plugin
- Create basic tick manager (advance time → evaluate conditions)
- Test DB queries and relationship updates via GDScript

### 6. **Begin Logging Layer**

- Markdown-based event log
- Human-readable scene output with causal metadata
- Format:  
  `Day 12: Alice betrayed Bob. Cause: Jealousy + Low Trust (<40). Effect: Trust -25, State: Alice = "satisfied", Bob = "furious"`

---

## ⚠️ Known Constraints / Pending Decisions

| Topic                    | Status | Notes                                             |
| ------------------------ | ------ | ------------------------------------------------- |
| Trait storage format     | ❓     | CSV vs. JSON vs. relational table                 |
| Scene generator logic    | ❓     | Will be needed to produce natural language blurbs |
| DSL / Event rules format | ❓     | Suggested JSON with condition + effect            |
| Tick pacing              | ⏳     | TBD: real-time vs. step-based                     |

---

## 🗃 Toolchain Status

| Tool                      | Purpose                       | Status                      |
| ------------------------- | ----------------------------- | --------------------------- |
| **Godot 4.x**             | Simulation UI + logic         | 🔜 Ready to install         |
| **SQLite**                | Character + relationship data | ✅ Ready (world.db planned) |
| **DB Browser for SQLite** | Easy schema editing           | ✅ Installed                |
| **Markdown Export**       | Log/report generation         | 🔜 Planned                  |

---

## 🤝 Strategic Recommendations

- Maintain **slow, modular development**: one concept at a time, thoroughly understood
- Keep creator UX primary: forms, dropdowns, and markdown logs over raw code
- Emphasize explainability: every simulation outcome should be human-readable
- Document schema and system changes for long-term clarity

---

## 💼 Final Note to Incoming Lead

You’re not inheriting a game. You’re inheriting the **brainstem of a transmedia storytelling system**. This is a world authoring engine, a simulation of interpersonal logic, and a prototype for narrative cognition.

Stay focused. Keep the pace sustainable. Build with intent.

When it’s done right, it won’t just simulate relationships.

It will generate meaning.

---

**End of Transfer Report**
