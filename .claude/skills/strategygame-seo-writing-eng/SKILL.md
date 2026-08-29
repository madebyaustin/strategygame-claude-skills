---
name: strategygame-seo-writing-eng
description: "Write a complete, publication-ready SEO article for strategygame.org, including images, links, meta data, and a WordPress draft — or refresh an existing article when the plan row's Content Type is refresh. Use this skill whenever Austin asks to write an article for strategygame.org — by content plan row number (\"làm tiếp #6\", \"viết bài #12\", \"write article #7 from the June plan\"), by keyword (\"write an SEO article targeting best tower defense games\"), or by title from the Strategygame.org Content Plan 2026 sheet — and whenever he asks to refresh, update, or rework an existing strategygame.org article. Also trigger when he asks to \"test\" article production, redo a draft, or produce any non-news evergreen piece (ranking, guide, primer, review) for strategygame.org. The skill handles the full pipeline: plan-row intake, SERP research, fact-check, drafting in the site's voice, per-game images from Steam/App Store, length-based link budget, Rank Math meta, category assignment, and draft creation via the WordPress MCP. Do NOT use for breaking news (use mcp-web-news-writing-eng) or for other websites (this skill is hardwired to strategygame.org)."
---

# SEO Writing for Strategygame.org

## Purpose

Produce a publication-ready, SEO-optimized article on strategygame.org: researched, fact-checked, written in the site's voice, illustrated with per-game images, internally linked into its topic cluster, and delivered as a WordPress draft with full Rank Math meta. All output is American English.

This skill is hardwired to one site. Everything below — categories, voice, image pipeline, link conventions — is strategygame.org-specific.

## The rule that matters most

**Rules you verify with a script get followed. Rules you follow from memory get broken.**

This is measured, not theoretical. In one production session, every scripted check (word count, link budget, em dashes, AI-tell phrases) passed 100% of the time, and every unscripted rule (image size, block markup, appid verification, featured-image distinctness) was violated 100% of the time — including a wrong game's key art reaching a live page.

So: Phase 5 has a pre-write script, Phase 8b has a post-write script, and **both are mandatory**. Do not replace either with careful reading.

---

## Site profile (fixed facts)

- **Site:** Strategy Game Hub — https://strategygame.org (WordPress + Rank Math + LiteSpeed Cache, connected via Royal MCP).
- **Scope:** digital strategy games only — mobile (primary focus), PC, console, browser. Tabletop/board/card game articles exist as legacy content but no new tabletop content is planned. If a plan row or keyword implies physical board games, flag it to Austin instead of writing.
- **Audience:** American strategy gamers under ~40, casual mobile to hardcore PC. They know the genre. Don't over-explain basics, don't talk down.
- **Content plan:** Google Sheet "Strategygame.org Content Plan 2026" (ID `1L4OnCL7ewMOCluDRUChu3zAiZ6vL2mMEMeXZJ4bXI70`), one tab per month. Each row carries: #, Cluster, Primary Keyword, Secondary Keywords, SV, KD, Intent, Content Type, Length Tier, Title, Content Brief, Category, Status, Article link. When Austin references an article by number, that row is the work order.
  - **Row number ≠ sheet row.** Plan item #N sits on sheet row N+1 (a header row occupies row 1). Always read the row back and confirm the `#` column matches before writing or updating.
  - **Content Type decides the mode.** `pillar` / `cluster` / `standalone` → write a new article (the normal path below). `refresh` → do NOT create a new post; follow **Refresh mode**. Refresh rows carry Status `Refresh` (not `Todo`) so daily new-article routines skip them; they are worked when Austin asks for refreshes.

### Categories (use these exact IDs)

