<!-- format: 13-section -->
# Memory intelligence

## 1. Purpose and applicability
How RACE reasons about RAM, VRAM and unified memory to set budgets without causing paging or crashes. Applies to cache, pool, buffer and batch-size tuning.

## 2. Detection signals
OS/runtime queries for total and available memory, container/cgroup limits, memory-pressure notifications, process working set, GPU memory from the graphics API, unified-memory indication. Record `unknown` when unavailable.

## 3. What to inspect
Largest allocations, cache sizes, growth patterns, allocation churn, memory-mapped files, runtime GC settings, large-object behavior, leak suspects, platform low-memory handling.

## 4. Metrics
Peak and steady-state memory, allocation rate, GC pause time, page-fault rate, swap activity if observable, cache hit rate, VRAM use.

## 5. Common bottlenecks and anti-patterns
Budgets as a fixed fraction of total RAM ignoring other processes; no response to pressure signals; unbounded caches; assuming channel count or bandwidth from capacity; ignoring container limits; tuning the OS pagefile or other system memory settings (forbidden).

## 6. Candidate optimization techniques
Bounded caches with eviction; budgets derived from currently available memory with headroom and re-evaluated on pressure; object pooling where churn is measured; contiguous layouts for hot data; streaming instead of loading whole files; shrink caches on pressure notifications.

## 7. Runtime tunables versus build-time changes
Runtime: cache and pool caps, batch size, prefetch depth. Build-time: data layout, allocator choice (a new dependency needs approval).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Budgets from detected memory are RACE. Fixing leaks or reducing allocations in code is universal.

## 9. Compatibility and version considerations
Mobile OSes terminate apps under memory pressure; browsers and sandboxes limit memory; 32-bit processes have address-space limits.

## 10. Security, privacy, accessibility, data integrity
Do not log memory contents. Clearing caches must not drop unsaved user data. Do not move secrets into pooled buffers that are not zeroed.

## 11. Validation and benchmark methodology
Soak test for bounded growth; simulate low-memory conditions; measure peak before/after; verify behavior at the minimum budget is correct, merely slower.

## 12. Rollback considerations
Restore previous caps; on out-of-memory signals drop to the smallest safe budget immediately.

## 13. Authoritative sources and last-reviewed
Platform memory APIs vary; consult official docs per project (not fetched; claims are generic and **unverified for specific platforms**). Last reviewed: 2026-11-07.
