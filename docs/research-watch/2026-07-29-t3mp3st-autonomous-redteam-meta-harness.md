# Research Watch: T3MP3ST — Autonomous Red-Team Meta-Harness for Offensive Security Testing

- Repo: https://github.com/elder-plinius/T3MP3ST (⭐3,900+)
- Source: Trending in July 2026 security tooling; GitHub Trending; multiple security research references

## Why this is worth watching

T3MP3ST is an autonomous red-team platform that wraps whatever coding agent the user already has running (Claude Code, Codex, Hermes Agent) and orchestrates the full kill chain — recon → exploit → report — via a web War Room interface or CLI. It requires no new API keys and no cloud: the existing agent is the reasoning engine; T3MP3ST provides the multi-agent coordination, offensive toolchain, and structured output layer around it.

This is a structurally important signal: it is an L2 meta-harness that wraps an existing L1/L2 agent to specialize it for a specific professional domain (offensive security). The pattern — "domain-specific meta-harness bolted around a general coding agent" — has been observed in research (agent-chief), creative (OpenMontage), and trading (vibe-trading) domains. T3MP3ST is the first clear signal for this pattern in offensive security.

3,900+ stars for a security tool with public benchmarks and 90.1% pass@1 on XBEN is a strong signal that the practitioner security community has independently validated the concept.

## What stands out immediately

- **No new API keys required:** the resident coding agent (Claude Code, Codex, Hermes) is the brain; T3MP3ST is the orchestration wrapper. Lowers barrier to adoption significantly.
- **90.1% pass@1 on XBEN:** XBOW's 104-challenge offensive security benchmark. 8/10 real CVEs from 2026 pinned to exact file, line, and CWE with a single agent; full pack surfaced all 10.
- **Verifiable claims:** `npm run verify-claims` recomputes all benchmark numbers from committed artifacts — reproducible-by-default design philosophy.
- **Full kill-chain orchestration:** recon, exploit development, report generation as a structured multi-agent workflow, not a single-pass agent invocation.
- **Web War Room interface:** dedicated management UI for running and monitoring the multi-agent offensive workflow — an L6 layer built specifically for the security domain.
- **Meta-harness architecture:** sits above the coding agent layer, not replacing it. This means T3MP3ST benefits from every improvement to the underlying agent without requiring its own model updates.
- **Keyless and open-source:** disclosed as Apache 2.0 or similar; no vendor lock-in.

## Why clawfit should care

clawfit currently has no `domain: security` or `task: pen-test` categorisation. T3MP3ST surfaces a gap: the taxonomy treats all tasks as roughly equivalent coding/research workloads. Offensive security has distinct requirements — tool isolation, legal authorization scope, CVE databases, structured vulnerability reporting — that differ from general code-gen or QA.

More importantly, T3MP3ST validates the "domain meta-harness" pattern at scale. clawfit currently models harnesses as a single L2 bucket. The data now suggests a sub-category worth distinguishing: `harness_type: domain-specialized` versus `harness_type: general-purpose`. This would affect routing: a security practitioner asking for a QA recommendation should see different candidates than someone building a general automation workflow.

Also: T3MP3ST explicitly lists its compatible base runtimes (Claude Code, Codex, Hermes Agent). This is one of the first tools to publish an explicit compatibility matrix against other tracked L2 tools — a structural pattern clawfit may want to represent as a `wraps: [list of compatible base runtimes]` field.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness/Wrapper layer** (primary): orchestrates and specializes an existing coding agent
- **Level 6 secondary:** provides a War Room UI on top of the agent workflow
- Sub-type: `domain-specialized` harness (security), not a general-purpose coding harness

Cross-watch: OpenMontage (L2, agentic video production), vibe-trading (L2, agentic trading), agency-agents (L2, persona-specialized). Same pattern, different domain.

## Claims to verify

- Whether XBEN (XBOW's benchmark) is independently maintained or self-referential; a benchmark maintained by the same team that created the winning system needs external validation
- Whether the 90.1% pass@1 figure holds against CVEs disclosed after T3MP3ST's training data cutoff (contamination risk)
- Legal scope: "authorized testing" is stated as the use case, but the tool's kill chain operates identically on unauthorized targets; enforcement is entirely procedural, not technical
- Whether the compatible agent list (Claude Code, Codex, Hermes) has been tested or is aspirational documentation

## Status

- 3,900+ stars, launched July 2026. Above registry threshold for star count, but no deterministic cost/latency data exists for the security task dimension — depends entirely on the underlying agent cost. Registry addition deferred.
- Open question: should clawfit add a `task: pen-test` or `task: security-audit` dimension? This would require at least one more security-focused harness (second signal) before adding to the taxonomy.
- Pattern flag: the "domain meta-harness" sub-type now has strong signal across creative, financial, and security domains. Three signals may be sufficient for a sub-type entry in reference-levels.md.
