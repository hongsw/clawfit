# Research Watch: Pocketty — iPhone SSH Terminal for AI Agent Monitoring

- Repo/Link: https://pocketty.app/
- Source: Hacker News (Show HN, front page 2026-10-09)

## Why this is worth watching
Pocketty extends herdr (tracked 2026-05-23) into a dedicated iPhone interface: it receives push notifications when an agent is blocked or done, then lets the user reply in a real SSH terminal without opening a laptop. The coupling between herdr's semantic agent-state API (blocked/working/done/idle) and a phone-native notification delivery chain is a new architectural primitive for human-in-the-loop agent workflows.

## What stands out immediately
- **Notification on block**: herdr detects the agent state transition; Pocketty delivers an end-to-end encrypted alert sealed with the phone's Secure Enclave key — no plaintext in the relay
- **Full SSH terminal from the alert**: tapping the notification opens the exact pane over SSH with real keystrokes (Return, Esc, Ctrl, arrows)
- **Turn diffs**: view what the agent changed in the current turn, since session start, or since the last commit — directly from the phone
- **Live multi-agent status**: see all running agents and their states without opening any pane
- **Supports Claude Code, Codex, OpenCode, Gemini CLI** (reads state from herdr, not from agent config)
- **Commercial, not open-source**: $99 one-time (launch price; rising to $129)

## Why clawfit should care
Herdr already represents the "terminal-multiplexer-as-agent-harness" sub-type at L2. Pocketty is the first tracked signal showing that sub-type extended to a dedicated mobile client — the agent monitoring surface has separated from the desktop terminal surface entirely. This is relevant to `output_destination` and `frequency: daily` scoring for solo and small-team developer profiles who run agents overnight or across locations. It also reinforces the herdr ecosystem (herdr + Pocketty) as a more complete stack than a single-tool entry.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human interface layer** (primary): Pocketty is the human-facing notification and terminal surface; it adds no orchestration capability of its own
- **Level 2 secondary**: tightly coupled to herdr's L2 harness state model; cannot function without herdr as the underlying runtime

## Status
- No open-source GitHub repo published; commercial iOS app only
- Herdr coupling: tracks herdr's ecosystem closely; if herdr reaches the 5k-star registry threshold, Pocketty surfaces as a companion tool note
- First signal for "mobile-first human-in-the-loop agent notification" sub-type at L6
