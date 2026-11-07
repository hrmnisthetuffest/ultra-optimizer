<!-- format: 13-section -->
# Request optimization: batching, dedup, coalescing, priority

## 1. Purpose and applicability
Reduce the number, size and waiting of requests without changing what the user gets.

## 2. Detection signals
Waterfalls of dependent calls; identical requests in flight together; N+1 patterns; chatty startup; requests for data already held.

## 3. What to inspect
Call graph from user action to requests; duplicate URL/parameter sets; dependency between calls; batch-capable endpoints; cancellation on navigation or input change.

## 4. Metrics
Requests per user operation, duplicate request ratio, sequential depth, bytes, operation latency.

## 5. Common bottlenecks and anti-patterns
Sequential awaits of independent calls; no cancellation of superseded requests; per-item calls in loops; refetch on every render.

## 6. Candidate optimization techniques
Batch where the API supports it; coalesce identical in-flight requests (single-flight); parallelize only independent calls; cancel superseded work; fetch only needed fields; prioritize critical-path requests.

## 7. Runtime tunables versus build-time changes
Runtime: batch window, max batch size, priority classes. Build-time: API shape.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal (also /optimize): dedup, single-flight, batching. Adaptive: batch window by measured RTT, bounded.

## 9. Compatibility and version considerations
Batching changes error semantics: partial failure handling must be explicit. Parallelism must respect ordering and consistency requirements.

## 10. Security, privacy and accessibility considerations
Dedup keys must include identity and authorization context so one user never receives another's response. Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Tests: duplicate calls collapse; error in one batched item does not corrupt others; cancellation leaves no orphan state; ordering-sensitive flows unchanged.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
