<!-- format: 13-section -->
# CPU intelligence

## 1. Purpose and applicability
What RACE should read about a CPU, how to reason about it, and what not to conclude. Applies to thread-count, work-partitioning, SIMD-path and cache-budget decisions.

## 2. Detection signals
Read via supported interfaces only: the OS/runtime API for logical and physical core counts, the language runtime's parallelism hint, CPU feature queries (CPUID on x86 with OS-enabled-state checks; platform feature APIs on ARM), cache-topology queries the OS exposes, NUMA queries. Do not parse brand strings to infer capability. Anything unreadable is recorded as `unknown`.

## 3. What to inspect
Vendor, family/model, architecture, physical vs logical cores (SMT/hyper-threading), heterogeneous cores (performance vs efficiency classes, where the OS exposes them), cache sizes and sharing, NUMA nodes, ISA extensions, whether the process is native or emulated/translated. Fields map to `schemas/hardware-capability.schema.json`.

## 4. Metrics
Single-thread time, parallel scaling curve (speedup versus threads), lock contention time, cache miss rate where measurable, context-switch rate, tail latency under load. Specs are hints; only measurement shows performance.

## 5. Common bottlenecks and anti-patterns
Thread count = logical cores without testing; ignoring efficiency cores or SMT siblings that share execution units; false sharing; hardcoding vendor assumptions; treating a newer generation as faster for the workload without a benchmark; setting thread affinity or priority at the OS level (system settings are out of scope; app-level pool sizing is allowed).

## 6. Candidate optimization techniques
Size worker pools from physical cores and measured scaling; cap parallelism for memory-bound work; partition work to keep data cache-local; select SIMD paths (see `instruction-sets-and-dispatch.md`); use bounded queues; keep a conservative default when topology is unknown.

## 7. Runtime tunables versus build-time changes
Runtime: pool size, chunk size, queue depth, path selector. Build-time: per-function SIMD compilation, data layout changes.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
All topology- and ISA-driven choices are RACE. Algorithmic complexity and data-structure fixes are universal.

## 9. Compatibility and version considerations
Heterogeneous-core reporting differs by OS and version; containers, VMs and cgroup limits can report host cores while granting fewer. Prefer the limit the process actually has (affinity/cgroup-aware count from the runtime) over the raw host value.

## 10. Security, privacy, accessibility, data integrity
Detailed CPU identifiers can fingerprint a device. Store a coarse capability class; do not transmit raw identifiers. Never disable speculative-execution mitigations.

## 11. Validation and benchmark methodology
Run a scaling test (1, 2, 4, ... threads) on the real workload; compare the chosen pool size against neighbors; repeat with warm and cold caches; check results equal the baseline.

## 12. Rollback considerations
Persist last-known-good pool size and path; return to the baseline default on capability-class change or regression.

## 13. Authoritative sources and last-reviewed
No vendor documents were fetched for this file; guidance is general method and is **unverified for any specific model**. Add vendor-specific facts via `knowledge-expansion.md` with URL and access date. Last reviewed: 2026-11-07.
