# 3D assets

## Models
- Use glTF 2.0 binary (`.glb`). Convert other formats offline, not at runtime.
- Optimize before shipping: remove unused nodes, materials, and animations; merge where possible; compress geometry (Draco or Meshopt) and textures (KTX2/Basis). Tools such as the `gltf-transform` CLI do this; verify the tool and its options in its own docs before use.
- Loading compressed assets needs the matching decoder: `DRACOLoader`, `KTX2Loader`, or `MeshoptDecoder` configured on `GLTFLoader` (drei `useGLTF` handles Draco/Meshopt). Host decoder files locally or from a pinned version; don't point to an unpinned CDN path.
- Set a budget per scene (for example: triangle count, draw calls, total download size) and check models against it.

## Textures
- Power-of-two sizes are no longer required in WebGL2 but still mipmap and compress best. Use the smallest size that looks right at the largest on-screen size; 2048 px is usually the upper limit on mobile.
- Color maps sRGB; data maps linear (see `fundamentals.md`).
- Pack channels where the material supports it (e.g. AO/roughness/metalness in one texture for glTF ORM).

## Rights and provenance
Record the source and license of every model, texture, and HDRI (e.g. CC0, CC-BY with attribution, purchased license). Never ship assets of unknown origin.
