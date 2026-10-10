---
name: content-copywriting
description: Website and marketing copy - headlines, hero and service descriptions, calls to action, FAQs, trust signals, about/contact sections, and rewriting, editing, or de-AI-ing existing page text for clarity, accuracy, and conversion. Use when writing or editing the words on a page. Not for search metadata, schema, or technical SEO (seo-content, local-seo), UI microcopy patterns inside app flows (ui-ux-design), or prompts (prompt-engineering).
---

# Content Copywriting

## Context
- **Brief:** who the reader is, what they came to do (search intent or referral context), what the business offers that alternatives don't, and the one conversion goal per page (call, book, buy, request a quote, sign up). Unknown and it changes the copy → ask; otherwise state the assumption.
- **Facts:** from the user, the existing site, or the client's real materials (Business Profile, brochures, price lists). Read the current page copy before rewriting it.
- **Voice:** existing brand voice and terminology first (site, socials, style guide). None → derive it from the audience and industry and state it in one line (e.g. "plain, calm, expert; no jargon").
- **Page role:** where the page sits in the site and which other page owns each neighbouring topic, so pages don't repeat each other.

## Write
- **Reader first:** answer "what is this, is it for me, why trust it, what do I do next" within the first screen. Lead with the outcome for the reader, then the how.
- **Specific over generic:** name the actual service, place, audience, process, timeframe, and what's included. Replace every sentence that could appear on a competitor's site unchanged.
- **Plain language:** short sentences, common words, active voice, one idea per paragraph. Define unavoidable jargon. Write at the reader's level, not below it.
- **Headlines:** state the benefit or the topic clearly; no puns or vague slogans that hide what's offered. Subheadings let a scanner understand the page without reading the body.
- **Service descriptions:** what it is, who it's for, the problem it solves, what happens step by step, what's included/excluded, and the next step. Use lists only for genuinely parallel items.
- **Calls to action:** verb + concrete result ("Book a free inspection", "Get a quote in 24 hours" only if true). One primary CTA per section; the same action uses the same label across the site. Say what happens after the click when it reduces friction.
- **FAQs:** real objections and questions (from the client, reviews, sales calls, search queries), answered directly in the first sentence. No filler questions written to stuff keywords.
- **Trust signals:** only verifiable ones the client supplied: licenses with numbers, real reviews with permission, named clients, guarantees with their actual terms, years in business, memberships. Show them near the decision they support.
- **Contact sections:** every way to reach the business, hours, service area, response time if known, and what to include in a message.
- **Frameworks:** headline formulas, section orders, and message tests ("Now you can", discomfort → vision → path) in `references/copywriting.md` and `references/copy-frameworks.md`; transitions in `references/natural-transitions.md`. These never override Accuracy below: where they suggest numbers, testimonials, or guarantees, use `[CONFIRM: ...]`.
- **Keywords** (from `seo-content`/`local-seo` when in scope): use them where a reader would naturally expect the words; never at the cost of readability.

## Accuracy (non-negotiable)
- Never invent testimonials, reviews, ratings, client names, certifications, awards, statistics, years of experience, team members, prices, warranties, guarantees, response times, or results.
- Missing fact → write a clearly marked placeholder such as `[CONFIRM: years in business]` and list every placeholder in the handoff. Never ship placeholder text silently.
- No unsupported superlatives ("best", "#1", "leading", "guaranteed") unless the client provides proof. Health, legal, financial, and safety claims need a source or are removed.
- Keep facts identical everywhere they appear (name, phone, hours, prices, service area).

## Edit pass
Remove: filler openers and closers, repeated points across sections, empty intensifiers, buzzwords, hedging stacks, awkward keyword phrasing, and anything the reader doesn't need. Check AI-sounding patterns in `references/ai-tells.md` (sentence shapes, with the self-check) and `references/ai-writing-detection.md` (words); fix from the facts, don't swap one stock phrase for another. Full edit of existing copy: the seven sweeps in `references/copy-editing.md` with `references/copy-editing-checklist.md` and `references/plain-english-alternatives.md`. Refreshing a published page: `references/content-refresh.md`.

## Deliver
Copy organized by page and section, in the order it appears. Then: voice line, assumptions, and the list of `[CONFIRM: ...]` items for the client.

## Verify
Read the copy in the rendered page, not only in the source: headings scan, CTAs match their destinations, nothing is truncated or orphaned at mobile width, no placeholder or lorem ipsum left unlisted, facts match across pages.
