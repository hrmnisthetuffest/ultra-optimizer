<!-- format: 13-section -->
# HTTP/3 and QUIC

## 1. Purpose and applicability
HTTP/3 maps HTTP onto QUIC, which runs over UDP with per-stream loss recovery and integrated TLS 1.3.

## 2. Detection signals
Server advertises Alt-Svc h3; UDP blocked on some networks; handshake-bound workloads; lossy mobile links.

## 3. What to inspect
Whether the client library supports HTTP/3; Alt-Svc handling; fallback to TCP when UDP fails; connection migration support; server and CDN support.

## 4. Metrics
Protocol share, handshake time versus H2, fallback rate, loss-recovery stalls.

## 5. Common bottlenecks and anti-patterns
Assuming H3 is faster everywhere; no fallback path; UDP rate limiting by networks; CPU cost on constrained clients.

## 6. Candidate optimization techniques
Allow H3 where library and server support it and measure per workload; keep automatic fallback to TCP-based HTTP.

## 7. Runtime tunables versus build-time changes
Runtime: protocol preference flag. Build-time: library with QUIC support.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Whether H3 helps is a measurement per deployment. Do not hardcode a preference.

## 9. Compatibility and version considerations
Per RFC 9114, clients should fall back to TCP-based HTTP if UDP is blocked; discovery via Alt-Svc with the h3 token.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Block UDP in the simulated environment and assert fallback; compare latency under loss.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
RFC 9114 HTTP/3, https://www.rfc-editor.org/rfc/rfc9114.html (fetched 2026-11-07, first 100000 chars read): each request on its own QUIC stream, QPACK header compression, Alt-Svc discovery. QUIC transport (RFC 9000) not fetched; unverified.
Last reviewed: 2026-11-07.
