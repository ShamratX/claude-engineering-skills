# Memory store

Plain Markdown, no database, no dependencies. Read this file before the first memory write in a session; reads don't need it.

## Layout
```
INDEX.md                    one line per project; the only file read on every project task
global/preferences.md       user preferences that apply across projects
global/decisions.md         cross-project decisions (tooling, conventions)
projects/<slug>/context.md   purpose, stack, architecture, key paths, constraints (stable facts)
projects/<slug>/tasks.md     Pending / Known issues / Done (recent)
projects/<slug>/decisions.md decision log, newest first
projects/<slug>/sessions.md  compact session summaries, newest first
projects/<slug>/research.md  research conclusions with source and review date (create when needed)
projects/<slug>/research/<topic>.md  resumable deep-research notes (format: research skill references/evidence-notes.md)
_template/                   copy from here for a new project
```
`<slug>` = project folder name, lowercase, hyphens (`Email sender bot` → `email-sender-bot`).

## Retrieval (keep reads small)
1. Read `INDEX.md`. Find the row whose path matches the working directory. No row → no project memory; continue.
2. Read that project's `context.md` and `tasks.md`.
3. Other files: grep for the task's keywords first, then read only the matching entries.
4. `global/` only when a preference or cross-project decision could change the result.

## Entry format
One fact per line:
```
- YYYY-MM-DD · <fact, one sentence> · confirmed|unverified [· src: <file:line | URL | user>]
```
- `confirmed` = seen in code, output, docs, or stated by the user. Everything else is `unverified`.
- Each file starts with front matter `updated: YYYY-MM-DD`. Change it on every edit.
- `research.md` entries add `· review-by: YYYY-MM-DD`. Past that date = stale until re-checked.

## Writing rules
- Write after non-trivial work only. Update in place; don't append duplicates.
- Promote durable facts from a session entry into `context.md`, `decisions.md`, or `tasks.md`.
- Decisions: what was chosen, why, and rejected alternatives in one line. Reversed decision → mark the old one `superseded` with the date; don't delete it.
- Session entry: at most 5 lines: goal, outcome, files touched, open items. Keep the newest 10 entries; delete older ones after promoting anything durable.
- `tasks.md` Done: keep the newest 15 items.
- New project: copy `_template/project/` to `projects/<slug>/` and add an `INDEX.md` row.
- Wrong or obsolete entry → fix or delete it. Never keep a known-false fact.

## Never store
Secrets, credentials, API keys, tokens, private keys, seed phrases, passwords, connection strings with passwords, session cookies, personal data not needed for the work, or full conversation transcripts. Refer to a secret by its location only (`.env: SMTP_PASS`).

## Git
This repo is public. Only this file and `_template/` are tracked; everything else here is gitignored. To sync memory across machines, make the repo private first, then change `.gitignore`.
