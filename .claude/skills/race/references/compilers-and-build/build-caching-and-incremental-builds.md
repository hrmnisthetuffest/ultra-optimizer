<!-- format: 13-section -->
# Build caching and incremental builds

## 1. Purpose and applicability
Reduce build time without altering outputs.

## 2. Detection signals
Detect compilers/build tools from manifests (CMake, Cargo, Gradle, Maven, MSBuild, Xcode, Vite/Webpack/Rollup/esbuild, Bazel/Meson).

## 3. What to inspect
Inspect: CI config, cache keys, dependency graph

## 4. Metrics
Binary/bundle size, build time, startup time, throughput, debuggability.

## 5. Common bottlenecks and anti-patterns
cache poisoning; non-hermetic steps; rebuilding the world

## 6. Candidate optimization techniques
remote/local caches, precompiled headers where supported, split targets, parallelism sized to builder

## 7. Runtime tunables versus build-time changes
Build-time options; keep a baseline build profile.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Mostly /optimize (universal build config for declared targets). RACE uses build outputs only for per-capability variants (multiversioning). No-go: caching secrets or untrusted artifacts

## 9. Compatibility and version considerations
Compiler/toolchain versions differ in flags and defaults; pin and record them.

## 10. Security, privacy, accessibility, data integrity
Keep hardening flags (stack protectors, CFI, ASLR support, sanitizers in test); do not strip security features for speed.

## 11. Validation and benchmark methodology
Verify reproducible outputs (hash compare) and clean-build correctness.

## 12. Rollback considerations
Keep the previous build configuration in version control; revert the config commit.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
