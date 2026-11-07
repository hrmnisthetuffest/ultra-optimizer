<!-- format: 13-section -->
# Platform and runtime intelligence

## 1. Purpose and applicability
Capture OS, process architecture and runtime context that change which paths are valid. Applies to every capability-detection step.

## 2. Detection signals
OS name/version, kernel, process architecture (and whether the process is native, emulated or translated), container/VM indicators, compiler and language-runtime versions, available graphics/compute APIs, sandbox constraints (browser, mobile, app store), driver/API versions as reported to the app.

## 3. What to inspect
Supported-platform matrix in manifests, CI targets, feature checks already in code, runtime flags, packaging format (installer, app store, portable).

## 4. Metrics
Startup and steady-state differences per platform; fallback hit rate; error rates by platform class.

## 5. Common bottlenecks and anti-patterns
Treating all OS versions alike; ignoring that browsers hide hardware detail; assuming desktop APIs on mobile; running x86 binaries under translation without noticing; using unsupported or undocumented APIs for detection.

## 6. Candidate optimization techniques
Feature-detect rather than version-detect; maintain a baseline path per platform; prefer official capability queries; treat virtualized or emulated environments conservatively.

## 7. Runtime tunables versus build-time changes
Runtime: platform-class keyed profile selection. Build-time: per-platform build targets and conditional compilation.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Which paths a platform can run is RACE. A declared minimum-supported-platform list is respected by `/optimize`, which never detects live hardware.

## 9. Compatibility and version considerations
Never raise minimum OS/runtime versions without approval. Record versions in every benchmark.

## 10. Security, privacy, accessibility, data integrity
Do not elevate privileges to read more detail; use only permissions the app already has. Respect sandboxes that forbid some probes.

## 11. Validation and benchmark methodology
Run tests on each available supported platform class; report platforms not tested explicitly.

## 12. Rollback considerations
A profile recorded on one platform class is never applied on another; mismatch means defaults.

## 13. Authoritative sources and last-reviewed
Platform vendor documentation per project (not fetched; **unverified**). Last reviewed: 2026-11-07.
