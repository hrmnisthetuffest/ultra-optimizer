<!-- format: 13-section -->
# Workload analysis and classification

## 1. Purpose and applicability
Decide what the application is bound by, from evidence, so RACE tunes the right thing. Applies before registering tunables and again when profiling data arrives.

## 2. Detection signals
Static: hot loops, parallel code, GPU/compute calls, large buffers, file/DB/network I/O, UI frame loops, media pipelines. Dynamic: profiler or timing data from `profiling-levels.md`.

## 3. What to inspect
Primary user journeys; startup path; the heaviest operations; concurrency model; data sizes; whether work is interactive, batch, or real-time; existing timings and logs.

## 4. Metrics
Per operation: p50/p95/p99 latency, throughput, CPU time vs wall time, GPU time, allocations, bytes read/written, network wait, frame time, error rate. Utilization alone is not a classification.

## 5. Common bottlenecks and anti-patterns
Classifying from hardware specs; classifying from a synthetic microbenchmark; ignoring wait time (an app at 5% CPU that waits on I/O is not CPU-bound); one label for the whole app when phases differ.

## 6. Candidate optimization techniques
Classes and the usual lever: **cpu-bound** (parallelism, SIMD, algorithm); **gpu-bound** (backend, batch, resolution scaling within quality rules); **memory-bound** (layout, cache budget, pooling); **storage-bound** (prefetch, batching, compression); **network-bound** (batching, caching, concurrency); **latency-sensitive** (avoid blocking, defer work); **throughput-oriented** (batching, pools); **real-time** (deadline safety first, never add jitter); **mixed**; **software-algorithm-bound** (hardware tuning will not help; hand to a code change).

## 7. Runtime tunables versus build-time changes
Classification selects which registered tunables are eligible (`workload_categories` field). A software-algorithm-bound finding yields a developer-time code change, not a runtime tunable.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Hardware-dependent: pool sizes, SIMD/GPU path. Universal: algorithmic fixes are noted and reported as outside RACE; do not delegate by invoking the other command.

## 9. Compatibility and version considerations
Classification is per workload and per app version; re-evaluate after major updates or capability changes.

## 10. Security, privacy, accessibility, data integrity
Workload profiles hold aggregated timings only (`contains_user_content` must be false). Do not log file names, URLs, content or identifiers.

## 11. Validation and benchmark methodology
Confirm a classification with a targeted measurement (e.g., scale threads and watch throughput; vary data size; compare wall to CPU time). Record the evidence in `bottleneck_evidence`.

## 12. Rollback considerations
A wrong classification must be recoverable: tunables chosen from it follow the normal staged-apply/rollback path.

## 13. Authoritative sources and last-reviewed
Project spec sections 4.3 and 5. Measurement practice: see `benchmarking-methodology.md`. Last reviewed: 2026-11-07.
