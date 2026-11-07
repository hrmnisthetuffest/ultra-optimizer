<!-- format: 13-section -->
# API performance

## 1. Purpose and applicability
Make endpoints fast and cheap: right-sized payloads, fewer round trips, safe caching and pagination.

## 2. Detection signals
Slow list endpoints, N+1 data access, large payloads, chatty clients, repeated identical requests.

## 3. What to inspect
Endpoint latency distribution, queries per request, response size, pagination, field selection, ETag/conditional support, rate-limit handling, idempotency of unsafe methods.

## 4. Metrics
p50/p95/p99 latency per endpoint, queries per request, payload bytes, cache hit rate, error rate.

## 5. Common bottlenecks and anti-patterns
N+1 queries, unbounded lists, returning unused fields, no conditional requests, retries on non-idempotent POST without keys.

## 6. Candidate optimization techniques
Eager loading or batching, pagination with stable cursors, field selection, conditional requests, response caching with correct keys, streaming large results, idempotency keys.

## 7. Runtime tunables versus build-time changes
Runtime: page sizes, cache TTLs, rate limits. Build-time: schema and query design.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: tune pool and batch sizes to verified capacity. /optimize lens: fix N+1, payload and algorithm issues. /ping-optimize lens: reduce round trips and bytes; separate server time from RTT.

## 9. Compatibility and version considerations
Changing response shape or defaults breaks clients; version or keep fields compatible.

## 10. Security, privacy and accessibility considerations
Preserve authorization on every path including cached and batched ones; never cache per-user responses under shared keys. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Contract tests, authorization tests, query-count assertions, load test against a representative dataset.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
