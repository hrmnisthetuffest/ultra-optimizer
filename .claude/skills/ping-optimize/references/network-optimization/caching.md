<!-- format: 13-section -->
# Caching: HTTP, memory and disk

## 1. Purpose and applicability
Avoid transfers by reusing valid data, while preserving freshness and confidentiality.

## 2. Detection signals
Repeated identical downloads; missing validators; no-store on static assets; caches that serve stale or wrong-user data.

## 3. What to inspect
Cache-Control, ETag, Last-Modified, Vary on responses; client cache layers and their keys; invalidation triggers; authentication context in keys.

## 4. Metrics
Hit rate, revalidation rate (304), bytes saved, staleness incidents.

## 5. Common bottlenecks and anti-patterns
Caching private responses in shared caches; keys without user or locale; no invalidation on write; ignoring Vary; caching errors.

## 6. Candidate optimization techniques
Use standard validators and conditional requests; set explicit freshness; include identity and Vary dimensions in keys; version static assets; short TTL or revalidate for changing data.

## 7. Runtime tunables versus build-time changes
Runtime: TTLs, cache sizes. Build-time: asset fingerprinting.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal. Caching rules do not depend on the user's device.

## 9. Compatibility and version considerations
Per RFC 9111, freshness comes from s-maxage, max-age or Expires; stale responses are revalidated with ETag/If-None-Match or Last-Modified/If-Modified-Since; a shared cache must not reuse a response to a request with Authorization unless the response permits it (must-revalidate, public or s-maxage); private bars shared-cache storage.

## 10. Security, privacy and accessibility considerations
Never cache authenticated or personalized content in shared caches or under keys lacking identity. Clear caches on logout. Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Tests: wrong-user leakage impossible; invalidation after write; 304 path; Vary respected; offline behavior unchanged.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
RFC 9111 HTTP Caching, https://www.rfc-editor.org/rfc/rfc9111.html (fetched 2026-11-07, first 100000 chars read).
Last reviewed: 2026-11-07.
