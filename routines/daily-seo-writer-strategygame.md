# Daily SEO writer routine — strategygame.org (v6, 2026-08-30)

Runs daily via Claude Code routines. 3 articles per run (reduced from 4 to afford the editorial pass). Requires connectors: strategygame.org (WordPress MCP), Google Drive/Sheets, Composio.

---

Run the daily strategygame.org article batch. Write 3 articles and publish them.
This instruction is my standing confirmation to publish. The strategygame-seo-writing-eng
skill normally requires explicit approval before setting status to publish. For this
routine you have it, subject to the safety gate in step 8.

1. VERIFY THE CONNECTOR FIRST.
   Call wp_get_site_info. Proceed only if the URL is exactly https://strategygame.org.
   If it is anything else, or if any WordPress tool returns a permissions error, stop
   immediately, write nothing, and report the mismatch. Do not try to fix it yourself.

2. PICK THE ROWS.
   Open the Google Sheet "Strategygame.org Content Plan 2026"
   (ID: 1L4OnCL7ewMOCluDRUChu3zAiZ6vL2mMEMeXZJ4bXI70).
   Use the tab for the current month. If that tab has no rows with Status = Todo,
   use the most recent tab that does, and say which tab you used.
   Take the first 3 rows with Status = Todo, in ascending order of the # column.
   Skip any row whose Status is Refresh or whose Content Type is refresh — refresh
   rows are a separate work stream and are never part of this routine.
   Remember: plan item #N sits on sheet row N+1, because row 1 is the header.
   Read each row back and confirm the # column matches before you write anything.

3. WORK STRICTLY ONE ARTICLE AT A TIME.
   Finish article 1 completely — research, write, check, editorial pass, publish,
   update the sheet — before starting any research for article 2. Do not gather
   material for several articles up front. Keep each article self-contained so
   context stays manageable across all three.

4. WRITE EACH ARTICLE WITH THE SKILL.
   Use the strategygame-seo-writing-eng skill and follow it end to end, including both
   mandatory scripts: the Phase 5 pre-write check and the Phase 8b post-write check.
   Follow its Phase 2 ladder when the brief is wrong: correct it and keep writing.
   For single-game live-service guides (Whiteout Survival, Rise of Kingdoms, Clash
   Royale, and similar), follow the skill's live-service guide rules: verify mechanics
   against the current version of the game and include a visible Updated line.
   Do not pause for my approval on lineup or angle changes.
   Be economical with context: use filters=screenshots on Steam calls, and do not
   reprint full article HTML except when actually sending it to WordPress.

5. EDITORIAL PASS — after Phase 8b prints all PASS, before publishing.
   The batch is 3 articles instead of 4 precisely to afford this step. Read the
   created post back once, top to bottom, and judge what the scripts cannot:
   - the first two sentences directly answer the primary query, no throat-clearing
   - every ranked entry or major section carries one concrete opinion AND one fair
     criticism, with a specific detail (price, mode, patch state), not adjectives
   - no two sections make the same point; the closing section helps a reader decide,
     it does not recap
   - image captions say something editorial, not just the game's name
   - any sentence that exists only to fill space gets cut
   Make the edits with wp_update_post (block markup, as the skill requires). If your
   edits changed word count or links, re-run the Phase 5 script numbers mentally and
   re-run Phase 8b once. One pass only — improve the article, do not rewrite it.

6. PUBLISH ONLY AFTER BOTH SCRIPTS PASS AND THE EDITORIAL PASS IS DONE.
   Publish each article as soon as step 5 is complete for it.

7. UPDATE THE SHEET IMMEDIATELY AFTER EACH ARTICLE.
   Right after publishing article N, set that row's Status = Published and
   Article link = the real permalink read back from WordPress with wp_search or
   wp_get_post. Never derive the URL from the title, because slugs get trimmed.
   If the title changed from the plan, update the Title column too.
   Per-article updates matter: if the run dies on article 3, articles 1 and 2 stay
   recorded and tomorrow's run will not redo them.

8. SAFETY GATE — leave it as a DRAFT instead of publishing when any of these is true:
   - any line of the Phase 5 or Phase 8b script prints FAIL
   - a game's image source cannot be verified: for Steam-sourced art, the appid
     confirmed against an independent source; for mobile-sourced art, the App Store
     trackId with matching trackName and publisher confirmed via apps.apple.com
   - for list/ranking articles: fewer than three verifiable entries exist for the
     topic; for single-game guides: the described mechanics cannot be verified
     against the current version of the game
   - fixing the brief would require changing the primary keyword
   - the row turns out to be tabletop or otherwise out of scope
   In that case set Status = Draft and Article link = https://strategygame.org/?p={POST_ID},
   and name the article and the exact failing condition in your report.

9. DO NOT cross-link the articles in this batch to each other.
   Each article links out only within its own budget at write time.

10. IF YOU RUN SHORT ON CONTEXT, STOP CLEANLY.
    Do not rush the last article or skip the check scripts or the editorial pass to
    fit it in. Finish the article you are on, publish it, update its row, then stop
    and report how many of the three you completed and which rows remain Todo.
    A short honest run beats three rushed ones.

11. REPORT WITH EVIDENCE, NOT CLAIMS.
    For each article, print:
    - item number, final title, Published or Draft, and the URL
    - the actual PASS/FAIL lines from the Phase 5 script
    - the actual PASS/FAIL lines from the Phase 8b script
    - the image verification list, one line per newly uploaded image, in the form
      "Gears Tactics = 1184050, verified via store.steampowered.com/app/1184050" for
      Steam art, or "Whiteout Survival = 1668735940, verified via apps.apple.com" for
      App Store art
    - one or two lines on what the editorial pass changed (or "no changes needed")
    - any brief correction you made, and why, in one or two lines
    Then list anything that needs a human. Do not summarize the checks as "all passed" —
    print the lines. A report without these blocks means the process was not followed.
