<!-- format: 13-section -->
# Server intelligence integration (race)

## 1. Purpose and applicability
Use verified server hardware and runtime facts to choose application-level execution strategies. The shared Server & Backend Intelligence library ships with the skill named server-optimize. If that skill is installed, read its references/INDEX.md and load only the domain files relevant to the backend component found. If it is not installed, continue with this skill's own references and tell the developer that the shared library is unavailable; never invent server facts.

## 2. Detection signals
Backend code, server frameworks, worker/thread pool configuration, container or Kubernetes manifests, serverless handlers.

## 3. What to inspect
Effective CPU and memory limits as the runtime sees them (cgroup), architecture, worker counts, connection pool sizes, cache budgets, deployment profile facts and their source (detected, developer-provided, verified-live).

## 4. Metrics
Throughput, p95/p99 latency, CPU utilization, memory, queue latency, cold-start duration.

## 5. Common bottlenecks and anti-patterns
Using host totals inside containers, assuming instance specs from a plan name, hard-coding core counts, unbounded worker or pool growth.

## 6. Candidate optimization techniques
Derive worker counts, concurrency, memory budgets, cache allocation, batch sizes and DB pool sizes from verified capabilities, clamped to developer-approved bounds with a safe fallback when facts are unknown.

## 7. Runtime tunables versus build-time changes
Runtime: worker counts, pools, budgets, within approved ranges. Never change OS, BIOS, firmware, driver or infrastructure settings.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: this file. /optimize lens: handled by /optimize without hardware data. /ping-optimize lens: handled by /ping-optimize for network conditions.

## 9. Compatibility and version considerations
Facts must carry a source; unverified facts are treated as unknown and the default is used.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Compare against a baseline on representative load; test the fallback path with missing facts; test out-of-range overrides are rejected.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
