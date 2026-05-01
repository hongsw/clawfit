# Research Watch: spawn-agent

- Repo/Link: https://github.com/millionco/spawn-agent
- Source: GeekNews front page

## Why this is worth watching
spawn-agent is an adapter that makes local coding agents (Claude Code, Codex CLI, etc.) behave as if they were Vercel AI SDK models — same API shape, same integration points. This means any developer already using the Vercel AI SDK can route calls to a local coding agent without changing their integration code. It is the inverse of `cc-switch` (which normalizes across CLI provider configs): spawn-agent normalizes across the SDK-vs-CLI divide.

## What stands out immediately
- Presents local coding agents as Vercel AI SDK model endpoints
- Zero-rebind for developers already in the Vercel AI SDK ecosystem
- Collapses the "SDK app vs. CLI agent" distinction at the integration boundary
- Small, focused scope — adapter pattern, not a full framework

## Why clawfit should care
spawn-agent extends the multi-vendor anti-lockin cluster noted 2026-04-28 (cc-switch, Sub2API, cmux, awesome-codex-skills). This entry adds the SDK-compatibility dimension: local agents are now first-class citizens of hosted AI SDK workflows. Relevant to `network: offline` + developer profiles who want to use familiar SDK abstractions without cloud routing. Level 4c adapter sub-type; complements GoModel (gateway) and cc-switch (CLI switcher) in the provider-portability cluster.

## Preliminary interpretation
Current best reading:
- **Level 4c — Tool-use extensions / adapter layer** — sits between SDK abstractions and CLI agent runtimes, normalizing the interface boundary

## Status
- Early signal; star count not reported. Tracking. Revisit when star count and feature scope are confirmed.
