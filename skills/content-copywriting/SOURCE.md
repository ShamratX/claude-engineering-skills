# Source

- `SKILL.md`: in-house.
- `references/ai-writing-detection.md`: from https://github.com/coreyhaines31/marketingskills (`skills/seo-audit/references/ai-writing-detection.md`).
  - Author: Corey Haines. License: MIT (`LICENSE`).
  - Commit: dda3841f0b294e01e93b1541486beefbfab0915e (unchanged upstream at 1efedbc).
  - Audited: 2026-10-05 (read in full; Markdown only, no scripts or network calls). Unchanged.
  - Moved here from `skills/seo-content/references/` on 2026-10-10 when copywriting became its own skill.
  - Reason: concrete list of AI-sounding words and patterns for the copy edit pass.
- `references/{copywriting,copy-frameworks,ai-tells,natural-transitions,copy-editing,copy-editing-checklist,plain-english-alternatives,content-refresh}.md`: from the same repo (`skills/copywriting/` and `skills/copy-editing/`, `SKILL.md` → `copywriting.md` / `copy-editing.md`, `checklist.md` → `copy-editing-checklist.md`).
  - Commit: 1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff
  - Audited: 2026-10-10. Every file read in full; Markdown only, no scripts, commands, network calls, or injected instructions. `evals/` not copied.
  - Changes: `copywriting.md` and `copy-editing.md` drop the product-marketing-context step and Related Skills lists, re-point links to this folder, and `copywriting.md` drops an unsourced conversion statistic; `copy-frameworks.md` gains a warning that its percentages and example numbers are unsourced. Each modified file says so in its first line. The rest are unchanged.
  - Known upstream issues: `copy-frameworks.md` cites "+81% conversions" and similar figures without a source; `copy-editing.md` specificity examples ("2,847 teams") are illustrative. `SKILL.md` Accuracy rules override both. `ai-tells.md` mentions the seo-audit skill's AI-writing file; here it is `ai-writing-detection.md` in this folder. `content-refresh.md` mentions "ai-seo skill" and "seo-audit skill's title-tags reference"; here they are `seo-content/references/ai-seo/index.md` and `seo-content/references/title-tags.md`.
  - Reason: the most-used Claude copywriting skill pack (53.9k stars, maintained); adds headline formulas, the AI-tell blacklist with self-check, and a structured seven-sweep editing process.
  - Review by: 2027-01-10.
