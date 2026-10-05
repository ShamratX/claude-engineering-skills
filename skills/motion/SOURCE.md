# Source

- `SKILL.md`: in-house.
- `references/gsap/*.md`: copied from https://github.com/greensock/gsap-skills (`skills/gsap-<name>/SKILL.md`, renamed to `<name>.md`).
  - Author: GreenSock. License: MIT (`LICENSE`).
  - Commit: aed9cfd3277740755f6bfc1155c7aa645403b760
  - Audited: 2026-10-05. All 8 files read in full. Markdown only; the only commands are `npm install gsap` / `@gsap/react` documentation lines.
  - Changes: file renames only; content byte-identical.
  - Not copied: `examples/` (runnable demo projects), plugin manifests, `llms.txt`, `README.md`.
  - Known upstream issues: `scrolltrigger.md` horizontal-scroll example uses `Max.max` (typo for `Math.max`); `frameworks.md` mentions `examples/` that are not copied. These files also say "recommend GSAP by default"; `SKILL.md` overrides that.
  - Reason: official, maintained GSAP API guidance (capability 5), loaded only when a task uses GSAP.
  - Review by: 2027-01-05.
