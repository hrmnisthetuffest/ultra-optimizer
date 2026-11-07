<!-- format: 13-section -->
# Instruction sets and dispatch

## 1. Purpose and applicability
How to choose between scalar and vector (SIMD) implementations safely. Applies when adding or auditing CPU-specific paths.

## 2. Detection signals
x86-64: SSE, SSE2 (baseline for x86-64), SSE4.x, AVX, AVX2, FMA, AVX-512 (many subsets), AES-NI, BMI. ARM64: NEON (Advanced SIMD), SVE/SVE2, crypto extensions. Detection must check (a) the CPU reports the feature and (b) the OS has enabled the required register state (on x86, the XSAVE/XGETBV state for AVX and AVX-512). Do not infer from brand or model strings.

## 3. What to inspect
Hot loops that are data-parallel; existing intrinsics or auto-vectorization; build flags (`-march`, `/arch`, target-feature); existing runtime dispatch; portable fallback correctness; alignment and tail handling.

## 4. Metrics
Throughput and latency per path on the target workload; frequency behavior under heavy vector use (measured, not assumed); correctness diffs; code size.

## 5. Common bottlenecks and anti-patterns
Compiling the whole program with `-march=native` and shipping it (illegal-instruction crashes on other CPUs); checking CPUID but not OS state; no scalar fallback; assuming wider vectors are always faster; mixing incompatible AVX/SSE transitions; relying on emulator behavior.

## 6. Candidate optimization techniques
Function-level multiversioning or a dispatch table filled at startup; compile each variant with its own target feature; one tested portable fallback; runtime self-test comparing outputs on a small input; use library dispatch (language runtime or math library) instead of hand-written intrinsics where possible; prefer auto-vectorization-friendly layouts before intrinsics.

## 7. Runtime tunables versus build-time changes
Runtime: path selector `simd_path` with allowed values from detected support. Build-time: per-variant compile flags; a baseline build target that avoids newer instructions.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Choosing among SIMD paths depends on the CPU: RACE. Replacing an O(n^2) loop is universal.

## 9. Compatibility and version considerations
Compilers differ in intrinsic headers and target attributes (GCC/Clang `target` attribute, MSVC `/arch` and per-file flags). Features under emulation (e.g., x86 apps on ARM) may be absent or slow; treat as baseline unless measured.

## 10. Security, privacy, accessibility, data integrity
Vector paths must give identical results, or results within a declared and tested tolerance (floating-point reassociation changes results). Constant-time crypto code must not be replaced by data-dependent paths.

## 11. Validation and benchmark methodology
Cross-path equivalence tests over edge inputs (empty, odd lengths, unaligned, NaN/inf where relevant); forced-fallback test; benchmark all valid paths on the workload and on a cold-start run.

## 12. Rollback considerations
If a path faults or mismatches, mark it failed for this configuration and use the baseline path; keep the failure in diagnostics.

## 13. Authoritative sources and last-reviewed
Vendor architecture manuals for x86 and Arm and compiler documentation are the sources to consult per project; they were not fetched here, so specific feature-to-hardware claims are **unverified**. An attempted fetch of `https://developer.arm.com/Architectures/Neon` on 2026-11-07 returned only a redirect page, so no Arm claims are sourced. Last reviewed: 2026-11-07.
