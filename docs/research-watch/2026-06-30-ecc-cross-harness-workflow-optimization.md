# Research Watch: ECC — Cross-Harness Workflow Optimization System

- Repo: https://github.com/affaan-m/ECC
- Also see: https://github.com/SuperClaude-Org/SuperClaude_Framework (comparable single-harness L2); https://github.com/affaan-m/everything-claude-code (same author, L3 taxonomy); https://github.com/msitarzewski/agency-agents (comparable L4b skill pack at scale)

## Why this is worth watching

ECC is the largest untracked signal in clawfit at 211k+ stars, surpassing opencode (157k) and sitting just below obra/superpowers (169k) in the L3 band — yet it belongs to a structurally distinct category from either. Its defining property is not being a harness for one tool but treating multiple harnesses (Claude Code, Cursor, Codex, OpenCode, Gemini, Copilot) as peers with platform-native configurations for each, which is a pattern that has no stable named slot in the current taxonomy. The v2.0.0 milestone and active Rust control-plane prototype suggest this is not a static resource but an evolving system with institutional momentum.

## What stands out immediately

From repo and README inspection:

- **Cross-harness parity as the explicit design center.** ECC ships platform-native artifacts for each supported harness rather than exporting a lowest-common-denominator format. Claude Code gets 67 agents + 271 skills + 92 command shims; Cursor gets a DRY adapter with 15 hook events reusing Claude Code scripts; Codex gets an AGENTS.md supplement with 32 skills in native format + 6 MCP servers; OpenCode gets 11 hook events + 35 commands + 13 instruction files. This per-harness depth distinguishes ECC from cross-tool portability tools (agency-agents, CLI-Anything) which generate from a single Markdown SSOT to a lowest-common format.
- **Named component taxonomy: Skills / Agents / Hooks / Rules / Memory / Security.** Skills (271) are the primary workflow surface. Agents (67) are specialized subagents for delegated tasks. Hooks (~15 event types) handle pre/post-execution automation. Rules (34 sets, language-aware) are always-follow behavioral constraints. Memory is a session-lifecycle closed loop (SessionStart loads prior summaries + learned instincts; Stop-phase extracts patterns; `/evolve` generates new skills). AgentShield is a separate npm package with 1,282 tests and 102 rules covering secret patterns, permission misconfigurations, hook injection risks, and MCP server risk profiling.
- **Closed-loop learning as first-class architecture.** The "Continuous Learning v2" system extracts instincts with confidence scoring across sessions, clusters related insights, surfaces contradictions for manual review, and feeds into `/evolve` for skill generation. This is not session memory in the claude-mem / Engram sense; it is a feedback loop that mutates the skill layer over time. No other L2/L3 entry in the taxonomy has documented this pattern at this depth.
- **AgentShield red-team pipeline.** The `--opus` flag runs three Claude 3.5 Opus agents in a red-team / blue-team / auditor pipeline for adversarial reasoning. This is supply-chain-hardening applied to agent configuration — a concern not present in any existing L2 or L4b tracked entry.
- **"Research-first development" as workflow positioning, not formal methodology.** The claim is anchored in the `/search-first` skill and documentation-lookup via Context7 MCP. It means "gather evidence before writing code" and is a product positioning statement, not an independently measurable criterion. Treat as claim to inspect, not validated methodology.
- **ECC 2.0 Rust control-plane prototype in-tree.** The `ecc2/` directory contains an active Rust rewrite of the control plane. This signals intent to move beyond YAML/Markdown orchestration toward a compiled execution layer — potentially repositioning ECC from a configuration system toward a runtime substrate. Architecture trajectory, not current state.
- **Star count anomaly requires scrutiny.** 211k+ stars with 32.5k forks and 230 contributors is an extraordinary figure for a harness-configuration repo. The same author's `everything-claude-code` sits at 168k in the L3 canonical section. Star velocity and organic vs. coordinated acquisition should be independently verified before treating this as an ecosystem consensus signal equivalent to opencode's 157k or obra/superpowers's 169k.

## Why clawfit should care

Two structural implications and one classification question.

First, ECC operates at a layer the taxonomy does not currently name: it sits above individual harnesses (L2) and coordinates behavior across them, but it does not govern a single team's workflow via executable SSOT (L3). The user's taxonomy description — "L2 Cross-Harness Workflow" — is accurate but points to a gap in the current L2 section. The existing L2 entries (oh-my-claudecode, SuperClaude, multica, etc.) are each harness-specific or harness-agnostic in the thin sense of "works with multiple runtimes." ECC's per-harness native artifact approach is a distinct structural pattern: it maintains harness fidelity rather than abstracting it away. This is a candidate L2 sub-type: "cross-harness native coordinator."

