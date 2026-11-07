<!-- format: 13-section -->
# Functionality preservation

## 1. Purpose and applicability
Enforce the standard: zero known functional regressions, preserved documented and observed behavior, relevant tests run, edge cases tested, performance measured, untested areas disclosed, failed or unsafe changes rolled back. Never claim proven 100% equivalence.

## 2. Detection signals
Existing tests, documented behavior, feature list, user flows, API schemas, changelog.

## 3. What to inspect
Feature inventory, public interfaces, file formats, permissions, integrations, accessibility and localization behavior, offline and sync behavior.

## 4. Metrics
Pass rate before/after, behavioral diff count, coverage of touched code, number of disclosed gaps.

## 5. Common bottlenecks and anti-patterns
Removing or stubbing features to look faster; changing defaults silently; skipping slow tests.

## 6. Candidate optimization techniques
Capture a baseline first; write characterization tests for untested behavior before changing it; compare outputs; manual checklist for UI flows.

## 7. Runtime tunables versus build-time changes
None at runtime; this is a process gate.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Not applicable; applies to both RACE and /optimize.

## 9. Compatibility and version considerations
Respect documented compatibility promises and deprecation policy.

## 10. Security, privacy, accessibility, data integrity
Security, privacy and accessibility behavior are part of functionality.

## 11. Validation and benchmark methodology
Run full suite before and after; list tests added; list what was not testable and why.

## 12. Rollback considerations
Revert the single change that broke behavior; do not discard unrelated user work.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
