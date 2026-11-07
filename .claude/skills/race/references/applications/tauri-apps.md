<!-- format: 13-section -->
# Tauri applications

## 1. Purpose and applicability
Rust core plus system webview; small footprint, different webviews per OS.

## 2. Detection signals
`tauri` in Cargo.toml / tauri.conf.json.

## 3. What to inspect
Command handlers, IPC payloads, webview-specific behavior, Rust async runtime, plugin usage.

## 4. Metrics
Startup, binary size, IPC latency, webview memory, Rust CPU time.

## 5. Common bottlenecks and anti-patterns
Large JSON over IPC; blocking commands; assuming one webview engine; heavy synchronous Rust in handlers.

## 6. Candidate optimization techniques
Async commands, stream large data, move compute to Rust threads sized by capability (RACE), trim bundle, LTO/size profile choices measured.

## 7. Runtime tunables versus build-time changes
Runtime: thread pool size, chunk size. Build-time: release profile, features.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: widening allowlist/capabilities, disabling CSP, bypassing permission scopes.

## 9. Compatibility and version considerations
Webview engines differ by OS and version; test each target.

## 10. Security, privacy, accessibility, data integrity
Keep capability scopes and CSP; do not expand filesystem or shell access.

## 11. Validation and benchmark methodology
Cargo bench/criterion for Rust, browser profiler for the front end.

## 12. Rollback considerations
Revert release-profile changes via config; keep command behavior flags.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