| Category | ID | Path |
|---|---|---|
| Guides | 11 | /guides/ |
| ├ 4X | 18 | /guides/4x/ |
| ├ Economic simulations | 19 | /guides/economic-simulations/ |
| ├ Grand Strategy | 16 | /guides/grand-strategy/ |
| ├ MOBA | 21 | /guides/moba/ |
| ├ Real-time Strategy | 13 | /guides/real-time-strategy/ |
| ├ Tactical Role-playing | 20 | /guides/tactical-role-playing/ |
| ├ Tower Defense | 17 | /guides/tower-defense/ |
| └ Turn-based | 15 | /guides/turn-based/ |
| News | 14 | /news/ |
| Rankings | 12 | /rankings/ |
| Reviews | 10 | /reviews/ |

Assignment convention: genre rankings get Rankings + the matching Guides subcategory (a tower defense ranking gets 12 + 17). Primers and tactical guides get Guides + subcategory. Game reviews get Reviews. The plan's Category column states the intended assignment; trust it. If a `categories` assignment errors, re-pull with `wp_get_categories` rather than guessing.

---

## Phase 0 — Verify the connector (do not skip)

Austin runs multiple WordPress sites through identically-named MCP tools (`wp_create_post` exists for every site). A reconnect once pointed this pipeline at the wrong site mid-session and images landed on a casino domain.

Before any write operation, call `wp_get_site_info`. Proceed only if the returned URL is `https://strategygame.org`. If it isn't, or if any tool returns a permission error, stop and tell Austin to reconnect — then verify again before resuming.

Re-verify at the start of every article in a multi-article session, not just once.

## Phase 1 — Intake

1. **A content plan row** ("làm tiếp #14"): primary keyword, secondaries, tier, title, brief, category all come from the row. The brief is the spec; the title is the working H1. Check the Content Type: `refresh` rows go to Refresh mode below.
2. **A keyword pack** stated directly in chat.
3. **Optional reference URL.** If provided, extract facts and angle, never copy phrasing (quoted spans under 15 words, attributed). If absent — the normal case — build from the brief plus Phase 2 research.

If the primary keyword is missing entirely, ask. Don't invent keywords.

## Refresh mode (Content Type = refresh)

A refresh row updates the live article named in its Article link column. Never create a new post for a refresh row — that ships duplicate content.

1. Run Phase 0, then **re-fetch the live post** with `wp_get_post` (find the ID via `wp_search` on the slug). Human edits — trimmed slugs, swapped images, tweaked titles — must survive; work from what is live, not from any earlier draft.
2. Read the brief: it names the GSC evidence (impressions, position) and the specific changes — typically an answer-first intro rewrite, refreshed picks, a Rank Math FAQ block if missing, and internal links from newer cluster articles.
3. Apply the standard editing rules: keep the existing Gutenberg block markup, change only the strings that need changing, never re-send the body as raw HTML. New sections use the block templates from Phase 5. New images follow Phase 6, verification included.
4. Fact-check any pick you keep (prices, availability) — a refresh that repeats stale facts is worse than no refresh.
5. Add or update a visible updated line near the top (e.g., `Updated September 2026`) so freshness is legible to readers and answer engines.
6. Keep the article's existing link total within the tier budget; add at most the links the brief asks for and remove any that died.
7. Re-run the **Phase 8b script** on the updated post. Fix FAILs before saving is considered done.
8. Update the plan row: Status = `Refreshed`, Article link unchanged (verify the permalink is still live), Title column updated only if the visible H1 changed.
9. Handoff per Phase 10, with a one-line diff summary of what changed instead of an appid list when no new images were uploaded.

## Phase 2 — Research and fact-check

**Treat the brief's game list as a hypothesis, never as fact.** Briefs are written months ahead and go stale. Real failures this has caught:

- A brief called for Ogre Battle, Super Conflict, and Fire Emblem from the Nintendo Switch Online SNES catalog. None are in the Western NSO library at all.
- A brief listed a game as having a "free tier" when it is a paid $9.99 release.
- A brief treated a sequel as "upcoming" when it had shipped eight months earlier.

Steps:

