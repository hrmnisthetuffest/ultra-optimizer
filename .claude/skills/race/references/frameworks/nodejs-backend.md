<!-- format: 13-section -->
# Node.js services

## 1. Purpose and applicability
Event-loop servers.

## 2. Detection signals
Detect via: package.json, server entry files

## 3. What to inspect
Inspect: blocking calls, DB access, streams, cluster/worker usage, keep-alive

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
event-loop blocking; N+1 queries; unbounded concurrency.

## 6. Candidate optimization techniques
stream, pool connections with bounds, cache with TTLs, worker threads for CPU work, concurrency from capability (RACE).

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: skipping validation or auth middleware, removing rate limits.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
autocannon-style load tests, --cpu-prof, event-loop delay metrics.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
