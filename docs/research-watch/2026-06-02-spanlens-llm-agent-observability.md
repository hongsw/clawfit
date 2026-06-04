# Research Watch: Spanlens — LLM Agent Observability Platform

- Repo/Link: https://github.com/sunes26/Spanlens — https://spanlens.io
- Source: GeekNews ("Show GN: Spanlens — Open-source observability platform for LLM calls and agent tracing")

## Why this is worth watching
Spanlens is an MIT-licensed, self-hostable observability platform that traces every LLM API call across OpenAI, Anthropic, and Gemini, tracking cost, latency, tokens, and full request/response bodies. It enters a crowded space (LangSmith, Langfuse, Helicone) but explicitly positions self-hosting as a zero-cost first-class option — not an enterprise upsell. The built-in experiment layer (A/B prompt versioning against fixed datasets with LLM-as-judge scoring) bundles eval tooling that competitors typically gate behind paid tiers.

## What stands out immediately
- Drop-in SDK replacement claiming two-line integration with no rewrite required
- Agent tracing renders multi-step workflows as waterfall span trees with critical-path analysis
- Anomaly detection uses 3-sigma deviation against a 7-day baseline — claim to inspect, not yet validated
- PII scanning is regex-based; auto-masks API keys in stored payloads
- Async ingestion with claimed p99 <3ms overhead — claim to inspect
- Model recommender suggests cost-optimized swaps backed by captured metrics
- Deployment: Docker Compose or single binary; runs entirely inside a private VPC
- Explicit comparison pages exist against LangSmith, Langfuse, Helicone, Braintrust, and Arize Phoenix

## Why clawfit should care
The current clawfit scoring model has no signal for observability tooling, and the registry has no `data_sensitivity: confidential` or `governance_need: hard` gate that would surface a self-hosted observability requirement. Teams that cannot send LLM call payloads to a third-party SaaS — regulated industries, internal tooling with PII, cost-sensitive orgs — need an observability layer that is sovereign by default. Spanlens is the first signal in this watch directory for that specific gap. If clawfit adds a `governance_need` or `data_sovereignty` filter dimension, this category becomes a scoring prerequisite rather than an optional add-on.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** (observability and eval sub-type: spans, cost tracking, experiment datasets, and LLM-as-judge scoring all operate on captured context flowing between agent steps)

## Status
- First-signal for self-hosted LLM observability category; registry candidate if GitHub star velocity confirms organic adoption; scoring model gap flagged for `data_sensitivity` / `governance_need` dimension
