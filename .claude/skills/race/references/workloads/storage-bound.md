<!-- format: 13-section -->
# Storage-bound workloads

## 1. Purpose and applicability
Work limited by disk or file-system I/O (loading, indexing, databases, logging, sync).

## 2. Detection signals
Time dominated by read/write waits; many small I/O calls; startup reads dominate.

## 3. What to inspect
I/O sizes and patterns, fsync usage, directory scans, caching, database settings under app control.

## 4. Metrics
Throughput, p95 latency, IOPS achieved, bytes read at startup, fsync count.

## 5. Common bottlenecks and anti-patterns
Tiny synchronous reads; UI-thread I/O; excessive scans; durable writes without batching.

## 6. Candidate optimization techniques
Batch/coalesce, async prefetch with bounds, memory-map where safe, tune app-owned database settings, lazy loading.

## 7. Runtime tunables versus build-time changes
Runtime: chunk size, prefetch depth, cache size. Build-time: format changes (approval needed).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Chunk/concurrency from measured storage speed are RACE; removing redundant reads is universal.

## 9. Compatibility and version considerations
File formats must stay compatible; behavior varies by file system and network volumes.

## 10. Security, privacy, accessibility, data integrity
Do not weaken durability; remove benchmark temp files.

## 11. Validation and benchmark methodology
Use bounded scratch space; compare cold and warm cache; crash-injection for durable paths.

## 12. Rollback considerations
Revert tunables; formats need tested migration/backup.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
