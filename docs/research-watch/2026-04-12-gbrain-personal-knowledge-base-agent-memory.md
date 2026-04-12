# Research Watch: GBrain — Personal Knowledge Base for Agent Memory

- Repo/Link: https://github.com/garrytan/gbrain
- Source: GeekNews (42 points)

## Why this is worth watching
GBrain is an MIT-licensed personal knowledge base built by YC CEO Garry Tan, explicitly designed as memory infrastructure for OpenClaw and Hermes Agent. It converts meetings, emails, notes, and conversations into a searchable markdown+Postgres knowledge graph that agents read before every response and write back to after each exchange. The YC CEO provenance gives it outsized signal value as an adoption indicator.

## What stands out immediately
- Markdown files in a git repo as source of truth — humans can inspect and diff; agents compile structured knowledge
- Postgres/PGLite backend; local-first "~2 second cold start"
- Install via `bun add -g github:garrytan/gbrain` + `gbrain init` — library and CLI both available
- Full MCP support coming (Supabase Auth) — bridges local-first with cloud MCP ecosystem
- Explicitly inspired by Karpathy's LLM-Wiki concept but built for agent integration, not personal indexing
- "Mini-AGI with electric hands" framing — persistence as the multiplier on agent capability

## Why clawfit should care
The Level 4a memory layer currently has claude-mem (45k★), OpenMemory, cipher, and claude-context. GBrain adds a new sub-pattern: memory as a compounding personal knowledge asset owned by the user (not the tool). The markdown+git storage model is developer-friendly and `data_sensitivity: confidential` compatible. The OpenClaw/Hermes integration means it scores highly for users already in that ecosystem. Also validates that the `research` task type is increasingly memory-dependent.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory / persistent context** (personal knowledge compounding sub-type)

## Status
- New entry, 42 GeekNews points. MIT-licensed. Add to registry as Level 4a memory tool. Monitor MCP integration release.
