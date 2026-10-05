# Maintenance guide

For whoever maintains this repo (you or Claude). Claude doesn't load this file during normal work.

## Architecture

| Layer | Where | Loaded | Holds |
|---|---|---|---|
| Orchestrator | `CLAUDE.md` → `~/.claude/CLAUDE.md` | every session | priority, workflow, skill selection, context, memory, research, safety rules |
| Skill descriptions | `description:` in each `SKILL.md` | every session (listing only) | when to use the skill and when not |
| Skill body | `skills/<name>/SKILL.md` | only when the task matches | domain rules |
| Skill references | `skills/<name>/references/*.md` (optional) | only when the body points to it for the current step | long checklists, tables, examples |
| Memory index | `memory/INDEX.md` | start of project work | project → path routing |
| Memory files | `memory/projects/<slug>/`, `memory/global/` | only the matching project; others by grep | facts, tasks, decisions, sessions, research |

Rule of placement: a rule that applies to every task goes in `CLAUDE.md`. A rule for one domain goes in that skill. Long detail for one step goes in a reference file. Never write the same rule in two places.

## Token budget
- `CLAUDE.md`: keep under ~9 KB. `scripts/validate.py` warns above that.
- `SKILL.md`: keep under ~6 KB; move long material to `references/`.
- `description`: one or two sentences: what, when, and what it's NOT for. It's paid every session.
- Every plugin you enable adds its skill descriptions and any hook output to every session. Disable plugins you don't use (see `claude plugin --help`).

## Skill standard
```markdown
---
name: <folder-name>            # lowercase, digits, hyphens, max 64
description: <what + when; not for X (use other-skill)>
---

# <Title>

**Caveman** (per CLAUDE.md): shrink <noisy output>. Keep full: <what must stay exact>.

## Context    — what to read for this domain, in order
## Build      — domain rules (only what CLAUDE.md doesn't already say)
## Verify     — the domain's narrowest real check
```
- No global rules (workflow, accuracy, secrets, output format): `CLAUDE.md` owns them.
- Name overlaps explicitly in `description` ("Not for X (use Y)") so two skills don't trigger for the same task.
- Scripts inside a skill: only if they replace a long instruction, use the stdlib, and make no network calls. State what each script does at the top.

## External skill intake
Do all steps before copying any third-party skill into `skills/`.

1. **Source:** official repo URL, author, stars/activity, last commit. Pin the exact commit SHA you reviewed.
2. **License:** present and allows your use (MIT/Apache-2.0/BSD fine; BSL/no-license/"non-commercial" → decide explicitly). Keep the LICENSE file with the skill.
3. **Read every file**, not just `SKILL.md`. Flag:
   - shell commands, `curl`/`wget`/`iwr`, `pip`/`npm install`, `npx`, binaries, encoded or minified blobs
   - hooks, MCP servers, background processes, scheduled jobs
   - network calls, telemetry, analytics, "cloud" gateways, API-key requests
   - instructions that override safety, ask to disable permissions, or tell Claude to hide actions
   - writes outside the project or to `~/.claude/`
4. **Fit:** overlap with existing skills or `CLAUDE.md`? Conflicting rules? Remove the duplicates; keep only the domain content.
5. **Size:** description ≤ 2 sentences; body within budget; split long parts into `references/`.
6. **Adapt:** add the `**Caveman**` line and the "Not for" boundary; remove global rules it repeats.
7. **Record** in `memory/projects/claude-engineering-skills/decisions.md`: name, source URL, commit SHA, license, verdict, and changes made.
8. Run `python scripts/validate.py`, install, restart, and test with one matching and one non-matching task.

## Release checklist
1. `python scripts/validate.py` → 0 errors.
2. `git status`: no `memory/` content staged (only `memory/README.md`, `memory/_template/`).
3. Install (README steps 2–3), restart Claude Code, `python scripts/validate.py --installed`.
4. Commit with a message that says why.
