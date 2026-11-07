<!-- format: 13-section -->
# Connection lifecycle and reuse

## 1. Purpose and applicability
Most avoidable latency comes from opening connections too often or using stale ones.

## 2. Detection signals
High DNS+TCP+TLS share of request time; many short-lived connections; errors on the first request after idle.

## 3. What to inspect
Client construction (one shared client versus per-call clients); pool limits; idle and lifetime timeouts; handling of connection reset on reuse; DNS refresh.

## 4. Metrics
Reuse rate, connections opened per minute, handshake share of request time, stale-connection error rate.

## 5. Common bottlenecks and anti-patterns
New client per request; pool too small or unlimited; no timeouts; reusing non-idempotent requests on stale connections without safe-retry rules.

## 6. Candidate optimization techniques
Single shared client per origin set; sized pool; idle timeout below middlebox timeout; preconnect when a request is certain.

## 7. Runtime tunables versus build-time changes
Runtime: pool size, idle timeout, max lifetime. Build-time: client construction pattern.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal fix: share clients. Adaptive: pool size by measured concurrency need, within bounds.

## 9. Compatibility and version considerations
Library defaults differ widely; read the specific library docs.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Count handshakes per scenario before and after; test stale-connection recovery.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
