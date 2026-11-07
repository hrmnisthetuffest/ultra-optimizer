<!-- format: 13-section -->
# CPU-bound workloads

## 1. Purpose and applicability
Work whose wall time is dominated by CPU execution (parsing, compression, crypto, simulation, layout, image processing). Use after profiling shows high CPU utilization with little waiting.

## 2. Detection signals
Profiler shows hot functions with high on-CPU time; adding cores or faster code reduces time; IO and GPU waits are small.

## 3. What to inspect
Hot loops, algorithmic complexity, allocation in hot paths, thread pool sizing, lock contention, vectorization opportunities, compiler/build settings.

## 4. Metrics
CPU time per operation, single-thread and parallel speedup, instructions-per-cycle if measurable, p95 latency, throughput.

## 5. Common bottlenecks and anti-patterns
Wrong complexity class; unnecessary copying; contended locks; oversubscribed threads; scalar loops that could vectorize; hot-path logging.

## 6. Candidate optimization techniques
Fix algorithms first (universal); reduce allocations; batch work; size pools from measured scaling; choose SIMD paths via capability detection (RACE); use cheaper data layouts.

## 7. Runtime tunables versus build-time changes
Runtime: pool size, chunk size, SIMD path selector. Build-time: algorithm, layout, compiler flags.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Pool size and SIMD path are RACE; complexity and data-structure fixes are universal.

## 9. Compatibility and version considerations
Parallelism changes can alter floating-point results and ordering; keep documented determinism guarantees.

## 10. Security, privacy, accessibility, data integrity
Constant-time code must stay constant-time; do not trade correctness or precision for speed silently.

## 11. Validation and benchmark methodology
Profile before/after on a fixed workload; compare outputs byte-for-byte or within declared tolerance; repeat for noise.

## 12. Rollback considerations
Revert tunable to default; keep previous algorithm behind a flag until validated.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
