<!-- format: 13-section -->
# TLS performance and safe reuse

## 1. Purpose and applicability
TLS adds handshake round trips and CPU work. Improve performance by reusing sessions and connections, never by weakening verification or ciphers.

## 2. Detection signals
Handshake time dominates first request; new TLS session per request; certificate validation done slowly or repeatedly.

## 3. What to inspect
Library TLS configuration; session resumption support; certificate pinning logic; OCSP or revocation behavior; protocol versions allowed.

## 4. Metrics
TLS handshake time, resumption rate, handshake failures, CPU time in crypto.

## 5. Common bottlenecks and anti-patterns
No connection reuse; disabled resumption; custom trust code on hot path; verification disabled in 'fast' builds.

## 6. Candidate optimization techniques
Connection reuse first; enable standard session resumption through the library; use modern protocol versions the stack supports; keep verification on.

## 7. Runtime tunables versus build-time changes
Runtime: pool and idle timeout. Build-time: TLS library version and supported protocol set.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Hardware crypto acceleration is chosen by the TLS library; do not hand-roll.

## 9. Compatibility and version considerations
Policy compliance (minimum TLS version, FIPS, pinning) must be preserved.

## 10. Security, privacy and accessibility considerations
NEVER disable certificate or hostname verification, downgrade protocol versions, or ship test bypasses. Early-data features (0-RTT) are replayable: use only for idempotent requests and only if the server permits. Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Security tests: invalid certificate must fail, hostname mismatch must fail, downgrade must fail.

## 12. Rollback and failure handling
If a TLS change breaks connectivity, revert to the previous library configuration immediately.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
