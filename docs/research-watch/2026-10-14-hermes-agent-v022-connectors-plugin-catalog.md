# Research Watch: Hermes Agent v0.22.0 — Native Connectors, Plugin Catalog, and Local llama.cpp Runtime

- Repo/Link: https://github.com/NousResearch/hermes-agent (⭐253,700)
- Stars: 253,700
- Source: GitHub release v0.22.0 (2026-10-13); last tracked: v0.20.0 (2026-08-22)

## Why this is worth watching
Hermes Agent v0.22.0 (released October 13) is the first release since v0.20.0 to introduce platform-level connectors (Linear, Notion) through a centralized Nous tool gateway, a 600-plugin catalog, and a one-click llama.cpp runtime for fully local inference. These changes shift Hermes from a standalone coding agent toward a multi-platform agent hub with curated tooling. The Python 3.14 runtime requirement and signed desktop packages signal a maturity push toward consumer-facing distribution alongside developer use.

## What stands out immediately
- **Connectors via Nous gateway:** Linear and Notion connections now route through a centralized gateway; "Connectors" page replaces the MCP tab — implies Nous is building platform-level tooling middleware, not just MCP forwarding
- **600-plugin catalog:** Reviewed plugins installable from desktop or CLI; memory providers (Honcho, Supermemory, Mem0, etc.) and Langfuse moved from bundled to catalog — a shift from opinionated defaults to user-curated tooling
- **llama.cpp one-click runtime:** Download, pause, and resume open models for fully local inference without API keys; the onboarding chat now runs on a free trial model (`nous/welcome`) to get started without credentials
- **Signed desktop packages:** Windows MSIX (including Microsoft Store), signed macOS Apple Silicon builds, `hermes pm` for pinned dependency management — enterprise distribution readiness
- **Claude 5.5, GPT-6, Gemini 4 Argon added:** Model support tracks the current frontier; provider outage handling improved
- **Browser credential safety:** Browser agent can sign in via 1Password, Bitwarden, or Hermes's own vault without exposing the password to the model — directly addresses a known agent security concern
- **Subagents now visible and steerable:** Previously opaque subagent execution is now surfaced in the UI — key for debugging multi-agent workflows
- **Codebase reduced by ~1/3:** The bundled-to-catalog migration of memory and integration plugins reduced codebase size; suggests cleaner plugin API boundary

## Why clawfit should care
- The shift from bundled integrations to a plugin catalog is architecturally significant for clawfit's L4 taxonomy: Hermes is now a platform with pluggable capabilities, not just an agent with built-in tools
- The Nous tool gateway (for Linear, Notion connectors) is a new intermediary layer between agent harnesses and SaaS tools — distinct from direct MCP connections; clawfit may need to track "gateway middleware" as a separate L4 sub-pattern
- The llama.cpp integration brings Hermes into direct overlap with `hardware: local` + `network: offline` profiles in clawfit's recommendation matrix
- The credential isolation model (vault-backed browser agent) is the first harness-level implementation of a pattern clawfit's `task: security-audit` scoring has been implicitly assuming but not tracking
- Python 3.14 requirement is a breaking change for teams on older runtimes; KittenTTS incompatibility is a concrete example of ecosystem tension when harnesses upgrade runtimes aggressively

## Preliminary interpretation
Current best reading:
- **Level 2 primary — Agent Harness/Wrapper** (multi-platform, multi-provider agent runtime)
- Secondary at **Level 4 — Capabilities/Plugins/MCP**: 600-plugin catalog + Nous gateway middleware is a platform-level L4 capability layer
- Tertiary at **Level 6 — Human Interface**: desktop app, signed packages, 16-language UI are L6 user experience signals

The architectural direction is toward a consumer-grade platform: signed packages, Microsoft Store distribution, no-API-key onboarding, and 16-language UI are not harness-developer features. Hermes is expanding from developer tool to general AI assistant, with the harness architecture as its foundation. The Nous gateway pattern — routing third-party integrations through Nous-controlled middleware — is the most strategically important new signal: it creates a dependency layer that could become significant if it gains adoption.

## Claims to verify
- "600 reviewed plugins" — what does "reviewed" mean? No criteria published in the release notes; confirm whether this is manual or automated review
- Nous tool gateway: hosted infrastructure, not local; privacy and data routing implications for enterprise use are undocumented at release
- llama.cpp one-click runtime: model availability, licensing, and performance relative to native llama.cpp (wrapper overhead) not yet independently measured
- Browser credential safety: vault-backed credential isolation is described but not independently audited at v0.22.0 launch
- Microsoft Store availability: listed as MSIX-compatible but Store listing status was not confirmed at time of tracking

## Status
- Already in tracking record (⭐253k; v0.20 tracked 2026-08-22)
- This document covers the v0.20 → v0.22.0 delta
- No new registry entry needed: Hermes is already in agents.json
- Watch: Nous gateway adoption and governance model, plugin catalog quality over time, whether the connector pattern becomes the dominant L4 integration pattern vs. direct MCP
