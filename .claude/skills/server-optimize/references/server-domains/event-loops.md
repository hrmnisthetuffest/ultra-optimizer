<!-- format: 13-section -->
# Event loops and async runtimes

## 1. Purpose and applicability
Keep single-threaded or cooperative runtimes responsive by never blocking the loop.

## 2. Detection signals
Latency spikes across unrelated requests, event-loop lag, timers firing late, CPU-bound handlers in async servers.

## 3. What to inspect
Blocking calls in async code (sync file/crypto/regex/JSON on large inputs), loop-lag metrics, worker offload, timers, promise/future fan-out.

## 4. Metrics
Event-loop lag p99, tick duration, blocked-time per handler, pending callbacks.

## 5. Common bottlenecks and anti-patterns
Synchronous heavy work on the loop, unbounded promise fan-out, awaiting in tight loops, mixing blocking drivers into async code.

## 6. Candidate optimization techniques
Offload CPU work to worker threads/processes, chunk long computations, use non-blocking drivers, bound fan-out, add loop-lag alarms.

## 7. Runtime tunables versus build-time changes
Runtime: worker pool size, chunk size. Build-time: handler structure.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size offload workers from verified cores. /optimize lens: remove blocking calls and chunk work. /ping-optimize lens: loop lag inflates apparent server RTT; measure it before blaming the network.

## 9. Compatibility and version considerations
Behavior of loop and thread pools differs per runtime and version.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Inject slow handler and assert other requests stay fast; loop-lag percentile before/after.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
