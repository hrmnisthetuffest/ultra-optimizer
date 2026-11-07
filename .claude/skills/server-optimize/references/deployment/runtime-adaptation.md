<!-- format: 13-section -->
# RACE runtime adaptation to verified server capabilities

## 1. Purpose and applicability
Let a RACE-using application adapt its OWN parameters (worker counts, concurrency, memory budgets, cache allocation, batch sizes, database pool sizes, scheduling slots) to verified server capabilities, within developer-approved bounds.

## 2. Detection signals
Fixed constants for workers or pools that ignore the actual container or instance limits; configuration copied between environments of different sizes.

## 3. What to inspect
Where each parameter is set, what limit it must respect, how capabilities are read (container limits, platform-provided environment variables, developer-supplied profile), and whether the value is verified or assumed.

## 4. Metrics
Parameter values chosen, bounds, capability provenance (verified or not), validation outcome, rollbacks triggered.

## 5. Common bottlenecks and anti-patterns
Trusting host totals inside a container, deriving from unverified numbers, unbounded growth, adapting by modifying OS or infrastructure settings, summing per-instance database pools above the database limit.

## 6. Candidate optimization techniques
Describe parameters in a policy (schemas/server-adaptation-policy.schema.json) with min, max, default, derived_from, fraction and safety margin. Use templates/server_adaptation_model.py as the executable contract: unverified capability gives the default; outputs are clamped to approved bounds; out-of-range overrides are rejected; failed validation restores the last known-good values; database pool totals respect the connection limit.

## 7. Runtime tunables versus build-time changes
Runtime: the policy's parameters. Build-time: where the application reads them.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: this is the primary home of the feature. /optimize lens: not used; universal changes do not depend on the host. /ping-optimize lens: network-aware limits (outbound concurrency) use measured conditions and have the same bounds and fallback.

## 9. Compatibility and version considerations
Capability sources vary: cgroup limits, platform variables, metadata services. Use only what the developer approved; a metadata call is a network action and needs documentation and control.

## 10. Security, privacy and accessibility considerations
Adaptation never changes OS, kernel, driver, firewall or infrastructure settings. No background monitoring agent is added without explicit developer authorization and documented user controls (disable, pause, restore last known-good). Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
tests/test_server_optimize.py exercises the model: unverified capability, clamping to bounds, rejected overrides, rollback on failed validation, and database pool totals.

## 12. Rollback and failure handling
Keep the last known-good parameter set; restore it automatically when validation fails; always provide a setting that disables adaptation. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
