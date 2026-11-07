<!-- format: 13-section -->
# Scalability

## 1. Purpose and applicability
Identify limits to scaling and remove software bottlenecks before adding hardware.

## 2. Detection signals
Throughput plateaus, per-instance saturation, shared-resource contention, scaling that does not help.

## 3. What to inspect
Single points of contention (locks, DB rows, singletons), statelessness, partitioning, queue-based decoupling, capacity model.

## 4. Metrics
Throughput versus instances, saturation curves, contention metrics, cost per request.

## 5. Common bottlenecks and anti-patterns
Scaling out a contended resource, global counters, sticky state, thundering herds.

## 6. Candidate optimization techniques
Remove contention, shard or partition hot data, decouple with queues, cache, apply load shedding and backpressure.

## 7. Runtime tunables versus build-time changes
Runtime: replica counts and limits (infrastructure; recommend only unless authorized).

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: worker counts within approved bounds. /optimize lens: remove software bottlenecks. /ping-optimize lens: reduce cross-region chatter.

## 9. Compatibility and version considerations
Autoscaling features vary by platform.

## 10. Security, privacy and accessibility considerations
Do not scale infrastructure without explicit authorization; scaling has cost implications. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Load test at 1x, 2x, 4x instances; verify near-linear scaling or document the limit.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
