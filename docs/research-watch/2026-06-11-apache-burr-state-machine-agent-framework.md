# Research Watch: Apache Burr — State Machine AI Agent Framework

- Repo/Link: https://github.com/apache/burr
- Source: Hacker News (#23, 168 pts)

## Why this is worth watching
Apache Burr is a Python framework for building stateful AI agent applications via action-driven state machines, now under Apache Foundation incubation. It is the first Apache Foundation-backed AI agent framework in this taxonomy — adding an institutional governance class distinct from startup-controlled (Cline, Aider) and Big Tech-controlled (Claude Code, Cursor) entries.

## What stands out immediately
- Pure Python: no DSL, no YAML — just functions and decorators
- State machine architecture with automatic state persistence (disk, DB, custom backends)
- Built-in UI for real-time monitoring, tracing, and debugging of agent runs
- Fan-out / fan-in parallel action execution; sub-application composition for modular design
- Framework-agnostic: integrates with LangChain, LlamaIndex, Haystack, and custom backends
- Apache Incubating governance: neutral IP holding, contributor model, formal release process

## Why clawfit should care
This is a new L2 harness candidate with Apache Foundation governance — a governance class not currently represented in the L2 taxonomy. Differs from `openai-agents-python` (vendor-controlled, lightweight handoffs) and LangGraph (complex graph DSL). Registry candidate for `task: orchestration` + `governance_need: hard` profiles. Apache provenance may appeal to enterprise/regulated orgs where legal and IP governance over infrastructure matters.

## Preliminary interpretation
Current best reading:
- **Level 2 primary — Agent Harness / Orchestration Framework** (action-driven state machine harness with parallel execution)
- **L3 secondary candidate** (built-in tracing + state persistence carry governance characteristics; blocking vs. advisory behavior unconfirmed)

## Status
- First signal; held pending star count verification (registry threshold: 5k+)
- Apache Foundation incubating — governance class confirmed; distinct from all existing L2 entries
- Registry candidate: `tasks: [orchestration, code-gen]`, `roles: [developer]`, `governance_need: hard` profiles
- Promotion criterion: confirm 5k+ GitHub stars OR adoption evidence from a second independent project citing Burr
