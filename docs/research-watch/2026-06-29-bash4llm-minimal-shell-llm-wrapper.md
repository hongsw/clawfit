# Research Watch: Bash4LLM+ — Dependency-Free Bash Wrapper for LLM APIs

- Repo/Link: https://github.com/kamaludu/bash4llm/
- Source: Hacker News (Show HN)

## Why this is worth watching
A single-file, auditable Bash script that wraps LLM provider APIs for CLI use — no Python, no Node, no package manager required. The security-first design (no `/tmp`, no `eval`, provider code validation) targets constrained environments like Termux/Android and air-gapped shells. Represents a counter-movement to heavyweight agent frameworks: the minimal harness as a unix primitive.

## What stands out immediately
- **Zero dependencies**: pure Bash, no runtime installation required
- **Security-explicit**: rejects `eval`, avoids `/tmp`, validates provider code before execution
- **Session memory**: NDJSON session files enable multi-turn context without a server
- **ui_state JSON output**: exposes metadata for external tool integration
- **Supported providers**: Groq (native), with optional Google Gemini, HuggingFace, Mistral extensions
- **Target environment**: Termux/Android, resource-constrained CI, air-gapped systems

## Why clawfit should care
Bash4LLM+ occupies the same niche as the `push` minimal shell harness (tracked 2026-05-01) but with a heavier focus on security auditability and offline-adjacent operation. It raises the question of whether clawfit's `setup_complexity: low` band should distinguish between "low because it's an installer" vs "low because it's a single file with no deps." The latter is meaningfully more accessible in regulated or resource-constrained environments.

## Preliminary interpretation
Current best reading:
- **Level 2 — Minimal Agent Harness / Shell Wrapper** (primary)

Analogous to: `push` (minimal shell coding agent harness, 2026-05-01), `zot` (minimal Go coding agent harness, 2026-05-30)

## Status
- First signal — 2026-06-29
- Low adoption signal (Show HN debut). Hold for registry until: 500★ OR second security-focused shell LLM wrapper surfaces
