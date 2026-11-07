<!-- format: 13-section -->
# Network-bound workloads

## 1. Purpose and applicability
Work limited by latency, bandwidth or request count (APIs, sync, streaming, web pages).

## 2. Detection signals
Waterfall of requests; waiting on responses; large payloads; retry storms.

## 3. What to inspect
Request count, payload sizes, caching headers, connection reuse, compression, serialization, retry/backoff policy.

## 4. Metrics
Request count, bytes transferred, p95 latency, time-to-first-byte, error and retry rates.

## 5. Common bottlenecks and anti-patterns
Sequential requests that could batch; missing caching; chatty protocols; unbounded retries.

## 6. Candidate optimization techniques
Batch, cache, compress, reuse connections, prefetch within bounds, reduce payloads; adapt concurrency to measured conditions (RACE, app-level only).

## 7. Runtime tunables versus build-time changes
Runtime: concurrency, timeouts, prefetch depth. Build-time: protocol/payload changes (API compatibility!).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Measured-condition adaptation is RACE; request reduction and caching are universal.

## 9. Compatibility and version considerations
Keep API contracts and wire formats compatible; server and client versions skew.

## 10. Security, privacy, accessibility, data integrity
No new telemetry; no sending data to new endpoints; keep TLS and auth behavior unchanged.

## 11. Validation and benchmark methodology
Use mock/replay servers and controlled latency; check error paths and offline behavior.

## 12. Rollback considerations
Revert concurrency/caching changes; keep old request path behind a flag.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
