# Research Watch: Mireye — Physical-World Location MCP for Agents

- Repo: https://github.com/Mireye-Labs/mireye-earth-mcp
- Source: Hacker News (launched September 3, 2026; YC S26 batch)

## Why this is worth watching
Mireye exposes 300+ geospatial fields (land use, demographics, regulatory rules, risk indices) for any US lat/lon through a single API and MCP server. The structural bet is that physical-world context — what's actually at a location and what rules apply there — is a reusable capability layer that AI agents should be able to call rather than each application assembling itself from raw government data. As agents take on tasks involving physical places (site selection, logistics, real estate, compliance), location context is a natural candidate for a standard MCP capability.

## What stands out immediately
- **300+ geospatial fields per coordinate**: land cover, zoning, FEMA flood zones, EPA superfund proximity, Census demographics, USGS seismic risk — drawn from ~85 sources
- **Source provenance per field**: each returned value carries its originating agency, fetch timestamp, and confidence metadata — this is auditable data, not a black-box API
- **Physical-world scope**: distinct from geospatial mapping tools (Google Maps, OSM); this is decision-support data for agents, not navigation
- **Single API / MCP server interface**: aligns with L4 MCP capability pattern — agents call it as a tool, not as a data pipeline
- **YC S26 batch**: institutional backing implies a supported product with a commercial sustainability path
- **Domain specificity**: US-only initially; global expansion claimed as roadmap

## Why clawfit should care
clawfit's L4 tier currently covers general capabilities (web search, code execution, knowledge retrieval). Mireye is evidence that domain-specific L4 capabilities are emerging with production-grade provenance metadata — attributes a general web search tool cannot provide. This is a pattern clawfit's taxonomy should recognize: "vertical MCP capabilities" as a sub-type within L4. If physical-world context becomes a reusable agent capability (alongside code execution, web browsing, memory), it could eventually inform a `domain_specialization` scoring axis.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capabilities/Skills/MCP** (primary: domain-specific tool capability accessible via MCP protocol)

## Claims to verify
- Star count for the GitHub repo (YC-backed but early-stage; may be below the 100-star general threshold)
- Whether the MCP server is production-ready or demo-quality (documentation depth)
- Data freshness: how often the underlying source data (FEMA, NOAA, Census) is refreshed
- Pricing model: free tier limits and per-call cost
- Coverage completeness: 300 fields claimed, but which are always populated vs. sparse

## Status
- First research-watch doc; YC S26 batch (institutional backing bypasses uncertain star count for monitoring purposes)
- Pattern: "vertical/domain-specific MCP capability" — first clear example of this sub-type in the scan log; watching for a second signal before proposing canonical taxonomy addition
- Registry: not applicable (external capability service, not an agent runtime or model)
