<!-- format: 13-section -->
# Client-server and offline-first/local-first apps

## 1. Purpose and applicability
Clients with local state and sync.

## 2. Detection signals
Detect from repo layout, deployment files, service boundaries and messaging dependencies.

## 3. What to inspect
Inspect: sync protocol, conflict resolution, local DB, startup load

## 4. Metrics
End-to-end latency, throughput, queue depth, error rate, resource use per component.

## 5. Common bottlenecks and anti-patterns
full re-syncs; large initial loads; blocking local DB access.

## 6. Candidate optimization techniques
delta sync, bounded local caches, background sync when idle (RACE), lazy hydration.

## 7. Runtime tunables versus build-time changes
Runtime: sync batch size, cache caps, schedule.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: adaptive concurrency and budgets inside the app. /optimize: protocol, query and structure fixes. No-go: dropping offline support or changing conflict semantics.

## 9. Compatibility and version considerations
Keep wire formats and API versions compatible across deployed versions.

## 10. Security, privacy, accessibility, data integrity
Do not weaken auth, tenant isolation or data protection for speed.

## 11. Validation and benchmark methodology
Offline/online transition tests; data round-trip tests.

## 12. Rollback considerations
Feature-flag architectural changes; revert flags first.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
