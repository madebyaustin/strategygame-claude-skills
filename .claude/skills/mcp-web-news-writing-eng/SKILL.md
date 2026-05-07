---
name: mcp-web-news-writing-eng
description: Use this skill when the user asks Claude to write a news article for an MCP-connected website (referenced in the Project's instructions) based on a reference article URL the user provides at task start. Triggers include phrases like "write a news article for [site]", "rewrite this for our news section", "publish a news post about this on [site]", or any request that pairs (a) a target website already wired up via MCP with (b) a source article URL to base the new piece on. The skill produces an American-English news article that is fact-checked, stylistically matched to the site, SEO-clean (no keyword stuffing), and properly linked with internal and external links following strict embedding rules. Do NOT use this skill for evergreen blog posts, opinion pieces, product pages, landing pages, or any content where the user has not provided a specific source article URL to base the news on.
---

# MCP Web News Writing (English)

## Purpose

Produce a publication-ready English-language news article on a WordPress/CMS site connected via MCP, derived from a single reference URL the user supplies. The output must read like native editorial work for the target site, not a translated rewrite, not a summary, not a copy.

All article output is **American English**. Skill instructions below are also in American English.

---

## Activation Inputs

This skill expects two inputs to be present:

1. **Target website (from Project instructions):** The site name, URL, MCP connector name, target audience, content vertical/niche, tone, and any house style notes. Always read the Project instructions before writing.
2. **Reference article URL (from the user's opening message):** The single source the user wants the news piece based on. Treat this URL as a *starting point*, not as content to reproduce.

If either input is missing, ask the user for the missing piece before proceeding. Do not guess the site or invent a source.

---

## Workflow

Execute these phases in order. Do not skip phases.

### Phase 1 - Read the source

1. Fetch the reference URL with the appropriate fetch tool.
2. Extract: the core news event, the key facts (who/what/when/where/why/how), named entities, dates, numbers, quotes, and the article's approximate word count.
3. Note the angle the source took, so the rewrite can keep, adjust, or reframe it as appropriate for the target site's audience.
4. Record the source's word count; this anchors the length target in Phase 5.

### Phase 2 - Fact-check against independent sources

The point of this phase is to confirm the source is accurate before amplifying it.

1. Run web searches for 2-3 of the most load-bearing factual claims in the source (names, numbers, dates, quotes, event details).
2. Cross-reference against **reputable, independent outlets**: established wire services (Reuters, AP, AFP), major newspapers, recognized trade publications, official statements from named entities, government or regulatory pages where applicable.
3. Flag any of the following before writing:
   - A claim no other reputable outlet is reporting.
   - A claim other outlets contradict.
   - A quote that cannot be traced to its original speaker or context.
   - Numbers or dates that disagree across sources.
4. If a material fact cannot be verified, either omit it from the rewrite or attribute it carefully ("according to [source outlet]") rather than stating it as confirmed fact.
5. If the entire source appears unreliable (single-source claim, fabricated quotes, suspicious outlet), surface this to the user and ask how to proceed before writing.

The reputable sources used for verification will later become the candidates for external links in Phase 6.

### Phase 3 - Learn the target site's voice

Before drafting, sample the site so the new article reads like it belongs there.

1. Use the site's MCP tools (e.g., wp_get_posts, wp_search, wp_get_categories) to pull 3-5 recent published articles, ideally from the same category the new piece will land in.
2. Read those articles to absorb:
   - **Sentence rhythm** (short and punchy vs. flowing; how often sentences exceed 25 words).
   - **Headline conventions** (sentence case vs. title case; question headlines, list headlines, declarative headlines).
   - **Lead style** (hard news lead, anecdotal lead, nut graf placement).
   - **Use of subheads** (frequency, formatting, H2 vs. H3 patterns).
   - **Quote density and attribution style** ("said" vs. "stated"; placement of attribution).
   - **Numbers, dates, and units** (AP-style vs. site-specific conventions; 12-hour vs. 24-hour; mi/ft vs. km/m).
   - **Treatment of acronyms and jargon** on first reference.
3. The new article must match this voice.

### Phase 4 - Find internal link candidates

Build a candidate pool *before* writing.

1. Use MCP search tools (wp_search, wp_get_posts) to find existing articles on the site that genuinely relate to the topic.
2. Collect at least 6-10 candidates. The draft will use 3-5 of them.
3. For each candidate, note: title, URL, primary topic, and a short phrase from the draft it would naturally fit.
4. Identify the **homepage URL** and the **most relevant category archive URL**.

A candidate is only valid if a reader clicking it would get *more relevant content* on the topic they were just reading about.

### Phase 5 - Draft the article

#### Length
Match the source's word count within roughly +/-15%.

#### Structure
- **Headline**: clear, factual, in the site's headline convention. No clickbait.
- **Lead paragraph**: the most important facts up top (inverted pyramid). 1-3 sentences.
- **Body**: supporting facts, context, quotes, background. Short paragraphs (1-3 sentences each).
- **Closing**: forward-looking line, next step, or open question. No summary-style endings.

#### Writing rules
- **American English throughout.**
- **Concise, active prose.** Strip filler.
- **No copy-paste from the source.** Hard limit: any quoted material from the source must be under 15 words and must be attributed.
- **Original framing.** Do not mirror the source article's headline, lead, or section ordering.
- **Attribution.** Every non-obvious factual claim should be traceable to a source.
- **Voice match.** Apply what was learned in Phase 3.

### Phase 6 - Place links

#### Required link counts
- External links: 1-2.
- Internal links to articles: 3-5.
- Internal navigational links: 2 (homepage + category).
Total: 6-9 links across the article.

#### External link rules
- Never link to the source article the user provided as input.
- Use only reputable, independent outlets.

#### Internal link rules
- Anchor each internal link in a keyword or phrase that already belongs in the sentence.
- Each internal link must point to genuinely relevant content.
- Spread links across the body.

#### Anchor text prohibitions
- No "Click here," "Read more here," "See here," "look here"
- No bare URLs in the body
- No "this article," "this post," or "here" as anchors

### Phase 7 - SEO basics (no keyword targeting)

News articles do **not** use a designated SEO keyword. Apply only baseline practices:
- **Title tag:** under ~60 characters, factual.
- **Meta description:** 140-160 characters, active voice.
- **Slug/URL:** short, lowercase, hyphenated.
- **Heading hierarchy:** one H1, then H2/H3, no skipped levels.
- **Image alt text:** descriptive, not a keyword string.
- **Readability:** Short paragraphs, plain language.

### Phase 8 - Self-check before publishing

- [ ] Length within +/-15% of the source word count.
- [ ] No near-paraphrase of source. No quoted span over 15 words.
- [ ] All factual claims verified or attributed.
- [ ] Voice matches the site.
- [ ] American English throughout.
- [ ] 1-2 external links present, none pointing to the source URL.
- [ ] 3-5 internal article links present on contextually appropriate anchors.
- [ ] 1 homepage link and 1 category link present.
- [ ] No prohibited anchor phrases.
- [ ] No bare URLs.
- [ ] Headline, meta description, and slug set per Phase 7.
- [ ] Heading hierarchy is clean.

### Phase 9 - Publish or hand off

Default: wp_create_post with status draft. Always confirm with user before publishing live.

When handing off, summarize: headline, slug, word count, all links placed, any flagged facts, post status and post ID.

---

## Edge cases

- **Source URL paywalled or unreachable:** Ask for alternative.
- **Source is an aggregator:** Treat the upstream outlet as the real source.
- **Site has no relevant existing articles for internal linking:** Use what you can find. Never invent URLs.
- **Facts cannot be independently verified:** Narrow scope or pause and ask.
- **Project instructions and site's published voice disagree:** Default to published voice.
- **User asks for non-English:** Decline. This skill is English-only.

---

## What this skill does not do

- It does not write opinion pieces, editorials, sponsored content, or product reviews.
- It does not translate articles between languages.
- It does not optimize for a specified SEO keyword.
- It does not publish to live without explicit user confirmation.
- It does not fabricate sources, links, or quotes under any circumstances.
