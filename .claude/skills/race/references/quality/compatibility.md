<!-- format: 13-section -->
# Compatibility

## 1. Purpose and applicability
Keep platform, API, file-format and dependency compatibility.

## 2. Detection signals
Supported-platform matrix, API specs, dependency constraints.

## 3. What to inspect
Minimum versions, public APIs, protocols, plugin interfaces, build targets.

## 4. Metrics
Platforms tested, API diffs, deprecated usage.

## 5. Common bottlenecks and anti-patterns
Raising minimum versions; using newer APIs without fallback.

## 6. Candidate optimization techniques
Feature-detect, keep fallbacks, test each supported platform class available, document untested ones.

## 7. Runtime tunables versus build-time changes
None at runtime.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE paths always keep a baseline for unsupported hardware.

## 9. Compatibility and version considerations
Follow semantic versioning and the project's deprecation policy.

## 10. Security, privacy, accessibility, data integrity
Compatibility shims must not weaken security.

## 11. Validation and benchmark methodology
Test matrix; contract tests for APIs.

## 12. Rollback considerations
Revert compatibility-breaking changes.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
