# Research Watch: claude-code-harness — Autonomous Plan→Work→Review→Ship Cycle

- Repo: https://github.com/Chachamaru127/claude-code-harness
- Also see: GitHub Trending Daily #11 (2026-05-28); candidate support for Codex and other tools documented in README

## Why this is worth watching

At ~1,800 total stars with 87 earned today, claude-code-harness is gaining traction fast enough to watch but not fast enough to act on immediately. Its explicit motivation — countering "Claude Code drift" (plans staying in chat, tests skipped, review deferred to ship day) — names a failure mode rather than a capability feature, which is a useful differentiator from tool-use or orchestration harnesses. The five-slash-command cycle enforces workflow gate discipline at the IDE level, with Go runtime components providing native guardrails rather than relying solely on CLAUDE.md prose instructions.

## What stands out immediately

- **Five named slash commands forming a closed cycle:** `/harness-plan`, `/harness-work`, `/harness-review`, `/harness-sync`, `/harness-release` — the cycle is sequential and gate-enforced, not advisory. Commands are not standalone utilities; each gate is meant to block forward progression without evidence from the prior stage.
- **Go runtime guardrails (31% of codebase):** Unlike pure-shell harnesses (Pu.sh, 400-line, 2026-05-01) and pure-CLAUDE.md behavioral specs (Karpathy-skills, obra/superpowers), the Go components suggest runtime verification rather than prompt-side enforcement only. What exactly Go enforces vs. what the shell layer enforces is not documented in the provided brief — this is a claim to inspect against the actual repo.
- **Evidence tracking per phase:** The review gate implies structured evidence accumulation — not just LLM self-report but captured artifacts (test output, diff summaries) that the next phase can reference. Whether this is persisted across sessions or chat-local is unconfirmed.
- **Multi-IDE stance (Claude Code v2.1+ primary, Codex candidate):** Multi-runtime compatibility has emerged as a baseline expectation across the harness category (ouroboros, multica, Kanbots, Superset all target ≥2 runtimes). Claude-code-harness targets Claude Code first but positions Codex support as imminent — this is in line with the portability-as-default pattern observed since 2026-04-28.
- **Shell (44%) + Go (31%) + JS/TS (22%) composition:** The trilingual split is unusual. Shell handles invocation; Go handles guardrails; JS/TS likely handles IDE command surface. This means the harness is not trivially auditable the way Pu.sh is, and is not as standalone as CLAUDE.md-only specs.

## Why clawfit should care

**Comparison to existing harness entries.** Three prior harness signals are directly relevant:

1. **Pu.sh (2026-05-01, Level 2 minimal harness):** Claude-code-harness is more opinionated — it enforces a named lifecycle rather than simply closing the loop. Pu.sh's 400-line posture makes auditing trivial; claude-code-harness's Go runtime layer adds complexity and (potentially) enforcement guarantees Pu.sh cannot provide. They address the same root problem from opposite ends of the complexity/audit tradeoff.

2. **ouroboros (2026-05-04, Level 2 primary / Level 3 secondary):** ouroboros derives its SSOT from Socratic pre-flight questioning; claude-code-harness imposes a fixed five-phase cycle. Both quantify or enforce gates rather than leaving execution order to the model's discretion. The key structural difference: ouroboros generates a spec, then runs it; claude-code-harness wraps an existing workflow with enforcement checkpoints. These are complementary sub-types — pre-flight spec generation vs. in-flight cycle enforcement.

3. **obra/superpowers and gsd (Level 3, SSOT behavioral specs):** Those entries install workflow philosophy via CLAUDE.md prose — the model reads and attempts to follow the spec. Claude-code-harness moves part of the enforcement outside the LLM context window into Go runtime checks. This is the same structural shift noted in the Mendral loop-outside-sandbox post (2026-05-03): governance that lives outside the prompt is more durable than governance that lives inside it. If the Go guardrail claim holds, this represents a meaningful structural upgrade over pure-prompt-based workflow enforcement.

**Scoring axis implication.** The distinction "prompt-enforced workflow vs. runtime-enforced workflow" has no current axis in clawfit's scoring model. For `governance_need: hard` profiles — where skipped tests or unreviewed code carry real organizational risk — a harness with runtime checkpoints is categorically different from a harness that merely instructs the LLM to follow steps. If the Go enforcement layer is confirmed, this becomes a candidate criterion for a `workflow_enforcement_mode: runtime | prompt | hybrid` field in the registry schema.

**Harness reliability axis.** The 2026-04 scan notes flagged "harness reliability" as an emerging evaluation criterion (Hashline, sprint-contracts). Claude-code-harness's explicit "drift" framing is the sharpest articulation yet of what harness reliability failure looks like in practice: the LLM does what it prefers (code immediately, skip tests, defer review) rather than what the workflow requires. Naming the failure mode before naming the solution is an analytically honest design posture.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team harness / executable SSOT / governance layer (primary candidate)**

The Plan→Work→Review→Ship cycle with gate enforcement is structurally closer to Level 3 (governance of agent behavior via an executable SSOT) than to Level 2 (orchestration of multiple agents or runtime adapters). It does not route between models or spawn sub-agents; it constrains a single Claude Code session to a named workflow. The Go runtime guardrails, if confirmed as blocking gates rather than advisory checks, are a Level 3 governance mechanism — not an orchestration mechanism. This would position it alongside obra/superpowers and gsd, distinguished by runtime enforcement vs. prose-only enforcement.

Secondary Level 2 signal is weak: the multi-IDE compatibility and shell invocation layer are typical of Level 2 meta-wrappers, but they serve the governance loop rather than defining it. The tool is governed by what it enforces, not by what it abstracts.

Notable sub-type framing: if the Go enforcement layer is confirmed, claude-code-harness represents the first **runtime-enforced cycle harness** (as distinct from CLAUDE.md behavioral spec harnesses and from multi-agent orchestration harnesses). Single signal — sub-type formalization deferred per the standard two-signal rule.

## Status

- Tracking. Below 5k★ registry threshold (approx. 1,800 total stars at capture). Hold for registry entry.
- Promotion threshold: 5k★ OR independent confirmation of Go guardrail blocking behavior (not just advisory output). The latter would also advance the `workflow_enforcement_mode` axis candidate.
- Map mutation deferred: single signal for runtime-enforced cycle harness sub-type. Flag: if a second independent harness uses a compiled runtime component specifically for workflow gate enforcement (not just for performance), promote the sub-type without waiting for a scheduled calibration cycle.
- Open verification items: (1) whether Go guardrails block forward progression or only log/warn; (2) whether evidence artifacts persist across sessions or are chat-local; (3) depth of Codex support claim (candidate vs. implemented).
