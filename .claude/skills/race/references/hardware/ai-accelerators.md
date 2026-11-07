<!-- format: 13-section -->
# AI accelerators (existing AI pipelines only)

## 1. Purpose and applicability
Applies **only** when the application already contains an AI inference pipeline or the developer explicitly selected AI optimization. RACE never adds a model, vendor, agent, network API or data collection on its own.

## 2. Detection signals
Existing inference runtime and backend in code/manifests; NPU/GPU/CPU execution providers the runtime reports; precisions the runtime reports (FP32/FP16/BF16/INT8, etc.); memory available for models.

## 3. What to inspect
Current backend, model format and precision, batch size, concurrency, device placement, KV-cache or context budgets, quality metrics already used, latency/throughput targets.

## 4. Metrics
Latency (time to first token or per inference), throughput, memory/VRAM, power if measurable, and **output quality metrics** on a fixed evaluation set.

## 5. Common bottlenecks and anti-patterns
Faster-but-worse output counted as a win; swapping models or vendors; sending prompts or data to a hosted service; quantizing without a quality check; benchmarking with toy inputs; assuming NPUs beat GPUs for the model.

## 6. Candidate optimization techniques
Select among the runtime's existing providers by measurement; tune batch size and concurrency; adjust cache budgets; choose among already-supported precisions only if quality holds on the evaluation set; warm-up and model-load strategies.

## 7. Runtime tunables versus build-time changes
Runtime: provider selector, batch size, concurrency, cache budget. Build-time: adding a new provider/backend (needs developer approval).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Placement on CPU/GPU/NPU is RACE. `/optimize` does not choose devices or backends.

## 9. Compatibility and version considerations
Runtime/provider versions determine available operators and precisions; record them with results.

## 10. Security, privacy, accessibility, data integrity
No uploading of user data or code to AI providers. Model files are verified artifacts; do not download new models at runtime.

## 11. Validation and benchmark methodology
Fixed evaluation set; compare quality metric and latency together; reject candidates below the developer's quality threshold.

## 12. Rollback considerations
Keep the previous backend/precision as last-known-good; revert on quality drop or errors.

## 13. Authoritative sources and last-reviewed
Project spec sections 6.8 and 10. Runtime vendor docs to be cited per project (not fetched; **unverified**). Last reviewed: 2026-11-07.
