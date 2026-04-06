# Research Watch: rtk — CLI Token Proxy for LLM Agents

- Repo/Link: https://github.com/rtk-ai/rtk
- Source: GeekNews

## Why this is worth watching
rtk is a zero-dependency Rust binary that sits between an AI coding agent and the shell, rewriting command output before the agent reads it. The claimed 60–90% token reduction on common dev commands would meaningfully change the cost curve for session-heavy agent workflows — an economic lever clawfit's scoring model currently does not represent.

## What stands out immediately
- Operates as a transparent CLI proxy via shell hooks — no agent-side changes required
- Four compression strategies: smart filtering, grouping, truncation, deduplication
- Rust single binary, zero external runtime dependencies
- 60–90% token reduction claimed; documented benchmark shows ~80% cumulative savings in a 30-minute session (~118k tokens → ~24k)
- Targets `git status`, `ls`, test output, log tails — the highest-frequency agent shell calls
- Token savings are a cost proxy: lower token count = lower API spend per session

## Why clawfit should care
clawfit scores (agent, llm, hardware) triples on a cost axis, but currently treats prompt/output token volume as fixed. rtk introduces a new variable: a tool-layer intervention that changes the effective token rate without swapping the LLM. If rtk-style proxies become common, clawfit may need a "token efficiency modifier" in its scoring model. This is also a direct Level 4c tool-use signal — a lightweight infrastructure shim that amplifies any base runtime.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use / action infrastructure** (shell-level context compression shim)
- Adjacent to Level 2 (could be bundled as a harness default) but the repo is explicitly positioned as a standalone tool

## Status
- Low star count today; watching for adoption rate. Concept is structurally significant regardless of repo velocity.
