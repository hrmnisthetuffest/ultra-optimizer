<!-- format: 13-section -->
# Concurrency and parallelism

## 1. Purpose and applicability
Use concurrency to hide I/O wait and use cores, without races, deadlocks or overload.

## 2. Detection signals
Low CPU with high latency (serial I/O), lock contention, thread starvation, request pile-ups, nondeterministic failures.

## 3. What to inspect
Sequential awaits that could be parallel, shared mutable state, locks and their hold times, transaction isolation, background tasks sharing resources, backpressure paths.

## 4. Metrics
In-flight requests, queue depth, lock wait time, thread/worker utilization, p99 under concurrency.

## 5. Common bottlenecks and anti-patterns
Parallelizing dependent operations, unbounded fan-out, locks held across I/O, check-then-act races, retry storms, missing backpressure.

## 6. Candidate optimization techniques
Parallelize only independent operations, bound concurrency with semaphores, use immutable or sharded state, add backpressure and load shedding, use idempotency keys for retried work.

## 7. Runtime tunables versus build-time changes
Runtime: concurrency limits, queue sizes. Build-time: synchronization design.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size concurrency limits from verified cores and downstream capacity within approved bounds. /optimize lens: fix races, deadlocks and unsafe sharing; correctness before speed. /ping-optimize lens: bound outbound concurrency so one slow dependency cannot starve others.

## 9. Compatibility and version considerations
Memory-model and async semantics differ per language and runtime version.

## 10. Security, privacy and accessibility considerations
Races can become authorization or double-spend bugs; treat them as security defects. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Race detectors, stress tests with randomized scheduling, deadlock timeouts, idempotency tests.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
