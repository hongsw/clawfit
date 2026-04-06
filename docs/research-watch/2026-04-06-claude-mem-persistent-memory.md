---
# Research Watch: thedotmack/claude-mem — persistent memory compression for Claude Code

- Repo: <https://github.com/thedotmack/claude-mem>

## Why this is worth watching
**45,600 stars** — one of the most-starred Claude Code plugins in existence. This level of adoption for a memory layer tool confirms that cross-session context loss is among the most painful friction points for Claude Code users. The technical approach (hooks + local worker + SQLite + Chroma vector DB) is substantially more sophisticated than typical `CLAUDE.md` approaches.

## What stands out immediately
- **5 lifecycle hooks:** session start/end, user prompt, tool execution — captures observations automatically
- **Worker service** on port 37777 — HTTP API for memory operations, runs as background daemon
- **Dual storage:** SQLite (sessions, observations, summaries) + Chroma (semantic vector search)
- **Progressive disclosure retrieval:** layers memory by token cost — cheap context first, expensive semantic search on demand
- **Hybrid search:** full-text + semantic queries combined
- **Install:** `npx claude-mem install` — registers hooks, deploys worker service
- **Access:** via `mem-search` skill (natural language queries inside Claude Code sessions)
- **Web UI:** real-time memory stream viewer
- **No manual intervention** — fully automatic capture and injection

## Why clawfit should care
claude-mem is the strongest evidence yet that **Level 5 (memory/context layer) is becoming productized and plugin-native** rather than staying a research concept. The 45k star count is extraordinary — it means this problem is universally felt. clawfit's recommendation engine could eventually factor in memory layer compatibility (e.g., recommending `local-rag` + claude-mem for offline persistent workflows).

The hook-based integration pattern (rather than MCP server) is also worth noting as a distinct plugin architecture for the taxonomy.

## Preliminary interpretation
- Primary: **Level 5 — Memory / MCP / context layer**
- Architecture subtype: **hook-based plugin with local daemon** (distinct from pure MCP server approach)

## Status
- Very high priority. 45k stars is a strong adoption signal.
- Strong candidate for promotion into `docs/reference-levels.md` Level 5.
- Not a registry entry (not an agent/LLM/hardware) but important for scoring context around statefulness requirements.
