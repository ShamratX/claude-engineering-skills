# Source

- `SKILL.md`: in-house.
- `references/hard-bugs.md`: adapted from https://github.com/mattpocock/skills (`skills/engineering/diagnosing-bugs/SKILL.md`).
  - Author: Matt Pocock. License: MIT (`LICENSE`).
  - Commit: f6abdeb8dd2a9be64f924ab44c7af374cb76726d
  - Audited: 2026-10-05. Read in full. Markdown only.
  - Changes: removed front matter, the GLOSSARY/ADR step (depends on that repo's setup), and references to `scripts/hitl-loop.template.sh` (replaced with numbered human steps). The file says so in its first line.
  - Not copied: `scripts/hitl-loop.template.sh`, `agents/openai.yaml`.
  - Reason: stricter hard-bug discipline (red-capable feedback loop first, minimised repro, ranked falsifiable hypotheses, tagged instrumentation, seam-level regression test, cleanup checklist).
  - Review by: 2027-01-05.
