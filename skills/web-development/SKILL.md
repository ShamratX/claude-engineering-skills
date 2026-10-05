---
name: web-development
description: Build or change websites, frontends, backends, APIs, and CMS sites (React, Node.js, any web stack) - pages, components, routes, endpoints, forms, data fetching, styling, SSR, CMS themes/plugins/content models. Not for smart contracts (web3-development) or bots/scrapers (automation-bots).
---

# Web Development

## Context
- **Stack once:** manifest deps + scripts. Framework config (`next.config.*`, `vite.config.*`, ...) only if the task touches build, routing, or env.
- **Target:** the named page/component/route/handler → direct imports → types/schemas → covering test.
- **Conventions:** copy the pattern of one existing sibling; don't survey many.
- **Versions:** check the lockfile/manifest when behavior differs by major (React 18/19, Next pages/app router, Express 4/5, Tailwind 3/4).
- **React/Next.js performance:** `references/react/index.md` lists rules by impact; read only the rule files matching the task. Rules that suggest new packages or Vercel-only features don't override project conventions.
- **Styling:** infer the system from the file being edited; read theme/tokens only when changing them.
- **CMS:** identify CMS + version; read the theme/plugin/schema file tied to the task, never CMS core.

## Build
- Match the existing framework, router, state, data fetching, and styling. New dependency → state why existing ones can't do it.
- Keep existing layering (route → service → data).
- **Frontend:** loading/error/empty states; semantic HTML, labels, `alt`, visible focus; API URLs from env config.
- **Responsive by default** (no need to be asked): every page and component works on mobile, tablet, laptop, and desktop. Mobile-first CSS with the project's breakpoints; fluid layout, type, and media (`max-width: 100%`, `srcset`); no horizontal scroll; touch targets ≥ 44×44 px; no hover-only actions; tables, nav, and modals adapt on small screens.
- **Backend:** validate input at the boundary with the project's validator; consistent response shape and correct status codes; no stack traces to clients; parameterized queries/ORM; server-side authorization; paginate lists; timeouts on outbound calls.
- **Performance:** fix measured or obvious issues (N+1, requests in loops, oversized bundles/images). No speculative memoization or caching.

## Verify
Project scripts only. UI change → load the page in the dev server, check the console, and check widths 360, 768, 1024, and 1440 px (browser responsive mode or screenshots); otherwise say it wasn't checked. API change → one real request.

## Pitfalls
- `NEXT_PUBLIC_*` / `VITE_*` vars ship to the client: no secrets.
- Server/client boundary: hydration mismatch, browser APIs during SSR, server-only imports in client code.
- CORS, cookie `SameSite`/`Secure`, and base URLs differ between dev and prod.
- Stale cache/build after config changes: restart or clear before concluding.
