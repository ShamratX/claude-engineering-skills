---
name: testing
description: Write, fix, or run unit, integration, end-to-end, and smart contract tests; coverage; flaky tests; test setup; pre-delivery QA checklists for websites, smart contracts, and bots. Use when adding tests, verifying a change, or checking work before calling it done. If a test fails because the code is broken, use debugging.
---

# Testing

## Context
- Framework from manifest scripts + test config. **One** nearby existing test as the style template.
- The unit under test + its direct dependencies' interfaces. Fixtures/mocks/helpers only when the test uses them.
- Never read the whole suite.

## Run
- Targeted first (single file or name filter via the framework's own flag; check `--help`/docs, don't guess) → related suite → full suite only for broad or cross-cutting changes.
- New feature or bug fix → see the test fail first, then pass.

## Write
- Behavior through the public interface. Arrange-Act-Assert, one behavior per test, descriptive names.
- Deterministic and independent: control time, randomness, network; no order dependence or shared mutable state.
- Cover: happy path, boundaries (0, 1, max, empty), invalid input/errors, permissions, a regression test per fixed bug.
- Mock at system boundaries (network, clock, external services), not internal modules.
- No tautological tests: expected values come from an independent source (a known-good literal, worked example, or the spec), never recomputed the way the code computes them.
- Test-first work goes in vertical slices: one test, the minimal code to pass it, repeat. Don't write a batch of tests for imagined behavior up front.
- Unit for logic, integration for boundaries (API + DB), e2e for critical user flows only.
- **Smart contracts:** fresh state per test (fixtures, `setUp`); assert reverts/custom errors, events, balance changes; access control with non-owner accounts; time manipulation for time-based logic; fuzz/invariant tests for math; fork tests for live-protocol integrations.
- **Flaky:** find the nondeterminism (timing, order, shared state, real network). Never mask with sleeps or retries.

## Pre-delivery QA
Before calling a feature, page, or project done, run the checklist for its type in `references/qa-checklists.md`: website, Web3/smart contracts, or automation/bots. Use only the sections that apply; skip items the project doesn't have and say which.

## Rules
Never delete, weaken, or skip a failing test to get green, or change an assertion to match buggy output. If the test is wrong, say why. Report pass/fail/skip counts and each failure.
Evidence only: a test, build, deploy, verification, or visual check counts as done only if it actually ran in this session and its output was read. Report each check as passed, failed, or not run (with the reason).
