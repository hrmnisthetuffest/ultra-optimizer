<!-- format: 13-section -->
# Reliability and resilience

## 1. Purpose and applicability
Keep the service correct and available under failure while optimizing.

## 2. Detection signals
Cascading failures, retry storms, no timeouts, single points of failure, slow recovery.

## 3. What to inspect
Timeouts, retries, circuit breakers, bulkheads, health checks, graceful degradation, shutdown handling, dependency failure behavior.

## 4. Metrics
Availability, error budget burn, MTTR, retry rate, breaker state changes.

## 5. Common bottlenecks and anti-patterns
Unbounded retries, missing timeouts, shared pools without isolation, optimizations that remove safety checks.

## 6. Candidate optimization techniques
Timeouts everywhere, retries with backoff and jitter on idempotent calls only, breakers, bulkheads, graceful degradation, load shedding.

## 7. Runtime tunables versus build-time changes
Runtime: timeout, retry and breaker parameters.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: parameters within developer-approved bounds. /optimize lens: correct failure handling. /ping-optimize lens: connection failure and reconnect behavior.

## 9. Compatibility and version considerations
Library defaults differ widely.

## 10. Security, privacy and accessibility considerations
Fail closed on authentication and authorization errors. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Fault-injection tests: dependency down, slow, erroring; verify no retry storm and no duplicate side effects.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
