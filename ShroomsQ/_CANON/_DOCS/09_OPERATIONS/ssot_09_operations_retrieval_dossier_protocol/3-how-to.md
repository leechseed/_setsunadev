---
title: "Retrieval dossier protocol: how-to"
type: how-to
for: "an operator or AI agent producing one retrieval dossier"
does: "gives the steps to run the protocol and check the dossier"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_09_operations_retrieval_dossier_protocol.md
source_version: 1.0.0
---

**Who it's for:** an operator or AI agent producing one retrieval dossier · **What it does:** gives the steps to run the protocol and check the dossier · **Type:** how-to

# Retrieval dossier protocol: how-to

## Produce a dossier as the operator

1. Select the raw retrieval batch extraction `.md` as Document A.
2. Provide this protocol `.md` as Document B.
3. Instruct the agent to generate Document C using the Mandatory Output Structure.
4. Store the dossier next to the dataset.
5. Link the dossier in the dataset header.

## Produce a dossier as the agent

1. Ingest Document A as a ranked evidence list.
2. Normalize the fragments into comparable units.
3. Cluster the units by function and structure.
4. Audit for duplicates, drift variants, conflicts, and orphan fragments.
5. Extract recurring constraints and section patterns.
6. Gap-scan for missing registry, versioning, lifecycle policy, or enforcement.
7. Decide: rank actions by priority with impact and complexity.
8. Direct: end with directives the operator runs without interpretation.

## Check that a dossier is decision-grade

1. Confirm the eight H2 sections appear in order, with none added.
2. Confirm the dataset is classified into actionable types.
3. Confirm duplicates, drift, and contradictions are named.
4. Confirm gaps and ranked actions with impact and complexity appear.
5. Confirm the last section holds directives, not explanation.
6. Confirm missing information reads "Not found in provided material."
