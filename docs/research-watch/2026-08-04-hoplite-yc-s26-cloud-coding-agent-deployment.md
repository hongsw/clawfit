# Research Watch: Hoplite — Cloud Coding Agent Platform

- Repo/Link: https://hoplite.sh
- Source: Hacker News (Launch HN — YC S26)

## Why this is worth watching
Hoplite is a Y Combinator S26-backed cloud service that runs AI coding agents in isolated development environments, verifies their changes via tests and browser preview, and opens pull requests for human review. It is the first YC-backed entrant explicitly framing itself as a "cloud coding agent deployment" platform rather than an IDE extension or local CLI tool.

## What stands out immediately
- Isolated per-task development environments (not shared runner)
- GitHub App integration + PR generation with human-approval gate
- Browser automation for preview testing as part of the verification step
- MCP server + CLI interfaces for programmatic access alongside the web UI
- Task threads support iterative refinement within the same conversation context
- Human-in-the-loop: "approve sensitive actions when required"

## Why clawfit should care
Hoplite occupies an L2 harness role (cloud-hosted orchestration shell around a coding agent) that clawfit's registry currently lacks as a standalone SaaS entry. It is distinct from cursor/cline (local IDE plugins) and from aider/opencode (bare CLI tools) — the differentiator is fully managed cloud isolation with built-in CI/test verification and PR workflow. This pattern — cloud agent harness with mandatory human approval gates — is a new sub-type candidate for the L2 layer.

## Preliminary interpretation
Current best reading:
- **Level 2 — Agent harness / wrapper layer** (cloud-hosted execution shell)
- Level 1 secondary — provides the underlying coding agent runtime

## Status
- First signal — YC S26 institutional backing, HN Launch HN post
- Registry candidate pending: `task: code-gen`, `role: developer`, `network: online`, `setup_complexity: low` (SaaS onboarding)
- Schema watch: `deployment_model: cloud-saas`; `human_approval_gate: bool`; `env_isolation: per-task`
