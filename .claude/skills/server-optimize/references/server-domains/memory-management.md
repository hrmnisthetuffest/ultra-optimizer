<!-- format: 13-section -->
# Server memory management

## 1. Purpose and applicability
Keep memory use within the host or container limit, avoid leaks and reduce allocation churn without risking out-of-memory kills.

## 2. Detection signals
Growing RSS, OOM kills, long GC pauses, high allocation rate, container restarts, swap use.

## 3. What to inspect
Heap profiles, object retention, unbounded caches/queues/maps, per-request buffers, container memory limit versus runtime heap settings, memory-mapped data.

## 4. Metrics
RSS, heap size, GC frequency and pause, allocation rate, OOM events, cache memory share.

## 5. Common bottlenecks and anti-patterns
Unbounded in-memory caches, loading whole payloads into memory, per-request large buffers, heap limit above the container limit, leaks through listeners or closures.

## 6. Candidate optimization techniques
Bound every cache and queue, stream instead of buffering, pool large buffers, size runtime heap to a fraction of the verified limit, release resources deterministically.

## 7. Runtime tunables versus build-time changes
Runtime: heap caps, cache sizes, buffer pool sizes. Build-time: data representation.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: set application memory budgets from the verified memory limit, with a safety margin and developer-approved bounds. /optimize lens: fix leaks, retention and allocation patterns. /ping-optimize lens: avoid buffering whole transfers; stream to keep memory flat under slow clients.

## 9. Compatibility and version considerations
Runtime memory flags are version and vendor specific; verify flags exist in the deployed runtime version.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Soak test with flat-memory assertion; load test at the memory limit; OOM and restart counts.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
