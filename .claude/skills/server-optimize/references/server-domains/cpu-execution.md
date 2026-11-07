<!-- format: 13-section -->
# CPU execution on the server

## 1. Purpose and applicability
Find and reduce CPU-bound work in server code and match parallelism to the verified core count.

## 2. Detection signals
High CPU with low I/O wait, flame graphs dominated by serialization, regex, crypto, compression or hot loops; throughput that stops scaling with threads.

## 3. What to inspect
Profiler output (sampling, flame graph), hot functions, per-request CPU time, GC/allocation share, regex and JSON/XML handling, container CPU limits as seen by the runtime.

## 4. Metrics
CPU utilization, CPU time per request, run-queue/throttling counters, GC pause share, throughput per core.

## 5. Common bottlenecks and anti-patterns
Counting logical cores inside a container limited by quotas, spawning more workers than cores for CPU-bound work, catastrophic regexes, repeated serialization, synchronous hashing on request path.

## 6. Candidate optimization techniques
Algorithmic fixes first, then cache pure results, batch work, use native/SIMD-capable libraries where the target CPU is verified, bound worker counts to the effective CPU quota.

## 7. Runtime tunables versus build-time changes
Runtime: worker/thread counts, per-worker limits, compression level. Build-time: compiler flags only for a declared target architecture.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: derive worker counts from the verified effective CPU limit (cgroup quota, not host cores); pick vectorized paths only after feature verification and keep a portable fallback. /optimize lens: fix algorithms and data structures; no host assumptions. /ping-optimize lens: keep CPU headroom for TLS and compression so network paths are not starved.

## 9. Compatibility and version considerations
CPU flags differ across instance generations and architectures (x86-64 vs arm64); a binary tuned for one may crash on another.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Profile before/after under the same load; verify results are bit-identical or within tolerance; test on every declared architecture.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
