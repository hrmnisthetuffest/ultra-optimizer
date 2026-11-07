<!-- format: 13-section -->
# Adaptive selection and dispatch

## 1. Purpose and applicability
How the Runtime Engine chooses among prebuilt paths and registered parameters, and how Claude builds those paths at development time.

## 2. Detection signals
Code that has multiple implementations (scalar/SIMD, CPU/GPU, different backends), compile-time feature flags, platform conditionals.

## 3. What to inspect
Which implementations exist and are tested; the capability each requires; the portable fallback; resource-loss behavior for GPU devices; the build flags needed per path.

## 4. Metrics
Per-path correctness (identical or within declared tolerance), speed on the target workload, memory, startup cost of initializing the path.

## 5. Common bottlenecks and anti-patterns
Inferring support from brand strings; trusting CPUID without checking OS-enabled state; selecting a path without a tested fallback; vendor pairing assumptions treated as facts; downloading generated code at runtime; "faster but different output" without a declared tolerance.

## 6. Candidate optimization techniques
Decision procedure: (1) read capabilities via supported APIs; (2) filter paths by hard requirements (ISA supported **and** OS-enabled; GPU API, device, driver versions); (3) among valid paths, choose by evidence: a stored local benchmark result, else a conservative default; (4) validate the chosen path (self-test, output comparison); (5) on any failure, fall back to the baseline and record why. Vendor/CPU/GPU pairing effects are hypotheses to test, never automatic score bonuses.
Developer-time: add a dispatch table, native-arch build with portable fallback, new backend module, new tunable; each with build, tests and fallback verified.

## 7. Runtime tunables versus build-time changes
Runtime: choose among compiled-in paths. Build-time: compile each path (per-function target attributes or separate objects) so the binary still runs on baseline CPUs.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
All of this file is hardware-dependent and belongs to RACE. A change that is better on every machine (a faster algorithm) is not dispatch; it is a universal change.

## 9. Compatibility and version considerations
See `references/hardware/instruction-sets-and-dispatch.md` for ISA specifics. Handle device loss/reset for GPU paths. Emulated or translated execution (e.g., x86 on ARM) must be detected and treated conservatively.

## 10. Security, privacy, accessibility, data integrity
Do not execute code fetched at runtime. Do not let a faster path change numerical results beyond declared tolerance, or change file/network formats.

## 11. Validation and benchmark methodology
For each path: unit tests against the baseline, cross-path equivalence tests, a forced-fallback test, and a benchmark on the target workload (`benchmarking-methodology.md`).

## 12. Rollback considerations
Persist the last-known-good path; on crash or mismatch in a path, mark it failed for this configuration and use the baseline until a capability change.

## 13. Authoritative sources and last-reviewed
Project spec sections 4.5, 4.7, 4.8. Vendor documentation is cited in the hardware references. Last reviewed: 2026-11-07.
