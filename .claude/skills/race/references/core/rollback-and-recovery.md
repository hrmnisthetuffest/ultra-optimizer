<!-- format: 13-section -->
# Rollback and recovery

## 1. Purpose and applicability
How runtime configuration and development-time edits are made reversible. Applies to every applied change.

## 2. Detection signals
Existing config persistence, crash handlers, feature-flag systems, migration framework, git state.

## 3. What to inspect
Where original defaults live; whether state writes are atomic; what happens on crash mid-apply; uncommitted user work in the repo.

## 4. Metrics
Time to restore last-known-good; rollback success rate in tests; number of auto-rollbacks (an indicator of unsafe candidates).

## 5. Common bottlenecks and anti-patterns
Overwriting defaults; non-atomic profile writes (corrupt on crash); no validation after apply; rolling back by hard reset; discarding user changes; silent rollback with no explanation.

## 6. Candidate optimization techniques
**Runtime**: store original defaults and a last-known-good (LKG) profile; apply in a staged, transactional way (write candidate, validate, switch, confirm, then promote to LKG); write state atomically (temp file then rename); auto-roll back on correctness failure, error-rate increase beyond a threshold, material regression, or instability; keep a local, auditable, user-clearable history that explains each change.
**Development time**: work from a git checkpoint or a clean diff; keep changes in small commits; revert only changes this skill made, and only when safe; if user edits may overlap, ask. Never run reset-hard or clean on user work and never force-push.

## 7. Runtime tunables versus build-time changes
Runtime changes roll back by restoring values; code changes roll back by reverting commits or flags. Prefer shipping risky changes behind a feature flag.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
LKG profiles are keyed by a coarse capability class; a hardware or driver change invalidates the match and returns to defaults until re-evaluated.

## 9. Compatibility and version considerations
Profiles carry `schema_version` and `app_version`; ignore profiles from incompatible versions rather than migrating blindly.

## 10. Security, privacy, accessibility, data integrity
Never roll back data the user created. Rollback must not leave partially migrated persisted data; data migrations need their own approval and plan.

## 11. Validation and benchmark methodology
Tests: kill the process mid-apply and confirm the next launch has a valid profile; inject a failing validation and confirm rollback; inject a regression and confirm rollback; confirm LKG restore equals prior values exactly.

## 12. Rollback considerations
This whole file is about rollback; the key invariant is: **at any moment, a valid known-good configuration exists and can be restored without the network**.

## 13. Authoritative sources and last-reviewed
Project spec sections 5.9 and 11.2. Last reviewed: 2026-11-07.
