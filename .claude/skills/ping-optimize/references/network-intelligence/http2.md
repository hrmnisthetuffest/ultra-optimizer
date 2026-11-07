<!-- format: 13-section -->
# HTTP/2

## 1. Purpose and applicability
HTTP/2 multiplexes many request/response streams over one TCP connection, with header compression and flow control.

## 2. Detection signals
Application opens many connections to one origin; sharding; priority hints unused.

## 3. What to inspect
Connections per origin; stream concurrency limits; flow-control window effects on large transfers; priority usage; server push remnants.

## 4. Metrics
Streams per connection, connection count, stall time, time to first byte per stream.

## 5. Common bottlenecks and anti-patterns
Residual HTTP/1.1 sharding and spriting; assuming priorities are honored; TCP head-of-line blocking under loss (not solved by HTTP/2); server push assumptions.

## 6. Candidate optimization techniques
One connection per origin, reuse; stop sharding; use the extensible priority scheme where the stack supports it; keep large downloads from starving interactive streams.

## 7. Runtime tunables versus build-time changes
Runtime: max concurrent streams used, priority hints. Build-time: bundling strategy.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal: remove sharding. Adaptive: stream concurrency by measured conditions with bounds.

## 9. Compatibility and version considerations
Per RFC 9113 the older prioritization scheme is deprecated; support varies by implementation.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Verify behavior under loss in network_sim; confirm no regression for HTTP/1.1 fallback.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
RFC 9113 HTTP/2, https://www.rfc-editor.org/rfc/rfc9113.html (fetched 2026-11-07, first 100000 chars read): multiplexing, hop-by-hop credit-based flow control (default 65,535 octets), prioritization deprecated in favor of RFC 9218 (RFC 9218 itself not fetched), TCP head-of-line blocking not addressed.
Last reviewed: 2026-11-07.
