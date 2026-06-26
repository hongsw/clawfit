# Research Watch: aws/agent-toolkit-for-aws — Official AWS MCP Toolkit

- Repo/Link: https://github.com/aws/agent-toolkit-for-aws
- Source: GitHub Trending — 1,125★

## Why this is worth watching
Amazon Web Services officially published a toolkit of MCP servers, skills, and plugins to help AI agents build on AWS services. This is a first-party vendor signal — the same pattern as `google/skills` (tracked 2026-06-09, 12.4k★) and `aws-labs` MCP examples. AWS entering the skill/plugin layer with an official, supported repo confirms the pattern of major platform vendors competing to capture the L4 capability surface.

## What stands out immediately
- Officially AWS-supported (not community or AWS Labs) — institutional commitment
- Python; covers build, deploy, and query workflows on AWS services
- Named alongside MCP servers AND skills AND plugins — covers the full L4 toolkit surface
- Third major platform vendor to publish a first-party agent skill pack (after Google and Anthropic)

## Why clawfit should care
The `google/skills` signal (2026-06-09) established "first-party platform-vendor skill pack" as a named L4b sub-type, but lacked a second signal. aws/agent-toolkit-for-aws is that second independent signal — both are first-party, both use MCP protocol, both target AWS/GCP services as the action surface. Two-signal threshold for the sub-type is now met, warranting a map entry for "first-party cloud-vendor agent skill packs" as a discrete L4b sub-type. Organizations that are AWS-native should see this in their recommendation alongside google/skills for GCP-native orgs.

## Preliminary interpretation
Current best reading:
- **Level 4b — Domain skill pack** (cloud-vendor first-party sub-type, AWS variant)

## Status
- 1,125★ — below individual registry threshold. Two-signal milestone met for the L4b sub-type.
- Map entry for "first-party cloud-vendor skill packs" sub-type warranted; individual aws-toolkit registry entry deferred.
- Promotion criterion: 5k★ OR confirmed MCP Registry listing.
