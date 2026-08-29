---
name: strategygame-news-writing-eng
description: Write a complete, publication-ready news article for strategygame.org from a single reference URL. Use this skill whenever Austin sends a source URL and wants it turned into a news post for strategygame.org — "write a news article from this," "rewrite this for our news section," "làm tin này," "viết bài news từ link này," or just a bare URL pasted with the intent to publish a news piece. The skill runs autonomously from the URL: it reads and fact-checks the source against independent outlets, checks the site for duplicate coverage, learns the house voice, writes a strategic-gamer-focused piece in natural human prose (no AI tells, no em dashes), sources a featured image, optimizes for both SEO and AEO (answer engines), links into the site's clusters, and creates a WordPress draft with Rank Math meta. Do NOT use for evergreen rankings/guides/reviews (use strategygame-seo-writing-eng), opinion pieces, sponsored content, or any site other than strategygame.org.
---

# News Writing for Strategygame.org (English)

## Purpose

Turn a single reference URL into a publication-ready news article on strategygame.org: fact-checked against independent sources, written in the site's voice, framed for strategy gamers, optimized for search and answer engines, illustrated, internally linked, and delivered as a WordPress draft with full Rank Math meta. All output is American English.

The piece must read like native editorial work by an experienced strategy gamer — not a translated rewrite, not a summary, not a reworded copy of the source. The reader should never be able to tell it started from one link.

**Design goal:** Austin sends a URL, nothing else. Everything below runs without further input unless a blocker forces a question.

---

## Site profile (fixed facts)

- **Site:** Strategy Game Hub — https://strategygame.org (WordPress + Rank Math + LiteSpeed Cache, connected via the strategygame.org MCP).
- **Scope:** strategy games across all platforms — mobile (primary focus), PC, console, browser. News covers announcements, updates, patch notes, releases, delistings, esports, acquisitions, and industry moves that matter to strategy players. If a source is about a non-strategy title with no strategy angle, flag it to Austin rather than forcing a piece.
- **Audience:** English-speaking, primarily American strategy gamers under ~40. Mix of casual mobile players and dedicated fans who've played everything from Civilization to mobile tower defense. They know the genre. Don't over-explain basics, don't talk down.
- **Monetization:** none. The only goal is content quality and time on site. Write to inform and keep them reading, not to sell.
- **Default post status:** `draft`. Never publish live without Austin's explicit confirmation.

### Categories (use these exact IDs)

| Category | ID | Path |
|---|---|---|
| News | 14 | /news/ |
| Guides | 11 | /guides/ |
| ├ 4X | 18 | /guides/4x/ |
| ├ Economic simulations | 19 | /guides/economic-simulations/ |
| ├ Grand Strategy | 16 | /guides/grand-strategy/ |
| ├ MOBA | 21 | /guides/moba/ |
| ├ Real-time Strategy | 13 | /guides/real-time-strategy/ |
| ├ Tactical Role-playing | 20 | /guides/tactical-role-playing/ |
| ├ Tower Defense | 17 | /guides/tower-defense/ |
| └ Turn-based | 15 | /guides/turn-based/ |
| Rankings | 12 | /rankings/ |
| Reviews | 10 | /reviews/ |

Every news piece gets the **News** category (ID 14). If the news is squarely about one genre (e.g., an RTS patch), also add the matching Guides subcategory so it surfaces in that cluster's archive. IDs can drift if categories are recreated — if a `categories` assignment errors, re-pull with `wp_get_categories` rather than guessing.

---

## Phase 0 — Verify the connector (do not skip)

Austin runs multiple WordPress sites through identically-named MCP tools (`wp_create_post` exists for every site). A reconnect on another project once pointed a pipeline at the wrong site mid-session, and images landed on a casino domain.

Before any write operation, call `wp_get_site_info`. Proceed only if the returned URL is `https://strategygame.org`. If it isn't, or if any tool returns a permission error ("requires additional permissions"), stop and tell Austin to reconnect the strategygame.org connector — then verify again before resuming. Never assume a reconnect restored the right site.

