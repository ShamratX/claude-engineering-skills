# Source

- `SKILL.md`: in-house.
- `references/*.md`: from https://github.com/coreyhaines31/marketingskills (`skills/seo-audit/SKILL.md` → `seo-audit.md`, `skills/seo-audit/references/international-seo.md`, `skills/schema/SKILL.md` → `schema.md`, `skills/schema/references/schema-examples.md`).
  - Author: Corey Haines. License: MIT (`LICENSE`).
  - Commit: dda3841f0b294e01e93b1541486beefbfab0915e
  - Audited: 2026-10-05. All files read in full. Markdown only; links are documentation; no scripts, tools, or API keys in the copied files. The repo's `tools/` CLIs, integrations, and other 48 skills were not copied.
  - Changes: `seo-audit.md` and `schema.md` drop the product-marketing-context step, AI-search pointers, and Related Skills lists (those files/skills don't exist here) and fix relative links; each says so in its first line. `international-seo.md` and `schema-examples.md` unchanged.
  - Moved out on 2026-10-10: `ai-writing-detection.md` → `skills/content-copywriting/references/` (see its `SOURCE.md`); in-house `local-seo.md` → `skills/local-seo/references/google-guidelines.md`.
  - Possibly stale content, based on the auditor's knowledge and not re-checked against Google's current docs: Google retired the Mobile-Friendly Test; FAQ and HowTo rich results were restricted/retired; the sitelinks search box was retired. `SKILL.md` requires checking current Google docs before promising rich results. Engagement metrics in `seo-audit.md` are context, not confirmed ranking factors.
  - Reason: maintained, prompt-injection-aware SEO audit and schema guidance. Chosen over claude-seo (hooks, Python deps, paid APIs).
  - Review by: 2026-12-05 (SEO guidance ages fast).
