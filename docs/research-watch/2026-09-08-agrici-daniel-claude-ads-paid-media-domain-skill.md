# Research Watch: claude-ads — Paid Media Domain Skill for Claude Code (12 Ad Platforms)

- Repo: https://github.com/AgriciDaniel/claude-ads (⭐9,000; 1,300 forks)
- Source: GitHub Topics: claude-code, agent-skill, paid-media; AI Agent Store weekly news (2026-09-01)
- Community mirror: https://github.com/AI-Marketing-Hub/claude-ads
- License: MIT; also compatible with Codex and Gemini CLI

## Why this is worth watching

claude-ads is a Claude Code Agent Skill that provides read-only and capability-gated write access to 12 paid media advertising platforms. The platforms covered (Google Ads, Meta Ads, YouTube Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Apple Ads, Amazon Ads, Reddit Ads, Pinterest Ads, Snapchat Ads, X Ads) collectively represent the majority of programmatic digital ad spend. The skill does not wrap a third-party marketing API aggregator — it implements direct platform integrations for each advertiser.

The design decisions that make this worth tracking are: (1) read-only by default, with writes requiring explicit capability gate activation; (2) source-grounded audits that cite the specific ad creative, keyword set, or campaign parameter being flagged; (3) deterministic scoring rules rather than model-generated scores; (4) versioned JSON output with a stable schema. These four properties together describe a domain skill with engineering discipline, not just a prompt-template wrapper around marketing APIs.

Submitted to Claude Code plugin marketplace March 13, 2026; 9,000 stars; 1,300 forks; active issue and PR activity as of July 2026.

## What stands out immediately

- **12 ad platforms, direct integrations**: each platform integration is maintained separately; this is not a thin wrapper around a single aggregator API
- **Read-only default, writes require capability gate**: the skill's default permission set is read-only; to enable campaign modifications, budget changes, or creative uploads, the user must explicitly activate the write capability in their `aas-stack.json` or skill configuration; this matches the explicit capability-gate pattern in coding-tools-mcp (2026-09-07)
- **Source-grounded audit output**: when the skill produces an audit finding (e.g., "keyword bidding inefficiency"), it cites the specific campaign ID, ad group ID, and keyword that triggered the finding; findings without citations are not generated
- **Deterministic scoring rules**: performance scores are computed from declared rules (e.g., CTR below X% for this vertical → efficiency flag), not from model-generated assessment; this means score reproducibility across runs, which is required for auditable marketing ops workflows
- **Versioned JSON output**: the audit schema is versioned; consuming systems can pin a schema version and receive breaking-change warnings before the schema changes; this is a rare design decision in agent skills
- **1,300 forks (1:6.9 fork ratio)**: similar fork ratio to coding-tools-mcp (1:6); high fork ratios in this range typically indicate production toolchain use, not reference interest
- **Cross-runtime compatibility**: the skill is compatible with Claude Code, Codex, and Gemini CLI; it is not Claude-specific in its runtime target
- **Community mirror at AI-Marketing-Hub**: the community mirror suggests the skill has been adopted beyond the original author's direct user base

## Why clawfit should care

1. **Paid media domain skills are a new L4 sub-type not previously seen in this log**: clawfit's registry has general-purpose skills (coding, search, file operations) but no domain-vertical skills that integrate with business-function APIs. claude-ads is the first signal for a "domain skill" sub-type — a skill with deep integration into a specific business function (paid media, in this case) that uses business-function data (campaign performance, spend, ROAS) rather than code or documents as its primary input. This is L4b territory: not a general-purpose capability but a domain-specific capability with business-function data contracts.

2. **Capability-gate pattern for write operations is now confirmed by two independent signals**: coding-tools-mcp (2026-09-07) uses a three-tier permission model (safe/trusted/dangerous) to gate write and execution operations; claude-ads uses a capability-gate pattern for ad platform write access. Two independent signals confirm the explicit capability gate as a design pattern for agent skills that combine read and write access. This is worth documenting as a repeating L4 design pattern — it may warrant a `write_capability_gate: required | optional | none` field in skill registry entries.

3. **Deterministic scoring rules in a Claude skill are a precedent for auditable AI outputs**: model-generated scores are reproducible only probabilistically; deterministic scoring rules (if CTR < threshold then flag) produce identical outputs for identical inputs. For marketing ops workflows where campaign audit findings are reviewed by humans and acted upon, deterministic scoring is a functional requirement. If clawfit adds domain skill recommendations, the `output_determinism: deterministic | probabilistic` property would be relevant to `task: audit` or `task: reporting` profiles.

4. **9,000 stars + 1,300 forks confirms paid media as a meaningful Claude Code user segment**: the size and fork count suggest this is in production toolchains, not only in personal projects. Paid media operations teams represent a user segment with recurring, structured, high-stakes workloads that map well to agent-assisted automation. This user segment's requirements (auditability, source-grounded output, write capability gates, schema versioning) are more demanding than the requirements in clawfit's current `task` filter set.

5. **Cross-runtime positioning (Claude Code, Codex, Gemini CLI) parallels coding-tools-mcp's model-neutral design**: the same pattern seen in yesterday's signal (model-neutral runtime) appears in today's domain skill signal. Cross-runtime compatibility is becoming an explicit design goal for skills in this size tier — a `runtime_compatibility: claude-only | multi-runtime` dimension would surface these as a distinct category.

## Preliminary interpretation

Current best reading:
- **L4 — Capabilities / Skills / MCP (primary)**: claude-ads is an agent skill that exposes ad platform APIs as agent-callable capabilities; it is consumed by agents at inference time as a structured tool
- **L4b — Domain Skills (emerging sub-type)**: the deep paid-media integration, deterministic scoring, and versioned output schema differentiate this from general-purpose capabilities; this belongs in an "L4b domain skill" sub-category if one were defined

## Claims to verify

- Whether the deterministic scoring rules are publicly documented (so users can audit and modify the scoring thresholds) or are baked into the skill implementation without user access
- Whether the 12 platform integrations use official advertiser APIs with documented rate limits, or unofficial endpoints that could break without notice
- Whether the read-only default is enforced at the API credential level (the credential provided to the skill has read-only API scope) or only at the skill's application logic level (a sufficiently capable model could bypass the application-level gate)
- Whether schema versioning is backward-compatible (consuming systems on v1.x continue to work after a v1.y release) or whether "versioned output" means only that breaking changes increment the major version
- Whether the cross-runtime compatibility claim has been tested against current Codex and Gemini CLI versions, or whether the compatibility is aspirational based on MCP protocol compliance

## Status

- 9,000 stars (well above registry threshold 5k★); MIT; plugin marketplace submission March 13, 2026 (borderline 6-month window: 5 months 26 days); active as of July 2026
- Registry consideration: blocked on schema gap — no `domain_skill` entry type in agents.json; no deterministic per-execution cost (cost is the model's API cost per session); the skill is not an agent
- First "paid media domain skill" signal in this log; first L4b domain skill signal overall
- Two-signal check for capability-gate write pattern: coding-tools-mcp (2026-09-07) + claude-ads (2026-09-08) = two signals for explicit capability-gate on agent write operations. This meets the two-signal rule for documenting as a confirmed repeating L4 design pattern in the taxonomy.
- Watch: whether other domain verticals (finance, legal, HR) produce similar deep-integration domain skills; whether the AI-Marketing-Hub community fork develops independently or stays in sync with the upstream repo; whether Anthropic's plugin marketplace publishes usage statistics that confirm production adoption