1. **SERP check:** search the primary keyword. Note what ranks and what the top results miss.
2. **Verify the brief's premises.** For catalog/service articles (Game Pass, NSO, PS Plus, storefront availability), pull the current official list. For "upcoming" articles, confirm nothing listed has already released.
3. **Fact-check load-bearing claims** (release states, platform availability, monetization, pricing) against official sources.
4. Keep the verified sources — they become external link candidates.

### Live-service and single-game guides (Whiteout Survival, Rise of Kingdoms, Clash Royale, Age of Origins, and similar)

These rows are guides about ONE game, so the ranking rules bend:

- The "three verifiable entries" floor applies to list/ranking articles only. For a single-game guide the equivalent gate is: the described systems must be verifiable against the CURRENT version of the game. Verify event names, hero/commander names, and mechanics against official patch notes, the game's official site or community wiki, and at least one recent community source. Live-service games change monthly; a guide describing a removed mechanic is a factual error.
- State the game version or season checked, and include a visible `Updated <Month Year>` line near the top. If the brief carries an update-cadence note, keep it in mind: these guides are expected to be refreshed on patches.
- Structure: task-oriented H2s instead of numbered entries. Each major H2 opens with the direct answer (the right formation, the right upgrade order) before the reasoning.
- Images: these are mostly mobile titles — use the App Store leg of the Phase 6 cascade or official press-kit art. The Steam-appid requirement applies only to games actually sourced from Steam.

### When the brief turns out to be wrong: fix it and keep going

Austin's standing instruction is to correct automatically and report afterwards, not to stop and ask.

**Auto-fix, no interruption — document in the handoff:** a named game is unavailable, delisted, mispriced, on the wrong platform, or misdescribed while the topic still supports three or more legitimate entries; or the brief calls something "upcoming" that already released. Swap the entry, correct the fact, continue.

**Auto-pivot the angle, keep the primary keyword:** when the brief's *premise* is wrong but the keyword still carries real search intent, rebuild the article around what is true and make the correction the hook. Conditions: at least three verifiable entries still exist, and the honest answer serves the searcher. Two worked examples:
- "SNES strategy games on Switch Online" — the brief's titles were absent from the service, so the article became the honest inventory of what is actually there, plus a straight answer that the real tactics live in the Genesis and GBA libraries.
- "Upcoming grand strategy games into 2027" — the headline sequel had already shipped, so the article led with the truth that the next 18 months are an expansion cycle and separated confirmed quarters from undated teasers.

If the pivot changes the working title, update the sheet's Title column to match.

**Only stop and ask when the article cannot be written honestly:** fewer than three verifiable entries exist (list articles); the fix would require changing the **primary keyword**; or the row is tabletop / out of scope.

## Phase 3 — Voice (site-calibrated)

- Experienced American strategy gamer with thousands of logged hours. Natural, relaxed, confident. Opinionated: if a game is mid, say so.
- One wry line per article is the sweet spot, never more than two.
- No fluff. Specifics over generalities: name the game, the mechanic, the patch, the price. Every ranking entry pairs a strength with a fair criticism.
- Short paragraphs (1–3 sentences). Headlines in title case. Ranking entries as numbered H2s ("1. League of Legends").
- **Leading with an inconvenient truth is on-brand.** When the honest answer is "this catalog is thin" or "most of what's coming is DLC," open with that.

Spot-check 2–3 recent published posts in the target category for drift, but the above takes precedence.

## Phase 4 — Internal link candidates

1. Pull candidates from the plan's Article link column and `wp_search`. **Only link to published posts** — never drafts, never a predicted URL. If a sibling from the same batch is still a draft, pick a different published candidate.
2. **Verify every internal URL is live.** Slugs change in review (`the-best-...` often trimmed to `best-...`). Confirm the current permalink with `wp_search` or `wp_get_post`. A wrong-slug internal link is the most common post-publish defect.
3. Prioritize cluster-mates.
4. Navigational links: homepage anchor on "Strategygame.org" or "StrategyGame" used naturally in-body; category anchors on natural phrases pointing at the paths in the category table. Never "click here."

## Phase 5 — Draft

### Length tiers

