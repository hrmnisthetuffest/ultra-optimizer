<!-- format: 13-section -->
# TCP behavior as seen by the application

## 1. Purpose and applicability
TCP gives reliable ordered delivery at the cost of handshake latency and head-of-line blocking. The app influences it through connection reuse, buffer use and write patterns, not OS tuning.

## 2. Detection signals
Handshake cost on every request; stalls after loss; small writes causing many packets; idle connections silently dropped.

## 3. What to inspect
Socket options the app sets (documented ones only); keep-alive usage; write coalescing; idle timeouts versus middlebox timeouts; connection counts.

## 4. Metrics
Connect time, reuse rate, resets, time to first byte after idle, retransmission signals where visible.

## 5. Common bottlenecks and anti-patterns
One connection per request; Nagle/delayed-ACK interactions on request-response patterns; stale pooled connections reused after idle drop; too many connections.

## 6. Candidate optimization techniques
Reuse and pool; coalesce small writes; validate or retry-safely on stale connections; application keep-alive with sane intervals.

## 7. Runtime tunables versus build-time changes
Runtime: pool size, idle timeout, keep-alive interval, socket options exposed by the library.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Do not change OS TCP/IP settings. App-level socket options are allowed only if documented and justified by measurement.

## 9. Compatibility and version considerations
Socket option names and defaults vary by platform and runtime.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Test stale-connection recovery and idle timeout with network_sim interruption; assert no duplicate non-idempotent requests.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
