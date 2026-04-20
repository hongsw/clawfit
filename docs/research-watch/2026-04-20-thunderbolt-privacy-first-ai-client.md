# Research Watch: Thunderbolt — Privacy-First Multi-Model AI Client

- Repo/Link: https://github.com/thunderbird/thunderbolt
- Source: GitHub Trending (+695 stars today, 2,205★ total)

## Why this is worth watching
Thunderbolt is an open-source, cross-platform AI client from the Thunderbird organization (Mozilla-adjacent) that explicitly frames itself around data ownership and vendor lock-in elimination. "AI You Control: Choose your models. Own your data." With on-premises deployment support and compatibility with Ollama/llama.cpp/OpenAI-compatible APIs, it fills a gap for enterprises that need AI interfaces without SaaS data exposure — a profile that appears in clawfit's `confidential` data_sensitivity tier.

## What stands out immediately
- Cross-platform: web, iOS, Android, macOS, Linux, Windows
- Compatible with frontier, local, and on-premises models (no single-vendor lock-in)
- Mozilla Public License 2.0 with Mozilla Community Participation Guidelines governance
- Security audit in progress — signals real enterprise production intent
- TypeScript 97.7% codebase; Rust minority
- 902 commits on main — not a weekend project

## Why clawfit should care
- Directly relevant to `data_sensitivity: confidential` and `governance_need: hard` profiles where a general AI chat interface is needed but Claude.ai/ChatGPT data sharing is not acceptable
- The "choose your models" framing maps to clawfit's multi-LLM recommendation axis — this tool is a runtime that surfaces that choice to non-developer users (exec, PM)
- Thunderbird's existing enterprise install base (~20M users) gives this product a plausible enterprise adoption path unlike most early-stage AI clients

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface layer** (cross-platform AI client for end-user interaction with multiple model backends)
- Possibly also Level 1 if it evolves into a platform for running agent workflows, not just chat

## Status
- Tracking: early-signal, 2.2k stars
- Revisit at 10k stars or enterprise beta announcement
