---
name: security
description: Security-sensitive work - secrets, authentication/authorization, untrusted input, dependency risk, security reviews and audits, vulnerability fixes, and pre-ship checks for web apps, APIs, bots, and smart contracts. Use when a task touches auth, payments, user data, keys, or external input, or asks for an audit.
---

# Security

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: shrink bulk scanner output (`npm audit`, `pip-audit`, Slither), then read every High/Critical finding in full. Keep full: vulnerable code lines, attack paths, and security warnings. Warnings go in complete sentences.

## Context: the exception to skim-reading
- **Scope first:** the diff (`git diff main...`), the named feature, or the entry points (routes, handlers, public/external functions, bot commands, webhooks).
- **For each in-scope entry point, read the complete path** from untrusted input to sink (DB, shell, filesystem, HTML, outbound request, value transfer). Partial reads miss vulnerabilities.
- Always include what guards that path: auth middleware, access-control modifiers, validation schemas, security config (CORS, CSP, cookies, headers), and the dependency versions involved.
- Code the data never flows into stays unread.
- **Secrets:** grep tracked files and the diff for key patterns, and check that `.gitignore` covers `.env`. Report *where* a secret is, never its value.

## Checks
- **Secrets:** none in code, config, logs, or git history. A leaked secret must be rotated (user action); rewriting history is secondary.
- **Input:** validate type, length, format, and range at the boundary with allowlists. Parameterized queries. No user input in shell strings (use argument arrays). Framework escaping, no raw HTML sinks with user data. Normalize and confine file paths. Allowlist server-side outbound URLs (SSRF).
- **Auth:** argon2/bcrypt for passwords; server-side authorization on every protected action and object (IDOR); `HttpOnly`/`Secure`/`SameSite` cookies; short-lived tokens; rate limits on login, signup, and reset; CSRF protection for cookie auth.
- **Errors and logs:** no internals to clients; no secrets or personal data in logs; log sensitive actions.
- **Dependencies:** audit High/Critical; check that the package is legitimate and maintained before adding it; commit lockfiles.
- **Bots and webhooks:** verify signatures, allowlist admins, rate-limit commands.
- **Smart contracts:** reentrancy (including cross-function and read-only); access control on privileged functions; oracle manipulation and staleness; front-running, slippage, and MEV; flash-loan assumptions; signature replay (nonce, chain ID, EIP-712); unchecked low-level call results; `delegatecall`; `tx.origin` auth; block-value randomness; DoS from unbounded loops or a revert in a loop; rounding and precision; upgradeable storage and initializers; centralization risk. Run Slither and fuzz/invariant tests when available. Recommend an external audit before significant mainnet value.

## Fixing
Fix minimally at the root: validate at the boundary, parameterize, authorize server-side. No security theater. Don't break existing behavior silently; add a test that proves the exploit is closed.

## Report
Per finding: `Severity | file:line | exploit scenario | fix`. Unconfirmed → mark it "possible" and state the condition. Authorized, defensive work on the user's own code only.
