# Research Watch: Alter — Access Control for Multi-User Agents

- Repo/Link: https://alterauth.com
- Source: Hacker News (Launch HN: Alter YC S25)

## Why this is worth watching
Alter provides access control primitives for multi-user AI agent deployments — addressing the gap where agents acting on behalf of multiple users need scoped permissions, audit trails, and identity boundaries. This is a YC S25 company and its HN launch attracted significant discussion.

## What stands out immediately
- Solves a real production gap: agents that act as multiple users simultaneously need fine-grained authz, not just authn
- Positioned as infrastructure, not an agent harness — an enabler for Level 3–4 orchestration layers
- Multi-user scope implies team and enterprise scenarios, not solo developer workflows

## Why clawfit should care
Governance and access control are dimensions clawfit scores but doesn't yet differentiate at the infrastructure layer. Alter could become a required dependency for any org deploying shared multi-user agents. It would be a good candidate for the `governance` feature tag in `tools_registry.json`.

## Preliminary interpretation
Current best reading:
- **Level 3 — Agent Harness / Wrapper Layer** (infrastructure/security sublayer)

## Status
- Tracking: early-stage YC startup, monitoring for registry addition once product matures
