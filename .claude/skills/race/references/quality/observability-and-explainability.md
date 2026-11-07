<!-- format: 13-section -->
# Observability and explainability

## 1. Purpose and applicability
Make optimization decisions visible and auditable without leaking private data.

## 2. Detection signals
Existing logging/metrics, diagnostics UI.

## 3. What to inspect
What decisions are recorded, where, retention, user visibility.

## 4. Metrics
History completeness, log volume, overhead.

## 5. Common bottlenecks and anti-patterns
Silent adaptation; logging content or identifiers; unbounded logs.

## 6. Candidate optimization techniques
Local diagnostics with reason codes, versioned records, user-visible summary on request, clear/export controls.

## 7. Runtime tunables versus build-time changes
Runtime: diagnostics level, retention. Build-time: log structure.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE records hardware class and chosen path; /optimize records changes and measurements.

## 9. Compatibility and version considerations
Record schema versions.

## 10. Security, privacy, accessibility, data integrity
No content, credentials, serials or account data; local by default; telemetry only with consent.

## 11. Validation and benchmark methodology
Check records validate against schemas and contain no private fields.

## 12. Rollback considerations
User can clear history; clearing does not alter active settings.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
