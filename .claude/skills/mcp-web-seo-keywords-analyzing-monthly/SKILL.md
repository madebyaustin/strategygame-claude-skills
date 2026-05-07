---
name: mcp-web-seo-keywords-analyzing-monthly
description: Use this skill when the user asks Claude to analyze a Semrush-style keyword research sheet on Google Drive and produce a monthly content plan of 90 SEO article titles for an MCP-connected website (referenced in the Project's instructions). Triggers include phrases like "analyze this keyword file and create titles for this month", "build the monthly SEO plan from [Drive URL]", or any request that pairs (a) a target website wired up via MCP, (b) a Google Sheet of keywords with seed, SEO keyword, search volume, and difficulty columns, and (c) intent to plan a month of content (typically 90 titles for 30 days). The skill clusters keywords by seed, audits existing site content via MCP to avoid duplicates, scores keywords by opportunity (search volume vs difficulty), and outputs an American-English plan with titles, content briefs, and per-title keyword packs ready to feed the writing skills. Do NOT use for ad-hoc keyword research, non-English plans, or when no input keyword sheet is provided.
---

# MCP Web SEO Keywords Analyzing (Monthly)

## Purpose

Turn a monthly Semrush-style keyword research sheet into a content plan of 90 unique, prioritized, non-duplicating SEO article titles for an MCP-connected website. Each title comes with a primary + secondary keyword pack and a short content brief, ready to feed the writing skills (mcp-web-seo-writing-eng in particular).

All article titles, briefs, and plan output are **American English**.

---

## Activation Inputs

1. **Target website (from Project instructions):** Site name, URL, MCP connector, target audience, niche, content categories, and monetization signal.
2. **Keyword research sheet (from user's opening message):** A Google Sheet with at least four columns: Seed keyword, SEO keyword, Search volume, Keyword difficulty (KD, 0-100).
3. **Month context (implicit):** Default plan covers 30 days x 3 articles = 90 titles.

If any input is missing, ask before proceeding.

---

## Topic cluster method

A topic cluster is an SEO content structure where:
- A **pillar page** targets a broad, high-volume seed-level topic and serves as the hub.
- Several **cluster pages** target more specific, longer-tail keywords within that topic.
- Cluster pages link up to the pillar; the pillar links down to clusters. This builds topical authority.

Each unique seed keyword in the input sheet defines one cluster. The skill identifies which keyword should be the pillar (broad scope, high SV) and which are cluster pieces (more specific, lower KD).

---

## Workflow

### Phase 1 - Read the keyword sheet

1. Use Google Drive MCP tools to fetch the sheet.
2. Parse all rows. Confirm the four required columns exist.
3. Note: total keyword count, unique seeds, SV distribution, KD distribution.
4. Drop empty rows and obvious data errors. List anything dropped in the handoff summary.

### Phase 2 - Audit existing site content

1. Use the site's MCP tools (wp_get_posts, wp_search, wp_get_categories) to pull existing posts.
2. For each existing post, capture: title, slug, primary keyword if exposed, category, publish date.
3. Build a lookup index of "topics already covered" keyed on normalized keyword stems.
4. This index becomes the duplicate filter for Phase 5.

### Phase 3 - Build topic clusters

1. Group SEO keywords by their seed keyword. Each group is one candidate cluster.
2. Within each cluster, identify:
   - **Pillar candidate:** broadest scope, reasonable SV, achievable KD.
   - **Cluster supporters:** more specific keywords, subtopics, comparisons, how-tos, long-tail variants.
3. Tag every keyword with search intent: Informational, Commercial-investigation, Transactional, or Navigational.
4. Drop keywords that don't fit any cluster. Note what was dropped and why.

### Phase 4 - Score and prioritize keywords

#### Opportunity score (baseline formula)

For each keyword: opportunity = search_volume x (1 - KD/100)

#### Adjustments
- **Site authority.** New/low-DA sites weight low-KD keywords more heavily.
- **Strategic value.** A high-KD pillar keyword may still be worth picking for cluster authority.
- **Intent alignment.** Use the site's monetization signal from the Project.

#### Difficulty bands (rule of thumb)
- KD 0-30 (easy): ~60% of the 90 titles.
- KD 30-60 (medium): ~30%.
- KD 60-100 (hard): ~10%, typically pillars only.

#### Cluster balance
No single cluster takes more than 30% of the 90 titles unless user explicitly requests niche depth.

### Phase 5 - Select 90 non-duplicating keywords

1. Sort all candidates by adjusted opportunity score.
2. Walk the sorted list, picking keywords with these filters:
   - **Existing-content filter:** skip if the index from Phase 2 already covers this intent.
   - **Internal cannibalization filter:** skip if a keyword already picked targets the same intent.
   - **Cluster cap filter:** skip if the cluster has filled its monthly quota.
   - **Intent mix filter:** maintain a healthy mix per the site's monetization signal.
3. If the input sheet doesn't yield 90 viable candidates, surface this to the user with options.

### Phase 6 - Generate titles and content briefs

#### Title rules (American English)
- Includes the primary keyword naturally, ideally near the front.
- Under ~60 characters where the topic allows.
- Title case or sentence case to match the site's house style.
- Promises something concrete. No clickbait, no ALL CAPS, no emoji.
- Format variety across the 90: mix how-tos, listicles, guides, comparisons, explainers.
- No template repetition. Don't stamp out 30 articles all titled "Best X for Y in 2026."
- No AI-tell phrases ("dive into," "unlock," "ultimate guide" overused, "navigate the complexities," etc.).

#### Content brief rules
- 2-3 sentences. Plain prose.
- States the angle, the key points the article should cover, and who it serves.
- Specific enough that two articles in the same cluster can't end up writing the same thing.

### Phase 7 - Build keyword packs per title

For each title, output:
1. **Primary keyword** from the sheet row.
2. **Secondary keywords** (2-4 related keywords from the same cluster or plausible long-tail variants).
3. **Suggested length tier** (T1: 600-1000w, T2: 800-1200w, T3: 1200-1600w, T4: 1600-2200w).
4. **Content type** (pillar, cluster, or standalone).

### Phase 8 - Self-check

- [ ] Exactly 90 titles, or the agreed alternative from Phase 5 with reason.
- [ ] No two titles target the same primary keyword or the same primary intent.
- [ ] No title duplicates a topic already covered by existing site content.
- [ ] Cluster distribution is balanced (no cluster >30% unless user-approved).
- [ ] Difficulty distribution is realistic for the site's authority.
- [ ] Intent mix matches the site's monetization signal.
- [ ] Every title is in American English and follows the title rules.
- [ ] Every brief is 2-3 sentences and specific enough to differentiate.
- [ ] Every row has primary keyword, 2-4 secondary keywords, length tier, and content type.
- [ ] No AI-tell phrases in any title.
- [ ] Pillar pieces are flagged and not all bunched in week one.

### Phase 9 - Output to Drive

Create a new Google Sheet named [Site Name] Content Plan - [Month Year] with columns:
#, Cluster (seed), Primary keyword, Secondary keywords, SV, KD, Search intent, Content type, Length tier, Title, Content brief, Status

When handing off, summarize: total titles, cluster breakdown, difficulty band breakdown, intent mix, pillar pieces flagged, anything dropped, Drive link.

---

## Edge cases

- **Missing required columns:** Ask user to confirm column mapping.
- **Column names differ:** Map with user confirmation.
- **New site with few existing posts:** Duplicate filter still runs but rarely fires. Lean toward more pillar coverage.
- **Most candidates already covered:** Surface this. Options: refresh existing posts, request expanded keyword sheet, or accept a smaller plan.
- **No clear seeds (flat list):** Cluster the keywords by topic similarity yourself, confirm with user.
- **Unclear search intent:** Use SERP for the keyword as a tiebreaker.
- **User wants more or fewer than 90 titles:** Adjust. The 90 default is not a hard rule.
- **Non-English plan requested:** Decline. This skill is English-only.
- **Overlapping clusters:** Merge them before Phase 4, note the merge.

---

## What this skill does not do

- It does not write the articles themselves.
- It does not pull keyword data from Semrush directly.
- It does not invent keywords not in the input sheet (except as secondary keyword variants).
- It does not publish anything to the site.
- It does not handle non-English plans.
- It does not auto-adjust for 29-day or 31-day months.
