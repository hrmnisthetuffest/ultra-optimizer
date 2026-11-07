<!-- format: 13-section -->
# Server security during optimization

## 1. Purpose and applicability
Make sure performance work never weakens security.

## 2. Detection signals
Changes touching auth, TLS, caching, headers, input parsing, secrets, permissions.

## 3. What to inspect
Authn/authz order, TLS settings, cache keys and Vary, CORS, rate limits, input validation, dependency versions, secret handling, logging of sensitive data.

## 4. Metrics
Security test pass rate, scan findings, auth bypass attempts blocked.

## 5. Common bottlenecks and anti-patterns
Skipping auth for speed, disabling verification, wide CORS, caching private data, logging bodies or tokens.

## 6. Candidate optimization techniques
Keep checks, move cost rather than removing it, cache authorization safely, constant-time comparisons where needed.

## 7. Runtime tunables versus build-time changes
Runtime: rate limits, timeouts.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: none; security is universal. /optimize lens: none; security is universal. /ping-optimize lens: TLS verification and strength are never traded for speed.

## 9. Compatibility and version considerations
TLS security posture must not drop.

## 10. Security, privacy and accessibility considerations
Any change that would weaken security is rejected regardless of speedup. Report suspected vulnerabilities privately to the developer. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Auth/authz regression suite; header and cache tests; secret-scan on diffs.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
