<!-- format: 13-section -->
# Spring and ASP.NET Core

## 1. Purpose and applicability
JVM and .NET web stacks.

## 2. Detection signals
Detect via: pom/gradle files, .csproj, Program.cs

## 3. What to inspect
Inspect: bean/service startup, DB access, thread pools, serialization, caching

## 4. Metrics
Framework-level timings (render/commit, request, startup), memory, bundle or binary size, tail latency.

## 5. Common bottlenecks and anti-patterns
startup cost; blocking in reactive/async paths; N+1; oversized thread pools.

## 6. Candidate optimization techniques
connection and thread pool sizing, caching, lazy init, AOT/native options as measured.

## 7. Runtime tunables versus build-time changes
Runtime: pool sizes, cache caps, concurrency set through the framework's own configuration. Build-time: bundler/compiler options.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: capability-driven concurrency and budgets. /optimize: framework-idiomatic code, query and build fixes. No-go: bypassing security filters, changing transaction semantics.

## 9. Compatibility and version considerations
Check the pinned framework version's release notes; major versions change defaults.

## 10. Security, privacy, accessibility, data integrity
Keep auth, CSRF/CORS, sanitization and accessibility behavior unchanged.

## 11. Validation and benchmark methodology
JFR/dotnet-trace, load tests, integration tests.

## 12. Rollback considerations
Per-change commits; revert independently.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
