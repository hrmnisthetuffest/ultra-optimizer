<!-- format: 13-section -->
# Jitter and packet-loss measurement

## 1. Purpose and applicability
Measure variation and loss for real-time paths.

## 2. Detection signals
Real-time audio/video/game features.

## 3. What to inspect
Sequence numbers, timestamps, jitter buffer, loss counters.

## 4. Metrics
Jitter statistic, loss rate, burst length, late-packet rate, recovery time.

## 5. Common bottlenecks and anti-patterns
Mean-only reporting; assuming uniform loss; counting reordering as loss.

## 6. Candidate optimization techniques
Inject uniform and bursty loss and variable delay in network_sim; run enough messages for stable rates.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Real networks differ from simulation; label simulated results as simulated.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
Assert correctness properties (no duplicates, eventual state) not just speed.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
