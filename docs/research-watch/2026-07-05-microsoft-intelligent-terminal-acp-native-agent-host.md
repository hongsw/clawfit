# Research Watch: microsoft/intelligent-terminal — Terminal as First-Class ACP Host

- Repo: https://github.com/microsoft/intelligent-terminal (⭐1,400, 94 forks)
- Source: WebSearch + GitHub, shipped Build 2026 (June 2, 2026), HN coverage
- Also see: https://zed.dev/acp · https://www.jetbrains.com/acp/ · https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/

## Why this is worth watching

Intelligent Terminal is a Windows Terminal fork that ships with native Agent Client Protocol (ACP) support — making it the first major OS terminal to adopt ACP as a cross-vendor agent-host protocol. The signal is not the tool alone (1.4k stars, early-access state) but the protocol crystallization it represents: ACP is now adopted by Zed, JetBrains, and Microsoft across three distinct editor/terminal product lines. The LSP analogy from the project's own documentation is accurate — ACP stands to do for agent-to-IDE connections what LSP did for language-to-IDE connections. Microsoft's adoption at Build 2026 moves ACP from a Zed/JetBrains bilateral agreement to a cross-vendor standard with OS-terminal coverage.

## What stands out immediately

- **ACP over stdio, not a cloud proxy:** The terminal spawns the configured agent CLI as a local subprocess and passes shell context (command output, errors, shell state) over stdin/stdout via JSON-RPC 2.0. The terminal itself does not call any cloud API; data routing follows the chosen agent CLI's own policy.
- **Auto-detection of installed agent CLIs:** Copilot CLI, Claude Code, Codex, and Gemini are auto-detected on the host machine. Custom or local agents are configurable — the protocol, not the vendor, is the integration point.
- **Dockable agent pane, not a separate application:** The agent pane (Ctrl+Shift+.) is context-aware across multiple shells within the same terminal window. This is architecturally different from running a chat interface alongside a terminal in a split screen.
- **No conversation history persistence:** Data is held in memory for active sessions only; no on-disk transcript is written by the terminal layer itself. Provenance control stays with the agent CLI.
- **Ships separate from mainline Windows Terminal:** Positioned as an opt-in fork rather than a replacement, preserving existing Windows Terminal flows. Signals Microsoft treating this as an experimental surface rather than a committed product direction — relevant to stability scoring.
- **ACP provenance clarification:** ACP was co-developed by Zed Industries and JetBrains (joint agreement, October 2025); it is not a Zed-unilateral standard. Microsoft's adoption is the third anchor, making it a three-vendor cross-platform protocol.
- **LSP analogy as a framing signal:** Both the Intelligent Terminal docs and third-party coverage describe ACP as "LSP for AI agents." If this framing holds, it implies a future where ACP support becomes table-stakes for any professional terminal or IDE — with agents implementing the protocol once and running anywhere.

## Why clawfit should care

Two distinct implications:

1. **Terminal-as-ACP-host as a new L7 sub-type candidate:** The existing L7 taxonomy names Zed as the first IDE to absorb ACP multiplexing as a first-class editor feature. Intelligent Terminal extends that pattern to the terminal surface — a different product class. If ACP adoption continues (VS Code, Warp, iTerm2 would each be independent signals), "ACP-native terminal" should become a named L7 sub-type. Clawfit currently has no slot for distinguishing ACP-aware terminals from plain terminals in hardware or agent-surface scoring.

2. **Protocol standardization shifts the comparison model:** Today, clawfit's registry treats agent-to-tool connections as MCP (tool-use layer, L4c) or skill packs (L4b). ACP occupies a different slot — it governs how the agent CLI itself is hosted and how shell context is conveyed to it. A user running Claude Code inside an ACP-native terminal gets richer context injection than one running it in a plain shell. This is a latency and capability axis that the current registry does not model. If ACP becomes standard across terminals and IDEs, `acp_native: true/false` may become a meaningful registry field for L7 surfaces.

**Comparison with herdr (L2, tracked 2026-05-23):** herdr is a terminal multiplexer that adds a semantic state API (blocked/working/done/idle) and a Unix socket layer for orchestrating multiple agent sessions. It operates as a harness above the terminal — the protocol happens outside the terminal process. Intelligent Terminal operates at the opposite end: ACP integration is inside the terminal, injecting shell context to a single agent CLI over stdio. Herdr multiplexes sessions; Intelligent Terminal makes the terminal itself the protocol-aware host. These are complementary architectural choices, not competing ones, and they sit at different levels (L2 harness vs. L7 terminal surface).

## Preliminary interpretation

Current best reading:
- **Level 7 primary — Human interface / interaction layer** (terminal sub-type: ACP-native agent host — distinct from plain terminal, distinct from ACP-native IDE)
- **Level 1 secondary** — By auto-detecting and hosting agent CLIs as subprocesses, the terminal functions as a base agent surface for the user's working environment; the terminal choice directly influences which agents are accessible and what context they receive
- Not L2: Intelligent Terminal does not orchestrate multiple agent sessions or provide a harness API; it is a single-agent-at-a-time ACP host surface
- Not L4: ACP is not a tool-use layer (MCP); it governs agent-to-host communication, not agent-to-tool communication

**Ecosystem signal note (ACP cross-vendor):** Microsoft's adoption raises ACP from a bilateral (Zed + JetBrains) to a three-vendor standard. The ACP Agent Registry is live with Claude Code, Codex CLI, GitHub Copilot CLI, OpenCode, and Gemini CLI registered. This is the strongest cross-vendor protocol convergence signal in the L7 layer to date. If a fourth major surface (VS Code, Warp, or iTerm2) adopts ACP, the taxonomy should consider whether ACP warrants a dedicated cross-cutting axis annotation, analogous to the MCP protocol annotation at L4.

## Claims to verify

- Whether Intelligent Terminal 0.1 has shipped a stable Windows installer or remains in preview/nightly-only state
- Whether the "auto-detection" of agent CLIs uses ACP capability handshake or simple binary path detection — the distinction matters for how fragile the integration is across CLI version changes
- Whether the agent pane preserves shell context across tab/pane splits, or only for the active shell session
- Whether Microsoft has committed a support timeline or positioned this explicitly as experimental (the separate-fork shipping strategy is consistent with either read)
- Whether JetBrains ACP registry and the Intelligent Terminal ACP implementation share a common spec version — ACP has had breaking changes between the Zed/JetBrains bilateral and the public registry release

## Status

- 1,400★ below the 5k registry threshold; early-access fork, Windows-only — registry hold
- First signal for "ACP-native terminal" as an L7 sub-type candidate (distinct from ACP-native IDE, established 2026-04-30 via Zed)
- ACP three-vendor milestone (Zed + JetBrains + Microsoft) is a standalone ecosystem signal — if a fourth major surface adopts ACP by end of Q3 2026, recommend annotating ACP as a cross-cutting axis at L7 alongside the existing MCP axis at L4
- Promotion criterion: 5k★ OR documented adoption by a non-Windows platform (macOS/Linux terminal or VS Code), OR a tracked L1/L2 agent explicitly lists "ACP-native terminal" as a supported deployment surface
