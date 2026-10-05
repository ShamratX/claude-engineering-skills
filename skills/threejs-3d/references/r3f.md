# React Three Fiber (R3F) and drei

Check versions first: each R3F major targets a specific React major (see the R3F docs/changelog: https://r3f.docs.pmnd.rs). Don't upgrade one without the other.

## Patterns
- `<Canvas dpr={[1, 2]} camera={{ position, fov }}>`; wrap async content in `<Suspense fallback={...}>`.
- Per-frame updates in `useFrame((state, delta) => { ref.current.rotation.y += delta * speed })`: mutate refs, never `setState` per frame. Scale motion by `delta`, not frame count.
- Static or interaction-driven scenes: `frameloop="demand"` and call `invalidate()` after changes, so nothing renders while idle.
- Load models with drei `useGLTF` (supports Draco/Meshopt) and textures with `useTexture`; preload with `useGLTF.preload(url)` for known assets.
- Reuse geometries and materials across meshes (declare once, pass by reference or use `<Instances>`/`InstancedMesh` for many copies).
- Events: `onClick`, `onPointerOver`, etc. on meshes use raycasting internally; call `e.stopPropagation()` to stop hits passing through to objects behind.
- R3F disposes objects it created when they unmount; objects you create manually (e.g. `new THREE.Texture()` in a hook) need manual disposal.

## drei helpers worth using before writing your own
`OrbitControls`, `Environment`, `ContactShadows`, `Html` (DOM labels in 3D), `Text`, `Bounds`/`Center`, `useProgress` (loading UI), `PerformanceMonitor` (adaptive quality), `Detailed` (LOD). Confirm each exists in the installed drei version.

## SSR (Next.js etc.)
The canvas renders only on the client. Load the 3D component client-side (e.g. `'use client'` component, or dynamic import with SSR disabled) and give it a sized container to avoid layout shift.
