# Research Watch: pi-generative-ui

- Repo/Link: https://github.com/Michaelliv/pi-generative-ui
- Source: hongsw GitHub stars

## Why this is worth watching
pi-generative-ui reverse-engineered Claude.ai's internal `show_widget` tool — including extracting Anthropic's 72K production design guidelines verbatim from exported conversation JSON — and rebuilt it for the `pi` macOS agent runtime. The result: LLMs can now generate live, streaming, interactive HTML/SVG widgets that open in native macOS windows (WKWebView). At 876 stars this is a meaningful signal that generative UI outside the browser is gaining traction.

## What stands out immediately
- Streams partial HTML tokens into a live DOM via morphdom — widgets render as they generate, not after
- Bidirectional bridge: `window.glimpse.send(data)` lets widgets send data back to the agent
- Extracted Anthropic's actual design system (typography, color, Chart.js config, SVG patterns) from claude.ai exports
- macOS-only (Swift/WKWebView); requires Xcode Command Line Tools
- Two automatic LLM tools: `visualize_read_me` (lazy design guideline loader) + `show_widget` (HTML renderer)
- Plugin install via `pi install git:github.com/Michaelliv/pi-generative-ui` — one command

## Why clawfit should care
This is a strong L7 signal: generative UI is moving from web browsers into native desktop agent surfaces. clawfit's human interface category currently has voice tools (Ghost Pepper) but no interactive visualization / generative UI entry. The Anthropic design system extraction is also a research artifact worth tracking — it reveals how Claude.ai structures visual output constraints internally. Relevant `tasks`: code-gen (for developers building dashboards), qa (for data visualization workflows).

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface / generative UI (native macOS, streaming widget rendering)**

## Status
- Tracking: new entry, medium-high signal. 876 stars. macOS-only limits reach; monitor for cross-platform port and whether Anthropic formalizes the `show_widget` API.
