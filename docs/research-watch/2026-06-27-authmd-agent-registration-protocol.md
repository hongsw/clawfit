# Research Watch: auth.md — Open Protocol for Agent-Initiated User Registration

- Repo: https://workos.com/auth-md
- Also see: docs/research-watch/2026-06-25-google-labs-design-md-format-spec.md, docs/research-watch/2026-06-03-agents-need-rss-discovery-protocol.md, docs/research-watch/2026-05-06-cloudflare-agent-account-deploy-autonomy.md

## Why this is worth watching
auth.md lands at the intersection of two converging forces: the "dot-md convention" (robots.txt / .well-known / agent.md / design.md) reaching the authentication layer, and a concrete unsolved problem — agents currently have no standard path to register users for services without a human clicking through a form. WorkOS is the author but explicitly decouples the protocol from its own infrastructure, which is the right move for adoption. Whether that claim holds deserves inspection.

## What stands out immediately
- Protocol is a single Markdown file hosted at `https://yourdomain.com/auth.md` — intentionally mirrors robots.txt placement; any agent HTTP client can retrieve it without prior negotiation
- Two flows: **Agent Verified** (agent's identity provider attests to the user; fully non-interactive) and **User Claimed** (agent generates a code; user confirms at sign-in — minimal human step preserved)
- Output is a scoped OAuth access token: short-lived, revocable, user-tied; no new token format, composes existing OAuth infrastructure
- Claimed open standard: no WorkOS account required to publish or consume auth.md — claim to inspect; WorkOS still controls the spec URL and presumably the governance process
- No repo or formal RFC location surfaced yet — the authoritative document lives at a WorkOS marketing domain, which is a governance red flag for a would-be open protocol
- Conceptual lineage: robots.txt (crawl policy), .well-known/ (capability discovery), agent.md (agent behavior policy) — auth.md is the authentication slot in the same family

## Why clawfit should care
Agents in the registry that handle multi-service task profiles (research, QA pipelines, deployment automation) currently assume authentication is a solved prerequisite — the user holds credentials, the agent is handed a token. auth.md, if it achieves adoption, shifts that assumption: the agent can bootstrap its own access surface during a task run. This changes how clawfit should score agents on `statefulness: session` vs `statefulness: persistent` dimensions, and raises a new axis — whether an agent can self-register for services it needs at runtime. The dot-md convergence is now spanning L3 (design.md governance), L4 (auth tooling), and L5 (discovery protocols) simultaneously, which suggests a coherent agent-web interface layer is forming below clawfit's current taxonomy.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / MCP / context layer** — auth.md is a discovery and handshake artifact; it tells the agent what the service accepts before any action is taken, analogous to how MCP describes tool surfaces; the token output feeds agent context
- **Level 4 secondary (weak)** — the Agent Verified flow activates a capability (registration-as-action) that is tool-use adjacent, but the protocol itself is not a skill or plugin; it is a negotiation surface
- The dot-md convention pattern (design.md at L3, auth.md here at L5) may warrant a named sub-category in the reference map: "machine-readable site policy files" spanning multiple levels

## Status
- Early signal; spec governance unclear — no formal repo, no RFC, no versioning scheme visible; the open-standard claim requires verification against who controls the schema
- Watch trigger: independent implementation by a non-WorkOS service, or a community spec repo separate from the workos.com domain
- If the dot-md convergence (design.md + auth.md + agent.md) reaches three independent open-standard instances, a map-level notation for the pattern is warranted — flag for reference-levels.md consideration at that point
