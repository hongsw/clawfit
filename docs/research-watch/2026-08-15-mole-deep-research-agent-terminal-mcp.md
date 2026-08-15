# Research Watch: lajosdeme/mole

- Repo/Link: https://github.com/lajosdeme/mole
- Source: Hacker News front page "Show HN" (2026-08-15, 44 pts)

## Why this is worth watching
Mole is a Go-based deep research agent for the terminal with three design constraints that distinguish it from other research agents: a **hard-enforced spending budget** (API calls are reserved before execution and settled after, with zero measured overshoot), **verified citations** (claims require verbatim quotes extractable from source pages — unverifiable claims are discarded), and a **local-data privacy boundary** (local CSV/folder analysis sends only aggregated statistics to the model, not raw content). It also serves as an MCP daemon, allowing coding agents to drive research in toolkit mode.

## What stands out immediately
- Single static binary (Go) — zero dependency install, matches ante (2026-08-10) in distribution simplicity
- MCP daemon mode: coding agents can use Mole as a research tool without a separate research agent loop
- Budget enforcement at the call-reservation layer (not post-hoc) — distinct from soft budget warnings in other research agents
- Local data privacy boundary is explicitly tested — not just documented
- 83 stars at HN launch (below 100-star tracking threshold, flagged for elevation if stars grow post-HN spike)

## Why clawfit should care
The enforced-budget constraint maps directly to clawfit's `monthly_budget` dimension — Mole is the first research agent that makes budget adherence a hard architectural guarantee rather than a setting. The MCP daemon mode means it could appear as a capability tool (L4c) inside a coding agent session, not just as a standalone research loop (L3). The `data_sensitivity: confidential` profile (offline_mid_codegen) would benefit from Mole's local-data privacy boundary more than from general research agents.

## Preliminary interpretation
Current best reading:
- **Level 3 — Research Loop System** (primary): autonomous research decomposition, search, citation verification
- **Level 4c — MCP Capability Layer** (secondary): MCP daemon mode lets coding agents invoke it as a tool

## Status
- Watching: HN front page signal; 83 stars below registry threshold — not eligible for tools_registry.json until ≥100 stars
- Architecturally notable: budget-enforced research + local-privacy boundary — two design features that directly match clawfit scoring dimensions
- Two-signal rule: not applicable (no canonical section for "budget-enforced terminal research agent" yet)
