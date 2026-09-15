# Research Watch: Salesforce AgentScript — Compiled DSL for Deterministic Agent Orchestration

- Repo: https://github.com/salesforce/agentscript (⭐267)
- Also see: https://www.salesforce.com/agentforce/
- Stars: 267 | License: Apache 2.0
- Source: Dreamforce 2026 (Sept 11, 2026); GitHub first confirmed 2026-09-15

## Why this is worth watching

AgentScript is the first tracked signal in this log that separates the **specification of agent control flow** from both the LLM prompt and the runtime execution environment. Every prior tracked harness (Claude Code, KiroCrew, Archon, Rowboat) defines agent behavior through prompts, YAML, or Python — all of which are interpreted at runtime. AgentScript compiles a declarative block-based spec to an internal execution format, which means control flow decisions (step ordering, branching conditions, verification gates) become compile-time artifacts rather than emergent LLM behavior. Whether this separation delivers on its determinism claim in practice is not yet independently verified, but the architectural intent is structurally distinct from anything else in this log.

Agentforce's Dreamforce 2026 announcement positions seven named job-specific agents as production-ready offerings, with Hunter introducing multi-week autonomous execution with memory retention. Two signals for "multi-week persistent agent execution" have arrived in four days (KiroCrew, 2026-09-14; Hunter via Agentforce, 2026-09-15) — this pattern is worth watching as a possible emerging canonical.

## What stands out immediately

- **Compile-time control flow enforcement**: AgentScript enforces step ordering and branching conditions through compilation, not through prompt instructions or runtime policy. The stated problem it solves: "you can't tell an LLM 'always do step A before step B, and only proceed to step C if the customer is verified' through prompt instructions alone." The compiled artifact — not the LLM — is the authority on sequencing.
- **Open toolchain, closed runtime**: The parser, linter, compiler, LSP implementation, VS Code extension, and UI playground are all Apache 2.0. The execution runtime that runs compiled AgentScript on Salesforce infrastructure is not open-sourced. This means the spec is inspectable but execution semantics are proprietary — auditing what a compiled script actually does at runtime requires trust in Salesforce's closed executor.
- **"Agentforce dialect" extends the base spec**: The general AgentScript language is claimed to be runtime-agnostic, with Agentforce-specific blocks as a named extension. Whether the base spec is independently executable on non-Salesforce infrastructure is unconfirmed; no reference runtime implementation appears to exist in the repo.
- **Seven named job-specific agents at GA**: Casey (sales), Paige (service), Carter (commerce), Hunter (sales/pipeline), Marshall (HR/IT), Piper (supply chain), Fin (field service). These are Salesforce-packaged instantiations of the Agentforce platform, not AgentScript directly — the distinction matters for what is actually open.
- **Hunter: multi-day/week autonomous execution with durable memory**: Hunter is described as using a "long-horizon runtime" that pursues business goals across multiple days or weeks, with memory retention between sessions and "dynamic steering." This is an explicit claim of persistent, non-session-scoped autonomous agent operation from a major enterprise vendor — the first such claim from this tier in this log.
- **Multi-Agent Orchestration now GA**: Multiple Agentforce agents can coordinate. The announcement describes this as GA (generally available as of September 14, 2026), not preview. No description of the inter-agent protocol (whether it uses MCP, a Salesforce-proprietary bus, or the AgentScript language itself to express coordination).
- **LSP and VS Code extension in the toolchain**: The presence of a Language Server Protocol implementation suggests Salesforce intends AgentScript to be authored in developer IDEs as part of normal engineering workflow — not just configured through a low-code builder. This is a signal that the target audience includes engineers who need version control and code review over agent definitions.

## Why clawfit should care

**Taxonomy gap — compiled orchestration DSL**: No current registry entry or tracked signal involves a compiled specification language for agent behavior. The closest analogues are YAML-based workflow definitions (GitHub Actions, Temporal), but those operate on deterministic tasks. AgentScript targets LLM-driven agent steps, which are non-deterministic by nature. If the compile-time control flow claim is validated, this represents a fundamentally different approach to the L3 governance problem than policy enforcement (Microsoft Agent Governance Toolkit) or runtime constraint (QM multiplayer postures): determinism is achieved at authoring time rather than execution time.

**Schema gap — `execution_model: compiled_dsl`**: The current registry schema has no field for whether an agent's control flow is defined by prompt, by runtime policy, or by a compiled spec. If AgentScript's approach proves reliable, this distinction will matter for governance-heavy profiles where the question is not "does the agent have a policy?" but "is the execution order structurally guaranteed?"

