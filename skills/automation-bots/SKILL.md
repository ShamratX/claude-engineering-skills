---
name: automation-bots
description: Build reliable automation - Telegram/Discord/WhatsApp bots, web scrapers, browser automation (Playwright, Puppeteer, Selenium), scheduled jobs, and API integrations. Use when writing scripts or services that run unattended.
---

# Automation & Bots

Automation runs without anyone watching, so it must be **reliable,
observable, and safe to re-run**.

## Workflow

1. Define the job: trigger (schedule, webhook, message), input, output, and
   what "done" looks like.
2. Check the target's rules: API terms, `robots.txt`, rate limits. Prefer an
   official API over scraping.
3. Build the smallest working version and run it once by hand.
4. Add error handling, retries, logging, and config.
5. Schedule or deploy it, then watch the first few runs.

## Reliability rules

- **Config in environment variables:** tokens, chat IDs, API keys, URLs.
  Never hardcode them. Provide `.env.example`.
- **Retries with backoff** for network calls (e.g. 3 tries, 1s → 2s → 4s).
  Do not retry on 4xx errors except 429.
- **Respect rate limits.** Add delays between requests; honor `Retry-After`.
- **Timeouts on every request.** No call should hang forever.
- **Idempotent jobs.** Re-running must not send duplicate messages or create
  duplicate records - track what was already processed.
- **Graceful shutdown.** Handle Ctrl+C / SIGTERM and finish or save the
  current item.

## Logging

- Log start, finish, item counts, and every error with context.
- Use timestamps and levels (INFO, WARN, ERROR).
- Never log tokens, passwords, or full personal data.
- For long-running bots, send a notification on crash or repeated failures.

## Browser automation

- Prefer Playwright. Use stable selectors (`data-testid`, roles, text) over
  long CSS/XPath chains.
- Wait for elements or network state, never fixed `sleep` calls.
- Run headless in production; save a screenshot on failure.
- Store login sessions securely and never commit cookie files.

## Bots (Telegram / Discord)

- Validate and sanitize every user command and argument.
- Restrict admin commands to an allowlist of user IDs.
- Reply to unknown commands with short help text.
- Use webhooks in production when possible; polling is fine for development.

## Running it

- Windows: Task Scheduler, or a process manager like `pm2`.
- Linux/servers: `systemd`, cron, `pm2`, or Docker with a restart policy.
- Document the start command in the README.

## Before finishing

- [ ] Runs end to end from a clean start
- [ ] Survives network failure (retries, then logs and continues)
- [ ] Running twice does not duplicate work
- [ ] No secrets in code or logs
- [ ] Start/stop instructions written down
