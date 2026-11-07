<!-- format: 13-section -->
# Reporting

## 1. Purpose and applicability
Final report format for /optimize runs, honest about evidence and gaps.

## 2. Detection signals
Collect changes, files touched, tests run, measurements, risks.

## 3. What to inspect
For each change: problem, evidence, files, approach, alternatives, expected benefit, measured result, test evidence, confidence, tradeoffs, rollback method.

## 4. Metrics
Before/after numbers with workload and environment.

## 5. Common bottlenecks and anti-patterns
Overclaiming; omitting untested areas.

## 6. Candidate optimization techniques
List remaining opportunities and untested areas explicitly.

## 7. Runtime tunables versus build-time changes
Not applicable.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Universal only; state declared targets.

## 9. Compatibility and version considerations
Note platforms not tested.

## 10. Security, privacy, accessibility, data integrity
Do not include secrets or user data in reports.

## 11. Validation and benchmark methodology
Reports reference commands that reproduce measurements.

## 12. Rollback considerations
Include revert instructions per change.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
