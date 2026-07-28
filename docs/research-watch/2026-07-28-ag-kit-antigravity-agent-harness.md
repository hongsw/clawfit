# Research Watch: ag-kit — Antigravity Agent Engineering Harness

- Repo/Link: https://github.com/vudovn/ag-kit
- Source: GitHub Trending (all languages, 2026-07-28) — ⭐7,950

## Why this is worth watching
ag-kit is a structured agent engineering harness targeting Google's "Antigravity" AI platform (Google's next-generation agent SDK). Its architecture — 20 specialist agents, 47 reusable skills, 13 slash-command workflows, persistent memory, MCP integration, and a native safety hook — closely mirrors the oh-my-pi / Hermes / Kiro family of harnesses, but targets Google AI as the primary LLM backend rather than Claude or Codex. First harness signal for a Google-AI-first harness at meaningful star count.

## What stands out immediately
- **20 specialist agents** with defined domain roles (not generic system prompts — agent definitions with scope constraints)
- **47 reusable skills** as progressive domain knowledge units (same conceptual model as Claude skills packs)
- **13 workflow templates** exposed as slash commands: `/plan`, `/coordinate`, `/orchestrate`
- **Persistent memory system** for project decisions and context across sessions
- **Native safety hook** that blocks destructive commands at the harness layer (root filesystem deletion and similar)
- **MCP integration** for external tool connections
- **Repo validation via CI** and automated testing — suggests production-grade intent
- TypeScript primary language; 7,950 stars on first trending appearance

## Why clawfit should care
ag-kit is a second independent signal for the "structured multi-role harness" pattern: the first (oh-my-pi, ⭐19.7k) targets terminal/Rust; ag-kit targets TypeScript/Google AI. If Mastra (2026-07-27, ⭐26.6k) is the framework-layer L2 for TypeScript, ag-kit is the harness-configuration layer above it — similar to how oh-my-pi builds on top of generic CLI agent runtimes. The Google Antigravity target is a registry gap: clawfit currently has no tool entries explicitly optimized for the Google AI / Gemini family. If ag-kit tracks Antigravity's release, this could become a significant recommendation entry for Google-ecosystem orgs.

## Preliminary interpretation
- **Level 2 — Harness / Meta-wrapper** (primary)
- **Level 4b — Skills / Capability packs** (secondary, via 47 reusable skill definitions)
- **Level 5 — Memory / Context management** (secondary, persistent memory system)

## Status
- First signal — ⭐7,950, GitHub Trending
- Below 5k threshold? No — 7,950 exceeds threshold but benchmark/latency data absent
- No registry entry this run: Google Antigravity platform maturity and API cost/latency data unavailable for `agents.json` fields
- Second signal for "structured multi-role harness" pattern (cross-day with oh-my-pi 2026-07-25)
- Monitor for: Antigravity platform launch date, benchmark data, registry addition candidate
