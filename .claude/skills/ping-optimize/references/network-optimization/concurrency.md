<!-- format: 13-section -->
# Request concurrency

## 1. Purpose and applicability
Right-size parallelism. More parallelism helps latency-bound independent work and hurts under bandwidth limits, loss, rate limits or shared bottlenecks.

## 2. Detection signals
Request storms; rate-limit errors; slow total despite many parallel calls; or serial code with idle link.

## 3. What to inspect
Concurrency caps; dependency graph; rate limits; per-origin connection limits; shared queues.

## 4. Metrics
In-flight requests, queueing time, 429/503 rate, throughput versus concurrency curve.

## 5. Common bottlenecks and anti-patterns
Unbounded Promise.all or thread fan-out; fixed high concurrency; concurrency raised just because bandwidth is high.

## 6. Candidate optimization techniques
Bounded pools; AIMD-style adaptation (increase slowly, decrease fast on errors or latency growth); per-host caps; respect Retry-After.

## 7. Runtime tunables versus build-time changes
Runtime: min, max, step, thresholds. All in the tuning registry with ranges.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Adaptive, measured, bounded. Never scale concurrency from bandwidth alone.

## 9. Compatibility and version considerations
Server-side limits are a contract; stay within them.

## 10. Security, privacy and accessibility considerations
Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Reference model: network_reference_model.AdaptiveConcurrency (hysteresis, bounds). Test flapping inputs.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
