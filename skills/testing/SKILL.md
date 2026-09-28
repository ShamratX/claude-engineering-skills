---
name: testing
description: Write, fix, or run unit, integration, end-to-end, and smart contract tests; coverage; flaky tests; test setup. Use when adding tests, verifying a change, or when tests fail.
---

# Testing

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: `caveman shrink -- <test cmd>` for suite runs and passing noise. Keep full: each failing test name, the assertion diff, the stack trace, and the pass/fail/skip counts.

## Context
- Detect the framework from manifest scripts and test config. Read **one** nearby existing test as the style template.
- Read the unit under test and the interfaces of its direct dependencies. Read fixtures, mocks, and helpers only when the test uses them.
- Never read the whole test suite.

## Run
- Targeted first: a single file or a name filter, using the framework's own flag (check its docs or `--help`, don't guess). Then the related suite. Full suite only for broad changes or before finishing a cross-cutting one.
- New feature or bug fix → watch the test fail first, then pass.

## Write
- Test behavior through the public interface. Arrange-Act-Assert, one behavior per test, descriptive names.
- Deterministic and independent: control time, randomness, and network; no reliance on order or shared mutable state.
- Cover: happy path, boundaries (0, 1, max, empty), invalid input and errors, permissions, and a regression test for each fixed bug.
- Mock at system boundaries (network, clock, external services), not internal modules.
- Levels: unit for logic, integration for boundaries (API + DB), e2e for critical user flows only.
- **Smart contracts:** fresh state per test (fixtures, `setUp`); assert reverts and custom errors, events, and balance changes; test access control with non-owner accounts; manipulate time for time-based logic; fuzz or invariant tests for math; fork tests for live-protocol integrations.
- **Flaky tests:** find the nondeterminism (timing, order, shared state, real network). Never mask it with sleeps or retries.

## Rules
- Never delete, weaken, or skip a failing test to get green, and never change an assertion to match buggy output. If the test itself is wrong, say why.
- Report pass/fail/skip counts and each failure.
