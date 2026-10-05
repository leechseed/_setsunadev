---
title: "Retrieval dossier protocol: reference"
type: reference
for: "an operator or AI agent looking up a dossier section, rule, or step"
does: "lists every component of the Retrieval Dossier protocol"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_retrieval_dossier_protocol.md
source_version: 1.0.0
---

**Who it's for:** an operator or AI agent looking up a dossier section, rule, or step · **What it does:** lists every component of the Retrieval Dossier protocol · **Type:** reference

# Retrieval dossier protocol: reference

The source has type `ssot_05_operations`, category operations, status canonical, version 1.0.0, last updated 2026-02-12. It applies to OVEREXITOUT, ASTRO7EX, LAKAD. Its stated purpose: it defines "the mandatory protocol for converting raw retrieval batch outputs into decision-grade dossiers optimized for analysis and operator action."

## Core Methodology

### Retrieval Dossier

A **Retrieval Dossier** is an operational analysis output. It converts noisy retrieval results into structured signal, explicit risks, and prioritized operator directives.

### Doctrinal Constraints

The dossier conforms to SSOT linguistic and structural standards:

- **No Contractions:** all statements use full forms.
- **No Hedging:** qualifiers are prohibited.
- **Present Tense:** the system is described as active and current.
- **Active Voice:** subjects perform actions with unambiguous verbs.
- **Technical Precision:** the first instance of a technical term is **Bolded** and defined.

### Input Model

The protocol assumes a two-document input pair:

- **Document A (Dataset):** a raw retrieval batch extraction `.md` with similarity scores, file paths, and excerpts.
- **Document B (Protocol):** this document, supplied to an AI agent as the governing instruction set.

### Output Model

The agent outputs **Document C (Dossier)**, a decision-grade dossier that answers one question. The question is what the operator must do with this dataset.

### Mandatory Output Structure

The dossier uses these H2 sections in this order, with no omissions:

1. Dataset Classification
2. Component Inventory
3. Redundancy and Drift Analysis
4. Pattern Extraction
5. Structural Gaps
6. System Risk Assessment
7. Decision Matrix
8. Final Operator Directive

### Operational Definition of “Decision-Grade”

A dossier is decision-grade when it satisfies all of these:

- It classifies the dataset into actionable types.
- It identifies duplicates, drift, and contradictions.
- It extracts recurring constraints and recurring structures.
- It enumerates gaps that block canonical consolidation.
- It produces prioritized actions with impact and complexity estimates.
- It ends with directives, not explanation.

## Implementation

### Operator Procedure

1. Select the raw retrieval batch extraction `.md` as Document A.
2. Provide this protocol `.md` as Document B.
3. Instruct the agent to generate Document C using the Mandatory Output Structure.
4. Store the dossier adjacent to the dataset and link it in the dataset header.

### Agent Execution Procedure

The agent runs eight steps internally:

1. **Ingest:** parse Document A as a ranked evidence list (scores, paths, excerpts).
2. **Normalize:** convert fragments into comparable units (templates, workflows, doctrine, standards, tooling, notes).
3. **Cluster:** group units by shared function and shared structure.
4. **Audit:** identify duplicates, drift variants, conflicts, and orphan fragments.
5. **Extract:** enumerate recurring constraints and recurring section patterns.
6. **Gap-Scan:** detect missing governance components (registry, versioning, lifecycle policy, enforcement).
7. **Decide:** produce operator actions ranked by priority with expected impact and estimated complexity.
8. **Direct:** end with a directive list that is executable without interpretation.

### Output Format Requirements

- **Single Markdown Output:** the agent returns one drop-in `.md` dossier.
- **No Added Sections:** the agent uses only the Mandatory Output Structure.
- **No Invention:** the agent does not fabricate files, counts, rules, or system capabilities.
- **Explicit Unknowns:** if information is absent, the agent states "Not found in provided material."
- **Operator-First Language:** directive verbs (Consolidate, Canonicalize, Deprecate, Extract, Refactor, Archive).

## Examples

### Example 1: Prompt Template Drift Cleanup

Input: a batch showing multiple prompt templates that repeat "no hallucination," "markdown only," and "linked TOC," with minor version differences. The dossier concludes with directives similar to: canonicalize one prompt as v3. Extract common hard rules into a standalone doctrine file. Deprecate legacy copies and replace with wikilinks. Add version headers to all surviving templates. Create a template registry index.

### Example 2: Mixed Workflow and Standards Bundle

Input: a batch mixing workflow procedures, YAML formatting rules, and operational environment notes. The dossier concludes with directives similar to: split methodology (SSOT) from project application (Authoritative). Merge all YAML rules into a single canonical "YAML Standard" file. Move environment notes into operations protocols. Add dependencies wikilinks across all operational documents. Create a lifecycle policy of Draft, Spec, Locked, Canonical, Deprecated.
