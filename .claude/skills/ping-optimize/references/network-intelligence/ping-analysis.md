<!-- format: 13-section -->
# Ping and round-trip time analysis

## 1. Purpose and applicability
Explain what a 'ping' is and is not. ICMP echo RTT, TCP connect time, application-level request RTT and server response time are different quantities. The application can lower round-trip COUNT and connection setup COST; it cannot lower physical path delay.

## 2. Detection signals
Users quote a ping number; game or real-time features feel laggy; developers equate TTFB with RTT.

## 3. What to inspect
How the app measures 'ping' today (ICMP, app-level echo, request timing); whether the probe endpoint is the same one real traffic uses; whether probes share connections with real traffic.

## 4. Metrics
RTT p50/p95/p99 to the endpoint actually used, RTT under load versus idle, probe loss rate, sample count and interval.

## 5. Common bottlenecks and anti-patterns
Pinging a different host than the service; ICMP being deprioritized or blocked; reporting a mean; sampling too rarely; confusing server think time with RTT.

## 6. Candidate optimization techniques
Use an application-level echo on the real protocol and endpoint for measurement; report percentiles; for endpoint choice use measured RTT to candidate regions where the developer offers multiple; cut round trips per operation.

## 7. Runtime tunables versus build-time changes
Runtime: probe interval and count (bounded). Build-time: whether probe endpoint exists on the server.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Endpoint selection from measured RTT is adaptive and app-level. It may only choose among developer-provided endpoints.

## 9. Compatibility and version considerations
ICMP may be unavailable to unprivileged code on some platforms; do not require elevated privileges.

## 10. Security, privacy and accessibility considerations
Probes target only owned or authorized endpoints, bounded in rate and count, cancellable. Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Compare idle versus loaded RTT; run at least several samples across time; state the endpoint and protocol with every number.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
