# Research Watch: Buzz — Agent-Identity Collaborative Workspace

- Repo: https://github.com/block/buzz
- Also see: https://buzz.xyz / TechCrunch: "Jack Dorsey is taking on Slack with Buzz" (2026-07-22)

## Why this is worth watching
Buzz is Block's open-source team workspace (chat + Git hosting + workflow automation) built on the Nostr identity protocol, where AI agents receive cryptographic keypair identities and participate as full workspace members using the same primitives as humans — not bot integrations, not plugin slots. The agent-first identity model, backed by Block's organizational credibility and Apache 2.0 licensing, is a structurally distinct bet that team collaboration should treat agents as co-equal principals from the substrate up. At 213 HN points on launch day, developer awareness is confirmed.

## What stands out immediately
- **Nostr keypair per principal**: every human and agent gets an Ed25519 keypair identity; agents additionally carry a second cryptographic signature binding them to a human owner — accountability is encoded at the protocol layer, not in application-level policy
- **No separate bot API**: agents search discussions, submit patches, review code, and trigger workflows via the same interfaces humans use — no secondary integration surface to maintain or break
- **Model-agnostic claim**: Dorsey's stated design intent; the specific LLM abstraction mechanism is unverified at v0.4.21
- **Apache 2.0, self-hostable**: open-source with buzz.xyz managed hosting also available; genuine self-sovereign deployment path exists
- **Git hosting bundled inside the identity space**: code patches and discussion share one audit trail and one permission model — agent submissions and human reviews are unified, not bridged
- **Desktop apps for macOS, Windows, Linux at v0.4.21**; mobile and push notifications noted as unfinished in the repo

## Why clawfit should care
Buzz introduces a workspace-membership model for agents that clawfit has not encountered in prior signals. The Nostr owner-signature creates implicit agent governance (all agent actions traceable to a human principal) without a standalone policy engine. This is structurally relevant to the `statefulness: session` and `network: online` recommendation paths and raises a schema gap: clawfit has no field for agents operating as persistent workspace members vs. ephemeral single-task invocations. If workspace-native agent identity becomes an expected deployment pattern, the registry will need `deployment_model: [task-scoped | session | workspace-member]`.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta Wrapper / Harness** (primary: agents are runtime principals inside the workspace, not add-on bots — this is an agent surface claim more than a UI claim)
- **Level 6 — Human Interface** (secondary: team chat, Git UI, cross-platform desktop apps)
- L3 (governance) has a credible secondary claim via the Nostr owner-signature accountability model; revisit if the agent governance surface expands beyond identity binding

## Status
- First signal. v0.4.21, Apache 2.0, Block-backed. No registry entry: platform-layer product; no deterministic cost/latency data mappable to clawfit's agent/LLM/hardware triples. Monitor for: agent API spec, MCP server integration, pricing for hosted tier, and whether "model-agnostic" claim holds at the harness API level.
