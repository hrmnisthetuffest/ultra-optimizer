<!-- format: 13-section -->
# Loaded latency (latency under load)

## 1. Purpose and applicability
Measure how latency grows when the link is busy with the app's own traffic.

## 2. Detection signals
Interactive features degrade during uploads or downloads.

## 3. What to inspect
Concurrent bulk transfers; prioritization; pacing; queue behavior.

## 4. Metrics
Idle RTT, loaded RTT, delta, interactive request latency during transfer.

## 5. Common bottlenecks and anti-patterns
Bulk traffic starving interactive requests; unbounded parallel uploads.

## 6. Candidate optimization techniques
Run an interactive probe while a bounded bulk transfer runs; compare before and after pacing or prioritization changes.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
App-level pacing and priority are adaptive options; bound them.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
Assert loaded-delta improvement without hurting bulk completion beyond an agreed budget.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
