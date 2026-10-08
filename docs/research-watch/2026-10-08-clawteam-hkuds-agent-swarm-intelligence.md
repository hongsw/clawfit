# Research Watch: ClawTeam — Leader-Worker Agent Swarm with Git Worktree Isolation

- Repo: https://github.com/HKUDS/ClawTeam (⭐5.2k)
- Source: GitHub Trending October 2026; Korean GeekNews discussion

## Why this is worth watching
ClawTeam adds a layer of **structured swarm coordination** on top of existing coding agent runtimes without replacing them. Rather than building a new agent runtime, it assumes you already have Claude Code, Codex, nanobot, or any other subprocess-spawnable agent, and provides a leader-worker orchestration framework where each worker runs in an isolated git worktree and tmux window. The isolation model is architecturally significant: each agent writes to its own branch and environment, avoiding the concurrent-write collisions that plague simpler multi-agent approaches. The agent-swarm framing also aligns with what the HKUDS lab (Hong Kong University Data Intelligence Lab) has been building in the OpenHarness and nanobot ecosystems, suggesting a deliberate multi-layer strategy from a single research group.

## What stands out immediately
- **Leader-worker architecture**: a leader agent creates, monitors, and dissolves worker agents; workers receive tasks via point-to-point or broadcast file-based or ZeroMQ P2P messaging — no shared database
- **Git worktree isolation per worker**: each worker operates in its own git worktree and tmux window, preventing concurrent write conflicts and preserving the ability to diff, merge, or discard each worker's output independently
- **Subprocess-agnostic**: worker agent runtime is pluggable — Claude Code, Codex, nanobot, Cursor, or any custom CLI via `subprocess.run()`; no SDK coupling
- **Task dependency graph**: the orchestrator manages dependencies between sub-tasks; progress visible via terminal dashboard or web UI
- **ZeroMQ P2P transport** (optional): allows inter-agent messaging without writing to the filesystem; relevant for latency-sensitive coordination
- **MIT license**, Python 3.10+ required; tmux is a runtime dependency
- **Actively maintained**: v0.2.0 released March 23, 2026; community fork (ClawTeam-OpenClaw) at 1.4k stars adds OpenClaw-default configuration
- **Empirical demo**: team of 8 agents on 8 H100 GPUs ran 2,000+ ML experiments, reducing val_bpb from 1.044 to 0.977 — vendor-reported, not independently verified

## Why clawfit should care
ClawTeam represents a distinct orchestration pattern not currently in the registry: **file-system-first multi-agent coordination with process-level isolation**. Unlike cloud-native multi-agent frameworks (e.g., CrewAI, AutoGen) that use shared in-memory state or an API orchestrator, ClawTeam grounds coordination in the git object model and the filesystem — both universally available and intrinsically auditable. The git-worktree approach also means each agent run is a proper branch that can be reviewed before merge, which introduces an `audit_trail` property absent from most harness entries. The zero-database-dependency design (state in `~/.clawteam/` flat files) is directly relevant to clawfit's `network` filter: ClawTeam can run fully offline once agents are installed.

## Preliminary interpretation
- **L3 — Team / SSOT Generator** (primary): coordinates a team of agents under a single leader with shared task graph and messaging
- **L1 — Base Agent Runtime** (secondary): `subprocess`-level agent spawning and lifecycle management are base runtime operations

## Claims to verify
- "2,000+ ML experiments" benchmark: vendor-reported demo result from their README; confirms the framework can coordinate multiple agent workers, but does not independently validate efficiency or correctness gains over a single-agent run
- ZeroMQ transport stability: the P2P messaging layer is listed as an optional upgrade path; production reliability under high-throughput multi-agent workloads is not documented
- Cross-platform tmux support: required runtime dependency; behavior on macOS vs. Linux vs. Windows (via WSL) is not specified in the README
- OpenClaw vs. Claude Code default: the community fork (ClawTeam-OpenClaw) uses a different default agent; compatibility with upstream orchestration logic is inferred, not stated

## Status
- 5.2k stars; launched March 2026; active maintenance with community fork activity
- MIT license; Python 3.10+ + tmux required
- **First dedicated signal for "git-worktree-isolated leader-worker swarm coordination framework"** in clawfit's research-watch corpus
- Registry candidacy: not warranted under current schema (orchestration layer, not LLM or hardware)
- Monitor: v1.0 roadmap items (Redis Transport, Shared State, Agent Marketplace), star growth relative to nanobot and OpenHarness from the same lab
