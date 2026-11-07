<!-- format: 13-section -->
# Tuning registry

## 1. Purpose and applicability
The registry is the allowlist of parameters RACE may change. If a value is not registered, it cannot be changed. Applies to every runtime adaptation and every integration.

## 2. Detection signals
Candidates are found in source: thread/pool sizes, cache and buffer capacities, batch sizes, chunk sizes, backend or path selectors, prefetch depth, render scale, decode concurrency, queue limits. Discover them from the real code; do not paste a generic list.

## 3. What to inspect
For each candidate: where it is read, whether it can change at run time, what depends on it, what output properties must not change (determinism, quality, ordering), and what the safe default is.

## 4. Metrics
Per tunable: effect on the target metric, effect on resource use, effect on correctness tests, validation pass/fail rate.

## 5. Common bottlenecks and anti-patterns
Registering a global or system setting; ranges wider than tested; no fallback; coupling two tunables without declaring dependency; a "path select" that has no tested fallback; mutating live state without a transaction.

## 6. Candidate optimization techniques
Entry fields (see `schemas/tunable-parameter.schema.json`): stable `id`; `purpose`; `type` plus `range` or `values`; `default` and `fallback`; `adjustability` (runtime/restart/rebuild); `workload_categories`; `requirements`; `dependencies`; `mutually_exclusive_with`; `quality_constraints`; `validation`; `apply`; `rollback`; `risk`; `requires_user_confirmation`.
Rules: reject out-of-range values, unsupported platforms/capabilities, invalid combinations, and anything whose validation fails. Reject arbitrary variable names, memory addresses, and code patches.

## 7. Runtime tunables versus build-time changes
`adjustability: runtime` may change while the app runs (at a safe point); `restart` applies next launch; `rebuild` is a developer-time change and never auto-applied. See `templates/race_reference_model.py` for an executable contract of registry behavior.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Hardware-dependent: values derived from detected cores/memory/GPU. Universal: constants that are better for everyone are code changes, not tunables.

## 9. Compatibility and version considerations
Version the registry (`schema_version`). When a tunable is removed or its range changes in an app update, stored profiles that reference it must be discarded or migrated, never applied blindly.

## 10. Security, privacy, accessibility, data integrity
No tunable may weaken auth, crypto, permissions, accessibility or data integrity. High-risk tunables need `requires_user_confirmation: true`. Registry and profile files are local; do not transmit them.

## 11. Validation and benchmark methodology
Each tunable has a named validation (test or function) that runs after apply. Test the boundary values, an out-of-range value (must be rejected), and apply-then-rollback restoring the prior value exactly.

## 12. Rollback considerations
Every entry defines how the previous value is restored. The engine keeps the original default and the last-known-good value per tunable.

## 13. Authoritative sources and last-reviewed
Project spec section 4.4. Last reviewed: 2026-11-07.
