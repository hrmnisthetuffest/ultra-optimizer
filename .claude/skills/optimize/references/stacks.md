<!-- format: 13-section -->
# Stack-specific hints

## 1. Purpose and applicability
Short pointers for common stacks; defer to project docs and official tooling.

## 2. Detection signals
Detect stack from manifests and lockfiles; support mixed stacks and monorepos.

## 3. What to inspect
JS/TS: bundle size, re-renders, event-loop blocking. Python: algorithmic loops, I/O, packaging. Rust/C/C++: allocation, build profiles, UB safety. Java/Kotlin/C#: allocations, async, query access. Go: allocations, goroutine leaks. SQL: indexes, query shapes. Web: critical rendering path, images, caching. Backends: pooling, caching, pagination.

## 4. Metrics
Stack-appropriate profilers and benchmarks.

## 5. Common bottlenecks and anti-patterns
Applying one stack's habits to another; enabling aggressive flags without measurement.

## 6. Candidate optimization techniques
Prefer the stack's idiomatic fix before exotic ones.

## 7. Runtime tunables versus build-time changes
Build flags (LTO, PGO, tree-shaking, minification, debug symbols) only as measured options for declared targets.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
No hardware-specific choices.

## 9. Compatibility and version considerations
Keep supported-version policy.

## 10. Security, privacy, accessibility, data integrity
Hardening flags and sanitizers stay.

## 11. Validation and benchmark methodology
Use each stack's standard test and benchmark tools.

## 12. Rollback considerations
Config changes live in version control.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
