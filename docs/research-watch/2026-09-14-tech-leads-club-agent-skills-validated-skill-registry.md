# Research Watch: tech-leads-club/agent-skills

- Repo/Link: https://github.com/tech-leads-club/agent-skills
- Source: GitHub Trending (all languages, 2026-09-14)
- Stars: 5,638 (+265 today)
- Language: TypeScript
- License: unconfirmed

## Why this is worth watching
`agent-skills` positions itself as a **security-validated, professionally-curated** skill registry for AI coding agents — distinct from every prior skill collection in this log (addyosmani's personal pack, Stitch, dotnet-skills, NVIDIA's vendor stack, garden-skills, sickn33 AAS v17) by leading with security guarantees and supply-chain validation. The 265/day velocity on a 5.6k-star repo suggests this is gaining rapid adoption in enterprise developer communities. This arrives one week after SnailSploit/Claude-Red demonstrated that offensive security skills can be distributed as agent skill packs — the security-first positioning of this registry appears to be a direct response to that risk surface.

## What stands out immediately
- Targets "professional AI coding agents" explicitly — not hobbyist or demo use
- Claims supply-chain validation: skills are reviewed before inclusion, not self-submitted
- TypeScript-native (matches Claude Code, Cline, Cursor, Goose plugin ecosystems)
- Emerging org (`tech-leads-club`) with no prior research-watch presence — new entrant
- No vendor lock: targets cross-agent compatibility (not Claude-specific, not OpenAI-specific)
- 5.6k stars puts it at threshold; 265/day velocity is above recent agent-skills entries (garden-skills was ~100/day at first tracking)

## Why clawfit should care
The security-validation angle introduces a new dimension not currently modeled in `org_fit`: **skill supply-chain trust**. A `governance_need: hard` profile today scores neutral on skill-layer risk — this registry demonstrates that enterprise teams are beginning to treat skill provenance as a hard constraint, not just a preference. Additionally, the cross-agent compatibility claim (TypeScript, no lock-in) is relevant to multi-tool org profiles that mix agents.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill library (security-validated variant)**, secondary **Level 3** (governance/validation policy layer)

The validation gatekeeping function (skills reviewed before inclusion) is a Level 3 behavior grafted onto what would otherwise be a pure L4 catalog. This hybrid L3/L4 placement makes it structurally different from all previously tracked skill collections.

## Status
- First appearance 2026-09-14; threshold crossed at 5,638★
- Registry entry deferred: no per-call pricing, no agent/LLM schema slot; skill collection pattern
- Watch: does the validation model survive scale? Does a `skill_trust_tier` axis emerge from community adoption?