---

## Phase 1 — Read the source

The only required input is the reference URL. If it's missing, ask for it. Don't invent a source.

1. Fetch the reference URL with the appropriate fetch tool. If it's paywalled, JS-rendered, or unreachable, see Edge cases.
2. Extract the core news event and the full who/what/when/where/why/how: named entities (games, studios, publishers, platforms, people), exact dates, version/patch numbers, prices, player counts, and any direct quotes.
3. **Record the source's publication date and time.** News is perishable — this anchors the freshness handling in Phase 5.
4. Note the angle the source took, so the rewrite can keep, sharpen, or reframe it for strategy gamers.
5. Treat the URL as a *starting point*, never as content to reproduce.

## Phase 2 — Verify, then widen the reporting

The point is twofold: confirm the source is accurate before amplifying it, and gather enough independent reporting that the final piece is genuinely yours, not a single-source echo.

1. Web-search the 2–3 most load-bearing claims (names, numbers, dates, quotes, the event itself).
2. Cross-reference against **reputable, independent outlets**: wire services (Reuters, AP, AFP), major newspapers, recognized games trade press (e.g., established outlets that cover the genre), official studio/publisher statements, patch notes, store pages, and regulatory/government pages where relevant.
3. **Pull real detail from these corroborating sources into the article**, not just a yes/no verification. A second source often supplies context, a reaction, a number, or a timeline the original missed. Synthesize across all of them — that is what makes the piece read like reporting rather than a rewrite.
4. Flag before writing: a claim no other reputable outlet reports; a claim others contradict; a quote that can't be traced to its speaker; numbers or dates that disagree across sources.
5. If a material fact can't be verified, omit it or attribute it carefully ("according to [outlet]") rather than stating it as confirmed.
6. If the whole source looks unreliable (single-source claim, fabricated quotes, suspicious outlet), surface it to Austin and ask how to proceed before writing.

The reputable sources used here become the external link candidates in Phase 6.

## Phase 3 — Check for duplicate coverage (do not skip)

Before drafting, confirm the site hasn't already covered this exact event — republishing the same story splits authority and cannibalizes rankings.

1. Use `wp_search` and `wp_get_posts` (News category) on the core entities and the event to find any existing post on the same news.
2. Decision:
   - **No existing coverage** → write a fresh piece (the normal case).
   - **Existing piece, and this source adds genuinely new developments** → tell Austin, and offer to update the existing post (`wp_update_post`) instead of creating a near-duplicate. Don't update without confirmation.
   - **Existing piece, no new development** → stop and tell Austin; don't write a duplicate.
3. Any related-but-distinct existing posts found here are strong internal-link candidates for Phase 4.

## Phase 4 — Internal link candidates

Build the pool before writing, so links sit naturally during drafting instead of being bolted on.

1. With `wp_search` / `wp_get_posts` (by tag/category), find published posts that genuinely relate to: the same game/studio/event, prior coverage, the affected genre, or concepts the piece will reference in passing.
2. Collect 6–10 candidates; the draft uses a subset. **Only link to published posts** — never drafts, never a predicted URL.
3. For each: note title, URL, topic, and a phrase in the draft it would fit.
4. Identify the homepage and the most relevant category archive (News, or the relevant Guides subcategory) for the two navigational links.

A candidate is valid only if a reader clicking it lands on *more relevant content*. If no organic anchor exists, don't force it.

## Phase 5 — Draft the article

### Voice (site-calibrated — write to this directly)

- Experienced American strategy gamer with thousands of logged hours. Natural, relaxed, confident. Not corporate, not academic, not hype-bro.
- Friendly but opinionated: if a release looks thin or a monetization change is a cash grab, you can say so, while keeping news reporting fair and attributed.
- One wry or dry line per article is the sweet spot. Never more than two. Dry wit, not stand-up.
- No fluff. Specifics over generalities: name the game, the patch number, the price, the platform, the date. Contractions on. Mixed sentence lengths.
- Spot-check 2–3 recent published News posts for current rhythm before writing, but this summary takes precedence over generic news-wire patterns.

