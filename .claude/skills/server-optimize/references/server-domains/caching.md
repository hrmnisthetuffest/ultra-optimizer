<!-- format: 13-section -->
# Server-side caching

## 1. Purpose and applicability
Avoid repeated work by reusing results safely, with correct keys, freshness and invalidation.

## 2. Detection signals
Repeated identical queries or computations, expensive pure functions, hot keys, stampedes after expiry.

## 3. What to inspect
Cache layers (CDN, HTTP, application, database), key composition, TTLs, invalidation on write, per-user data, stampede protection, memory bounds.

## 4. Metrics
Hit rate, miss latency, eviction rate, stale-serve rate, memory use, origin load.

## 5. Common bottlenecks and anti-patterns
Caching per-user or authorized data under shared keys, no invalidation, unbounded caches, stampedes, caching errors.

## 6. Candidate optimization techniques
Include identity, locale and Vary dimensions in keys; use TTL plus explicit invalidation; request coalescing (single flight); bound size; negative-cache briefly; use stale-while-revalidate only where staleness is acceptable.

## 7. Runtime tunables versus build-time changes
Runtime: TTLs, sizes, eviction. Build-time: key design.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: allocate cache memory from the verified budget within approved bounds. /optimize lens: fix key design, invalidation and correctness. /ping-optimize lens: fewer origin round trips and conditional requests.

## 9. Compatibility and version considerations
Cache semantics must follow HTTP caching rules for shared caches; behavior varies by CDN.

## 10. Security, privacy and accessibility considerations
Never cache authenticated or personalized content in shared caches; flush on permission change. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Wrong-user leakage tests, invalidation-after-write tests, stampede test, hit-rate comparison.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
