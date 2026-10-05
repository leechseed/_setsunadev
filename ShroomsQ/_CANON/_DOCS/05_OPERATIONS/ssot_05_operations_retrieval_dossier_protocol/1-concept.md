---
title: "Retrieval dossier protocol: concept"
type: concept
for: "an operator or AI agent turning a raw retrieval dump into an action list"
does: "explains why the retrieval dossier ends in directives and how the protocol forces that"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_retrieval_dossier_protocol.md
source_version: 1.0.0
---

**Who it's for:** an operator or AI agent turning a raw retrieval dump into an action list · **What it does:** explains why the retrieval dossier ends in directives and how the protocol forces that · **Type:** concept

# The dossier tells the operator what to do

A raw retrieval batch is noise: similarity scores, file paths, and excerpts. The **Retrieval Dossier** is the operational analysis that turns the noise into structured signal, explicit risks, and prioritized operator directives.

## One question governs the whole output

The dossier answers one question: what must the operator do with this dataset. Every section serves that question, and the dossier ends with directives, not explanation.

## Two documents in, one document out

The operator supplies Document A, the raw dataset, and Document B, this protocol. The agent returns Document C, the dossier. The protocol is the agent's instruction set, so the same protocol yields the same shape each time.

## The structure leaves no room to drift

The dossier uses eight H2 sections in a fixed order, with none omitted and none added. The agent also may not invent files, counts, rules, or capabilities. Where information is absent, the agent writes "Not found in provided material."

## Decision-grade is a test, not a mood

A dossier is **decision-grade** when it meets six conditions: it classifies, finds duplicates and drift, extracts recurring constraints, enumerates gaps, ranks actions with impact and complexity, and ends with directives. A dossier that fails one condition is not decision-grade.

For every component, read the [reference](2-reference.md). For the tasks, read the [how-to](3-how-to.md). For a worked example, read the [tutorial](4-tutorial.md).

## The long read

The protocol inherits the SSOT language standards: no contractions, no hedging, present tense, active voice, and bolded first terms. It uses directive verbs because the reader of a dossier is an operator about to act: Consolidate, Canonicalize, Deprecate, Extract, Refactor, Archive. The two examples in the source show the typical shape of a conclusion: collapse drifted copies into one canonical file, and split methodology from project application.
