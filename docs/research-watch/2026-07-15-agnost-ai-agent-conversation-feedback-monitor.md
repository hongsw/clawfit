# Research Watch: Agnost AI — Agent Conversation Failure Monitor

- Repo/Link: https://www.agnost.ai
- Source: Hacker News (Launch HN: YC S26)

## Why this is worth watching
Agnost AI (YC S26) is a production monitoring platform that reads real agent conversations to detect where users fail, get stuck, or churn — then opens PRs with proposed fixes. It sits at the evaluation/observability layer of the agent stack, filling the gap between passing evals and production reliability.

## What stands out immediately
- OpenTelemetry-native; claims 2-minute setup with any LLM/framework
- Automatically surfaces failure categories: broken workflows, repeated retries, setup friction, churn risk
- Can auto-open pull requests for high-impact fixes that teams review before merging
- Clients include Google and Exa — enterprise early adoption signal
- Distinguishes itself from tracing tools by generating actionable fixes, not just dashboards

## Why clawfit should care
This is a new category in the ecosystem: **agent conversation evaluation-to-fix** loop. clawfit's `data_sensitivity` and `governance_need` dimensions already score tools on compliance and oversight; Agnost fits into the governance/evaluation layer for mid-to-large orgs. It should be considered for addition to tools_registry under a new `agent_eval_monitoring` category. High governance-need profiles should see it recommended alongside coding agents.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation / Observability** (production agent conversation monitor that closes the eval-to-fix loop)

## Status
- New entry, YC S26 batch. Watch for: open-source tier, pricing announcement, MCP integration.
