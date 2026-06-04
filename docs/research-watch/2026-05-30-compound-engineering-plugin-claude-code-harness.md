# Research Watch: Compound Engineering Plugin — Cross-Platform Methodology Harness

- Repo/Link: https://github.com/EveryInc/compound-engineering-plugin
- Source: GitHub Trending Daily #3 (all languages, 2026-05-30), 353 stars today, 18,100 total stars

## Why this is worth watching

At 18,100 total stars with 353 earned today, this is the highest-star cross-platform engineering plugin observed to date — materially above ECC (182k★ but distribution-focused) and task-specific harnesses like claude-code-harness (1,800★). The "Compound Engineering" methodology (80% planning and review, 20% execution; each unit of work makes subsequent units easier) is an explicit opinionated workflow philosophy — not a skill pack and not a raw orchestration harness. Its cross-IDE reach (Claude Code, Codex, Cursor, Copilot, Factory Droid, Qwen Code, OpenCode, Pi, Gemini, Kiro) makes it one of the broadest single-distribution methodology artifacts in this taxonomy.

## What stands out immediately

- **37 skills and 51 agents in a structured named workflow:** The slash-command set (`/ce-strategy`, `/ce-brainstorm`, `/ce-plan`, `/ce-work`, `/ce-code-review`, `/ce-debug`, `/ce-compound`) forms a sequential engineering lifecycle — strategy grounds all downstream decisions; `/ce-compound` closes the loop by documenting learnings back into the project. This is cycle enforcement embedded in a skill pack, not advisory prose.
- **10+ supported runtimes at launch:** The broadest multi-IDE reach confirmed in the skill pack category so far. OpenCode, Pi, Gemini, and Kiro support is delivered via a converter — suggesting the canonical format is Claude Code / SKILL.md, with translation for other targets. The converter mechanism is a claim to inspect.
- **80/20 execution ratio as stated design intent:** The explicit framing "80% planning and review, 20% execution" is the same anti-drift motivation documented in `claude-code-harness` (Plan→Work→Review→Ship cycle) and `gsd` (GSD harness), but delivered as an installable skill pack rather than as a runtime-enforced governance layer. Enforcement here is behavioral (model reads instructions), not structural (Go guardrails, subprocess gating).
- **MIT license:** No governance blockers.
- **"Every Inc." provenance:** A company, not an independent community author. The official "plugin" framing signals commercial motivation; continuity risk is lower than solo-author repos but higher than Anthropic or Microsoft first-party entries.
- **51 agents:** The agent count is high relative to other skill packs; whether these are discrete sub-agents dispatched at runtime or slash-command aliases with distinct behavioral instructions is a claim to inspect.

## Why clawfit should care

Compound Engineering sits between the governance layer (L3 behavioral spec) and the skill pack layer (L4b) in a way that exposes a classification gap the taxonomy has seen before with ECC and obra/superpowers. The `/ce-compound` learning-loop command and `/ce-strategy` upstream grounding are L3 signals — they govern workflow philosophy and persist learnings back into the project. But the distribution mechanism is SKILL.md / slash-command installable, which is the canonical L4b form. The cross-IDE converter also echoes the L4b portability pattern confirmed as stable since 2026-05-22. Scoring implication: for `task: code-gen` profiles where the user has no existing harness and wants opinionated workflow discipline, Compound Engineering is structurally different from domain skill packs (it adds workflow governance, not domain knowledge) and from raw harnesses (it imposes no runtime gating). The current registry schema has no field that captures "provides opinionated workflow discipline via behavioral spec" as distinct from "provides domain capabilities."

## Preliminary interpretation

Current best reading:
- **Level 4b — Skill packs (primary):** Distribution is SKILL.md / slash-command installable; the atomic unit is a named slash command. This places it in the same distribution tier as taste-skill, dotnet/skills, and agency-agents.
- **Level 3 secondary (non-trivial):** `/ce-compound` (learnings documentation) and `/ce-strategy` (product grounding that flows downstream) are governance artifacts — they enforce workflow philosophy across sessions and accumulate project-level knowledge. This is the same L3 signal noted for ECC's 34 rule sets co-packaged inside an L4b distribution unit. Not enough to flip the primary classification, but too significant to ignore.

Not L2: Compound Engineering does not route between models, spawn sub-agents across runtimes, or manage parallel execution. The 51 agents are co-installed skills, not dispatched workers.

## Status

- 18,100★ — above the 5k registry threshold. Registry entry held pending: (1) verification that 51 agents are distinct behavioral units vs. slash-command aliases; (2) confirmation that the converter mechanism for non-Claude-Code targets (OpenCode, Pi, Gemini, Kiro) produces functionally equivalent behavior rather than degraded stubs; (3) clarification of the enforcement model — does `/ce-work` block if `/ce-plan` has not been completed, or is the cycle advisory? The answer determines whether the L3 secondary classification is strengthened or dropped.
- Flag for schema-analyst: "workflow methodology skill pack" is an L4b sub-type candidate distinct from domain skill packs, output-quality governance packs, and compression skills. Compound Engineering is the first high-star signal for this sub-type; promotion threshold requires a second independent installable methodology pack at ≥5k★.
