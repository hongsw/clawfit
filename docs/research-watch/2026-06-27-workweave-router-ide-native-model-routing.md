# Research Watch: workweave/router — IDE-Native Smart Model Routing

- Repo: https://github.com/workweave/router
- Also see: docs/research-watch/2026-05-05-manifest-mnfst-smart-model-routing.md, docs/research-watch/2026-05-31-openrouter-series-b-llm-routing-infrastructure.md, docs/research-watch/2026-05-04-deepclaude-claude-deepseek-cost-bridge.md

## Why this is worth watching
workweave/router reached HN front page with 133 points on day of signal capture, at 259 stars — early-stage but with meaningful public traction. What distinguishes it from the routing cluster already tracked (Manifest, OpenRouter, DeepClaude) is the integration surface: this tool targets the developer's active coding environment directly, providing first-class install paths for Claude Code, Codex CLI, Cursor, and opencode rather than positioning as a standalone proxy. IDE-native routing is a new structural pattern not yet represented in the existing L4c sub-types.

## What stands out immediately
- Named integration targets are current agentic coding surfaces: Claude Code (`make install-cc`), Codex CLI (config patch), Cursor (base URL override), opencode — not generic OpenAI-SDK consumers
- Routes across Anthropic, OpenAI, Google (Gemini), and open-source models via OpenRouter (DeepSeek, Llama, Mistral, Qwen) from a single endpoint
- Routing algorithm described as "cluster scoring algorithm derived from academic research" — no methodology or paper citation surfaced in the signal brief; claim to inspect
- "<50ms routing decision" is the stated latency overhead — considerably higher than Manifest's 2ms claim, likely because the algorithm is inference-adjacent rather than keyword-only; claim to inspect
- "40-70% cost reduction" is unqualified: no methodology, no workload distribution, no quality benchmark published (same evidentiary gap as Manifest's 70% claim)
- BYOK architecture: provider credentials remain on-prem and encrypted; no request payload transits workweave infrastructure — relevant for `data_sensitivity: confidential` profiles
- Streaming, tool calls, and vision are claimed as supported — toolcall passthrough fidelity is material for coding agent use cases

## Why clawfit should care
The existing L4c routing sub-type (established via Manifest, 2026-05-05) assumed the routing layer sits between an agent runtime and its LLM backends, invisible to the IDE. workweave/router inserts at the IDE configuration layer instead — the proxy is configured as the agent's base URL or via a first-party install script. This is a meaningfully different integration locus: the agent surface itself (Claude Code, Cursor) is the adoption path, not a generic SDK shim.

For clawfit's scoring model, the same schema gap applies as noted for Manifest: `--budget` and LLM preference weight (0.15) assume a fixed agent-to-LLM binding. An IDE running workweave/router produces a blended cost profile that the current registry cannot express. The IDE-native angle adds a second gap: clawfit's `hardware` filter does not currently distinguish whether the inference call leaves the developer's coding surface or is intercepted in-environment.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool / capability / plugin layer (model-routing gateway sub-type, IDE-native variant)** — same primary layer as Manifest, but the integration surface (coding IDE as the injection point) is a distinct sub-pattern from standalone proxy deployment
- Level 2 read absent: no workflow orchestration, task decomposition, or agent lifecycle management is present or implied

## Status
- 259 stars at time of capture; below individual registry threshold (5k). Too early for registry consideration.
- Represents a new IDE-native variant of the L4c routing sub-type — not yet a second independent signal, but worth separating from Manifest's standalone-proxy classification if the pattern is confirmed by a second tool
- Key claims to inspect before any promotion: (1) "cluster scoring algorithm" source or methodology; (2) independent benchmark of <50ms overhead under realistic coding-agent traffic; (3) toolcall passthrough fidelity in Claude Code specifically
- Watch trigger: 2k+ stars or a confirmed integration test in a public Claude Code configuration
