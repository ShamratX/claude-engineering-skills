---
name: automation-bots
description: Scrapers, crawlers, Telegram/Discord/Slack bots, browser automation (Playwright, Puppeteer, Selenium), scheduled/cron jobs, workflow automation, and email/SMS/message sending. Use when building, changing, or running unattended jobs that talk to external sites or services.
---

# Automation & Bots

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: shrink run logs, crawl output, and HTML/JSON dumps. `caveman browse <url>` gives a compressed page view when inspecting a site. Keep full: the failing request/response, the selector that broke, provider error codes, and the stack trace.

## Context
- Entry point → config/env loading → the handler or step the task names. Read scheduler config only if timing is involved.
- **Logs:** grep the error or the timestamp window. Never read a whole log.
- **Target sites:** fetch one page and grep the relevant markup, or find the JSON endpoint the page calls. Don't dump full HTML into context.
- **Provider SDKs** (Telegram, Discord, Twilio, SendGrid, SMTP, ...): check the installed version and the official docs for the exact method and limits. Never guess.

## Build
- Cheapest reliable source first: official API → the site's own JSON endpoint → HTML parsing → full browser automation.
- Respect ToS, `robots.txt`, auth requirements, and rate limits.
- Config and secrets in env, with a `.env.example`.
- Timeout on every network call. Retry network errors, 429, and 5xx with exponential backoff and jitter; honor `Retry-After`; don't retry other 4xx.
- **Idempotent:** persist processed IDs or cursors and dedupe before acting, so a re-run never double-sends or double-writes.
- Graceful shutdown (SIGINT/SIGTERM). Checkpoint long jobs.
- Structured logs (timestamp, level, job/item ID). No secrets or personal data in logs. Alert on crashes or repeated failures for long-running jobs.

## Browser automation
- Use the library the project has. Role, text, or test-id locators over long CSS/XPath chains.
- Wait on conditions, never fixed sleeps. Headless in production. Screenshot or trace on failure.
- Session and cookie files stay out of git.

## Bots
- Validate every command and argument. Admin commands behind a user-ID allowlist.
- Webhooks in production (verify the platform's secret or signature), polling is fine in development.
- Handle platform rate limits and send short help for unknown commands.

## Email / SMS / messaging
- Dry-run or sandbox mode by default during development. Sending to real recipients requires explicit user approval.
- Consent and opt-out handling; follow the provider's policies and applicable law.
- Email: SPF/DKIM/DMARC on the sending domain; escape user data in templates.
- Throttle to the provider's documented limits.

## Verify
Run once on a small real or fixture input. Run it again and confirm there are no duplicates. If retry logic changed, simulate a failure.
