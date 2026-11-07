<!-- format: 13-section -->
# Monolith and modular monolith

## 1. Purpose and applicability
Single deployable; optimize inside before splitting.

## 2. Detection signals
Detect from repo layout, deployment files, service boundaries and messaging dependencies.

## 3. What to inspect
Inspect: hot modules, shared state, DB access patterns

## 4. Metrics
End-to-end latency, throughput, queue depth, error rate, resource use per component.

## 5. Common bottlenecks and anti-patterns
tangled modules; chatty internal calls; shared locks.

## 6. Candidate optimization techniques
profile first; fix module boundaries; cache; do not split services without evidence.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: adaptive concurrency and budgets inside the app. /optimize: protocol, query and structure fixes. No-go: microservice splits or rewrites without approval and evidence.

## 9. Compatibility and version considerations
Keep wire formats and API versions compatible across deployed versions.

## 10. Security, privacy, accessibility, data integrity
Do not weaken auth, tenant isolation or data protection for speed.

## 11. Validation and benchmark methodology
Compare end-to-end metrics before/after.

## 12. Rollback considerations
Feature-flag architectural changes; revert flags first.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
