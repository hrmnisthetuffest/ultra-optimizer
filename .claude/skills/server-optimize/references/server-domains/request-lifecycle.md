<!-- format: 13-section -->
# Request lifecycle

## 1. Purpose and applicability
Break one request into stages (accept, TLS, routing, auth, parse, handler, data access, serialize, send) so time can be attributed to a stage.

## 2. Detection signals
High TTFB with low CPU, slow handlers with fast queries, large serialization time, middleware that runs on every route.

## 3. What to inspect
Middleware order and cost, authentication/authorization cost, body parsing limits, handler awaits, serialization format, response streaming support, timeout and cancellation propagation.

## 4. Metrics
Per-stage durations, queue/accept delay, handler time, serialization time, bytes in/out, cancelled-request waste.

## 5. Common bottlenecks and anti-patterns
Heavy work in middleware, parsing bodies for routes that ignore them, synchronous crypto or compression on the event loop, no cancellation when the client disconnects, unbounded body size.

## 6. Candidate optimization techniques
Order cheap rejections first, skip unneeded middleware per route, stream large responses, propagate cancellation, cache auth lookups safely, precompute serializers.

## 7. Runtime tunables versus build-time changes
Runtime: body limits, timeouts, keep-alive settings in the app server. Build-time: route/middleware structure.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: choose compression level or crypto implementation by verified CPU features. /optimize lens: remove redundant per-request work. /ping-optimize lens: separate server processing time from network RTT using Server-Timing or equivalent.

## 9. Compatibility and version considerations
Changing middleware order can alter auth or logging semantics; verify security checks still run first.

## 10. Security, privacy and accessibility considerations
Never move authentication or authorization after expensive work or skip it for speed. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Per-stage timing before/after; auth and authorization regression tests; cancellation tests.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
