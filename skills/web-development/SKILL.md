---
name: web-development
description: Build and change web applications - frontend (React, Next.js, Vue, HTML/CSS), backend APIs (Node, Express, Python), and full-stack features. Use when creating pages, components, routes, API endpoints, or fixing web UI and server behavior.
---

# Web Development

## Workflow

1. **Understand the stack first.** Read `package.json` (or `requirements.txt`),
   the framework config, and one or two existing components or routes. Use the
   same framework, styling approach, and state management already in place.
2. **Plan the change.** List the files to touch: component, route, API
   handler, types, tests.
3. **Build in small steps.** Get one piece working end to end before adding
   the next.
4. **Run it.** Start the dev server and check the change in the browser, or
   call the endpoint with `curl`. Check the console and network tab for errors.
5. **Test and lint.** Run the project's test, lint, and type-check scripts.

## Frontend conventions

- Components: one component per file, small and focused, named in PascalCase.
- Keep data fetching out of presentational components where the project
  already separates them.
- Handle all three states for async data: **loading, error, and empty**.
- Accessibility: semantic HTML (`button`, `nav`, `main`), `alt` text on
  images, labels on inputs, keyboard focus visible.
- Responsive by default: test at phone width (~375px) and desktop.
- Do not hardcode API URLs; read them from environment config.

## Backend / API conventions

- Validate every input at the boundary (zod, joi, pydantic, etc.).
- Return consistent JSON shapes and correct HTTP status codes
  (200, 201, 400, 401, 403, 404, 409, 500).
- Never leak stack traces or internal errors to the client in production.
- Keep secrets in environment variables; document them in `.env.example`.
- Use parameterized queries or an ORM - never build SQL with string
  concatenation.
- Add pagination to list endpoints.

## Performance checklist

- [ ] Images sized and compressed; lazy-load below the fold
- [ ] No unnecessary re-renders (memoize only where measured)
- [ ] Heavy libraries imported only where needed (code splitting)
- [ ] API calls not repeated in loops (batch or cache)

## Before finishing

- [ ] Build passes with no new warnings
- [ ] Lint and type checks pass
- [ ] Feature works in the browser, including error and empty states
- [ ] No `console.log` debugging left behind
- [ ] New env variables added to `.env.example`
