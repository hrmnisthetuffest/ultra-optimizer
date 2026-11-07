<!-- format: 13-section -->
# Latency-sensitive workloads

## 1. Purpose and applicability
Work judged by response time (UI interactions, typing, input handling, request tails).

## 2. Detection signals
Complaints or metrics about p95/p99 or input delay; long tasks on the main/UI thread.

## 3. What to inspect
Main-thread work, long tasks, synchronous calls, GC pauses, lock hold times, startup/time-to-interactive.

## 4. Metrics
p50/p95/p99 latency, input-to-response time, long-task counts, jank frames.

## 5. Common bottlenecks and anti-patterns
Blocking calls on UI thread; large synchronous initialization; unbounded queues; GC pauses.

## 6. Candidate optimization techniques
Move work off the critical path, chunk long tasks, prioritize interactive work, defer non-essential init, bounded queues.

## 7. Runtime tunables versus build-time changes
Runtime: chunk size, priority tiers, deferral thresholds. Build-time: structure of init.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Thresholds from measured devices are RACE; removing blocking work is universal.

## 9. Compatibility and version considerations
Platform scheduling differs; keep accessibility timing expectations.

## 10. Security, privacy, accessibility, data integrity
Do not skip validation or security checks to save time.

## 11. Validation and benchmark methodology
Measure tail latency under realistic load; compare distributions, not means.

## 12. Rollback considerations
Revert scheduling parameters; keep behavior flags.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
