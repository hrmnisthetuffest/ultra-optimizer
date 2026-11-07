<!-- format: 13-section -->
# Opportunity catalog

## 1. Purpose and applicability
Prompts for finding broadly beneficial optimization candidates in any stack.

## 2. Detection signals
Look in code, build config, dependencies, queries, rendering logic, request patterns, startup code and tests.

## 3. What to inspect
Algorithms and data structures; repeated work and missing caching; allocation churn; N+1 queries and missing indexes; redundant network calls; oversized assets; synchronous work on interactive paths; dead code and unused dependencies; inefficient build configuration; error-handling that retries blindly.

## 4. Metrics
Time, allocations, bytes transferred, query counts, bundle size, startup time.

## 5. Common bottlenecks and anti-patterns
Premature micro-optimization; cache without invalidation; speed gains that remove checks.

## 6. Candidate optimization techniques
Replace quadratic loops, hoist invariants, batch calls, add bounded caches with correct invalidation, lazy-load, remove unused dependencies, tighten queries, compress transfers, defer non-critical work.

## 7. Runtime tunables versus build-time changes
Configuration changes limited to project-owned settings; no per-device parameters.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Only changes valid for every supported device.

## 9. Compatibility and version considerations
Preserve API contracts and file formats.

## 10. Security, privacy, accessibility, data integrity
Do not weaken validation, auth, encryption or accessibility.

## 11. Validation and benchmark methodology
Benchmark before/after on a fixed workload; verify outputs equal.

## 12. Rollback considerations
Keep each change independently revertible.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
