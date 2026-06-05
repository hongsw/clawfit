# Research Watch: Anthropic Defending Code Reference Harness

- Repo/Link: https://github.com/anthropics/defending-code-reference-harness
- Source: Hacker News (#2, 224 points)

## Why this is worth watching
Anthropic open-sourced a reference harness for AI-powered vulnerability discovery — the tooling behind Project Glasswing, where Claude Mythos Preview scanned 1,000+ open-source projects and identified 23,019 issues (6,202 high/critical severity). This is the first first-party Anthropic open-source release explicitly in the security domain, and signals that AI-native vulnerability discovery is productizing beyond one-off research.

## What stands out immediately
- Reference harness explicitly, not a production tool — README states unmaintained, no contributions accepted
- Resource-intensive: ~10K uncached input tokens/min + ~2K output tokens/min per agent; costs hundreds to thousands of dollars per run depending on model
- Design philosophy mirrors "shop jigs" — purpose-built customizable tools, not universal scanners
- Practical limitation: effective use requires custom harness development tailored to specific vulnerability patterns; significant expertise needed for triage and false positive reduction
- Connected to Project Glasswing: Claude Mythos Preview and Claude Security (enterprise public beta) are the production versions
- HN comment thread emphasizes cost-benefit only positive for high-severity legacy codebase audits

## Why clawfit should care
This is the fourth signal in the security cluster (Shannon L1 + Strix L1 + Decepticon L2 + this L4 reference harness). It occupies a new cell: **first-party vendor capability-layer tooling for security scanning**. Unlike Shannon and Strix (autonomous agents that find/exploit), this harness provides the *scaffolding* for custom AI-driven security scanning pipelines. Also notable: the unmaintained/reference status is a counterpoint to registry promotion — it illustrates the "reference signal with no registry candidate" pattern. For the `security-testing` task type and `governance_need: hard` schema additions this cluster has been motivating, this is a confirming signal.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability/Tool-use layer (primary)**: Reference scanning harness providing tool scaffolding for AI-driven vulnerability discovery; not an autonomous agent (no L1 loop) and not an orchestration harness (no multi-agent dispatch, no L2 structure)
- **L1 LLM-axis adjacent**: Claude Mythos Preview is the LLM substrate; the harness itself is model-configurable

## Status
- First signal for "first-party vendor security scanning harness" sub-type at L4.
- No registry candidate: explicitly unmaintained reference implementation.
- Confirms `task: security-testing` as a schema-addition candidate (fourth cluster signal: Shannon + Strix + Decepticon + this).
- Watch: if Anthropic releases a maintained successor or `claude-security` SDK with similar scaffolding.
