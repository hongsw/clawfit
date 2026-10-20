# Research Watch: Websites Blocking AI Agents — Web Access Restrictions for Browsing Agents

- Repo/Link: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web
- Source: GeekNews (front page)

## Why this is worth watching
Major commercial websites are actively blocking AI browsing agents that attempt to automate reservations, purchases, and searches on their behalf. This is a new infrastructure constraint on `network: online` agents — the open web is becoming selectively inaccessible rather than universally crawlable.

## What stands out immediately
- Blocking is asymmetric: sites that offer their own AI features may block third-party agents while permitting direct user access
- Signals a transition from permissive crawl tolerance (search-bot era) to active agent discrimination
- Creates a new dimension for recommending online agents: **web access reliability** differs from general `network: online` capability
- Affects any agent that relies on web browsing, form filling, or web scraping for its primary workflow
- Likely to accelerate demand for MCP-based structured APIs (alternatives to browser scraping), already tracked in Atlassian MCP and Xerj signals

## Why clawfit should care
Current clawfit `network` dimension is binary: online/offline/hybrid. This signal introduces a sub-category: **online but web-blocked** — agents that require internet but rely on unstructured web access (browser automation) rather than structured API calls. Tools like Goose, OpenCode, and general browser-use agents will be differentially affected versus tools that use structured MCP/API calls. A `web_access_reliability` annotation on registry entries that use browser automation is a candidate addition.

## Preliminary interpretation
Current best reading:
- **Infrastructure constraint** cutting across L1–L4 (affects base runtimes, harnesses, and capabilities that rely on web browsing)

Not a new tool — an ecosystem constraint signal.

## Status
- First signal for "major commercial sites actively blocking AI browsing agents at scale"
- Confirms trajectory toward MCP/structured-API as preferred agent access pattern
- No registry entry warranted; candidate `web_access_reliability` annotation for browser-automation tools
