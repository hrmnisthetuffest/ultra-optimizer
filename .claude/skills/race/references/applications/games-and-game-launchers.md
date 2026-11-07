<!-- format: 13-section -->
# Games and game launchers

## 1. Purpose and applicability
Real-time rendering and simulation apps; launchers/overlays.

## 2. Detection signals
Engine markers (Unity, Unreal, Godot, custom), graphics API usage.

## 3. What to inspect
Frame loop, draw calls, asset streaming, shader compilation, physics, memory/VRAM budgets, loading screens.

## 4. Metrics
Frame time p95/p99, hitches, load time, VRAM, CPU frame breakdown.

## 5. Common bottlenecks and anti-patterns
Hitching from shader compile or asset streaming; CPU-bound draw submission; unbounded VRAM.

## 6. Candidate optimization techniques
Pipeline caches, streaming budgets from detected VRAM, quality tiers within declared limits (RACE), job-system sizing.

## 7. Runtime tunables versus build-time changes
Runtime: render scale, texture budget, thread count, shader cache. Build-time: asset packing.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: lowering gameplay-relevant fidelity silently, touching graphics-driver control-panel settings, anti-cheat bypass.

## 9. Compatibility and version considerations
Console/PC targets differ; follow platform certification rules.

## 10. Security, privacy, accessibility, data integrity
Do not weaken anti-cheat or DRM-related integrity; honor accessibility options.

## 11. Validation and benchmark methodology
Capture scripted scenes; measure p95/p99 and hitches; soak tests.

## 12. Rollback considerations
Revert quality tier to baseline on device reset or crash.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
