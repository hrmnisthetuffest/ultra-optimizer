<!-- format: 13-section -->
# Network-adaptive behavior

## 1. Purpose and applicability
Let the application adjust its OWN networking behavior to measured conditions, with evidence and limits. This is the RACE-style adaptive layer for networking.

## 2. Detection signals
One configuration fails on slow, unstable or high-latency links; quality or concurrency fixed regardless of conditions.

## 3. What to inspect
Existing adaptation (ABR, quality tiers); condition classifier; thresholds; hysteresis; user overrides.

## 4. Metrics
Condition classification accuracy against measurement, switch frequency, user-perceived latency per condition.

## 5. Common bottlenecks and anti-patterns
Flapping between modes; adapting on one sample; scaling concurrency with bandwidth; hiding degradation from the user.

## 6. Candidate optimization techniques
Classify into fast-stable, slow, unstable, high-latency, lossy using rolling percentiles; hysteresis and dwell time; per-condition policy tables: fast-stable (bounded concurrency increase, justified prefetch), slow (prioritize critical, defer nonessential, smaller payloads), unstable (resumable, backoff, preserve state), high-latency (fewer round trips, reuse, batch), lossy (avoid aggressive retransmission, conservative recovery).

## 7. Runtime tunables versus build-time changes
Runtime: thresholds, dwell time, policy values, in the tuning registry with ranges, fallbacks and last-known-good.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Entirely measured-condition (RACE-style). Requires developer authorization, a user control to pause or disable, and documented behavior.

## 9. Compatibility and version considerations
Policy changes must not break API contracts or rate limits.

## 10. Security, privacy and accessibility considerations
Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized. No runtime monitoring without developer authorization and documented user controls.

## 11. Validation and testing
Reference model AdaptiveConcurrency/classifier tests; network_sim sweeps; verify no flapping and bounded outputs.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
