# Research Watch: Shepherd — Reversible Agent Execution Substrate

- Repo: https://github.com/shepherd-agents/shepherd (⭐1,513)
- Source: GitHub Search API — new Python repos (created 2026-06-24, 27 days old), topics: [mcts-rl, meta-agents, meta-optimization, runtime-supervision, tree-rl], v0.3.0 released 2026-07-08

## Why this is worth watching

Shepherd solves a problem that most agent frameworks handle informally: how does a meta-agent (supervisor, optimizer, or RL trainer) observe, fork, replay, or revert a sub-agent's execution without rebuilding the entire computation? The answer is a "Git-like trace" — a persistent, branching record of every agent action and file write, with copy-on-write semantics, KV-cache reuse on replay, and OS-level permission enforcement. At 1,513 stars after 27 days, Shepherd is lower-star than the other signals in today's scan. It is included because the topics (`mcts-rl`, `meta-optimization`, `tree-rl`) signal a specific technical niche — RL-driven agent supervision — that no other tool in the current scan corpus addresses at the execution-substrate level.

## What stands out immediately

- **Reversible execution model**: agent work lands as a "proposal" held separately from the working tree; a human or meta-agent must explicitly accept/apply before file changes take effect. Nothing is destructive until approved. This is the `git add` + `git commit` model applied to agent execution rather than source control
- **Copy-on-write forking at ~5× Docker-commit speed**: branching a running agent session is cheap — enables tree-search (MCTS-style) over agent execution paths without the overhead of full environment snapshots
- **95% KV-cache reuse on replay**: replaying a trace from any branch point reuses cached KV states, making iterative refinement of agent outputs economically viable. Cache reuse at this rate is a prerequisite for practical RL training loops over agent behavior
- **OS-level permission grants in task signatures**: `repo: sp.GitRepo` (read-write) vs. `May[GitRepo, ReadOnly]` (read-only) enforced at native syscalls (macOS Seatbelt; Linux Landlock). Permissions declared in Python function signatures, not in a separate config file — permission documentation is co-located with the code it governs
- **MCTS-RL supervision label**: the README mentions "meta-agents can observe and steer" execution, supporting "tree-search and reinforcement learning patterns." The mechanism is the reversible trace + forking substrate — MCTS exploration over agent execution paths becomes a data structure operation, not a full environment rerun
- **Deterministic provider for offline use**: Shepherd includes a deterministic provider for testing without an LLM API, enabling local development of meta-agent logic without cloud cost
- **MIT license, Python 3.11+ only**: lower star count and Python-only target suggest a research-adjacent tool rather than a production deployment framework at this stage

## Why clawfit should care

Shepherd addresses the L5 gap in clawfit's taxonomy: observability and meta-optimization of agent execution. Current L5 entries are largely focused on memory (mem0, GBrain) and evaluation (benchmarks, score tracking). Shepherd is the first tool in the scan corpus that makes agent execution *intrinsically reversible* at the infrastructure level — not as an evaluation afterthought, but as a design constraint that every task runs inside.

The RL training angle is strategically significant. If agent fine-tuning (MCTS-RL, DPO, PPO over execution traces) becomes standard practice for production agent deployments — a direction signaled by open-swe's integration with learning loops and UniRL (Tencent, tracked separately) — then the substrate that makes execution traces cheap to fork and replay will be table stakes, not experimental. Shepherd is the earliest-stage infrastructure bet on that trajectory.

Schema implication for clawfit: `execution_reversible: true/false`; `replay_capable: true/false`; `meta_agent_ready: true/false` — these are L5 capability flags absent from both `agents.json` and the current `evidence-schema.md`.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory/Observability** (primary: persistent, reversible execution traces as a substrate for meta-agent supervision and RL training)
- **Level 2 — Harness/Wrapper** (secondary: tasks are declared as Python signatures; Shepherd wraps agent invocations with proposal staging and permission enforcement)

Not L1: Shepherd does not run the underlying LLM inference. Not L4: it does not expose tools or capabilities to agents; it records and structures what agents do with existing tools.

Closest comparables: No direct comparable in current scan corpus. The closest architectural peer is Git (versioned working tree with staging area) applied to agent execution rather than source code. Among agent frameworks: open-swe has audit-trail-as-PR-draft, but that is an output pattern, not a substrate-level reversible execution model. Shepherd is an architectural primitive at a lower level than any current L2 entry.

## Claims to verify

- **95% KV-cache reuse on replay**: this is a strong performance claim that depends heavily on the conversation structure. KV-cache reuse drops significantly with branching prompts that diverge from the cached context. Independent benchmark needed.
- **"~5× Docker-commit speed" for copy-on-write forking**: copy-on-write filesystem semantics (btrfs/APFS) can support this, but the comparison baseline (Docker commit for a typical agent workspace) needs specification. Performance claim is plausible but needs context.
- **MCTS-RL meta-agent**: the README labels this capability but the v0.3.0 implementation may not yet include a working MCTS supervisor — this may be a roadmap feature documented at the architecture level. Needs code inspection.
- **macOS Seatbelt + Linux Landlock enforcement**: OS-level syscall enforcement is a strong claim. macOS Seatbelt (sandbox-exec) and Linux Landlock have well-known limitations; the enforcement surface needs independent verification for the specific syscall patterns Shepherd's tasks generate.

## Status

- No registry entry: 27 days old (v0.3.0, pre-1.0); 1,513 stars is the lowest-star signal accepted this cycle (accepted for architectural distinctiveness, not star count); no deterministic cost/latency data.
- Schema gap: `execution_reversible: true/false`; `replay_capable: true/false`; `permission_model: [none | application | os-syscall]`; `meta_agent_ready: true/false`.
- First signal for "reversible agent execution substrate" as an L5 architectural pattern. Single signal — two-signal rule applies before canonical section consideration.
- Cross-watch: UniRL (Tencent/Hunyuan, 836 stars, tracked separately as RL training framework for multimodal agents) + Shepherd together may constitute a second signal for "RL over agent execution traces" as an L5 sub-type. UniRL focuses on the training algorithm; Shepherd provides the execution substrate. These are complementary layers of the same emerging pattern.
- Registry candidate when: (a) v1.0 released with stable task API, (b) MCTS-RL supervisor implementation confirmed, (c) independent KV-cache reuse benchmark available.
