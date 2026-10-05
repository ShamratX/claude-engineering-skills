---
name: debugging
description: Find and fix the root cause of errors, crashes, failing builds, wrong output, regressions, performance problems, and flaky behavior. Use when something is broken or behaves unexpectedly; combine with the affected domain's skill. For writing new tests, use testing.
---

# Debugging

**Caveman** (per CLAUDE.md): shrink repro runs, verbose logs, install/build noise. Keep full: the **first** error, project-code stack frames, failing assertion, exact versions. Clue hidden → `caveman retrieve` or rerun unshrunk.

## Context: follow the evidence
1. **Evidence:** exact error, stack trace, repro steps, recent changes (`git log --oneline -10`, `git diff`).
2. **Anchor:** top project-code stack frame → read that function. No trace → grep the exact error string.
3. **Trace the bad value backward** one hop at a time: caller → input source → config.
4. **Symptoms promote low-priority files:** after an upgrade → lockfile; env-specific / "works on my machine" → config and env; build-only failure → build config and generated output.
5. **Regressions:** `git log -S "<string>"` or `git bisect`.

## Process
1. Reproduce, or say it couldn't be reproduced and what that means for confidence.
2. One hypothesis, one sentence. Test it with the cheapest experiment (targeted log, single test, REPL); change one thing at a time.
3. Root cause = why the bad state arose, not where it crashed.
4. Minimal fix at the cause.
5. Verify: repro passes, related tests pass. Add a regression test when a test setup exists.
6. Remove temporary debug code.

## Common causes
null/undefined, missing fields · missing `await`, races, unhandled rejections · off-by-one, wrong comparisons · stale cache/build, process not restarted · wrong/missing env · dependency version drift · type coercion, floating point, timezones · Web3: wrong chain ID, decimals, nonce, gas, `require` reverts.

## Don't
Patch symptoms (swallowed errors, null guards hiding bad data, retrying flaky tests until green). Claim a cause without evidence; say "suspected" until confirmed.

## Report
`Symptom / Cause (file:line) / Fix / Verified by`, one line each.
