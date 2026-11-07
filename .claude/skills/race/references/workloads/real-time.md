<!-- format: 13-section -->
# Real-time workloads

## 1. Purpose and applicability
Work with deadlines (audio, video calls, games, control loops). Misses are failures, not slowdowns.

## 2. Detection signals
Fixed frame or buffer deadlines; glitches when deadlines missed.

## 3. What to inspect
Deadline budget per frame/buffer, allocations and locks on the real-time path, GC/IO in the loop.

## 4. Metrics
Deadline-miss rate, jitter, worst-case time, underruns, frame pacing.

## 5. Common bottlenecks and anti-patterns
Allocation or locking in the loop; unpredictable calls; heavy profiling on the real-time path.

## 6. Candidate optimization techniques
Preallocate, avoid locks and blocking, move non-real-time work out, add headroom, adapt quality within bounds.

## 7. Runtime tunables versus build-time changes
Runtime: buffer size, quality tier, lookahead. Build-time: loop structure.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Buffer/quality adaptation is RACE; removing blocking work is universal.

## 9. Compatibility and version considerations
Platform audio/video APIs impose constraints; do not change OS scheduling or priorities.

## 10. Security, privacy, accessibility, data integrity
Never lower safety-critical or accessibility quality.

## 11. Validation and benchmark methodology
Measure worst-case and tail, not averages; soak for long periods; no profiling on the deadline path unless lightweight.

## 12. Rollback considerations
Revert to conservative buffers on any underrun.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
