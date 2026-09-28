---
name: security
description: Security-focused work - audits and security reviews, vulnerability fixes, secrets handling, authentication/authorization logic, and pre-ship security checks for web apps, APIs, bots, and smart contracts. Use when security is the task or the change alters auth, permissions, payments, keys, or trust boundaries; not for routine feature work.
---

# Security

**Caveman** (check/install per CLAUDE.md): shrink bulk scanner output (`npm audit`, `pip-audit`, Slither), then read every High/Critical finding in full. Keep full: vulnerable lines, attack paths, security warnings (complete sentences).

## Context: the exception to skim-reading
- **Scope:** the diff (`git diff main...`), the named feature, or entry points (routes, handlers, public/external functions, bot commands, webhooks).
- **Read the complete path** from untrusted input to each sink (DB, shell, filesystem, HTML, outbound request, value transfer) for in-scope entry points. Partial reads miss vulnerabilities.
- Include its guards: auth middleware, access-control modifiers, validation schemas, security config (CORS, CSP, cookies, headers), involved dependency versions.
- Code the data never reaches stays unread.
- **Secrets:** grep tracked files and the diff for key patterns; confirm `.gitignore` covers `.env`. Report location, never the value.

## Checks
- **Secrets:** none in code, config, logs, or git history. Leaked → must be rotated (user action); history rewrite is secondary.
- **Input:** validate type/length/format/range at the boundary with allowlists. Parameterized queries. No user input in shell strings (argument arrays). Framework escaping, no raw HTML sinks with user data. Normalize and confine file paths. Allowlist server-side outbound URLs (SSRF).
- **Auth:** argon2/bcrypt passwords; server-side authorization per action and object (IDOR); `HttpOnly`/`Secure`/`SameSite` cookies; short-lived tokens; rate limits on login/signup/reset; CSRF protection for cookie auth.
- **Errors/logs:** no internals to clients; no secrets or personal data in logs; log sensitive actions.
- **Dependencies:** audit High/Critical; verify a package is legitimate and maintained before adding; commit lockfiles.
- **Bots/webhooks:** verify signatures, allowlist admins, rate-limit commands.
- **Smart contracts:** reentrancy (incl. cross-function, read-only); access control; oracle manipulation/staleness; front-running, slippage, MEV; flash-loan assumptions; signature replay (nonce, chain ID, EIP-712); unchecked low-level calls; `delegatecall`; `tx.origin` auth; block-value randomness; DoS via unbounded loops or revert-in-loop; rounding/precision; upgradeable storage and initializers; centralization risk. Run Slither and fuzz/invariant tests when available. Recommend an external audit before significant mainnet value.

## Fixing
Minimal, at the root (boundary validation, parameterization, server-side authz). No security theater. Add a test proving the exploit is closed.

## Report
Per finding: `Severity | file:line | exploit scenario | fix`. Unconfirmed → "possible" plus the condition. Authorized, defensive work on the user's own code only.
