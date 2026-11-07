<!-- format: 13-section -->
# Desktop applications (general)

## 1. Purpose and applicability
Baseline guidance for native and cross-platform desktop apps.

## 2. Detection signals
Manifests (CMake, Cargo, .csproj, Package.swift, pyproject), entry points, UI framework imports.

## 3. What to inspect
Startup path, UI thread work, background workers, caches, file I/O, GPU use, memory growth, update and installer behavior.

## 4. Metrics
Cold/warm startup, time-to-interactive, input latency, frame time, memory, CPU idle usage, battery impact where measurable.

## 5. Common bottlenecks and anti-patterns
Heavy work on UI thread; eager loading; polling timers; unbounded caches; redundant redraws.

## 6. Candidate optimization techniques
Defer non-critical init; async I/O; coalesce redraws; bounded caches; adapt worker counts and cache budgets to detected capability (RACE).

## 7. Runtime tunables versus build-time changes
Runtime: worker pool size, cache caps, render scale. Build-time: lazy loading, packaging.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: disabling features, lowering required visual quality, changing OS or driver settings.

## 9. Compatibility and version considerations
Support the declared OS list; keep file formats and plugin APIs.

## 10. Security, privacy, accessibility, data integrity
Preserve auth, permissions and accessibility trees; no telemetry added.

## 11. Validation and benchmark methodology
Measure startup and key flows before/after; run accessibility checks; test on supported OS classes available.

## 12. Rollback considerations
Flag-guard changes; keep last-known-good profile.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
