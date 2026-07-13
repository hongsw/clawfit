# Research Watch: MCP Gateway & Registry — Enterprise Control Plane for MCP Ecosystems

- Repo: https://github.com/agentic-community/mcp-gateway-registry (⭐794)
- Source: Web search (new MCP tools July 2026), v1.26.0
- Also see: Manufact (L7, MCP cloud hosting, tracked 2026-07-02); mcpsnoop (L4c, MCP protocol debugger, tracked 2026-07-04); microsoft/agent-governance-toolkit (L5, policy enforcement middleware, tracked 2026-07-03)

## Why this is worth watching

The MCP ecosystem has been scaling in a structurally fragile way: each agent runtime or harness vendor maintains its own list of MCP servers, each developer machine carries its own credential set, and there is no shared inventory, no security gate before a server reaches agents, and no audit trail after. MCP Gateway Registry is the first open-source project this scan series has tracked that addresses that fragmentation at the infrastructure level rather than the individual-server level — it proposes a single authenticated control plane through which all MCP server access in an organization flows. The A2A reverse-proxy mode extends that governance posture to agent-to-agent traffic, which is a pattern not yet represented in any tracked tool. At 794 stars and Apache 2.0 with a 1.26.0 release on July 6, 2026, this is moving toward production readiness before a second well-known tool in this space has emerged.

## What stands out immediately

- **Control plane / data plane split is explicit and production-oriented**: nginx reverse proxy as data plane (TLS, auth validation, routing) plus FastAPI control plane (inventory, access policy, audit) mirrors how mature API gateways are built. This is not a thin YAML-configured proxy — it is a two-tier system with separate operational domains for throughput and governance.
- **A2A reverse-proxy mode is architecturally novel**: opt-in routing for agent-to-agent traffic through the gateway, with per-agent access control, is the first tracked implementation of a centralized A2A access gate. Prior tracked A2A signals (go-micro, routa, strands-agents) implement A2A as a direct peer protocol; this externalizes the trust boundary into a proxy. How stable this is in v1.26.0 is a claim to verify.
- **Semantic tool discovery at runtime — not static registration**: agents can use natural-language queries to discover available tools at call time. This is materially different from static MCP config files; it implies the gateway can route an agent to the right server without the agent knowing which specific server hosts a capability. Whether this performs reliably under load or in heterogeneous server inventories is unverified.
- **Fail-closed security scanning on admission**: newly registered MCP servers pass through a security scan; if the scan fails, the server is not admitted. The specific scanning mechanism (static analysis, CVE lookup, LLM semantic scan, or some combination) is not documented in the main README — this is a claim to inspect before treating it as a governance guarantee.
- **Per-user credential brokering via 3LO (three-legged OAuth)**: users authenticate once with GitHub/Slack/Atlassian accounts; the gateway vaults per-user tokens and injects them on egress. Tokens never reach developer laptops. This resolves a real security gap in the current MCP deployment pattern, where third-party SaaS tokens live in dotfiles. The vault implementation and secret-rotation behavior are unverified.
- **Federation with Anthropic MCP Registry and AWS Agent Registry**: the gateway can pull server listings from external registries, including Anthropic's own. This positions the tool as a meta-aggregator above the registries maintained by model vendors — a structurally significant claim if the federation is bidirectional or persistent rather than a one-time import.
- **Multi-cloud deployment parity**: Helm/EKS, Terraform/ECS, and Docker Compose are all documented deployment targets. This is unusual for a 794-star community project and suggests the deployment story has received engineering attention beyond a quick open-source launch.
- **v1.26.0 security hardening scope**: the July 6 release addressed SSRF and CSRF protections, MongoDB credential tightening, a weak-secret preflight that prevents startup without SECRET_KEY, serialized nginx config regeneration (fixes a race that could corrupt routing configs on concurrent MCP server registration), and CVE-2026-4438 (glibc) remediation. The breadth of this hardening release is consistent with a project approaching production use, not a prototype.

## Why clawfit should care

**Taxonomy placement is the first-order question.** MCP Gateway Registry is not a leaf MCP server exposing domain capabilities (that is L4c). It is infrastructure that governs access to L4c servers. The existing taxonomy does not have a named sub-type for this architectural role. The closest analogues are:

- Manufact (L7 primary): manages the *deployment lifecycle* of MCP servers (auto-deploy, PR previews, hosting). Manufact is a deployment platform; MCP Gateway Registry is a runtime access control plane. These are complementary, not competing.
- microsoft/agent-governance-toolkit (L5 primary): application middleware for policy enforcement between agent decisions and action execution. AGT targets agent workflow governance; MCP Gateway Registry targets the MCP transport layer between agents and servers.
- mcpsnoop (L4c, first signal for MCP protocol debugger): passive transparent proxy capturing MCP JSON-RPC traffic for debugging. MCP Gateway Registry is an active proxy that enforces access policy and transforms credentials — a different role than passive inspection.

MCP Gateway Registry does not fit cleanly into any current L4c sub-type (browser-vendor MCP, local OS MCP, visualization MCP, etc.) because it does not expose domain capabilities. It aggregates and governs access to servers that do. This is architecturally a **management plane for L4c** — a layer that does not exist as a named concept in the current taxonomy.

