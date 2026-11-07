<!-- format: 13-section -->
# Flutter and React Native

## 1. Purpose and applicability
Cross-platform mobile UIs.

## 2. Detection signals
Detect via: pubspec.yaml, package.json with react-native

## 3. What to inspect
Inspect: widget/component rebuilds, list virtualization, bridge or channel traffic, image sizes, startup

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
rebuild storms; chatty bridge calls; unbounded images.

## 6. Candidate optimization techniques
const/memo widgets, virtualization, batch native calls, image resizing, deferred init.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: removing platform a11y semantics, dropping platform support.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
framework profilers (DevTools, Flipper-style tools), device tests.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
