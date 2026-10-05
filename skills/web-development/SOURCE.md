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
- `references/postgres/`: copied from https://github.com/supabase/agent-skills (`skills/supabase-postgres-best-practices/`: `SKILL.md` → `index.md`, `references/*.md`).
  - Author: Supabase. License: MIT (`references/postgres/LICENSE`).
  - Commit: c9be0e931b7930f7d02126d04774d904c381e7d7
  - Audited: 2026-10-05. Index and all 32 copied files read in full. Markdown only; SQL examples; links to PostgreSQL and Supabase docs.
  - Changes: `SKILL.md` renamed to `index.md` (its `references/<rule>.md` paths mean files in this same folder); content unchanged. Not copied: `_contributing.md`, `_template.md`, `CHANGELOG.md`.
  - Possible upstream inaccuracies (auditor's knowledge, not re-verified): `conn-prepared-statements.md` attributes `{ prepare: false }` to Node.js `pg`, but that is a `postgres.js` option; `schema-primary-keys.md` says UUIDv7 needs the `pg_uuidv7` extension, but PostgreSQL 18 ships `uuidv7()`. Check the installed driver and Postgres version.
  - Reason: official Postgres schema, indexing, RLS, locking, and query rules (Backend capability), loaded one rule at a time.
  - Review by: 2027-01-05.
