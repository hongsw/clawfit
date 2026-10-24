# Research Watch: Kimi K3.1 Pro — Moonshot AI Post-Training Update

- Repo/Link: https://www.kimi.ai/blog/kimi-k3-1-pro (⭐N/A — Moonshot AI product)
- Source: GeekNews / Hacker News (2026-10-24)

## Why this is worth watching
Kimi K3.1 Pro is a post-trained revision of Kimi K3 — same 3T-class MoE architecture, substantially more post-training compute. The headline change that matters to clawfit is not the benchmark improvements (those are self-reported) but the hallucination rate: K3's claim-level hallucination rate on Kimi Hallu Bench Hard fell from 23.4% to 8.3%. For clawfit recommendation profiles where factual reliability matters (task: `qa`, `research`), this is the largest single-version reliability improvement any tracked model has published. Open weights are scheduled for November 4, 2026.

## What stands out immediately
- **Hallucination reduction**: claim-level error rate 23.4% → 8.3% on Kimi Hallu Bench Hard (Kimi internal benchmark; not independently verified)
- **Coding improvement**: Kimi Code Bench 3.0 Long-horizon 55.95% (K3) → 61.2% (K3.1 Pro); direct benchmark, but internal
- **Finance reasoning**: OfficeQA Pro v2 at 64.4%; Financial Research up 11.6 points vs K3; Business Operation 4.2× K3
- **1M token context window**: inherited from K3; no regression on this dimension
- **3D and design additions**: BenchCAD with tools at 92.7%; Kimi 3D Make released alongside
- **Cybersecurity**: cyber training data removed; xdev-bench-hard jumps to 81.0% from K3's 33.3% — the post claims it "remains behind frontier proprietary models" while publishing a number higher than most
- **Variants**: K3.1 Pro and K3.1 Pro Highspeed (2–3× speed); no Instant Mode equivalent (same high-reasoning-cost constraint as K3)
- **Open weights**: promised November 4, 2026; API is live now (`kimi-k3.1-pro`, `kimi-k3.1-pro-highspeed`)
- **Pricing**: not published in the release post; K3 was $3/$15 (input/output); assume at or above that tier until confirmed

## Why clawfit should care
K3 was tracked in July 2026 (`2026-07-18-kimi-k3-moonshot-open-weights-benchmark.md`). The key conclusions from that doc were: (1) K3 cannot satisfy `latency: low` due to forced max-reasoning mode; (2) K3's pricing removed it from `budget` profiles below ~$0.015/task; (3) open weights were pending. K3.1 does not change (1) or (2) — Highspeed variant may relax latency but pricing is unconfirmed.

What changes: if the 8.3% hallucination rate survives independent verification, K3.1 Pro becomes a serious candidate for `task: qa` and `task: research` at medium/high latency profiles, where factual reliability is weighted more heavily than cost. It does not qualify for `latency: low` until a confirmed fast/instant mode emerges.

Registry action: **defer** until (a) open weights are confirmed November 4, (b) pricing is published, and (c) hallucination rate is independently verified. Do not add based on self-reported benchmarks alone.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM** (primary): updated foundation model for agent backends
- clawfit category: `llms.json` candidate (same as K3), pending pricing and weight confirmation

## Claims to verify
- Hallucination rate (8.3%) is from Kimi's own internal benchmark — no external replication available at time of writing
- Highspeed variant's actual latency: "2–3× faster" is relative to K3.1 Pro, not to a concrete tokens/second number
- Whether open weights ship on November 4, 2026 as stated
- Pricing for K3.1 Pro vs. K3 ($3/$15) — the post does not mention pricing
- Whether the cyber capability claim (81.0% on xdev-bench-hard) is comparable to previously tracked models

## Status
- Tracking: new release signal, Moonshot AI Blog / HN / GeekNews 2026-10-24
- Registry eligibility: deferred — check back November 4, 2026 for weight release and pricing confirmation
