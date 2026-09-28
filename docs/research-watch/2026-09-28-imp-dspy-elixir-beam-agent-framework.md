# Research Watch: Imp — DSPy Port to BEAM/Elixir

- Repo/Link: https://github.com/deepfates/imp
- Source: Hacker News (38 points, 2026-09-28)

## Why this is worth watching
Imp is a full-fidelity port of the DSPy optimization framework to Elixir and the BEAM runtime, the first time DSPy's declarative LM program model has landed in a production-grade concurrent runtime outside Python. As agentic workloads shift toward high-concurrency and fault-tolerance requirements, BEAM's supervised OTP processes offer a compelling alternative to Python asyncio for long-running agents.

## What stands out immediately
- **Agent-as-OTP-process**: each agent runs as a supervised GenServer with message passing, state, and deadline management — crash recovery is native
- **Full optimizer suite**: GEPA, BootstrapFewShot, MIPROv2, SIMBA all ported — prompt and instruction optimization works the same as in Python DSPy
- **MCP server support**: tools can be imported from any MCP server, putting it on the same integration surface as Claude Code and other harnesses
- **ACP protocol**: IDE client support via Zed's ACP, enabling direct embedding in editor workflows
- **v0.5 on Hex**: first public release, API still stabilizing; 94 stars

## Why clawfit should care
DSPy's spread to BEAM signals that self-optimizing agent harnesses are becoming cross-ecosystem standards, not Python-only libraries. If BEAM-based agents gain adoption in back-end and telco workloads (historically Elixir territory), clawfit may need a harness-layer entry for Elixir agents. The MCP support also means Imp connects to the same tool ecosystem clawfit already tracks.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper Layer** (self-optimizing OTP-based agent harness with MCP integration)

## Status
- Tracking — early adoption signal; watch for v1.0 and benchmark results on optimizers
