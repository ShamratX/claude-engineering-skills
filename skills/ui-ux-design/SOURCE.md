# Source

- `SKILL.md`: in-house.
- `references/ios.md`, `references/android.md`: adapted from https://github.com/pbakaus/impeccable (path `plugin/skills/impeccable/reference/`).
  - Author: Paul Bakaus. Upstream origin: ehmo/platform-design-skills (MIT).
  - License: Apache-2.0 (`LICENSE`), notices in `NOTICE.md`, MIT text in `LICENSE-ehmo-MIT.txt`.
  - Commit: ece38d9904b8a619b3f77cab476eacad09c4fb11
  - Audited: 2026-10-05. Both files read in full. Markdown only. Commands they mention (`xcrun simctl`, `adb`) are documentation for verifying native builds; nothing runs automatically.
  - Changes: removed Impeccable-specific "mode" and review-flow wording.
  - Not copied: the rest of Impeccable (Rust CLI, hooks on SessionStart/Edit/Stop, browser scripts).
  - Reason: compact HIG and Material 3 rules for iPhone and Android UX (capability 3). Chosen over ehmo's originals (37–40 KB each) for token cost.
  - Review by: 2027-01-05.
