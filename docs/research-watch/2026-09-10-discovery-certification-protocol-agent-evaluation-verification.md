# Research Watch: Discovery Certification Protocol — Scores Alone Do Not Prove Agent Research Discovery

- Repo/Link: https://arxiv.org/abs/2609.09219
- Source: Hugging Face Daily Papers 2026-09-10 (15 upvotes)

## Why this is worth watching
The Discovery Certification Protocol (DCP) argues that a high benchmark score from an AI research agent does not constitute evidence of genuine discovery. The paper proposes a three-tier validation framework: executable recovery tests (can the claimed result be reproduced deterministically?), controlled audits (was the agent given unfair access to the target?), and finite-sample recovery bounds (with what statistical confidence does the finding hold?). This is a direct challenge to how research-agent outputs are currently accepted in the literature — and by extension, how tool vendors claim their agents perform scientific or analytical tasks.

## What stands out immediately
- Three-tier validation: executable recovery, controlled audit, deterministic verification — each addresses a different failure mode of agent evaluation
- "Finite-sample recovery bounds" — introduces statistical confidence quantification for agent-produced findings, not just binary pass/fail
- Targets AI research agents specifically (those used for scientific discovery, literature review, hypothesis generation) — not general coding benchmarks
- Published Sept 7, 2026; appearing in daily papers Sept 10; 15 HF upvotes — modest traction, as expected for a protocol/methodology paper
- No code or reference implementation mentioned in the abstract — primarily a theoretical/methodological contribution

## Why clawfit should care
Two separate signals today (DCP here + SWE-Bench Pro Verified, arxiv 2609.08149) both challenge the trustworthiness of agent evaluation outputs. The specific failure modes differ — DCP targets research/discovery tasks where "recovery" is the verification primitive; SWE-Bench Pro Verified targets coding benchmarks where reward hacking corrupts scores — but the underlying concern is the same: published numbers cannot be taken at face value.

For clawfit, this matters at three levels:
1. **Scoring inputs**: fit_score is calibrated against benchmark claims. If benchmark claims are systematically inflated (SWE-Bench Pro Verified) or unverifiable (DCP), the scoring model inherits those errors.
2. **Task taxonomy**: clawfit does not currently have a `task: research` category. DCP's focus on research agents implies there is a meaningful segment (research automation, literature review, hypothesis generation) that operates under different evaluation standards than code-gen or QA.
3. **Registry validation**: the phase 4 rule "deterministic cost/latency data is publicly available" has an analog in evaluation: "benchmark results are independently reproducible." DCP formalizes this as a protocol, which could inform future registry admission criteria for tool capability claims.

Second-signal note: this is the second evaluation-trustworthiness signal today alongside SWE-Bench Pro Verified (2609.08149), forming a same-day two-signal pattern. See reference-levels.md for the discovery log entry.

## Preliminary interpretation
- **Level 5 — Evaluation / Observability** (primary: a validation protocol that operates at the agent-output evaluation layer)
- **Level 3 — Research-Loop / Scientific Agents** (secondary: directly targets agents used for autonomous scientific discovery)

## Claims to verify
- Whether "executable recovery tests" requires the agent to reproduce its own finding deterministically or whether a separate auditor reproduces it — the distinction matters for practical adoption
- Statistical grounding of "finite-sample recovery bounds" — what distribution assumptions does this make? Is it applicable to black-box LLM outputs?
- Which existing research agents are evaluated in the paper? The abstract does not name them
- Whether any major research labs or benchmark maintainers have committed to adopting the DCP

## Status
- Signal strength: low-medium — 15 HF upvotes, but structurally significant as a methodology paper
- Registry eligibility: not applicable — protocol paper, not a deployable tool
- Pattern note: two-signal building pattern on "agent evaluation trustworthiness" confirmed today — DCP (research domain) + SWE-Bench Pro Verified (coding benchmark domain); different sub-types; see reference-levels.md
- Next: watch for adoption by benchmark maintainers; relevant if a major benchmark announces DCP compliance
