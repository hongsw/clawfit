# Research Watch: OpenMythos — Looped Transformer Architecture Reconstruction

- Repo/Link: https://github.com/kyegomez/OpenMythos
- Source: GeekNews front page

## Why this is worth watching
OpenMythos is a first-principles PyTorch reconstruction of the suspected Claude Mythos architecture — a Recurrent-Depth Transformer (looped transformer) with Mixture-of-Experts routing. It represents the developer community's attempt to reverse-engineer the capability tier that Anthropic has acknowledged sits above Claude Opus. The architecture's defining characteristic — adjustable reasoning depth at inference time via loop count — is a new axis for LLM capability selection that clawfit's current model doesn't capture.

## What stands out immediately
- Looped transformer: same weights recycled N times per forward pass instead of stacking unique layers
- Sparse MoE: router chooses different expert subsets at each loop iteration — each pass computes different functions
- Handles multi-step math, long-horizon planning, and layered arguments without explicit chain-of-thought
- Amazon Bedrock now offers Claude Mythos Preview (gated research preview) as of April 2026
- Not a model leak — a theoretical reconstruction based on public architecture research

## Why clawfit should care
- Mythos introduces a compute-time reasoning depth dial that Opus/Sonnet/Haiku don't have — affects LLM tier scoring beyond latency/cost
- If Mythos becomes accessible (e.g., via API or open weights), clawfit's LLM registry needs a new capability tier above "opus"
- OpenMythos signals that the developer community is treating Mythos as a new capability paradigm, not just a model update
- For `large_exec_research` or `governance_need: hard` profiles where reasoning depth matters, this tier shift is relevant

## Preliminary interpretation
Current best reading:
- **Level 5 — Research / evaluation / benchmark** (architecture research and capability tier signal, not a production runtime)
- If Mythos becomes production-accessible, this elevates to Level 1 LLM registry addition

## Status
- Tracking: architecture signal, not yet production
- Monitor: Anthropic Mythos API availability, open-weight release timeline
