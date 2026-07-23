# Research Watch: onecli/onecli — Credential Gateway for AI Agent API Access

- Repo: https://github.com/onecli/onecli (⭐2,571)
- Source: Hacker News (Show HN, 2026-07-23)

## Why this is worth watching
OneCLI is an open-source credential gateway that interposes between an AI agent and the external services it calls. Instead of exposing raw API keys to agents, service credentials are stored in OneCLI's built-in vault; agents receive scoped access tokens issued per-call that can be audited, rate-limited, and revoked without rotating the underlying service credentials. The core security claim: an agent that is compromised, confused, or behaving unexpectedly cannot exfiltrate or misuse the API keys for services it has access to, because it never holds them.

At 2,571 stars — below the 5,000-star threshold for strong consideration — OneCLI does not yet have the adoption weight of tools like Traceforce (YC-backed, tracked 2026-07-17) or ReasonGate (tracked 2026-07-17). However, 42 releases in 4.5 months (created 2026-03-08, v1.42.0 released today) signals an active development cycle and iterative feedback from real users. The pattern it addresses — credential isolation for agent tool use — has no dedicated solution in the prior scan corpus. Prior security signals (Traceforce: runtime behavioral monitoring; ReasonGate: prompt injection defense) operated at different layers; OneCLI targets the credential exposure surface specifically.

## What stands out immediately
- **Vault-native credential storage:** API keys never leave the vault; agents receive scoped tokens issued per-call by the gateway, not the underlying credentials
- **"Unified first-match policy engine" (v1.42.0):** the most recent release replaces a complex precedence model with a first-match rule evaluation — policy migration runs automatically, reducing misconfiguration risk on upgrade
- **TypeScript primary:** consistent with a lightweight proxy/gateway deployment model; low overhead, no native binary dependency required
- **"Give your AI agents access to services without exposing keys":** the description is tightly scoped — credential isolation for agent tool use, not a general API gateway or monitoring platform
- **42 releases in 4.5 months:** a release every 3 days on average signals an active product development phase; v1.42.0 includes a policy engine rewrite, not a patch
- **HN Show HN (22 pts, 12 comments):** modest but non-trivial reception; comments indicate developer evaluation of the security model

## Why clawfit should care
Current agent recommendations treat `network: online` as a binary property: either the agent can reach the internet or it cannot. No current registry field captures whether the agent's outbound tool-use API calls are mediated through a credential gateway or exposed directly to the agent context. OneCLI introduces a credential-mediation layer that is structurally independent of which agent harness or LLM is in use — it sits at the tool-call boundary and is substitutable per-service.

For `governance_need: hard` profiles specifically: an enterprise deploying Claude Code (or any L1 agent) against production services wants audit trails and revocation capability for the agent's API access. The current recommendation path for `governance_need: hard` surfaces policy engines (ReasonGate, Traceforce), but none specifically address the credential exposure vector. OneCLI fills that slot.

Schema gap: `credential_mediation: [direct | vaulted | gateway]` as a field in recommendation output would let clawfit surface OneCLI as a companion recommendation for any profile with `network: online` + `governance_need: hard`, regardless of the specific agent runtime.

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / Observability / Evaluation** (security monitoring sub-type: credential access auditing and isolation — distinct from Traceforce's runtime behavioral monitoring and ReasonGate's pre-inference injection defense)
- **Level 4c** has a secondary claim: OneCLI acts as action infrastructure middleware at the tool-call layer between agent and external API

## Claims to verify
- Vault architecture: is the vault a local encrypted store, a hosted SaaS, or operator-choice? (affects `network: offline` vs. `network: online` applicability — a hosted vault defeats local-only deployment)
- Scoped token model: do issued tokens carry per-service scope restrictions, per-agent scope restrictions, or time bounds? (determines what governance guarantees are actually enforceable)
- Agent runtime compatibility: which runtimes (Claude Code, Codex, Cursor, OpenCode) have tested integrations vs. "should work if it speaks HTTP"?
- Audit log output: does the policy engine produce human-readable audit logs, or only enforcement events? (determines whether it satisfies `audit_trail: full` vs. `audit_trail: partial`)

## Status
- First signal; 2,571 stars (below 5,000 threshold; above 100-star minimum); active development confirmed by 42-release cadence
- No registry entry: below star threshold; `tools_registry.json` lacks a credential-mediation category; no deterministic cost/latency data
- Schema gaps: `credential_mediation: [direct | vaulted | gateway]`; `token_scoping: [none | per-service | per-agent | time-bound]`; `audit_trail: [none | partial | full | encrypted-only]` (re-confirmed as needed; previously flagged in Codex sub-agent signal 2026-07-16)
- Monitor for: star growth to 5,000+; published integration guides for major agent runtimes; independent security audit of vault implementation; second independent "agent credential gateway" tool to confirm this as an L5 sub-type
