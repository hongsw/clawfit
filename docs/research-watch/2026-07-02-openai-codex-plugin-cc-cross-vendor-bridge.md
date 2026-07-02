# Research Watch: openai/codex-plugin-cc — Cross-Vendor Code Review and Delegation Bridge

- Repo: https://github.com/openai/codex-plugin-cc (⭐22,481)
- Source: GitHub Trending (all languages, daily, 2026-07-02; +448 today)
- Language: JavaScript (100%)
- License: Apache 2.0
- Created: 2026-03-30; latest release: v1.0.5 (2026-06-23)

## Why this is worth watching

openai/codex-plugin-cc is an official OpenAI plugin that connects a running Claude Code session to the OpenAI Codex CLI and Codex app server — enabling cross-vendor code review, adversarial review, and task delegation from inside a Claude Code context. It does not run a separate Codex runtime; it wraps the locally installed `codex` binary and inherits Codex authentication. The practical implication is that a team using Claude Code can access Codex model opinions on the same codebase without context switching and without duplicating credentials.

At 22,481 stars with five point releases in three months, this is a tool in active use, not an experiment. The cross-vendor provenance — official OpenAI plugin targeting Claude Code — is structurally unusual. It signals that at least OpenAI sees Codex and Claude Code as complementary tools in the same user workflow, not mutually exclusive alternatives.

## What stands out immediately

- **Official OpenAI authorship targeting Claude Code**: this is not a community bridge — it comes from the Codex team, shipped to the Claude Code plugin marketplace
- **Seven slash commands** covering the full review-and-delegation cycle: `/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:transfer`, `/codex:status`, `/codex:result`, `/codex:cancel`
- **`/codex:adversarial-review`**: specifically designed to steelman and challenge the current implementation — pressure-tests design decisions, failure modes, and alternative approaches; free-form focus text makes it steerable
- **`/codex:transfer`**: converts the active Claude Code session transcript into a persistent Codex thread; the resulting `codex resume <session-id>` command allows seamless handoff to the Codex App or TUI — session state is preserved across tool boundaries
- **`/codex:rescue`** delegates to a `codex-rescue` subagent running inside the Agent tool — task can be resumed in the Codex App/TUI after the fact
- **Optional Stop hook as review gate**: a `Stop` hook that triggers a targeted Codex review on every Claude response before it completes; documented to create long-running loops that can drain usage limits — a notable honesty in the README
- **Background mode on review commands**: `--background` flag runs Codex review asynchronously while Claude Code continues; `--wait` blocks until complete; either mode writes to the session log
- **Cross-vendor config delegation**: defers entirely to `~/.codex/config.toml` for model, effort, and base URL settings — no plugin-specific config format required

## Why clawfit should care

This is the first tracked signal for a cross-vendor agent skill — a capability layer defined by one AI lab that explicitly routes tasks to a second lab's runtime. The existing L4 taxonomy (skills, plugins, MCP tools) assumes a single-vendor skill pack: a Claude Code skill does Claude Code things; a Codex skill does Codex things. codex-plugin-cc is a delegation bridge, not a skill in the conventional sense.

The structural implication for clawfit is a new `agent_delegation_target` concept: when a user has both Claude Code and Codex installed, some workflows (adversarial review, independent second-opinion debugging) are better served by dispatching to a second agent runtime with a different model. clawfit's current (agent, llm, hardware) triple does not model multi-runtime configurations. The `codex-plugin-cc` pattern suggests that an increasingly common user setup involves a primary agent with secondary-agent delegation targets — a configuration the recommendation model does not currently surface.

The Stop-hook review gate is also architecturally relevant to the `governance_need: hard` profile: it implements a lightweight quality gate on every agent response without a separate observability system. Whether that pattern belongs at L4c (plugin) or L3 (governance enforcement) is a genuine classification question.

## Preliminary interpretation

Current best reading:
- **Level 4c — Tool-use / plugin / MCP layer** (primary): a skill module that adds Codex-delegated capabilities to a Claude Code agent session
- **Level 3 secondary — Governance / SSOT** (weak): the optional Stop-hook review gate enforces a quality gate on agent responses, which is a lightweight governance pattern

The cross-vendor framing suggests this might warrant a new sub-type rather than a clean classification into existing categories. Monitor for whether other labs ship similar bridge plugins — if Gemini CLI gets a Claude Code plugin or vice versa, a `cross-vendor-delegation` L4 sub-type becomes justified.

## Claims to verify

- Star count accuracy: trending data shows 22,481 total stars from a March 30, 2026 creation date — a rapid accumulation; whether this reflects organic adoption or a spike needs a star-history check
- Codex version compatibility: the plugin targets the Codex CLI; whether it works with both the npm `codex` package and the Codex app server identically, or only one, is not explicit in the README
- Stop-hook behavior on loop termination: the README warns of draining usage limits but does not specify any built-in circuit breaker; whether runaway loops are protected is unverified
- `/codex:transfer` persistence: whether session transcript conversion to a Codex thread retains full fidelity or a compressed summary is not confirmed

## Status

- First signal — 2026-07-02; 22,481★, Apache 2.0, official OpenAI authorship, active release cadence
- Registry candidate: `tasks: [code-gen, code-review]`, `roles: [developer]`, `network: online`, `statefulness: session`, `pricing_tier: paid` (requires ChatGPT subscription or OpenAI API key)
- Promotion criterion: 25k★ AND independent write-up confirming production use in a multi-agent workflow; OR cross-vendor delegation becomes a named L4 sub-type warranting dedicated classification
