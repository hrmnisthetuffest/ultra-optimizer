<!-- format: 13-section -->
# Server workload profiling

## 1. Purpose and applicability
Describe how to establish a baseline and profile representative workloads safely before changing anything.

## 2. Detection signals
Any optimization claim, capacity question or latency complaint.

## 3. What to inspect
Existing metrics, logs and traces first (passive). Then bounded, authorized load against local or staging targets. Collect request latency percentiles, server processing time, throughput, CPU, memory, database query performance, cache effectiveness, queue latency, error rate, availability, cold-start duration and, where measurable, cost.

## 4. Metrics
p50, p95, p99 latency; requests per second; CPU and memory under load; query time and count; hit rate; queue age; error rate; availability; cold-start time; cost per request when billing data is provided.

## 5. Common bottlenecks and anti-patterns
One-shot measurements, unrepresentative data, load from a noisy laptop, load against production without authorization, comparing runs on different hardware, mixing warm and cold results.

## 6. Candidate optimization techniques
Run several repetitions after a warm-up, report percentiles and spread, keep data volume and request mix representative, separate warm and cold, record environment details, make the load tool bounded and cancellable, and save a baseline file next to the results.

## 7. Runtime tunables versus build-time changes
Runtime: load duration, concurrency, request mix.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: benchmark candidate configurations on the verified target class. /optimize lens: use deterministic, host-independent comparisons (operation counts, query counts) where possible. /ping-optimize lens: separate network time from server processing time using Server-Timing or equivalent.

## 9. Compatibility and version considerations
Tools and metrics differ per stack; choose what the project already uses.

## 10. Security, privacy and accessibility considerations
No traffic floods or scans; only owned or explicitly authorized targets; bounded rate and duration; never include real user data in test payloads. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Variation between repeated baselines must be small enough to detect the claimed improvement; otherwise report inconclusive.

## 12. Rollback and failure handling
Stop load immediately on error-rate or latency guard breaches; load tools must be cancellable. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
