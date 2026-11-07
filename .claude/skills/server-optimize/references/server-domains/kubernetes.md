<!-- format: 13-section -->
# Kubernetes

## 1. Purpose and applicability
Right-size requests, limits, probes and scaling for workloads on Kubernetes without changing cluster-level settings.

## 2. Detection signals
CPU throttling, OOMKilled pods, slow rollouts, pods not ready, flapping autoscaler.

## 3. What to inspect
Manifests/Helm charts: resource requests and limits, probes, HPA, PodDisruptionBudget, anti-affinity, rollout strategy, config and secret handling, service and ingress definitions.

## 4. Metrics
Throttling ratio, restarts, ready time, HPA behavior, rollout duration, error rate during rollout.

## 5. Common bottlenecks and anti-patterns
No requests/limits, limits far below usage, probes that kill healthy pods, aggressive HPA flapping, no graceful shutdown.

## 6. Candidate optimization techniques
Set requests from measured usage, tune probes, add PDB and preStop/graceful shutdown, tune HPA metrics and stabilization, keep manifests declarative.

## 7. Runtime tunables versus build-time changes
Runtime: replicas, requests/limits, HPA targets. Build-time: manifests.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: derive app worker counts from the pod's effective limits; verify node architecture and instance types before arch-specific builds. /optimize lens: manifest correctness and sane defaults. /ping-optimize lens: readiness, service and ingress path latency.

## 9. Compatibility and version considerations
API versions and features depend on cluster version; verify before use.

## 10. Security, privacy and accessibility considerations
Do not apply manifests to a cluster, change RBAC, network policy or node settings without explicit authorization; inspect with read-only credentials first. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Dry-run and server-side validation, staging rollout test, no downtime during rollout, rollback via previous revision.

## 12. Rollback and failure handling
Rollback via the previous Deployment revision or git revert, only inside the authorized environment. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
