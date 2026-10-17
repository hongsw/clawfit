# Research Watch: Radware MCP Server Protection — Commercial Security Category for MCP Attack Surface

- Product: https://helpnetsecurity.com/?p=387929 (announcement coverage)
- Source: Web search (announced October 14, 2026)
- Stars: N/A (commercial security product)

## Why this is worth watching
Radware — a network security vendor with existing commercial products for DDoS, WAF, and bot management — announced a dedicated product targeting MCP server infrastructure on October 14, 2026. This is the first commercial network security product explicitly designed for MCP servers. It marks the transition from community MCP security best-practice documents (OWASP MCP Top 10, mcp.directory vulnerability reports) to formal commercial investment in MCP attack surface management.

## What stands out immediately
- **First commercial product category for MCP server defense:** Radware's product joins their LLM Firewall and Agentic AI Protection as a third dedicated AI security SKU; "MCP server protection" is now a named commercial security category
- **Named attack vectors:** authentication attacks and denial-of-service against MCP servers; agent activity monitoring for behavioral anomaly detection
- **Deployment scope:** public cloud, private cloud, Kubernetes, hardware data centers — full enterprise deployment posture
- **Ecosystem context — 200k exposed servers:** mcp.directory's 2026 security report cites approximately 200,000 publicly exposed MCP servers; OWASP MCP Top 10 was published earlier in 2026 as a community vulnerability framework
- **Two-sided commercial ecosystem forming:** Tencent AI Infra Guard (2026-08-20) scanned MCP servers for vulnerabilities from the offensive/audit side; Radware now addresses the defensive commercial side
- **Product not yet shipping at announcement:** Dec 3, 2026 webinar listed; enterprise sales cycle, not yet generally available

## Why clawfit should care
clawfit recommends MCP-capable agent stacks for enterprise governance profiles. The emergence of a commercial MCP security product category is a maturity signal: the MCP attack surface is now large enough and well-enough defined to support dedicated commercial tooling. This affects how clawfit frames `governance_need: hard` recommendations for MCP-using stacks — teams adopting MCP at enterprise scale should now anticipate budgeting for MCP security products alongside the agent tooling itself. Paired with today's Atlassian MCP tiered-access signal, two complementary governance patterns are converging: first-party access control (read/write/destructive tiers, built into the server) and third-party perimeter defense (commercial security product around the server). These are not substitutes; enterprise stacks will likely need both.

## Preliminary interpretation
- **Level 4 — Capabilities / MCP** (primary): MCP security is a governance-and-defense dimension of the MCP layer
- **Level 3 — Governance / Workflow Config** (secondary): access control enforcement and behavioral monitoring are governance-layer concerns

## Claims to verify
- Product functionality described only in press release and trade-outlet coverage; no technical documentation, SDK, or configuration reference reviewed
- "200,000 exposed MCP servers" — primary source for this claim is mcp.directory; methodology not verified
- No production customers or case studies named at announcement time
- Whether the product operates at MCP transport layer (HTTP/SSE) or MCP semantic layer (tool call inspection) or both — not specified in available coverage

## Status
- First signal for "commercial network security product category targeting MCP infrastructure"
- Second MCP security signal overall (after Tencent AI Infra Guard offensive scanner, 2026-08-20); first commercial defensive product
- Two-signal convergence with Atlassian MCP (today): both signals point toward MCP governance at enterprise scale becoming a distinct operational and commercial concern; candidate for dated discovery log note in reference-levels.md
- Monitor: GA announcement date, first customer case studies (webinar December 3, 2026), and whether competing products emerge from existing WAF/API gateway vendors
