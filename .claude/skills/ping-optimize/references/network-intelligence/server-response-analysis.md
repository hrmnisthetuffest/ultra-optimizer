<!-- format: 13-section -->
# Server response time versus network time

## 1. Purpose and applicability
Separate time spent waiting for the server from time spent in the network. Only the server owner can fix the former, and RTT cannot be inferred from it.

## 2. Detection signals
TTFB high but RTT low (server slow); TTFB tracks RTT (round-trip bound); response varies with payload.

## 3. What to inspect
Server-Timing headers if provided; TTFB minus connection setup; repeated identical requests for variance; cache status headers.

## 4. Metrics
TTFB, wait time, server-reported processing time, response size, variance across repeats.

## 5. Common bottlenecks and anti-patterns
Blaming the network for slow endpoints; N+1 API patterns; large uncompressed responses; missing server caching.

## 6. Candidate optimization techniques
If server time dominates, report it as a server finding, reduce calls, cache, request less data, or hand off to the backend owner. Do not hide server slowness with retries.

## 7. Runtime tunables versus build-time changes
Runtime: timeouts and hedging (only for idempotent reads, bounded). Build-time: API shape.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Not hardware-specific. Hedged requests are an app-level adaptive choice with bounded extra load.

## 9. Compatibility and version considerations
Changing API shapes needs versioning and client compatibility.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Compare slow-server profile versus slow-network profile in network_sim; confirm the attribution matches.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07) (TTFB composition). Server-Timing spec not fetched; unverified.
Last reviewed: 2026-11-07.
