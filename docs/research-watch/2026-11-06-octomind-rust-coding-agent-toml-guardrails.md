# Research Watch: Octomind — Rust Coding Agent Harness with TOML Policy Guardrails

- Repo: https://github.com/Muvon/octomind (⭐615)
- Source: munderdiffl.in agent-tools roundup 2026-11-04

## Why this is worth watching

Octomind is an Apache 2.0 coding agent harness written in Rust, distributed as a single binary, with policy expressed in `.agents/guardrails.toml` rather than runtime approval prompts. The TOML policy model is architecturally distinct from the approval-mode taxonomy seen in Open Duet (Ask first / Accept edits / Approve for me / Plan only) and from the continuous-confirmation model of Claude Code's permission prompts. Declarative policy files are easier to audit, diff, and enforce in CI — they're governance artifacts, not runtime behaviors. The supervisor model (a second LLM that checks the primary agent's completion claims) is an internal verification step not commonly surfaced in harness tooling at this star count.

## What stands out immediately

- Single Rust binary; MCP-native; runs as interactive CLI, non-interactive pipe, daemon, WebSocket server, or ACP agent
- Policy via `.agents/guardrails.toml`: pre-call guards, post-result hooks, post-turn validators — distinct from per-session approval prompts
- Supervisor model: a second LLM plans work and verifies completion claims against the primary agent's output
- Context compression and cross-session lesson recall
- Supports roles, workflows, Agent Skills, local tools, and "specialist" agents via taps (a packaging concept)
- Model providers: Octomind Cloud, OpenRouter, Anthropic, OpenAI, DeepSeek, Ollama and others
- `--sandbox` restricts writes to working directory on Linux and macOS (not confirmed on Windows)
- Benchmark claim: 24 of 25 tasks on vendor's own published benchmark vs. 23 for Claude Code and 19 for OpenCode — vendor-run, unverified
- 615 stars; 2,776 commits — suggests the project predates its current trending visibility

## Why clawfit should care

Octomind's policy-as-code model is a distinct harness governance pattern. The closest clawfit comparators are Open Duet (approval modes), deepseek-harness ("everything is a plugin"), and ECC (config-driven performance). None of them center policy expressibility in a versionable file. If declarative guardrails become a category — vendor-auditable, CI-diffs — clawfit would need a `policy_model` dimension (approval-prompt vs. declarative-file vs. programmatic-hook) in its harness scoring. The supervisor model is a second signal for internal agent verification loops (first: OpenAI Pando's internal review chain, 2026-10-22), though Pando is a different context (security disclosures). Octomind applies the pattern to general coding tasks.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/wrapper** (single-binary agent harness wrapping model access, tool execution, and policy enforcement)
- **Level 3 secondary** (TOML guardrails function as a lightweight SSOT governance layer for agent policy)
- clawfit: `agents.json` candidate pending deterministic cost/latency data and independent benchmark replication; schema has no `policy_model` field

## Claims to verify

- Benchmark methodology: "own benchmark" is not SWE-bench or any named public suite; task set, scoring, and comparison conditions are vendor-defined
- Supervisor model cost: calling a second LLM to verify every turn — what's the overhead at scale?
- Rust binary reproducibility: can builds be verified independently?
- "Taps" packaging: how are specialist agents distributed and vetted?
- TOML sandbox enforcement: `--sandbox` on Linux/macOS restricts writes to CWD; Windows status unstated

## Status

- Tracking: first signal (munderdiffl.in 2026-11-04)
- Registry action: none — no deterministic cost/latency data; vendor benchmark not independently verified; watch for SWE-bench or LiveCodeBench score
