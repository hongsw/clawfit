# Research Watch: Cognition SWE-2 — Multi-Trillion-Parameter RL Closes the Gap on Fable 5.1

- Repo/Link: https://cognition.com/blog/swe-2
- Source: Hacker News (128 pts, 64 comments)

## Why this is worth watching
Cognition's SWE-2 is a post-trained derivative of Kimi K3 (2.8T parameters) that lands within one point of Fable 5.1 on FrontierCode 1.1 Main while pricing 64% cheaper. The methodological claim — scaling RL to the multi-trillion-parameter regime "for the first time" with a length-weighted reward baseline — is meaningful if it replicates, because it suggests the compute regime for RL post-training just expanded by an order of magnitude. Whether the benchmark results hold under independent evaluation is unconfirmed.

## What stands out immediately
- 92.8% on Terminal-Bench 2.1; 50.0% on FrontierCode 1.1 Main (within 1 pt of Fable 5.1); 73.0% on DeepSWE 1.1; 27.3% on Terminal-Bench 4 (a new, apparently harder benchmark variant)
- "Scaled RL to the multi-trillion-parameter regime for the first time" — specific architecture and training recipe claimed; not independently verified
- Length-weighted reward baseline credited for training stability at this scale
- Pareto-informed cost penalties derived from first principles — attempts to train the full cost-performance frontier in a single run rather than multiple separate runs per cost tier
- Low-precision inference: NVFP4/FP8 kernels with quantization-aware training to maintain accuracy
- Online draft-model training during inference for improved decoding throughput
- "Focused exploration" and "enhanced verification discipline" noted as behavioral improvements — vague without specific metrics
- Deployed as Devin Desktop, CLI, Web, and Fusion — not open-weight; Cognition proprietary

## Why clawfit should care
SWE-2 is relevant at two levels. First, as an L1 signal: if the FrontierCode 1.1 Main result is replicated independently, SWE-2 joins the set of Fable 5.1 competitors at a meaningfully different price point ($X vs. $Y per million tokens — Cognition has not published list pricing yet). This would directly shift the `task: code-gen, budget: medium` recommendation landscape. Second, the Terminal-Bench 4 mention (27.3%) is a flag — this benchmark presumably exists and SWE-2's performance there is noticeably lower than on Terminal-Bench 2.1. If Terminal-Bench 4 is a stricter successor, the 92.8% on 2.1 may overstate real-world senior coding task performance.

The "Pareto-informed cost penalties in a single training run" claim, if reproducible, also changes how the L1 market segments: instead of frontier labs producing one model per cost tier, a single training run could populate an entire cost-performance curve.

## Preliminary interpretation
- **Level 1 — Base Model** (primary: LLM post-training producing a new coding-focused agent model substrate)
- Cognition's harness (Devin ecosystem) is L2 secondary, but SWE-2 itself is evaluated and deployed primarily as a model artifact

## Claims to verify
- "Multi-trillion-parameter regime for the first time in RL" — who else has done multi-trillion RL training? This needs citation or denial from other labs
- FrontierCode 1.1 Main 50.0% — who maintains this benchmark? What is the leaderboard methodology? Same caveats as SWE-Bench Pro Verified apply (see separate doc today)
- Terminal-Bench 4 — what changed between 2.1 and 4? The 92.8% → 27.3% drop is dramatic and unexplained in the blog post
- Devin pricing — Cognition has not published SWE-2 API list pricing; "64% cheaper than Fable 5.1" is a relative claim without an absolute anchor
- NVFP4 inference quality — quantization-aware training at NVFP4 precision is aggressive; accuracy degradation vs. BF16 baseline not reported

## Status
- Signal strength: medium-high — HN 128 pts, significant benchmark claim, but entirely self-reported
- Registry eligibility: blocked — no public API pricing published; Devin is subscription-based, not per-token; no GitHub repo
- Next: watch for independent FrontierCode 1.1 Main and Terminal-Bench 2.1/4 replications; watch for API pricing announcement
