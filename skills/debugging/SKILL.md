---
name: debugging
description: Systematically find and fix the root cause of bugs, errors, crashes, failing tests, and unexpected behavior. Use when something is broken, an error message appears, or behavior differs from what is expected.
---

# Debugging

Fix the **cause**, not the symptom. Do not guess-and-patch.

## Process

1. **Reproduce it.** Get exact steps, input, and the full error message and
   stack trace. If you cannot reproduce it, you cannot confirm the fix.
2. **Read the error carefully.** Note the file, line, error type, and the
   first frame that is in the project's own code.
3. **Form a hypothesis.** State what you think is wrong and why, in one
   sentence.
4. **Test the hypothesis.** Add targeted logging, use a debugger, or write a
   failing test. Change one thing at a time.
5. **Find the root cause.** Ask "why?" until you reach the real source - not
   just where it crashed, but why the bad value got there.
6. **Fix it minimally.** Change only what is needed.
7. **Verify.** Re-run the reproduction steps and the related tests. Add a
   regression test so the bug cannot return silently.
8. **Clean up.** Remove temporary logs and debug code.

## Narrowing techniques

- **Binary search:** comment out or bypass half the code path; see which half
  still fails.
- **git bisect:** find the commit that introduced the bug.
- **Minimal reproduction:** strip the case down to the smallest input that
  still fails.
- **Compare working vs broken:** environment, versions, config, data.
- **Check assumptions:** print the actual values instead of trusting what they
  "should" be.

## Common causes to check

- `undefined` / `null` values and missing optional fields
- Async issues: missing `await`, race conditions, unhandled promise rejections
- Off-by-one errors and wrong comparison operators
- Stale cache, old build output, or a server that was not restarted
- Wrong environment variables or a missing `.env`
- Version mismatch between packages (check the lockfile)
- Type coercion (`"1" + 1`), floating point, timezone and date handling
- Web3: wrong network/chain ID, insufficient gas, wrong decimals, reverts from
  `require` checks, nonce issues

## Reporting the fix

State clearly:
- **What** was broken (the symptom)
- **Why** (the root cause)
- **How** it was fixed
- **How** it was verified
