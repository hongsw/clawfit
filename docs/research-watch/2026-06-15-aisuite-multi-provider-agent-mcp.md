# Research Watch: andrewyng/aisuite — Multi-Provider Agent Runtime with MCP

- Repo: https://github.com/andrewyng/aisuite
- Source: GitHub Trending (today, 291 new stars, 14,381 total)

## Why this is worth watching

aisuite from Andrew Ng presents a unified OpenAI-style Chat Completions API across 10+ providers (Anthropic, OpenAI, Google, Mistral, HuggingFace, AWS, Cohere, Ollama, OpenRouter). What elevates it above a simple LLM abstraction: a first-class **Agents API with Toolkits** (files, git, shell), native **MCP server integration**, and **OpenCoworker** — a desktop agent for macOS/Windows built on aisuite that runs all data locally. This is a base runtime + provider router collapsed into a single lightweight package.

## What stands out immediately

- `<provider>:<model-name>` routing (e.g., `anthropic:claude-sonnet-4-6`) lets teams switch backends with one string change
- `max_turns` parameter drives automatic multi-turn agentic loops; manual mode also available
- MCP attachment requires zero boilerplate: `client.attach_mcp_server(server)` — cleanest MCP surface observed in an L1 runtime to date
- Ollama support means `network: offline` is fully supported without any code change
- OpenCoworker desktop agent keeps all data local — relevant for `data_sensitivity: confidential` profiles
- Provider adapter pattern: automatic discovery via naming convention (`<provider>_provider.py`) makes adding new providers trivial
- 14.4k★ is above the 5k registry promotion threshold but this is the first scan signal — single-signal rule applies

## Why clawfit should care

aisuite collapses the L1 runtime / provider selection decision. A team using aisuite can switch from `anthropic:claude-sonnet-4-6` (online, paid) to `ollama:llama3` (offline, free) without changing agent code. This is directly relevant to clawfit's `network` and `monthly_budget` scoring axes — aisuite is a network-agnostic, budget-flexible runtime. If the OpenCoworker trajectory mirrors Claude Cowork's adoption, this could become a significant L1 competitor.

## Preliminary interpretation

- **Level 1 — Base agent runtime** (primary): provides the execution loop (Agents API + Toolkits + MCP)
- **L1/L0 cross-cutting** (secondary): unified provider router that abstracts the inference substrate
- Distinct from LiteLLM: LiteLLM is a proxy server; aisuite is a Python library with agentic loop semantics
- Distinct from LangChain: no graph/DAG overhead; intentionally minimal — stdlib-adjacent

## Status

- First signal 2026-06-15 at 14,381★ — above 5k threshold but single-signal rule applies; hold for second independent source
- Promotion criterion: confirmed functional adoption in a second project citing aisuite OR MCP Marketplace listing
- Registry candidate: `tasks: [code-gen, research]`, `roles: [developer]`, `network: hybrid`, `setup_complexity: low`
