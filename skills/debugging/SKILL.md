---
name: debugging
description: Find and fix the root cause of errors, crashes, failing builds or tests, wrong output, regressions, performance problems, and flaky behavior. Use when something is broken or behaves unexpectedly; combine with the skill for the affected domain.
---

# Debugging

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: shrink repro runs, verbose logs, and install/build noise. Keep full: the **first** error, stack frames in project code, the failing assertion, and exact versions. If shrunk output hides the clue, `caveman retrieve <handle> [query]` or rerun without shrink.

## Context: follow the evidence, not the tree
1. **Collect evidence:** exact error text, stack trace, repro steps, and what changed recently (`git log --oneline -10`, `git diff`).
2. **Anchor:** the top stack frame in project code → read that function. No trace → grep the exact error string to find where it's thrown.
3. **Trace the bad value backward** one hop at a time: caller → input source → config.
4. **Logs:** grep the error or the timestamp window. Never read whole logs.
5. **Low-priority files become first-class** when symptoms point at them: after an upgrade → lockfile; env-specific or "works on my machine" → config and env; build-only failure → build config and generated output.
6. **Regressions:** `git log -S "<string>"` or `git bisect`.

## Process
1. Reproduce it, or say it couldn't be reproduced and what that means for confidence in the fix.
2. State one hypothesis in one sentence. Test it with the cheapest experiment (targeted log, single test, REPL). Change one thing at a time.
3. Root cause means *why the bad state arose*, not where it crashed.
4. Fix minimally at the cause. No refactor.
5. Verify: the repro now passes and related tests pass. Add a regression test when a test setup exists.
6. Remove temporary debug code.

## Common causes
null/undefined and missing fields · missing `await`, races, unhandled rejections · off-by-one and wrong comparisons · stale cache, build, or process not restarted · wrong or missing env · dependency version drift · type coercion, floating point, timezones · Web3: wrong chain ID, decimals, nonce, gas, or a revert from a `require`.

## Don't
- Patch symptoms: swallowing errors, null guards that hide bad data, retrying a flaky test until it's green.
- Claim a cause without evidence. Say "suspected" until it's confirmed.

## Report
`Symptom / Cause (file:line) / Fix / Verified by`, one line each.