### The strategic-gamer angle (what makes this *our* news)

Wire copy reports the event. We report **why a strategy player should care.** Every piece should land, somewhere in the body, the tactical/meta/competitive implication: what this changes for how the game is played, what it signals for the genre, whether it's worth a returning player's time. That angle is the difference between reprinting news and owning it.

### Length (scaled to the story, not the source's word count)

Pick the target by what kind of news it is. Never pad to hit a number, and never truncate so hard that real content is lost.

- **Single-event news** (one announcement, a delisting, an acquisition, a single balance change): **450–800 words.** Tight, inverted-pyramid.
- **Patch / update / season roundups** (multiple new features, modes, or systems in one drop): **1,000–1,500 words.** These are reference pieces readers return to, and completeness is the value (time on site, plus SEO/AEO snippet coverage). Cover every meaningful change, not just the headline two.

**When the source has structured data or an FAQ, that's a signal to match it, not trim it:**

- Reproduce any **reward tables, tier tables, or price lists** the source carries as on-page HTML tables. They earn featured snippets and give readers a reason to come back.
- Include an **FAQ section** (H2 "FAQ" with H3 questions) on any patch/update roundup. Answer each question in a self-contained first sentence containing the question's key terms — this is the single strongest AEO pattern. Reword the questions; don't copy the source's phrasing.
- Don't drop whole feature sections to save length. If the patch adds a mode, an event, a card, and a progression change, each gets its own H2.

The source's length is a floor for completeness on roundups, never a ceiling to distill toward.

### Structure (built for readers *and* answer engines)

- **Headline** — clear, factual, in the site's News convention (title case). Front-load the entity and the event. No clickbait, no all-caps, no editorializing.
- **Answer-first lead** — the first 1–2 sentences state what happened, who's involved, and when, in plain declarative language. This is the inverted-pyramid lead *and* the passage most likely to be quoted by Google's AI Overviews and other answer engines, so make it self-contained and factual. Land the core entity + event in the first ~30 words.
- **Body** — supporting facts, context, quotes, and the strategy angle, in short paragraphs (1–3 sentences). Use H2 subheads for major beats. Each H2 should read as a clear, scannable claim a reader (or a model) could lift on its own.
- **Key takeaways** — a short "What this means for players" or 2–4 line bullet recap near the end. This serves skimmers and gives answer engines a clean, extractable summary block. (Bullets are allowed here specifically; keep the body in prose.)
- **Closing** — a forward-looking line: what to watch next, the next patch/date, an open question. Never a summary that restates the lead.

### AEO (answer-engine optimization)

Beyond the answer-first lead and takeaways:

- Write so individual sentences are **true and complete out of context** — answer engines quote sentences, not paragraphs. Avoid "this" and "it" carrying meaning across sentence boundaries in key factual lines.
- Name entities explicitly and consistently (full game/studio name on first mention per section, not just pronouns).
- Where the news naturally raises a reader question ("When does it release?", "Is it free?", "What changed?"), answer it directly in a sentence that contains the question's key terms.
- Use real dates ("June 11, 2026"), not "today" or "this week," in factual statements — extracted snippets lose the publish context.

### Writing rules (non-negotiable)

- **American English throughout.** "Color," not "colour." "Toward," not "towards." US punctuation (periods inside quotation marks), US dates (Month Day, Year).
- **No copy-paste from the source.** Restate every fact in original structure and word choice. Any quoted span from the source is under 15 words and attributed. Don't mirror the source's headline, lead, or section order.
- **Concise, active prose.** Strip filler. "In order to" → "to." "Due to the fact that" → "because." Cut redundant adjectives.
- **No em dashes.** Use periods, commas, or parentheses. **No semicolons.** No emojis. No reflexive transitions ("Furthermore," "Moreover," "Additionally").
- **AI-tell blacklist, strike on sight:** "dive into," "in today's fast-paced world," "ever-evolving landscape," "it's important/worth noting," "whether you're X or Y," "not just X, it's Y," "unlock," "unleash," "game-changing," "cutting-edge," "seamless," "robust," "delve," "tapestry," "journey" (metaphor), "realm," "navigate the complexities," "a testament to," "at the end of the day," lazy "ultimately," "in conclusion."
- **Attribution.** Every non-obvious factual claim is traceable — named in-text ("according to Reuters") or via a Phase 6 external link.
- If a sentence exists only to host a keyword or a link, cut it.

