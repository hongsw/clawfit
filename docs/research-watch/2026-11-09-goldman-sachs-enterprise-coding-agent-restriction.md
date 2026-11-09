# Research Watch: Goldman Sachs Restricts Claude Code for Bankers and Traders

- Repo/Link: https://thestateofai.com (reported, HN thread)
- Source: Hacker News (550 points)

## Why this is worth watching
Goldman Sachs is reportedly pulling Claude Code from its bankers and traders, citing data-security and compliance concerns. This is the first widely-reported case of a Tier-1 financial institution explicitly restricting an agentic coding tool at the desk level — it signals that enterprise AI governance for coding agents is moving from policy discussion to enforcement.

## What stands out immediately
- Restriction is role-specific (bankers + traders, not all engineers)
- Likely driven by the "Don't Ask Again" secret-leak vector documented earlier this week (see `2026-11-08-coding-agent-secret-leak-dont-ask-again.md`)
- Suggests financial-services firms need on-premises or air-gapped agent deployments, not just data-retention policies
- 550 HN points indicates broad developer awareness of the governance gap

## Why clawfit should care
The `governance_need` dimension in clawfit's scoring directly maps to this scenario: `hard` governance should surface tools with `on-prem`, `audit-logs`, or `air-gapped` features and filter out cloud-only tools with implicit data retention. The Goldman signal validates that the `large_exec_research` and `offline_mid_codegen` profiles — which already penalize cloud-only tools — are directionally correct. It may also warrant a new `financial-services` tag in `org_fit.features`.

## Preliminary interpretation
Current best reading:
- **Governance signal** — not a tool, but a real-world validation of clawfit's `governance_need: hard` filter logic

## Status
- Tracking: policy signal — monitor for other Tier-1 finance/healthcare institutions following suit
