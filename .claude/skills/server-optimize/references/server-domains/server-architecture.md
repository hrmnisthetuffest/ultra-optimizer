<!-- format: 13-section -->
# Server architecture

## 1. Purpose and applicability
Understand how the backend is decomposed (monolith, services, serverless, workers) so optimization targets the real critical path. Applies to any server-side project.

## 2. Detection signals
Multiple entry points, service-to-service calls, worker/queue processes, API gateway or reverse proxy config, serverless handlers, shared databases.

## 3. What to inspect
Entry points and process model; synchronous call chains per user-facing operation; shared state; where state lives (memory, DB, cache, disk); statelessness of request handlers; fan-out and fan-in points.

## 4. Metrics
End-to-end latency per operation, calls per request (fan-out), per-hop latency, error propagation rate, saturation per component.

## 5. Common bottlenecks and anti-patterns
Chatty service-to-service calls, hidden synchronous dependencies, global singletons with locks, in-process state that blocks horizontal scaling, shared database as integration bus.

## 6. Candidate optimization techniques
Remove unnecessary hops, batch or parallelize independent calls, make handlers stateless, move slow work off the request path, add timeouts and bulkheads between components.

## 7. Runtime tunables versus build-time changes
Runtime: timeouts, concurrency limits, pool sizes. Build-time: module boundaries, deployment topology.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size worker/process counts from verified CPU and memory of the target. /optimize lens: remove redundant hops, fix algorithmic and structural inefficiency regardless of host. /ping-optimize lens: measure per-hop latency and separate network time from handler time.

## 9. Compatibility and version considerations
Splitting or merging services changes deployment, versioning and failure modes; keep API contracts and data ownership intact.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Trace one operation across all hops before and after; run contract tests; compare p50/p95/p99 under a representative load.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