## Phase 6 — Featured image (every article, before the post is created)

News posts need a featured image so they render properly in archives, the homepage feed, and social cards. One featured image is required; 1–2 in-body images are welcome when a relevant screenshot adds something.

### Sourcing cascade (all free, no accounts)

1. **Media library first.** Search existing attachments (`wp_get_media`) for the game's name and reuse the existing URL rather than re-uploading — games recur across posts and should share a file.
2. **Steam** (most PC games): resolve appid via `https://steamcommunity.com/actions/SearchApps/{name}`, then `https://store.steampowered.com/api/appdetails?appids={id}&filters=basic,screenshots`. Verify the returned `name` matches the intended game — search returns sequels and impostors. Use `header_image` for the **featured image** (key art), and `screenshots[].path_full` (1920×1080) for any **in-body** shots. Never use `header_image` (460×215) for an in-section figure — it's too small.
3. **Apple App Store** (mobile games): `https://itunes.apple.com/search?term={name}&entity=software&limit=3`, fields `screenshotUrls` / `artworkUrl512`. Upscale by rewriting the size suffix (e.g., `406x228bb.jpg` → `2208x1242bb.jpg`). Some publishers (Moonton, for one) ship zero screenshots — fall back to the icon at `1024x1024bb` or official key art from a sibling listing, with an honest caption.
4. **Neither store** (Riot PC titles, delisted classics): official publisher art from a related official listing, with an honest caption. Never pull files from competitor gaming blogs. Never AI-generate anything presented as game imagery.

### Upload and markup

Upload each new image with `wp_upload_media_from_url`: descriptive hyphenated filename, alt text describing what's actually shown (factual, not a keyword string), and a credit caption. In-body figures:

```html
<figure><img src="{library-url}" alt="{description}" /><figcaption>{one editorial line}. Image: {Studio/Publisher} via Steam|App Store</figcaption></figure>
```

Set the featured image with `wp_set_featured_image` after the post is created. WebP conversion is handled server-side by LiteSpeed.

## Phase 7 — Place links

Every link is an editorial decision, not a checkbox.

### Link budget (standard news item)

| Type | Count | Notes |
|---|---|---|
| External | 1–2 | Reputable independent sources that corroborate or expand a fact. |
| Internal articles | 3–4 | Published posts on the same game/genre/prior coverage. |
| Homepage | 1 | Anchor on "Strategygame.org" / "StrategyGame" used naturally. |
| Category | 1 | News archive, or the relevant Guides subcategory. |

Total ~6–8. Spread them across the body (~1 per 150 words max, never two in one sentence, closing stays light).

### Rules

- **Never link to the source URL Austin provided.** It's the origin, not a citation.
- External links go to wire services, major papers, recognized trade press, official studio/publisher/store pages, Liquipedia/Wikipedia for genre history, or regulatory pages. Never a competitor strategy-game blog.
- Internal anchors sit on a keyword or phrase that already belongs in the sentence; the sentence must read naturally without the link. Each internal link points to genuinely relevant content. Spread them; don't cluster.
- Navigational anchors: homepage on the site name in-body; category on a natural phrase ("the latest strategy game news," "our RTS coverage"), pointing at the paths in the category table.
- **Anchor text — avoid:** "click here," "read more here," "learn more," "see here," "this article," bare URLs, anchors that cram the full target title into one sentence. **Do:** anchor on the entity/concept (2–6 natural words), vary anchors, use exact-match phrasing at most once.

## Phase 8 — Create the draft and set meta

