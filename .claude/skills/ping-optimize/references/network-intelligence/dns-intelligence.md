<!-- format: 13-section -->
# DNS resolution behavior

## 1. Purpose and applicability
DNS lookup precedes the first connection to a host. The application can reduce lookups and avoid blocking on them; it cannot change the user's resolver.

## 2. Detection signals
First request to each host is slow; many distinct hostnames per page or session; failures when DNS is flaky.

## 3. What to inspect
Number of distinct hostnames; resolver calls on hot paths; whether the library caches results and honors TTL; use of connection coalescing; DNS failure handling.

## 4. Metrics
DNS time p50/p95, lookups per session, DNS failure rate, cache hit rate of the app or library resolver.

## 5. Common bottlenecks and anti-patterns
Many hostnames (domain sharding in an HTTP/2 world); lookups on the UI thread; re-resolving per request; no timeout or fallback on failure.

## 6. Candidate optimization techniques
Consolidate hostnames; reuse connections; pre-resolve or preconnect only to hosts that will certainly be used soon (see prefetching); set bounded timeouts with fallback behavior.

## 7. Runtime tunables versus build-time changes
Runtime: resolver timeout, prefetch list. Build-time: hostnames in API design.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Pre-resolving is a measured, bounded decision. Never change the user's DNS settings or resolver.

## 9. Compatibility and version considerations
DNS-over-HTTPS and OS resolver behavior differ; respect platform-provided resolution.

## 10. Security, privacy and accessibility considerations
Hostnames can reveal browsing; do not log them beyond necessity. Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Simulate slow and failing DNS; assert bounded wait and graceful fallback.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
