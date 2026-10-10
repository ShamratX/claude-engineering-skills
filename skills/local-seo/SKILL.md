---
name: local-seo
description: Local SEO for businesses that serve a city or service area - local search intent, service-area research, service and location page architecture, local titles/headings/URLs/internal links, NAP consistency, LocalBusiness structured data, and local technical SEO checks. Use when building or auditing a site for a local business (trades, clinics, restaurants, agencies, shops). Not for general or international SEO (seo-content), writing the page copy itself (content-copywriting), or Google Business Profile management beyond guidance.
---

# Local SEO

General on-page, technical, and schema rules live in `seo-content`; load it alongside this skill. This skill adds what changes when the business is local.

## Context
- **Verified business facts:** legal/trading name, address or service-area-only status, phone, hours, services, areas actually served, licenses. Source: the user, the existing site, or the client's Business Profile. Missing → `[CONFIRM: ...]` placeholder; never invent an address, area, or phone.
- **Search intent:** what people in the area type (service + place, "near me", emergency/urgent variants, problem-led queries). Use the user's data (Search Console, Business Profile insights, call logs, ad reports) or keyword tools they provide; without data, propose terms as hypotheses and say so. Never state search volumes or rankings you didn't measure.
- **Existing site:** where titles, meta, canonical, sitemap, robots, and JSON-LD are generated (framework/CMS config, layout, SEO plugin). Change them at the source.
- Platform guidelines and their sources: `references/google-guidelines.md`. Re-check the cited Google pages when a decision depends on rich-result eligibility or spam policy.

## Site architecture
- **Service pages:** one page per distinct service a customer searches for separately, with its own process, inclusions, pricing approach, and FAQs. Thin variants merge into one page.
- **Location pages:** only for real locations, or service areas where the page has genuinely local content (jobs done there, local regulations, travel times, area-specific services, staff based there). No location → no page. Never generate city pages by swapping the place name; that is doorway abuse.
- **URLs:** `/services/<service>/`, `/locations/<city>/` or the project's existing pattern; short, lowercase, hyphenated, stable. Don't change live URLs without 301 redirects.
- **Internal links:** home → services and locations; each service ↔ relevant locations and related services; descriptive anchors ("drain cleaning in Leeds"), not "click here". No orphans.
- **Contact and NAP:** the same name, address, and phone (same format) in the footer, contact page, schema, and Business Profile; `tel:` links; address as text; hours; map or directions link on the contact/location page.

## On-page
- Title: service + place + brand where it reads naturally; unique per page. H1 states the page's service and area in plain words. Meta description: specific offer and next step, no keyword lists.
- Copy proves local relevance with facts, not repeated place names. Hand the writing to `content-copywriting`.
- Images: real photos of the business, team, work, and premises over stock; descriptive file names; alt text describes what's shown (place name only when it's actually in the image); sizes and formats per `visual-direction`.

## Structured data
- `LocalBusiness` with the most specific schema.org subtype, one entity per real location, values identical to the visible page and Business Profile. Service-area businesses: add `areaServed`; Google lists `address` as required, so use the real (possibly partial) address the client confirms, never an invented one, and say if the page won't be eligible.
- Add `openingHoursSpecification`, `geo`, `telephone`, `url`, `image`, `priceRange` only when true and known.
- No self-serving `aggregateRating`/`Review` markup; don't promise FAQ or HowTo rich results (see the reference).
- Other types (`BreadcrumbList`, `Service`, `Organization`) only when they match visible content.

## Technical
- Every service and location page: indexable (no stray `noindex`, not blocked in `robots.txt`), self-referencing canonical, in the XML sitemap, reachable by crawlable `<a href>` links.
- Duplicate or near-duplicate pages: merge, or canonicalize to the primary; parameter and filter URLs don't compete with landing pages.
- Mobile layout, page speed, and HTTPS matter for local searchers on phones; fixes belong to `web-development`.

## Never
Keyword stuffing; fake or virtual addresses; locations the business doesn't serve; doorway pages; fake reviews or review gating; hidden text; promising rankings, map-pack placement, traffic, or calls.

## Verify
Inspect the rendered page and the built source, not just templates: title, meta description, one H1, canonical, robots meta, `lang`; JSON-LD parses and matches the visible NAP; sitemap lists the new pages; internal links resolve; NAP identical across pages. Validate schema with Google's Rich Results Test or the Schema Markup Validator when available, otherwise say it wasn't validated.

## Report
Separate **implemented** (pages, metadata, schema, links, fixes, with paths) from **user actions** (Business Profile, citations, reviews, Search Console submission) and **outcomes that can't be guaranteed** (rankings, map-pack visibility, traffic).
