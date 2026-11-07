<!-- format: 13-section -->
# Bandwidth benchmarks

## 1. Purpose and applicability
Measure goodput honestly and cheaply.

## 2. Detection signals
Need to compare transfer changes or characterize a link.

## 3. What to inspect
Transfer size, number of flows, warm-up, whether the server or the link limits.

## 4. Metrics
Goodput up and down, p50/p95 across repeats, transfer duration, CPU.

## 5. Common bottlenecks and anti-patterns
Single run; tiny transfers dominated by slow start; testing against a different path than production; consuming user data plan.

## 6. Candidate optimization techniques
Warm-up, repeats, fixed sizes, bounded bytes; compare in network_sim with a bandwidth cap; also test with a real authorized endpoint if available.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Results are environment-specific; do not generalize across machines or networks.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
Hash-verify payloads; run at least several repeats; report variance.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
