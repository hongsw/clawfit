# Research Watch: Agentic Resource Discovery (ARD) Specification

- Repo/Link: https://agenticresourcediscovery.org
- Source: Hacker News

## Why this is worth watching
ARD is an open protocol specification for pre-invocation discovery of agentic resources — enabling AI systems to locate available agents, APIs, plugins, and workflows before calling them. Unlike MCP (which governs execution), ARD is the layer that answers "what capabilities exist?" not "how do I call them?" A working group including Microsoft, Google, HuggingFace, Cisco, Databricks, GitHub, Nvidia, Salesforce, ServiceNow, and Snowflake signals broad institutional intent to standardize this layer.

## What stands out immediately
- Explicitly **not a replacement for MCP, Skills, or API runtimes** — it's a pre-invocation discovery layer
- Defines AI Catalog entries covering agents, APIs, plugins, and workflows
- Working group spans 10+ major companies across cloud, infra, and tooling sectors
- Positioned as a cross-vendor open standard, not proprietary to any single platform
- Fills a genuine taxonomy gap: no current clawfit L4 entry covers capability *discovery* vs. capability *execution*

## Why clawfit should care
The clawfit recommendation engine currently treats tool capabilities as static metadata in a JSON registry — a user picks a tool and its tools are fixed. ARD proposes a dynamic discovery layer where agents self-describe available resources at runtime. If ARD achieves adoption (given the working group composition, plausible within 12 months), harness-selection decisions may increasingly factor in "does this harness support ARD?" as a criterion. This could require a new scoring dimension: `discovery_protocol: [ard, mcp-only, static]`.

## Preliminary interpretation
Current best reading:
- **Cross-cutting L2/L4 — pre-invocation capability discovery protocol**
- L4 primary (what capabilities are available and how to find them)
- L2 secondary (harnesses that consume the discovery layer to route agent actions)
- Distinct from MCP (L4 execution), Skills distribution (L4b), and agent orchestration (L2)

## Status
- First signal — hold pending (a) public reference implementation or (b) adoption by any existing L1/L2 agent runtime
- Promotion criterion: confirmed ARD implementation by a registry-tracked harness OR a public open-source implementation with independent usage
- Schema watch: potential new `discovery_protocol` field in org_fit if protocol adoption accelerates
