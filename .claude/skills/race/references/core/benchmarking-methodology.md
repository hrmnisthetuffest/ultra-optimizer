<!-- format: 13-section -->
# Benchmarking methodology

## 1. Purpose and applicability
How to measure so results can be trusted. Applies to RACE L3 benchmarks, developer-time before/after comparisons, and any performance claim in reports.

## 2. Detection signals
Existing benchmark harnesses (`bench/`, `benchmarks/`, criterion, JMH, Benchmark.NET, pytest-benchmark, Lighthouse CI); CI performance jobs.

## 3. What to inspect
Workload representativeness; sources of noise (background load, thermal state, frequency scaling, caches, GC/JIT warm-up); available timers and their resolution.

## 4. Metrics
Startup and time-to-interactive; operation duration p50/p95/p99; throughput; frame time and dropped frames; CPU/GPU time; peak memory/VRAM; error rate; footprint; energy only when measured.

## 5. Common bottlenecks and anti-patterns
No baseline; single run; no warm-up; comparing different workloads; ignoring variance; synthetic test generalized to real use; fixed A-then-B order (drift biases B); unbounded stress; GPU stress for non-GPU apps; fabricated or remembered numbers.

## 6. Candidate optimization techniques
Method: capture baseline first; warm up; repeat enough to estimate noise; use comparable workloads; randomize or alternate (crossover) order; record thermal and background-load indicators; use robust statistics (median, percentiles, bootstrap or similar confidence intervals); report units, sample count and conditions. Categories: CPU single-thread and parallel, thread contention, GPU render/compute/transfer, memory, storage (only if relevant and safe), startup/TTI/operation duration.
Budget: active benchmarking targets about 5-10 minutes total (a target, not a mandate), bounded, with pause/resume/abort, stopping on user activity, thermal or battery limits. Never run unbounded stress.

## 7. Runtime tunables versus build-time changes
Runtime: repeat counts and time caps. Build-time: where the harness hooks into the app.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Which benchmark categories apply is workload- and hardware-dependent (RACE). Universal before/after comparisons for code changes use the same statistics but run on declared targets.

## 9. Compatibility and version considerations
Record OS, runtime, compiler, driver and app versions with every result; results from different versions are not comparable.

## 10. Security, privacy, accessibility, data integrity
Benchmarks use synthetic or consented data, never user content. They must not corrupt user data or leave temp files behind.

## 11. Validation and benchmark methodology
A claimed improvement needs: baseline and candidate on the same workload, N repeats, a stated interval, and a check that tests still pass. If the interval overlaps zero improvement, say "no measurable difference". Keep raw numbers in the `optimization-result` record.

## 12. Rollback considerations
If a candidate is slower, noisier, or breaks tests, revert it automatically and keep the evidence.

## 13. Authoritative sources and last-reviewed
Project spec section 5.4-5.5. Statistics practice is general; cite the specific tool's docs per integration. Last reviewed: 2026-11-07.
