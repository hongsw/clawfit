# Research Watch: Kimi CLI (MoonshotAI) — Terminal Coding Agent with MCP and ACP Support

- Repo: https://github.com/MoonshotAI/kimi-cli (⭐9,377)
- Also see: `docs/research-watch/2026-07-18-kimi-k3-moonshot-open-weights-benchmark.md` (today's K3 LLM signal); https://github.com/MoonshotAI/kimi-code (declared active successor, installs auto-migrate); https://github.com/xai-org/grok-build (`docs/research-watch/2026-07-16-grok-build-xai-open-source-coding-agent-tui.md`)
- Source: GitHub Trending (All Languages, rank 11; Python, rank 6), 2026-07-18

## Why this is worth watching

MoonshotAI shipping both a frontier LLM (K3, tracked today) and a CLI coding agent creates a vertical integration pattern — same lab controlling the model and the agent runtime — previously seen only at Anthropic (Claude + Claude Code) and xAI (Grok + Grok Build). The structural implication: labs pursuing this pattern can tune agent-model interaction at the pre-training level, potentially closing the "generic wrapper" gap that neutral harnesses face. Kimi CLI / Kimi Code is the clearest non-English-first entry in the L1 terminal coding agent tier; MoonshotAI's explicitly Chinese-market positioning makes this a distinct access surface that existing clawfit registry entries do not cover.

## What stands out immediately

- **MCP support via `kimi mcp` subcommand:** adds and manages HTTP-based and stdio-based MCP servers with OAuth handling — full parity with Claude Code on MCP client capability
- **Agent Client Protocol (ACP) for IDE embedding:** second tracked runtime to support ACP alongside Grok Build; targets Zed, JetBrains, and any ACP-compatible editor — broader than MCP for editor integration
- **Shell mode with Ctrl-X toggle:** surfaces an explicit interactive shell mode distinct from the main agent loop; Claude Code blends these; the explicit toggle is an architectural choice, not an oversight
- **Apache 2.0 license:** commercially usable without restriction; same tier as Grok Build and agentscope
- **Actively being deprecated in favor of `MoonshotAI/kimi-code`:** existing installs auto-migrate; the research-watch target should be the successor repo (`kimi-code`) for future tracking; this signal captures the ecosystem entry
- **Python 78.5%:** contrast with Grok Build (Rust TUI) and Goose (Go); Python base makes extension and forking lower-friction
- **9,377 stars, 1,160 forks, 767 open issues:** fork ratio (1:8 stars) and open issue count suggest significant adoption and downstream modification; the high open issue count likely reflects the migration period from kimi-cli to kimi-code
- **Last pushed Jul 16, 2026** — same date as K3 announcement, not coincidental; coordinated release signals the vertical integration is intentional

## Why clawfit should care

Two distinct scoring implications:

1. **Model-native agent as a distinct profile.** Kimi CLI/Code routes exclusively through Kimi models. For clawfit profiles where `network: online` and `llm_brand_alignment: branded` are relevant, this is a third vendor-native terminal agent (after Claude Code and Grok Build). Neutral harnesses like Goose and OpenHands accept any LLM backend — model-native agents cannot. This is a structural axis missing from `agents.json`.

2. **ACP support as a differentiator.** ACP support is rare enough that tracking it as a binary (`acp_support: true/false`) could help distinguish harnesses with vs. without editor embedding capability. The ACP-capable tier currently has only Grok Build and Kimi CLI/Code; Claude Code uses MCP for editor integration.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base agent runtime (primary):** CLI coding agent that runs directly on the user's terminal, executes shell commands, edits files, and invokes web search; architecturally identical to grok-build, claude-code, and crush at this level
- **Level 4c — MCP client capability (secondary):** full MCP client support makes it a consumer of the L4c server ecosystem, not a producer; secondary classification only

## Claims to verify

- Kimi-code (successor) star count and feature delta vs. kimi-cli — the future registry entry, if any, should target kimi-code
- Whether kimi-code supports local Kimi model inference (vs. cloud-only API calls) — determines offline viability
- ACP vs. MCP for editor integration: whether these compete or compose in practice
- K3 model performance on the benchmark tasks that clawfit profiles care about (code-gen, qa) — the model-native advantage only holds if K3 is competitive on the relevant tasks at the agent level

## Status

- 9,377 stars — above the 5,000 registry threshold on star count, BUT: (a) actively being deprecated in favor of kimi-code; (b) model-native agent schema doesn't map to existing `agents.json` fields without adding `llm_brand_alignment`; (c) no deterministic public latency/cost data for agent-level (not LLM-level) performance. **Hold registry entry; switch watch target to MoonshotAI/kimi-code.** Schema watch: `acp_support: true/false`; `llm_brand_alignment: [vendor-agnostic | branded]`; `successor_repo: string`.
