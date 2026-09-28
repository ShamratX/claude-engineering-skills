---
name: web-development
description: Build or change websites, frontends, backends, APIs, and CMS sites (React, Node.js, or any web stack). Use for pages, components, routes, API endpoints, forms, data fetching, styling, SSR, and CMS themes/plugins/content models. Not for smart contracts (web3-development) or bots/scrapers (automation-bots).
---

# Web Development

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: use `caveman shrink -- <cmd>` for installs, builds, dev-server logs, and full lint runs. Keep full: the first compile/type error, the failing request/response, hydration and console errors.

## Context
- **Stack once:** manifest deps + scripts, then framework config (`next.config.*`, `vite.config.*`, etc.) only if the task touches build, routing, or env.
- **Then the target:** the page/component/route/handler the task names → its direct imports → types/schemas → the test that covers it.
- **Conventions from one example:** read one existing sibling (another route, form, or component) and copy its pattern instead of surveying many.
- **Versions matter:** grep the lockfile or manifest when behavior differs by major (React 18/19, Next pages/app router, Express 4/5, Tailwind 3/4).
- **Styling:** identify the system from the file you're editing. Read theme/tokens only when changing them.
- **CMS:** identify the CMS and its version. Read the theme/plugin/schema file tied to the task, never CMS core.

## Build
- Match the existing framework, router, state, data fetching, styling, and folder structure.
- New dependency only when existing deps or the platform can't do it reasonably. State why.
- Keep the separation already there (route → service → data). Add a layer only when duplication or testability demands it.
- **Frontend:** loading/error/empty states for async data; semantic HTML, input labels, `alt` text, visible keyboard focus; responsive by default; API URLs from env config.
- **Backend:** validate input at the boundary with the project's validator; consistent response shape and correct status codes; no stack traces to clients; parameterized queries/ORM; server-side authorization; pagination on list endpoints; timeouts on outbound calls.
- **Performance:** fix measured or obvious problems (N+1 queries, requests in loops, oversized bundles or images). No speculative memoization or caching.

## Verify
Narrowest first: typecheck/lint the touched files → related tests → build. Use the project's own scripts.
UI change → load the page in the dev server and check the console, or say it wasn't checked. API change → one real request (`curl` or equivalent).

## Pitfalls
- Client-exposed env vars (`NEXT_PUBLIC_*`, `VITE_*`) are public. No secrets there.
- Server/client boundary bugs: hydration mismatch, browser APIs during SSR, server-only imports in client code.
- CORS, cookie `SameSite`/`Secure`, and base URLs differ between dev and prod.
- Stale cache or build output after config changes. Restart or clear before concluding.

Pair with `testing` for test work and with `security` for auth, payments, uploads, or user-controlled input.
