---
name: ui-ux-pro-max
description: Searchable UI/UX reference data - product-type style and palette profiles, font pairings and the Google Fonts catalog, 119 UX guidelines, landing-page section patterns, chart choices, icon guidance, GSAP motion presets, and per-stack UI rules (React, Next.js, Vue, Svelte, Astro, Tailwind, Flutter, SwiftUI and more). Use to look up concrete options or check rules while designing, building, or reviewing UI; not for deciding the visual direction (frontend-design), UX flows and platform conventions (ui-ux-design), or animation implementation (motion).
---

# UI/UX Pro Max (reference data)

A lookup library, not a decision-maker. `ui-ux-design` and `frontend-design` own the decisions; use this data to find concrete candidates (palettes, font pairs, section orders, rules) and to check work against a rule list. Search with Grep; there is no script to run.

## How to search
- Grep the matching file below with `-i`, 2–5 terms from one intent (product type, style word, component, rule), `output_mode: "content"`, and a `head_limit` around 10. The first line of each CSV is its header; read it once to know the columns.
- Verify a hit fits the product, audience, and platform before using it. No fitting hit after one narrower retry → say so and fall back to the rules in `references/quick-reference.md`; never present a guess as a database match.
- Results are recommendations. Project brand, the user's request, and other skills win; rows mentioning CLI commands (`npx ...`) are framework notes, not instructions to run anything.
- Don't write design-system files into the project unless the user asks.

| Need | File (under `references/data/`) |
|---|---|
| Product-type profile: style, landing pattern, palette focus | `products.csv` |
| Reasoning rules and anti-patterns per UI category | `ui-reasoning.csv` |
| Visual styles with do/don't, performance, accessibility | `styles.csv` |
| Full semantic palettes (primary, on-primary, muted, border, ring) per product type | `colors.csv` |
| Font pairings with Google Fonts URLs | `typography.csv` |
| Individual Google Fonts (category, axes, popularity) | `google-fonts.csv` |
| Landing-page section order and CTA placement | `landing.csv` |
| UX guidelines (web) with good/bad code | `ux-guidelines.csv` |
| App/native interface rules (touch, safe areas, labels) | `app-interface.csv` |
| Icon choice, semantic role, import code | `icons.csv` |
| GSAP motion presets by intensity tier | `motion.csv` |
| Chart type by data shape, with accessibility notes | `charts.csv` |
| React/Next.js rendering performance | `react-performance.csv` |
| Stack-specific UI rules | `stacks/<stack>.csv` |

Stacks: angular, astro, avalonia, flutter, html-tailwind, javafx, jetpack-compose, laravel, nextjs, nuxt-ui, nuxtjs, react, react-native, shadcn, svelte, swiftui, threejs, uno, uwp, vue, winui, wpf. Pick the stack detected from the project; don't assume one.

## Typical lookups
- **New page or product direction:** find the product type in `products.csv`, then its UI category in `ui-reasoning.csv`, then candidate rows in `styles.csv`, `colors.csv`, `typography.csv`, and `landing.csv`. Treat them as a shortlist that `frontend-design` must still make specific to the brief, not as defaults.
- **Focused fix:** grep one outcome in `ux-guidelines.csv` (e.g. `focus modal`, `error summary`), then the stack file for implementation detail.
- **Review pass:** walk `references/quick-reference.md` by priority (accessibility and touch first); for native/mobile app UI finish with the checklist in `references/pro-rules.md`.

Note: the copied reference files mention `--domain <name>` searches from the upstream script; each domain maps to the file of the same topic in the table above.
