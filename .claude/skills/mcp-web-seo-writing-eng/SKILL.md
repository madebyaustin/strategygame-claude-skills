---
name: mcp-web-seo-writing-eng
description: Use this skill when the user asks Claude to write an SEO-optimized article for an MCP-connected website (referenced in the Project's instructions), specifying one or more target SEO keywords (or a topic cluster) and a reference URL at task start. Triggers include phrases like "write an SEO article for [site] targeting [keyword]", "write an SEO post on [topic cluster] for [site]", or any request that pairs (a) a target website wired up via MCP, (b) one or more SEO keywords or a topic cluster, and (c) a source article URL. The skill produces an American-English article that is fact-checked, stylistically matched to the site, optimized for the keyword(s) without keyword stuffing, properly linked according to a length-based link budget, and complete with optimized meta data. Do NOT use this skill for breaking news, opinion pieces, sponsored content, or product pages, and do NOT use it when the user has not specified target SEO keywords.
---

# MCP Web SEO Writing (English)

## Purpose

Produce a publication-ready, SEO-optimized English-language article on a WordPress/CMS site connected via MCP, derived from a reference URL the user supplies and aimed at one or more target SEO keywords (or a topic cluster). The output must read like native editorial work for the target site, informative, useful to a real reader, and naturally optimized.

All article output is **American English**.

---

## Activation Inputs

1. **Target website (from Project instructions):** Site name, URL, MCP connector, target audience, niche, tone, house style notes.
2. **SEO keyword(s) (from user's opening message):** One primary keyword, or a topic cluster (primary/pillar + supporting/semantic keywords).
3. **Reference article URL (from user's opening message):** A single source the user wants the new piece based on.

If any input is missing, ask before proceeding.

---

## Workflow

### Phase 1 - Read the source

1. Fetch the reference URL.
2. Extract: core topic, key facts, named entities, dates, numbers, quotes, article's angle, approximate word count.
3. Note which subtopics the source covers.

### Phase 2 - Fact-check + SERP awareness

**Fact-check:**
1. Search for 2-3 key factual claims.
2. Cross-reference against reputable, independent outlets.
3. Flag unverified claims. Omit or attribute carefully.

**SERP awareness:**
1. Search the primary keyword and review top 3-5 ranking pages.
2. Note: typical content length, dominant search intent, recurring subtopics, common formats.
3. The new article's length and depth must meet or exceed what currently ranks.

### Phase 3 - Learn the target site's voice

1. Use MCP tools to pull 3-5 recent published articles from the same category.
2. Absorb: sentence rhythm, headline conventions, lead style, subhead patterns, quote density, numbers/dates/units treatment, acronym handling.
3. Match this voice in the draft.

### Phase 4 - Find internal link candidates

1. Use MCP search tools to find existing articles related to the primary keyword, cluster keywords, and subtopics.
2. Gather enough candidates to fill the link budget for the planned length tier.
3. Identify homepage URL and most relevant category archive URL(s).

### Phase 5 - Draft the article

#### Plan before drafting

Work through these five questions before writing:
1. **Search intent.** What is the reader trying to do or learn?
2. **Reader baseline.** What does the reader already know? Skip basics they don't need.
3. **Reader gap.** What would actually help them?
4. **Angle.** Pick one clear angle.
5. **Evidence plan.** What concrete examples, numbers, comparisons, or real scenarios will anchor the article?

#### Length and link tier

| Word count | Tier |
|---|---|
| 600-1,000 | 1 |
| 800-1,200 | 2 |
| 1,200-1,600 | 3 |
| 1,600-2,200 | 4 |

#### Structure

- **Title (H1 / SEO title tag)**: clear, includes primary keyword naturally, under ~60 chars.
- **Introduction**: opens with the topic and primary keyword in the first paragraph (within ~100 words).
- **Body**: organized into H2 sections (and H3 subsections). Subheads incorporate semantic variants where natural.
- **Conclusion**: points forward, not a sales pitch.

#### Keyword usage rules

- **Primary keyword:** In H1, SEO title tag, meta description, URL slug, first paragraph, and at least one H2. Repeat naturally beyond that.
- **Semantic variants and synonyms:** Use them freely.
- **Topic cluster keywords:** Each supporting keyword appears at least once. Most important ones 2-3 times.
- **Hard prohibition: keyword stuffing.** Don't repeat the keyword more than once per ~150 words on average.

#### Writing rules

- **American English throughout.** US spellings, US punctuation, US date format.
- **Concise, active prose.** Short paragraphs (1-3 sentences).
- **No copy-paste from the source.** Hard limit: any quoted material under 15 words, must be attributed.
- **Original framing.** Don't mirror the source's structure.
- **Voice match.** Apply what was learned in Phase 3.
- **Reader value first.** If a sentence exists only to host a keyword or link, cut it.

#### Sound human, not robotic

- Clear, direct, human tone. Use contractions where natural.
- Mix sentence lengths. Short sentences punctuate. Medium sentences carry the argument. Longer sentences add nuance.
- Start each section with the point. No generic setup lines.
- Every paragraph earns its place.
- Use concrete examples, specific details, numbers, comparisons, real scenarios.
- Replace vague adjectives with observable details.
- Replace marketing claims with plain explanations.
- Allow some imperfection in rhythm. The writing should feel edited, not sterilized.
- Vary section lengths. Vary heading patterns.
- Do not overuse rhetorical questions.
- Should not sound like a corporate blog, motivational speech, movie trailer, or LinkedIn post.

#### Format prohibitions

- No em dashes. Use periods, commas, or parentheses.
- No semicolons unless absolutely necessary.
- No emojis. No hashtags.
- No reflexive transitions ("Furthermore," "Moreover," "In addition").
- No bullet lists where paragraphs would feel more natural.
- No generic summary endings. The closing should give the reader something.
- No forced positivity. No fake profundity. No over-explaining obvious ideas.

#### AI-sounding phrases (never use any of these)

"Let's dive into", "In today's fast-paced world", "In the ever-evolving landscape", "It's important to note", "It's worth noting", "Whether you're X or Y", "This is not just X, it's Y", "Unlock the power of", "Unleash", "Game-changing", "Cutting-edge", "Seamless", "Robust", "Delve", "Tapestry", "Journey" (as metaphor), "Realm", "Navigate the complexities", "A testament to", "At the end of the day", "Ultimately" as lazy conclusion, "In conclusion" unless format requires it.

#### Substitute up

- Abstract claim -> specific evidence.
- Vague adjective -> observable detail.
- Marketing language -> plain explanation.
- Long introduction -> direct answer.
- Generic advice -> practical step.

### Phase 6 - Place links (length-based budget)

#### Link budget by length tier

| Tier | Words | External | Internal articles | Homepage | Category |
|---|---|---|---|---|---|
| 1 | 600-1,000 | 2 | 3 | 1 | 1 |
| 2 | 800-1,200 | 3 | 4 | 1 | 1 |
| 3 | 1,200-1,600 | 4 | 6 | 1 | 2 |
| 4 | 1,600-2,200 | 4 | 8 | 1 | 3 |

#### Distribution rules
- Spread links across the body. At most one link per ~150 words. No two links in the same sentence.
- Vary anchor text. Don't reuse the same phrase as anchor text more than once.
- Two adjacent links are a smell.

#### External link rules
- Never link to the source article URL.
- Use only reputable, independent sources.

#### Internal link rules
- Anchor each internal link in a keyword or phrase that already belongs in the sentence.
- Each internal link must point to genuinely relevant content.
- Use descriptive anchor text (2-6 words typically).
- Vary anchors across the article.
- Homepage and category links sit on natural phrases (site name, topic area phrases).

#### Anchor text prohibitions
- No "Click here," "Read more here," "See here," "look here," "check this out"
- No bare URLs in the body
- No "this article," "this post," or "here" as anchors
- No repeating exact-match primary keyword as anchor more than once

### Phase 7 - SEO meta data and on-page optimization

- **Title tag:** Includes primary keyword near front. Under ~60 chars. Compelling.
- **Meta description:** 140-160 chars. Active voice. Includes primary keyword once.
- **URL slug:** Short, lowercase, hyphenated. Includes primary keyword. 3-6 words.
- **Heading hierarchy:** One H1, then H2/H3, no skipped levels. Primary keyword in H1 and at least one H2.
- **Image alt text:** Descriptive. Primary keyword in featured image alt only if image depicts the keyword's subject.
- **Open Graph (if supported):** Mirror SEO title and meta description or use slight variants.
- **Schema markup (if site supports):** Article or BlogPosting schema with standard fields.
- **Readability:** Short paragraphs, short sentences, plain language.

### Phase 8 - Self-check before publishing

#### Voice and prose self-edit

Read the draft as a skeptical American reader:
- Delete any sentence that sounds like AI filler.
- Delete generic intros.
- Remove repeated phrasing.
- Flag any paragraph that states something obvious without adding a specific detail. Cut or specify.
- Replace remaining vague claims with examples.
- Remove hype.
- Remove em dashes.
- Sharpen the first 100 words.
- Make the final section useful, not just a recap.
- If it sounds too polished, flatten it. If too vague, add specifics. If it sounds like marketing, make it plain.

#### Structural checklist

- [ ] Word count within +/-10% of target. Link tier matches actual length.
- [ ] No near-paraphrases from source. No quoted spans over 15 words.
- [ ] All factual claims verified or attributed.
- [ ] Voice matches the site. American English throughout.
- [ ] Primary keyword in: H1, title tag, meta description, slug, first paragraph, at least one H2.
- [ ] No paragraph repeats keyword in near-identical phrasing.
- [ ] Topic cluster keywords each appear at least once.
- [ ] Link counts match the tier exactly.
- [ ] No external link points to the source URL.
- [ ] No link clustering. At most one link per ~150 words. No two links in the same sentence.
- [ ] No prohibited anchor phrases.
- [ ] No bare URLs.
- [ ] Anchor text is varied. No exact-match keyword anchor used more than once.
- [ ] Meta data fully set: SEO title, meta description, slug, OG fields (if applicable).
- [ ] Heading hierarchy clean. No skipped levels.
- [ ] Image alt text set on every image.
- [ ] No em dashes anywhere.
- [ ] No AI-tell phrases from the blacklist.
- [ ] No reflexive transitions used as filler.
- [ ] First 100 words are sharp and land on the point.
- [ ] Final section delivers something useful, not a recap.
- [ ] Section lengths and H2 patterns vary.

### Phase 9 - Publish or hand off

Default: wp_create_post with status draft. Always confirm with user before publishing live.

When handing off, summarize: headline (H1), SEO title tag, meta description, slug, word count, assigned link tier, primary keyword and cluster keywords with placement notes, all links placed (organized by type), any flagged facts, post status and post ID.

---

## Edge cases

- **Source URL paywalled or unreachable:** Ask for alternative.
- **Source is an aggregator:** Treat the upstream outlet as the real source.
- **Site has insufficient existing articles for internal linking at required count:** Surface to user with options: reduce length tier, accept fewer internal links, or pause until more content exists.
- **No clearly relevant category:** Use closest match, note to user.
- **User supplies cluster but no clear primary keyword:** Ask which is primary, or pick broadest and confirm.
- **Primary keyword's search intent doesn't match what user wants:** Surface the mismatch before writing.
- **Facts cannot be independently verified:** Narrow scope or pause and ask.
- **Top SERP results dramatically longer than source:** Default to SERP-calibrated length. Confirm new tier with user.
- **Project instructions and site's published voice disagree:** Default to published voice, flag discrepancy.
- **Non-English requested:** Decline. This skill is English-only.

---

## What this skill does not do

- It does not write breaking news, opinion pieces, sponsored content, or product/sales pages.
- It does not translate articles between languages.
- It does not optimize for keywords the user has not specified.
- It does not stuff keywords or build pages whose primary purpose is ranking rather than serving a reader.
- It does not publish to live without explicit user confirmation.
- It does not fabricate sources, links, citations, or quotes under any circumstances.
