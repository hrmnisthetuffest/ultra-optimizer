<!-- format: 13-section -->
# Thread and worker pools

## 1. Purpose and applicability
Choose pool sizes and queue policies that match the workload mix (CPU-bound versus blocking I/O).

## 2. Detection signals
Pool exhaustion, long queue waits, rejected tasks, thread count in the thousands, deadlock through nested pool waits.

## 3. What to inspect
Pool types and sizes, queue boundedness, rejection policy, tasks that block on other tasks in the same pool, separation of pools by workload.

## 4. Metrics
Active threads, queue length and wait, rejection count, task duration distribution.

## 5. Common bottlenecks and anti-patterns
One shared pool for CPU and blocking work, unbounded queues, nested blocking waits, pool size equal to request volume.

## 6. Candidate optimization techniques
Separate pools per workload class, bound queues, apply rejection/backpressure, size CPU pools near the effective core count and blocking pools by downstream capacity.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, queue capacity, timeouts.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: derive CPU pool size from verified effective cores; keep within approved min/max. /optimize lens: fix nested waits and misuse. /ping-optimize lens: limit outbound pools to the remote's tolerance.

## 9. Compatibility and version considerations
Virtual threads/green threads change sizing advice; check runtime version.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Load test with mixed workloads; pool saturation behavior; no deadlock under full queue.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
