# Research Watch: ppt-master — AI Agent Skill for Native Document-to-PPTX Conversion

- Repo: https://github.com/hugohe3/ppt-master (⭐46.8k)
- Source: GitHub Python Trending (+383 stars today, 2026-08-14)

## Why this is worth watching

ppt-master is a Python tool that converts source documents (PDFs, DOCX files, topics) into native PowerPoint presentations — actual .pptx files with shapes, transitions, animations, and data-backed charts, not flat images. The project explicitly frames itself as "a workflow (a 'skill') that runs inside any agent-capable AI tool" compatible with Claude, GPT, Gemini, and Kimi. At 46.8k stars (3.8k forks) with sustained Python trending velocity today, it has accumulated significantly more stars than most tracked L4b skills — a distribution scale that warrants understanding even if the project's taxonomy position is less clear-cut than harness or runtime entries.

## What stands out immediately

- **Self-described as "a workflow / skill" for agent tools**: the framing is intentional — not a standalone CLI, but a skill designed to run within Claude Code, ChatGPT Canvas, Gemini, or other agent-capable interfaces; the project does not build its own agent loop
- **Native PPTX object model output**: generates actual PowerPoint objects (shapes, transitions, data-backed charts, tables, audio narration from speaker notes) rather than flat images or screenshots; output is editable in PowerPoint and Google Slides
- **Custom template support**: accepts .pptx templates for brand consistency across generated decks
- **Multi-model and multi-harness compatibility**: Claude, GPT, Gemini, Kimi listed as backends — explicit cross-harness design, not Claude Code-specific (unlike diagram-design, which is Claude Code-primary)
- **High fork-to-star ratio (~8%)**: 3.8k forks relative to 46.8k stars indicates active customization, not just passive starring
- **Python implementation**: consistent with the agent skill ecosystem where Python is the primary implementation language
- **46.8k stars**: the highest star count of any tracked L4b candidate whose primary artifact is a business document; exceeds diagram-design (6.3k★ at first tracking), K-Dense scientific-agent-skills (33.5k★ at first tracking)

## Why clawfit should care

ppt-master raises a specific taxonomy question: should the clawfit L4b skill layer include skills whose primary artifact is a business document (PPTX) rather than code, prose, or a diagram?

Prior tracked L4b entries producing human-readable artifacts:
- **diagram-design** (2026-08-11, L4b/L6): HTML+SVG editorial diagrams via Claude Code slash commands
- **book-to-skill** (2026-07-01, L4b): PDF-to-skill format conversion — the artifact is a structured skill file, not a finished document
- **K-Dense scientific-agent-skills** (2026-08-04, L4b): 161 domain skills for scientific workflows — artifacts are code, analyses, and data, not presentations

ppt-master is the first tracked L4b entry whose primary output is a native office document format (.pptx) rather than code, prose, structured data, or an SVG diagram. The "task: presentation-generation" workflow differs from "task: code-gen" and "task: writing" in ways that affect model selection (multi-modal models that understand layout and visual hierarchy are better suited than pure text generators). **Schema watch:** `skill_artifact_type: [code | prose | data | diagram | presentation | media]`; `document_format: [html | svg | pptx | docx | xlsx]`; `template_aware: bool`.

## Preliminary interpretation

- **Level 4b primary** (skills/installable capabilities): runs as a workflow within agent-capable tools — same form factor as diagram-design (skill-invoked via agent conversation) and phuryn/pm-skills (procedural agent skills); explicitly does not build its own agent loop
- **Level 6 secondary** (human interface): the primary artifact — a native PPTX file — is a business document for direct human consumption and presentation delivery

## Claims to verify

- **Creation date and recency**: 46.8k stars is very high for a project claiming to be new; verify whether the repo was created within the 6-month recency window (after February 2026) or whether it accumulated stars over a longer period with a recent viral resurgence
- **"Native PPTX objects" claim**: verify whether generated .pptx files open cleanly in PowerPoint and Google Slides with fully editable objects, or whether there are known format compatibility issues (incorrect shape anchoring, missing font substitution, broken chart data links)
- **Cross-harness compatibility**: the project claims to work with Claude, GPT, Gemini, and Kimi — verify whether this requires specific agent configuration or whether a natural-language prompt ("create a deck from this PDF") is sufficient without additional setup
- **Template accuracy**: verify whether .pptx template inheritance is faithfully applied (font stack, color palette, master slide layout) or whether the tool defaults override template styles in generated slides

## Status

- 46.8k⭐, Python; license not confirmed in available data
- **Registry eligibility: no** — no cost/latency data (free open-source tool); does not map to agents.json, llms.json, or hardware.json schema; no installable agent runtime
- **First signal for "native office document generation skill" in the L4b track** — distinct from diagram-design (SVG/HTML, Claude Code-primary) and book-to-skill (skill format conversion)
- **No canonical section change**: single signal; diagram-design (2026-08-11, L4b) is a prior visual-output skill signal but targets diagrams (SVG/HTML), not office documents (PPTX); same-layer confirmation requires a second L4b skill whose primary artifact is a native office document format
