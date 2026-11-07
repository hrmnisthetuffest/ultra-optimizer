<!-- format: 13-section -->
# Databases

## 1. Purpose and applicability
Find slow or wasteful queries and connection patterns and fix them without risking data.

## 2. Detection signals
Slow query log entries, N+1 patterns, high connection counts, lock waits, full table scans, replication lag.

## 3. What to inspect
Query plans, missing or unused indexes, ORM-generated SQL, transaction scope, connection pool config versus database max connections, read/write split, schema in repo.

## 4. Metrics
Query latency percentiles, rows examined versus returned, lock wait, pool wait time, connections in use, cache hit ratio.

## 5. Common bottlenecks and anti-patterns
N+1, SELECT star on wide rows, unbounded scans, long transactions, pool sizes that sum above the database limit, per-request connections.

## 6. Candidate optimization techniques
Add or correct indexes (reviewed), batch and eager load, narrow selects, shorten transactions, size pools to database capacity, use read replicas only where staleness is acceptable.

## 7. Runtime tunables versus build-time changes
Runtime: pool min/max, statement timeouts. Build-time: schema, indexes, query code.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size the connection pool from the verified database connection limit and app instance count. /optimize lens: fix queries and transaction design. /ping-optimize lens: count round trips to the database and place caches to reduce them.

## 9. Compatibility and version considerations
Index and schema changes are migrations; they need explicit authorization and a tested reversal. Behavior differs by engine and version.

## 10. Security, privacy and accessibility considerations
No destructive statements, no migrations against staging or production without explicit authorization; never print connection strings; use read-only credentials for inspection. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
EXPLAIN before/after on a representative dataset in a safe environment; results identical; lock and write-amplification checks for new indexes.

## 12. Rollback and failure handling
Index and migration changes need a tested down path before they are authorized. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
