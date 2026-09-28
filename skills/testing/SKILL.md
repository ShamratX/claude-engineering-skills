---
name: testing
description: Write and run effective automated tests - unit, integration, end-to-end, and smart contract tests (Jest, Vitest, Pytest, Playwright, Hardhat, Foundry). Use when adding tests, fixing failing tests, or verifying a change.
---

# Testing

## Workflow

1. **Find the existing setup.** Check the test framework, config, test folder,
   and `test` script in `package.json` (or equivalent). Follow the same
   patterns and naming.
2. **Decide what to test.** Focus on behavior that matters: business logic,
   edge cases, error paths, and anything that broke before.
3. **Write the test.** Arrange → Act → Assert. One behavior per test.
4. **Run it and watch it fail first** when writing a test for a bug or a new
   feature. A test that never failed may not be testing anything.
5. **Make it pass,** then run the full suite to check for regressions.

## What makes a good test

- **Descriptive name:** `it("reverts when a non-owner calls mint")`.
- **Independent:** no reliance on test order or shared mutable state.
- **Deterministic:** no real network calls, random values, or current time
  without control (mock or fix them).
- **Fast:** mock slow external services in unit tests.
- **Tests behavior, not implementation:** survives a refactor.

## What to cover

- [ ] The happy path
- [ ] Boundary values (0, 1, max, empty string, empty list)
- [ ] Invalid input and error handling
- [ ] Permission checks (who can and cannot call it)
- [ ] Regression tests for every fixed bug

## Test types

| Type | Scope | Tools |
|------|-------|-------|
| Unit | One function or component | Jest, Vitest, Pytest |
| Integration | Several parts together (API + DB) | Supertest, Pytest, test DB |
| End-to-end | Full user flow in a browser | Playwright, Cypress |
| Smart contract | Contract logic on a local chain | Hardhat + Chai, Foundry |

## Smart contract testing

- Use fixtures (`loadFixture`) for a fresh state per test.
- Test every `require` / custom error with `revertedWith` or
  `revertedWithCustomError`.
- Check emitted events and balance changes.
- Test access control with non-owner signers.
- Use time helpers for time-based logic; fuzz tests in Foundry for math.
- Run coverage (`npx hardhat coverage` / `forge coverage`).

## Rules

- Never delete or weaken a failing test just to make the suite pass. Fix the
  code, or explain why the test itself was wrong.
- Do not mark tests as skipped without saying why.
- Report results honestly: how many passed, failed, or were skipped.
