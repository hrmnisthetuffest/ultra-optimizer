<!-- format: 13-section -->
# C and C++

## 1. Purpose and applicability
Language/runtime-specific optimization guidance. Detect the real stack from manifests and lockfiles first.

## 2. Detection signals
Manifests/lockfiles: C

## 3. What to inspect
Runtime and memory model: manual memory/RAII; undefined behavior risks; compiler-dependent optimization.

## 4. Metrics
Use the profilers listed in section 11; track wall time, CPU time, allocations and tail latency.

## 5. Common bottlenecks and anti-patterns
Common traps: UB from aggressive changes; false sharing; virtual call overhead in hot loops; header bloat; -march=native shipping.

## 6. Candidate optimization techniques
Idiomatic optimizations: cache-friendly layouts, avoid allocation in loops, SIMD with runtime dispatch, restrict aliasing only when proven.

## 7. Runtime tunables versus build-time changes
Build/compiler levers: optimization levels, LTO/PGO as measured options, ABI compatibility.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven pool, cache and path choices via registered tunables. /optimize: algorithm, data structure and build fixes. Interop: ABI and header compatibility for libraries.

## 9. Compatibility and version considerations
Pin and respect the project's language/runtime versions; check release notes before relying on version-specific behavior.

## 10. Security, privacy, accessibility, data integrity
Keep security checks, input validation and accessibility intact; do not disable safety features (bounds checks, sanitizers in test) for speed without approval.

## 11. Validation and benchmark methodology
Profiling tools: perf, VTune-like profilers, valgrind/callgrind, sanitizers (ASan/UBSan/TSan) in test. Tests: unit tests under sanitizers, fuzzing for parsers.

## 12. Rollback considerations
Keep the change behind a flag or in a separate commit so it reverts cleanly.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
