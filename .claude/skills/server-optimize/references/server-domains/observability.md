<!-- format: 13-section -->
# Observability

## 1. Purpose and applicability
Provide the measurements optimization needs, without adding hidden telemetry.

## 2. Detection signals
No metrics or traces, unknown hot paths, alerts without context.

## 3. What to inspect
Existing logs, metrics, traces, Server-Timing, health endpoints, sampling, cardinality, log volume.

## 4. Metrics
Coverage of the key signals, overhead of instrumentation, cardinality.

## 5. Common bottlenecks and anti-patterns
High-cardinality labels, logging bodies, always-on debug logs, unsampled tracing at high volume.

## 6. Candidate optimization techniques
Add low-overhead timing for the stages being optimized, sample traces, structured logs without sensitive data.

## 7. Runtime tunables versus build-time changes
Runtime: sampling rates, log levels.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: overhead budget set by developer. /optimize lens: consistent instrumentation. /ping-optimize lens: Server-Timing separates processing from network time.

## 9. Compatibility and version considerations
Telemetry libraries differ.

## 10. Security, privacy and accessibility considerations
New telemetry or monitoring requires explicit developer authorization and documented controls; no hidden agents. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Instrumentation overhead measured; no sensitive data in output.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
