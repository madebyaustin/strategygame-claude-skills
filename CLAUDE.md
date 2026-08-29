# Claude Skills Repository — Strategy Game Content Automation

This repository contains custom Claude skills for automated content creation on strategy game websites. Synced with the account skills on 2026-08-30.

## Available skills

Site-specific (strategygame.org — used by the daily routine):

- **strategygame-seo-writing-eng** — Write a publication-ready SEO article for strategygame.org (rankings, guides, primers, reviews), or refresh an existing article when the plan row's Content Type is `refresh`. Includes the mandatory Phase 5 pre-write and Phase 8b post-write check scripts, live-service single-game guide rules, and Steam appid / App Store trackId image verification.
- **strategygame-news-writing-eng** — Write a news article for strategygame.org from a single reference URL, fact-checked and AEO-optimized.

Generic (multi-site, MCP-connected):

- **mcp-web-seo-writing-eng** — Write SEO-optimized articles from a keyword pack and reference URL.
- **mcp-web-news-writing-eng** — Write news articles from a reference URL (no keyword targeting).
- **mcp-web-seo-keywords-analyzing-monthly** — Analyze a Semrush keyword sheet and produce a monthly content plan (2026 methodology: GSC striking-distance boosts, AI Overview CTR discounts, query-fan-out clustering, refresh slots, scaled-content guardrails).

## Content plan sheet conventions (all skills and routines depend on these)

- Sheet: "Strategygame.org Content Plan 2026" (ID `1L4OnCL7ewMOCluDRUChu3zAiZ6vL2mMEMeXZJ4bXI70`). Tabs: `Keywords Research` + one tab per month (May, Jun, Sep, ...).
- Plan item #N sits on sheet row N+1 (row 1 is the header). Always read a row back and confirm the `#` column before writing.
- Status values in monthly tabs: `Todo` (to write), `Draft`, `Published`, `Refresh` (refresh work stream — daily routines must skip these), `Refreshed`.
- Status values in Keywords Research: `Todo`, `Done` (+ Article link), `Planned`, `Skip`.

## General rules (apply to all skills)

- All content output in American English.
- For strategygame.org work, the site context (voice, audience, categories, image and link conventions) is embedded in the strategygame-* skills themselves — no external context document is needed. For the generic mcp-web-* skills, read the project context document whose URL is provided in the task or routine prompt.
- Default publish status: `draft`. Never publish live without explicit confirmation (a routine prompt that grants standing confirmation counts, subject to its safety gate).
- Always check existing site content via MCP before writing or planning, to avoid duplication.
- Do not fabricate internal link URLs. Only link to posts confirmed to exist on the site via MCP.
