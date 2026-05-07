# Claude Skills Repository — Strategy Game Content Automation

This repository contains custom Claude skills for automated content creation on strategy game websites.

## Available skills

- **mcp-web-seo-writing-eng** — Write SEO-optimized articles from a keyword pack and reference URL.
- **mcp-web-news-writing-eng** — Write news articles from a reference URL (no keyword targeting).
- **mcp-web-seo-keywords-analyzing-monthly** — Analyze a Semrush keyword sheet and produce a monthly 90-title content plan.

## General rules (apply to all skills)

- All content output in American English.
- Always read the project context document before writing. The URL is provided in the routine prompt.
- Default publish status: `draft`. Never publish live without explicit confirmation.
- Always check existing site content via MCP before writing or planning, to avoid duplication.
- Do not fabricate internal link URLs. Only link to posts confirmed to exist on the site via MCP.
