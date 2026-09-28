# Engineering Rules

Core: **minimum context → maximum relevant information → minimum output.**

## Skills
Select by skill `description`. Load only the skill(s) the task touches; combine for cross-domain work (contract audit → `web3-development` + `security`; broken bot → `automation-bots` + `debugging`). No match → none. Never "just in case".

## Workflow
1. Understand the task. Ask only if ambiguity changes the result.
2. Gather minimum context (below).
3. **Plan:** simple/trivial task → implement directly, no plan. Non-trivial (multiple files, new feature, schema/API/contract change, unclear approach) → short actionable plan first (steps naming files and checks), sized to the task. Revise only when new information materially changes the approach.
4. Smallest clean change that fully solves the task, following project conventions. No unrelated refactors.
5. Verify with the narrowest relevant check (targeted test, typecheck, build, run); widen only for broad changes.

## Architecture
- Inspect the existing architecture before significant changes; preserve it when reasonable. Never restructure unrelated parts.
- New features: simplest production-ready structure with clear responsibilities that fits the project.
- No speculative abstractions, layers, dependencies, services, or microservices. Weigh maintainability, security, scalability, and extension only where the decision actually affects them.

## Context
Don't read everything. Don't ignore everything. Read what is necessary.
- **Anchor** on what the task names: files, symbols, error text, stack frames, routes, failing tests.
- **Locate, then read:** narrow Grep/Glob; read the hits. Large file → read the relevant range plus what it depends on (imports, enclosing function).
- **Expand one hop** along real links (callers, callees, types, config, tests). Stop once you can explain current behavior and your change's effect.
- **No blanket skips.** Lockfiles, config, generated code, logs, vendored deps, and build output are low priority, not forbidden. Read the relevant part when the task points there (version → lockfile entry; env/build issue → config; runtime failure → matching log lines).
- Unsure whether a file matters → grep it, don't read it whole. Orient with the manifest and the relevant directory, not a repo scan. Don't re-read unchanged files.
- Broad unknown-location search → one Explore subagent returning paths, not dumps.
- Never guess an unread file's contents when correctness depends on it.

## Caveman
Official: https://github.com/JuliusBrussee/caveman. Each skill's `Caveman:` line names what to shrink and what to keep in full there.
- **Detect:** a `caveman` skill is listed, or the `caveman` CLI is on PATH.
- **Missing:** install it yourself, no tutorial: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman`. It activates next session; continue now. Blocked → one-line note, continue normally.
- **Replies:** caveman style (auto-activated by the plugin; otherwise `/caveman`). Code, commands, paths, exact errors, and security warnings stay verbatim.
- **Noisy output** (CLI present): `caveman shrink -- <cmd>`. Need an omitted detail → `caveman retrieve <handle> [query]` or rerun unshrunk. Never act on output that hides what you need. Don't shrink short output.

## Accuracy
Never invent APIs, commands, packages, flags, config keys, versions, features, limits, pricing, or error causes. Version-dependent → check the installed version or official docs. Unverified → say so.

## Output
Final reply: what changed (`file:line`), how verified, open risks. A few lines. No restating the task, explaining obvious code, or pasting large files/logs/diffs. Report failures honestly with the key lines.

## Safety
- Never commit secrets (keys, seed phrases, tokens, `.env`); use `.env.example` placeholders. Never print secret values.
- Ask first before irreversible or outward actions: mainnet deploys, deleting data, force-push, messaging real people, paid API spend.
- Commit/PR messages say why.

## This repo
Install: copy `skills/*` to `~/.claude/skills/` (or `<project>/.claude/skills/`) and the sections above into `~/.claude/CLAUDE.md`. New skill: `skills/<name>/SKILL.md`, frontmatter `name` + precise `description` (triggers and exclusions), a `Caveman:` line, and domain-only rules.
