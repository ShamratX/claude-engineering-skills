---
name: security
description: Apply secure coding practices and review code for vulnerabilities - secrets handling, input validation, authentication, dependency risks, web and smart contract security. Use before shipping, when handling user data or credentials, or when asked for a security review.
---

# Security

## Secrets

- Never hardcode API keys, private keys, seed phrases, passwords, or tokens.
- Store them in `.env` (in `.gitignore`) or a secrets manager. Commit only
  `.env.example` with placeholders.
- Before committing, search the diff for secrets
  (`git diff --cached | grep -iE "key|secret|token|password|private"`).
- If a secret was ever committed, treat it as leaked: **rotate it**. Removing
  it from history is not enough.
- Never print secrets in logs, errors, or chat output.

## Input and output

- Validate all external input: type, length, format, range. Use allowlists.
- **SQL injection:** parameterized queries or an ORM only.
- **XSS:** let the framework escape output; avoid `innerHTML` /
  `dangerouslySetInnerHTML` with user data.
- **Command injection:** never pass user input to a shell; use argument arrays.
- **Path traversal:** normalize and restrict file paths to an allowed folder.
- **SSRF:** do not fetch arbitrary user-supplied URLs from the server without
  an allowlist.

## Authentication and access

- Hash passwords with bcrypt or argon2 - never store plain text or use MD5/SHA1.
- Check authorization on the server for every protected action, not only in
  the UI.
- Use secure, `HttpOnly`, `SameSite` cookies; short-lived tokens.
- Rate-limit login, signup, and other sensitive endpoints.
- Use HTTPS everywhere.

## Dependencies

- Run `npm audit` / `pip-audit` and review high and critical findings.
- Prefer well-maintained packages; check before adding a new one.
- Commit lockfiles so installs are reproducible.

## Smart contract security

- Reentrancy: checks-effects-interactions + `ReentrancyGuard`.
- Access control on every privileged function.
- Integer handling: Solidity 0.8+ checks overflow, but watch `unchecked` blocks
  and precision loss in division (multiply before dividing).
- Do not use `tx.origin` for auth or `block.timestamp` / `blockhash` for
  randomness.
- Watch for front-running, price-oracle manipulation, and flash-loan attacks.
- Limit owner powers; document any that could harm holders.
- Run Slither; get an external audit before large mainnet deployments.

## Review checklist

- [ ] No secrets in code, config, logs, or git history
- [ ] All inputs validated at the boundary
- [ ] Auth and permission checks on the server side
- [ ] Error messages do not expose internals
- [ ] Dependencies audited
- [ ] Sensitive actions logged (without sensitive data)

## Reporting findings

For each issue give: **severity** (Critical / High / Medium / Low), **location**
(file:line), **what can go wrong** (a concrete attack scenario), and **the fix**.
Stay within authorized, defensive work on code the user owns.
