# Research Watch: "Agents don't need memory, they need documentation" — Architecture Signal

- Repo/Link: https://liao.gg/blog/agents-dont-need-memory
- Source: Hacker News front page (2026-10-04, 26 points)

## Why this is worth watching
This blog post argues that the standard framing of "agents need memory systems" is wrong — agents need well-structured, discoverable documentation about their own capabilities, context, and task history. This is a direct challenge to the entire Level 4a memory category in clawfit's taxonomy.

## What stands out immediately
- Argues persistent memory stores (vector DBs, KV stores) are the wrong primitive for agents
- Documentation-as-context: CLAUDE.md, AGENTS.md, structured task specs are better than episodic retrieval
- Connects to the ponytail/YAGNI pattern: structured constraint documents outperform unstructured memory
- Gaining traction at 26 HN points — appears to resonate with practitioners

## Why clawfit should care
The clawfit taxonomy has a distinct Level 4a layer for memory systems. If the "documentation over memory" pattern gains adoption, tools at L4a may split into two sub-types: episodic memory stores (vector DBs, KV, semantic search) versus structured documentation systems (AGENTS.md, CLAUDE.md loaders, context-injection skill layers). The current scoring treats all L4a tools as equivalent on the memory dimension; this signal suggests that `governance_need: hard` profiles may actually prefer documentation-first tools over retrieval-first memory stores.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal** (architecture opinion, not a new tool)
- Relevant to scoring: `governance_need: hard` + `data_sensitivity: confidential` profiles may weight structured documentation tools higher than retrieval-based memory

## Status
- Single-signal opinion piece; track for follow-on tooling that implements the documentation-first approach
- Prior related signals: ponytail (2026-06-24), superpowers (in registry), CLAUDE.md pattern
