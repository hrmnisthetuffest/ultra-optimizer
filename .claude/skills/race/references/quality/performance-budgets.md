<!-- format: 13-section -->
# Performance budgets

## 1. Purpose and applicability
Set measurable limits so optimizations are judged against targets with context.

## 2. Detection signals
Existing SLOs, CI performance gates, product goals.

## 3. What to inspect
Startup/time-to-interactive, p95 latency, frame time, memory/VRAM, package size, CPU time, request count, error rate.

## 4. Metrics
Each budget with workload and environment context and confidence label.

## 5. Common bottlenecks and anti-patterns
Budgets without workload definition; comparing different machines; single-run claims.

## 6. Candidate optimization techniques
Define budget per metric with workload and environment; measure repeatedly; report ranges; flag regressions beyond noise.

## 7. Runtime tunables versus build-time changes
Budget values are configuration, not secrets.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE budgets may depend on hardware class; /optimize budgets assume declared targets only.

## 9. Compatibility and version considerations
Budgets are per platform class.

## 10. Security, privacy, accessibility, data integrity
No per-user data in budget records.

## 11. Validation and benchmark methodology
Use robust statistics and confidence intervals; control for background load.

## 12. Rollback considerations
A budget miss triggers rollback or a documented exception.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
