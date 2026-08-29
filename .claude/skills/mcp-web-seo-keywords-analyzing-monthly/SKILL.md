---
name: mcp-web-seo-keywords-analyzing-monthly
description: "Use this skill when the user asks Claude to analyze a Semrush-style keyword research sheet on Google Drive and produce a monthly content plan for an MCP-connected website (referenced in the Project's instructions). Triggers include phrases like \"analyze this keyword file and create titles for this month\", \"build the monthly SEO plan from [Drive URL]\", or any request that pairs (a) a target website wired up via MCP, (b) a Google Sheet of keywords with seed, SEO keyword, search volume, and difficulty columns, and (c) intent to plan a month of content. The skill cleans and clusters keywords by seed, audits existing site content via MCP and the sheet's Status/Article link columns to avoid duplicates, pulls Google Search Console data (via Composio when connected) for striking-distance prioritization, scores keywords by opportunity adjusted for AI Overview click erosion, and outputs an American-English plan of new articles plus refresh slots, with titles, answer-first content briefs, and per-title keyword packs ready to feed the writing skills. Do NOT use for ad-hoc keyword research, non-English plans, or when no input keyword sheet is provided."
---

# MCP Web SEO Keywords Analyzing (Monthly) — 2026 methodology

## Purpose

Turn a monthly Semrush-style keyword research sheet into a prioritized, non-duplicating monthly content plan for an MCP-connected website: new articles plus refresh/consolidation slots, each with a primary + secondary keyword pack and an answer-first brief ready for `mcp-web-seo-writing-eng`.

All output is **American English**.

## Why the 2026 changes (context for judgment calls)

- ~68% of US Google searches end without a click; when an AI Overview appears, organic CTR drops ~60%. Pure definitional queries are increasingly zero-click; list/comparison/experience-driven queries retain clicks better.
- Google AI Mode uses **query fan-out** (one question → many sub-queries). Sites covering a topic's sub-questions deeply are ~161% more likely to be cited in AI Overviews. Depth per cluster now beats breadth across clusters.
- Google's scaled-content-abuse enforcement (March 2026 core update) hit mass-published thin AI pages with 50–80% traffic drops. Volume without differentiation is an active penalty. Every planned piece must have a distinct angle and real substance; refresh/consolidation of existing pages is a first-class alternative to new pages.

## Activation Inputs

1. **Target website (from Project instructions):** site, URL, MCP connector, audience, categories, monetization signal.
2. **Keyword research sheet:** Google Sheet with at least: Seed keyword, SEO keyword, Search volume, KD. May also have **Status** (Done/Todo), **Article link** (covering article URL), and Semrush extras (CPC, SERP features). Read the sheet via the Sheets API (Composio `GOOGLESHEETS_BATCH_GET`), never via Drive file export, which truncates large sheets.
3. **Search Console + GA4 (optional but preferred):** if Composio connections exist, pull last-90-day GSC queries and pages. Used for striking-distance boosts and refresh candidates. If unavailable, proceed without and say so.
4. **Month context:** default 30 days. Default volume: **60 new articles + up to 15 refresh slots** (2/day new + refreshes). The user can request the legacy 90-new pace; if they do, flag the scaled-content risk once and comply.

If a required input is missing, ask before proceeding. Do not invent keywords.

## Workflow

### Phase 1 — Read and clean the keyword sheet

1. Fetch ALL rows via the Sheets API (paginate ranges until an empty batch).
2. Map columns; confirm mapping with the user if names differ.
3. Clean: drop empty/malformed rows; **normalize seed columns** (if a section has seed = the keyword itself on every row, assign one shared seed and note it); **flag off-topic junk** (e.g., gift-card/coupon queries inside a games cluster) as `Skip` rather than deleting; note Semrush column spill into Status/Article link columns and clear it.
4. Report counts: total keywords, clusters, SV/KD distribution, junk flagged.

### Phase 2 — Audit coverage (sheet first, site second, GSC third)

1. **Sheet Status column is the primary dedup index** when maintained: rows already `Done` (with Article link) are covered; verify a sample against the live site.
2. Site audit via MCP (`wp_get_posts`, `wp_search`, `wp_get_categories`) for anything the sheet doesn't cover; note per-category article counts (thin categories are strategic priorities). Beware connector quirks (e.g., `wp_get_posts` returning only newest N — fall back to `wp_search` and prior plan tabs' Article link columns).
3. **GSC pull (if connected):** top queries and pages, 90 days. Derive: (a) *striking-distance queries* — impressions ≥ 50, position 8–25, no dedicated article → priority targets; (b) *refresh candidates* — existing pages with high impressions but position > 12 or CTR well below position average; (c) queries the site already wins (skip near-duplicates).

### Phase 3 — Build topic clusters (fan-out aware)

