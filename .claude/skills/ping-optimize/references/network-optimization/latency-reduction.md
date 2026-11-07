<!-- format: 13-section -->
# Latency reduction playbook

## 1. Purpose and applicability
Ordered checklist for lowering user-perceived waiting.

## 2. Detection signals
Operations bound by round trips rather than bandwidth.

## 3. What to inspect
Round trips per operation; handshakes; dependency chains; critical path; post-response work.

## 4. Metrics
Sequential round trips, operation latency percentiles, handshake share.

## 5. Common bottlenecks and anti-patterns
Serial awaits; per-call connections; large first payloads; waiting on non-critical data; work after response on main thread.

## 6. Candidate optimization techniques
1) Remove requests. 2) Parallelize independent ones. 3) Reuse connections. 4) Combine dependent calls server-side where owners agree. 5) Shrink payloads. 6) Cache. 7) Stream partial results. 8) Move processing off the critical path. 9) Only then adaptive tuning.

## 7. Runtime tunables versus build-time changes
Runtime: concurrency, timeouts. Build-time: API shape and bundling.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Steps 1-8 are universal; step 9 is measured-condition adaptation.

## 9. Compatibility and version considerations
API changes require versioning and old-client support.

## 10. Security, privacy and accessibility considerations
Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Report round-trip count and percentile latency before and after for each step; keep only changes that help.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack. web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07) (TTFB components).
Last reviewed: 2026-11-07.
