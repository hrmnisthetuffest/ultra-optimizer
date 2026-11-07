<!-- format: 13-section -->
# Backup, recovery and failover

## 1. Purpose and applicability
Preserve recoverability while optimizing.

## 2. Detection signals
Backup jobs, snapshots, replication, failover configs, restore procedures.

## 3. What to inspect
Backup schedule and verification, RPO/RTO claims, restore tests, failover automation, impact of optimization on backup windows.

## 4. Metrics
Backup success, restore time, replication lag.

## 5. Common bottlenecks and anti-patterns
Untested restores, optimizations that disable backups, state outside backup scope.

## 6. Candidate optimization techniques
Keep backups verifiable, schedule heavy jobs away from peak, document restore steps.

## 7. Runtime tunables versus build-time changes
Runtime: schedules. Backup configuration is infrastructure and needs authorization.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: none. /optimize lens: none. /ping-optimize lens: replication bandwidth and lag awareness.

## 9. Compatibility and version considerations
Provider features differ.

## 10. Security, privacy and accessibility considerations
Do not modify backup, retention or failover configuration without explicit authorization. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Restore drill in a non-production environment.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
