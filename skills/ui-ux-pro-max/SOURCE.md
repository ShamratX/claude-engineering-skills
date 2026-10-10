# Source

- `SKILL.md`: in-house adaptation (upstream `SKILL.md` drives a Python search script; rewritten to search the data with Grep).
- `references/quick-reference.md`, `references/pro-rules.md`, `references/data/*.csv`, `references/data/stacks/*.csv`: copied from https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (`.claude/skills/ui-ux-pro-max/references/` and `data/`).
  - Author: Next Level Builder. License: MIT (`LICENSE`).
  - Commit: 50d8a7de0900119855614541f15a1a616691eb33
  - Audited: 2026-10-10. Read: `SKILL.md`, both references, every CSV header, scan of all data for commands/URLs/injected instructions; CLI source (`cli/src`) and published npm package `ui-ux-pro-max-cli@2.15.0` (no install scripts; network only to api.github.com/npm). Data is plain CSV; the only commands are framework setup notes in stack files (`npx shadcn ...`, `npx astro add ...`).
  - Changes: none to copied files; `data/` moved under `references/data/`.
  - Not copied: `scripts/` (Python search/design-system generator and tests; repo rule: no scripts), `google-font-licenses.json`, `phosphor-icons-upstream.json`, `data-provenance.json`, `catalog-summary.json` (machine data for the scripts), the CLI, gallery, stack example (its `.claude/settings.json` enables all project MCP servers and broad permissions).
  - Reason: large, maintained lookup dataset (styles, palettes, font pairs, UX rules, stack rules) to supplement `ui-ux-design` and `frontend-design`; added at user request.
  - Review by: 2027-01-10.
