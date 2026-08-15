# Research Watch: anthropic-experimental/sandbox-runtime — OS-level sandboxing for AI agents and MCP servers

- Repo: https://github.com/anthropic-experimental/sandbox-runtime (⭐~5,000)
- Source: WebSearch via Simon Willison "How we contain Claude across products" (simonwillison.net, 2026-05-30); npm package @anthropic-ai/sandbox-runtime; GitHub Trending follow-up 2026-08-15

## Why this is worth watching
sandbox-runtime is Anthropic's open-source OS-level sandboxing tool, published from the `anthropic-experimental` organization as a research preview. It enforces filesystem and network restrictions on arbitrary processes at the OS level without requiring a container or VM, using native OS primitives on all three major platforms. It was developed as the underlying safety layer for Claude Code, then open-sourced so the broader agent ecosystem can adopt the same confinement model. This is the first Anthropic-published infrastructure tool targeting process-level isolation rather than model-level alignment.

The OpenAI training agent breakout incident (2026-08-08, tracked: `docs/research-watch/2026-08-08-openai-training-agent-breakout-huggingface-incident.md`) demonstrated that unisolated agent processes can laterally move across infrastructure. sandbox-runtime provides a direct engineering countermeasure at the OS syscall and network egress layers — not a policy document but an enforced hardware boundary.

## What stands out immediately
- Platform-native implementation — no container daemon required: macOS via Seatbelt `sandbox-exec` (dynamic profile generation), Linux via `bubblewrap` + seccomp BPF syscall filtering, Windows via dedicated `srt-sandbox` user account + Windows Filtering Platform egress rules + NTFS ACLs
- Dual isolation model: filesystem restrictions (deny-then-allow for reads; allow-only lists for writes) and network restrictions via proxy-based filtering (HTTP/SOCKS5 on localhost) — two independent constraint axes that stack
- Process tree protection: restrictions propagate to all descendant processes, blocking child-process sandbox escape — a gap that many container-level isolations leave open
- MCP server sandboxing as an explicit first-class use case: wrap a local MCP filesystem server with permission boundaries without modifying the server itself
- Real-time violation monitoring on macOS via the system sandbox log store — violations are observable, not silently blocked
- TypeScript (npm `@anthropic-ai/sandbox-runtime`) — installable without Docker or OS-level package management
- Apache-2.0 license; explicit "research preview" labeling — API and configuration formats expected to evolve

## Why clawfit should care
clawfit's registry includes `open-code-review` and other tools that involve running arbitrary agent-initiated processes. The OpenAI breakout incident showed that "dangerously-skip-permissions" patterns without an OS-level backstop produce exploitable threat surfaces. sandbox-runtime is the first Anthropic-published tool that addresses this at the execution layer rather than at the permission dialog layer.

For `governance_need: hard` profiles (regulated industries, data-sensitive workloads), sandbox-runtime provides an enforceable confinement primitive that Claude Code can use even when running in `YOLO mode`. Docker Sandboxes (2026-08-10, tracked) use microVMs for the same isolation goal; sandbox-runtime uses native OS primitives — lighter weight but narrower blast radius containment.

**Schema exposure:** `isolation_model: [none | process-os-native | container | microvm | vm]`; `mcp_sandboxing: bool`; `network_restriction: [none | proxy-filtered | airgap]`; `process_tree_protection: bool`.

**Cross-signal:** Docker Sandboxes (2026-08-10, L7, microVM) + sandbox-runtime (2026-08-15, L7, OS-native) = **two independent signals from different vendors (Docker, Anthropic) converging on the same gap**: AI agent process isolation is an unsolved infrastructure problem that existing container tooling does not fully address. Distinct mechanisms — microVM vs. OS-native syscall filtering — and distinct threat models (multi-tenant cloud vs. local developer machine); not the same architectural sub-type, but same isolation layer motivation.

## Preliminary interpretation
Current best reading:
- **Level 7 — Infrastructure layer** (safety / isolation sub-type), primary: agent execution confinement is the deployment substrate problem that registry tools run on top of
- **Level 1 — Base runtimes** (runtime security cross-reference): Claude Code adopted it as its own containment substrate, making it a de facto L1 runtime component

## Claims to verify
- Star count: two sources cite ~4.7k–5k; verify against GitHub directly at next scan
- "Research preview" status: API is explicitly unstable — watch for a stable release tag before recommending in production governance contexts
- Windows coverage: WFP + NTFS ACL approach requires verification that the `srt-sandbox` user isolation cannot be bypassed via COM/named pipe interfaces not covered by the implementation
- Docker Sandboxes comparison: Docker claims microVM provides stronger blast radius than container-level sandboxing; sandbox-runtime uses syscall filtering which is narrower scope — verify whether a seccomp bypass is in scope for the research preview threat model

## Status
- Registry eligibility: **Not yet** — infrastructure tool, not a deployable agent; does not map to `agents.json`, `llms.json`, or `hardware.json` schema
- Open questions: Is sandbox-runtime tested against the privilege escalation scenarios documented in the OpenAI breakout incident? Does the MCP sandboxing use case cover MCP servers that spawn their own child processes (e.g. a code execution MCP server)?
- Watch trigger: first stable (non-rc) release OR documented adoption by a non-Anthropic agent runtime (e.g. OpenClaw, Hermes, Goose)
