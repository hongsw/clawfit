# Research Watch: Fosowl/agenticSeek — Fully Local Autonomous Agent Without API

- Repo: https://github.com/Fosowl/agenticSeek (⭐27,305)
- Source: GitHub Trending Python (daily, today)

## Why this is worth watching
agenticSeek is a self-hosted, fully local autonomous agent: it runs on-device without calling any external API. It uses local LLMs (Ollama, LM Studio), local web browsing, local code execution, and local file access. The positioning is explicitly anti-cloud: no API key, no telemetry, no external data transit. With 27k+ stars, it is one of the highest-starred local-only autonomous agent frameworks in the scan corpus. The combination of local inference + autonomous task execution represents a different deployment philosophy from API-dependent agents like Codex, Goose, or Claude Code.

## What stands out immediately
- **No external API required**: inference, web search, and code execution all run locally via Ollama/LM Studio or compatible local runtimes
- **Autonomous task execution**: not a chat assistant — executes multi-step tasks with tool use (web browse, write code, run files)
- **27,305 stars**: among the highest-starred fully-local autonomous agent frameworks in this scan series
- **Trending today on GitHub Python**: current active community interest, not just historical adoption
- **Positioned for privacy-critical and air-gapped use cases**: healthcare, legal, enterprise compliance contexts where cloud API calls are prohibited
- **Compatible with existing local inference stacks**: Ollama and LM Studio are already tracked in clawfit's hardware/inference tier

## Why clawfit should care
clawfit's `network` filter supports `offline` but the existing corpus of autonomous agents in `agents.json` is predominantly API-dependent (Claude Code, Goose, Aider). agenticSeek is evidence that a fully local autonomous agent tier with 27k+ stars now exists. If agenticSeek or a successor reaches registry-entry quality, clawfit's scoring model would need to weight `network: offline` + `hardware: local` configurations more richly — currently the scoring model has limited representation at that intersection. The `statefulness` and `autonomy_level` axes would also apply differently to a locally-run autonomous agent vs. a managed API agent.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Runtime** (primary: autonomous agent execution environment, multi-step task loop)
- **Level 2 — Harness/Wrapper** (secondary: wraps local inference via Ollama/LM Studio)

## Claims to verify
- Whether the "autonomous" framing reflects full plan-and-execute loop or a more limited command-following mode
- What web browsing implementation is used (browser-use, Playwright, custom)
- License type (check GitHub)
- Whether it supports tool-calling LLMs only, or also completion-based models
- Date of initial release vs. current star velocity (has it grown over a year, or recently spiked?)

## Status
- First research-watch doc; 27,305★ above 5k registry threshold; on GitHub Trending today
- Registry candidate: agents.json entry feasible if `network: offline`, `hardware: local`, and `statefulness: session` map cleanly; deferred pending license verification and latency data for common local model configurations
- Pattern: highest-starred confirmed fully-local autonomous agent in scan corpus; watching for second signal of comparable scale confirming "local-first autonomous agent" as a mature sub-type at L1
