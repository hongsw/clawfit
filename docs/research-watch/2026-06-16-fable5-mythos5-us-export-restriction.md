# Research Watch: Fable 5 / Mythos 5 — US Export Control Restriction Signal

- Repo/Link: https://cnbc.com (CNBC report, 2026-06-16)
- Source: GeekNews front page (18 pts, 28 comments) + GeekNews item (12 pts)

## Why this is worth watching
The US government directed Anthropic to disable Fable 5 and Mythos 5 globally under export control directives. This is the first confirmed instance of frontier AI model access being blocked at the API level by government order, rather than through voluntary geographic restrictions. GeekNews commentary describes sudden loss of customer access without warning. See prior signal: `2026-06-10-claude-fable-5-async-agent-model-tier.md`.

## What stands out immediately
- No advance notice to customers; access cut without warning
- Both consumer (Fable 5) and agentic (Mythos 5) tiers affected simultaneously
- US export control mechanism — not an Anthropic product decision
- GeekNews discussion references "the shadow this casts over the Fable situation" (12 pts, 8 comments)
- Sets a precedent: any frontier model can be disabled retroactively regardless of existing contracts

## Why clawfit should care
This directly affects the `network: online` reliability axis. A tool scored highly for an `online` profile that depends exclusively on cloud-frontier models (Claude Code on Mythos 5, or any harness routing to it) now carries an external-shutdown risk that the registry does not model. Two implications:
1. **Model-dependency risk** is now a real scoring axis — tools that hard-code a single frontier provider are more brittle than multi-provider routers (OpenRouter, aisuite, LiteLLM).
2. **Offline/local mode scoring** gains additional weight for `data_sensitivity: confidential` or `governance_need: hard` profiles where regulatory risk extends beyond data privacy to model-access continuity.

## Preliminary interpretation
Current best reading:
- **Not a tool** — regulatory ecosystem signal
- **Scoring implication**: `network: hybrid` tools (Goose, Aider, Continue with Ollama backend) gain relative score advantage for risk-sensitive profiles
- **LLM registry note**: Fable 5 / Mythos 5 entries should carry `availability_risk: high` if added to `llms.json`

## Status
- Ecosystem signal. No map mutation. No registry entry. Monitor: (a) whether access is restored, (b) whether other providers receive similar directives, (c) whether aisuite/LiteLLM routes away from affected endpoints automatically.
