# Research Watch: browserbase/skills

- Repo: https://github.com/browserbase/skills
- Also see: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · https://www.browserbase.com · https://github.com/VoltAgent/awesome-agent-skills

## Why this is worth watching

At 1,794 total stars, the repo sits below clawfit's usual 5k registry threshold, but the +322/day velocity on 2026-05-04 (GitHub Trending All Languages #6) is the sharpest one-day climb for any skill pack tracked since marketingskills (+285/day, 2026-04-24). The signal gains additional weight from Browserbase's institutional positioning: $67.5M raised across seed, Series A, and a $40M Series B (lead: Notable Capital; existing: Kleiner Perkins, CRV; angels include Patrick Collison and Guillermo Rauch), 36M+ remote browser sessions served, and 800k weekly SDK downloads as of March 2026. More concretely, this is the first official first-party skill pack from a well-funded web-infrastructure company explicitly targeting the Claude Agent SDK's skill layer — a different provenance class from practitioner dotfiles (mattpocock/skills, Karpathy autoresearch) and community aggregators (VoltAgent/awesome-agent-skills).

## What stands out immediately

- Nine distinct skills shipped as a single installable pack: `browser` (core automation + remote Browserbase sessions), `browserbase-cli` (full `bb` CLI wrapper), `functions` (serverless function deployment to Browserbase cloud), `site-debugger` (bot-detection / selector / auth failure diagnosis), `browser-trace` (DevTools protocol tracing with screenshots + DOM capture), `bb-usage` (terminal dashboard for session metrics and cost forecasting), `cookie-sync` (local Chrome cookie synchronization to persistent contexts), `fetch` (static page retrieval without a live session), and `ui-test` (adversarial QA with git diff analysis).
- Dual execution environment model in the `browser` skill: local mode uses the machine's Chrome instance; remote mode routes through Browserbase's cloud infrastructure with anti-bot stealth, residential proxies across 201 countries, and automatic CAPTCHA solving. This is a claim-to-inspect: the stealth and CAPTCHA claims are stated in documentation; independent adversarial testing has not been conducted by this team.
- The `browser` skill uses the `@browserbasehq/browse-cli` npm package as its execution layer. Skills are pure markdown-plus-YAML following Anthropic's `SKILL.md` frontmatter schema — no novel format, portable in principle.
- Installation is via `npx skills add browserbase/skills` (the Vercel-ecosystem `skills` CLI, tracked 2026-04-23 as a platform-vendor skill manager) or directly through the Claude Code plugin marketplace. This demonstrates the cross-vendor tool chain that the 2026-04-28 skill-portability observation anticipated.
- License not stated on the repo page at time of review. Content is JavaScript (85%) + HTML (15%). 118 forks, 27 open pull requests, 44 commits on main — early but actively maintained stage.
- The `ui-test` skill frames browser automation as adversarial QA with git diff context, not just extraction. This is a distinct use-case angle from the existing browser-automation sub-cluster (Libretto, browser-harness, Obscura) which was tracked primarily under research and scraping use cases.

## Why clawfit should care

The existing browser automation sub-cluster (confirmed as a named Level 4c sub-cluster 2026-04-29) was built around raw CDP tools. browserbase/skills approaches the same capability from the opposite direction: it layers agent-oriented cloud infrastructure into a native Anthropic skill pack, meaning the capability surfaces as `clawfit task: qa` and `clawfit task: research` enrichment rather than as a standalone tool-use selection. This makes it a direct input to capability scoring for any recommendation profile that includes `web-interaction` as a hard requirement. The `network: online` versus `network: offline` filter axis is directly affected: the remote Browserbase path requires an API key and live connectivity; the local path degrades gracefully to Chrome on the user's machine. The `budget` axis is also live: Browserbase sessions are metered (bb-usage exists precisely because session cost is non-trivial at scale). Additionally, the `ui-test` skill closes a gap in the `task: qa` recommendations where browser-based adversarial testing was previously not available as a skill-pack form factor.

## Preliminary interpretation

Current best reading:
- **Level 4b — Domain skill pack** (primary): Nine skills deployed as a single installable pack extending Claude Code's native capabilities, authored and maintained by the infrastructure vendor. This follows the same L4b pattern as marketingskills, obsidian-skills, and Claude-Code-Game-Studios, but targets web-interaction and QA domains.
- **Level 4c — Tool-use extension** (secondary): The remote execution path (stealth browser, CAPTCHA, proxies) is a cloud tool-use capability mediated through the `browse` CLI. The `fetch` skill is a lightweight HTTP tool-use extension with no browser overhead.
- Relationship to existing browser-automation sub-cluster (Level 4c, confirmed 2026-04-29): this is structurally distinct — the sub-cluster (Libretto, browser-harness, Obscura) are standalone tools the agent calls; browserbase/skills is a skill pack that packages the invocation workflow itself as reusable agent instructions plus CLI dependency. The two layers are complementary, not competing.
- The `ui-test` skill could eventually support a `security-testing` or `adversarial-qa` task-type axis if corroborating signals accumulate — consistent with the Shannon signal (2026-04-26) suggesting `qa` as a clawfit task label may be too broad.

## Status

- Tracking active. Below 5k-star registry threshold (1,794 stars, 2026-05-04). Velocity (+322/day) and institutional provenance (Browserbase, Series B, Kleiner/CRV/Notable) justify inclusion as a research-watch signal without registry entry. Promote to Level 4b registry if stars cross 5k or a second major infrastructure vendor ships a comparable first-party skill pack within the same quarter.
