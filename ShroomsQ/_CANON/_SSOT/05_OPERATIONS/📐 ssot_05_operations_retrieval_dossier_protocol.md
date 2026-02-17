---
type: ssot_05_operations
category: operations
version: 1.0.0
last_updated: 2026-02-12
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: "Defines the mandatory protocol for converting raw retrieval batch outputs into decision-grade dossiers optimized for analysis and operator action."
dependencies:
  [
    "[[📐 ssot_05_operations_writing_guide]]",
    "[[📐 ssot_05_operations_ai_instruction_protocol]]",
    "[[📐 ssot_methodology_creation_standard]]",
  ]
---

# 📐 ssot_05_operations_retrieval_dossier_protocol

## Table of Contents

1. [Purpose](https://chatgpt.com/c/698db8f7-b0cc-8333-9bcb-01de070b5cd3#purpose)
2. [Core Methodology](https://chatgpt.com/c/698db8f7-b0cc-8333-9bcb-01de070b5cd3#core-methodology)
3. [Implementation](https://chatgpt.com/c/698db8f7-b0cc-8333-9bcb-01de070b5cd3#implementation)
4. [Examples](https://chatgpt.com/c/698db8f7-b0cc-8333-9bcb-01de070b5cd3#examples)
5. [Version History](https://chatgpt.com/c/698db8f7-b0cc-8333-9bcb-01de070b5cd3#version-history)

---

## Purpose

This document defines the canonical protocol for transforming a raw retrieval batch extraction Markdown file into a **Retrieval Dossier**, a decision-grade artifact that tells the operator exactly what to do with the dataset. This protocol enforces doctrinal language, structural rigor, and action-first outputs aligned to SSOT standards.

---

## Core Methodology

### **Retrieval Dossier**

A **Retrieval Dossier** is an operational analysis output that converts noisy retrieval results into structured signal, explicit risks, and prioritized operator directives.

### Doctrinal Constraints

The dossier output conforms to SSOT linguistic and structural standards:

- **No Contractions**: All statements use full forms.
- **No Hedging**: Qualifiers are prohibited.
- **Present Tense**: The system is described as active and current.
- **Active Voice**: Subjects perform actions with unambiguous verbs.
- **Technical Precision**: The first instance of a technical term is **Bolded** and defined.

### Input Model

This protocol assumes a two-document input pair:

- **Document A (Dataset)**: A raw retrieval batch extraction `.md` containing similarity scores, file paths, and excerpts.
- **Document B (Protocol)**: This document, supplied to an AI agent as the governing instruction set.

### Output Model

The agent outputs a third artifact:

- **Document C (Dossier)**: A decision-grade dossier that answers one question: **What must the operator do with this dataset.**

### Mandatory Output Structure

The dossier produced by the agent uses the following H2 section order with no omissions:

1. Dataset Classification
2. Component Inventory
3. Redundancy and Drift Analysis
4. Pattern Extraction
5. Structural Gaps
6. System Risk Assessment
7. Decision Matrix
8. Final Operator Directive

### Operational Definition of “Decision-Grade”

A dossier is decision-grade when it satisfies all of the following:

- It classifies the dataset into actionable types.
- It identifies duplicates, drift, and contradictions.
- It extracts recurring constraints and recurring structures.
- It enumerates gaps that block canonical consolidation.
- It produces prioritized actions with impact and complexity estimates.
- It ends with directives, not explanation.

---

## Implementation

### Operator Procedure

1. Select the raw retrieval batch extraction `.md` as **Document A**.
2. Provide this protocol `.md` as **Document B**.
3. Instruct the agent to generate **Document C** using the Mandatory Output Structure.
4. Store the dossier adjacent to the dataset and link it in the dataset header.

### Agent Execution Procedure

The agent executes the following workflow internally:

1. **Ingest**: Parse Document A as a ranked evidence list (scores, paths, excerpts).
2. **Normalize**: Convert fragments into comparable units (templates, workflows, doctrine, standards, tooling, notes).
3. **Cluster**: Group units by shared function and shared structure.
4. **Audit**: Identify duplicates, drift variants, conflicts, and orphan fragments.
5. **Extract**: Enumerate recurring constraints and recurring section patterns.
6. **Gap-Scan**: Detect missing governance components (registry, versioning, lifecycle policy, enforcement).
7. **Decide**: Produce operator actions ranked by priority with expected impact and estimated complexity.
8. **Direct**: End with a directive list that is executable without interpretation.

### Output Format Requirements

- **Single Markdown Output**: The agent returns one drop-in `.md` dossier.
- **No Added Sections**: The agent uses only the Mandatory Output Structure.
- **No Invention**: The agent does not fabricate files, counts, rules, or system capabilities.
- **Explicit Unknowns**: If information is absent, the agent states: “Not found in provided material.”
- **Operator-First Language**: The dossier uses directive verbs (Consolidate, Canonicalize, Deprecate, Extract, Refactor, Archive).

---

## Examples

### Example 1: Prompt Template Drift Cleanup

**Input (Document A)**: A retrieval batch showing multiple prompt templates that repeat “no hallucination,” “markdown only,” and “linked TOC,” with minor version differences.

**Output (Document C) Must Conclude With Directives Similar To**:

- Canonicalize one prompt as v3.
- Extract common hard rules into a standalone doctrine file.
- Deprecate legacy copies and replace with wikilinks.
- Add version headers to all surviving templates.
- Create a template registry index for discovery and governance.

### Example 2: Mixed Workflow and Standards Bundle

**Input (Document A)**: A retrieval batch mixing workflow procedures, YAML formatting rules, and operational environment notes.

**Output (Document C) Must Conclude With Directives Similar To**:

- Split methodology (SSOT) from project application (Authoritative).
- Merge all YAML rules into a single canonical “YAML Standard” file.
- Move environment notes into operations protocols.
- Add dependencies wikilinks across all operational documents.
- Create a lifecycle policy: Draft → Spec → Locked → Canonical → Deprecated.

---

## Version History

| Version | Date       | Changes                                                                    |
| :------ | :--------- | :------------------------------------------------------------------------- |
| 1.0.0   | 2026-02-12 | Initial canonical protocol for transforming retrieval dumps into dossiers. |
