---
name: motion
description: Web animation and motion - CSS transitions/animations, Web Animations API, JavaScript animation libraries (GSAP, Motion), scroll-triggered and scroll-driven effects, interaction and state-change animation, SVG/text animation, motion performance and reduced-motion accessibility. Not for 3D scenes (threejs-3d), native mobile platform transitions (ui-ux-design references), or deciding visual style (frontend-design).
---

# Motion

## Context
- Existing animation library and version from the manifest/lockfile. Existing library wins; add a new one only when the need can't be met otherwise, and say why.
- Where the motion happens (page load, scroll, hover/press, state change, route change) and what it communicates.

## Choose the tool
1. **CSS transitions/animations** for simple state changes, hovers, and entrances.
2. **Web Animations API** for simple JS-controlled sequences without a dependency.
3. **Library already in the project** (GSAP, Motion, etc.) for anything it already handles.
4. **GSAP** when there is no library and the work needs timelines, scroll-linked scrubbing/pinning, SVG morphing, FLIP layout transitions, or text splitting. Read only the matching reference:
   `references/gsap/core.md` (tweens, easing, stagger, matchMedia) · `timeline.md` · `scrolltrigger.md` · `plugins.md` (Flip, Draggable, SplitText, SVG) · `utils.md` · `react.md` · `frameworks.md` (Vue/Svelte/Nuxt) · `performance.md`.
   Those files recommend GSAP by default; this section's order takes priority.
- Scroll reveal without scrubbing → `IntersectionObserver` + CSS class, or the existing library. CSS scroll-driven animations (`animation-timeline`) only after checking current browser support for the project's targets.

## Rules
- **Purpose:** motion explains a change (what appeared, moved, or responded). Decorative motion is rare and deliberate; one orchestrated moment beats many scattered effects.
- **Timing:** micro-interactions about 100–200 ms; entrances/exits about 200–400 ms; large movements longer but rarely over 600 ms. Ease-out for entering, ease-in for leaving.
- **Performance:** animate `transform` and `opacity`; avoid `width`, `height`, `top`, `left`, and layout-triggering properties. `will-change` only on elements that actually animate. Pause or kill off-screen and unmounted animations.
- **Accessibility:** honor `prefers-reduced-motion` (crossfade or no animation, never parallax/large movement); nothing flashes more than 3 times per second; auto-playing motion longer than 5 s needs pause/stop; content and focus never depend on an animation finishing.
- **Frameworks:** create animations after mount, scope selectors to the component, clean up on unmount; never run animation code during SSR.
- **Layout stability:** entrance animations must not cause layout shift; reserve space first.

## Verify
Run the page: check smoothness in the browser's performance tools or by observation on a throttled CPU, test with reduced motion enabled, and confirm no console errors or leftover dev markers/devtools.
