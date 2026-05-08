# Research Watch: OpenSpec — Spec-Driven Development (SDD) Framework for AI Coding Assistants

- Repo: https://github.com/Fission-AI/OpenSpec
- Also see: https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md (artifact architecture), https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md (30-tool compatibility list), https://redreamality.com/garden/notes/openspec-guide/ (independent deep-dive), https://github.com/acai-sh/acai (L3 neighbor — ACID-tagged SSOT, tracked 2026-05-03), https://github.com/Q00/ouroboros (L2/L3 neighbor — spec-generative harness, tracked 2026-05-04)

## Why this is worth watching

OpenSpec is the highest-starred pure spec-layer framework in this taxonomy — 46.2k stars, 3.2k forks, 36 releases, 586 commits, v1.3.1 shipped 2026-04-21. Unlike acai.sh (L3, ACID-tagged, 2026-05-03) or ouroboros (L2/L3, spec-generative harness, 2026-05-04), OpenSpec does not try to run the agent loop; it inserts a structured artifact layer — `proposal.md`, `spec.md`, `design.md`, `tasks.md` — between human intent and code execution, and explicitly claims cross-tool portability across 30 AI coding assistants. The star velocity (+294 in a single GitHub Trending session) and the breadth of tool support together make this the strongest multi-tool spec-layer signal observed in this watch log to date.

## What stands out immediately

