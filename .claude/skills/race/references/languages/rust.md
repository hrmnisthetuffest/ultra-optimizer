<!-- format: 13-section -->
# Rust

## 1. Purpose and applicability
Language/runtime-specific optimization guidance. Detect the real stack from manifests and lockfiles first.

## 2. Detection signals
Manifests/lockfiles: C

## 3. What to inspect
Runtime and memory model: ownership, no GC; threads and async runtimes; zero-cost abstractions.

## 4. Metrics
Use the profilers listed in section 11; track wall time, CPU time, allocations and tail latency.

## 5. Common bottlenecks and anti-patterns
Common traps: needless clones; allocation in hot paths; blocking inside async; debug builds measured.

## 6. Candidate optimization techniques
Idiomatic optimizations: borrow instead of clone, preallocate, iterator chains, SIMD via std/arch with runtime detection, rayon sized by capability (RACE).

## 7. Runtime tunables versus build-time changes
Build/compiler levers: profile settings (opt-level, LTO, codegen-units, panic strategy) - measure binary size and speed; never default to target-cpu=native for shipped binaries.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven pool, cache and path choices via registered tunables. /optimize: algorithm, data structure and build fixes. Interop: FFI: keep ABI stable.

## 9. Compatibility and version considerations
Pin and respect the project's language/runtime versions; check release notes before relying on version-specific behavior.

## 10. Security, privacy, accessibility, data integrity
Keep security checks, input validation and accessibility intact; do not disable safety features (bounds checks, sanitizers in test) for speed without approval.

## 11. Validation and benchmark methodology
Profiling tools: cargo bench/criterion, perf, flamegraph, cargo-llvm-lines. Tests: cargo test, miri where relevant, benchmarks.

## 12. Rollback considerations
Keep the change behind a flag or in a separate commit so it reverts cleanly.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
