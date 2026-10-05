---
name: web-development
description: Build or change websites, frontends, backends, APIs, and CMS sites (React, Node.js, any web stack) - pages, components, routes, endpoints, forms, data fetching, styling, SSR, CMS themes/plugins/content models. Not for smart contracts (web3-development) or bots/scrapers (automation-bots).
---

# Web Development

**Caveman** (per CLAUDE.md): shrink installs, builds, dev-server logs, full lint runs. Keep full: first compile/type error, failing request/response, hydration and console errors.

## Context
- **Stack once:** manifest deps + scripts. Framework config (`next.config.*`, `vite.config.*`, ...) only if the task touches build, routing, or env.
- **Target:** the named page/component/route/handler → direct imports → types/schemas → covering test.
- **Conventions:** copy the pattern of one existing sibling; don't survey many.
- **Versions:** check the lockfile/manifest when behavior differs by major (React 18/19, Next pages/app router, Express 4/5, Tailwind 3/4).
- **Styling:** infer the system from the file being edited; read theme/tokens only when changing them.
- **CMS:** identify CMS + version; read the theme/plugin/schema file tied to the task, never CMS core.

## Build
- Match the existing framework, router, state, data fetching, and styling. New dependency → state why existing ones can't do it.
- Keep existing layering (route → service → data).
- **Frontend:** loading/error/empty states; semantic HTML, labels, `alt`, visible focus; responsive; API URLs from env config.
- **Backend:** validate input at the boundary with the project's validator; consistent response shape and correct status codes; no stack traces to clients; parameterized queries/ORM; server-side authorization; paginate lists; timeouts on outbound calls.
- **Performance:** fix measured or obvious issues (N+1, requests in loops, oversized bundles/images). No speculative memoization or caching.

## Verify
Project scripts only. UI change → load the page in the dev server and check the console, or say it wasn't checked. API change → one real request.

## Pitfalls
- `NEXT_PUBLIC_*` / `VITE_*` vars ship to the client: no secrets.
- Server/client boundary: hydration mismatch, browser APIs during SSR, server-only imports in client code.
- CORS, cookie `SameSite`/`Secure`, and base URLs differ between dev and prod.
- Stale cache/build after config changes: restart or clear before concluding.