**Hunter and the `statefulness: persistent` gap**: Hunter's multi-week autonomous execution is the second signal in four days for persistent agent execution that survives session boundaries (KiroCrew being the first). The current statefulness filter only models `session` and `stateless`. The difference from KiroCrew is architectural: KiroCrew is an open-source daemon; Hunter is a closed Salesforce cloud service. The user cannot audit or modify Hunter's persistence model. For governance profiles, the distinction between "persistent via open daemon I control" and "persistent via proprietary cloud service" is significant.

**Enterprise deployment realism**: The job-specific agent packaging (7 named agents with pre-built templates) compresses deployment friction. If clawfit's `task` dimension eventually needs to model "business function agents" (not just `code-gen`, `qa`, `research`), the Agentforce agent roster is an early data point for what functional decomposition looks like at scale.

## Preliminary interpretation

Current best reading:
- **Level 3 — Team Workflow / Executable SSOT / Governance** (primary): AgentScript's core value proposition is authored, compiled, version-controlled governance over agent step sequencing — the definition of L3. It is not a base runtime (L1) and it is not a harness wrapping another tool (L2); it is the specification layer that tells the runtime what is and is not permitted in execution order.
- **Level 2 — Harness / Orchestration** (secondary): The Agentforce platform as a whole — the runtime that executes compiled AgentScript, coordinates the named agents, and surfaces the multi-agent orchestration layer — is an L2 harness. Agentforce (L2, closed) runs compiled AgentScript (L3, open spec). The two are separable in taxonomy even though Salesforce ships them together.

The "Agentforce dialect" framing reinforces this split: the general language is L3 (governance/SSOT); the Salesforce-specific extension blocks are L2 runtime bindings.

Hunter (long-horizon, multi-week) has a secondary L5 (memory/context) characteristic due to its stated inter-session memory retention — but this is a property of the proprietary runtime, not of AgentScript itself.

## Claims to verify

- **Compile-time determinism in practice**: Does the compiled output actually prevent the LLM from deviating from the specified step order, or does AgentScript enforce ordering at the calling-convention level while still allowing the LLM to produce unpredictable outputs within each step? The distinction between "deterministic control flow" and "deterministic agent behavior" is not made explicit in available materials.
- **Base spec executability outside Salesforce**: Is there a reference runtime for plain (non-Agentforce-dialect) AgentScript, or is the compiler only usable if you have Salesforce credentials? If the runtime is always proprietary, "runtime-agnostic language spec" is a claim, not a fact.
- **Hunter's human-in-the-loop provisions**: Multi-week autonomous operation with spend authority and external communications implies some escalation or approval mechanism. No details on human-override points, spend caps, or rollback provisions appear in available materials.
- **Multi-Agent Orchestration protocol**: "GA" for multi-agent coordination does not specify the inter-agent communication mechanism. If Agentforce agents communicate through Salesforce-proprietary channels only, the orchestration layer has no interoperability surface with non-Salesforce agents.
- **267 stars provenance**: The repo has 267 stars as of 2026-09-15, four days after Dreamforce 2026. Is this organic developer interest, Salesforce employee stars, or a post-announcement spike that will plateau? The star count should be re-checked in 2-4 weeks to assess organic momentum.
- **"Agentforce dialect" documentation**: Is the Agentforce-specific extension documented in the open repo, or only in Salesforce's proprietary developer docs? If the latter, the claim that AgentScript is a general language with an enterprise extension cannot be independently verified.

## Status

- First tracking: 2026-09-15
- Stars: 267 (above 100-star minimum; below 5,000 registry threshold; qualifies under official framework module exception as the open-source toolchain for Salesforce's enterprise agent platform)
- Registry: Not eligible at this time — execution runtime is proprietary, no per-call pricing data available, no independent runtime for non-Salesforce deployments
- Flag: Two "multi-week persistent agent execution" signals in four days (KiroCrew 2026-09-14, Hunter/Agentforce 2026-09-15). A third would trigger consideration for `statefulness: persistent` as a canonical schema value.
- Watch: Does a reference runtime for base AgentScript emerge? Does the Agentforce dialect spec get published in the open repo? Does Hunter document its human-in-the-loop and containment model?
- Related signals: KiroCrew daemon persistent workspace (2026-09-14), QM multiplayer governance postures (2026-08-01), Pion autonomous business operator (2026-09-14), tech-leads-club agent-skills (2026-09-14)
