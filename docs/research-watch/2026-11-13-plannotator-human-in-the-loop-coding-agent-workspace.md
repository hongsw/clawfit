# Research Watch: plannotator — Human-in-the-Loop Annotation Workspace for Coding Agents

- Repo: https://github.com/backnotprop/plannotator (⭐10,364)
- Source: GitHub Trending (all languages, daily, 2026-11-13)

## Why this is worth watching

plannotator creates a persistent, local review surface between the user and any coding agent — not as a wrapper or fork, but as a lightweight annotation layer that agents publish to and users respond through. Rather than adding yet another prompt structure or approval mechanism, it provides a browser-based inbox, plan-review pane, and inline code annotator that multiple agent systems already support. The 10k+ stars in what appears to be an early release, with support for Claude Code, Codex, Copilot CLI, Gemini CLI, and six other agents, indicates this fills a real gap.

## What stands out immediately

- **Structured plan review:** When an agent proposes a plan, plannotator intercepts it, opens a browser UI, and waits for the user to annotate, approve, or deny; denials return structured feedback to the agent rather than a raw text rejection
- **Inline code review:** Works on local diffs, GitHub PRs, and GitLab MRs with inline comments that are routed back as agent feedback
- **Annotation surface for artifacts:** Users can annotate markdown files, HTML artifacts, URLs, and agent replies — not just code
- **Plannotator Inbox:** A persistent message channel where agents send questions and files; the user replies asynchronously; this decouples the agent's output cadence from the user's attention
- **TUI mode:** A terminal-based variant (`Herdr Annotate`) for users who prefer to stay in the terminal
- **Broad agent support:** Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro, Droid, Amp, DeepSeek Harness, Pi — the breadth suggests a protocol-neutral design
- **Privacy-conscious sharing:** AES-256-GCM encrypted short links with SLSA provenance attestations and SBOM; no usage telemetry reported
- **IDE and tool integrations:** VS Code, Obsidian, Bear, Notion; devcontainer and SSH remoting support

## Why clawfit should care

The existing clawfit harness registry evaluates agents on latency, cost, and task type. plannotator is not an agent — it is the missing approval and feedback layer that every agent harness currently handles internally (or not at all). Three dimensions of clawfit's current scoring are affected: (1) `statefulness` scoring does not distinguish between agents with structured human-in-the-loop cycles and those with just an approve/deny prompt; plannotator materializes that gap. (2) The `task: code-gen` and `task: qa` profiles assume the human reviews output after the fact; plannotator lets the human annotate at plan time, which changes what a recommendation means. (3) Multiple agents using plannotator simultaneously via the shared Inbox is a first signal for a "shared human-review bus" pattern — no existing registry entry covers this.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper Layer** (primary) — plannotator is a human-facing harness complement: it does not run the agent but manages the review loop that sits between user and agent
- **Level 6 — Human Interface Layer** (secondary) — the Inbox, annotation surface, and browser review pane are distinct human interface primitives that go beyond a simple approval dialog

## Claims to verify

- Whether the "structured feedback on denial" is a free-text return or a structured schema that agents consume — the difference matters for harness-level compatibility
- Star count reliability: 10,364 at time of scan; the dual Apache-2.0/MIT license and security features suggest serious intent, but creation date and velocity are not shown
- Whether agents receive plannotator annotations via CLI pipe, MCP, or a custom protocol
- TUI mode maturity vs. browser mode

## Status

- New signal — tracking; registry action deferred (not an agent/LLM/hardware entry; a potential `review_surface` capability dimension is under consideration)
- **First signal for "structured human-in-the-loop annotation workspace for coding agents"** as a distinct product category — distinct from approval-prompt models (Open Duet's four-tier approval 2026-11-04), plan-only gatekeeping, and inline review hooks
