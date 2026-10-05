# 3D performance

Measure first: `renderer.info` (draw calls, triangles, geometries, textures in memory), the browser performance panel, and a real mid-range phone. Fix the biggest cost, then measure again.

## Draw calls (usually the first limit)
- Many copies of one mesh → `InstancedMesh` (or drei `<Instances>`).
- Many static different meshes sharing a material → merge geometries (`BufferGeometryUtils.mergeGeometries`) or use `BatchedMesh` if the installed version has it.
- Share materials; each unique material can break batching.

## GPU work
- Pixel ratio capped at 2 (or lower adaptively when frame rate drops).
- Limit real-time shadows and post-processing passes; bake lighting/shadows into textures for static scenes.
- Use level of detail (`LOD` / drei `Detailed`) for distant objects; frustum culling is on by default, so keep bounding volumes correct after moving vertices.
- Transparent objects are sorted and drawn last; many overlapping transparent layers are expensive.

## CPU and memory
- No allocation inside the render loop (reuse vectors, matrices, and arrays).
- Render on demand for static scenes; pause the loop when off-screen (IntersectionObserver) or when the tab is hidden.
- Dispose replaced geometries, materials, textures, and render targets; watch `renderer.info.memory` for growth.

## Loading
- Show progress; load the hero asset first and the rest after first render.
- Compressed geometry and textures (see `assets.md`); serve with HTTP caching.
