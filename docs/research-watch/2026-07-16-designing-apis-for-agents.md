# Research Watch: "Designing APIs for Agents" — Agent-Centric API Design Principles

- Repo/Link: https://www.freestyle.sh/blog/opinion/designing-apis-for-agents
- Source: Hacker News (36 points, 2026-07-16)

## Why this is worth watching
This article articulates a design philosophy that inverts standard API ergonomics: what is good for human developers (implicit defaults, terse names, minimal required fields) is actively harmful for agent consumers. As LLM agents become primary API consumers alongside humans, API design conventions will need to diverge. This is an early but clear signal that "agent-native API design" is becoming a distinct discipline.

## What stands out immediately
- **Explicit over implicit**: agents should fill all parameters, defaults breed agent hallucination
- **Unambiguous naming**: `displayName`/`slug`/`externalId` vs. generic `name`
- **Precise errors as teaching moments**: errors clarify semantics for agent reasoning traces
- **Facts over utility wrappers**: APIs should expose core capabilities, not convenience abstractions that obscure meaning
- Directly addresses agent hallucination at the API contract layer — not just prompt engineering

## Why clawfit should care
clawfit's recommendation engine is itself consumed by agents (via the CLI) in multi-agent harness configurations. This article's principles apply to clawfit's own output format: explicit field names, deterministic error responses, and zero-ambiguity schema choices reduce agent misuse. More broadly, as clawfit tracks agent tooling adoption, tools that expose "agent-native" APIs should score higher for `current_ai_usage: multi_agent` profiles.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal** — design principle, not a deployable tool
- Conceptually adjacent to L4 (capability/tool layer) — how tools expose themselves to agents

## Status
- Tracking as ecosystem signal; no registry entry
- Schema watch: `api_design: [human-first | agent-native | dual]` as a tool metadata field
