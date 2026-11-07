<!-- format: 13-section -->
# Server networking

## 1. Purpose and applicability
Make the server's own network handling efficient: connections, protocols, buffers and timeouts. Network-path diagnosis itself belongs to the /ping-optimize lens.

## 2. Detection signals
Many short connections, handshake cost in traces, slow clients holding workers, large uncompressed responses, missing keep-alive.

## 3. What to inspect
Keep-alive and idle timeouts, protocol support (HTTP/1.1, HTTP/2, HTTP/3 where the platform provides it), TLS termination location, compression, response streaming, outbound connection reuse.

## 4. Metrics
Connections per second, reuse rate, handshake time, bytes per response, slow-client count, outbound pool hit rate.

## 5. Common bottlenecks and anti-patterns
Disabling keep-alive, per-request outbound clients, TLS re-termination at every hop, no timeouts, compressing already-compressed data.

## 6. Candidate optimization techniques
Reuse connections, tune app-level timeouts, enable compression where it pays, terminate TLS once, stream responses, use HTTP/2 or HTTP/3 only where the platform and clients support it.

## 7. Runtime tunables versus build-time changes
Runtime: keep-alive, timeouts, compression thresholds, pool sizes. Build-time: server framework choice.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size buffers and connection limits from verified memory and file-descriptor limits. /optimize lens: remove per-request client creation and redundant serialization. /ping-optimize lens: this is the primary lens: attribute delay to DNS, connect, TLS, server, transfer; see the ping-optimize skill when installed.

## 9. Compatibility and version considerations
Protocol availability depends on the platform edge; do not assume HTTP/3 is available.

## 10. Security, privacy and accessibility considerations
Never disable certificate verification or weaken TLS for speed; do not change host firewall or OS network settings. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Measure connection reuse, handshake counts and tail latency with slow-client and packet-loss simulation.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
