<!-- format: 13-section -->
# Binary and package size

## 1. Purpose and applicability
Reduce shipped size when it matters.

## 2. Detection signals
Detect compilers/build tools from manifests (CMake, Cargo, Gradle, Maven, MSBuild, Xcode, Vite/Webpack/Rollup/esbuild, Bazel/Meson).

## 3. What to inspect
Inspect: bundle analyzers, symbol sizes, assets

## 4. Metrics
Binary/bundle size, build time, startup time, throughput, debuggability.

## 5. Common bottlenecks and anti-patterns
unused dependencies; duplicate assets; debug info in releases

## 6. Candidate optimization techniques
tree-shaking, code splitting, compression, dependency pruning, stripping symbols while keeping crash symbolication separately

## 7. Runtime tunables versus build-time changes
Build-time options; keep a baseline build profile.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Mostly /optimize (universal build config for declared targets). RACE uses build outputs only for per-capability variants (multiversioning). No-go: removing features or locales to hit a number

## 9. Compatibility and version considerations
Compiler/toolchain versions differ in flags and defaults; pin and record them.

## 10. Security, privacy, accessibility, data integrity
Keep hardening flags (stack protectors, CFI, ASLR support, sanitizers in test); do not strip security features for speed.

## 11. Validation and benchmark methodology
Compare size and startup; verify features still load.

## 12. Rollback considerations
Keep the previous build configuration in version control; revert the config commit.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
