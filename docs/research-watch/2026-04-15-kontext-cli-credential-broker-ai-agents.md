# Research Watch: Kontext CLI — Credential Broker for AI Coding Agents

- Repo/Link: https://github.com/kontext-dev/kontext-cli
- Source: Hacker News (Show HN)

## Why this is worth watching
Kontext CLI is an early-stage (98★, v0.3.0) but conceptually novel tool: it replaces long-lived API keys with ephemeral, scoped credentials injected at agent session start and automatically expired on exit. It introduces **governance telemetry** — streaming captures of PreToolUse, PostToolUse, and UserPromptSubmit hook events to an audit backend. This is the first dedicated credential brokering + audit tool in this taxonomy that is explicitly designed for AI coding agents rather than adapted from general DevOps tooling.

## What stands out immediately
- OIDC-based auth → RFC 8693 token exchange → short-lived `.env.kontext` injected at session start
- Zero stored API keys; automatic expiration when agent session ends
- Claude Code supported now; Cursor and Codex planned
- Go binary, no daemon required, single command: `kontext start --agent claude`
- Governance hooks capture tool call telemetry for compliance/audit use cases
- v0.3.0, April 2026 — very early; concept ahead of adoption

## Why clawfit should care
The `governance_need: hard` scoring dimension in clawfit currently maps to harnesses that support governance features (agentapi, aperant, etc.). Kontext CLI represents a **new sub-category**: infrastructure-level credential governance that sits *below* the harness, orthogonal to which base agent is used. Orgs with `data_sensitivity: confidential` + `governance_need: hard` profiles may need both a governance harness *and* a credential broker. This points to a gap in the current single-axis governance scoring. Also relevant: if kontext adoption grows, it could become a registry entry for Level 4c (security/identity layer for agents).

## Preliminary interpretation
Current best reading:
- **Level 4c — Identity / persona / security configuration layer** (credential brokering + telemetry governance at agent boundary)

## Status
- Very early signal (98★); watch for Cursor/Codex support and org adoption; revisit at 1k★
