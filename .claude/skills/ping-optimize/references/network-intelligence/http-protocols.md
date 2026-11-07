<!-- format: 13-section -->
# HTTP protocol versions: choosing and detecting

## 1. Purpose and applicability
HTTP/1.1, HTTP/2 and HTTP/3 offer different tradeoffs. Detect what the client, server and path actually negotiate; never assume newer is faster for a given workload.

## 2. Detection signals
Library defaults decide protocol silently; mixed environments; proxies that downgrade.

## 3. What to inspect
Negotiated protocol per host (ALPN, response version); proxy and CDN in path; server support; connection counts per origin.

## 4. Metrics
Protocol share of requests, time per phase by protocol, failure and fallback rate.

## 5. Common bottlenecks and anti-patterns
Assuming H2 or H3 is active when a proxy forces HTTP/1.1; domain sharding left over from HTTP/1.1; large single-connection H2 flows suffering TCP loss.

## 6. Candidate optimization techniques
Enable multiplexed protocols through the library's supported switch where the server supports them; remove HTTP/1.1-era workarounds only when H2/H3 is verified; keep fallback.

## 7. Runtime tunables versus build-time changes
Runtime: protocol preference flags if library offers. Build-time: library versions.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Choose from measurement per deployment. Universal: removing workarounds that are harmful on any multiplexed protocol.

## 9. Compatibility and version considerations
Server and client library version skew; fallback must work.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Compare protocols under network_sim profiles (loss, latency); report percentile results, not a single run.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
RFC 9113 HTTP/2, https://www.rfc-editor.org/rfc/rfc9113.html (fetched 2026-11-07, first 100000 chars read); RFC 9114 HTTP/3, https://www.rfc-editor.org/rfc/rfc9114.html (fetched 2026-11-07, first 100000 chars read).
Last reviewed: 2026-11-07.
