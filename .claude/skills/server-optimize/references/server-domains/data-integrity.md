<!-- format: 13-section -->
# Data integrity

## 1. Purpose and applicability
Ensure optimizations never lose, duplicate or corrupt data.

## 2. Detection signals
Retries, caching, batching, async writes, concurrency, migrations.

## 3. What to inspect
Transactions, constraints, idempotency, ordering, replication, write paths, caches that can serve stale data after writes.

## 4. Metrics
Constraint violations, duplicate rate, divergence between replicas or caches, checksum mismatches.

## 5. Common bottlenecks and anti-patterns
Async writes without confirmation, batching that loses partial failures, caches not invalidated, relaxed isolation without analysis.

## 6. Candidate optimization techniques
Keep constraints, use idempotency keys, transactional outbox, checksums, careful batching with per-item results.

## 7. Runtime tunables versus build-time changes
Runtime: batch size, flush interval within durability limits.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: none. /optimize lens: correctness first. /ping-optimize lens: retries must not duplicate operations.

## 9. Compatibility and version considerations
Isolation levels differ by engine.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Crash tests, duplicate-injection tests, checksum comparison before and after.

## 12. Rollback and failure handling
Data-affecting changes need a tested restore path before they are authorized. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
