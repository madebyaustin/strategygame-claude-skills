# strategygame-claude-skills

Custom Claude skills for automated strategy game website content creation.

## What this repo is for

This repository is attached to **Claude Code Cloud Routines** so that scheduled tasks (e.g., daily article writing) can access the skills defined here. Skills live in `.claude/skills/` and are automatically discovered by Claude Code sessions.

## Skills included

| Skill | Purpose |
|---|---|
| `mcp-web-seo-writing-eng` | Write SEO-optimized articles from keyword pack + reference URL |
| `mcp-web-news-writing-eng` | Write news articles from reference URL (no SEO keyword targeting) |
| `mcp-web-seo-keywords-analyzing-monthly` | Analyze Semrush keyword sheet > 90-title monthly content plan |

## How it works

1. A Cloud Routine is scheduled (e.g., daily at 2 AM).
2. The Routine clones this repo automatically.
3. Claude reads `CLAUDE.md` and discovers skills in `.claude/skills/`.
4. The Routine prompt references the skill by name > Claude loads the full `SKILL.md` instructions.
5. Claude writes articles using MCP connectors (WordPress, Google Drive, Composio Google Sheets).

## Setup

1. Push this repo to GitHub (public or private).
2. In Claude Code Routines (`claude.ai/code/routines`), create a new Routine.
3. Attach this repository.
4. Add connectors: WordPress MCP, Google Drive, Composio (Google Sheets).
5. Paste the Routine prompt and set the schedule.

## Reusing for other sites

To add a new site:
1. Create a new project context document (Google Docs) with site identity, audience, voice, categories.
2. Create a new content plan spreadsheet (Google Sheets).
3. Create a new Routine with the new site's details in the prompt.
4. The same skills work across sites - only the prompt and context doc change.
