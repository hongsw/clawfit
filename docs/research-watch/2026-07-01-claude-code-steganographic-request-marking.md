# Research Watch: Claude Code Steganographic Request Marking

- Repo: N/A — reverse-engineering finding; no public repo
- Also see: https://thereallo.dev/blog/claude-code-prompt-steganography · https://news.ycombinator.com/item?id=48734373 · https://github.com/Piebald-AI/claude-code-system-prompts · https://github.com/anthropics/claude-code/issues/26898

## Why this is worth watching

A reverse-engineering analysis of the Claude Code binary revealed that the client silently embeds invisible Unicode markers inside date strings injected into the system prompt, encoding metadata about the API base URL and timezone at request time. This is not a tool or library — it is an infrastructure mechanism already in production that reveals a previously undocumented governance dimension: **request provenance marking** at the agent-runtime layer. With 1,322 points and 379 comments on Hacker News (2026-07-01), it has generated the highest practitioner-discussion volume of any single Claude Code architectural finding this tracking cycle, and the signal is directly relevant to how clawfit reasons about LLM gateway tools.

## What stands out immediately

- **Mechanism (claim to inspect):** The Claude Code client modifies system-prompt date strings before sending the request to the Anthropic API. Invisible or near-invisible Unicode characters are inserted into the date string. Domain and keyword lists are stored base64-encoded and decoded client-side using XOR key 91. The resulting marker encodes whether the request is transiting a known reseller domain, a hostname containing signals like "deepseek" or "zhipu", or a non-standard API base URL.
- **Visual stealth:** The altered date string is visually identical in monospace terminal fonts. The marking is not surfaced to the user and is not documented in release notes or privacy policy disclosures, per the thereallo.dev analysis.
- **Inferred purpose (claim to inspect):** Anthropic backend parses the marker to flag requests that have passed through unauthorized gateways, API resellers, or potential model distillation pipelines. The classifier appears geographically targeted based on the domain list content.
- **Gateway impact (validated pattern, not edge case):** Claude Code's own documentation acknowledges common gateway configurations via LiteLLM and OpenRouter. CVE-2026-21852 (separately documented) showed that `ANTHROPIC_BASE_URL` manipulation is an active attack surface, which contextualizes why Anthropic would want in-band provenance signals independent of HTTP headers.
- **Header-based provenance already existed:** Claude Code sends `X-Claude-Code-Session-Id`, `X-Claude-Code-Agent-Id`, and `X-Claude-Code-Parent-Agent-Id` on every request. The steganographic marking is a *second, in-band* provenance channel that survives gateway header stripping — which is architecturally meaningful.
- **GitHub issue #26898:** A bug report about stray Unicode subscript characters appearing in Claude Code terminal output (version 2.1.47, closed as not planned) may be a surface manifestation of the same encoding mechanism leaking into rendered output. This is circumstantial; correlation only.
- **HN debate framing:** Top comments divide between "undisclosed client-side behavior is a trust violation" and "steganography is necessary precisely because a detectable watermark would be stripped by the gateways being targeted." Neither camp disputes the technical finding.

## Why clawfit should care

clawfit's recommendation engine scores (agent, llm, hardware) triples and applies filters including `network` (online/offline) and `statefulness` (session/stateless). It does not currently model **the path between the agent runtime and the LLM API** as a governance-relevant dimension. This finding surfaces two concrete gaps:

1. **Gateway tools are not currently in the registry.** LiteLLM, OpenRouter, and similar API routing layers appear in the ecosystem (LiteLLM: primary L2/L4, routing and cost management; OpenRouter: L2 meta-routing) but are not registered as scoreable candidates. If an org's deployment routes Claude Code through one of these gateways, the provenance-marking behavior may cause the request to be flagged by Anthropic, creating a hidden compliance risk. This is a new failure mode for org-fit scoring that has no current field.

2. **`org_fit` schema does not include request provenance.** The `missing-recommendation-axes.md` reference note flags governance and autonomy level as under-modeled. Request provenance — specifically, whether an org's API routing path is Anthropic-direct or gateway-mediated — is now a concrete dimension that affects the behavior of a production tool (Claude Code) in ways the operator may not anticipate. A candidate `api_routing` field (values: `direct`, `gateway_mediated`, `offline`) would capture this.

The finding also raises a categorization question for clawfit's L3 layer. L3 is defined as "team harness / executable SSOT / governance layer." Request provenance marking is a governance mechanism, but it is implemented at L1 (inside the base runtime client binary) and enforced at the infrastructure layer (Anthropic backend). It does not cleanly belong to any single layer — it is a cross-cutting governance signal embedded in the transport.

## Preliminary interpretation

Current best reading:

- **Ecosystem meta-signal, not a deployable tool** — no registry entry warranted
- **Primary layer resonance: Level 3 — Governance layer** (the mechanism implements a governance control: request provenance enforcement)
- **Secondary layer resonance: Level 1 — Base runtime** (the marking is embedded inside the Claude Code binary, not in any external harness or wrapper)
- **Tertiary implication: Level 2** — LLM gateway tools (LiteLLM, OpenRouter) that intercept Claude Code traffic are the primary affected surface; their registry characterization should note the provenance-marking interaction
- The mechanism does not fit neatly into the current 7-layer taxonomy because it is a governance primitive implemented cross-layer (L1 client + L7 backend enforcement). It is closer to a **governance transport channel** than a capability or interface layer.
- `org_fit.api_routing` is the most actionable schema implication; flag for `missing-recommendation-axes.md` review rather than immediate map mutation.

## Status

- Ecosystem meta-signal logged 2026-07-01; no registry entry; flag `org_fit.api_routing` dimension for next `missing-recommendation-axes.md` revision; monitor for Anthropic disclosure or formal documentation of the mechanism.
