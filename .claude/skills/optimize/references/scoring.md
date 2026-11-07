<!-- format: 13-section -->
# Scoring candidates

## 1. Purpose and applicability
Rank candidate changes transparently without fabricated precision.

## 2. Detection signals
Score each candidate on expected benefit (with basis), evidence confidence, scope, effort, regression risk, security/privacy risk, compatibility impact, reversibility, dependency/maintenance cost.

## 3. What to inspect
Use categories (low/medium/high) or ranges, not invented decimals.

## 4. Metrics
Rated categories plus one-line rationale.

## 5. Common bottlenecks and anti-patterns
False precision; ignoring maintenance cost.

## 6. Candidate optimization techniques
Prefer high benefit, high confidence, small scope, high reversibility. Defer high-risk, low-evidence work.

## 7. Runtime tunables versus build-time changes
Not applicable.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Universal only.

## 9. Compatibility and version considerations
Compatibility impact weighs heavily.

## 10. Security, privacy, accessibility, data integrity
Any security/privacy risk of high blocks the change without approval.

## 11. Validation and benchmark methodology
Re-score after measurement.

## 12. Rollback considerations
Low-reversibility items require explicit approval.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
