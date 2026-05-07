# Routine: Daily SEO Article Writer — Strategygame.org (v4)

## What this routine does

Write and publish 3 separate SEO articles for strategygame.org per run. Source titles, keywords, and briefs from the content plan spreadsheet. Track progress by updating the Status column after each article.

## Connectors

- **strategygame.org** (WordPress MCP)
- **Google Drive**
- **Composio** (Google Sheets)

## Before writing anything

1. Read the project context document: https://docs.google.com/document/d/15J-7AL9hjvEaPzW3CZTUUlKxIj3LFOPYOmrfktlZzYE/edit?usp=sharing
2. Load and follow the **mcp-web-seo-writing-eng** skill from this repository for all article writing rules.

## Spreadsheet details

- **Spreadsheet ID:** `1L4OnCL7ewMOCluDRUChu3zAiZ6vL2mMEMeXZJ4bXI70`
- **Sheet name:** discover via `GOOGLESHEETS_GET_SHEET_NAMES` (currently `Strategygame.org Content Plan – May 2026`)
- **Columns A–L:** #, Cluster, Primary Keyword, Secondary Keywords, SV, KD, Intent, Content Type, Length Tier, Title, Content Brief, Status
- **Status values:** `Todo` = pick this, `Draft` = skip, `Published` = skip

## Workflow

### Step 1 — Read sheet and pick 3 Todo rows

Use Composio `GOOGLESHEETS_BATCH_GET` to read all rows. Scan top to bottom. Select the first 3 rows where Status (column L) = `Todo`. Record exact row numbers for later Status updates.

If fewer than 3 Todo rows remain, write only what is available.

### Step 2 — For each row, sequentially

Complete ALL sub-steps for one article before starting the next:

**a) Extract from the row:** Title, Primary keyword, Secondary keywords, Content brief, Length tier, Content type, Intent, Cluster.

**b) Find a reference article:** Web search the primary keyword. Pick one reputable top result as reference. Do NOT copy from it. Do NOT use it as an external link in the finished article.

**c) Write the article following the mcp-web-seo-writing-eng skill.** This includes:
- Fact-checking against independent sources
- Learning the site voice from 3–5 existing posts via WordPress MCP
- Finding internal link candidates via WordPress MCP
- Drafting with keyword optimization per skill rules
- Placing links per the length-tier budget:
  - T1 (600–1,000w): 2 ext, 3 int, 1 home, 1 cat
  - T2 (800–1,200w): 3 ext, 4 int, 1 home, 1 cat
  - T3 (1,200–1,600w): 4 ext, 6 int, 1 home, 2 cats
  - T4 (1,600–2,200w): 4 ext, 8 int, 1 home, 3 cats
- Setting SEO meta data (title tag, description, slug)
- Running the self-check from the skill

**d) Create WordPress draft** via `wp_create_post` with status `draft`. Set title, HTML content, category, SEO title, meta description, slug. Record post ID.

**e) Update spreadsheet Status immediately.** Use Composio `GOOGLESHEETS_VALUES_UPDATE`:
- range: `'<sheet_name>'!L<row_number>`
- value_input_option: `RAW`
- values: `[["Draft"]]`
- Confirm updatedCells = 1 before moving to next article.

### Step 3 — Summary

For each article: row number, title, primary keyword, word count, tier, link counts, WP post ID, Status cell updated.

Overall: total written, Todo rows remaining, errors encountered.

## Rules

1. One row = one separate WordPress post. Never combine.
2. Only write rows with Status = Todo.
3. Always draft, never publish live.
4. Update sheet Status immediately after each article, before starting the next.
5. If a step fails, log error, skip to next article, report in summary.
6. Do not invent internal link URLs.
7. Do not use the reference article URL as an external link.
