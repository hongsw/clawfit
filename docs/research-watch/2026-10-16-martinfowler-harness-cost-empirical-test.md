# Research Watch: Martin Fowler — Empirical Harness Cost Test with Frontier vs. Cost-Optimized Models

- Repo/Link: https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
- Source: GeekNews front page (6 pts); martinfowler.com

## Why this is worth watching
This is an empirical, controlled test of whether a behavioral harness (contract specs, request-response examples, API development skill, contract-driven mocks, test reports) adds value across two model tiers on a single concrete task. The methodology—10 paired runs per model, with and without harness, evaluated by an external 178-test acceptance suite—is more rigorous than the typical practitioner blog post. The key finding contradicts a simple "harnesses always help" or "frontier models don't need harnesses" narrative: harnesses make a cost-optimized model reliable, but add no quality benefit to a frontier model while multiplying token cost by 10x. The author's recommendation differs by model tier.

## What stands out immediately
- GPT-6 Sol (frontier): 10/10 acceptance rate both with and without harness; harness added no quality benefit but increased average token use from 1.1M to 11.3M and cost from ~$0.41 to ~$2.68 per accepted run
- GPT-6 Luna (cost-optimized): 3/10 without harness → 10/10 with harness; harnessed Luna at ~$0.27 per accepted run beats unharnessed Sol at ~$0.41 — the harness pays for itself and then some
- Luna's failures without harness were specification compliance issues: deferred 202 boundary handling, Kafka wire contract violations, wrong HTTP status codes — the harness provided machine-readable contracts the model could follow; without them, these constraints were lost mid-task
- The harness tool set (Specmatic-based: OpenAPI/AsyncAPI specs + contract mocks) is specific and measurable; the article avoids vague claims about "system prompts" or "memory"
- Task scope is limited: one greenfield backend service, one detailed brief, low reasoning effort setting — not a multi-service or multi-session test
- The "executable attention" framing (Naresh Jain's phrase) — harness as a mechanism to keep model attention on specification constraints across a long context — is a more precise conceptual claim than "scaffolding" or "guidance"
- Harness setup and maintenance costs were explicitly excluded from cost comparison; this is a known limitation the author acknowledges

## Why clawfit should care
This is the most rigorous empirical data point in the research-watch record for harness cost-vs-value tradeoffs. For clawfit's scoring model:

First, the result suggests a model-tier interaction: `harness_value` is not constant across `llm_quality`. A lower-capability LLM in a well-specified harness may outperform a frontier LLM without one, at lower cost. clawfit currently scores (agent, llm, hardware) triples but does not model harness configuration as a variable — this test suggests harness presence is a meaningful dimension for `fit_score`.

Second, the failure taxonomy is useful: specification compliance failures (wire contracts, HTTP semantics, error codes) are the category where harnesses help; these are schema-validation-type constraints that can be encoded in OpenAPI/AsyncAPI. Tasks with clear, machine-readable output contracts benefit most from harnesses; tasks with subjective or emergent output criteria benefit less.

Third, the cost arithmetic is clawfit-relevant: if an organization's primary consideration is cost, the right recommendation may not be the best LLM but the best (LLM + harness) pair — and the harness setup cost amortizes over many runs.

This is a second empirical signal for harness economics after the "Four Horsemen" failure patterns doc (2026-10-05), which addressed why agent projects fail from an architectural standpoint. The Fowler test gives a cost-side numerical calibration.

## Preliminary interpretation
Current best reading:
- **Level 2 primary — Harness/wrapper layer**: the test is about behavioral harnesses that wrap agent execution with specification constraints; the finding is about when L2 harness investment produces returns relative to raw L1/LLM capability
- **Level 3 secondary — Team workflow / SSOT generators**: the OpenAPI/AsyncAPI specs used as harness inputs are executable specification artifacts that act as a SSOT for both agent behavior and test validation

## Claims to verify
- 10 runs per condition is a small sample; the Luna 3/10 without-harness result has wide confidence intervals (could be as high as 6/10 or as low as 1/10 in a larger sample)
- Task representativeness: a single greenfield service with a detailed brief is not a typical enterprise coding agent task
- Low reasoning effort setting for Codex: results at higher reasoning effort may differ substantially, particularly for Luna
- GPT-6 Sol and GPT-6 Luna are not publicly documented model designations as of this writing; the test validity depends on these being consistent model versions
- Harness maintenance cost exclusion: in production, contract specs require ongoing maintenance; the per-run cost comparison is incomplete without amortizing setup and maintenance

## Status
- Discourse signal (martinfowler.com article; no GitHub repo for the test itself)
- Not a registry candidate
- 📡 note: second empirical harness economics signal (after Four Horsemen 2026-10-05); first controlled quantitative test of harness cost vs. quality across model tiers; the Luna 3/10→10/10 result is the specific claim to track as frontier model capabilities change — if cost-optimized models improve, the crossover point shifts