| Tier | Words | Use |
|---|---|---|
| T1 | 600–1,000 | narrow long-tail |
| T2 | 800–1,200 | standard cluster piece |
| T3 | 1,200–1,600 | bigger cluster piece / small pillar |
| T4 | 1,600–2,200 | full pillar |

The plan may write the tier as `T2` or `Tier 2`; both mean the same band. Write within ±10% (the FAQ is additional and excluded). Structure: one H1; intro landing the primary keyword in the first ~100 words; H2 sections (numbered H2s for ranking entries); a closing section giving a decision aid, never a recap; then the FAQ.

Entry count is not fixed. Four strong ranked entries beat five where the fifth is padding or lacks a legitimate image. Cover the rest in honorable mentions.

### Keyword rules

Primary keyword in: H1 (natural phrasing — reorder awkward Semrush word order), SEO title, meta description, first paragraph, at least one H2. Each secondary keyword appears at least once. Never more than one repetition per ~150 words.

### Writing rules (non-negotiable)

- American English. Contractions. Mixed sentence lengths. Start every section on the point.
- **Answer-first openers.** The intro's first two sentences directly answer the primary query (the verdict, the top pick, the straight answer) before any scene-setting. Each major H2 opens with its own direct answer in the first 40–60 words, then the reasoning. AI Overviews and answer engines lift the tidiest self-contained passage; give them one per section.
- Concrete specifics: prices, match lengths, roster counts, patch states. Specific, checkable claims earn citations; vague ones don't.
- **No em dashes.** **No semicolons.** No emojis. No reflexive transitions ("Furthermore," "Moreover"). No bullet lists where prose works. No generic summary endings.
- AI-tell blacklist: "dive into," "in today's fast-paced world," "ever-evolving landscape," "it's important/worth noting," "whether you're X or Y," "not just X, it's Y," "unlock," "unleash," "game-changing," "cutting-edge," "seamless," "robust," "delve," "tapestry," "journey" (metaphor), "realm," "navigate the complexities," "a testament to," "at the end of the day," lazy "ultimately," "in conclusion."
- If a sentence exists only to host a keyword or link, cut it.

### Always send Gutenberg block markup, never raw HTML

`wp_create_post` may convert raw HTML into blocks, but **`wp_update_post` stores exactly what you send**. Raw `<figure><img></figure>` loses the `wp-block-image` class, falls outside the theme's CSS, and renders at full intrinsic size — a 1920px screenshot then blows out of the column on desktop and breaks aspect ratio on mobile. This shipped to production once and had to be repaired across four live articles.

Send this on **both create and update**:

```html
<!-- wp:paragraph {"className":"ext-animate--on"} -->
<p class="ext-animate--on">Body text.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"className":"ext-animate--on"} -->
<h2 class="wp-block-heading ext-animate--on">Section Title</h2>
<!-- /wp:heading -->

<!-- wp:image {"className":"ext-animate--on"} -->
<figure class="wp-block-image ext-animate--on"><img src="{library-url}" alt="{description}"/><figcaption class="wp-element-caption">{one editorial line}. Image: {Studio/Publisher} via Steam</figcaption></figure>
<!-- /wp:image -->
```

### FAQ section (every article)

Close with a `Frequently Asked Questions` H2, then a Rank Math FAQ block of 5 Q&As after the closing section. Pick People-Also-Ask-style queries: the best pick, is it free, platform/availability, one beginner how-to, and a "games like X". Answers run 2–4 sentences in house voice, no em dashes or semicolons. At most one internal link across the whole FAQ, and the FAQ does not count against the link budget.

Where research contradicts a common assumption, make that a FAQ question and answer it directly ("Is Ogre Battle on Nintendo Switch Online?" → "No."). These win answer-engine citations.

Use the Rank Math FAQ block, not plain H3s — only the block emits FAQPage schema. Keep `ext-animate--on`.

