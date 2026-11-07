<!-- format: 13-section -->
# GPU-bound workloads

## 1. Purpose and applicability
Work limited by GPU execution or GPU-CPU transfer (rendering, compute, video effects, inference on GPU). Applies only to apps that already use the GPU.

## 2. Detection signals
Frame time or batch time tracks GPU time; CPU waits on GPU; GPU profilers show high utilization or transfer stalls.

## 3. What to inspect
Draw/dispatch counts, shader cost, overdraw, texture sizes, transfers per frame, pipeline/shader compilation, synchronization points, device-loss handling.

## 4. Metrics
GPU time per pass, frame time p95/p99, VRAM use, transfer bandwidth, shader compile stalls.

## 5. Common bottlenecks and anti-patterns
Per-frame uploads; overdraw; huge textures; shader hitching; stalls from synchronous readbacks.

## 6. Candidate optimization techniques
Batch draws, cache pipelines, reduce transfers, scale render resolution within quality bounds, pick backend by capability (RACE).

## 7. Runtime tunables versus build-time changes
Runtime: render scale, batch size, pipeline cache size, backend selector. Build-time: shader variants, new backends.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Backend and budgets are RACE; culling/algorithm fixes are universal.

## 9. Compatibility and version considerations
Driver differences are common; test fallbacks; record driver versions.

## 10. Security, privacy, accessibility, data integrity
Respect accessibility (motion, contrast); never degrade required fidelity.

## 11. Validation and benchmark methodology
Compare GPU time and frame time distributions with warm-up; image diff for equivalence; no stress tests for non-GPU apps.

## 12. Rollback considerations
Revert to baseline backend/scale on hang, reset or visual defect.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
