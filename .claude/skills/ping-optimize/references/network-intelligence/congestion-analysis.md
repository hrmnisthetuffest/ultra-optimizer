<!-- format: 13-section -->
# Congestion analysis

## 1. Purpose and applicability
Congestion shows up as growing queueing delay and loss under load. The application must avoid causing or worsening it.

## 2. Detection signals
Latency rises sharply during uploads or downloads (bufferbloat symptom), many flows competing, retry bursts after an outage.

## 3. What to inspect
Number of simultaneous flows; background transfers sharing the link with interactive traffic; retry synchronization across clients; whether the app paces bulk traffic.

## 4. Metrics
Loaded versus idle RTT delta, throughput fairness among own flows, retry burst size, queue depth where visible.

## 5. Common bottlenecks and anti-patterns
Unbounded parallel uploads; synchronized retries (thundering herd); prefetch that competes with interactive requests.

## 6. Candidate optimization techniques
Prioritize interactive traffic; cap and pace background transfers; add jitter to retries; back off on rising latency signals.

## 7. Runtime tunables versus build-time changes
Runtime: bulk-transfer concurrency and rate cap, backoff parameters.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Reducing own traffic under measured congestion is adaptive; keeping bulk transfers from starving interactive ones is universal.

## 9. Compatibility and version considerations
Server-side signals (429, 503 with Retry-After) must be honored.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Measure interactive latency while a bulk transfer runs, before and after.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack. RFC 9110 HTTP Semantics, https://www.rfc-editor.org/rfc/rfc9110.html (fetched 2026-11-07
Last reviewed: 2026-11-07.
