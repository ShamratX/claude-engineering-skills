# Pre-delivery QA checklists

Run only the section for the project type, and only items the project has. Each item ends as **passed**, **failed** (fix or report), or **not run** (state why: no tool, no access, out of scope). Never mark an item passed without having run or seen it.

## Website / web app

**Build and runtime**
- [ ] Install, lint, type-check (if configured), and production build succeed with the project's scripts.
- [ ] Existing tests pass; new behavior has tests where the project has a test setup.
- [ ] Dev or preview server runs; each changed page loads without console errors or failed network requests (4xx/5xx, blocked assets, CORS).

**Layout (rendered, not inferred from code)**
- [ ] Screenshots or responsive-mode checks at 360, 768, 1024, 1440 px for each changed page.
- [ ] No horizontal scroll, overlap, clipping, or text overflow; images load, are sharp, and keep their aspect ratio.
- [ ] Spacing, type, and components consistent with the rest of the site; no leftover placeholder or lorem ipsum.

**Function**
- [ ] Navigation, including the mobile menu, works; every link and button goes to the right place (no `#`, no 404s).
- [ ] Forms: required fields, validation messages, successful submit, failure state, data actually arrives (or say the backend wasn't reachable).
- [ ] Primary CTA works on mobile and desktop; `tel:`/`mailto:` links are correct.

**Accessibility basics**
- [ ] One H1, logical heading order, landmarks; every control has a label; images have meaningful or empty `alt`.
- [ ] Keyboard: tab through the page, focus visible, no traps, menu and dialogs operable.
- [ ] Text contrast meets WCAG AA; nothing relies on color alone; reduced motion respected.
- [ ] Automated scan (axe, Lighthouse) if available; it doesn't replace the manual checks above.

**Content**
- [ ] Facts (name, phone, address, hours, prices, claims) match the client's confirmed info and are identical across pages.
- [ ] No invented testimonials, stats, certifications, or guarantees; every `[CONFIRM: ...]` placeholder is listed for the client.

**Technical SEO (when in scope)**
- [ ] Per page: unique title and meta description, canonical, no unintended `noindex`, `lang` set.
- [ ] `robots.txt` and XML sitemap correct for the new pages; internal links resolve.
- [ ] JSON-LD parses and matches visible content; validated with Rich Results Test or Schema Markup Validator when reachable.
- [ ] Performance: Lighthouse or field data when available (LCP, INP, CLS); report measured numbers only.

**Clean-up**
- [ ] No temporary screenshots, debug code, unused assets or dependencies left in the project.

## Web3 / smart contracts

These are minimums; `web3-development` and `security` rules still apply in full. Don't skip or shorten them to save time or tokens.
- [ ] Clean compile with the project's pinned compiler; no new warnings left unexplained.
- [ ] Full test suite passes; new or changed functions have tests for success, reverts/custom errors, events, access control (non-owner), and edge values.
- [ ] Fuzz/invariant tests for math and accounting; fork tests for live-protocol integrations, when the toolchain supports them.
- [ ] Coverage report and Slither (or the project's static analyzer) run when available; findings triaged, not ignored.
- [ ] Security review of changed value-transfer, access-control, oracle, and upgrade paths (`security` skill).
- [ ] Deploy script tested on a local node, then testnet; addresses, constructor args, and chain ID recorded.
- [ ] Explorer verification succeeded (link or command output), if deployed.
- [ ] dApp: wrong-network prompt, wallet rejection, pending/confirmed/failed states, mobile wallet flow.
- [ ] Claims about tests, coverage, deployments, verification, or audits are backed by output from this session; mainnet steps only with explicit user approval.

## Automation / bots

- [ ] Config loads from env or config files; startup fails clearly when a required value is missing; no secrets in code, logs, fixtures, or test output.
- [ ] Runs once end-to-end against a fixture, sandbox, test account, or dry-run mode, never real customer data or real recipients unless the user approves.
- [ ] Second run produces no duplicate sends or writes (idempotency).
- [ ] Error paths: timeout, 429 with `Retry-After`, 5xx retry with backoff, non-retryable 4xx, malformed input; simulated at least once when retry logic changed.
- [ ] Graceful shutdown and resume from checkpoint for long jobs.
- [ ] Regression tests for parsers, command handlers, and fixed bugs; selectors or endpoints of scraped sites re-checked if they changed.
- [ ] Logs are structured and contain no personal data or tokens.