```html
<!-- wp:heading {"className":"ext-animate--on"} -->
<h2 class="wp-block-heading ext-animate--on">Frequently Asked Questions</h2>
<!-- /wp:heading -->

<!-- wp:rank-math/faq-block {"questions":[{"id":"faq-1","title":"Question one?","content":"<p>Answer one.</p>","visible":true},{"id":"faq-2","title":"Question two?","content":"<p>Answer two.</p>","visible":true}],"className":"ext-animate--on"} -->
<div class="wp-block-rank-math-faq-block ext-animate--on"><div class="rank-math-faq-item"><h3 class="rank-math-question">Question one?</h3><div class="rank-math-answer"><p>Answer one.</p></div></div><div class="rank-math-faq-item"><h3 class="rank-math-question">Question two?</h3><div class="rank-math-answer"><p>Answer two.</p></div></div></div>
<!-- /wp:rank-math/faq-block -->
```

### PRE-WRITE CHECK (mandatory script, before creating the post)

Save the draft body to a file and run this. Fix and re-run until it prints all PASS. Do not eyeball it.

```python
import re
html = open('article.html').read()
tier_min, tier_max = 800, 1200     # set from the plan row
ext_q, int_q, home_q, cat_q = 3, 4, 1, 1   # set from the budget table
secondaries = ["keyword one", "keyword two"]  # from the plan row
primary = "primary keyword"

idx = html.find('Frequently Asked Questions')
body = html[:idx]
t = re.sub(r'<figcaption.*?</figcaption>', '', body, flags=re.S)
t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
t = re.sub(r'<[^>]+>', ' ', t)
words = len([w for w in re.split(r'\s+', t) if w.strip()])

links = re.findall(r'href="([^"]+)"', html)
ext = [l for l in links if 'strategygame.org' not in l]
home = [l for l in links if l.rstrip('/') == 'https://strategygame.org']
cat  = [l for l in links if re.search(r'strategygame\.org/(rankings|news|reviews|guides)/', l)]
inte = [l for l in links if 'strategygame.org' in l and l not in home and l not in cat]

bl = ["dive into","ever-evolving","worth noting","whether you're","not just","unlock",
      "unleash","game-changing","cutting-edge","seamless","robust","delve","tapestry",
      "journey","realm","navigate the complexities","testament","at the end of the day",
      "in conclusion"]
low = html.lower()

checks = [
  (f"words {words}",            tier_min <= words <= tier_max),
  ("no em dash",                html.count('—') == 0),
  ("no semicolon in prose",     body.count(';') == 0),
  ("no AI-tells",               not [p for p in bl if p in low]),
  (f"external {len(ext)}",      len(ext) == ext_q),
  (f"internal {len(inte)}",     len(inte) == int_q),
  (f"homepage {len(home)}",     len(home) == home_q),
  (f"category {len(cat)}",      len(cat) == cat_q),
  ("primary kw present",        primary.lower() in low),
  ("all secondaries present",   all(s.lower() in low for s in secondaries)),
  ("faq block present",         'wp:rank-math/faq-block' in html),
]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
```

Watch for false positives: "not justify" contains "not just", and a literal "realm" in alt text is fine.

## Phase 6 — Images

