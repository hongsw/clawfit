---
# Research Watch: Mozilla AI cq — shared knowledge commons for AI agents

- Repo/Post: <https://blog.mozilla.ai/cq-stack-overflow-for-agents/>

## Why this is worth watching
Mozilla AI is building a **multi-agent knowledge sharing system** — agents query a shared commons before tackling unfamiliar tasks and contribute learnings back after completion. This is qualitatively different from single-agent memory (like claude-mem). It addresses collective intelligence at the agent population level, not the individual session level. The "Stack Overflow for agents" framing is memorable and likely to spread.

## What stands out immediately
- **Shared knowledge base:** agents query before acting on unfamiliar tasks
- **Multi-agent verification:** trust built through consensus, not single-agent assertion
- **Collective learning loop:** agents contribute learnings back to the commons
- **Mozilla AI provenance:** institutional credibility, likely open-source commitment
- Framed as preventing agents from "repeating identical mistakes" — speaks directly to a known pain point in multi-agent systems

## Why clawfit should care
cq represents a new Level 5 subtype: **collective/distributed memory** as opposed to session-local or project-local memory. This has implications for clawfit's statefulness axis — currently `stateless | session | persistent`. A fourth mode — `collective` or `shared` — may be needed to accurately describe agent patterns that participate in knowledge commons.

Also: Mozilla entering the agent tooling space is an ecosystem signal about institutional investment in open agent infrastructure.

## Preliminary interpretation
- Primary: **Level 5 — Memory / MCP / context layer**
- Subtype: **collective memory / multi-agent knowledge commons** (distinct from session/project-local memory)

## Status
- High interest. Novel architecture pattern not currently represented in clawfit's taxonomy.
- May require extending statefulness schema (`collective` mode) — flag for scoring-analyst.
