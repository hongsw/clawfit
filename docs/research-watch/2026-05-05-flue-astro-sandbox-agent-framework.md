# Research Watch: withastro/flue — Sandbox Agent Framework

- Repo: https://github.com/withastro/flue
- Also see: https://flueframework.com/ | https://github.com/SuperagenticAI/pyflue (community Python port)

## Why this is worth watching

Flue is the Astro team applying their "compile once, deploy anywhere" web framework philosophy directly to agent runtimes — resulting in a TypeScript build system that compiles agent directories into deployable server artifacts targeting Node.js, Cloudflare Workers, and CI/CD pipelines with no runtime changes. The +290 stars/day velocity on 2026-05-05 places it among the fastest-growing agent harness entries tracked this quarter. The explicit positioning as "not another AI SDK" but a production build-and-deploy layer for agents is a structurally novel claim in the Level 2 space.

## What stands out immediately

- **Agent-as-directory model**: agents are filesystem directories compiled into standalone server artifacts via `flue build`; the `dist/` output is fully self-contained and target-aware
- **Tiered sandbox model**: virtual sandbox (default, just-bash + in-memory FS) → container sandbox (Daytona, full Linux) → local sandbox (host FS mount for CI). The virtual tier is the differentiator — explicitly pitched as "dramatically faster and cheaper" than full container launches for high-traffic agents
- **Connector model via markdown**: connectors (sandbox providers, third-party integrations) are not npm packages; they are markdown installation instructions piped through an existing coding agent (`flue add daytona | claude`), which writes a small TypeScript adapter into `.flue/connectors/`. This is a claim-to-inspect: the pattern is architecturally interesting but the real-world DX has not been validated here
- **Multi-target deployment parity**: same agent source deploys to Node.js (dev server on port 3583 "FLUE" on keypad), Cloudflare Workers + Durable Objects, and GitHub/GitLab CI — target is a build flag, not a runtime concern
- **Session architecture with child task depth limit**: sessions spawn child sessions up to depth 4; automatic context compaction at token thresholds; exclusive-operation locking per session prevents concurrency bugs; event stream (SSE) for progress observation
- **Role-based prompt overlays**: roles are call-scoped system prompt injections, not persisted in history — avoids system prompt contamination across turns
- **Markdown-first skills**: `AGENTS.md` convention for skill definitions, consistent with the broader AGENTS.md ecosystem standard visible across multiple 2026-04 signals
- **Provider abstraction**: model/provider settings are runtime-scoped (not global), preventing state mutation across multi-agent runs
- **Positioned against rentable agents**: explicitly targets teams who want to own their agent infrastructure rather than subscribe to Dosu, Greptile, or CodeRabbit — ownership/customizability framing
- **Python port exists**: `SuperagenticAI/pyflue` is an independent community Python port; validates multi-language interest but is not officially maintained by the Astro team
- **License**: Apache-2.0; requires `ANTHROPIC_API_KEY` (Anthropic-native by default, though provider abstraction layer is present)

## Why clawfit should care

Flue is a direct entry in the Level 2 harness space with a differentiating axis clawfit does not currently score well: **sandbox tier selection**. The virtual-vs-container decision maps cleanly onto clawfit's `latency` and `budget` dimensions — virtual sandbox favors `latency: low` + `budget: *` profiles; container sandbox (Daytona) favors `task: code-gen` with heavy environment requirements. The build-artifact model also introduces a `statefulness` consideration: `session` statefulness is natively supported via Durable Objects on Cloudflare and in-memory on Node.js; `stateless` is the CI one-shot mode (`flue run`).

The Astro team's provenance matters for clawfit's registry: this is not an indie weekend project but a web framework team with demonstrated discipline around build systems, deployment targets, and DX design. The connector-via-markdown pattern, if it validates, represents a novel approach to capability extension that sits between the Level 4 skill-pack pattern (installable plugins) and Level 2 harness configuration — worth a cross-reference at L4a once more data is available.

The Cloudflare Workers native target makes this relevant to the `2026-04-17-cloudflare-agent-infrastructure-triple` signal: Flue is a harness that can run on top of Cloudflare's agent infrastructure stack (Workers + Durable Objects + AI Platform), not a competing product.

## Preliminary interpretation

Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layer** (build-system-first harness sub-type; compile-and-deploy orientation distinguishes from runtime-only harnesses)
- Secondary: **Level 4a** — skill/connector model warrants a secondary tag if the connector-via-markdown pattern validates at scale; hold for now
- Notable subcategory: **sandbox-tier-aware harness** — first tracked entry that formalizes virtual-vs-container sandbox selection as a first-class build-time concern rather than a deployment afterthought

## Status

- High signal: 2,392 stars, +290/day, Astro team provenance, TypeScript GitHub Trending #4 on 2026-05-05; add to Level 2 registry candidates; re-evaluate sandbox tier model against clawfit scoring dimensions within 2 weeks
