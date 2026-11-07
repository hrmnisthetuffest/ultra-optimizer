<!-- format: 13-section -->
# Regression testing strategy

## 1. Purpose and applicability
Choose and run tests that catch regressions introduced by optimization changes.

## 2. Detection signals
Test frameworks in manifests, CI config, existing fixtures.

## 3. What to inspect
Test commands, flaky tests, coverage gaps near changed code, golden-output tests.

## 4. Metrics
Pass/fail, flake rate, coverage delta, time to run.

## 5. Common bottlenecks and anti-patterns
Treating flaky tests as noise; only running unit tests for cross-component changes.

## 6. Candidate optimization techniques
Baseline run; targeted tests per change; characterization tests; property tests for equivalence of old/new paths; differential testing between baseline and optimized paths.

## 7. Runtime tunables versus build-time changes
None at runtime.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Applies to both skills.

## 9. Compatibility and version considerations
Match the project's test tooling; add no heavy new test dependency without approval.

## 10. Security, privacy, accessibility, data integrity
Test data must not contain real user data.

## 11. Validation and benchmark methodology
Record commands and results in the history record.

## 12. Rollback considerations
Keep tests added unless they are wrong; remove only with reasoning.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
