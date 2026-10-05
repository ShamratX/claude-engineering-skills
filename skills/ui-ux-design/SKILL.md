---
name: ui-ux-design
description: UX decisions for websites, web apps, Android, and iPhone/iPad apps - information architecture, navigation, user flows, screen states, forms, responsive behavior, accessibility, and platform conventions. Use when deciding how a product or screen should work. Not for visual style or anti-generic aesthetics (frontend-design), implementation code (web-development), imagery (visual-direction), or animation detail (motion).
---

# UI/UX Design

## Context
- Product goal, primary users, their top 1–3 tasks, and the platform(s). Unknown and it changes the design → ask; otherwise state the assumption.
- Existing design system, components, and navigation: reuse before inventing. Read one existing screen of the same type.
- Platform conventions: web → this file; iPhone/iPad → `references/ios.md`; Android → `references/android.md`. Cross-platform apps follow each platform's conventions on that platform.

## Decide
- **Structure:** content and tasks before layout. Group by user goals, not by internal system structure. Navigation depth ≤ 3 for primary tasks.
- **Flows:** shortest path for the primary task. Each step has one primary action. Destructive actions need confirmation or undo.
- **States** for every screen and component: loading, empty, error, partial, success, offline when relevant. Errors say what happened and how to fix it.
- **Forms:** fewest fields possible; labels always visible; correct input types and autocomplete; inline validation after the field is left; keep entered data on error.
- **Hierarchy:** one clear primary action per view; most important content first; progressive disclosure for advanced options.
- **Responsive (web):** design the narrowest layout first; no horizontal scroll; touch targets ≥ 44×44 px on touch devices; no hover-only functions.
- **Accessibility (WCAG 2.2 AA):** text contrast ≥ 4.5:1 (large text 3:1); full keyboard operation with visible focus; semantic headings and landmarks; labels for every control; no information by color alone; respect reduced motion and text scaling.
- **Consistency:** same name and same behavior for the same action everywhere.

## Deliver
State briefly: users and primary tasks, structure/navigation, key flows, screen list with required states, and the platform conventions applied. Hand visual style to `frontend-design` and implementation to `web-development` or the native stack.

## Verify
Walk each primary task step by step on the target platform and the narrowest viewport. Check keyboard-only use and screen-reader labels on web; system text size and dark mode on native.
