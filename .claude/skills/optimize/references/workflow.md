<!-- format: 13-section -->
# Optimization workflow

## 1. Purpose and applicability
Step-by-step method for /optimize runs: audit, prioritize, implement, verify, report.

## 2. Detection signals
Start by reading project instructions and the declared environment; inspect repo state and uncommitted work.

## 3. What to inspect
Inspect build and test commands, hot paths, queries, dependency graph, bundle/package size and startup path.

## 4. Metrics
Baseline test status, timings, sizes and any available diagnostics.

## 5. Common bottlenecks and anti-patterns
Optimizing without baseline; touching unrelated files; mixing refactors with optimizations; large unreviewable commits.

## 6. Candidate optimization techniques
Audit -> filter (eligibility) -> score -> implement small bounded changes -> targeted tests -> broader regression -> compare performance -> report. Ask before rewrites, feature removals, data migrations, significant new dependencies and irreversible actions.

## 7. Runtime tunables versus build-time changes
Modes: audit (no edits), apply (edit and verify), review (assess an existing diff), report (summarize recorded work).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Universal changes only.

## 9. Compatibility and version considerations
Respect the project's tooling and style; avoid new tooling without approval.

## 10. Security, privacy, accessibility, data integrity
No destructive git operations; no push, publish, deploy or PR without explicit authorization.

## 11. Validation and benchmark methodology
Run baseline checklist before and regression checklist after every change group.

## 12. Rollback considerations
Use version-control diffs/checkpoints; revert only your own changes.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
