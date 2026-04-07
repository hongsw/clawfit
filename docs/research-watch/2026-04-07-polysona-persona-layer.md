# Research Watch: Polysona

- Repo/Link: https://github.com/LilMGenius/polysona
- Source: hongsw GitHub stars

## Why this is worth watching
Polysona applies 10 psychology frameworks (MBTI, Enneagram, and Eastern reflection systems) to extract a structured personal persona from an interview session, then injects that persona into any AI agent runtime (Claude Code, Codex, OpenCode). At 71 stars it is early, but the approach — treating persona as a portable, structured artifact rather than a system prompt — is architecturally distinct from existing prompt-customization tools.

## What stands out immediately
- Three-component pipeline: Profiler (one-time interview) → Trendsetter (trend collection) → Content-Writer (persona + trend → draft)
- Output is `persona.md`, `nuance.md`, `accounts.md` — structured markdown files that travel with the user across agents
- Explicitly targets multiple sub-personas per person (executive, creator, gamer modes)
- HTML as primary language suggests a UI-heavy demo layer; actual agent logic appears to be prompt engineering
- Tags include `metacognition`, `psychiatry`, `philosophy` — signals an unusually theory-grounded design intent
- Contrast with gstack which targets org knowledge; Polysona targets individual cognitive style

## Why clawfit should care
Polysona is a nascent L4a/L4b hybrid: it generates persistent personal context (L4a memory) but delivers it as a skill pack / persona layer (L4b). clawfit does not currently have a `persona` category or a user-profile maturity dimension. If portable persona artifacts become common, the org_fit scoring model may need a `personalization` feature flag. Low star count (71) keeps signal strength low for now.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill pack / persona layer (metacognition-driven, portable across agent runtimes)**

## Status
- Tracking: early watch, low signal. 71 stars. Monitor for adoption in Claude Code community and whether persona portability becomes a standard pattern.
