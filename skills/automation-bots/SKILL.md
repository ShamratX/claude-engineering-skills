---
name: automation-bots
description: Scrapers, crawlers, Telegram/Discord/Slack/WhatsApp bots, browser automation (Playwright, Puppeteer, Selenium), scheduled/cron jobs, workflow automation, and email/SMS/message sending. Use for unattended jobs that talk to external sites or services. Not for browser e2e tests of your own app (testing).
---

# Automation & Bots

**Caveman** (per CLAUDE.md): shrink run logs, crawl output, HTML/JSON dumps; `caveman browse <url>` for a compressed page view. Keep full: failing request/response, broken selector, provider error codes, stack trace.

## Context
- Entry point → config/env loading → the named handler/step. Scheduler config only if timing is involved.
- **Target sites:** fetch one page and grep the relevant markup, or find the JSON endpoint the page calls. Never dump full HTML.
- **Provider SDKs** (Telegram, Discord, Twilio, SendGrid, SMTP, ...): check the installed version and official docs for exact methods and limits.

## Build
- Cheapest reliable source: official API → site's own JSON endpoint → HTML parsing → browser automation.
- Respect ToS, `robots.txt`, auth requirements, rate limits.
- Timeout on every network call. Retry network errors, 429, 5xx with exponential backoff + jitter; honor `Retry-After`; don't retry other 4xx.
- **Idempotent:** persist processed IDs/cursors and dedupe before acting; re-runs never double-send or double-write.
- Graceful shutdown (SIGINT/SIGTERM); checkpoint long jobs.
- Structured logs (timestamp, level, job/item ID), no secrets or personal data. Alert on crashes/repeated failures for long-running jobs.

## Browser automation
Project's existing library. Role/text/test-id locators over long CSS/XPath. Wait on conditions, never fixed sleeps. Headless in production; screenshot/trace on failure. Session/cookie files out of git.

## Bots
Validate every command and argument. Admin commands behind a user-ID allowlist. Production webhooks verify the platform secret/signature; polling is fine in dev. Handle platform rate limits; short help for unknown commands.

## Email / SMS / messaging
- Dry-run or sandbox mode by default in development.
- Consent and opt-out handling; follow provider policies and applicable law.
- Email: SPF/DKIM/DMARC on the sending domain; escape user data in templates.
- Throttle to the provider's documented limits.

## Verify
Run once on a small real or fixture input, run again to confirm no duplicates. Retry logic changed → simulate a failure.
