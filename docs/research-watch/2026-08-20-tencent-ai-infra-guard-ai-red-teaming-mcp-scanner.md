# Research Watch: AI-Infra-Guard — Full-Stack AI Red Teaming Platform

- Repo: https://github.com/Tencent/AI-Infra-Guard (⭐4,864)
- Source: GitHub Trending Python (2026-08-20); Tencent Zhuque Lab

## Why this is worth watching
AI-Infra-Guard is the most comprehensive open-source AI attack-surface scanner to date. Its scope is deliberate: it doesn't test the LLM itself (jailbreaking is one module, not the core) — it tests the infrastructure around the LLM. The MCP Server Scan module specifically enumerates 14+ risk categories in Model Context Protocol servers, including tool poisoning and credential exfiltration. As MCP adoption grows and more production systems expose MCP endpoints, tooling that can audit those endpoints systematically is filling a real gap. This comes from Tencent Zhuque Lab, which has credible prior security research; it's not a lightweight demo project.

## What stands out immediately
- **Four scan modules with distinct threat models:**
  - Agent Scan: workflow-level vulnerabilities in Dify, Coze; unsafe agent behaviors
  - Skills Scan: plugin/skill code analysis for 9 SkillTrustBench risk categories (T01–T09): instruction hijacking, malicious code, privilege escalation, insecure dependencies
  - MCP Server Scan: 14+ risk categories; targets tool poisoning and credential exfiltration specifically
  - AI Infrastructure Scan: fingerprints 130+ components (vLLM, Ollama, ComfyUI, Triton, etc.) against 2,000+ CVE rules
- **Jailbreak evaluation module** using multi-turn attack chains — tests prompt robustness, not just output safety
- **Model/API relay checker** for fingerprinting and verifying API endpoints; relevant for detecting unauthorized model proxies
- **Apache 2.0 license, Docker deployment, React web UI** — not a research artifact; designed for internal security self-assessment
- **"Integrates with OpenClaw agent ecosystem"** — direct integration point suggests enterprise deployment path
- Currently warns "should not be deployed on public networks" due to missing authentication — honest about production readiness

## Why clawfit should care
clawfit currently has no security/red-team dimension in its registry schema. AI-Infra-Guard makes that gap concrete: an organization choosing a harness or MCP server today cannot query clawfit for its attack surface. The Skills Scan module covers exactly the categories a governance-conscious team needs to assess before enabling a skill library (the `governance_need: hard` segment). The MCP Server Scan is directly relevant as clawfit's L4 (capabilities/MCP) recommendations grow.

More specifically: if MCP server security scanning becomes standard practice before production deployment, a `security_assessed: [none | self-assessed | external-audit]` dimension becomes meaningful for L4 registry entries.

## Preliminary interpretation
- **Level 5 — Evaluation / Observability / Security** (primary): systematically audits AI agent infrastructure for attack surface, not just performance
- **Level 4 — Capability Layer / MCP** (secondary): the MCP Server Scan directly targets the L4 layer

## Claims to verify
- "14+ risk categories in MCP servers" — the specific category list needs review; do these categories overlap with known MCP threat models (prompt injection, tool shadowing, SSRF) or introduce new ones?
- SkillTrustBench taxonomy (T01–T09): this taxonomy needs independent sourcing; is it Tencent-internal or published separately?
- CVE coverage: "2,000+ CVEs across 130+ components" — scope sounds ambitious; verify whether these are AI-specific CVEs or general CVEs across named components
- OpenClaw integration: "integrates with OpenClaw agent ecosystem" — OpenClaw is not tracked in clawfit registry; verify what OpenClaw is before treating integration as a credibility signal
- Production readiness caveat: missing authentication is a significant self-limitation; real-world internal deployments would require custom auth wrapper

## Status
- Tracking: new signal 2026-08-20; 4.9k★ meets registry star threshold
- Registry eligibility: partially eligible — star count qualifies, but AI-Infra-Guard is a security tool, not an agent/LLM/hardware; no direct `agents.json`, `llms.json`, or `hardware.json` schema mapping
- Two-signal rule: single signal for "AI red teaming platform with MCP scanner" sub-type; watch for second independent project before promoting taxonomy sub-type
- Schema gap: `security_scan_coverage: [none | skills | mcp | infrastructure | full-stack]`; `red_team_support: bool`
