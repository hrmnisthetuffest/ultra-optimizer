<!-- format: 13-section -->
# APIs and SaaS clients

## 1. Purpose and applicability
Fewer, cheaper, safer API calls.

## 2. Detection signals
Chatty clients, rate-limit errors, slow dashboards, retry storms.

## 3. What to inspect
Call patterns, pagination, batching endpoints, serialization, auth refresh flow, rate-limit handling, caching, streaming endpoints.

## 4. Metrics
Calls per screen, payload size, 429 rate, p95 latency, retry count.

## 5. Common bottlenecks and anti-patterns
N+1 calls, unpaginated lists, refetching unchanged data, auth refresh stampede, ignoring Retry-After.

## 6. Candidate optimization techniques
Batch and field-select, conditional requests, single-flight, cursor pagination, streaming for large results, single-flight token refresh, respect Retry-After, circuit breaking.

## 7. Runtime tunables versus build-time changes
Runtime: page size, concurrency, timeouts. Build-time: API version.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal mostly; concurrency bounds may adapt to measured conditions.

## 9. Compatibility and version considerations
Respect API versioning, quotas, terms of service.

## 10. Security, privacy and accessibility considerations
Never log tokens; keys per user; caching respects authorization.

## 11. Validation and testing
Mock server tests for 429/5xx/partial responses; assert idempotent retries only.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
