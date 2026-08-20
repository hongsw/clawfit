# Research Watch: CHAP — Collaborative Human-Agent Protocol

- Repo/Link: https://github.com/brightbeamai/chap
- Source: Hacker News (14 pts, front page 2026-08-20)

## Why this is worth watching
CHAP is a v0.2 open protocol for creating hash-linked, auditable records of work performed jointly by humans and AI agents. It fills a gap that MCP and A2A leave open: once a tool call is made and a human edits the output, where does that decision live? CHAP captures the agent draft, human edit, rationale, and structured override tags in a single verifiable envelope, producing supervision data as a natural by-product of the workflow rather than a separate annotation step.

## What stands out immediately
- **Seven core methods + eleven optional profiles** — minimal core, extensible without versioning churn
- **Override envelope** — distinguishes refining edits (rewording) from substituting overrides (different decision) with a hash-linked chain
- **Five framework bridges** ship at v0.2: LangGraph, Pydantic AI, AG2, LlamaIndex, Google ADK
- **MCP + A2A transport** — CHAP records attach to existing tool-use workflows, not a new channel
- **Conformance harness** included; 39 method handlers covered by reference implementations in TypeScript + Python
- 44★ at launch; very early but spec-complete at v0.2

## Why clawfit should care
clawfit's `governance_need` dimension (none / soft / hard) currently scores tools on whether they *support* governance, but has no schema representation for human-agent interaction audit trails. CHAP defines the primitives that would populate a `governance_need: hard` workflow with verifiable evidence — the override envelope is the data structure that a compliance-grade deployment would need. If the protocol gains traction across the framework bridges (LangGraph etc.), it becomes the audit-layer that `hard` governance orgs require below their orchestration stack.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team Workflow / Governance Layer** (primary): CHAP sits above the agent runtime (L1) and harness (L2), imposing a recordkeeping contract on human-agent interaction
- **Level 4 — Capability Layer** (secondary, MCP/A2A transport): the MCP server mode makes CHAP callable as a tool from within agent pipelines

## Schema gap signal
`human_override_audit: [none | soft-log | chap-v0 | ...]`; `governance_evidence_format: [none | chat-log | chap-envelope]`

## Status
- Tracking: watch for framework adoption (LangGraph, LlamaIndex integrations going live)
- Two-signal rule: not yet met for L3 governance-audit protocol; single signal
- Registry entry: no — 44★, protocol spec, no direct agent/LLM/hardware schema mapping
