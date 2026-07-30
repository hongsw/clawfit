# Research Watch: OpenAI Codex Security

- Repo/Link: https://github.com/openai/codex-security
- Source: GeekNews (2026-07-30)

## Why this is worth watching
OpenAI open-sourced Codex Security as a standalone tool for local security scanning in CI/CD pipelines. This is structurally distinct from the Codex CLI (coding agent) and the Codex Plugin system — it is a purpose-built security analysis layer that runs locally without sending code to the cloud. For enterprises with strict data governance requirements, a vendor-signed security scanner that operates fully offline is a meaningful trust signal.

## What stands out immediately
- Local-first operation: runs on-device without code leaving the CI/CD environment — targets the `data_sensitivity: confidential` persona directly
- CI/CD integration focus: designed as a pipeline step, not an interactive agent — pure L4 tool-call primitive rather than a session-oriented agent
- OpenAI vendor signature: same brand as Codex CLI creates natural bundling opportunity for orgs already on the OpenAI stack
- Positioned as security-specific capability rather than a general code reviewer — narrower scope than alibaba/open-code-review (hybrid architecture, already tracked 2026-06-22)
- Open-source release (MIT implied by "open-source" framing) lowers procurement friction for regulated environments

## Why clawfit should care
Adds a second datapoint to the emerging "vendor-provided security scanning layer" pattern (MAI-Cyber-1/MDASH was first, 2026-07-27, Microsoft). OpenAI doing the same move within days signals convergence: all major providers are releasing security scanning as a free local companion to their paid agent products. For clawfit's `tasks: security-testing` filter, the registry should distinguish open-source local scanners from SaaS security agents — the governance and cost implications are orthogonal.

## Preliminary interpretation
Current best reading:
- **Level 4c — Capability Layer Tool** (MCP-compatible local security scanning primitive for CI/CD)
- **Level 3 secondary — Behavioral Governance** (automated security policy enforcement in the pipeline)

## Status
- First signal — registry candidate if verification confirms offline-only operation and deterministic latency data
- Schema gap: `requires_cloud_inference: bool` — no way to distinguish tools that claim offline from those that actually run inference locally
