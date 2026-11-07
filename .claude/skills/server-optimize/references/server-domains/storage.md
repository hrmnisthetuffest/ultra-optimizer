<!-- format: 13-section -->
# Storage and file I/O

## 1. Purpose and applicability
Reduce storage latency and wasted I/O for disks, object stores and shared filesystems.

## 2. Detection signals
High I/O wait, many small reads/writes, large temporary files, slow cold reads, object-store request costs.

## 3. What to inspect
Access patterns (random versus sequential), file sizes, fsync use, temp files, object-store request counts, local versus network storage, ephemeral disk assumptions.

## 4. Metrics
IOPS, throughput, I/O wait, request count and cost, p99 read/write latency.

## 5. Common bottlenecks and anti-patterns
Many tiny writes, synchronous fsync per record, storing state on ephemeral disks, reading whole objects for small ranges.

## 6. Candidate optimization techniques
Batch and buffer writes, use range reads, stream, compress where it pays, keep durable state off ephemeral disks, use multipart uploads for large objects.

## 7. Runtime tunables versus build-time changes
Runtime: buffer sizes, batch sizes. Build-time: storage layout.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size buffers from verified memory; storage speed class must be verified, not inferred from instance name. /optimize lens: fix access patterns. /ping-optimize lens: transfer in ranges/chunks and resume safely.

## 9. Compatibility and version considerations
Durability semantics differ by filesystem and service; do not reduce fsync guarantees without data-loss analysis.

## 10. Security, privacy and accessibility considerations
Preserve encryption at rest and access policies; do not widen bucket or file permissions. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Integrity checksums after change; crash/recovery test; throughput comparison on representative data.

## 12. Rollback and failure handling
Never delete or rewrite production data as part of optimization. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