**In a ranking, every ranked entry gets its own image** inside its section (after the entry's first paragraph), plus a featured image. Guides get a featured image and 2–3 contextual screenshots.

### Asset sizes — get these right

| Asset | Size | Use |
|---|---|---|
| `screenshots[].path_full` | 1920×1080 | **in-body figures** |
| `library_hero.jpg` | 1920×620 | **featured image** (official key art) |
| `header.jpg` | 460×215 | **never use** — far too small |

**The featured image must not also appear in the body.** Use `library_hero.jpg` key art, and vary it across cluster articles so archives don't show duplicate thumbnails. If a game has no `library_hero`, fall back to a screenshot not used in the body.

### Sourcing cascade (all free, no accounts)

1. **Media library first.** `wp_get_media` for the game's name; reuse the existing attachment rather than re-uploading.
2. **Steam.** Fetch **`https://store.steampowered.com/api/appdetails?appids={id}&filters=screenshots`** — compact payload, just the screenshot URLs. Key art: `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{id}/library_hero.jpg`.
3. **Apple App Store** (mobile-only): `https://itunes.apple.com/search?term={name}&entity=software&limit=3`, fields `screenshotUrls` / `artworkUrl512`. Upscale by rewriting the size suffix (`406x228bb.jpg` → `2208x1242bb.jpg`).
4. **Neither store** (Nintendo-exclusive, Riot titles, delisted classics): Nintendo store pages are client-rendered and usually fail plain fetching. Use official publisher art from a related listing, or key art of a modern game in the same series, and **make the caption honest about it** (Wargroove art in an Advance Wars entry, captioned as the modern stand-in). Never use competitor blogs, never AI-generate game imagery.

### Verify the source before uploading — always

**Never guess a Steam appid from memory.** Guessed appids silently return a different game's art. This happened twice: `1085660` was assumed to be Gears Tactics and is actually Destiny 2 (that art reached production as a featured image), and a guessed Halo Wars appid returned a Train Simulator DLC.

Confirm the appid via an independent source — `WebSearch` for the game name plus "Steam appid" surfaces the store URL or a SteamDB entry — **before** `wp_upload_media_from_url`. A successful upload proves only that the appid exists, not that it is the right game.

**App Store images get the same discipline.** The iTunes search API matches loosely — confirm the result's `trackName` and `artistName` (publisher) match the intended game before using its `screenshotUrls`, and record `game = trackId, verified via apps.apple.com/...` just like an appid line. Mobile-only games have no Steam appid; the appid rule applies per-game to Steam-sourced art only.

**Record the verification.** For every game, keep `game name = appid (or trackId), verified via <URL>` and reproduce that list in the handoff. If you cannot produce the line, you did not verify it.

## Phase 7 — Link budget

| Tier | External | Internal articles | Homepage | Category | Total |
|---|---|---|---|---|---|
| T1 | 2 | 3 | 1 | 1 | 7 |
| T2 | 3 | 4 | 1 | 1 | 9 |
| T3 | 4 | 6 | 1 | 2 | 13 |
| T4 | 4 | 8 | 1 | 3 | 16 |

Hit the budget exactly (FAQ excluded). Spread links (~1 per 150 words, never two in one sentence, conclusion stays light). Anchors: 2–6 natural words, varied, exact-match primary keyword at most once. Prohibited: "click here," "read more," bare URLs, full post titles.

Do not go back and add reciprocal links between articles after a batch publishes. Each article links out within its own budget at write time, and that is the whole of it.

External conventions: official game/publisher sites, Steam store pages, platform holders, Liquipedia and Wikipedia for genre history, research outlets for skill/psychology claims. Never the reference URL itself, never competitor strategy-game blogs.

## Phase 8 — Create the post and set meta

1. `wp_create_post` with `status: draft`, the full **block-markup** body, an excerpt (1–2 sentences, house voice), and `categories` from the plan's Category column. The tool has no slug parameter — the slug derives from the title. Austin often adjusts slugs before publishing.
2. `wp_set_featured_image` with the key-art attachment ID.
3. `wp_update_seo_meta` (routes to Rank Math): SEO title (≤60 chars, keyword near the front), meta description (140–160 chars, keyword once, active voice, no quotes), `focus_keyword` = primary keyword, OG title/description.
4. **Never set `status: publish` without Austin's explicit confirmation** for that batch. A routine prompt that says so counts as confirmation.

Note: Rank Math's SEO score is only computed when a post is opened in the WordPress editor, so API-created posts show N/A. That is cosmetic and not a ranking signal. Never fake `rank_math_seo_score` via meta.

## Phase 8b — POST-WRITE CHECK (mandatory script, before publishing)

Read the created post back with `wp_get_post`, resolve the featured image URL from `_thumbnail_id`, and run this. **If anything prints FAIL, do not publish. Leave it as a draft and report which check failed.**

```python
import re
content = ...       # post content returned by wp_get_post
featured_url = ...  # media URL of _thumbnail_id
expected_figures = 4   # ranked entries with images, or planned figure count for guides

figures = content.count('<figure')
blocks  = content.count('wp-block-image')
srcs    = re.findall(r'<img src="([^"]+)"', content)
links   = re.findall(r'href="([^"]+)"', content)

checks = [
  ("every figure is a block",   figures == blocks == expected_figures),
  ("featured not reused in body", featured_url not in content),
  ("no 460px header art",       not any('header.jpg' in s for s in srcs)),
  ("no tiny steam assets",      not any('capsule' in s for s in srcs)),
  ("every img has alt",         content.count('<img') == content.count('alt="')),
  ("faq block survived",        'wp:rank-math/faq-block' in content),
  ("no draft preview links",    not any('?p=' in l for l in links)),
  ("no em dash",                content.count('—') == 0),
]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
```

The first three checks exist because each corresponds to a defect that reached a live page.

## Phase 9 — Update the content plan sheet

- **At draft time:** Status = `Draft`, Article link = `https://strategygame.org/?p={POST_ID}`.
- **After publishing:** Status = `Published`, Article link = the **real permalink read back from WordPress** via `wp_search` or `wp_get_post`. Never derive the URL from the title — Austin trims slugs (`best-strategy-games-you-can-actually-play-on-a-mac` became `best-strategy-games-for-mac`).
- **After a refresh:** Status = `Refreshed`, Article link unchanged.
- If the title changed from the plan, update the Title column too.
- In a multi-article run, write each row immediately after that article finishes, never batched at the end, so a crash partway through does not lose completed work.
- Verify by reading the rows back after writing.
- The Keywords Research tab is reconciled monthly by the planning skill; per-article write-back there is not required.

## Phase 10 — Hand off with evidence

The handoff must contain, per article:

1. Post ID, final title, status, URL.
2. Word count and tier.
3. **The PASS/FAIL output of both scripts** (Phase 5 and Phase 8b). Not a claim that they passed — the actual lines.
4. **The image verification list**: `game = appid (or trackId), verified via <URL>` for every game whose art was newly uploaded. For refreshes with no new images, a one-line diff summary instead.
5. Link counts by type.
6. **Any brief correction**: what changed from the plan and why, in one or two lines.
7. Anything that needs a human.

Keep prose short — the evidence blocks are the point. If a defect reached production, say so directly, explain the cause, state the fix, and name the rule that prevents a repeat. Do not bury it.

---

## Edge cases

- **Permission error mid-run:** stop, tell Austin to reconnect the strategygame.org connector, re-run Phase 0 before resuming. Work already prepared survives — save it rather than redoing it.
- **Wrong site detected in Phase 0:** report which site the connector points at and wait. Never write to it.
- **A planned game has no usable image anywhere:** use the honest-fallback options; if those fail, drop it to honorable mentions rather than shipping a ranked entry with no image.
- **The brief's game list is stale or wrong:** apply the Phase 2 ladder — correct and keep writing, report after. Only stop if fewer than three verifiable entries exist (list articles), the primary keyword would have to change, or the row is out of scope.
- **Fewer published internal-link candidates than the tier requires:** use what exists and note the shortfall.
- **Plan row implies tabletop/physical games:** out of scope — flag to Austin before writing.
- **A daily routine reaches a row with Status `Refresh` or Content Type `refresh`:** skip it and take the next `Todo` row — refreshes are a separate work stream, run on request via Refresh mode.
- **Editing an already-published article:** re-fetch the live post first so human edits (trimmed slugs, swapped images) are preserved, keep the existing block markup, and change only the strings that need changing. Never re-send the body as raw HTML. Re-run Phase 8b afterwards.
- **Adding an FAQ to an older article:** keep the visible H2 and replace any plain H3 FAQ with the Rank Math block. Check its internal links for wrong-slug breakage while you are there.
