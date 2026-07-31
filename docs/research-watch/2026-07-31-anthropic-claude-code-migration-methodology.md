# Research Watch: Anthropic's Official Claude Code Large-Scale Migration Methodology

- Repo/Link: https://claude.com/blog/ai-code-migration
- Source: GeekNews ("Claude Code로 대규모 코드 마이그레이션을 수행한 방법")

## Why this is worth watching
Anthropic's own methodology guide for large-scale code migration using Claude Code with dynamic multi-agent workflows. Covers two real migrations: Jarred Sumner's Bun Zig→Rust (1M lines, $165k API tokens, 100% test suite passing) and an internal Anthropic Python→TypeScript project (165k lines; compile time dropped from 30 min to 2 sec). The 6-step framework (rulebook → stress-test → multi-agent translation → compile → smoke test → parity verification) is the first first-party production migration playbook for agentic code transformation. Distinct from the Pragmatic Engineer coverage (already tracked 2026-07-28) by its methodology orientation and inclusion of the internal Anthropic case.

## What stands out immediately
- "Adversarial reviewers" pattern: separate Claude instances explicitly tasked with refuting the migration output — structural quality gate, not prompt-softening
- Model stratification: smaller models for fan-out implementation, larger models for review — direct validation of cost-tiered agent design
- Core insight: "You fix the process (loop) that produced the code, not individual failures" — loop-level debugging is the unit of work, not file-level
- $165k in API tokens for a 1M-line production migration: establishes a rough cost-per-KLOC benchmark for migration-class tasks

## Why clawfit should care
Confirms that `orchestration` is a distinct primary task category requiring different tooling than `code-gen`. The model-stratification pattern (cheap models for bulk, expensive for review) maps directly to clawfit's budget filter. The $165k benchmark anchors what `monthly_budget: high` actually means for migration-class work. Reinforces that `network: online` + `governance_need: none` is the practical requirement profile for running large multi-agent migration workflows.

## Preliminary interpretation
- **Level 2 — Harness/methodology** (multi-agent orchestration workflow for large-scale transformation tasks)

## Status
- Second signal for the migration use case (first: Pragmatic Engineer 2026-07-28); this signal is the official methodology framing. No new registry entry needed; strengthens existing `code-gen` + `orchestration` task co-occurrence pattern.
