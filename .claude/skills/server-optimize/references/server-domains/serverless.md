<!-- format: 13-section -->
# Serverless workloads

## 1. Purpose and applicability
Reduce cold starts, per-invocation overhead and cost on function platforms.

## 2. Detection signals
Cold-start latency, timeouts, high per-invocation cost, connection exhaustion on databases.

## 3. What to inspect
Package size, initialization work, handler/global separation, memory setting, connection handling, concurrency limits, provisioned concurrency.

## 4. Metrics
Cold-start duration, warm duration, billed duration, error and throttle rate, cost per request.

## 5. Common bottlenecks and anti-patterns
Heavy init per invocation, large bundles, new DB connection per invocation, long synchronous chains.

## 6. Candidate optimization techniques
Initialize clients outside the handler, shrink bundles, lazy-load rarely used code, use pooled or proxy connections, right-size memory by measurement.

## 7. Runtime tunables versus build-time changes
Runtime: memory, timeout, concurrency. Build-time: bundle contents.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: memory/CPU allocation is provider-defined and must be verified from the platform, not assumed. /optimize lens: reduce init and package cost. /ping-optimize lens: edge versus regional placement; measure real RTT, not assumed.

## 9. Compatibility and version considerations
Limits, runtimes and pricing change often; consult current provider documentation.

## 10. Security, privacy and accessibility considerations
Do not widen IAM roles or function URLs for speed. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Measure cold and warm separately over many invocations; cost per request before/after.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
