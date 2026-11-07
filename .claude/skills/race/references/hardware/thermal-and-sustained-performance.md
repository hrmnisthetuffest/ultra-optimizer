<!-- format: 13-section -->
# Thermal and sustained performance

## 1. Purpose and applicability
Short bursts and sustained load behave differently. Applies to benchmark design, scheduling and tunables for long-running workloads.

## 2. Detection signals
Only signals the platform exposes to apps without special privileges: thermal-state notifications (where offered), battery/charging state, low-power-mode flag, observed throughput decay over time. Record `unknown` otherwise; do not read protected sensors or change fan/clock behavior.

## 3. What to inspect
Workloads running longer than a minute at high utilization; mobile/laptop share of targets; whether the app already reacts to thermal or battery state.

## 4. Metrics
Throughput over time (first minute vs steady state), frame time drift, thermal-state changes reported by the platform, battery drain rate when measurable.

## 5. Common bottlenecks and anti-patterns
Choosing a configuration from a 10-second benchmark that collapses at minute five; running benchmarks on battery; ignoring thermal notifications; attempting to control fans, clocks or power plans (forbidden).

## 6. Candidate optimization techniques
Benchmark long enough to see sustained behavior but within the bounded budget; reduce parallelism or quality gradually on thermal notification; schedule optional work when charging and idle; prefer configurations with stable throughput for sustained workloads.

## 7. Runtime tunables versus build-time changes
Runtime: parallelism cap, quality scale, background-work toggle keyed to thermal/battery state.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Reacting to thermal state is RACE; making the algorithm do less work is universal.

## 9. Compatibility and version considerations
Thermal APIs differ widely or are absent; degrade to "no adaptation".

## 10. Security, privacy, accessibility, data integrity
Battery and thermal data can reveal usage patterns; keep it local. Do not degrade accessibility features when throttling.

## 11. Validation and benchmark methodology
Compare burst vs sustained results; repeat runs with a cool-down; flag or exclude runs affected by thermal events.

## 12. Rollback considerations
On thermal or battery abort, discard the run and keep last-known-good.

## 13. Authoritative sources and last-reviewed
Platform thermal/power API docs per project (not fetched; **unverified**). Last reviewed: 2026-11-07.
