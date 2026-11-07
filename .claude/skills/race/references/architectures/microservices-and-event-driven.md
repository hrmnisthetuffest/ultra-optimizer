<!-- format: 13-section -->
# Microservices and event-driven systems

## 1. Purpose and applicability
Distributed services, queues and streams.

## 2. Detection signals
Detect from repo layout, deployment files, service boundaries and messaging dependencies.

## 3. What to inspect
Inspect: service call graph, payload sizes, retries, queue consumers, idempotency

## 4. Metrics
End-to-end latency, throughput, queue depth, error rate, resource use per component.

## 5. Common bottlenecks and anti-patterns
chatty calls; retry storms; head-of-line blocking; unbounded queues.

## 6. Candidate optimization techniques
batch calls, bound retries with backoff, backpressure, partitioning review, caching.

## 7. Runtime tunables versus build-time changes
Runtime: consumer concurrency, batch size, timeouts.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: adaptive concurrency and budgets inside the app. /optimize: protocol, query and structure fixes. No-go: changing delivery semantics or message schemas without versioning.

## 9. Compatibility and version considerations
Keep wire formats and API versions compatible across deployed versions.

## 10. Security, privacy, accessibility, data integrity
Do not weaken auth, tenant isolation or data protection for speed.

## 11. Validation and benchmark methodology
Distributed traces; load and failure-injection tests.

## 12. Rollback considerations
Feature-flag architectural changes; revert flags first.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
