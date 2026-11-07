<!-- format: 13-section -->
# Electron applications

## 1. Purpose and applicability
Chromium plus Node apps: large memory and startup costs, multi-process.

## 2. Detection signals
`electron` dependency, main/renderer/preload files.

## 3. What to inspect
Main-process work, IPC volume, renderer bundle size, preload, window creation, native modules, background throttling.

## 4. Metrics
Startup to first paint, renderer memory, IPC latency, main-thread blocking, bundle size.

## 5. Common bottlenecks and anti-patterns
Blocking main process; chatty IPC; loading everything at start; many hidden windows; large unoptimized bundles.

## 6. Candidate optimization techniques
Lazy-load modules and windows, batch IPC, move CPU work to workers/utility processes, code-split renderer, cache with bounds; choose worker count and cache sizes from capability (RACE).

## 7. Runtime tunables versus build-time changes
Runtime: worker count, cache caps, GPU-process flags the app itself sets via supported APIs. Build-time: bundling, V8 snapshot where supported.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: disabling context isolation or sandbox for speed, enabling nodeIntegration in renderers, changing system browser settings.

## 9. Compatibility and version considerations
Electron major versions change defaults; check release notes for the pinned version.

## 10. Security, privacy, accessibility, data integrity
Keep sandbox, CSP, contextIsolation and IPC validation; accessibility tree must remain.

## 11. Validation and benchmark methodology
Use Chromium tracing/DevTools profiling; measure per-process memory; test packaged build.

## 12. Rollback considerations
Revert flags; keep previous windows/IPC contract behind a toggle.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
