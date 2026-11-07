<!-- format: 13-section -->
# AI applications (existing pipelines only)

## 1. Purpose and applicability
Apps with inference pipelines already present. Developer-selected AI features are separate; RACE never adds AI.

## 2. Detection signals
Inference runtimes, model files, provider calls.

## 3. What to inspect
Runtime/backend, precision, batching, concurrency, caches, quality metrics.

## 4. Metrics
Latency, throughput, memory, quality score on a fixed evaluation set.

## 5. Common bottlenecks and anti-patterns
Faster-but-worse output; unbounded context; per-request model load.

## 6. Candidate optimization techniques
Provider selection among existing ones, batching, caching with bounds; quality-gated precision (RACE, see ai-accelerators).

## 7. Runtime tunables versus build-time changes
Runtime: provider, batch size, concurrency, cache budget.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: adding models/vendors/agents/network APIs, uploading data, silent quality loss.

## 9. Compatibility and version considerations
Runtime and operator support vary by version.

## 10. Security, privacy, accessibility, data integrity
No data leaves the device unless the app already does so by design; keep consent flows.

## 11. Validation and benchmark methodology
Quality plus speed measured together.

## 12. Rollback considerations
Previous backend/precision as last-known-good.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
