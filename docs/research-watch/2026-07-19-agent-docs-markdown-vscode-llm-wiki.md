# Research Watch: Agent Docs for Markdown — VS Code Extension for Agent-Readable Knowledge Bases

- Repo/Link: https://marketplace.visualstudio.com/items?itemName=agent-docs-markdown (via GeekNews Show GN, 2026-07-19)
- Source: GeekNews (Show GN, 2026-07-19)

## Why this is worth watching
This VS Code extension converts local markdown files into an AI agent-accessible "LLM Wiki" — a structured knowledge format explicitly designed for agent consumption rather than human browsing. It operates inside the editor workflow rather than as a standalone MCP server or RAG backend, making it the first tracked tool that treats the developer's own markdown documentation as a first-class agent knowledge input.

## What stands out immediately
- Editor-native: lives inside VS Code, not a separate server process or cloud API
- Output format is "LLM Wiki" — a format targeting agent consumption patterns (structured context, not rendered HTML)
- Targets local markdown files: runbooks, ADRs, README files, personal notes
- Show GN format suggests creator-submitted; star count unknown (VS Code marketplace, not GitHub)
- Different framing from existing tracked memory tools: not about persisting agent memories, but about making existing human docs agent-readable

## Why clawfit should care
Current L4a/L4b tools split between persistent memory layers (mem0, GBrain, codebase-memory-mcp) and skill packs (mattpocock/skills, addyosmani/agent-skills). This extension is a third category: static documentation-to-agent-context conversion. For `offline_mid_codegen` profiles where documentation is kept locally (architecture decisions, internal APIs), this fills a gap between "raw file search" and "full vector store RAG." Relation to Context7 (MCP server for library docs): Context7 serves external library docs; this serves internal team markdown. The combination represents a more complete agent knowledge architecture.

## Preliminary interpretation
Current best reading:
- **Level 4a — Agent context management** (markdown-to-LLM-Wiki pipeline, editor-native)
- Possible secondary: **Level 4b** if it generates skill-like prompt artifacts rather than retrieval indexes

## Status
- First signal; GeekNews Show GN (creator-submitted, unverified adoption).
- No registry entry: VS Code extension, no schema match; star count/popularity unknown.
- Schema watch: `knowledge_source: [generated | documentation | conversation | code]`; `editor_integrated: true/false`; `knowledge_format: [vector | graph | llm-wiki | raw-text]`.
- Blocked on: public GitHub repo link (not surfaced in GN post); independent user reports of quality.
