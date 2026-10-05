# Third-party material

Every file copied or adapted from outside this repo. Copies are pinned; nothing is fetched at runtime. Each skill folder that holds third-party material also has `SOURCE.md` and the original LICENSE/NOTICE. Update procedure: `docs/maintenance.md` → External skill intake.

| Skill path | Source | Author | License | Commit | Audited | Changes | Reason |
|---|---|---|---|---|---|---|---|
| `skills/frontend-design/` | [anthropics/skills](https://github.com/anthropics/skills) `skills/frontend-design` | Anthropic | Apache-2.0 | `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4` | 2026-10-05 | None | First-party anti-generic visual design guidance |
| `skills/ui-ux-design/references/{ios,android}.md` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `plugin/skills/impeccable/reference/` (derived from ehmo/platform-design-skills, MIT) | Paul Bakaus; ehmo | Apache-2.0 (+ MIT upstream) | `ece38d9904b8a619b3f77cab476eacad09c4fb11` | 2026-10-05 | Removed Impeccable-specific mode/review-flow wording | Compact iOS HIG and Material 3 rules |
| `skills/motion/references/gsap/` | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) `skills/gsap-*` | GreenSock | MIT | `aed9cfd3277740755f6bfc1155c7aa645403b760` | 2026-10-05 | Renamed SKILL.md → `<name>.md`; content unchanged | Official GSAP API guidance, loaded on demand |
| `skills/web-development/references/react/` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) `skills/react-best-practices` | Vercel | MIT (declared in README/front matter; no upstream LICENSE file) | `063bee94c3f4df8453406c830b0a7df0f2860278` | 2026-10-05 | `SKILL.md` → `index.md`; dropped `_template.md`, `AGENTS.md` | React/Next.js performance rules, loaded per rule |
