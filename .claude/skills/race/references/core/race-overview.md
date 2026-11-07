<!-- format: 13-section -->
# RACE overview

## 1. Purpose and applicability
RACE (Runtime Adaptive Configuration Engine) lets an application adapt its **own** internal behavior to the hardware and workload it actually meets. It has two halves:
- **Developer Intelligence**: Claude, at development time, inspects the project, designs the integration, and edits source (adds a tunable, a CPU-dispatch path, a GPU backend choice, a benchmark hook).
- **Runtime Engine**: code that ships inside the target app and, at run time, detects capabilities, observes the workload, and selects among prevalidated paths and registered parameters.

RACE is not an OS tuning utility. It never changes the device, OS, firmware, drivers or other applications. Use it when the user wants hardware-aware, workload-aware application optimization. For hardware-independent cleanup, the separate `/optimize` command applies instead.

## 2. Detection signals
Ask RACE when the request mentions: adapting to CPU/GPU/RAM, picking thread counts or cache sizes per machine, choosing SIMD or GPU backends, calibration, "benchmark and optimize", or last-known-good performance profiles. A request that only asks to speed up code without reference to machine variation is `/optimize`, not RACE.

## 3. What to inspect
Repository state (uncommitted work, branch), build and test commands, contribution rules, stack (see `project-detection.md`), existing configuration surfaces, existing telemetry, existing AI pipeline (if any), whether a loading screen exists, platforms supported.

## 4. Metrics
Per integration: startup time and time-to-interactive, operation p50/p95/p99, throughput, frame times, peak memory/VRAM, error rate, CPU time, and the overhead RACE itself adds (must be reported and bounded).

## 5. Common bottlenecks and anti-patterns
- Treating RACE as a generic refactoring skill with an optional hardware part.
- Reading device specs and assuming performance ("this GPU is newer, therefore faster").
- Changing system settings to "help" the app. Forbidden.
- Benchmarks that run during loading screens or the first 30 minutes of cumulative use.
- Over-abstracting the twelve components when a small app needs three.

## 6. Candidate optimization techniques
Select among prevalidated code paths; resize bounded caches and pools; choose a rendering or compute backend the app already contains; adjust batch sizes within quality limits; defer non-critical initialization; schedule optional work when idle.

## 7. Runtime tunables versus build-time changes
Runtime: registered parameters only (see `tuning-registry.md`). Build-time/code: new dispatch paths, native-arch builds with portable fallback, new tunables. Runtime adaptation never rewrites source, patches code, or downloads and executes generated code.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Hardware-dependent (this skill): thread/cache/memory budgets from detected cores and memory; SIMD, CUDA/Metal/DirectML/Vulkan path selection; GPU vs CPU placement. Universal changes (algorithms, queries, bundle size, build config for declared targets) belong to the separate `/optimize` command; do not perform or invoke it implicitly.

## 9. Compatibility and version considerations
Every adaptive path needs a correct portable fallback. If detection fails, use the safe baseline. Record framework and runtime versions a path requires in the tunable's `requirements`.

## 10. Security, privacy, accessibility, data integrity
Local-only by default; no telemetry unless explicitly consented; never collect serials, accounts, content, passwords or tokens. Optimization must not weaken crypto, auth, accessibility, localization or data integrity (see `privacy-and-consent.md`).

## 11. Validation and benchmark methodology
Baseline first, then change, then compare with warm-up and repeats (`benchmarking-methodology.md`). Run the project's tests. Disclose untested areas. Never claim a benefit without measurement.

## 12. Rollback considerations
Keep original defaults and a last-known-good profile; apply transactionally; auto-roll back on correctness failure or regression (`rollback-and-recovery.md`). For code edits, use git checkpoints; never reset or discard user work.

## 13. Authoritative sources and last-reviewed
Project build specification (`ULTRA_OPTIMIZER_CLAUDE_CODE_BUILD_SPEC.md`, v1.0, 7 Nov 2026) is the source for this file. Last reviewed: 2026-11-07. No external sources were fetched for this overview.
