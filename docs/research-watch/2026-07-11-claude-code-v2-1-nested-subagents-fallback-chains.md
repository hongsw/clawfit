# Research Watch: Claude Code v2.1 — 5-Level Nested Subagents and Fallback Model Chains

- Repo/Link: https://code.claude.com/docs/en/agent-sdk/subagents
- Source: Anthropic Claude Code changelog / sitepoint.com feature summary (June 2026)

## Why this is worth watching
Claude Code v2.1.172 (released June 10, 2026) extended the harness's subagent architecture from 3 levels to 5 levels and introduced fallback model chains — two changes that together materially change how clawfit should model Claude Code's task capability. The 5-level hierarchy is not a cosmetic increment: Anthropic's internal research found that 5 levels cover "virtually all practical software engineering workflows." The fallback chains add cost governance that wasn't previously programmable — per-model cost ceilings and automatic downgrade on rate limits.

## What stands out immediately
- Subagent hierarchy depth: parent → child → grandchild → up to 5 levels; each level can spawn its own children
- Prior depth was 3 levels (v2.0); the additional 2 levels target multi-module software engineering workflows spanning codebases with complex dependency structures
- `fallbackModel` config: ordered list of models Claude Code attempts sequentially on rate limit or unavailability
- Per-model `maxTokens` and `costCeiling` parameters in fallback chain: dollar-amount budget per model before advancing
- Automatic fallback: no user intervention required; the runtime detects rate-limit errors and rotates
- Generally available as of CLI 2026.6 release train
- Nested subagents, fallback models, and the Anthropic marketplace available together in same release
- Natural language invocation preserved at all levels: no new syntax for nested delegation

## Why clawfit should care
The `statefulness: session` agents in clawfit's registry (e.g., `react-agent`) implicitly assume a flat or shallow execution model. 5-level subagent support changes the effective `tasks` capability — a Claude Code agent can now decompose and delegate to specialist subagents at depth, covering larger codebases than any single-turn agent could. Scoring for `tasks: code-gen` + `maturity_min: 6+` profiles should surface this capability. The fallback chain with `costCeiling` also introduces a new governance primitive: per-model spend limits are not just about cost, they define what level of capability the agent is authorized to invoke. This maps to a `governance_need` scoring dimension clawfit is already evaluating. Schema watch: `max_agent_depth: int` as a capability field; `fallback_chain: true/false` for cost governance.

## Preliminary interpretation
- **Level 2 — Harness/wrapper** (primary: Claude Code is a harness; this is a harness capability update)
- **Level 3 secondary** (fallback chain with cost ceiling is a behavioral governance primitive, not just error handling)
- This is Anthropic's official answer to the multi-agent orchestration depth that Microsoft Agent Framework, agentscope, and OpenManus offer

## Claims to verify
- "5 levels covers virtually all practical software engineering workflows" — this is Anthropic's own research; no independent validation cited
- Fallback chain rate-limit detection: whether the trigger is HTTP 429 only or also covers context window limits and API errors in general
- Marketplace integration depth: whether marketplace plugins are accessible at all 5 subagent levels or only at the root agent level

## Status
- First signal 2026-07-11 (official Anthropic product update; no star count applicable)
- No registry entry: Claude Code is already implicitly referenced in agents.json via preferred_llms; this is a capability update, not a new agent type
- Schema watch: `max_agent_depth: int`; `fallback_chain: true/false`; `cost_ceiling_supported: true/false`
- Monitor: whether analogous depth increases appear in Codex CLI, Goose, or Pi — a cross-harness race on agent hierarchy depth would be a category signal
