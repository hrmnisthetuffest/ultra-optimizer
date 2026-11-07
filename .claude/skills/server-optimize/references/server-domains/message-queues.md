<!-- format: 13-section -->
# Message queues and streams

## 1. Purpose and applicability
Improve queue throughput and latency while keeping delivery guarantees.

## 2. Detection signals
Growing backlog, slow consumers, redelivery loops, poison messages, ordering bugs.

## 3. What to inspect
Producer rate, consumer concurrency, ack/commit strategy, retry and dead-letter policy, ordering requirements, message size, idempotent handling.

## 4. Metrics
Queue depth, age of oldest message, consumer lag, processing time, redelivery rate, DLQ size.

## 5. Common bottlenecks and anti-patterns
Auto-ack before processing, infinite redelivery, no idempotency, huge messages, one slow partition blocking all.

## 6. Candidate optimization techniques
Idempotent consumers, bounded retries with backoff and DLQ, batch consumption, right-sized concurrency, store large payloads externally.

## 7. Runtime tunables versus build-time changes
Runtime: prefetch, batch size, consumer count, visibility timeout.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: set consumer counts from verified cores and downstream limits within approved bounds. /optimize lens: fix idempotency and retry design. /ping-optimize lens: consumer round trips and broker network efficiency.

## 9. Compatibility and version considerations
Guarantees (at-least-once, exactly-once, ordering) differ per broker and configuration.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Duplicate-delivery test, poison-message test, backlog drain test, ordering test.

## 12. Rollback and failure handling
Never purge or replay production queues without explicit authorization. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
