<!-- format: 13-section -->
# Storage and I/O intelligence

## 1. Purpose and applicability
Reason about storage latency and throughput for the app's own I/O patterns. Applies to apps with significant file, database or cache I/O.

## 2. Detection signals
App-level measured read/write latency and throughput on the app's own data directory using small, safe, bounded tests; OS-reported volume type where available (do not assume SSD/HDD from names); file system type; network or removable volume indication.

## 3. What to inspect
I/O patterns (sequential vs random, small vs large, sync vs async), fsync frequency, cache and temp-file locations, database settings under app control, startup file reads, directory scanning.

## 4. Metrics
Read/write throughput, p95/p99 latency, IOPS achieved, bytes read at startup, fsync count, cache hit rate.

## 5. Common bottlenecks and anti-patterns
Many tiny synchronous reads; scanning large trees on the UI thread; excessive fsync; benchmarking by filling the disk; benchmarks that wear storage; assuming a local disk when the path is a network share; changing disk, scheduler or mount settings (forbidden).

## 6. Candidate optimization techniques
Batch and coalesce I/O; async/prefetch with bounded depth; memory-map where safe; compress when CPU is cheaper than I/O (measured); tune the app's own database page/cache settings within registered ranges; write-ahead patterns that keep durability.

## 7. Runtime tunables versus build-time changes
Runtime: prefetch depth, I/O chunk size, cache size, concurrency. Build-time: file format changes (need approval; compatibility).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Chunk sizes and concurrency from measured storage characteristics: RACE. Removing redundant reads or fixing N+1 queries: universal.

## 9. Compatibility and version considerations
File formats and on-disk layouts must remain readable by previous and next app versions. Behavior differs across file systems and network volumes.

## 10. Security, privacy, accessibility, data integrity
Never reduce durability guarantees (fsync/atomic rename) for speed without explicit approval. Temp files must not leak content; benchmark files must be removed.

## 11. Validation and benchmark methodology
Use app-owned scratch space with a hard size limit; compare warm vs cold cache; crash-injection tests for durability-sensitive changes.

## 12. Rollback considerations
Revert tunables to previous values; any format change needs a migration with a tested downgrade or backup path.

## 13. Authoritative sources and last-reviewed
Generic method; platform I/O documentation to be cited per project (not fetched; **unverified** for specifics). Last reviewed: 2026-11-07.
