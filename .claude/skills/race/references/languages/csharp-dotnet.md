<!-- format: 13-section -->
# C# and .NET

## 1. Purpose and applicability
Language/runtime-specific optimization guidance. Detect the real stack from manifests and lockfiles first.

## 2. Detection signals
Manifests/lockfiles: .

## 3. What to inspect
Runtime and memory model: managed runtime with generational GC and JIT/AOT options.

## 4. Metrics
Use the profilers listed in section 11; track wall time, CPU time, allocations and tail latency.

## 5. Common bottlenecks and anti-patterns
Common traps: LINQ in hot paths; allocations causing gen2 GCs; sync-over-async; boxing.

## 6. Candidate optimization techniques
Idiomatic optimizations: Span/Memory, pooling, ValueTask where measured, async IO, struct layout.

## 7. Runtime tunables versus build-time changes
Build/compiler levers: tiered compilation, ReadyToRun/AOT, trimming - verify reflection use first.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven pool, cache and path choices via registered tunables. /optimize: algorithm, data structure and build fixes. Interop: P/Invoke: keep fallbacks.

## 9. Compatibility and version considerations
Pin and respect the project's language/runtime versions; check release notes before relying on version-specific behavior.

## 10. Security, privacy, accessibility, data integrity
Keep security checks, input validation and accessibility intact; do not disable safety features (bounds checks, sanitizers in test) for speed without approval.

## 11. Validation and benchmark methodology
Profiling tools: dotnet-trace, dotnet-counters, BenchmarkDotNet, PerfView. Tests: xUnit/NUnit suites, BenchmarkDotNet.

## 12. Rollback considerations
Keep the change behind a flag or in a separate commit so it reverts cleanly.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
