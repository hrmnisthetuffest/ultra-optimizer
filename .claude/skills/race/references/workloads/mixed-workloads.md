<!-- format: 13-section -->
# Mixed workloads

## 1. Purpose and applicability
Applications with several bottleneck types or phases (most real applications).

## 2. Detection signals
Different phases show different bounds; profiles change by user action.

## 3. What to inspect
Per-phase profiles, shared resources, interference between background and foreground work.

## 4. Metrics
Per-phase metrics from the other workload references; interference measures.

## 5. Common bottlenecks and anti-patterns
Optimizing the wrong phase; global settings that help one phase and hurt another.

## 6. Candidate optimization techniques
Classify by phase; keep per-class tunables; budget background work against foreground latency.

## 7. Runtime tunables versus build-time changes
Runtime: per-class parameters. Build-time: phase separation.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Per-phase selection is RACE; shared-code fixes are universal.

## 9. Compatibility and version considerations
State machines for phases must stay consistent with app lifecycle.

## 10. Security, privacy, accessibility, data integrity
Same as constituent workloads.

## 11. Validation and benchmark methodology
Benchmark each phase and the mixture; test interference.

## 12. Rollback considerations
Roll back per class independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
