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
- **Postgres** (schema, migrations, indexes, RLS, slow queries, connections, locking): `references/postgres/index.md` lists rules by impact; read only the matching rule files in that folder.
- **UI work:** existing design tokens, shared components, layout shell, fonts, and icon set; any reference designs, brand assets, or screenshots the user supplied (look at them, don't just list them).

## Design before code
New pages, redesigns, or substantial UI (skip for small fixes inside an existing design):
1. **Brief:** business, audience, the visitor's intent, the page's single conversion goal, and fixed constraints (brand, existing design system, content, stack). Missing and it changes the design → ask; otherwise state the assumption.
2. **Direction:** if the project has no recorded visual direction, set one with `ui-ux-design` (structure, flows, states) and `frontend-design` (type, color, composition), plus `visual-direction` for imagery, before writing substantial UI code. Write it down as a few concrete lines: type pairing and scale, color tokens, spacing scale, grid, component character, image treatment, motion stance.
3. **Content first:** real or client-confirmed copy (`content-copywriting`) drives the layout; no lorem ipsum in delivered work, and sections exist because the content needs them, not to fill a template.
4. **Existing design system wins:** extend its tokens and components; don't replace a working system or restyle unrelated pages. Changing it → explain why and ask.
5. **Every breakpoint is designed:** decide what changes at mobile, tablet, and desktop (navigation, column count, image crops, type scale, CTA placement), not just what stacks.

## Build
- Match the existing framework, router, state, data fetching, and styling. New dependency → state why existing ones can't do it.
- Keep existing layering (route → service → data).
- **Frontend:** loading/error/empty states; semantic HTML, labels, `alt`, visible focus; API URLs from env config.
- **Responsive by default** (no need to be asked): every page and component works on mobile, tablet, laptop, and desktop. Mobile-first CSS with the project's breakpoints; fluid layout, type, and media (`max-width: 100%`, `srcset`); no horizontal scroll; touch targets ≥ 44×44 px; no hover-only actions; tables, nav, and modals adapt on small screens. Techniques (fluid type/spacing, container queries, breakpoints, responsive tables): `references/responsive/fluid-layouts.md`, `container-queries.md`, `breakpoint-strategies.md`.
- **Backend:** validate input at the boundary with the project's validator; consistent response shape and correct status codes; no stack traces to clients; parameterized queries/ORM; server-side authorization; paginate lists; timeouts on outbound calls.
- **Performance:** fix measured or obvious issues (N+1, requests in loops, oversized bundles/images). No speculative memoization or caching.

- **Consistency:** spacing, type, color, radius, and shadow from tokens, not one-off values; one component per pattern (buttons, cards, form fields) reused everywhere.

## Verify
Project scripts only (build, lint, tests). API change → one real request.

**UI change → visual verification on the rendered page:**
1. Run the dev or preview server; load each changed page; check the console and failed network requests.
2. When a browser tool is available (browser MCP/extension, or Playwright/Puppeteer already in the project), capture screenshots at 360, 768, 1024, and 1440 px wide, full page, and look at them. Don't add a dependency only for screenshots without asking. Save screenshots outside the project (scratchpad/temp) and delete them afterwards.
3. Look for and fix: horizontal overflow, overlapping or clipped elements, broken or distorted images, unreadable contrast, cramped or uneven spacing, orphaned headings, inconsistent components, tap targets too small, sticky elements covering content.
4. Exercise the primary flow: navigation (including the mobile menu), links, forms (valid, invalid, submit), primary CTA.
5. Full pre-delivery checklist: `testing` skill (website QA).

No browser or screenshot available → say exactly which visual checks were not performed. Never describe a layout as verified from reading code alone.

## Pitfalls
- `NEXT_PUBLIC_*` / `VITE_*` vars ship to the client: no secrets.
- Server/client boundary: hydration mismatch, browser APIs during SSR, server-only imports in client code.
- CORS, cookie `SameSite`/`Secure`, and base URLs differ between dev and prod.
- Stale cache/build after config changes: restart or clear before concluding.
