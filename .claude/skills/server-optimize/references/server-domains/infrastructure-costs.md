<!-- format: 13-section -->
# Infrastructure costs

## 1. Purpose and applicability
Reduce cost per unit of work where measurable, never by reducing correctness or safety.

## 2. Detection signals
Over-provisioned instances, idle capacity, expensive queries, egress heavy traffic, serverless cost spikes.

## 3. What to inspect
Instance/plan sizes, utilization, storage classes, egress, request counts, cache hit rate, billing exports when the developer provides them.

## 4. Metrics
Cost per request, utilization, egress bytes, idle share.

## 5. Common bottlenecks and anti-patterns
Optimizing latency with unbounded spend, ignoring egress, oversized instances.

## 6. Candidate optimization techniques
Right-size from measured utilization, cache to cut origin and egress, compress, batch, schedule non-urgent work.

## 7. Runtime tunables versus build-time changes
Infrastructure sizing is a recommendation unless authorized.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: sizing recommendations come from verified specs. /optimize lens: reduce wasted work. /ping-optimize lens: reduce bytes transferred.

## 9. Compatibility and version considerations
Prices change; consult current provider pricing and record the date.

## 10. Security, privacy and accessibility considerations
Respect the developer's stated spending limit. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Before/after cost estimates labeled as estimates unless billing data shows otherwise.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
