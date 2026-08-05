# Research Watch: SkyRL — Modular Full-Stack RL Library for Long-Horizon LLM Agents

- Repo: https://github.com/NovaSky-AI/SkyRL (⭐2,125)
- Source: GitHub Trending Python (2026-08-05)

## Why this is worth watching

SkyRL is a modular reinforcement learning library for language models that explicitly targets "long-horizon, real-world agents" — meaning multi-turn, tool-using agents that complete tasks requiring sequential reasoning over extended trajectories, not single-step completion tasks. This distinction matters: most RL-for-LLM work in the corpus addresses RLHF/preference tuning for instruction following, not RL for training agents that use tools across many steps to complete real tasks.

The project shipped SkyRL-Agent (November 2025), integrated the Tinker API (February 2026), and added Harbor integration (February 2026), indicating sustained development not a one-time release.

The "full-stack" label is technically accurate: the library covers training (skyrl-train), agent infrastructure (skyrl-agent), environment library (skyrl-gym), and cross-platform Tinker API implementation (skyrl-tx). This vertical scope is unusual — most RL libraries target one layer (training or environments), not all four simultaneously.

## What stands out immediately

- **Tinker API as training backend:** SkyRL implements the Tinker API, a specification for running training scripts on local GPU infrastructure. The Tinker API implies a client/server split where training orchestration is decoupled from execution hardware — agents submit training jobs to a Tinker API endpoint, which can be local (via skyrl-tx) or hosted. This enables training on local GPU clusters without cloud infrastructure lock-in.
- **Asynchronous training with in-flight weight updates:** skyrl-train supports async training where weight updates propagate to running agents without stopping the training loop — an important optimization for long-horizon tasks where environment rollout time dominates training time.
- **skyrl-gym: tool-use environment library:** Includes gymnasium-compatible environments for text-to-SQL, SWE-Bench (software engineering agent), coding tasks, mathematical reasoning, and web search. These are real agent tasks with non-trivial tool call sequences, not toy benchmarks.
- **Apache-2.0 license:** commercially permissive, supporting enterprise adoption without license negotiation
- **2,125 stars with active 2026 releases:** star count and release cadence suggest genuine community adoption, not a one-off research release

## Why clawfit should care

SkyRL sits at L1 (training infrastructure for base agent models) — a layer where clawfit currently has almost no tracked entries. The registry covers inference-focused L1 tools (AirLLM, KTransformers, Swiftlet) and coding agents (Claude Code, Codex), but the gap between inference and trained behavior — how you get an agent that can do multi-step tool use reliably — is unaddressed.

This matters for clawfit recommendations indirectly: a user asking for a `task: code-gen` agent with `latency: low` gets a recommendation, but clawfit does not model whether the recommended agent was trained with RL for tool use or is a zero-shot prompted base model. The difference in task completion quality for long-horizon tasks can be significant.

**Tinker API implications:** if the Tinker API emerges as a standard for training-job submission (similar to how MCP standardized tool-call dispatch), it would become a new axis in the L1 landscape. SkyRL is among the first to implement it locally. Watch for other training libraries adopting the same API.

**skyrl-gym task environments:** the included benchmark tasks (SWE-Bench, text-to-SQL, web search) directly overlap with clawfit's `task` taxonomy (`code-gen`, `data-analysis`, `research`). Training performance on these benchmarks could become a scoring input if deterministic public metrics become available.

## Preliminary interpretation

- **Level 1 — Training infrastructure / base agent tuning layer** (primary): RL training framework that produces tool-using agents from base models
- **Level 5 secondary:** skyrl-gym's evaluation environments and benchmark tasks overlap with the evaluation layer (L5)
- The Tinker API backend (skyrl-tx) could emerge as an L7 infrastructure primitive if it standardizes training-job dispatch across platforms

## Claims to verify

- **Tinker API origin:** the API specification is not well-documented in the repository; verify who defines the spec and whether SkyRL is implementing a third-party standard or creating their own
- **Async weight update mechanism:** in-flight weight updates during rollout is architecturally complex; verify whether this requires specific hardware configuration (e.g., NVLink) or works on commodity GPU clusters
- **Benchmark performance:** the project references SWE-Bench and other standard benchmarks but published results are not confirmed in the README; verify whether SkyRL-trained agents post competitive scores
- **"Long-horizon" definition:** the project uses this term without quantifying trajectory length; verify what episode length and tool-call count their training infrastructure targets
- **Harbor integration:** "Harbor" is listed as a 2026 integration but the library for this is unclear; verify whether Harbor refers to the container registry (irrelevant) or an agent harness (relevant)

## Status

- First signal for "modular full-stack RL library targeting long-horizon tool-using LLM agents"
- 2,125 stars, Apache-2.0, NovaSky-AI origin (NovaSky is a research lab with prior published work)
- No registry entry: RL training frameworks are not in current schema (`task`, `latency`, `budget` axes assume inference, not training)
- Schema watch: `training_method: [supervised | rl | rl-tool-use]`; `supports_tinker_api: bool`; `benchmark_envs: [swe-bench | text-to-sql | web-search]`
- Cross-reference: OpenClaw-RL (2026-07-05) is the closest prior signal — RL training from conversational feedback; SkyRL is distinct in targeting multi-turn tool use specifically via gym environments rather than conversation history
