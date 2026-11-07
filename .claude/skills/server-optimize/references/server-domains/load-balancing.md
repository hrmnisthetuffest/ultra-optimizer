<!-- format: 13-section -->
# Load balancing and routing

## 1. Purpose and applicability
Distribute traffic evenly and fail over quickly.

## 2. Detection signals
Uneven instance load, sticky-session hot spots, slow failover, health-check flapping.

## 3. What to inspect
Algorithm, health checks, connection draining, session affinity, timeouts, retries at the balancer, TLS termination.

## 4. Metrics
Per-instance request share, health-check results, failover time, 5xx at the balancer, connection reuse.

## 5. Common bottlenecks and anti-patterns
Round-robin with unequal requests, sticky sessions for stateless apps, retries amplifying overload, no draining.

## 6. Candidate optimization techniques
Least-outstanding-request where supported, drain connections, bound retries, externalize session state.

## 7. Runtime tunables versus build-time changes
Runtime: app-side health endpoints, timeouts. Balancer settings are infrastructure and need authorization.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: capacity per instance must be verified. /optimize lens: stateless handler design. /ping-optimize lens: balancer-to-origin latency and connection reuse.

## 9. Compatibility and version considerations
Features differ by balancer product.

## 10. Security, privacy and accessibility considerations
Do not modify balancer, firewall or WAF rules without explicit authorization. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Failover drill in staging, uneven-load test.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
