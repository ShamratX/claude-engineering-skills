# Source

- `SKILL.md`: in-house.
- `references/react/index.md` and `references/react/rules/*.md`: copied from https://github.com/vercel-labs/agent-skills (`skills/react-best-practices/SKILL.md` → `index.md`, `rules/`).
  - Author: Vercel. License: MIT as declared in the source README and front matter; no LICENSE file upstream, so standard MIT text is in `references/react/LICENSE`.
  - Commit: 063bee94c3f4df8453406c830b0a7df0f2860278
  - Audited: 2026-10-05. Index and all 71 copied rule files read in full. Markdown only; URLs are documentation links or `example.com` placeholders; commands are examples (`npx svgo`).
  - Changes: `SKILL.md` renamed to `index.md`; content unchanged. Not copied: `_template.md`, `AGENTS.md` (112 KB compiled duplicate; `index.md` still mentions it), `README.md`, `metadata.json`.
  - Caveats: some rules suggest extra packages (SWR, lru-cache, better-all) or Vercel-specific features; `SKILL.md` keeps project conventions and the "no new dependency without a reason" rule in charge.
  - Reason: React/Next.js performance rules (capability 4), loaded one rule at a time.
  - Review by: 2027-01-05.
