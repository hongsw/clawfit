---
# Research Watch: langchain-ai/deepagents — batteries-included agent harness

- Repo: <https://github.com/langchain-ai/deepagents>

## Why this is worth watching
LangChain is entering the harness layer directly with a production-ready, open-source agent runtime that explicitly positions itself as an alternative to proprietary coding assistants (e.g. Claude Code). At 19.4k stars it is gaining real traction, and the "batteries-included" positioning is a deliberate contrast to LangChain's historically abstract, glue-code nature.

## What stands out immediately
- **Foundation:** compiled LangGraph graph — inherits streaming, persistence, checkpointing, Studio compatibility
- **Two surfaces:** Python SDK (`create_deep_agent`) and interactive CLI with TUI + web search
- **Built-in tool set:** `write_todos`, `read_file`, `write_file`, `edit_file`, `execute` (sandboxed), `task` (sub-agent delegation), `ls`, `glob`, `grep`
- **Provider-agnostic:** any LLM supporting tool calling
- **MCP integration:** via `langchain-mcp-adapters`
- **Explicitly inspired by Claude Code** — frames itself as the extensible open-source counterpart
- **Companion UI repo:** `langchain-ai/deep-agents-ui` (see separate watch)

## Why clawfit should care
deepagents validates the harness layer as the dominant competitive surface. LangChain's entry means the harness space now has major institutional players alongside community-driven projects. This directly affects clawfit's registry: deepagents is a candidate entry as both a Level 1 runtime (CLI mode) and Level 2 harness (SDK + LangGraph orchestration).

It also signals that **LangGraph is becoming a harness substrate** — the same role LangChain itself played for chains/agents. This is worth tracking as a platform pattern, not just a single tool.

## Preliminary interpretation
- Primary: **Level 2 — Meta wrappers / harnesses / orchestration layers** (SDK mode)
- Secondary: **Level 1 — Base runtimes** (CLI/TUI mode)
- Platform substrate: **LangGraph** (cross-cutting — affects Level 2 and Level 3)

## Status
- High priority. LangChain institutional entry into the harness layer.
- Candidate for promotion into `docs/reference-levels.md` Level 1/2.
- Registry entry candidate: needs latency/cost benchmarks before adding to `agents.json`.
