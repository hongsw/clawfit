# Research Watch: Sierra Poppy (Personal Agent Protocol) — Open Standard for Personal Agents Accessing Businesses

- Repo/Link: https://sierra.ai/blog/poppy (spec draft; no GitHub repo confirmed at time of tracking)
- Source: Web search / industry coverage (announced Oct 6, 2026; Draft 0.1 published Oct 9, 2026; 35 design partners added)
- Stars: N/A (protocol specification, not a GitHub repo; qualifies under official-spec exception)

## Why this is worth watching
Sierra and Meta announced the Personal Agent Protocol (PAP), nicknamed Poppy, on October 6, 2026, as an open standard for how personal AI agents (OpenAI Dots, Anthropic's Claude, Meta AI) authenticate with and act on behalf of users at business websites and APIs. The protocol is built on OAuth, JWTs, HTTPS, OpenAPI, and MCP. Design partners include Shopify, Stripe, Visa, Walmart, OpenAI, Bank of America, Mastercard, Cloudflare, and Genesys (reported, not independently confirmed). Sierra's existing tracked entry (`2026-05-05-sierra-ai-enterprise-agent-950m.md`) covers the company's enterprise platform funding; this document tracks the protocol standard specifically.

## What stands out immediately
- Discovery via `.well-known/poppy.json`: businesses publish a file describing which scopes, authentication methods, and agent-accessible actions they support — analogous to `robots.txt` or `.well-known/openid-configuration` for agent-readable capability declarations
- OAuth as the trust foundation: access is scoped to what a user explicitly grants; businesses decide which personal agents can access which APIs
- MCP as the underlying call mechanism: Poppy sits above MCP, using it to carry API calls once authentication and scope negotiation are complete
- Cross-domain trust model: a user's personal agent (from any provider) can access a business's services without the business maintaining per-provider integrations — the protocol abstracts provider identity
- Governance is user-centric: users choose their personal agent and the scopes it holds; businesses specify which actions are grantable
- Draft 0.1: major technical and governance decisions are still open; this is not a stable spec
- Design-partner status ≠ production deployment: none of the named partners have confirmed live implementations

## Why clawfit should care
Poppy/PAP is the first tracked cross-vendor open protocol for the personal-agent-to-business access layer — structurally distinct from MCP (agent-to-tool) and from A2A (agent-to-agent). It addresses the connection surface at the boundary between L6 (personal agent interface where users delegate tasks) and L4 (the capability layer where tools and business APIs live). If Poppy stabilizes, it would affect clawfit's `network: online` and `statefulness: persistent` recommendation paths: a fully Poppy-compliant personal agent (OpenAI Dots, Claude, etc.) could replace many harness-level integration patterns with a standard business-access layer. The dependency on OAuth also means that existing enterprise OAuth infrastructure becomes an enablement layer for personal AI agents — a significant convergence signal.

## Preliminary interpretation
Current best reading:
- **Level 4 — Protocol/Capability Layer** (business-access authentication and scope negotiation above MCP)
- Secondary L6 (the protocol is designed for personal agents operating on behalf of human users at the L6 interface layer)
- Tertiary L2 (harness-level integration patterns may eventually be replaced by Poppy at the access-delegation layer)

## Claims to verify
- Whether named partners (OpenAI, Bank of America, Mastercard, Visa) are confirmed design partners or reporting artifacts from a single uncorroborated source
- Status of the reference implementation Sierra committed to publishing — this would be the first trackable GitHub artifact for Poppy
- Whether the MCP-as-call-mechanism claim is in the spec draft itself or only in secondary reporting
- Any fork or competing draft from non-Sierra parties (e.g., Mozilla, W3C participation — common for `.well-known`-based standards)

## Status
- First scan: 2026-11-16
- Registry action: none — this is a protocol specification, not an agent/LLM/hardware entry
- 📡 Note: First tracked cross-vendor open standard for personal-agent-to-business access; no second signal yet from independent org; monitor for reference implementation GitHub release, W3C/IETF standardization track, or a competing draft from a different vendor — any of these would constitute a second signal for "personal-agent business-access protocol" as a distinct L4 protocol sub-type
