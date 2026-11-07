<!-- format: 13-section -->
# Retry, backoff and recovery

## 1. Purpose and applicability
Retries recover transient failure but can create duplicates and storms. Design them deliberately.

## 2. Detection signals
Duplicate side effects after timeouts; synchronized retry bursts; infinite loops; users stuck offline.

## 3. What to inspect
Retry layers (library, app, UI); idempotency of each operation; timeouts; Retry-After handling; offline queue; cancellation.

## 4. Metrics
Retry rate, attempts per success, duplicate-operation count, time to recover.

## 5. Common bottlenecks and anti-patterns
Retrying non-idempotent operations blindly; fixed intervals without jitter; stacked retry layers multiplying attempts; no budget.

## 6. Candidate optimization techniques
Retry only idempotent or idempotency-keyed operations; exponential backoff with randomized jitter; retry budget and max attempts; honor Retry-After; offline queue with dedup keys; cancel on user action.

## 7. Runtime tunables versus build-time changes
Runtime: base delay, cap, max attempts, budget. All bounded in the registry.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal logic; thresholds may be tuned by measured conditions within bounds.

## 9. Compatibility and version considerations
Idempotency semantics of HTTP methods are defined in RFC 9110 (section 9.2.2, text not read here); keys require server support.

## 10. Security, privacy and accessibility considerations
Idempotency keys must be unguessable per operation and not reused across users. Never retry on authentication failure by replaying credentials. Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Reference model tests: backoff bounds, jitter range, retry budget, no retry of non-idempotent without key, dedup of replayed key.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
RFC 9110 HTTP Semantics, https://www.rfc-editor.org/rfc/rfc9110.html (fetched 2026-11-07 (retrieved section pointers only; semantics unverified in this session).
Last reviewed: 2026-11-07.
