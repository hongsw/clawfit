# Research Watch: Grok Build — xAI's Open-Source TUI Coding Agent

- Repo/Link: https://github.com/xai-org/grok-build
- Source: Hacker News (196 points, 2026-07-16)

## Why this is worth watching
xAI has open-sourced Grok Build, a full-screen TUI coding agent written in Rust that competes directly with Claude Code, Goose, and OpenInterpreter. It ships with headless mode for CI/CD integration and supports the Agent Client Protocol (ACP), placing it in the same interoperability tier as OpenInterpreter's Rust rewrite. First coding agent in the tracked set to explicitly brand itself via its underlying LLM (Grok).

## What stands out immediately
- Full-screen terminal UI with mouse support; headless mode for scripting and CI/CD
- Capabilities: codebase analysis, file editing, shell execution, web search, long-running task management
- Built in Rust (cold-start advantages, same trend as OpenInterpreter Rust rewrite)
- ACP (Agent Client Protocol) support — plugs into editors as an embedded agent
- Auth via browser on first launch; cloud-dependent on xAI inference (Grok models)
- Precompiled binary distribution (macOS, Linux, Windows)

## Why clawfit should care
Grok Build is a direct competitor to every L1 coding agent already in the registry (Claude Code, Goose, Crush, OpenCode, Aider). It is the second tracked agent to support ACP natively (after OpenInterpreter Rust). ACP as a shared interoperability layer is becoming a credible standard — clawfit's registry should capture ACP support as a field. Network dependency: fully online (xAI auth required), which constrains it for `offline_mid_codegen` and governance-hard profiles.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (primary): full-stack TUI coding agent with file edit, shell, web search
- **Level 2 — Harness** (secondary): ACP embedding mode enables editor-level integration

## Status
- Added to tools_registry.json as `grok-build`
- Schema watch: `acp_support: true/false` as coding agent registry field; `llm_brand_alignment: [vendor-agnostic | branded]`
