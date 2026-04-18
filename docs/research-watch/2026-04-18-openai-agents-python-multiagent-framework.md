# Research Watch: openai/openai-agents-python

- Repo/Link: https://github.com/openai/openai-agents-python
- Source: GitHub Trending

## Why this is worth watching
OpenAI published an official "lightweight, powerful framework for multi-agent workflows" in Python under the openai GitHub org. At 21,803★ it is the most-starred official multi-agent framework from a major LLM provider. It sits in direct competition with LangGraph/deepagents (also 19k★) and CrewAI at the Level 2 harness layer while remaining provider-agnostic at the API level.

## What stands out immediately
- Official OpenAI repo — same provenance weight as Anthropic Managed Agents or Claude Code Routines
- "Lightweight" framing positions it against LangGraph's complexity — targets developers who found LangGraph too heavy
- Python-first (vs. LangGraph's Python + JS dual-track)
- 21,803★ while still trending — adoption signal is unusually fast for a framework
- Multi-agent workflow primitives: handoffs, routing, tool calling, async execution
- Complements OpenAI Codex plugin system (Level 4b) by providing the orchestration layer above it

## Why clawfit should care
This is a Level 2 harness that directly competes with deepagents, SuperClaude Framework, and oh-my-openagent. For orgs running on OpenAI Codex (not Claude Code), this is now the canonical harness recommendation from the vendor itself. clawfit's registry currently lacks an "official OpenAI multi-agent framework" entry — adding this closes that gap. It may also signal that "vendor-published harness" is becoming a pattern (Anthropic Managed Agents, Claude Code Routines, now openai-agents-python), deserving its own taxonomy sub-type in Level 2.

## Preliminary interpretation
Current best reading:
- **Level 2 — Multi-agent harness / orchestration framework (OpenAI-native)**

## Status
- High signal — add to registry and reference-levels.md
- Monitor whether it absorbs or replaces the oh-my-* family for OpenAI users
