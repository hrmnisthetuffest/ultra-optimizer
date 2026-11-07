<!-- format: 13-section -->
# Serverless, batch and streaming

## 1. Purpose and applicability
Short-lived functions, scheduled batches, continuous streams.

## 2. Detection signals
Detect from repo layout, deployment files, service boundaries and messaging dependencies.

## 3. What to inspect
Inspect: cold starts, memory sizing, batch sizes, checkpointing

## 4. Metrics
End-to-end latency, throughput, queue depth, error rate, resource use per component.

## 5. Common bottlenecks and anti-patterns
cold-start cost; oversized batches; non-idempotent retries.

## 6. Candidate optimization techniques
trim dependencies, tune batch and memory settings within app/config control, checkpoint safely.

## 7. Runtime tunables versus build-time changes
Runtime: batch size, concurrency.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: adaptive concurrency and budgets inside the app. /optimize: protocol, query and structure fixes. No-go: changing exactly-once/at-least-once guarantees.

## 9. Compatibility and version considerations
Keep wire formats and API versions compatible across deployed versions.

## 10. Security, privacy, accessibility, data integrity
Do not weaken auth, tenant isolation or data protection for speed.

## 11. Validation and benchmark methodology
Replay tests with fixed inputs.

## 12. Rollback considerations
Feature-flag architectural changes; revert flags first.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
