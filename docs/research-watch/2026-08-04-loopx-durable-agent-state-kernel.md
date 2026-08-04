# Research Watch: loopx — Durable State Kernel for Long-Running Agent Teams

- Repo: https://github.com/huangruiteng/loopx (⭐1,523)
- Source: GitHub Trending Python #4 (618 stars/day, 2026-08-04)

## Why this is worth watching

loopx describes itself as a "lightweight state kernel for long-running AI agent teams with durable goals and auto-wake capabilities." The word choice — kernel, not harness or framework — is deliberate: it does not replace the agent execution runtime, it sits beneath it and maintains persistent control state across agent turns, restarts, and handoffs between agents.

The problem it addresses is real: existing L2 harnesses (qm, oh-my-pi, Hermes, OpenWork) manage agent *execution* but not agent *continuity*. When a long-running coding session is interrupted — the terminal closes, the token budget runs out, the user walks away — harnesses typically lose all tracking state. loopx proposes to make that state durable and auditable, independent of which agent runs next.

## What stands out immediately

- **Objectives and goals layer:** persists what the agent is trying to accomplish across turns — not just the conversation history, but the structured goal representation that survives session restarts
- **Typed todos and claims:** task ownership can be assigned to specific agents and handed off between them, with peer verification before accepting a handoff
- **Gates:** explicit human judgment checkpoints requiring manual approval before the agent continues — models the "human-in-the-loop" pattern as a first-class state machine event rather than a harness convention
- **Evidence logs:** maintains a validated run history linking agent actions to their declared objectives, producing an audit trace without requiring a full observability platform
- **Quota tracking + auto-wake:** monitors token and execution budget consumption; automatically decides whether the next agent turn should fire based on remaining budget and scheduling hints
- **Agent-agnostic design:** declared compatible with Claude Code, Codex, Cursor, and others — the state layer is not bound to any single agent runtime
- **Philosophy stated explicitly:** "Keep the loop moving. Keep the judgment human."

## Why clawfit should care

loopx occupies a position between L2 (harness) and L3 (governance/behavior control) that no existing registry entry covers. It is not a harness that runs agents; it is the state substrate that makes multi-turn, multi-agent, and resumable work auditable and controllable. The distinction matters:

- For `governance_need: hard` profiles, loopx provides durable audit trails without requiring a full observability platform (Langfuse tier)
- For `statefulness: session` profiles, loopx extends session semantics into durable-goal semantics — a session that can survive agent restarts
- For multi-agent orchestrations (task: orchestration), loopx's typed todo handoff model provides the first structured peer-verification pattern in the corpus
- The quota-aware auto-wake mechanism is a new primitive for cost-controlled background agent work — relevant to `monthly_budget: low` profiles running long tasks

Schema gap: `state_persistence: [none | session | durable]` — current filters assume either stateless or session-scoped; loopx introduces a durable tier. Also: `human_gate_model: [none | advisory | blocking]` — gates are structurally different from audit logging.

## Preliminary interpretation

- **Level 2 — Agent harness / wrapper layer** (primary: manages the agent execution loop and state)
- Secondary: **Level 3 — Governance / behavior control** (gates implement policy enforcement as state machine transitions)
- Cross-watch: toris-agent (2026-08-04, evidence receipt) shares the auditability goal but operates post-hoc (receipt after completion); loopx operates continuously during execution — complementary, not overlapping

## Claims to verify

- **Agent-agnosticism:** verify that the state kernel integrates with Claude Code and Codex without harness-level coupling to a specific CLI; the handoff model requires protocol compatibility
- **Gate enforcement:** verify whether gates are technically blocking (agent cannot continue without approval) or advisory (agent proceeds and logs the skipped gate) — the distinction matters significantly for `governance_need: hard`
- **Production vs. early-stage:** 1,523 stars with 618 stars today suggests a viral trending day rather than established production use; check commit history depth and test coverage
- **Auto-wake precision:** verify whether quota-aware scheduling integrates with actual token counting APIs or estimates usage independently

## Status

- First signal for "durable agent state kernel" pattern (distinct from session-scoped harnesses)
- 1,523 stars meets threshold; high velocity (618/day) suggests discovery wave rather than established adoption
- No registry entry: `task: orchestration` is the closest match but state management is cross-task
- Schema watch: `state_persistence: [none | session | durable]`; `human_gate_model: [none | advisory | blocking]`; `multi_agent_handoff: bool`
- Cross-watch: toris-agent (2026-08-04) — complementary auditability primitives; qm (2026-08-01) — shares governance intent but operates as a full harness rather than a state substrate
