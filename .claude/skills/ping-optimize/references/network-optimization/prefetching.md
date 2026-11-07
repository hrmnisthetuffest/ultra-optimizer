<!-- format: 13-section -->
# Prefetching and preconnect

## 1. Purpose and applicability
Fetching early can hide latency but wastes data and can slow critical work. Prefetch only when the need is probable and the cost bounded.

## 2. Detection signals
Predictable next navigation or content; idle gaps; cold first requests.

## 3. What to inspect
Existing prefetch/preload/preconnect usage; hit rate; data plan sensitivity; priority of prefetch versus user requests.

## 4. Metrics
Prefetch hit rate, wasted bytes, effect on interactive latency.

## 5. Common bottlenecks and anti-patterns
Prefetch on metered or slow links; prefetch competing with critical requests; prefetching private data to shared caches.

## 6. Candidate optimization techniques
Preconnect to certain origins; prefetch low priority and cancellable; limit depth; skip when conditions are poor or user opted for data saving.

## 7. Runtime tunables versus build-time changes
Runtime: depth, enable threshold, priority. Respect user data-saver preference.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Whether to prefetch is conditional on measured network state (adaptive, bounded).

## 9. Compatibility and version considerations
Browser hint support varies; use standard mechanisms.

## 10. Security, privacy and accessibility considerations
Never prefetch state-changing or private endpoints with side effects; GET only. Honor data-saver. Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Measure hit rate and wasted bytes; verify no side effects.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
