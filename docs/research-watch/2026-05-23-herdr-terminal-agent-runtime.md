# Research Watch: Herdr — Agent-Aware Terminal Multiplexer

- Repo: https://github.com/ogulcancelik/herdr
- Also see: https://herdr.dev · docs/research-watch/2026-04-06-ohmy-pi-hashline-harness-problem.md · docs/research-watch/2026-05-22-runtime-yc-team-agent-sandbox.md

## Why this is worth watching
Herdr sits at an architectural gap that no other tracked entry occupies: it treats the terminal multiplexer itself as the harness surface rather than building a separate overlay. Persistent sessions, semantic state tracking (blocked/working/done/idle), and a socket API for programmatic pane control are all native to the same single Rust binary — there is no daemon, web dashboard, or Electron shell. The AGPL-3.0 license and 2.1k stars at v0.6.1 suggest early but active development with a meaningful community footprint.

## What stands out immediately
- Single Rust binary for Linux and macOS; AGPL-3.0; 92% Rust; v0.6.1 released 2026-05-22
- Socket API (newline-delimited JSON over Unix socket): agents programmatically create workspaces, spawn panes, run commands, read output, and wait for state transitions — structured orchestration from within the agent, not from a separate controller
- Semantic agent states (blocked / working / done / idle) surfaced in a sidebar; workspace rollup shows the most urgent state across all active agents — distinct from tmux's dumb session model
- Built-in detection for Claude Code, Codex, Opencode, Pi, Hermes, Droid, Amp; direct attach integrations for at least five of these
- Remote operation via SSH without additional apps; sessions survive terminal disconnect (PTY persistence)
- SKILL.md ships as the CLI reference, signaling alignment with the cross-vendor portability pattern tracked at L4b
- 2.1k stars, 141 forks, 37 open issues — organic engagement, not a star-farm pattern
- No pricing published; AGPL-3.0 is a hard blocker for `governance_need: hard` profiles without a commercial license agreement

## Why clawfit should care
Herdr targets the same harness-reliability problem analyzed in the ohmy-pi Hashline doc — long-running agent workflows losing coherence — but from a different angle: instead of file-hash verification inside the agent, it externalizes session continuity and state visibility to the multiplexer layer. The socket API makes it a coordination substrate that sits below the orchestration tools tracked at L2 (multica, Runtime YC, DureClaw) but above the raw VM/PTY layer (Freestyle). clawfit has no current axis for terminal-multiplexer-as-harness; this would require a new sub-type under L2 distinct from "project-management + harness collapse" and "sandboxed team agent platform." The `statefulness: persistent` filter is directly relevant: Herdr is the first terminal-native entry that makes persistence a first-class harness property rather than an agent-side concern.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (primary): Herdr wraps multiple L1 agent runtimes inside a persistent, API-driven terminal session layer; the orchestration surface is the socket API, not the agent itself
- **No credible secondary classification**: the semantic state display is a human interface primitive, but it is entirely terminal-resident — does not constitute a standalone L6 surface

Candidate sub-type for L2: "terminal-multiplexer-as-agent-harness" — structurally distinct from cloud sandbox harnesses (Runtime YC, Freestyle) and from project-management collapses (multica). Single signal; sub-type formalization deferred.

Comparison with ohmy-pi (L2): ohmy-pi addresses harness correctness at the protocol level (Hashline file-hash verification). Herdr addresses harness continuity and observability at the session level (PTY persistence + state sidebar). Both are responses to the "harness problem"; neither subsumes the other.

## Status
- 2.1k stars — below the 5k-star registry promotion threshold; map mutation deferred
- AGPL-3.0 license is a hard blocker for `governance_need: hard` without a commercial agreement
- Promotion threshold: 5k stars OR an independent benchmark or case study confirming multi-agent socket orchestration at production scale
- Watch: whether the SKILL.md API surface enables cross-agent portability consistent with the tracked SKILL.md cross-vendor axis (currently four signals, stable)
