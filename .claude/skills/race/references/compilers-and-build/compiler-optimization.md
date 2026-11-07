<!-- format: 13-section -->
# Compiler optimization levels

## 1. Purpose and applicability
Choose optimization levels and flags with evidence.

## 2. Detection signals
Detect compilers/build tools from manifests (CMake, Cargo, Gradle, Maven, MSBuild, Xcode, Vite/Webpack/Rollup/esbuild, Bazel/Meson).

## 3. What to inspect
Inspect: current flags, per-target flags, debug vs release

## 4. Metrics
Binary/bundle size, build time, startup time, throughput, debuggability.

## 5. Common bottlenecks and anti-patterns
blindly using the most aggressive level; -march=native on shipped binaries; UB exposed by optimization

## 6. Candidate optimization techniques
measure -O2/-O3/-Os alternatives, inspect vectorization reports, test under sanitizers

## 7. Runtime tunables versus build-time changes
Build-time options; keep a baseline build profile.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Mostly /optimize (universal build config for declared targets). RACE uses build outputs only for per-capability variants (multiversioning). No-go: enabling fast-math without numerical review

## 9. Compatibility and version considerations
Compiler/toolchain versions differ in flags and defaults; pin and record them.

## 10. Security, privacy, accessibility, data integrity
Keep hardening flags (stack protectors, CFI, ASLR support, sanitizers in test); do not strip security features for speed.

## 11. Validation and benchmark methodology
Differential tests and benchmarks per flag set.

## 12. Rollback considerations
Keep the previous build configuration in version control; revert the config commit.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
