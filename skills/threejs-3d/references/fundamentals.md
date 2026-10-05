# Three.js fundamentals

Check the installed `three` version first; the notes below describe recent releases. Official docs: https://threejs.org/docs/ and the migration guide in the three.js GitHub wiki.

## Setup
- `WebGLRenderer({ antialias: true })` is the default choice. `WebGPURenderer` (imported from `three/webgpu` in recent versions) only when the project targets it and its features are needed; it uses node materials (TSL) instead of `ShaderMaterial`.
- `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`.
- Use `renderer.setAnimationLoop(fn)` (also required for WebXR) rather than a hand-rolled `requestAnimationFrame` loop; pass `null` to stop it.
- Resize: `camera.aspect = w / h; camera.updateProjectionMatrix(); renderer.setSize(w, h)`. Size from the canvas container, not always the window.
- Addons (controls, loaders, post-processing) import from `three/addons/...` in current versions; older projects use `three/examples/jsm/...`. Match the project.

## Color and lighting
- Color management: output color space sRGB (the default in recent versions). Color/albedo textures use `texture.colorSpace = THREE.SRGBColorSpace`; data maps (normal, roughness, metalness, AO) stay linear.
- Physically based materials (`MeshStandardMaterial`, `MeshPhysicalMaterial`) look right only with sensible lighting; an environment map (HDR via `RGBELoader`/PMREM or `RoomEnvironment`) usually gives the biggest quality gain for the lowest cost.
- Tone mapping (e.g. ACES Filmic or AgX, depending on version) plus exposure for a photographic look; keep it consistent across the scene.
- Shadows are expensive: enable per light and per mesh only where they matter; keep shadow map sizes and the shadow camera frustum tight.

## Cameras and interaction
- `PerspectiveCamera` with a sensible `near`/`far` ratio (avoid `near` = 0.0001 with large `far`: depth fighting).
- `OrbitControls` for viewers: limit zoom and polar angle; enable damping and call `controls.update()` each frame.
- Picking: `Raycaster` with normalized device coordinates from pointer events; raycast against a small list of candidate meshes, not the whole scene.

## Cleanup
Removing an object from the scene does not free GPU memory. Call `dispose()` on geometries, materials, textures, and render targets you created; dispose controls and the renderer when the canvas is torn down.
