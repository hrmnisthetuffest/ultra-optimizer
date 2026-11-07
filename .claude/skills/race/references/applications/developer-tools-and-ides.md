<!-- format: 13-section -->
# Developer tools and IDEs

## 1. Purpose and applicability
Editors, language servers, build tools, debuggers.

## 2. Detection signals
Plugin APIs, language-server protocol use.

## 3. What to inspect
Indexing, file watching, extension host, syntax highlighting, memory growth on large repos.

## 4. Metrics
Startup, keystroke latency, indexing time, memory on large workspaces.

## 5. Common bottlenecks and anti-patterns
Eager full-repo indexing; unbounded watchers; main-thread analysis.

## 6. Candidate optimization techniques
Incremental indexing, throttled background work scheduled when idle (RACE), caches with bounds.

## 7. Runtime tunables versus build-time changes
Runtime: indexer concurrency, watcher limits. Build-time: extension loading.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: breaking extension APIs, dropping language features, changing user project files.

## 9. Compatibility and version considerations
Keep protocol and extension compatibility.

## 10. Security, privacy, accessibility, data integrity
Never read or transmit user code externally; do not alter workspace files while profiling.

## 11. Validation and benchmark methodology
Benchmarks on small/medium/large fixture repos.

## 12. Rollback considerations
Revert concurrency/limit settings.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
