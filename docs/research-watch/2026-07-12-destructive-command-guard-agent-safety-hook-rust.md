# Research Watch: Destructive Command Guard — PreToolUse safety hook for AI coding agents

- Repo: https://github.com/Dicklesworthstone/destructive_command_guard (⭐2,633)
- Source: GitHub Trending (444 stars gained in one day — July 12, 2026)

## Why this is worth watching
Every AI coding agent that can execute shell commands carries a concrete risk: the agent proposes `git reset --hard`, `rm -rf ./src`, or `DROP TABLE users` and the host system executes it before the operator notices. Destructive Command Guard (DCG) is a Rust binary that intercepts commands at the PreToolUse hook point — before execution — and denies those matching a pattern database of 50+ destructive categories. It is not an agent itself; it is a safety layer that wraps any compliant agent. The 2.6k-star traction in a narrow safety niche, plus 444 stars in a single day, indicates this is solving a real problem that teams have been patching individually with ad-hoc hooks.

## What stands out immediately
- Operates as a `PreToolUse` hook — reads command JSON on stdin, returns deny decision before execution proceeds
- SIMD-accelerated quick-reject passes 95%+ of commands in <10μs; only suspicious commands proceed to full regex matching
- Tree-sitter / ast-grep for AST-level pattern matching (catches obfuscated or templated destructive commands)
- 50+ rule categories organized in a "pack" system — can be selectively enabled per team policy
- Native installer supports Claude Code, Codex CLI 0.125.0+, Gemini CLI, GitHub Copilot CLI, Cursor IDE, Grok, Aider, Hermes Agent
- Written in Rust with zero unsafe code; ships prebuilt binaries with SHA256 verification
- DCG is the companion to `cass_memory_system` (persistent cross-agent memory) by the same author

## Why clawfit should care
This occupies the agent-constraints sub-layer that sits between L2 (harness) and L3 (SSOT/governance). DCG is not a harness — it does not orchestrate agents — but it enforces a hard safety boundary that harnesses should ideally enforce. If this pattern becomes standard (teams adopting DCG or equivalents as part of their Claude Code/Codex deployment), it becomes a taxonomy signal: "agent runtime + safety hooks" as a distinct configuration archetype. clawfit's current scoring has no `safety_level` dimension; a tool like DCG hints that teams operating in sensitive environments may need that axis. The registry's hardware/network fields don't capture governance constraints — this suggests a gap.

## Preliminary interpretation
Current best reading:
- **Level 3 — Team / SSOT / Governance Layer** (enforces team-level constraints on what agents are allowed to execute)
- Secondary: **Level 4 — Capabilities / Skills / MCP Layer** (operates at the tool-execution boundary, specifically PreToolUse hooks)

## Claims to verify
- Whether the pattern pack is community-maintained or author-only (determines long-term coverage quality)
- Whether SIMD path is portable across ARM/x86 without manual configuration
- Whether AST-based matching has meaningful false-positive rate in typical coding agent sessions
- The "2.6k stars" figure — verify whether this represents organic adoption or a spike from a viral post
- Whether competing hooks (in oh-my-claudecode, claude-code-templates) duplicate this functionality

## Status
- 2,633 stars exceeds registry threshold of 5,000? No — below 5k for registry inclusion
- No registry entry warranted today: star count below threshold and no deterministic cost/latency data (it's a local binary with no inference cost)
- Taxonomy note: if 2+ signals confirm the "agent safety hook" pattern, this warrants a new L3 sub-type entry in reference-levels.md
- Re-evaluate at 5k stars for potential registry entry as a harness-adjacent safety tool
