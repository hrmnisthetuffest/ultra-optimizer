<!-- format: 13-section -->
# GPU intelligence

## 1. Purpose and applicability
What to read about GPUs and how to select graphics/compute backends safely. Applies only to applications that use the GPU or could benefit from it; never stress the GPU for non-GPU apps.

## 2. Detection signals
Through the app's own graphics/compute API (Vulkan, Direct3D, Metal, OpenGL/ES, WebGPU/WebGL, CUDA, ROCm/HIP, OpenCL, DirectML): enumerate adapters, query device type (integrated, discrete, software), memory sizes, feature levels/extensions, compute limits, driver/API versions. Record `unknown` for anything the API does not return.

## 3. What to inspect
Which APIs and backends the app already supports; shader/compute workloads; memory transfer patterns; frame loop; multi-GPU/hybrid laptop behavior; fallback to CPU or software rendering; device-loss handling.

## 4. Metrics
Frame time p50/p95/p99, GPU time per pass, compute throughput, upload/download bandwidth, VRAM use, shader compile stalls, dropped frames, power/thermal behavior if measurable.

## 5. Common bottlenecks and anti-patterns
Choosing the backend by vendor name; assuming the OS picks the discrete GPU; unconditional CUDA requirements; transferring data every frame; shader compile hitches at first use; no device-loss recovery; changing global driver or graphics-control-panel settings (forbidden).

## 6. Candidate optimization techniques
Select among already-implemented backends by capability and a local measurement; scale internal resolution or batch size within declared quality limits; cache compiled pipelines/shaders in the app's own cache; reduce transfers; size VRAM budgets from reported memory with headroom; fall back to the baseline backend on error.

## 7. Runtime tunables versus build-time changes
Runtime: backend selector, render scale within bounds, batch size, pipeline cache size. Build-time: adding a new backend, shader permutations.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Backend and budget choices are RACE. Removing redundant draw calls or fixing O(n^2) culling is universal.

## 9. Compatibility and version considerations
Driver bugs and feature gaps vary; test the fallback on real devices where possible; record driver versions in results. NVIDIA compute capability: see `nvidia-gpu-architectures.md`. Take Metal, Direct3D and Vulkan feature-level tables from platform docs per project.

## 10. Security, privacy, accessibility, data integrity
GPU identifiers can fingerprint; store coarse classes. Quality reductions must respect accessibility (contrast, motion sensitivity) and any fidelity requirement (e.g., color-accurate editing).

## 11. Validation and benchmark methodology
Compare backends on a representative scene with warm-up; verify output equivalence (image diff or compute results within tolerance); test device-loss recovery by simulation where the API allows.

## 12. Rollback considerations
Persist last-known-good backend per capability class; on GPU hang/reset or visual defect, revert to the baseline backend automatically.

## 13. Authoritative sources and last-reviewed
Generic method; no vendor documents fetched for this file (specific claims **unverified**). `nvidia-gpu-architectures.md` holds one sourced record set. Last reviewed: 2026-11-07.
