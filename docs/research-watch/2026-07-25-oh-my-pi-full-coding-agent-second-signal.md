# Research Watch: oh-my-pi (omp.sh) — Full Coding Agent Maturation: LSP/DAP/MCP-Native, 19.7k Stars

- Repo: https://github.com/can1357/oh-my-pi (⭐19,714)
- Source: GeekNews front page ("Pi를 IDE 수준으로 확장한 터미널 AI 코딩 에이전트", 15 pts, 2026-07-25); omp.sh marketing site

## Why this is worth watching

oh-my-pi was first tracked 2026-04-06 for the author's "Harness Problem" blog post and the Hashline content-hash edit primitive. That entry treated oh-my-pi as the vehicle for a design concept. This entry treats it as what it has become: a full-featured L2 terminal coding agent with 19.7k stars, ~400 releases since December 2025, and a native Rust engine (~55k lines) embedded in the TypeScript orchestration layer. The tool now implements LSP (language server protocol), DAP (debugger adapter protocol), native MCP integration, subagent orchestration, and 40+ LLM backends in the same binary — making it the most feature-complete terminal coding agent in the current scan corpus that has not received a dedicated L2 entry.

The evolution from "blog-post concept" to "19.7k-star production agent in 5 months" is itself a signal about the velocity of the L2 harness layer this cycle.

## What stands out immediately

- **Hash-anchored edits (from v1 Hashline concept, now production):** edits indexed by content hash, not line number — concurrent multi-agent edits do not produce stale-line failures; this is the only L2 harness in the corpus where edit atomicity is a protocol primitive, not an application-level workaround
- **32 built-in tools, 14 LSP operations, 28 DAP operations:** language server and debugger operations are first-class tool calls, not shell subprocess wrappers — go-to-definition, find-references, type resolution, and breakpoint management callable in the same agent loop as file reads
- **Native Rust engine (~55k lines) for performance-critical paths:** token counting, diff application, symbol lookup, and type resolution run at native speed without spawning separate processes
- **40+ LLM backends:** Claude, OpenAI, Gemini, Ollama, llama.cpp, and local endpoints — single agent harness covers cloud and air-gapped scenarios without configuration forking
- **Native MCP integration:** any MCP server's tools are callable inline, with the same token context as built-in tools; no separate MCP-to-agent bridge layer required
- **Subagent orchestration built in:** task decomposition without an external orchestrator — parent agent can spawn subagents and collect results in the same session
- **Plan mode + hindsight memory:** forward planning before execution, post-execution memory update after — both in the same agent loop, not external infrastructure
- **~400 releases since Dec 2025, today's push confirms active maintenance:** highest observed development cadence for any L2 harness in this scan series; v16.2 reached by June 2026

## Why clawfit should care

oh-my-pi now occupies the same L2 scoring tier as Claude Code, Goose, and Kimi CLI but with architecture differences that matter for filter outcomes:

1. **`latency: low` profiles:** the native Rust engine removes subprocess overhead from code-intelligence tool calls; no other tracked L2 harness has this. If the latency claim is verified vs. Claude Code on equivalent hardware, oh-my-pi may score higher on `latency: low` profiles than current registry rankings suggest.

2. **`network: offline` profiles:** 40+ backends include local inference endpoints (Ollama, llama.cpp); combined with a native binary that runs without cloud dependencies, oh-my-pi is a candidate for fully air-gapped deployments — a gap in the current registry for code-gen profiles with `network: offline`.

3. **`statefulness: session` profiles:** hindsight memory built into the agent loop means session context accumulates natively, without requiring an external memory infrastructure (unlike harnesses that depend on mem0 or similar). This is a scoring differentiator for `statefulness: session` profiles.

4. **Hash-anchored edit model vs. line-anchored:** no registry axis currently captures this distinction. For multi-agent parallel editing scenarios, the correctness guarantee differs — line-anchored harnesses can produce silent corruption, content-hash harnesses cannot. This may become a `statefulness: multi-agent` filter criterion.

## Preliminary interpretation

- **Level 2 — Harness / Coding Agent (primary):** coordinates agent loops, manages tool calls, orchestrates subagents for software development tasks
- **Level 4c secondary:** native LSP + DAP + MCP embedded as first-class tool primitives — the tool capability layer is integrated at the harness level, not grafted on via plugin
- Not L1 (does not define a model or base runtime); the multi-provider support is a harness feature, not a model contribution

Second signal for `can1357/oh-my-pi`: first signal was the Hashline/harness-problem concept (2026-04-06); this signal is the full L2 agent as a production artifact.

## Claims to verify

- **TTFT and throughput vs. Claude Code:** native Rust engine claims performance parity or better — no published benchmark vs. a direct competitor on the same SWE-bench task set
- **Hash-anchored edit behavior under adversarial concurrent edits:** what is the merge strategy when two subagents' edits produce conflicting content hashes? Is it abort-and-retry or last-write-wins?
- **40+ LLM backend maintenance depth:** how many backends are actively tested in CI vs. listed as "supported" with untested adapters?
- **Subagent token budget isolation:** how is the parent agent's context window protected from subagent output accumulation in long sessions?
- **LSP completeness:** are all 14 LSP operations natively implemented in the Rust engine, or do some fall back to spawning a language server process (e.g., clangd, pyright)?

## Status

- Second signal for oh-my-pi; first dedicated full-agent assessment (prior entry 2026-04-06 covered only the Hashline design concept)
- Registry candidate: **Strong candidate** — stars exceed 5,000 threshold; L2 harness category exists; but `latency` and `cost` data require benchmark before entry; `statefulness: session` applies; `hardware: cloud` and `local` both supported
- Schema gaps: `edit_model: [line-anchored | content-hash-anchored]`; `lsp_native: true/false`; `dap_native: true/false` — no fields for distinguishing harnesses with embedded vs. subprocess code intelligence
- Monitor for: published SWE-bench or equivalent benchmark vs. Claude Code/Goose; cost/latency registry data availability; whether `oh-my-pi` stabilizes the product name vs. `omp.sh` branding
