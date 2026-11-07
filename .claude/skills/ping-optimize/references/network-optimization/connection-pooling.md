<!-- format: 13-section -->
# Connection pooling and reuse

## 1. Purpose and applicability
Reuse connections to avoid repeated DNS, TCP and TLS cost.

## 2. Detection signals
Handshake share high; many sockets; first-after-idle failures.

## 3. What to inspect
Client instances, pool limits per host and total, idle and lifetime timeouts, DNS refresh, proxy settings.

## 4. Metrics
Reuse rate, pool wait time, connection opens per minute, stale errors.

## 5. Common bottlenecks and anti-patterns
Per-request clients; unbounded pools; leaking connections on error paths; pool starvation from long requests.

## 6. Candidate optimization techniques
Share clients; size pools from observed concurrency; release connections on all paths; separate pools for long-lived streaming and short calls.

## 7. Runtime tunables versus build-time changes
Runtime: pool size, idle timeout, lifetime. Build-time: client lifecycle ownership.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Pool sizing from measured concurrency is adaptive and bounded; sharing clients is universal.

## 9. Compatibility and version considerations
Library defaults vary; verify with docs of the exact library and version.

## 10. Security, privacy and accessibility considerations
Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Test leak-free release on timeouts, cancellation and exceptions; test stale-connection recovery.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
