# Research Watch: DeepSeek Harness — "Everything is a Plugin" Coding Agent Framework

- Repo: https://github.com/deepseek-ai/deepseek-harness (⭐93.7k)
- Source: GeekNews front page ("DeepSeek Harness - 모든 구성 요소를 플러그인으로 만든 오픈소스 코딩 에이전트", 2026-08-14); GitHub Trending

## Why this is worth watching

DeepSeek Harness (`dsh`) is a coding agent framework from DeepSeek AI built around a "Everything is a Plugin" architecture using Cordis, a framework for spatiotemporal composability. At 93.7k stars with no official releases (still in developer preview), it has accumulated more stars than most established agent frameworks while remaining pre-1.0 — reflecting DeepSeek's existing large developer audience. The Cordis-based plugin architecture represents a structural approach to agent extensibility that differs from monolithic harness designs (DeerFlow, LifeOS) or configuration-file-based harnesses (Herdr): the core IS the plugin manager, not a system that happens to support plugins.

## What stands out immediately

- **"Everything is a Plugin" as a hard architecture constraint**: not a plugin system bolted onto a monolithic core — the core IS the Cordis plugin manager; all agent capabilities, provider integrations, and behaviors are plugins
- **Cordis framework basis**: the harness inherits its composability model from a paper titled "A Programming Paradigm for Spatiotemporal Composability" — formally described programming paradigm, not an ad-hoc plugin registry
- **TypeScript + Python polyglot**: TypeScript core (tsconfig.json, package.json, pnpm-workspace.yaml), Python components (pytest.ini), YAML configuration — agent loop is TypeScript with Python tool interfaces
- **Developer preview with breaking changes expected**: explicit "compatibility-breaking changes possible" note signals rapid early-stage iteration, not a stable release
- **Built-in Web UI at port 3080**: browser-based control surface alongside CLI — L6-adjacent capability bundled with the L2 harness
- **93.7k stars, 8.6k forks, zero release tags**: star accumulation without a release tag indicates organic growth from DeepSeek's developer community, not a launch-event spike
- **MIT licensed**: permissive, contrasting with AGPL-3.0 (paseo), Modified Apache 2.0 (holaOS), and proprietary options

## Why clawfit should care

The "Everything is a Plugin" architecture produces a qualitatively different extensibility model than clawfit's current tracked harnesses. Comparison:

- **DeerFlow** (2026-03-30, L2): orchestration harness with sub-agent dispatch and persistent memory — extensible via workflows but core is fixed
- **LifeOS** (2026-08-10, L2): named subsystem architecture (Synapse, Atlas, Ledger, Cortex) — extensible via configuration, structure is prescribed
- **prime-agent** (2026-08-07, L1/L2): RLM-based with Continual Harness — extensible via self-modification, fundamentals are fixed
- **deepseek-harness**: no fixed core behavior; capability emerges entirely from the plugin composition set

If all capabilities are plugins, adding or removing capabilities requires only plugin management — architecturally auditable and constrainable for `governance_need: hard` profiles in a way that monolithic harnesses are not. **Schema watch:** `extensibility_model: [fixed | configurable | plugin-composition | self-modifying]`.

## Preliminary interpretation

- **Level 2 primary — Harness/Wrapper**: a coding agent framework that wraps LLM providers behind a plugin-composed interface, providing the execution layer between base models and task completion
- **Level 6 secondary**: built-in Web UI at port 3080 — browser-based interface for agent control alongside CLI

## Claims to verify

- **Cordis provenance**: verify whether "A Programming Paradigm for Spatiotemporal Composability" is a published academic paper or an internal specification, and whether Cordis is independently maintained or internal to this project
- **Plugin composition model completeness**: verify whether any fixed core behaviors exist (authentication, model routing, session management) or whether these are also plugins with reference implementations that can be swapped
- **Star velocity source**: 93.7k stars without a release is extraordinary — verify whether this accumulated over a long pre-release development period or via a single viral event; the GeekNews post (5 pts) suggests the GeekNews audience discovered it today, meaning prior accumulation was from other channels
- **Python interface scope**: whether Python components are tool-execution adapters or whether Python agents can author plugins alongside TypeScript

## Status

- 93.7k⭐, MIT, developer preview, no official releases — above 5k registry threshold by star count but no deterministic cost/latency data (no documented pricing, runtime is self-hosted)
- **Registry eligibility: no** — no agent schema field maps cleanly without a formal release defining the capability surface
- **First signal for "pure plugin-composition coding agent harness" from a major model provider (DeepSeek)**
- **No canonical section change**: single signal; two-signal rule requires a second harness with the same Cordis-style pure plugin-composition architecture before adding a stable L2 sub-type
