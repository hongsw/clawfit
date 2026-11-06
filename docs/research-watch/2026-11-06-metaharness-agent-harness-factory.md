# Research Watch: metaharness — Factory for Generating Owned, Customized Agent Harnesses

- Repo: https://github.com/ruvnet/metaharness (⭐739)
- Source: WebSearch / agent harness release search 2026-11-06

## Why this is worth watching

metaharness is not itself an agent harness — it is a scaffold that generates a branded, owned agent harness from a GitHub repo or a blank template. The output is an npm-publishable package with its own CLI, MCP server, memory namespace, skills, slash commands, and governance policy. The concept is architecturally one level above harnesses: a meta-layer that customizes harnesses at the team or product level without requiring a fork of an existing framework. The README explicitly states "not another agent framework — a factory for agent frameworks." At v0.1.x beta with 739 stars, the idea is early but structurally distinguishable from every other harness tracked in clawfit.

## What stands out immediately

- Generates a fully owned npm-publishable harness package from `npx metaharness` or a browser Studio
- Generated harnesses include agents, skills, slash commands, MCP tools, scoped memory namespace, governance policy
- Supports 10 host adapters: Claude Code, Codex, pi.dev, Hermes, OpenClaw, RVM, Copilot, OpenCode, GitHub Actions, Prime Agent
- MCP is default-deny in generated harnesses; modes: off, local, remote
- "Darwin Mode": harness tests config changes in a sandbox and retains only measured improvements (self-tuning)
- Router picks cheapest model predicted to meet a quality bar (cost-optimization layer built into generated harnesses)
- 19 vertical templates: coding, research, legal, trading, and others
- Witness-signed releases using Ed25519; Rust kernel
- Repo analysis on generation is static (does not execute repo code)
- v0.1.x beta; 1,045 commits; 220 ADRs — substantial pre-release development
- SWE-bench claims in README not verifiable from the README alone

## Why clawfit should care

metaharness sits at a layer clawfit doesn't model: "harness generation" rather than harness use. If this pattern takes hold — teams generating their own harness rather than adopting a shared one — clawfit's agent registry becomes less representative of what teams actually run. The Darwin Mode (self-tuning) and built-in cost router are also signals for a convergence between L2 (harnesses) and L5 (evaluation/optimization): harnesses that self-evaluate their own configuration are a qualitatively different category from harnesses that are statically configured. The 19 vertical templates overlap with clawfit's `task` and `org_profile` dimensions; a harness that generates task-specific policy from a template could replace or complement the scoring logic clawfit applies at recommendation time.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/wrapper** (the generated artifact is a harness; the factory itself is a meta-tool at L2)
- **Level 3 secondary** (Darwin Mode and governance policy generation touch the SSOT/team-workflow layer)
- clawfit: not a registry entry; signals a gap in the taxonomy — no current level describes "harness factory" or "harness generation layer"; potential L2a sub-category

## Claims to verify

- SWE-bench score claimed in README: methodology and task set not specified
- Darwin Mode (self-tuning): what benchmark measures "improvement"? Manual or automated? How is regression detected?
- 10 host adapters: which have been tested end-to-end vs. which are listed as "supported"?
- Ed25519 witness signing: what's the trust model? Who holds signing keys for generated harnesses?
- v0.1.x beta: API stability and upgrade path for generated harnesses are unstated

## Status

- Tracking: first signal (WebSearch / ruvnet/metaharness, approximately 2026-10-28 to 2026-11-06)
- Registry action: none — meta-tool, no cost/latency data; watch for adoption metrics (how many harnesses generated, any notable organizations)
