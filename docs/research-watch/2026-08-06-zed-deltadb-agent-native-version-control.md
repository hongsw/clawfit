# Research Watch: Zed DeltaDB

- Repo/Link: https://zed.dev/deltadb
- Source: Hacker News (267 pts, 2026-08-06)

## Why this is worth watching
DeltaDB is a CRDT-based version control system from Zed Industries that records every editing operation (not just commits) and permanently links each change to the agent conversation that produced it. It enables bidirectional tracing between a line of code and the specific agent dialogue that generated it. Waitlist opened June 11, 2026; HN traction continues into August. This is the first agent-native version control system in the corpus — it assumes agents are primary code authors, not edge-case contributors.

## What stands out immediately
- Every edit (sub-commit granularity) gets a stable Delta ID — enables `git blame` at the operation level
- Bidirectional link: code → conversation, conversation → code
- Multiple agents can edit the same file simultaneously without merge conflicts (CRDT)
- Agents can summon past agents for design reviews by replaying prior conversation context
- Positioned as a complement to Git (not a replacement) — lives in the pre-commit layer
- Backed by Sequoia; waitlist beta with rollout underway as of late June 2026

## Why clawfit should care
DeltaDB adds a new governance axis absent from current clawfit schema: `code_provenance_tracking` — whether a tool records which agent conversation produced which change. As multi-agent development becomes normal, audit trails for AI-generated code become a compliance requirement. DeltaDB is the first commercial product targeting this gap. Clawfit's Zed entry (2026-04-23) should be updated to note DeltaDB as a distinct product offering at L3.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent Harness / IDE Layer** (primary: Zed IDE with embedded agent support)
- **Level 3 — Governance / Auditability** (secondary: records which agent conversation produced code)

## Status
- Waitlist beta; actively rolling out. First signal for "agent-native version control" sub-type.
- Schema watch: `code_provenance_tracking: bool`; `crdt_collab: bool`; `sub_commit_history: bool`
