# Research Watch: agentmemory — Persistent Memory for AI Coding Agents

- Repo/Link: https://github.com/rohitg00/agentmemory
- Source: GitHub Trending TypeScript #1 / ALL Languages #6
- Stars: 14.1k (+ 1,609 today)

## Why this is worth watching

agentmemory is a TypeScript-native persistent memory system targeting AI coding agents that claims 95.2% recall (R@5 on LongMemEval-S) against mem0's stated 68.5% — a gap large enough to be structurally meaningful if independently confirmed. Its MCP server exposes 51 tools, making it one of the largest MCP tool surfaces in the Level 5 memory cluster (Engram ships 17, by comparison). The +1,609 single-day star velocity on a 14.1k-star repo is anomalous and warrants a discovery-event check before treating as organic growth.

## What stands out immediately

- Built on an internal runtime called "iii" (primitive-based: functions, triggers, KV state, streams) that replaces Express, Postgres, Redis, and pm2 — architectural lock-in risk worth inspecting
- 4-tier memory consolidation: working → episodic → semantic → procedural; mirrors Hippo's biologically-inspired hierarchy (claim to inspect: independently validating consolidation behavior at tier boundaries is non-trivial)
- Triple-stream retrieval: BM25 + vector similarity + knowledge graph, fused via Reciprocal Rank Fusion — most architecturally complete retrieval stack in this taxonomy so far
- 12 lifecycle hooks for auto-capture across Claude Code, Codex CLI, OpenClaw, Hermes, pi, OpenCode; passive capture is a differentiator over Engram's explicit `mem_session_start/end` pattern
- SHA-256 dedup with 5-minute window and pre-storage secret stripping — privacy-aware pipeline, relevant for `data_sensitivity: confidential` profiles
- 51 MCP tools span memory ops, governance, scheduling, and multi-agent coordination (leases, signals, routines) — the multi-agent coordination scope pushes it into L3-adjacent territory
- Token efficiency claim: ~1,900 tokens/session vs 22K+ in static-file approaches (vendor-authored, awaits independent verification)
- v0.9.21 (May 2026), 118 source files, 950+ passing tests — not a prototype shape

## Why clawfit should care

The multi-agent coordination MCP tools (leases, signals, routines) are a Level 5 → Level 3 bleed not seen in prior memory-layer entrants; if this is validated, agentmemory would need a secondary Level 3 classification. For clawfit's recommendation engine: the `data_sensitivity: confidential` + auto-capture hook model is directly relevant to `network: offline` profiles — the iii runtime's self-contained SQLite storage and no-external-DB posture supports this. The 51-tool MCP surface also makes it a scoring-axis edge case: current memory tools in the taxonomy top out at 17 tools (Engram), so a sub-category note for "high-tool-count MCP memory" may be warranted if a second tool crosses ~30 tools.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / MCP / context layer** (primary; SQLite-backed, MCP-native, 4-tier consolidation)
- **Level 4 — Capability / plugin / tool-use layer** (secondary; 51-tool MCP server functions as a broad capability surface for any MCP client)
- Level 3 adjacency flagged (multi-agent leases, signals, routines via MCP) — insufficient to promote without independent confirmation that these tools are used for cross-agent governance rather than intra-session coordination

## Status

- New signal; high star velocity but discovery-event origin unconfirmed — treat recall benchmarks and token-efficiency figures as claims to inspect until independent reproduction exists. Monitor for organic vs. trending-driven retention over next 7 days.
