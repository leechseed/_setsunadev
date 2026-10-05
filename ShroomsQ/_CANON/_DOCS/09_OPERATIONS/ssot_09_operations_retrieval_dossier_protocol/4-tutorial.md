---
title: "Retrieval dossier protocol: tutorial"
type: tutorial
for: "an operator running a first retrieval dossier"
does: "walks the source's drift-cleanup example from dataset to directives"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_09_operations_retrieval_dossier_protocol.md
source_version: 1.0.0
---

**Who it's for:** an operator running a first retrieval dossier · **What it does:** walks the source's drift-cleanup example from dataset to directives · **Type:** tutorial

# Turn a drifted template batch into directives

You will run the protocol on the source's first example. It is a batch of prompt templates that repeat the same rules with minor version differences. You finish with the directive list a dossier must end on.

## Step 1. Set the inputs

Select the batch as Document A. Provide the protocol as Document B. Tell the agent to write Document C in the mandatory structure.

## Step 2. Ingest and normalize

The agent reads the ranked batch and turns each fragment into a comparable unit. Here every unit is a prompt template.

## Step 3. Cluster and audit

The agent groups the templates by function and finds the drift. The same rules ("no hallucination," "markdown only," "linked TOC") repeat across copies with minor version differences.

## Step 4. Extract and scan

The agent lists the recurring hard rules. It then notes the missing governance: no version headers and no template registry.

## Step 5. Decide and direct

The agent writes the Final Operator Directive. The source says it concludes with directives similar to these:

- Canonicalize one prompt as v3.
- Extract common hard rules into a standalone doctrine file.
- Deprecate legacy copies and replace with wikilinks.
- Add version headers to all surviving templates.
- Create a template registry index for discovery and governance.

## Step 6. File the dossier

Store it beside the dataset and link it in the dataset header.

Next, read the [reference](2-reference.md) for all eight sections.
