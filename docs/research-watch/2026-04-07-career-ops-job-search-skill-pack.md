# Research Watch: Career-Ops

- Repo/Link: https://github.com/santifer/career-ops
- Source: hongsw GitHub stars

## Why this is worth watching
Career-Ops is a 12,103-star Claude Code skill pack that turns the agent into a full job search pipeline — evaluating offers, generating tailored ATS PDFs, scanning portals with Playwright, and maintaining a structured tracker. It was battle-tested on 740+ real offers by its creator and represents one of the most mature, domain-specific skill packs built on Claude Code. The star count signals strong practitioner adoption for a niche use case.

## What stands out immediately
- 14 skill modes including offer evaluation (A-F scoring, 10 dimensions), CV generation, portal scraping, and negotiation scripting
- Go dashboard + Node.js/Playwright scraping stack — not a pure Python repo, closer to a full app than a script
- Explicitly non-spray-and-pray: designed as a filter to reduce noise, not automate mass-applying
- Accumulates an "interview story bank" of STAR+R stories across evaluations — persistent memory pattern
- Real case study: creator used it to evaluate 740+ offers and land a Head of Applied AI role

## Why clawfit should care
This is the clearest current example of an L4b skill pack targeting a non-developer persona (job seeker / researcher). clawfit's `tasks` taxonomy currently has `research` and `summarization` but no job-search or career-ops category — this signals a gap. The multi-language stack (Go + Node) also stretches the assumption that skill packs are single-language CLI tools.

## Preliminary interpretation
Current best reading:
- **Level 4b — Skill pack operating on top of Claude Code (domain: career / job search)**

## Status
- Tracking: new entry, very high signal. 12,103 stars (live count). Strong adoption curve since April 2026. Monitor for enterprise/team features and whether skill modes become reusable primitives.
