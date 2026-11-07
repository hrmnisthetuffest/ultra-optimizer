<!-- format: 13-section -->
# Access levels and authorization

## 1. Purpose and applicability
Define the six progressive access levels and the explicit authorization each requires, so nothing live happens without consent.

## 2. Detection signals
Any step that would contact a live system, run a profiler remotely, modify staging or production, or use credentials.

## 3. What to inspect
Level 0 repo-only (default). Level 1 read-only infrastructure inspection. Level 2 read-only runtime metrics. Level 3 staging profiling. Level 4 explicitly authorized staging modifications. Level 5 explicitly authorized production modifications. The profile's access.level and access.authorized_environments record what the developer granted.

## 4. Metrics
Actions taken per level, authorizations requested, authorizations denied, actions refused for lack of authorization.

## 5. Common bottlenecks and anti-patterns
Escalating silently, treating general approval as approval for a specific environment, reusing staging approval for production, using broad credentials when read-only ones exist, printing credentials.

## 6. Candidate optimization techniques
Each step names the level it needs. If the profile's level is lower, stop and ask once for that specific authorization, naming the environment and the exact action. Use the developer's existing secret mechanism with read-only identities where possible. Without authorization never restart production services, change production infrastructure, run database migrations, scale infrastructure, change firewall rules, or deploy code.

## 7. Runtime tunables versus build-time changes
Runtime: none. Authorization is recorded in the profile and is per environment and per action class.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: live capability verification is read-only (level 1 or 2). /optimize lens: repository-only unless the developer asks otherwise. /ping-optimize lens: active probes require the endpoint to be listed with authorized_for_active_testing true.

## 9. Compatibility and version considerations
Provider CLIs and APIs differ; always prefer the developer's existing, already configured read-only tooling.

## 10. Security, privacy and accessibility considerations
Never print, log, store or transmit secrets. Redact tokens in command output before showing it. Do not create new credentials, roles or API keys. Treat any credential seen accidentally as compromised-by-exposure and tell the developer without repeating it. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Test that no workflow step runs above the granted level, that production-modify requires production in authorized_environments, and that refusal messages name the missing authorization.

## 12. Rollback and failure handling
Live changes are made only at levels 4 or 5, each with a recorded rollback point; if validation fails, restore the previous state within the same authorization, otherwise report and stop. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
