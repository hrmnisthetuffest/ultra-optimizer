<!-- format: 13-section -->
# Memory-bound workloads

## 1. Purpose and applicability
Work limited by memory bandwidth, latency or capacity (large data scans, caches, large models, big images).

## 2. Detection signals
More cores do not scale; cache misses high; paging or GC pressure visible; footprint near limits.

## 3. What to inspect
Data layout, working-set size, cache sizes, allocation churn, GC settings, mapped files.

## 4. Metrics
Peak/steady memory, bandwidth achieved, cache-miss rate, GC pause, page faults.

## 5. Common bottlenecks and anti-patterns
Pointer-chasing structures; oversized caches; unbounded growth; copying large buffers.

## 6. Candidate optimization techniques
Contiguous layouts, streaming, blocking/tiling, bounded caches sized from available memory (RACE), reduce copies.

## 7. Runtime tunables versus build-time changes
Runtime: cache caps, batch size. Build-time: layout, allocator (dependency needs approval).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Budgets from detected memory are RACE; layout fixes are universal.

## 9. Compatibility and version considerations
Container and mobile limits differ from host totals.

## 10. Security, privacy, accessibility, data integrity
Never retain secrets longer than needed; eviction must not lose unsaved data.

## 11. Validation and benchmark methodology
Soak test bounded growth; test at minimum budget; measure peak before/after.

## 12. Rollback considerations
Restore previous caps; shrink immediately on pressure.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
