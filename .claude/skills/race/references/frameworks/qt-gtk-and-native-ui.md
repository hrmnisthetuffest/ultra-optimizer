<!-- format: 13-section -->
# Qt, GTK and native desktop UI

## 1. Purpose and applicability
Retained-mode native UI toolkits.

## 2. Detection signals
Detect via: CMake find_package(Qt), meson.build gtk

## 3. What to inspect
Inspect: event loop blocking, model/view updates, painting, threading

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
UI thread blocking; excessive repaint; synchronous model loads.

## 6. Candidate optimization techniques
worker threads with queued signals, incremental model updates, caching painted assets.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: bypassing toolkit a11y, changing system themes or settings.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
toolkit profilers, scripted UI tests.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
