# Research Watch: BasedHardware/omi

- Repo/Link: https://github.com/BasedHardware/omi
- Source: GitHub Trending

## Why this is worth watching
Omi describes itself as "AI that sees your screen, listens to your conversations and tells you what to do" — a persistent ambient AI layer that continuously observes screen content and audio, then proactively surfaces suggestions or takes actions. At 9,824★ it is the first high-signal entry in this taxonomy for *passive* multimodal input (screen-watching + always-on microphone) as distinct from push-to-talk or on-demand voice tools.

## What stands out immediately
- Dart (Flutter) primary language — targets mobile and cross-platform from the start
- Persistent screen + audio observation without a push-to-talk trigger
- "Tells you what to do" framing implies proactive rather than reactive agent behavior
- Distinct from Ghost Pepper (hold-to-talk, offline STT) and Superwhisper (explicit dictation)
- Distinct from Claude Computer Use (agent takes action) — omi advises the human who acts
- Closes the gap between ambient wearable AI (like Humane AI Pin) and desktop agent tooling

## Why clawfit should care
Omi occupies a new position in Level 7: passive ambient input, not active invocation. Current Level 7 entries assume the human initiates each interaction (push-to-talk, type, invoke). Omi inverts this — the AI monitors continuously and speaks up. For exec and PM personas who don't want to manage an agent session, this "advisor in the room" model is distinct enough to warrant a separate sub-type. It also raises the question of whether clawfit should add a `passive_monitoring` capability dimension to the org_fit model.

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface layer (ambient / passive multimodal input sub-type)**

New sub-type: passive ambient AI vs. active-invocation voice tools.

## Status
- Medium-high signal — add to registry; revisit at 15k★ for reference-levels update