1. Group by seed; each cluster gets one **pillar** (broad, hub) and **cluster supporters** (sub-questions, comparisons, platform/audience variants). Merge overlapping clusters.
2. For each cluster, sketch the **fan-out map**: the sub-questions an AI would decompose the pillar query into (what is / best / vs / for <platform> / free / beginners / how to). Supporters should collectively cover the map — that coverage is what earns AI citations.
3. Tag intent per keyword: informational / commercial-investigation / transactional / navigational. Additionally tag **zero-click risk = high** for pure definitional or short factual queries (meaning, definition, "what is X" with an instant answer) — these can still be planned as sections inside a hub, but rarely as standalone articles.
4. **Volatile-variant collapse:** when a cluster is dozens of near-identical variants of one intent (e.g., "best decks arena 7/8/9…", monthly "best X <month year>"), plan ONE evergreen hub (optionally with per-variant sections) plus a scheduled-update note — never one article per variant.
5. **Live-service game guides** (Rise of Kingdoms, Whiteout Survival, etc.): plan hub-and-spoke (one main guide + spokes for major sub-systems), and mark the hub with an update cadence tied to game patches.

### Phase 4 — Score and prioritize

```
opportunity = SV × (1 − KD/100) × intent_weight × ctr_factor + boosts
```

- **intent_weight:** from the site's monetization signal (publisher/retention sites weight informational+commercial-investigation; affiliate weights commercial; e-commerce transactional).
- **ctr_factor:** 1.0 default; **0.5 for zero-click-risk-high queries or when the sheet's SERP-features column shows an AI Overview on an informational query**; 0.85 when an AI Overview shows on a commercial list query (lists still earn clicks).
- **boosts:** striking-distance match from GSC (large boost — the site already has proof of relevance); pillar/strategic value for a key cluster; thin-category fill (a subcategory with almost no content).
- **Difficulty bands:** ~60% KD 0–30, ~30% KD 30–60, ~10% KD 60+ as a default, adjusted to the site's authority (GSC average position is the reality check).
- **Cluster cap:** no single cluster over 30% of the plan unless the user asks for niche depth — but respect fan-out: it is better to finish one cluster's map than to open three clusters shallowly.

### Phase 5 — Select the plan (new + refresh)

1. Walk candidates by adjusted score, applying filters: sheet-Status/site dedup, internal cannibalization (one intent = one article), cluster caps, intent mix, zero-click-standalone exclusion.
2. Fill the refresh slots from Phase 2's refresh candidates: each refresh row names the existing URL, what to add (sections for striking-distance queries, FAQ, updated data, answer-first rewrite of the intro), and the queries it should capture.
3. If viable candidates run short, surface options: fewer titles, more refreshes, or an expanded sheet.

### Phase 6 — Titles and answer-first briefs

Title rules: primary keyword near the front; under ~60 chars where possible; house style casing; concrete promise; format variety; no template stamping; no AI-tell phrases; American English.

Brief rules (2–4 sentences, now AEO-aware): state the angle and audience, the 3–5 sub-questions from the cluster's fan-out map the article must answer, and the AEO requirements: **open each major section with a direct 40–60-word answer**, include an FAQ block with real query phrasings, keep claims specific and checkable, show a visible updated date. Specific enough that two articles in one cluster cannot converge.

### Phase 7 — Keyword packs

Per title: primary keyword; 2–4 secondary keywords (cluster siblings + fan-out sub-queries for H2/H3s); length tier (Tier 1 600–1,000 / Tier 2 800–1,200 / Tier 3 1,200–1,600 / Tier 4 1,600–2,200 for pillars); content type — `pillar`, `cluster`, `standalone`, or `refresh` (with target URL).

### Phase 8 — Self-check

- [ ] Agreed count of new + refresh rows; reason if short.
- [ ] No two rows share a primary intent; nothing duplicates covered content (per Status column AND site audit).
- [ ] No standalone article whose query an AI Overview fully answers; those live as sections/FAQs instead.
- [ ] Volatile variants collapsed into hubs; live-service hubs carry update cadence notes.
- [ ] Cluster fan-out maps reasonably covered; cluster/intent/KD distributions balanced.
- [ ] Every brief carries answer-first + FAQ instructions; titles pass the rules.

### Phase 9 — Output and write-back

1. **Default output: a new tab in the SAME spreadsheet**, named for the month (e.g., `Sep`), matching the established column order: `# | Cluster (seed) | Primary keyword | Secondary keywords | SV | KD | Intent | Content Type | Length Tier | Title | Content Brief | Category | Status | Article link`. Only create a separate spreadsheet if the user asks.
2. **Write back to the Keywords Research tab:** set Status = `Planned` on rows selected for this plan (and `Skip` on junk), so the research tab stays the single source of truth. When articles are later published, the writing workflow sets `Done` + Article link.
3. Handoff summary: counts (new/refresh), cluster breakdown, KD bands, intent mix, pillars flagged, GSC-boosted picks, junk flagged, tab name.

## Edge cases

- Missing/odd columns → confirm mapping; never guess.
- New site with no GSC history → skip boosts, lean pillar-heavy.
- Most candidates already covered → propose refresh-heavy month.
- Flat list with no seeds → cluster by similarity, confirm with user.
- Ambiguous intent → check the live SERP for that query.
- Non-English → decline; point to the language-specific skill.

## What this skill does not do

It does not write articles, pull keywords from Semrush directly, invent keywords beyond long-tail variants in packs, publish to the site, or handle non-English plans.
