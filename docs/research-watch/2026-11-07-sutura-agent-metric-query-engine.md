# Research Watch: sutura — Agent Query Engine for Company Metrics

- Repo/Link: https://github.com/telekom/sutura
- Source: GeekNews front page

## Why this is worth watching
sutura (Deutsche Telekom OSS) is a query engine that lets AI agents answer data questions using the company's own metric definitions, so agent-computed results match what employees see on dashboards. The key design choice: instead of letting agents write ad-hoc SQL or call data APIs directly, sutura exposes a semantic metrics layer — agents query named metrics, not raw tables. This addresses a known failure mode where agents produce numbers that contradict official reporting.

## What stands out immediately
- Semantic metric definitions are the query surface, not raw schemas
- Results align with dashboards by construction (not by luck)
- From Deutsche Telekom's OSS org — enterprise-validated use case
- Directly relevant to `large_exec_research` and `data-analysis` profiles in clawfit
- Addresses the "data freshness and pipeline status" gap noted in the GeekNews signal about autonomous-agent data platforms

## Why clawfit should care
clawfit currently has `data-analysis` as a task type but no scoring distinction between agents that query raw data vs. agents that use a governed semantic layer. sutura represents a new *governed data access* capability type that matters specifically for `governance_need: hard` profiles. For large orgs with hard governance, recommending an agent that bypasses the metric layer would be a significant mis-fit. First signal for this pattern as a named, deployable tool.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability Layer** (data access / semantic metrics sub-type)
- Secondary: L3 (governance layer) — the metric definitions function as a policy constraint on what agents can compute

## Status
- First signal for governed semantic-layer data access for agents (distinct from MCP data connectors and raw DB tools)
- Registry action: candidate entry pending star count verification and independence from Deutsche Telekom's internal stack
