# Local SEO

In-house reference. Facts below were checked against Google's own documentation on 2026-10-05 (sources at the end); re-check before relying on anything rich-result or policy related.

## Google Business Profile (the user's action; guidance only)
- **Name** = the real-world business name as used on the storefront, website, and stationery. No keywords, city names, or slogans added. Address, service area, hours, and category belong in their own fields.
- **Service-area businesses** (serve customers at their locations): one profile for the central office with a designated service area; no "virtual" office unless staffed during business hours. Hybrid businesses (storefront plus on-site service) follow Google's hybrid rules.
- **One profile per location.** No duplicate profiles for the same location.
- **Phone and website** connect to that location, under the business's direct control; a local number instead of a central call-center number where possible; no redirecting or referral numbers/URLs.
- **Categories:** as few as possible, as specific as possible, representative of the core business; never categories used as keywords.

## Website
- **NAP** (name, address, phone) identical everywhere: site footer or contact page, Business Profile, major directories. Same abbreviations and phone format.
- **Location pages:** one page per real location, with content unique to it (address, hours, staff, directions, services offered there, local proof). Service-area businesses: one page per service area only when it has genuinely distinct, useful content.
- **No doorway pages:** never generate near-identical pages per city or neighborhood that funnel to one page; Google's spam policies name "multiple ... pages targeted at specific regions or cities that funnel users to one page" as doorway abuse.
- **Contact basics:** clickable phone (`tel:`), real address text (not only an image or map), opening hours, a map embed or directions link on the contact/location page.
- **Titles/H1:** service + place + brand where it reads naturally (e.g. "Emergency Plumber in Leeds | Smith & Sons"); never keyword lists.

## Structured data (JSON-LD)
- Use `LocalBusiness` with the **most specific subtype** (e.g. `Plumber`, `Dentist`, `Restaurant`); several types can be combined in `@type` for multi-service businesses. Google requires `name` and `address`; also add `telephone`, `url`, `openingHoursSpecification`, `geo`, `image`, `priceRange` when true and available. One `LocalBusiness` entity per location page. General JSON-LD examples: the `seo-content` skill.
- **No self-serving review stars:** a business's own `aggregateRating`/`Review` markup about itself on its own site is not eligible for review stars in Google. Add `aggregateRating` only on sites that collect reviews about *other* businesses.
- **FAQ rich results** stopped showing in Google Search on 2026-05-07 for all sites (documentation removed 2026-06-15); **HowTo** rich results were retired in 2023. Visible FAQ content can still help readers, and `FAQPage` stays valid Schema.org; don't promise a rich result.
- Markup must match visible page content. Validate with Google's Rich Results Test.

## Reviews (process advice, not code)
- Ask every real customer; make leaving a review easy (direct link). Never incentivize, gate, or fake reviews; never post reviews on behalf of customers.
- Reply to reviews, especially negative ones, factually and without personal data.

## Measure
Search Console (queries with the city/service, location pages' impressions), Business Profile insights, calls and direction requests. Rankings vary by searcher location; don't report a single "rank" as fact.

## Sources (accessed 2026-10-05)
- Google Search Central, Local business structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business (last updated 2026-09-08)
- Google Search Central, Review snippet guidelines (self-serving reviews): https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Google Search Central, FAQ structured data and documentation updates (FAQ rich results retired 2026-05-07, per Google's documentation-updates changelog, checked 2026-10-10; HowTo no longer shown): https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Google Search Central, Spam policies (doorway abuse): https://developers.google.com/search/docs/essentials/spam-policies (last updated 2026-08-28)
- Google Business Profile Help, Guidelines for representing your business: https://support.google.com/business/answer/3038177
