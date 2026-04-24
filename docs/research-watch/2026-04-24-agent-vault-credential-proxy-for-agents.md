# Research Watch: Agent Vault — Open-Source Credential Proxy and Vault for Agents

- Repo/Link: https://github.com/agent-vault/agent-vault (HN link, exact path unconfirmed)
- Source: Hacker News front page (2026-04-24, #9)

## Why this is worth watching
A second credential proxy for AI agents surfaced on HN front page today alongside the existing `kontext-cli` (tracked 2026-04-15). While kontext-cli uses OIDC+RFC 8693 ephemeral token exchange (Go binary, governance-telemetry focus), Agent Vault frames itself as a "credential proxy and vault" — implying secrets management beyond ephemeral credentials, potentially long-lived service account vault functionality.

## What stands out immediately
- HN front page placement — editorial relevance signal even without star count
- "Vault" framing suggests broader secrets management than ephemeral tokens (Hashicorp Vault mental model vs. OIDC ephemeral rotation)
- "Open-source" — self-hostable, relevant to `governance_need: hard` + `data_sensitivity: confidential` profiles
- Distinct from kontext-cli: kontext-cli = ephemeral OIDC rotation; Agent Vault = secrets vault/proxy

## Why clawfit should care
- A second HN-prominent entry for "credential infrastructure for AI agents" in 10 days confirms this is becoming a stable product category at L4c — not just a one-off project
- Both tools target the same governance gap: agents with write access to production systems need credential hygiene
- clawfit's `governance_need: hard` scoring dimension is directly addressed — if two independent projects arrive at the same problem independently, the market need is real
- GeekNews was unreachable today (503); re-check tomorrow for Korean community signal on this tool

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (secrets vault / credential proxy sub-type alongside kontext-cli)

## Status
- Tracking; need confirmed GitHub URL and star count before registry consideration
