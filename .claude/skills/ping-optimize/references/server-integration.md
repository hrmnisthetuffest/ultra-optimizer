<!-- format: 13-section -->
# Server intelligence integration (ping-optimize)

## 1. Purpose and applicability
Use server intelligence to separate network time from server processing time and to reduce avoidable round trips to backends. The shared Server & Backend Intelligence library ships with the skill named server-optimize. If that skill is installed, read its references/INDEX.md and load only the domain files relevant to the backend component found. If it is not installed, continue with this skill's own references and tell the developer that the shared library is unavailable; never invent server facts.

## 2. Detection signals
HTTP clients, API calls, WebSocket or gRPC clients, Server-Timing headers, retry logic, connection pools.

## 3. What to inspect
Endpoint response time versus RTT, server processing time where observable (Server-Timing, application logs), connection reuse to the backend, payload sizes, retry behavior, rate-limit handling, region of the endpoint only if verified.

## 4. Metrics
RTT percentiles, TTFB, server processing time, total operation time, connection reuse rate, failure and retry rate.

## 5. Common bottlenecks and anti-patterns
Calling slow server processing a network problem, claiming ping improved without endpoint-specific measurements, assuming server region.

## 6. Candidate optimization techniques
Attribute latency to client, network or server; batch and coalesce calls; reuse connections; recommend server-side fixes to /optimize or /server-optimize when processing dominates.

## 7. Runtime tunables versus build-time changes
Application networking configuration only.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/ping-optimize lens: this file. /race lens: hardware selection out of scope here. /optimize lens: universal code fixes out of scope here.

## 9. Compatibility and version considerations
Server-Timing and similar signals exist only if the backend emits them.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Measure repeatedly against owned or authorized endpoints with bounded traffic; compare before and after.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
