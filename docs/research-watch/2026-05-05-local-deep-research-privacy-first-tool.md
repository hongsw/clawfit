# Research Watch: local-deep-research — Privacy-First Autonomous Research Agent

- Repo/Link: https://github.com/LearningCircuit/local-deep-research
- Source: GitHub Trending Python #13, ~171 stars today

## Why this is worth watching
local-deep-research combines a LangGraph-driven autonomous research loop with local LLM support (Ollama, LM Studio, llama.cpp) and 10+ search engine integrations, positioning itself at the intersection of research-loop tooling and privacy-preserving offline execution. At 4.8k stars with active trending velocity, it has not yet crossed the 5k registry threshold but is approaching it. The project's simultaneous MCP server surface, REST API, and SQLCipher-encrypted local knowledge base spans at least three distinct ecosystem layers — a multi-layer collapse pattern worth tracking.

## What stands out immediately
- **LangGraph agent strategy**: an autonomous mode where the LLM chooses which search engines and research strategies to apply — not a scripted pipeline; the research loop is LLM-driven
- **Local-first LLM support**: Ollama, LM Studio, llama.cpp listed alongside cloud providers (OpenAI, Claude, Gemini); offline-capable profiles are a first-class deployment target
- **MCP server included**: exposes the research capability to Claude and compatible surfaces — makes this a dual-role tool (standalone agent + MCP tool-use extension)
- **SQLCipher per-user encrypted storage**: AES-256, zero telemetry, Docker images with signed SLSA provenance — security posture is stronger than typical research tools at this star count
- **95% SimpleQA accuracy claim**: cited as preliminary testing with GPT-4.1-mini + SearXNG; claim-to-inspect, no independent benchmark published
- **10+ search engine integrations**: arXiv, PubMed, Wikipedia, SearXNG, GitHub, Wayback Machine — domain-targeted search rather than generic web-only
- **Knowledge base with encrypted local storage**: users build persistent searchable libraries from downloaded research sources — bridges agent memory and retrieval tooling

## Why clawfit should care
The MCP server surface means local-deep-research can be consumed as a Level 4c tool-use extension by any MCP-compatible agent, not just as a standalone Level 1 tool. This dual-role pattern (self-contained agent + MCP-exposed capability) is increasingly common and creates classification ambiguity. For clawfit's recommendation engine, the `task: research` profile with `network: offline` or `data_sensitivity: confidential` constraints currently lacks a strong local-first option with deep search-engine coverage — local-deep-research is a candidate to fill that gap if it crosses 5k stars and the offline LLM path is independently confirmed at production quality. The encrypted knowledge base also overlaps the L5 memory layer; whether it functions as persistent agent memory (write-authority LLM → L6b) or as a human-curated retrieval store (write-authority pipeline/human → L6a) is not clear from the README alone and requires inspection.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (primary): autonomous LangGraph research loop with self-directed search strategy selection; functions as a standalone agent, not merely a tool wrapper
- **Level 4c — Tool-use / capability layer** (secondary): MCP server surface exposes research capability to Claude and other MCP-compatible agents
- **Level 5 / L6a** (weak tertiary): encrypted knowledge base with searchable local storage touches the memory/retrieval layer but write-authority remains with the user/pipeline, not the LLM — closer to L6a retrieval-native than L6b LLM-native KB

The suggested Level 7 (infrastructure/local execution) classification is not the primary read; local-first execution is a deployment property here, not the architectural role. Level 5 alone is insufficient — the research loop and MCP surface are more structurally significant than the storage layer.

## Status
- 4.8k stars, below the 5k registry threshold — tracking only
- Revisit at 5k stars or when offline LLM path (Ollama + local search) is independently confirmed at production quality
- Watch for clarification on whether the knowledge base write-authority is LLM-driven (L6b) or user/pipeline-driven (L6a)
- MCP server sub-type warrants cross-reference to L4c if a second high-signal research-loop MCP server appears
