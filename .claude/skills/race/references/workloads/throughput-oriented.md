<!-- format: 13-section -->
# Throughput-oriented workloads

## 1. Purpose and applicability
Work judged by items per time (batch jobs, encoding, indexing, bulk imports).

## 2. Detection signals
Large queues; success measured by completion time; latency per item matters little.

## 3. What to inspect
Batching, parallelism, pipeline stages, backpressure, resource contention with foreground work.

## 4. Metrics
Items/sec, total completion time, resource use, error rate.

## 5. Common bottlenecks and anti-patterns
Too small batches; oversubscription hurting foreground; no backpressure.

## 6. Candidate optimization techniques
Tune batch and pool sizes by measurement, pipeline stages, run heavy work when idle and safe (see scheduling reference).

## 7. Runtime tunables versus build-time changes
Runtime: batch size, workers, queue depth. Build-time: pipeline structure.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Sizes from measured hardware are RACE; algorithm and pipeline fixes are universal.

## 9. Compatibility and version considerations
Resumable jobs and idempotence must be preserved.

## 10. Security, privacy, accessibility, data integrity
Keep result correctness and ordering guarantees.

## 11. Validation and benchmark methodology
Compare total time and resource use on fixed input sets; verify outputs identical.

## 12. Rollback considerations
Revert sizes; ensure partial work can resume.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
