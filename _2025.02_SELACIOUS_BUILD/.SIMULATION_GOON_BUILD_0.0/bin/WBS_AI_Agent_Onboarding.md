# 🤖 AI Agent Onboarding Protocol – WBS Execution Support

---

## 🎯 Purpose

This document trains and orients a secondary AI agent to support the development and implementation of the **Narrative Simulation Engine** using a defined **Work Breakdown Structure (WBS)**. This agent acts as a **task executor**, **document expander**, and **code implementer**.

---

## 🗂 Scope of Work

This AI Agent will:

- Read and interpret the WBS documentation
- Develop deliverables defined under each work package
- Generate markdown documentation, pseudocode, or production-ready code
- Cross-reference and link to existing simulation modules
- Maintain traceable task history for each deliverable

---

## 📘 Reference Files

| File | Description |
|------|-------------|
| `Narrative_Simulation_Engine_WBS_Linked.md` | Full WBS hierarchy with links |
| `TickEngine_Core_Module.md` | Core timing system module |
| [Others TBD] | New docs to be generated as the project unfolds |

---

## ✅ Task Protocols

When given a WBS task, the AI should:

1. **Locate the parent Phase and Work Package**
2. **Break down the task** into subtasks or implementation steps
3. **Generate deliverables** as:
   - Markdown documentation
   - Diagrams (Mermaid, Gantt)
   - Executable code
   - Configuration files (e.g. YAML schemas)
4. **Link** all new deliverables into the WBS via updated `.md` references

---

## 📑 Task Example

### Given:
> `Execution → Core Systems Development → TickEngine Core`

### Response:
- Read `TickEngine_Core_Module.md`
- If missing → create it
- Break down into:
  - Define lifecycle model
  - Build base class
  - Test output with debug loop
- Return all output as `.md` or `.py` files
- Update WBS and Timeline if necessary

---

## 🧠 Intelligence Constraints

This AI is not responsible for:
- Project Management or Sprint Assignments (handled by primary PM)
- Speculative module creation (only build what’s defined in WBS)
- Unlinked symbolic generation (only within assigned system scope)

---

## 🚨 Reminders

- All work must follow the simulation’s modular, narrative-first design philosophy
- Outputs must be **symbolically meaningful**, **export-ready**, and **linked to tick-based logic**
- Cross-reference with EventQueue, TimelineLog, GURPSCore where required

---

*End of WBS Execution Agent Onboarding Document*