Second, the Skills / Agents / Hooks / Rules / Memory / Security component taxonomy maps partially to multiple clawfit layers simultaneously: Skills and Agents are L2/L3 surface; Memory is L4a/L5; Security (AgentShield) is L4c-adjacent. ECC bundles these under a single install identity. This multi-layer bundling is not unprecedented (obra/superpowers spans L3 + L4b; DureClaw spans L2 + L3 + L4c) but ECC's bundling is wider in scope and more intentionally integrated. clawfit's current scoring model treats these as distinct dimensions; a tool that deliberately bundles them raises the question of whether a "platform score" or "integration penalty" is appropriate in recommendations.

Third, ECC has a direct relationship to the affaan-m author's `everything-claude-code` (168k, currently in the L3 canonical section). Both repos are from the same author and share star-count territory. Understanding whether ECC supersedes, complements, or overlaps with `everything-claude-code` is a prerequisite for any registry or map entry.

## Preliminary interpretation

Current best reading:

- **Level 2 — Meta wrappers / harnesses / orchestration layers** — primary classification. ECC's core function is transforming how individual coding agents operate by wrapping them in a cross-harness configuration layer. This fits the L2 definition ("sit on top of existing base agents and transform how they operate"). The per-harness native artifact approach makes it a candidate for a new L2 sub-type: "cross-harness native coordinator" — distinct from single-harness wrappers (oh-my-claudecode, SuperClaude) and from thin multi-runtime abstractions (multica's task-queue routing across 11 runtimes).

- **Level 3 — Team harness / executable SSOT / governance layer** — secondary, via the Rules layer (34 language-aware always-follow behavioral constraints) and the AgentShield supply-chain audit. These components function as executable governance artifacts — agents read the rules before acting, and AgentShield enforces configuration policy. However, ECC does not define a sprint lifecycle, approval chain, or team workflow SSOT in the way cc-sdd or cc-best-practice do. The L3 signal is present but subordinate to the L2 coordination function.

- **Level 4b — Skill packs** — tertiary, via the 271 skills. These are functionally a very large domain-spanning skill pack embedded within a cross-harness coordinator. They exceed any standalone L4b entry in scope but are not distributed independently.

- **Level 4a — Memory / persistent context** — weak tertiary, via the Continuous Learning v2 / instinct persistence system. The closed-loop session memory is architecturally closer to agentmemory or claude-mem than to a pure harness feature, but it is tightly coupled to ECC's install identity rather than offered as an independent module.

Notable sub-classification note: the cross-harness native coordinator pattern (per-harness native artifacts with maintained fidelity rather than lowest-common-denominator export) has no current named slot. This is structurally different from CLI-Anything's generative-synthesizer sub-type and from agency-agents's cross-tool-portable-SSOT sub-type. Single signal; sub-type naming deferred per single-signal rule.

## Distinguishing claims vs. validated facts

- **Validated by repo inspection:** 271 skills, 67 agents, ~15 hook event types, 34 rule sets, per-harness native configurations for Claude Code / Cursor / Codex / OpenCode, AgentShield npm package with stated 1,282 tests, v2.0.0 milestone, Rust control-plane prototype in `ecc2/`, MIT license, plugin install via `/plugin install ecc@ecc`, ECC Pro $19/seat/month commercial tier.
- **Claim to inspect:** 211k+ star count — organic acquisition vs. coordinated. The same author's `everything-claude-code` at 168k is already in the L3 canonical section; two repos from the same author in the 150k–220k range warrants independent verification of star provenance before treating either figure as an ecosystem signal equivalent to opencode or obra/superpowers.
- **Claim to inspect:** "Research-first development" — anchored to a single skill (`/search-first`) and Context7 integration. This is a workflow positioning claim, not a methodology with measurable properties.
- **Claim to inspect:** Continuous Learning v2 closed-loop instinct extraction — mechanism is described but no independent benchmark or user case study validates the claim that instincts materially improve subsequent sessions.
- **Not validated:** ECC 2.0 Rust control-plane — in-tree prototype only; no release, no independent benchmark.

## Archon L2 classification revisit

The user asks whether Archon's L2 classification needs revisiting in light of ECC. The answer is no — they occupy non-overlapping L2 sub-types. Archon is classified as a "harness-builder sub-type" (generates harness configuration artifacts from project specifications — meta-tool that outputs other harnesses). ECC is a "cross-harness native coordinator" candidate (maintains per-harness native artifacts for 8 coding tools simultaneously). Archon generates; ECC deploys and maintains. The L2 classification for Archon is stable and requires no revision. What ECC does highlight is that the "harness builder" and "cross-harness coordinator" sub-types are distinct niches at L2 — a distinction worth recording when the next calibration cycle formalizes L2 sub-types.

## Status

- New entry. Star count requires independent provenance verification before registry or map promotion. Hold pending: (1) verification that 211k stars are organically acquired, (2) clarification of relationship to `everything-claude-code` (same author, same star-count territory, already in L3 canonical section), (3) second independent signal for the "cross-harness native coordinator" sub-type candidate. If star count is verified as organic, this is the largest untracked L2 signal in the taxonomy and should be promoted to the L2 canonical section at the next scan cycle.
