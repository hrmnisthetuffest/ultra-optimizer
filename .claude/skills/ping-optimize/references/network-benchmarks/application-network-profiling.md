<!-- format: 13-section -->
# Application network profiling

## 1. Purpose and applicability
Profile the app's actual requests and attribute time.

## 2. Detection signals
Starting any audit.

## 3. What to inspect
Request log with phase timings, sizes, status, protocol, connection id, cache status, retries.

## 4. Metrics
Waterfall, per-phase p95, requests per operation, reuse rate, cache hit rate, failure and retry rate, TTFB, total duration.

## 5. Common bottlenecks and anti-patterns
Logging sensitive data; instrumentation overhead; only measuring happy paths.

## 6. Candidate optimization techniques
Use existing telemetry or a temporary, developer-approved local trace with redaction; summarize with detect/summary script outputs; compare operations not just requests.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Traces are per environment; keep them local.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
Redaction test: confirm traces contain no tokens, cookies or bodies.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07)
Last reviewed: 2026-11-07.
