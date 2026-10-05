---
name: visual-direction
description: Visual and image direction for websites and apps - deciding whether each section needs imagery, which type (photo, illustration, icon, diagram, chart, screenshot, video, 3D, or none), art direction, sourcing and licensing, alt text, and image delivery (formats, sizes, loading). Not an image generator. Not for overall visual style and typography (frontend-design), layout/UX (ui-ux-design), or animation (motion).
---

# Visual Direction

## Context
- Brand assets, existing photography/illustration style, and the design direction from `frontend-design` if one exists.
- Real assets available from the user (product photos, team, locations, screenshots). Real beats generic.

## Decide per section
For each section ask: what must the visitor understand or feel here, and does an image do that better than text or whitespace?
- **None:** when the image would only decorate. Default for dense text, forms, legal, and most UI chrome.
- **Photo:** real people, places, products, proof. Use the client's own; stock only when generic is acceptable.
- **Product screenshot/UI:** software features; current, cropped to the relevant part, not blurry mockups.
- **Illustration:** abstract concepts, onboarding, empty states; one consistent style per project.
- **Icon:** scannable lists and navigation; one icon set, consistent stroke and size; never the only label. See Iconography.
- **Diagram/chart:** processes, comparisons, data; must be accurate and labeled.
- **Video/animation/3D:** only when motion or spatial understanding is the point; hand to `motion` or `threejs-3d`.

## Art direction
Define once: subject matter, mood, color treatment, lighting, framing/crop, and what to avoid (clichés such as handshakes, generic laptops, stock smiles). Keep it consistent across the site. Images support the hierarchy; they never compete with the primary action.

## Iconography
Icon choice is a design decision, not a placeholder.
- **System:** reuse the project's existing icon set when it fits. Otherwise pick one reputable, maintained, permissively licensed library whose style (outline/filled, stroke, corner radius, visual weight) matches the brand and platform (SF Symbols on iOS and Material Symbols on Android when native). One family per project; don't mix libraries without a real need.
- **Consistency:** same size scale, stroke weight, optical weight, alignment to text baseline, and spacing everywhere.
- **Meaning:** use widely understood metaphors for the context; ambiguous icons get a visible text label; icon-only buttons get an accessible name (`aria-label`) and a tooltip where helpful; decorative icons are hidden from screen readers.
- **No emojis** as UI icons unless the user asks or it genuinely fits the brand.
- **Logos:** never draw or approximate brand/product logos; use official assets under their usage terms.
- **Lean:** import only the icons used (tree-shaken per-icon imports or an SVG sprite); no whole-library bundles, icon fonts for a handful of icons, or unused icon files. Custom SVG icons only when the library lacks the meaning, drawn to the same grid and stroke.

## Honesty and rights
- Never fabricate real people, testimonials, customers, awards, locations, or product photos. Generated or stock images must not pose as real customers, staff, or results.
- Sourcing order: user-provided → licensed stock (record source and license) → AI-generated only if the user agrees. Note any required attribution.

## Delivery
- Alt text describes the content or function; decorative images get `alt=""`.
- Formats: SVG for icons and logos; AVIF/WebP with a fallback for photos; compress to the smallest acceptable quality.
- Responsive `srcset`/`sizes`; explicit `width`/`height` (or aspect ratio) to prevent layout shift.
- The LCP image loads eagerly with high fetch priority; below-the-fold images lazy-load.

## Deliver
A table: section · visual (or none) · type · subject/composition · source · alt text. Then the shared art-direction notes.