**Registry-level implication**: clawfit's current recommendation pipeline treats MCP server access as a direct agent-to-server binding (registered in `agents.json` or noted in scoring metadata). If an organization deploys a gateway like this, that model changes: agents connect to the gateway, which determines which servers they reach. The `statefulness` and `network` filter axes do not capture "MCP gateway mediated vs. direct MCP" as a deployment variant. If the gateway pattern gains a second independent signal, a `mcp_access: [direct, gateway-mediated]` field becomes relevant to the scoring model.

**The stateless MCP RC (tracked 2026-07-05) creates a specific interaction**: the 2026-07-28 RC removes `Mcp-Session-Id` and requires stateless any-request-to-any-server routing. The MCP Gateway Registry's nginx data plane is a natural fit for stateless MCP because load balancing across server instances becomes trivial when routing is session-independent. However, the gateway's per-user credential brokering introduces session-like state at the auth layer (token vaulting, egress injection) even if the MCP protocol layer becomes stateless. Whether the gateway's 3LO token model is compatible with the RC's stateless request semantics is a claim to verify.

## Preliminary interpretation

Current best reading:

- **Level 5 primary — MCP ecosystem management plane**: The gateway operates as governance infrastructure *for* the L4c layer rather than *as* a member of it. Its security scanning on admission, audit trail, OAuth2/OIDC enforcement, and semantic discovery are management-plane functions that parallel what microsoft/agent-governance-toolkit does for agent action policies — but applied to the MCP transport layer. L5 in the existing taxonomy covers management tools that operate on the MCP ecosystem (the MCP spec is tracked as L5), policy enforcement middleware (AGT at L5), and observability platforms (Spanlens at L5). The MCP Gateway Registry fits the same category of "infrastructure that manages an ecosystem layer" rather than "a component that participates in it."
- **Level 4c secondary — MCP intermediary**: the gateway sits inline in every agent-to-MCP-server call path, making it functionally part of the L4c capability delivery chain. Agent tool calls pass through it; it is therefore a structural member of L4c even if it does not itself expose domain capabilities.
- **Level 3 secondary weak**: fail-closed security scanning on admission, OAuth2/OIDC authorization scopes, and tamper-evident audit logging carry L3 governance characteristics (blocking-mode enforcement, not logging-only). Whether the admission scan is truly fail-closed or fail-open by configuration is a claim to verify; if fail-closed is confirmed, the L3 secondary strengthens.

**Is "MCP governance layer" a new emergent sub-type warranting a taxonomy note?** This is a first signal for the "MCP ecosystem control plane" pattern. A taxonomy note in `docs/reference-levels.md` is not warranted at single-signal stage (794★, no second independent MCP management-plane tool confirmed). However, the pattern is architecturally distinct enough from the existing L4c sub-types that if a second independent implementation surfaces, the two-signal rule would be met and a named sub-type entry ("MCP gateway / control plane") should be added to the L5 section alongside the existing MCP-spec entry. The conceptual precedent from the Manufact / ARD / AGT signals suggests this layer is forming even if no second tool has crossed the visibility threshold yet.

## Claims to verify

- **A2A reverse-proxy stability in v1.26.0**: the A2A mode is described as opt-in but the hardening release changelog does not mention A2A-specific testing or fixes. Verify whether A2A routing is production-ready in v1.26.0 or still considered experimental.
- **Fail-closed admission scanning mechanism**: the README claims security scanning with fail-closed admission but does not specify the scanning implementation (static pattern matching, CVE database, LLM semantic analysis, or NVIDIA SkillSpector-style two-stage). The specific mechanism determines whether this is a real security gate or a policy-document claim.
- **OAuth2/OIDC flow completeness**: the gateway claims support for Keycloak, Entra ID, Okta, Auth0, Cognito, and PingFederate. Verify whether all six identity providers are tested to the same level or whether some are listed as "supported" based on documentation alignment alone.
- **3LO token vault security model**: per-user credential brokering (tokens never on developer laptops) is a meaningful security claim. Verify the vault implementation — where tokens are stored at rest (MongoDB with encryption-at-rest?), how rotation is handled, and what happens on token revocation by the upstream provider.
- **Semantic tool discovery latency and accuracy under load**: natural-language tool discovery at runtime is architecturally appealing but introduces an embedding/search step on the critical path of every agent tool call. No latency benchmarks for the discovery path are visible in the README. This matters for `latency: low` agent profiles.
- **MCP 2026-07-28 RC stateless compatibility**: the gateway's per-user token state model is in tension with the RC's stateless transport design. Verify whether the maintainers have addressed or acknowledged the RC's requirements.
- **Federation mechanism**: the Anthropic MCP Registry and AWS Agent Registry federation is listed as a feature. Verify whether this is pull-on-startup (one-time import), periodic sync, or live federation at query time — the distinction affects stale-listing risk.

## Status

- 794★ — well below the 5k registry threshold; no registry entry warranted.
- Apache 2.0 license; Python 73.2% / TypeScript 15.4%; multi-cloud deployment documented; v1.26.0 July 6, 2026.
- First signal for "MCP ecosystem control plane" as an architectural pattern; two-signal rule not met; taxonomy note deferred.
- Open questions: A2A stability, security scanning implementation, 3LO vault model, MCP RC compatibility.
- Monitoring trigger: a second independent open-source MCP management-plane tool (not a deployment platform like Manufact and not a single-server debugger like mcpsnoop) would meet the two-signal threshold for a named L5 sub-type entry.
