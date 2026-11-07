<!-- format: 13-section -->
# React and Next.js

## 1. Purpose and applicability
Component rendering, hydration and server/client boundaries.

## 2. Detection signals
Detect via: package.json deps react/next, next.config.*

## 3. What to inspect
Inspect: component tree, state placement, memoization, data fetching, server components, bundle splits

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
needless re-renders; large client bundles; waterfalls; hydration cost.

## 6. Candidate optimization techniques
memoize where profiled, split state, virtualize lists, move work to server, stream, lazy-load routes.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: removing a11y attributes, disabling strict mode checks to hide issues, hiding consent UI.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
React Profiler, Lighthouse, bundle analyzer; compare lab vs field.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
