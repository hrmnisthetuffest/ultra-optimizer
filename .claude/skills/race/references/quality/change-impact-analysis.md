<!-- format: 13-section -->
# Change-impact analysis

## 1. Purpose and applicability
Assess what a change can affect before and after making it.

## 2. Detection signals
Dependency graph, callers, tests, config, docs.

## 3. What to inspect
Callers of changed code, serialized formats, public APIs, feature flags, build outputs.

## 4. Metrics
Files touched, interfaces affected, tests covering them, risk category.

## 5. Common bottlenecks and anti-patterns
Missing indirect callers; ignoring generated code and build scripts.

## 6. Candidate optimization techniques
Search references, read tests, list affected contracts, record test gaps, rank risk (low/medium/high).

## 7. Runtime tunables versus build-time changes
None at runtime.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Applies to both skills.

## 9. Compatibility and version considerations
Check versioned APIs and persisted data.

## 10. Security, privacy, accessibility, data integrity
Flag any change touching security, privacy or data paths.

## 11. Validation and benchmark methodology
Re-run impact check after the change; compare predicted to actual.

## 12. Rollback considerations
Impact record guides which changes to revert first.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
