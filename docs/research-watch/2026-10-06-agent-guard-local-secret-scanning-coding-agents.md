# Research Watch: Agent Guard — Local Secret-Scanning Guardrail for Coding Agents

- Repo/Link: https://github.com/JeongJaeSoon/agent-guard
- Source: GeekNews (Show GN)

## Why this is worth watching
Agent Guard is a local-first MIT-licensed tool that prevents AI coding agents (Claude Code, Codex) from leaking credentials. It blocks risky `.env` file reads at the plugin layer, masks secrets in tool responses, and adds Git pre-commit hooks using gitleaks 8.30+ for staged-change scanning. The pattern — a harness-side interception layer specifically for credential hygiene — is new in the tracked corpus.

## What stands out immediately
- Three defensive layers: agent plugin (blocks risky commands), Git hook (scans staged files), GitHub Actions (CI-level scanning)
- Native Claude Code and Codex plugin integration via guided setup commands
- No hosted accounts, no telemetry — strictly local
- MIT license; macOS + Linux (x64 / arm64); 31 stars at time of tracking (early stage)
- Uses gitleaks as the detection engine — battle-tested secret-pattern library

## Why clawfit should care
Credential exposure via coding agents is an emerging governance failure mode not yet addressed in `org_fit.governance_need` scoring. Agent Guard is the first tracked tool representing a dedicated "secret-scanning guardrail" sub-type at the harness layer — distinct from general MCP trust governance (Codemode, Figma whitelist) and from broader compliance auditing (iFixAi). Orgs with `governance_need: hard` and `data_sensitivity: confidential` are the natural fit; the tool directly addresses the OWASP-style secret-leakage risk that arises when agents read full project directories.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper Layer** (primary) with **Level 4 — Capability Layer** secondary (plugin integration point)

## Status
- New signal 2026-10-06 — early-stage tool (31★); monitoring for adoption growth and whether the pattern consolidates into a standalone sub-category of agent security tooling
