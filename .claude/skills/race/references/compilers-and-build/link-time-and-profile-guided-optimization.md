<!-- format: 13-section -->
# LTO and profile-guided optimization

## 1. Purpose and applicability
Use LTO/PGO when evidence supports it.

## 2. Detection signals
Detect compilers/build tools from manifests (CMake, Cargo, Gradle, Maven, MSBuild, Xcode, Vite/Webpack/Rollup/esbuild, Bazel/Meson).

## 3. What to inspect
Inspect: link times, representative profile workloads

## 4. Metrics
Binary/bundle size, build time, startup time, throughput, debuggability.

## 5. Common bottlenecks and anti-patterns
stale or unrepresentative profiles; large link-time cost

## 6. Candidate optimization techniques
trial thin/full LTO; PGO from representative workloads kept in version control

## 7. Runtime tunables versus build-time changes
Build-time options; keep a baseline build profile.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Mostly /optimize (universal build config for declared targets). RACE uses build outputs only for per-capability variants (multiversioning). No-go: shipping PGO built from private user data

## 9. Compatibility and version considerations
Compiler/toolchain versions differ in flags and defaults; pin and record them.

## 10. Security, privacy, accessibility, data integrity
Keep hardening flags (stack protectors, CFI, ASLR support, sanitizers in test); do not strip security features for speed.

## 11. Validation and benchmark methodology
Measure speed, size, build time; run the full test suite.

## 12. Rollback considerations
Keep the previous build configuration in version control; revert the config commit.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
