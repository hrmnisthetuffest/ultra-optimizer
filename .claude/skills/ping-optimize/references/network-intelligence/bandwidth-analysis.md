<!-- format: 13-section -->
# Bandwidth and throughput analysis

## 1. Purpose and applicability
Separate 'the link is slow' from 'the app uses the link badly'. Throughput is bits delivered per second; it says little about latency.

## 2. Detection signals
Large transfers slow while small requests are fine; throughput plateaus below link capacity; many small parallel flows each slow.

## 3. What to inspect
Payload sizes and compression; number of parallel flows; windowing and buffer sizes in app code; whether a single connection or many is used; server-side rate limits; upload versus download asymmetry.

## 4. Metrics
Goodput (useful bytes/s) down and up, bytes per operation, transfer duration, share of time idle between chunks, compression ratio.

## 5. Common bottlenecks and anti-patterns
Tiny buffers, serial chunk requests, no compression, redundant bytes, retransmitted whole files instead of ranges, uploads blocked behind downloads.

## 6. Candidate optimization techniques
Compress compressible payloads, send deltas, use range or chunked transfers, size buffers to the bandwidth-delay product, add bounded parallelism only when measurement shows a single flow cannot fill the link.

## 7. Runtime tunables versus build-time changes
Runtime: chunk size, concurrency cap, buffer size. Build-time: wire format and compression support.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Choosing concurrency or chunk size from measured throughput is adaptive (RACE-style, app-level). Removing needless bytes is universal.

## 9. Compatibility and version considerations
Server must support ranges and compression the client asks for; keep wire compatibility with older clients.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Benchmark with a controlled bandwidth cap (network_sim) and report goodput percentiles across repeated runs; verify integrity (hash) of transferred data.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
