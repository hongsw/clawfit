# Research Watch: ouroboros (Q00/ouroboros) — Agent OS, Spec-First Execution

- Repo: https://github.com/Q00/ouroboros
- Also see: https://github.com/Q00/ouroboros/blob/main/CLAUDE.md (CLAUDE.md skill integration), https://github.com/Q00/ouroboros/releases (v0.32.0 latest, 77 releases)

## Why this is worth watching

ouroboros is the highest-velocity spec-first agent runtime to surface in this taxonomy — 3.2k stars, 312 forks, 773 commits, and 77 releases against a Python-heavy codebase with Rust components suggests sustained development rather than a spike. It occupies a distinct structural position: it is not a harness wrapper over a base agent (L2) nor a behavioral spec file (L3 SSOT), but a standalone local-first execution runtime that *generates* the spec from Socratic questioning before any code runs — sitting between those two layers with a quantified ambiguity gate. The combination of measurable pre-flight criteria (ambiguity ≤ 0.2, ontology convergence ≥ 0.95) and a named persistent runner ("Ralph" via event sourcing) distinguishes it from the looser workflow systems already tracked at L2 and L3.

## What stands out immediately

- **Four-phase loop with named gates:** Interview → Seed → Execute → Evaluate. Each transition is governed, not assumed — ambiguity scoring blocks the Seed phase if goal/constraint/success-criteria clarity does not reach 80% weighted. This is a claim to inspect; the formula is documented in the repo but independent reproductions of the threshold behavior are not yet available.
- **Nine specialized reasoning personas loaded on-demand:** Socratic Interviewer, Ontologist, Seed Architect, Evaluator, Contrarian, Hacker, Simplifier, Researcher, Architect. These are not sub-agents in the multi-agent harness sense; they are modal personas applied to structured reasoning phases, more analogous to a checklist-enforced review process than to parallel agent spawning.
- **Ontology convergence termination criterion:** The evolutionary loop halts when consecutive schema generations score ≥ 0.95 similarity (name overlap 50%, type matching 30%, exact field matching 20%), with a 30-generation ceiling and stagnation detection. Quantitative loop termination is uncommon in this ecosystem; most harnesses exit on task completion or timeout.
- **Ralph — stateless persistent runner via event sourcing:** `ooo ralph` reconstructs session state from an event journal (SQLAlchemy + aiosqlite) rather than holding in-memory state. This design means the convergence loop survives process restarts and is replayable — a property not present in, e.g., acai.sh (ACID requirement SSOT, tracked 2026-05-03) or gsd (prose spec-driven, L3 primary), which operate on static spec files.
- **PAL Router — 3-tier cost-escalation:** 1x / 10x / 30x cost tiers with auto-escalation logic. Suggests the system makes LLM inference-cost decisions autonomously as complexity rises — relevant to clawfit's cost scoring dimension.
- **Runtime abstraction over multiple base agents:** Targets Claude Code, Codex CLI, OpenCode, and Hermes. This is the third multi-vendor adapter cluster signal in the past week (after cc-switch, awesome-codex-skills); it reinforces the portability-as-default-design pattern without itself being a switcher utility.
- **97.3% Python, Rust components:** Install via `curl | bash`; Python ≥ 3.12 required. No third-party agent SDK dependency listed in the README — claims stdlib-adjacent posture for the runtime core. Claim to inspect.
- **Double Diamond decomposition in Execute phase:** Discover → Define → Design → Deliver. Vendor-borrowed design-thinking framework applied as execution scaffolding. Whether this produces substantively different output from a flat code-gen prompt chain is a testable question not yet answered by independent evaluation.

## Why clawfit should care

**Scoring dimension: pre-flight ambiguity resolution.** ouroboros introduces a pre-generation spec gate that is absent from every current clawfit registry entry. If the ambiguity threshold claim holds under independent testing, it represents a new evaluation axis: *does the agent defer execution until the task is sufficiently specified?* This matters most for profiles where task expansion risk is high (e.g., `task: research`, open-ended `task: code-gen` with complex domain requirements). The current scoring model has no weight for this property; if the pattern proves durable (a second tool adopting pre-flight ambiguity quantification would confirm it), a `spec_clarification_before_exec` axis would sharpen recommendations for those profiles.

**L3 SSOT sub-type expansion.** The 2026-05-03 scan noted acai.sh as a candidate *requirement-tagged SSOT* sub-type at L3 (deferred, single signal). ouroboros is a second, independent L3-adjacent signal but with a different shape: acai.sh tags *requirements in generated artifacts*; ouroboros *generates the spec* from structured questioning *before* any artifact is produced. They solve the same root problem (non-deterministic scope in agentic coding) from opposite ends of the timeline. Two signals in three days does not yet promote a new sub-type, but the pairing is meaningful: the SSOT gap at L3 is now visible from both directions.

**Ralph as event-sourced harness state** also reinforces the 2026-04-30 Mendral scan note on "durable execution" as a named harness property — Mendral via Inngest step-checkpoints; ouroboros via SQLAlchemy event journal. Two independent implementations of harness-level durability within two weeks suggest "resilient execution state" is solidifying as an L2/L3 evaluation criterion.

## Preliminary interpretation

Current best reading:

- **Primary: Level 2 — Meta wrappers / harnesses / orchestration layers.** ouroboros is a full execution runtime that wraps multiple base agents (Claude Code, Codex CLI, OpenCode, Hermes), orchestrates a multi-phase loop with named state transitions, and provides persistent recovery via event sourcing. The "Agent OS" self-description fits the harness-orchestration role, not the base-runtime role. It does not replace the underlying coding agent; it governs it.
- **Secondary: Level 3 — Team harness / executable SSOT / governance layer.** The Interview→Seed phase generates an immutable specification before execution; that spec functions as an executable SSOT — a contractual artifact that downstream phases (Execute, Evaluate) are bound to. The ontology convergence criterion and per-generation evaluation create a governance loop that is closer to L3 methodology guides (gsd, obra/superpowers) than to pure harness plumbing.
- **Notable sub-positioning.** ouroboros does not fit cleanly into any existing L2 sub-type. It is not a minimal harness (contra Pu.sh, mini-swe-agent), not a batteries-included SDK (contra deepagents), and not a sprint-contract/context-reset pattern (contra Anthropic harness patterns, Hashline). The closest analog is gsd/get-shit-done (L3 SSOT, prose spec-driven, 52k★) — but ouroboros adds quantified gates and loop termination criteria that gsd lacks. A provisional label: **spec-generative harness** — a harness that derives its SSOT from in-session elicitation rather than receiving it as a precondition.

## Status

- Single signal. Not yet in registry. Watching velocity over the next two scan cycles (target: 5k★ or v1.0 tag) before evaluating for L2 registry entry. The PAL Router cost-escalation behavior and ambiguity threshold claims both require independent reproduction before the spec-generative harness sub-type can be named in `docs/reference-levels.md`. Flag: if acai.sh or a third tool adopts quantified pre-flight ambiguity scoring, promote the pattern immediately.
