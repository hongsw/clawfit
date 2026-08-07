# Research Watch: wshobson/agents — Multi-Harness Plugin Marketplace

- Repo: https://github.com/wshobson/agents (⭐38,600)
- Source: GitHub Trending Python (2026-08-07), 57 daily stars
- Related: mattpocock/skills (2026-04-26), addyosmani/agent-skills (2026-04-08), google/skills (2026-06-09), obra/superpowers (2026-04-11)

## Why this is worth watching

Most skills/plugin repositories in the corpus target one harness (Claude Code, Cursor, Gemini CLI) and require manual porting to others. wshobson/agents takes a different approach: a single Markdown source generates native artifacts for five harnesses simultaneously — Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, and GitHub Copilot. The claim is not lowest-common-denominator portability but explicit harness-native output: each adapter emits the artifacts that each harness expects natively, including harness-specific constraints (Codex CLI's 8KB skill cap is respected; OpenCode's `permission:` block is populated; Gemini CLI gets TOML format native skills).

At 38.6k stars and 94 plugins covering 203 agents, 175 skills, 109 commands, and 16 orchestrators, this is the highest-star cross-harness plugin marketplace in the corpus. The `plugin-eval` quality framework (static + LLM-judge + Monte Carlo scoring) is also notable: most plugin repos lack systematic quality assessment.

## What stands out immediately

- **Single-source-of-truth, five harness outputs:** `plugins/` directory is the truth; `make generate-all` emits harness-native trees for Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, Copilot — explicit decision to not use a lowest-common-denominator format
- **Tiered model strategy explicitly encoded:** Fable 5 for longest-horizon autonomous work; Opus for architecture/security/code review; Sonnet for docs/testing; Haiku for fast operational tasks — model assignment is a structured decision in the plugin metadata, not left to user preference
- **`plugin-eval` three-tier quality framework:** static structural checks (<2 s), LLM-judge semantic evaluation (~30 s via Haiku + Sonnet), Monte Carlo statistical reliability (50–100 simulated runs, 2–5 min) — quality gates before plugins ship
- **94 plugins, domain-complete coverage:** architecture, languages, infrastructure, security, data, ML, docs, business, SEO, LLM fine-tuning (`llm-finetuning`, added July 14), DGX Spark operations (`dgx-spark-ops`) — the fine-tuning and GPU infrastructure plugins are unusual additions for a coding-agent skills repo
- **Orchestrators as first-class entity:** 16 multi-agent coordination workflows for full-stack, security, ML pipeline, and incident response scenarios — not just single-agent skills but multi-agent workflow templates
- **Pensyve external memory integration:** `git-subdir` dependency on Pensyve (major7apps/pensyve) for cross-session agent memory — the marketplace bundles an external memory layer by default

## Why clawfit should care

This repository is direct evidence for a pattern now confirmed across multiple signals in the corpus: **harness-agnostic skills as an emerging standard**. mattpocock/skills, addyosmani/agent-skills, obra/superpowers, google/skills — these all target skills for specific harnesses or a narrow set. wshobson/agents is the first to formally maintain multi-harness output adapters as a first-class build system concern.

The tiered model strategy (Fable 5 → Opus → Sonnet → Haiku, explicitly assigned per task type) is also a registry-relevant signal: it demonstrates that production plugin authors are already reasoning about model cost/capability trade-offs at the skill level, which clawfit currently models only at the recommendation level. A `recommended_model_tier` field in the registry schema would capture this emerging pattern.

The orchestrators category adds a meaningful new concern: L3-level multi-agent coordination workflows bundled alongside individual L4 skills. This conflation of L3 and L4 in a single package is consistent with the collapser pattern observed elsewhere in the corpus.

## Preliminary interpretation

- **Level 4 — Capabilities / Skills / MCP** (primary): skills, agents, commands, plugins — the capability layer for agent harnesses
- **Level 3 secondary** (orchestrators): 16 multi-agent coordination workflows that encode team-level task decomposition — these operate at the governance layer, not just the capability layer
- **Cross-watch:** mattpocock/skills (2026-04-26), addyosmani/agent-skills (2026-04-08), obra/superpowers (2026-04-11), google/skills (2026-06-09) — same layer, different harness scope; wshobson/agents is the first confirmed cross-harness adapter system at this scale

## Claims to verify

- **"Single-source generates native artifacts":** verify that Codex CLI output respects the 8KB skill cap and that Gemini CLI TOML output is accepted by the actual Gemini CLI parser — "native" claims are testable and worth verifying against current harness specs
- **Monte Carlo `plugin-eval` methodology:** verify what the 50–100 simulated runs actually sample and whether the statistical reliability metric captures real-world failure modes, or whether it is mostly prompt-coverage variance testing
- **38.6k stars with 530 commits:** star count is high relative to commit volume — check whether stars reflect an organic discovery event or a coordinated promotion; last commit was July 18, 2026 (no commits in the last 3 weeks)
- **Multi-harness drift:** with six harnesses and active harness spec changes (Gemini CLI, Codex CLI, OpenCode all shipped major updates in Q2–Q3 2026), verify how quickly the adapter layer stays current when upstream harnesses change their schema

## Status

- Last commit July 18, 2026; no versioned releases; active issue/PR backlog
- 38.6k stars well above research-watch and registry thresholds; deterministic cost/latency data not applicable (it is a plugin collection, not a deployable agent)
- Registry eligibility: registry schema maps to agents/LLMs/hardware, not plugin collections — no direct registry entry warranted; consider schema note for `cross_harness_portable: bool`
- Schema watch: `cross_harness_portable: bool`; `recommended_model_tier: [fable5 | opus | sonnet | haiku]`; `orchestrator_included: bool`
- Cross-reference: mattpocock/skills (2026-04-26), addyosmani/agent-skills (2026-04-08), obra/superpowers (2026-04-11), google/skills (2026-06-09)