- **46.2k stars, MIT, TypeScript 98.9%.** Verified via GitHub fetch 2026-05-09. 36 releases; v1.3.1 released 2026-04-21. 228 open issues and 81 open PRs indicate active but not bottlenecked development. npm package at `@fission-ai/openspec` with global install; requires Node.js 20.19.0+.
- **Four-artifact change unit: proposal + spec + design + tasks.** Each proposed change produces a self-contained folder under `openspec/changes/[change-name]/` containing: `proposal.md` (why + scope), `spec.md` (delta requirements, ADDED/MODIFIED/REMOVED sections with RFC 2119 language — MUST/SHALL/SHOULD/MAY + Given/When/Then scenarios), `design.md` (technical rationale), `tasks.md` (hierarchical implementation checklist). Completed changes merge delta specs into `openspec/specs/` and archive to `openspec/changes/archive/`. This is a delta-not-full spec model — a distinguishing design choice relative to Modo's `.modo/specs/` (full replacement) and acai.sh's feature.yaml (accumulate-and-tag).
- **Seven documented slash commands.** `/opsx:propose`, `/opsx:apply`, `/opsx:archive`, `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:onboard`. The commands are injected per-tool via tool-specific config directories — OpenSpec configures itself into the host agent rather than the inverse. This is the same distribution shape as acai.sh's `acai skill` CLI: the framework installs its command interface into the host tool, not the other way around.
- **30 AI coding assistants supported.** Confirmed via `docs/supported-tools.md`: Claude Code, Cursor, Windsurf, Codex, Gemini CLI, GitHub Copilot, Amazon Q Developer, Cline, Continue, RooCode, Kiro, OpenCode, Kimi CLI, Qwen Code, Lingma, and 15 others. Breadth is a structural claim: the commands are installed into tool-specific config paths (e.g., `.claude/commands/` for Claude Code, `.cursor/rules/` for Cursor). The actual portability depends on each tool's slash-command execution model, which varies significantly — a claim worth verifying per tool.
- **Explicit comparison to Kiro and GitHub Spec Kit in the README.** OpenSpec frames itself as "lighter than Spec Kit (no rigid phase gates)" and "more flexible than Kiro (tool-agnostic)." This competitive positioning is notable: both Kiro and Spec Kit are either vendor-controlled or single-tool; OpenSpec is the neutral, multi-tool spec layer in the same SDD segment. Claim-to-inspect: whether tool-agnostic portability holds in practice for the full 30-tool list or degrades to a Claude Code + Cursor core.
- **"Brownfield-first" design emphasis.** The documentation explicitly states that "most software work modifies existing systems" and positions delta specs as the essential abstraction for that context. This is architecturally distinct from the proposal-and-generate pattern common in agentic scaffolding tools (ouroboros's Interview→Seed phases target green-field problem framing). Delta specs imply the spec layer is a diff-based contract on an existing artifact graph, not a generated starting state.
- **No agent loop, no harness plumbing.** OpenSpec does not orchestrate agent execution, manage state, or provide LLM routing. It produces artifact files that the host agent reads. The spec artifacts live in the repository — they are git-tracked, reviewable, and not runtime-only. This is a zero-runtime-dependency design.
- **Telemetry opt-out available.** Anonymous telemetry on command names and version is collected by default; opt-out via env vars. Minor governance note for enterprise adoption evaluation.

## Why clawfit should care

**Three spec-first signals in six days (acai.sh 2026-05-03, ouroboros 2026-05-04, OpenSpec 2026-05-09).** The pattern is no longer a single-signal curiosity. Three structurally distinct approaches to the same root problem — non-deterministic scope in agentic coding — have surfaced within a week, each with meaningful traction. This is the clearest cluster pattern in the watch log since the memory-layer consolidation signals (GBrain, Hippo, claude-mem) in April. The pattern warrants a named L3 sub-type consideration: **"pre-execution spec layer"** — distinct from methodology guides (gsd, obra/superpowers), behavioral spec files (CLAUDE.md), and requirement-tagged SSOT (acai.sh).

The three tools differ structurally in ways that matter for clawfit's recommendation engine:
- **acai.sh:** ACID tags embedded in generated code — the spec is a traceability scaffold for agent output.
- **ouroboros:** Spec is synthesized in-session via Socratic questioning with a quantified ambiguity gate — the spec is generated pre-flight from elicitation.
- **OpenSpec:** Spec is authored by humans before agent invocation, stored as delta artifacts, and consumed by 30 different host agents — the spec is a portable multi-tool contract.

These three are not substitutes. A profile with `governance_need: hard` + `task: code-gen` + `statefulness: session` might want acai.sh (traceable IDs in output) or ouroboros (pre-flight scope reduction) depending on whether the bottleneck is review-time traceability or runtime scope drift. OpenSpec fits best for a team already using multiple AI tools and wanting a shared spec artifact across them — a multi-tool governance signal that the current clawfit registry does not yet model.

**Scoring implication.** If the `tool_agnostic` property of spec layers is a meaningful differentiator (OpenSpec serves 30 tools; acai.sh and ouroboros are Claude Code-primary), clawfit may want a `multi_tool_portability` boolean in the governance or L3 scoring axis. OpenSpec is the first concrete reason to add it.

## Comparison to nearest neighbors

| Axis | OpenSpec | acai.sh | ouroboros |
|------|----------|---------|-----------|
| Stars | 46.2k | ~1k | 3.2k |
| Primary layer | L3 (SSOT) | L3 (SSOT) | L2 primary / L3 secondary |
| Spec source | Human-authored delta artifacts | YAML ACID-tagged requirements | AI-generated via Socratic elicitation |
| Spec format | Markdown files (proposal/spec/design/tasks) | feature.yaml with stable numeric IDs | Convergence-scored schema |
| Tool support | 30 AI coding assistants | Claude Code primary | Claude Code, Codex, OpenCode, Hermes |
| Runtime dependency | None (artifact-only) | Dashboard (app.acai.sh) + agent skill | Python runtime + event-sourced persistent runner |
| Brownfield / greenfield | Explicit brownfield-first (delta model) | Greenfield-capable | Greenfield-focused (Interview phase) |
| Quantified gates | None | None | Ambiguity ≤ 0.2 before execution |
| Closest prior art | Modo (L1 IDE with `.modo/specs/`) | Gherkin/Cucumber (HN comparison) | gsd/get-shit-done (L3, prose spec-driven) |

## Preliminary interpretation

Current best reading:

- **Level 3 — Team harness / executable SSOT / governance layer (primary).** OpenSpec's `openspec/specs/` directory is a canonical source of truth for current system behavior, maintained across changes via delta-and-merge. The artifacts (proposal, spec, design, tasks) are the spec layer — they are what governs what the agent builds. The 30-tool support means this governance layer is explicitly designed to span agent runtimes, which is the core L3 value proposition. The lack of a runtime harness, agent loop, or LLM routing component cleanly excludes L2 classification.
- **Level 4b — Capability / skill / plugin layer (secondary, weak).** The slash-command injection mechanism (tools install per-tool command files) uses the same distribution shape as L4b skill packs. The `/opsx:*` commands are delivered as tool-local skills. However, the commands are governance workflow steps (propose, apply, verify, archive), not capability extensions (search, compute, memory) — so the primary classification is L3 even though the delivery mechanism resembles L4b.
- **Not L2:** OpenSpec has no runtime. It does not orchestrate agent execution. It produces and maintains artifact files that agents read. Governance layer without orchestration layer.
- **Not L1:** Not a standalone agent or IDE runtime.

OpenSpec occupies a distinct cell in the L3 space: **human-authored, delta-based, multi-tool portable spec SSOT** — separate from acai.sh's machine-readable ACID tagging and ouroboros's AI-generated convergence specs. If a fourth tool in this space emerges before the next scan cycle, the sub-type should be named in `docs/reference-levels.md`.

## Status

- Strong multi-tool signal; classify L3 primary. At 46.2k stars MIT-licensed, this substantially exceeds the 5k registry threshold and is a registry candidate for the L3 cluster — sub-type "pre-execution spec layer (human-authored, delta-based, multi-tool portable)." Three concurrent spec-first signals (acai.sh, ouroboros, OpenSpec) now visible in a 6-day window; flag for `docs/reference-levels.md` consideration if a fourth independent adoption of the pre-execution spec layer pattern is confirmed. No `docs/reference-levels.md` mutation today per protocol; sub-type naming requires the fourth-signal confirmation. Defer registry promotion pending: (1) independent verification that tool portability holds for tools beyond the Claude Code + Cursor core, (2) any user-facing adoption data (downloads, community posts) beyond star count.
