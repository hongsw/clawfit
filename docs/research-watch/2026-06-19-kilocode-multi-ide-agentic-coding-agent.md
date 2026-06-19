# Research Watch: Kilo Code — Multi-IDE Agentic Engineering Platform

- Repo/Link: https://github.com/Kilo-Org/kilocode
- Source: GitHub Trending (1,345 stars today, 22,109 total)

## Why this is worth watching
Kilo Code is a multi-IDE open-source agentic coding agent (VS Code, JetBrains, CLI) with 22K stars and 1,345 today — one of the largest single-day star gains for any L1 coding agent in recent scans. Its MIT license, zero-API-key-required framing, and 500+ model support position it as a direct competitor to Roo Code, Cline, and Cursor. The five-specialist-agent model (Code, Plan, Ask, Debug, Review) mirrors the multi-role pattern Roo Code pioneered but extends to JetBrains.

## What stands out immediately
- **Multi-IDE scope**: VS Code + JetBrains + CLI — broader than any current L1 registry entry
- **500+ model support** with mid-task model switching (no lock-in)
- **5 specialized agents**: Code (implementation), Plan (architecture), Ask (codebase Q&A), Debug (troubleshooting), Review (quality)
- **`kilo run --auto`**: headless CI/CD autonomous mode — executes without permission prompts in trusted environments
- MIT license; no API key lock-in; TypeScript (83.5%) + Kotlin (12%)

## Why clawfit should care
Kilo Code occupies the same L1 cell as Cline and Roo Code but introduces JetBrains reach that no current registry entry covers. The five-agent specialization model (vs. Cline's single-agent model) and mid-task model switching are architecturally distinct from existing entries. Registry threshold (22K stars) is met. This is the first L1 coding agent to credibly target both VS Code and JetBrains ecosystems simultaneously in this taxonomy.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime (IDE multi-surface sub-type)**
- L1 primary (autonomous coding agent with full tool-use loop)
- L7 secondary (VS Code + JetBrains extension as primary user surface)
- Distinct from Cline (VS Code only), Roo Code (VS Code + multi-role), Cursor (proprietary fork), Claude Code (terminal)

## Status
- Registry threshold met (22K+ stars) — adding to tools_registry.json as a held first signal
- Promotion criterion for map mutation: second independent project citing Kilo Code JetBrains support OR confirmed JetBrains Marketplace listing with 1k+ installs
