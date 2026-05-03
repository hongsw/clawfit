# Research Watch: acai.sh — Specsmaxxing / ACID-Driven Spec-First Development

- Repo: https://github.com/acai-sh/acai (Apache 2.0, CLI also at `@acai.sh/cli` on npm)
- Also see: https://acai.sh / https://acai.sh/blog/specsmaxxing / https://news.ycombinator.com/item?id=47994012

## Why this is worth watching

acai.sh introduces ACIDs (Acceptance Criteria IDs) — stable, greppable requirement identifiers embedded in YAML `feature.yaml` specs, then referenced by agents in generated code and test comments to maintain bidirectional traceability. The HN post hit 158 points and 171 comments on or around 2026-05-02, which is above the threshold for a pattern with traction rather than a lone practitioner experiment. More substantively, it lands in a crowded-but-still-forming sector: at least six other spec-driven-dev tools reached HN front page in the 2025–2026 window (Plain, Specil, spec-kit, VSDD, Kiro), signalling that "spec as canonical truth for agents" is a genuine recurring pattern, not a one-off post.

## What stands out immediately

- **ACID tagging is the core differentiator.** Unlike prose prompts or free-form markdown, each requirement in a `feature.yaml` is assigned a stable numbered ID (e.g., `animated-terminal.FRAME.1-1`). Agents embed that tag in code comments and test assertions. The result is grep-navigable traceability from specification to implementation to test coverage — claim made in the blog; not independently validated.
- **Three-phase "reactive software factory" roadmap.** The author lays out: (1) Specsmaxxing — tight specs; (2) Testmaxxing — full QA automation + observability; (3) Reactive factory — agents autonomously react to test failures and alerts without human intervention. Phase 3 is aspirational, not demonstrated.
- **Dashboard at app.acai.sh tracks requirement state.** Requirement lifecycle: No status → Assigned → Completed → Accepted → Rejected. Collaborative commenting per requirement. Backend is Elixir/Phoenix/Postgres. Free tier offered.
- **Agent self-assignment via dashboard.** The dashboard exposes agent-readable JSON API so agents can query which requirements remain unimplemented and self-assign work. This is described, not shown in a working demo visible at time of research.
- **CLI installs teaching agent via `acai skill`.** Running `npx @acai.sh/cli skill` teaches the agent the ACID process — same pattern as SKILL.md-based skill injection seen in the obra/superpowers and Vercel skills ecosystems (L4b). Cross-layer shape: the CLI is L4b (skill/capability delivery) while the spec infrastructure it governs is L3 (SSOT).
- **YAML format draws HN skepticism.** Multiple commenters flagged YAML as a poor LLM-facing format and questioned material difference from Jira tickets. The Gherkin/Cucumber executable-spec tradition was raised as a prior art comparison. These are claims to inspect, not invalidations.
- **Stability trade-off acknowledged.** Author notes ACIDs rely on stable numbering — easy to append new requirements, but revision requires re-aligning code. This is a real governance cost for evolving specs, not just boilerplate caution.

## Why clawfit should care

acai.sh occupies the same territory as `gsd/get-shit-done` (spec-driven, L3, 52k★, tracked 2026-04-14) and `gitagent` (git-as-SSOT, L3 pattern). If ACID tagging produces measurably better agent traceability than prose-spec alternatives, it could become a named L3 sub-type: **"requirement-tagged SSOT"** — distinct from (a) workflow methodology guides (gsd, obra/superpowers), (b) behavioral spec files (CLAUDE.md, forrestchang/andrej-karpathy-skills), and (c) git-native agent definitions (gitagent). That sub-type distinction matters for clawfit's recommendation engine: a `governance_need: hard` profile with audit requirements would score differently against a requirement-tagged SSOT than against a prose methodology guide.

The reactive-factory end-state, if it stabilizes, also has scoring implications for `statefulness: session` vs. event-driven profiles — agents reacting to test failures without human intervention is the same shape as Claude Code Routines triggered by GitHub events (L2, tracked 2026-04-15), but operating from a spec layer rather than a webhook layer.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team harness / executable SSOT / governance layer** (primary). The `feature.yaml` + ACID mechanism is the spec-as-canonical-truth pattern that defines L3 in this taxonomy. The dashboard and requirement-state lifecycle reinforce governance character.
- **Level 4b — Skill/capability layer** (secondary). The `acai skill` CLI command injects the ACID process as an agent skill, using the same SKILL.md-style delivery mechanism as other L4b entries.

**Flag for reference-levels.md consideration:** If a second independent tool adopts stable-ID requirement tagging for agent traceability (not just prose spec-first workflow), promote **"requirement-tagged SSOT"** as a named L3 sub-type alongside methodology guides and behavioral spec files. Not enough evidence today — single-signal, HN traction only, no independent adoption confirmed.

## Status

- Tracking as single-signal L3 candidate; revisit if a second high-signal tool adopts the ACID/stable-ID requirement tagging pattern, or if acai.sh crosses 2k GitHub stars.
