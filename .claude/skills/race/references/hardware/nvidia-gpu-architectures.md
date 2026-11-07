<!-- format: 13-section -->
# NVIDIA GPU architectures (curated, sourced)

## 1. Purpose and applicability
A small, verified set of NVIDIA CUDA compute-capability records plus guidance for using them. This is **not** an exhaustive SKU database. Applies when a project uses CUDA or NVIDIA-specific features.

## 2. Detection signals
CUDA runtime/driver API device-property queries (compute capability major.minor, memory, multiprocessor count); NVML for monitoring where permitted. Do not infer from marketing names.

## 3. What to inspect
Minimum compute capability the project's CUDA binaries target (fat binary/PTX); presence of a non-CUDA fallback; use of tensor-core or RT features; driver and toolkit versions.

## 4. Metrics
Kernel time, memory throughput, occupancy, transfer bandwidth, achieved speedup versus the fallback.

## 5. Common bottlenecks and anti-patterns
Shipping only SASS for one capability; no PTX or fallback; assuming higher compute capability always means faster for the workload; assuming NVIDIA-specific paths on non-NVIDIA hardware.

## 6. Candidate optimization techniques
Build for multiple capabilities plus PTX; choose kernels by queried capability; test the CPU/other-GPU fallback; use vendor-tuned libraries where they exist.

## 7. Runtime tunables versus build-time changes
Runtime: kernel variant, batch size, stream count. Build-time: `-gencode` targets, fat-binary composition.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Capability-based kernel selection is RACE. Algorithmic kernel fixes are universal.

## 9. Compatibility and version considerations
**Verified records** (source type: official page; confidence label `official-specification`):

| GPU | Compute capability | Source | Accessed |
|---|---|---|---|
| GeForce RTX 4090 | 8.9 | https://developer.nvidia.com/cuda-gpus | 2026-11-07 |
| GeForce RTX 3090 | 8.6 | https://developer.nvidia.com/cuda-gpus | 2026-11-07 |
| NVIDIA A100 | 8.0 | https://developer.nvidia.com/cuda-gpus | 2026-11-07 |
| NVIDIA H100 | 9.0 | https://developer.nvidia.com/cuda-gpus | 2026-11-07 |

GTX 1080 was not on the fetched page (it points to a legacy table), so its value is `unverified` here. These records state capability level only, not performance.

## 10. Security, privacy, accessibility, data integrity
Do not send device identifiers externally. Numerical differences between architectures (fused multiply-add, TF32) must stay within the declared tolerance.

## 11. Validation and benchmark methodology
Run the same workload on the CUDA path and the fallback; compare output and speed; record driver and toolkit versions using `hardware-benchmark` records (confidence `internally-measured`).

## 12. Rollback considerations
On kernel launch failure or mismatch, switch to the fallback and remember the failure for this driver/capability pair.

## 13. Authoritative sources and last-reviewed
NVIDIA CUDA GPUs page, https://developer.nvidia.com/cuda-gpus, accessed 2026-11-07. Values were read through the fetch tool's page summary; re-verify against the page before relying on them in a release. Last reviewed: 2026-11-07.
