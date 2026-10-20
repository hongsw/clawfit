# Research Watch: RuneBench — RuneScape as Agent Evaluation Environment

- Repo/Link: https://maxbittker.github.io/runebench/
- Source: Hacker News (140 points, 54 comments)

## Why this is worth watching
RuneBench uses an emulated RuneScape game server with a TypeScript SDK to benchmark AI agents on 16–32 skill-training tasks. Unlike code-execution benchmarks, it requires agents to read game world state, query a knowledge base, and take sequential in-game actions across a long horizon — a real-time feedback loop that code-centric benchmarks miss entirely.

## What stands out immediately
- Scores via `ln(1 + XP/min)` averaged across skill tasks — a continuous metric rather than pass/fail
- May 2026 snapshot: GPT-5.5 xhigh leads at 5.7%, Gemini 3.5 Flash 5.4%, GPT-5.5 5.3% — all agents score very low (sub-6%), indicating this is genuinely hard
- Agents must handle game knowledge retrieval, action planning, and real-time state changes simultaneously
- Harbor Framework has indexed the dataset (`maxbittker/runebench`), signaling use within research harness infra
- No GitHub repo published yet; primary exposure is via YouTube video and BenchLM/Harbor catalog

## Why clawfit should care
Current clawfit scoring has no dimension for **long-horizon sequential task evaluation** or **game-environment benchmarks**. RuneBench reveals a capability gap: coding agents and research agents have very different long-horizon performance profiles, yet clawfit today treats `task: code-gen` and `task: research` as the primary axes for scoring. An emerging cluster of game-env benchmarks (GAIA, OSWorld, RuneBench) is converging on games as evaluation substrate — worth watching for a new `evaluation_complexity` dimension.

## Preliminary interpretation
Current best reading:
- **Level 5 — Evaluation & Benchmarking**

Secondary: L4 (capability surface — game state as tool-use interface)

## Status
- First signal for "MMO/game environment as agent evaluation substrate"
- Two-signal candidate: pairs with GAIA/OSWorld for "non-code sequential task benchmark" cluster
- No registry entry warranted yet (no deterministic cost/latency)
