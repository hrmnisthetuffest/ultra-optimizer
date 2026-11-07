<!-- format: 13-section -->
# JavaScript and TypeScript

## 1. Purpose and applicability
Language/runtime-specific optimization guidance. Detect the real stack from manifests and lockfiles first.

## 2. Detection signals
Manifests/lockfiles: p

## 3. What to inspect
Runtime and memory model: single-threaded event loop; GC; workers for parallelism; V8-like JIT.

## 4. Metrics
Use the profilers listed in section 11; track wall time, CPU time, allocations and tail latency.

## 5. Common bottlenecks and anti-patterns
Common traps: sync work on main thread; large JSON parse; closures in hot loops; memory leaks via listeners; excess re-renders.

## 6. Candidate optimization techniques
Idiomatic optimizations: batch DOM/IPC work, use workers, streaming, typed arrays for numeric data, memoize with bounds, lazy import().

## 7. Runtime tunables versus build-time changes
Build/compiler levers: bundler target, tree-shaking, code splitting, minification; verify source maps and compatibility targets.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven pool, cache and path choices via registered tunables. /optimize: algorithm, data structure and build fixes. Interop: native addons/WASM: validate fallbacks.

## 9. Compatibility and version considerations
Pin and respect the project's language/runtime versions; check release notes before relying on version-specific behavior.

## 10. Security, privacy, accessibility, data integrity
Keep security checks, input validation and accessibility intact; do not disable safety features (bounds checks, sanitizers in test) for speed without approval.

## 11. Validation and benchmark methodology
Profiling tools: browser DevTools performance panel, Node --cpu-prof, clinic/0x. Tests: existing unit tests, e2e flows, bundle-size checks.

## 12. Rollback considerations
Keep the change behind a flag or in a separate commit so it reverts cleanly.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
