<!-- format: 13-section -->
# Validation and rollback for server changes

## 1. Purpose and applicability
Define how every server-side change is validated under representative load and rolled back when validation fails and rollback is safe and authorized.

## 2. Detection signals
Any code, configuration or (when authorized) infrastructure change made by the workflow.

## 3. What to inspect
Baseline results, change diff, behavior and contract tests, security tests, data-integrity checks, supported deployment environments, rollback point.

## 4. Metrics
Request latency, server processing time, throughput, CPU, memory, database query performance, cache effectiveness, queue latency, error rate, availability, cold-start duration and cost where measurable; plus test pass rate.

## 5. Common bottlenecks and anti-patterns
Declaring success from one run, skipping contract or security tests, validating only on the developer's machine when other environments are supported, rolling back by changing things outside the authorized scope.

## 6. Candidate optimization techniques
Record baseline, make one focused change, run behavior, contract, security and integrity tests, rerun representative load, compare with spread, keep only changes that pass; otherwise restore the previous state. Label results as measured, estimated or unverified.

## 7. Runtime tunables versus build-time changes
Runtime: acceptance thresholds, guard limits.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: validate on each supported hardware class or mark untested. /optimize lens: validate on host-independent criteria. /ping-optimize lens: validate under simulated latency, loss and slow-server conditions.

## 9. Compatibility and version considerations
A change valid on one deployment target may break another declared target; validate or restrict it.

## 10. Security, privacy and accessibility considerations
Rollback must not expose secrets, widen permissions or touch data; production rollback requires the same explicit authorization as production change. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Automatic rollback is tested with a failing validation callback in the reference model; real-infrastructure rollback is untested unless the developer provides a safe environment.

## 12. Rollback and failure handling
Automatically roll back changes made by this workflow when validation fails, provided rollback is safe and within the authorized scope; otherwise stop and report the exact state and manual steps. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
