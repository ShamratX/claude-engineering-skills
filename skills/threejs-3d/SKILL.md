---
name: threejs-3d
description: 3D on the web - Three.js scenes, React Three Fiber (R3F) and drei, WebGL/WebGPU rendering, cameras, lights, materials, glTF models and textures, 3D interaction (raycasting, controls), shaders, and 3D performance. Use when a task builds or fixes a 3D scene, viewer, configurator, or 3D hero. Not for 2D/DOM/SVG animation (motion) or deciding whether a page needs 3D at all (visual-direction).
---

# Three.js / 3D Web

## Context
- `three` version (and `@react-three/fiber`, `@react-three/drei` if React) from the lockfile. APIs, import paths, and defaults change between releases: check the installed version and the official docs/changelog before using an API you are unsure of.
- Existing scene setup, render loop, and asset pipeline: extend it; don't create a second renderer or loop.
- Target devices: mobile GPUs and battery set the budget.

## Route
- Core concepts (renderer, scene, camera, lights, materials, color management, resize, loop, disposal): `references/fundamentals.md`.
- React project: `references/r3f.md`. Use R3F only when the project already uses React; vanilla Three.js otherwise.
- Models, textures, compression, loaders: `references/assets.md`.
- Slow frames, memory growth, mobile issues: `references/performance.md`.

## Rules
- 3D must earn its cost: it explains a product or space, or it is the experience. Decorative 3D on a content page needs a lightweight static fallback.
- **Accessibility:** the canvas is invisible to screen readers. Key information also exists as HTML text. Honor `prefers-reduced-motion` (stop auto-rotation and camera moves). Interactive controls need keyboard alternatives or equivalent HTML controls.
- **Robustness:** handle WebGL being unavailable or the context being lost with a visible fallback. Load assets with progress and error states.
- **Lifecycle:** one render loop; pause it when the canvas is off-screen or the tab is hidden; dispose geometries, materials, textures, and render targets when removing objects or unmounting.
- **Responsiveness:** update camera aspect and renderer size on resize; cap pixel ratio at 2.

## Verify
Run it: no console errors or WebGL warnings; acceptable frame rate on a throttled CPU or a real mid-range phone; resize, reduced motion, and fallback paths work; memory stable after mounting and unmounting the scene a few times.