1. `wp_create_post` with `status: draft`, the full HTML body (figures included), an excerpt (1–2 sentences, house voice), and `categories` set to News (14) plus any relevant subcategory ID. The tool has no slug parameter — the slug derives from the title, so keep the title clean and descriptive of the event (no date in the slug unless the URL pattern requires it).
2. `wp_set_featured_image` with the key-art attachment ID.
3. Tags: add 3–6 relevant tags (game title, studio, genre, platform) via `wp_add_post_terms` so the piece threads into tag archives.
4. `wp_update_seo_meta` (routes to Rank Math):
   - **SEO title** ≤ 60 chars, event and key entity front-loaded.
   - **Meta description** 140–160 chars, active voice, summarizing what's reported, no clickbait, no question-only-answered-by-clicking.
   - **No focus keyword.** News pieces do not target a keyword — leave it empty. They rank on freshness, authority, and links, not keyword density.
   - OG title/description: light social-tuned variants.
5. Never set `status: publish` without Austin's explicit confirmation.

## Phase 9 — Self-check, then hand off

Verify before handoff. Fix any failure first.

- [ ] Every load-bearing fact verified in Phase 2 or attributed in-text; no contested fact stated as confirmed.
- [ ] Not a duplicate of existing site coverage (Phase 3 cleared).
- [ ] Answer-first lead lands entity + event in the first ~30 words; "What this means" takeaways present.
- [ ] Key factual sentences read true and complete out of context (AEO); real dates, not "today."
- [ ] Strategic-gamer angle is explicit somewhere in the body.
- [ ] Length matches the site's News depth; no padding, no lost facts.
- [ ] No near-paraphrase of any source sentence; no quoted span over 15 words from the source; headline/lead not mirrored from the source.
- [ ] American English; no em dashes, no semicolons, no AI-tell phrases.
- [ ] Featured image set, with alt + credit; any in-body figure uses `path_full`, not `header_image`.
- [ ] Links match the budget: 1–2 external (none to the source URL), 3–4 internal articles (published only), 1 homepage, 1 category; no prohibited anchors; no bare URLs.
- [ ] Categories (News + any subcategory), tags, SEO title, meta description set; focus keyword left empty.
- [ ] Heading hierarchy clean: one H1, then H2/H3, no skipped levels.

Handoff summary (keep it short — Austin reviews the draft itself): headline and slug; word count and the source's word count; the reporting sources used and any facts flagged in Phase 2 with how they were handled; every link placed by type with anchor and target; featured image source (new vs. reused); post status and post ID/preview URL.

---

## Edge cases

- **Source paywalled / JS-rendered / unreachable:** if a plain fetch returns a shell or a paywall, escalate to the Chrome reader tools to get the rendered text; if still blocked, tell Austin and ask for an alternative source or the article text. Never work around fetch restrictions with bash/curl.
- **Source is an aggregator citing another outlet:** treat the upstream outlet as the real source and verify there.
- **Source's facts can't be independently verified:** don't write on contested facts. Narrow to what's confirmed, or pause and ask.
- **Stale source:** if the source predates a newer development the corroborating reporting reveals, report the current state and note the update, rather than reprinting old news as new.
- **No relevant existing posts for internal links:** use what exists; if the site has fewer than 3 relevant published posts, surface it and ask how to proceed. Never invent internal URLs.
- **Permission error mid-run:** stop, tell Austin to reconnect the strategygame.org connector, re-run Phase 0. Save prepared text/image URLs rather than redoing them.
- **Wrong site detected in Phase 0:** report which site the connector points at and wait. Never write to it; clean up anything accidentally written.
- **Source is a non-strategy game with no strategy angle:** flag to Austin instead of forcing a piece.
- **Request is for a language other than English:** this skill is English-only. Decline and point to the appropriate language-specific skill.

## What this skill does not do

- Evergreen rankings, guides, primers, or reviews (use **strategygame-seo-writing-eng**).
- Opinion pieces, editorials, sponsored content, product pages.
- Translation between languages.
- Keyword-targeted SEO (news targets no focus keyword).
- Publishing live without explicit confirmation.
- Fabricating sources, links, quotes, or images under any circumstances.
