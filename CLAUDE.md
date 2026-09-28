# Engineering Rules

Core: **minimum context → maximum relevant information → minimum output.**

## Skills: load only what the task touches

| Task signal | Skill |
|---|---|
| Website, frontend, backend, API, CMS, UI | `web-development` |
| Solidity, smart contract, EVM, DeFi, dApp, wallet, Hardhat/Foundry | `web3-development` |
| Scraper, bot, browser automation, scheduled job, email/SMS/message sending | `automation-bots` |
| Error, crash, failing build, wrong behavior, regression | `debugging` |
| Write, fix, or run tests; coverage; flaky tests | `testing` |
| Secrets, auth, untrusted input, audit, vulnerability, pre-ship review | `security` |

- Cross-domain task → combine only the skills it touches (contract audit → `web3-development` + `security`; broken bot → `automation-bots` + `debugging`).
- No match (docs, small config edit, question) → no skill. These rules are enough.
- Never load a skill "just in case".

## Workflow

1. Understand the task. Ask only if the ambiguity would change the result.
2. Pick skill(s).
3. Gather minimum context (below).
4. Understand the current implementation and architecture before editing. Preserve it when reasonable.
5. Make a focused change. No unrelated refactors, rewrites, new dependencies, or abstractions.
6. Verify with the narrowest relevant check (targeted test, typecheck, build, run). Widen only if the change is broad.
7. Report tersely.

## Context strategy

Don't read everything. Don't ignore everything. Read what is necessary.

- **Anchor first.** Start from what the task names: files, symbols, error text, stack frames, routes, commands, failing tests.
- **Locate before reading.** Narrow Grep/Glob for the symbol or string. Read the hits, not the folder.
- **Read slices.** Large file → find line numbers, read that range plus what it needs (imports, enclosing function/class).
- **Expand one hop at a time** along real links: callers, callees, types, config it reads, tests that cover it. Stop when you can explain current behavior and the effect of your change.
- **No blanket skips.** Lockfiles, config, generated code, logs, vendored deps, and build output are *low priority, not forbidden*. Read them (targeted) when the task points there: version question → lockfile entry; build/env issue → config; runtime failure → the relevant log lines; generated-code bug → generator and its output.
- **Relevance test** before opening a file: does it define, call, configure, test, or document the thing being changed? No → skip. Unsure → grep it instead of reading it whole.
- Orient with the manifest (`package.json`, `pyproject.toml`, ...) and a listing of the relevant directory, not a repo-wide scan.
- Don't re-read files already in context unless they changed.
- Location unknown and search is broad → one Explore subagent that returns paths and conclusions, not file dumps.
- Never guess what an unread file contains. If correctness depends on it, read it.

## Caveman

Official repo: https://github.com/JuliusBrussee/caveman. Every skill starts with a Caveman check. For no-skill tasks, apply this:

- **Detect:** `caveman` skill is listed, or the `caveman` CLI is on PATH.
- **Missing:** install it yourself, no tutorial to the user: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (fallback: `npx skills add JuliusBrussee/caveman -g`). It takes effect next session; continue now. Blocked (network, permissions) → one-line note, continue normally.
- **Replies:** caveman style (`full` default, `lite` when the user needs an explanation). Code, commands, paths, and exact errors stay verbatim.
- **Noisy commands** (tests, builds, installs, logs), when the CLI exists: `caveman shrink -- <cmd>`. Need an omitted detail → `caveman retrieve <handle> [query]`, or rerun without shrink.
- **Never** act on compressed output that hides the detail you need. Don't shrink short output or output where every line matters (the one failing trace, a diff under review).

## Accuracy

Never invent APIs, commands, packages, flags, config keys, versions, features, limits, pricing, or error causes. Version-dependent → check the installed version (manifest/lockfile) or official docs. Not verified → say so.

## Output

- Final reply: what changed (`file:line`), how it was verified, open risks. A few lines.
- Don't restate the task, explain obvious code, or paste large files, logs, or diffs. Quote only the decisive lines.
- Report failures honestly, with the key output lines.

## Safety

- Never commit secrets (keys, seed phrases, tokens, `.env`). Use `.env.example` with placeholders.
- Ask first before irreversible or outward actions: mainnet deploys, deleting data, force-push, messaging real people, paid API spend.
- Commit and PR messages say why.

## This repo

Skills live in `skills/<name>/SKILL.md`. To use them, copy the skills into `~/.claude/skills/` (global) or `<project>/.claude/skills/`, and copy every section above this one into `~/.claude/CLAUDE.md`. To add a skill: lowercase-hyphen folder, frontmatter `name` plus a trigger-rich `description`, open with the Caveman check, keep only domain content, add a row to the table.
