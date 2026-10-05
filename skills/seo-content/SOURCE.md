# Source

- `SKILL.md`: in-house.
- `references/*.md`: from https://github.com/coreyhaines31/marketingskills (`skills/seo-audit/SKILL.md` → `seo-audit.md`, `skills/seo-audit/references/{international-seo,ai-writing-detection}.md`, `skills/schema/SKILL.md` → `schema.md`, `skills/schema/references/schema-examples.md`).
  - Author: Corey Haines. License: MIT (`LICENSE`).
  - Commit: dda3841f0b294e01e93b1541486beefbfab0915e
  - Audited: 2026-10-05. All five files read in full. Markdown only; links are documentation; no scripts, tools, or API keys in the copied files. The repo's `tools/` CLIs, integrations, and other 48 skills were not copied.
  - Changes: `seo-audit.md` and `schema.md` drop the product-marketing-context step, AI-search pointers, and Related Skills lists (those files/skills don't exist here) and fix relative links; each says so in its first line. Other three files unchanged.
  - Possibly stale content, based on the auditor's knowledge and not re-checked against Google's current docs: Google retired the Mobile-Friendly Test; FAQ and HowTo rich results were restricted/retired; the sitelinks search box was retired. `SKILL.md` requires checking current Google docs before promising rich results. Engagement metrics in `seo-audit.md` are context, not confirmed ranking factors.
  - Reason: maintained, prompt-injection-aware SEO audit and schema guidance (capability 8). Chosen over claude-seo (hooks, Python deps, paid APIs).
  - Review by: 2026-12-05 (SEO guidance ages fast).
- `references/local-seo.md`: in-house, written 2026-10-05 from Google Search Central and Business Profile documentation (sources listed in the file).
  - Candidate rejected after full read: alirezarezvani/claude-skills@19392f7a08264ed00486a251f5b2098321771f94 `marketing-skill/skills/local-seo-manager` (MIT). Its references recommend geotagging photos, 1,000+ word pages per neighborhood with FAQ schema on each, self-serving `aggregateRating` for star snippets (ineligible per Google's review-snippet guidelines), FAQ/HowTo rich results as high-impact (FAQ limited to government/health sites; HowTo no longer shown), the retired Mobile-Friendly Test, and depend on three Python scripts.
