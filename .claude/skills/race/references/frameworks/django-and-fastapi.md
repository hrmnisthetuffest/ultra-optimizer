<!-- format: 13-section -->
# Django and FastAPI

## 1. Purpose and applicability
Python web backends.

## 2. Detection signals
Detect via: manage.py, settings.py, FastAPI app modules

## 3. What to inspect
Inspect: ORM query counts, serializers, middleware, async/sync mix, worker count

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
N+1 queries; sync calls in async handlers; heavy serializers; missing indexes.

## 6. Candidate optimization techniques
select_related/prefetch, indexes (migration approval), caching, correct worker/process model, pagination.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: weakening auth/permissions, disabling CSRF, changing schemas without migration plan.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
query count assertions, load tests, profile endpoints.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
