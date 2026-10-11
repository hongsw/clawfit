# Research Watch: Repowise — MCP-Native Codebase Intelligence Layer

- Repo: https://github.com/repowise-dev/repowise (⭐7,514)
- Source: GitHub Trending Python (daily)

## Why this is worth watching
Most coding agent setups send file contents raw into the context window. Repowise replaces that pattern with an indexed representation: a call graph, git blame, generated wiki, ADR history, and dead-code map — all queryable via 10 MCP tools. The architectural premise is that agents should query a codebase index rather than read raw files, the same shift from filesystem dumps to structured retrieval that vector stores brought to document search. With 7,514 stars and 841 forks, this is past the "interesting prototype" stage. The self-reported 31.6% agent token reduction on the django/django benchmark is a testable claim, not a vague efficiency promise.

## What stands out immediately
- **Call graph across 26 languages** with per-edge resolution confidence — agents can ask "what calls this function" without hallucinating call relationships from file content
- **Dead-code detection** with confidence tiers — feeds directly into refactoring and removal decisions without requiring the agent to read every file
- **Architectural decision capture**: mines ADRs, code comments, commits, and agent session transcripts — "why was this built this way" becomes a queryable fact
- **Change-risk scores** (0–10) per commit or branch, plus test-impact analysis — changes the agent's uncertainty about what it might break
- **Reversible CCR cache**: the index is a local artefact, not a cloud upload; AGPL-3.0 license keeps it self-hostable
- **`headroom wrap`-style transparent injection**: `repowise serve` patches the MCP config for Claude Code, Codex, Cursor, VS Code without changing agent prompts
- **10 default + 7 opt-in MCP tools**: granular surface exposure lets teams limit what the agent can query
- **One-time indexing cost ~25 min for 3,000-file project**: upfront cost is bounded and documented

## Why clawfit should care
Repowise operates at L4 (MCP capability layer) but its effects reach into L5 (the agent's effective memory of the codebase) and L2 (harness-level context injection). clawfit currently scores agents on stated features and metadata; it does not model the effect of capability layer additions on recommendation quality. A team using Repowise with a standard harness will experience materially different token costs and accuracy than the baseline entry implies. The `governance_need: hard` filter axis is also relevant: AGPL-3.0 with no cloud upload satisfies data residency constraints that many tracked harnesses do not. The 7,514-star count also signals adoption beyond early adopters — this is not a "watch it reach 1k" situation.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability layer** (primary): 17 MCP tools exposing codebase intelligence to any MCP-compatible agent host
- **Level 5 — Observability/memory** (secondary): agent session transcripts fed back into architectural decision tracking creates a feedback loop between agent activity and codebase memory

## Claims to verify
- The 31.6% token reduction figure is self-reported on the django/django benchmark (43 questions, method not fully described on the project page); independent replication not confirmed
- AGPL-3.0 backend: the license requires source distribution of modified versions, which may complicate embedding in proprietary CI pipelines — relevant to `governance_need: strict` profiles
- Whether the 25-minute indexing time scales linearly with repository size (3,000 files is a mid-size project; large enterprise monorepos at 50k+ files are a different regime)

## Status
- First signal for "MCP-native codebase call-graph intelligence" as a distinct L4 sub-type
- Registry candidate: above 5k threshold, but AGPL-3.0 creates `governance_need: hard` complications; no per-call pricing model (self-hosted only); `agents.json` schema does not yet have a `capability_layer` category
- Next trigger: independent benchmark replication, a commercial-friendly license variant, or a cloud-hosted API mode with deterministic pricing
