# Research Watch: Claw Patrol — Agent Security Firewall

- Repo/Link: https://clawpatrol.dev
- Source: GeekNews

## Why this is worth watching
Claw Patrol is an open-source (MIT, maintained by Deno) security gateway that sits between agents and production services: it holds agent credentials, inspects traffic at the wire level across HTTP/SQL/Kubernetes protocols, and enforces HCL-based policy rules before any action reaches the target. It fills a gap that Shannon (pentest agent) and Strix (security testing platform) do not cover — runtime security of deployed agents rather than testing security of software.

## What stands out immediately
- Credentials never reach the agent itself — all secrets stay in the gateway
- Protocol-level matching: rules can key on SQL verbs, Kubernetes resource types, or HTTP methods, not just URLs
- Approval routing: ambiguous requests go to an LLM judge or human (Slack integration)
- Hot rule updates: no restart required for policy changes
- Regression testing: rules can be tested against recorded traffic fixtures before deploying
- Single binary deployment via WireGuard or Tailscale

## Why clawfit should care
This is a new sub-pattern at L3 (governance layer): **agent security firewall**. Previously tracked L3 tools focused on team architecture (revfactory/harness, Archon), SSOT governance (hiclaw, ms-teams-BYOA), or billing/routing (hermes-md). Claw Patrol introduces credential brokering and traffic-level policy enforcement as a distinct L3 sub-type. For `data_sensitivity: confidential` or `governance_need: hard` profiles, this category is a hard prerequisite for production deployment, and currently no registry tool addresses it.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance/Security** (agent security firewall sub-type, credential proxy + wire-level policy enforcement)

## Status
- Tracking: first-signal for production agent security gateway category; registry candidate if project reaches 2k+ stars in next 60 days
