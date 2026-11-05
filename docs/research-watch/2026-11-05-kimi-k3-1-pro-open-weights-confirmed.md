# Research Watch: Kimi K3.1 Pro — Open Weights Confirmed Released

- Repo/Link: https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- Source: Hacker News front page (2026-11-05)

## Why this is worth watching
The October 24 tracking doc (`2026-10-24-kimi-k3-1-pro-moonshot-post-training-update.md`) deferred registry action on three explicit conditions: open weights confirmed, pricing published, and hallucination rate independently verified. Condition (a) is now met: the HuggingFace model card for `moonshotai/Kimi-K3.1-Pro` is public. This unblocks the K3.1 Pro registry evaluation for `llms.json`.

## What stands out immediately
- Weights are on HuggingFace under Moonshot AI org: `moonshotai/Kimi-K3.1-Pro`
- Release is consistent with the November 4, 2026 commitment in the original blog post
- Pricing: still not confirmed publicly — K3's rate was $3/$15 per 1M input/output tokens
- Hallucination rate (8.3% on Kimi Hallu Bench Hard): remains self-reported; no external replication announced alongside the weight release
- The Highspeed variant open weights status is not confirmed in the HN post

## Why clawfit should care
With weights public, K3.1 Pro satisfies the same `network: offline` and `hardware: local` profiles that made K3 a local inference candidate. The latency constraint from K3 (forced max-reasoning mode → no `latency: low`) likely remains unless the architecture changes are detailed in the model card. The deferred registry action requires confirming: (1) model card licensing for commercial use, (2) a credible third-party hallucination benchmark result, and (3) pricing for the cloud API variant.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM** (open-weight frontier model candidate for agent backends)
- clawfit category: `llms.json` candidate — same as K3; now unblocked on the weights condition

## Claims to verify
- License on HuggingFace model card (Apache 2.0 or restrictive commercial license?)
- API pricing (K3 reference: $3/$15; K3.1 Pro may differ)
- Third-party hallucination benchmark replication (8.3% claim from Kimi internal only)
- Highspeed variant weights availability

## Status
- Tracking: follow-up signal; weights confirmed as of 2026-11-04 (HN front page 2026-11-05)
- Registry action: unblocked on weights condition; blocked on pricing and independent hallucination verification
