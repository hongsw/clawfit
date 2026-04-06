---
# Research Watch: Anthropic engineering — harness design for long-running applications

- Article: <https://www.anthropic.com/engineering/harness-design-long-running-apps>

## Why this is worth watching
This is **Anthropic's own engineering blog describing multi-agent harness patterns** for long-running autonomous coding tasks. It is a primary source — not a third-party interpretation — of how the harness layer should be architected. Patterns described here will likely influence all harness projects built on Claude.

## What stands out immediately
- **Dual-agent design:** two agents with distinct roles (planner + executor split)
- **Context reset mechanisms:** strategies for handling long sessions without context overflow
- **Sprint contracts:** bounded work units as a primitive for autonomous coding
- Target use case: complex frontend and full-stack development tasks
- Published by Anthropic engineering — represents internal production patterns

## Why clawfit should care
This article defines the **canonical harness architecture from the model provider's perspective**. clawfit's `plan-execute` agent pattern (already in `agents.json`) is closely related — but the dual-agent + sprint-contract pattern described here is more structured. Key implications:
1. The `plan-execute` registry entry may need richer description
2. Sprint contracts could become a scoring dimension (bounded autonomy vs. open-ended)
3. Context reset strategy may be a new axis for harness comparison in the taxonomy

## Preliminary interpretation
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (architectural pattern definition)
- Authoritative: Anthropic-published pattern — treat as near-canonical for Claude harness design

## Status
- High priority reference. Should be cited in `docs/reference-levels.md` Level 2 notes.
- Flag for scoring-analyst: sprint contract / bounded autonomy as potential new scoring axis.
