<!-- format: 13-section -->
# Scheduling and idle detection

## 1. Purpose and applicability
Decide when optional RACE work (L2 sampling bursts, L3 benchmarks, calibration) may run so users never feel it. Applies to any integration that benchmarks.

## 2. Detection signals
App-owned signals: time since last input, foreground task state, active call/recording/render/export/gameplay/meeting, pending safe-queue work, battery or low-power mode flag exposed by the platform to apps.

## 3. What to inspect
Where the app already tracks activity; which states are critical in this product (ask the developer if not obvious); available platform idle APIs and their permissions.

## 4. Metrics
Idle window length; number of benchmark pauses/aborts; foreground interference measured as added latency during a run (target: none observable).

## 5. Common bottlenecks and anti-patterns
Relying only on OS idle time; starting at an exact minute mark regardless of state; benchmarks that cannot be cancelled; ignoring low-power or battery-saver as a signal; running on battery with no policy.

## 6. Candidate optimization techniques
Scheduler policy: eligible only when (a) cumulative foreground time threshold met, (b) app-defined idle, (c) no critical state, (d) battery and thermal acceptable. Run in small cancellable slices; pause on any user activity; resume later; abort on thermal, battery or error signals. Treat low-power/battery-saver as an app policy input; **never change the device setting**.

## 7. Runtime tunables versus build-time changes
Runtime: idle threshold, slice length, max run duration. Build-time: where activity hooks are installed.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Thermal and battery policies are hardware/platform dependent and belong to RACE. Generic job-queue changes for the app's own background work are universal.

## 9. Compatibility and version considerations
Idle and power signals differ by OS and by API version; always degrade to "do not run" when a signal is unavailable.

## 10. Security, privacy, accessibility, data integrity
Idle signals must not reveal what the user is doing; store only booleans/durations. A running benchmark must be visibly pausable by assistive-technology users if a notice is shown.

## 11. Validation and benchmark methodology
Test: no run before the threshold; pause within a bounded time after user activity; abort on thermal/battery; resume correctly; no run in critical state (see `tests/test_race_reference_model.py`).

## 12. Rollback considerations
An aborted run discards partial results and applies nothing; state returns to last-known-good.

## 13. Authoritative sources and last-reviewed
Project spec sections 5.2-5.6. Platform idle APIs: consult each platform's official docs per integration (not fetched this session). Last reviewed: 2026-11-07.
