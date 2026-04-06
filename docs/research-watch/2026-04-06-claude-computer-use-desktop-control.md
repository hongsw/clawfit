---
# Research Watch: Claude Computer Use — direct mouse, keyboard, screen control

- Reference: <https://x.com/felixrieseberg/status/2036193240509235452>

## Why this is worth watching
Anthropic shipped native computer control for Claude — direct mouse, keyboard, and screen operation without a specialized vision API wrapper. Integration is through Claude Code Desktop and the Cowork product. Remote task dispatch is available via a `Dispatch` layer. macOS first, Windows "within weeks." This is Anthropic's move into the **computer-use layer** that previously required separate tooling (browser agents, RPA, vision APIs).

## What stands out immediately
- **First-party integration:** shipped inside Claude Code Desktop, not a third-party plugin
- **Cowork integration:** computer use is part of the consumer-facing agentic product
- **Remote dispatch:** tasks can be triggered and monitored remotely via Dispatch
- **Deliberate pacing:** Claude operates slower than humans intentionally — accuracy over speed
- **Cross-surface:** any application on the system, not just browser or terminal

## Why clawfit should care
Computer use collapses what were previously distinct layers:
- Level 1 (runtime) + Level 7 (human interface) merge when the agent can directly operate the desktop
- `understudy` (tracked separately) is now a direct competitor pattern to Claude's own computer use
- The `latency: high` implication of deliberate pacing is a scoring signal for computer-use tasks

For clawfit's registry: if a task type `desktop-automation` were added, Claude (via Cowork/Desktop) and `understudy` would be the primary candidates. Neither fits current task taxonomy well.

## Preliminary interpretation
- Primary: **Level 7 — Human interface / input-output layer** (direct desktop control)
- Secondary: **Level 1** (extends base runtime capability envelope)
- Implication: Level 7 should be renamed or expanded to include "computer use / desktop control"

## Status
- High priority. First-party Anthropic feature affecting taxonomy.
- Flag for ecosystem-mapper: consider expanding Level 7 definition to include computer-use agents.
