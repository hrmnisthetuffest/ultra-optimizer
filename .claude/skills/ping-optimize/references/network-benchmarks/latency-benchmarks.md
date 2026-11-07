<!-- format: 13-section -->
# Latency benchmarks

## 1. Purpose and applicability
Measure RTT and operation latency as distributions.

## 2. Detection signals
Any claim about faster responses.

## 3. What to inspect
Probe protocol and endpoint; sampling interval; warm versus cold connection; clock source.

## 4. Metrics
RTT and request duration p50/p95/p99, cold versus warm, per-phase timings, sample counts.

## 5. Common bottlenecks and anti-patterns
Reporting a mean; mixing cold and warm; clock jumps; too few samples; testing a different endpoint than users use.

## 6. Candidate optimization techniques
Separate cold and warm series; fixed warm-up; many samples; record environment; compare with identical method before and after.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Network measurements describe one path and time; label them as such.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
Repeatability check: two baseline runs should agree within noise before changes are credited.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07)
Last reviewed: 2026-11-07.
