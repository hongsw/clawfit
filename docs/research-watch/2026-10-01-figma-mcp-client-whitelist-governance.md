# Research Watch: Figma MCP Client Whitelist — Application-Layer MCP Access Governance

- Repo/Link: https://github.com/earendil-works/pi/issues/10226 (community issue documenting the restriction)
- Announcement context: https://twitter.com/gayanifigma (Figma MCP team)
- Source: Hacker News front page #23 (111 points, 2026-10-01)

## Why this is worth watching

Figma's decision to restrict its MCP server to a whitelist of approved clients — with all others receiving HTTP 403 on dynamic client registration — establishes a new governance pattern at the L4 capability layer: **platform-enforced MCP client identity filtering**. This is the first documented case of a major design application using client identity as an MCP access control mechanism, and it arrives on the same day that Earendil Pi published the Codemode architecture (tracked separately, 2026-10-01) addressing trust boundaries for MCP tool orchestration from the harness side. The two signals together create a pincer pattern: harnesses are building trusted execution contexts to handle MCP composition (Codemode), while MCP servers are building client identity checks to restrict harness access (Figma). Neither approach was needed when MCP was only used with official IDE clients. The pattern is likely to propagate: any MCP server that handles sensitive enterprise data has organizational incentives to restrict access to auditable, known clients. At 111 HN points, the developer community response confirms this is landing as a meaningful constraint, not an obscure product decision.

## What stands out immediately

- **Allowlisted clients**: VS Code (GitHub Copilot), Cursor, Claude Code, Claude Desktop, Codex, Windsurf, Xcode 27 beta, Gemini CLI — all official IDE clients from major platform vendors
- **HTTP 403 enforcement**: rejection occurs at the dynamic client registration step, before any tool calls are made; Pi 0.99.1 sends `"pi"` as the client name, which Figma rejects at the edge
- **No custom OAuth path**: `mcp:connect` scope is unavailable to custom OAuth apps; dynamic client registration is closed; personal access tokens are not accepted — three separate closure mechanisms
- **No workaround via Pi adapter**: `nicobailon/pi-mcp-adapter` filed an issue to get `pi-mcp-adapter` submitted to the Figma MCP Catalog; this requires an explicit approval process from Figma
- **Security framing by Figma**: the whitelist is justified as preventing unauthorized access to Figma files — Figma handles design assets for products used by hundreds of millions of people; the risk model differs from a code tool
- **Identity vs. capability**: Figma's restriction is based on client identity, not capability scope — an approved client with broad scopes is accepted; an unapproved client with minimal scope is rejected
- **Effective breakage of "open MCP" premise**: MCP's stated model is that any MCP-compatible client can connect to any MCP server; Figma is the first high-profile counterexample from a proprietary application layer

## Why clawfit should care

The L4 capability layer in clawfit's taxonomy currently tracks MCP servers and skill/tool registries as predominantly open-access resources. Figma's whitelist establishes that L4 resources can be closed to non-approved harnesses, which has two implications for clawfit recommendations: (1) recommending an agent harness for a workflow that includes Figma access requires checking whether that harness is on Figma's allowlist — this is a new `integration_compatibility` axis for the recommendation engine; (2) the pattern will recur for any L4 MCP server handling commercially sensitive data (Salesforce, GitHub Enterprise, internal tooling). A future "requires approved client" flag on MCP server capability entries would let clawfit filter out harness/MCP combinations that cannot connect. The signal also validates the Codemode architecture (earendil, tracked today) from a different angle: harnesses that can mimic approved client identity profiles would pass Figma's check, which introduces a new incentive for harnesses to implement client identity spoofing — a governance race condition the MCP spec does not currently address.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capability Layer** (primary): this is an MCP server access control pattern that affects what capabilities a harness can access; governs the L4 layer from the server side
- **Level 2 — Harness / SDK Layer** (secondary): the restriction directly affects harness design decisions — harnesses must now account for client identity as an authorization factor when accessing certain MCP servers

## Claims to verify

- **Whether the whitelist is documented**: Figma's MCP catalog criteria are not publicly documented as of this writing; the allowlist itself may be opaque, making it difficult for harness developers to know whether they qualify
- **Whether this creates a client spoofing incentive**: harnesses that send `"Claude Code"` as their client name to pass Figma's check — this is technically trivial; whether this is a recognized attack surface or an expected workaround
- **Propagation**: other high-value MCP servers (Notion MCP, GitHub Enterprise, Google Workspace MCP) have not announced similar restrictions; whether this is Figma-specific or the beginning of a trend requires confirmation from additional sources within 60 days

## Status

- 📡 Tracking: **first signal for "application-layer MCP client identity whitelist"** as a distinct L4 governance sub-type
- No GitHub repo (platform policy, not open-source tooling); tracked via community issues and HN discussion
- Registry eligibility: not applicable — this is a policy signal, not an agent/LLM/hardware entry
- Related signals: earendil Codemode (2026-10-01, same day) — trust boundary pattern at the harness side; this is the server-side counterpart
- Open questions: Figma's catalog approval process for third-party harnesses; whether MCP spec will address client identity in a future revision
