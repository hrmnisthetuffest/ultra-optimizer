<!-- format: 13-section -->
# Latency analysis and attribution

## 1. Purpose and applicability
Attribute user-perceived delay to its cause before changing anything. Latency has nine places to hide: (1) application logic, (2) local networking implementation (queues, thread pools, serialization), (3) DNS, (4) connection establishment (TCP, TLS, QUIC), (5) transport behavior (slow start, loss recovery, head-of-line blocking), (6) network path, (7) remote server processing, (8) data transfer, (9) client processing after the response arrives.

## 2. Detection signals
Operations feel slow although bandwidth is fine; first request much slower than later ones; delay scales with the number of sequential requests (round-trip bound).

## 3. What to inspect
Request waterfall; per-phase timing (DNS, connect, TLS, send, wait, receive); dependency chains; time between response arrival and UI update; server timing headers if provided.

## 4. Metrics
Per-phase durations (p50/p95/p99), number of sequential round trips per user operation, TTFB, time to last byte, total operation latency, client post-processing time.

## 5. Common bottlenecks and anti-patterns
Serial request chains, per-request handshakes, work done on the main thread after the response, polling, oversized responses, cold connections after idle.

## 6. Candidate optimization techniques
Remove avoidable round trips (batch, combine, parallelize independent calls), reuse connections, reduce payload, move post-processing off the critical path; see latency-reduction.

## 7. Runtime tunables versus build-time changes
Runtime: concurrency, timeouts, idle timeout. Build-time: API shape changes (compatibility!).

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Nothing in the attribution method is hardware-specific. Using one user's measured RTT to tune defaults is a RACE-style adaptive decision requiring authorization.

## 9. Compatibility and version considerations
Timing APIs differ (Resource Timing needs Timing-Allow-Origin for cross-origin detail). Document what each platform can and cannot observe.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Produce an attribution table per operation (bucket, measured ms, evidence). Re-measure after each change; require repeated runs. Never attribute to a bucket without a measurement or mark it hypothesis.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07). Other timing API docs not fetched; unverified.
Last reviewed: 2026-11-07.
