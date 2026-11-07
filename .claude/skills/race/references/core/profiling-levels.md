<!-- format: 13-section -->
# Profiling levels

## 1. Purpose and applicability
Three levels separate "observe", "measure lightly" and "actively benchmark". Permission to observe is not permission to modify, and profiling is not stress benchmarking.

## 2. Detection signals
Need to know: does the app have a loading screen; how foreground time is tracked; what metrics already exist.

## 3. What to inspect
Existing timing and logging; cost of adding counters; platform profiling APIs that are permitted without special privileges.

## 4. Metrics
**L1 passive**: startup phases, time-to-interactive, operation durations the app already records. **L2 lightweight**: sampled p50/p95/p99, frame times, queue depths, memory footprint, with a bounded overhead budget the developer approves (state it, measure it). **L3 active**: controlled benchmarks (see `benchmarking-methodology.md`).

## 5. Common bottlenecks and anti-patterns
Running anything heavy on a loading screen; lengthening startup for data collection; always-on profilers with unmeasured overhead; logging content or identifiers; benchmarking GPU for non-GPU apps.

## 6. Candidate optimization techniques
Timing rules:
- **Loading screen**: only minimal capability detection and startup timings, within a strict budget. Never prolong the loading screen. Record already-known timings. Defer deeper work.
- **No loading screen**: minimal detection, passive observation. No heavy benchmark until **30 minutes of cumulative active/foreground use** have accrued; even then only when idle or otherwise safe (the 30 minutes is the earliest point deeper profiling may be considered, not a moment to interrupt).
- **Daily use**: low-overhead metrics subject to privacy and user preference. No daily full benchmark. Initial calibration once per relevant install/configuration; repeat only on a major app update, a runtime/driver/API capability change, a persistent regression, a changed workload profile, or explicit user request.

## 7. Runtime tunables versus build-time changes
Runtime: sampling rate, whether L2/L3 are enabled, pause/disable. Build-time: instrumentation points.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Which L3 benchmarks to run depends on the detected hardware and workload class (CPU 1T/parallel, GPU render/compute/transfer, memory, storage). Generic code-level profiling for algorithm fixes is outside RACE.

## 9. Compatibility and version considerations
Use only supported, permissioned APIs per platform. Where no API exists, report the metric as `unknown`.

## 10. Security, privacy, accessibility, data integrity
Aggregate only; no content, serials, accounts, passwords or tokens. User can pause/disable profiling. Accessibility: a profiling notice must be screen-reader accessible.

## 11. Validation and benchmark methodology
Measure the profiler's own overhead with it on and off; verify the loading screen duration is unchanged; verify no L3 run occurs before the cumulative-foreground threshold (see `templates/race_reference_model.py` and `tests/test_race_reference_model.py`).

## 12. Rollback considerations
Disabling profiling must leave the app fully functional with defaults or last-known-good values.

## 13. Authoritative sources and last-reviewed
Project spec section 5. Last reviewed: 2026-11-07.
