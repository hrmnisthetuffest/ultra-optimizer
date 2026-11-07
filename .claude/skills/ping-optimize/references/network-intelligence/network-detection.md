<!-- format: 13-section -->
# Network detection and connection characteristics

## 1. Purpose and applicability
Decide what the application can legitimately learn about its connection and how to use it. The application may read what supported APIs expose (for example the browser Network Information API where available, platform reachability callbacks, its own request timings). It must not change any device or network setting.

## 2. Detection signals
App already branches on online/offline; has retry or quality logic; media or sync features that should adapt; user complaints that differ by connection (mobile, hotel Wi-Fi, VPN).

## 3. What to inspect
Which signals the platform exposes and their permission requirements; which signals the app already records; whether decisions use connection TYPE (weak predictor) or MEASURED behavior (preferred); where reachability events are handled.

## 4. Metrics
Effective throughput up/down, RTT percentiles, jitter, loss estimate, interruption count, connection type label (as a hint only), request failure and reconnect rates.

## 5. Common bottlenecks and anti-patterns
Treating 'wifi' or 'cellular' as quality; trusting a vendor-reported downlink estimate as truth; one-shot detection at startup that never refreshes; blocking startup on a speed test.

## 6. Candidate optimization techniques
Prefer passive estimation from real request timings (rolling percentiles); use platform hints only to seed an initial guess; refresh on connectivity-change events; expose a single 'network condition' value with hysteresis (see adaptive-bandwidth).

## 7. Runtime tunables versus build-time changes
Runtime: thresholds, window sizes, sampling rate. Build-time: which platform APIs are compiled in. Record chosen values in the tuning registry with ranges and fallbacks.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Adapting to measured conditions is RACE-style, app-internal and only with developer authorization. Fixing the app so it does not need a fast link (fewer requests, smaller payloads) is universal and belongs to /optimize as well.

## 9. Compatibility and version considerations
Browser connection hints are not available in every engine and may be coarse or absent; mobile platforms differ in reachability semantics. Treat missing data as 'unknown', never guess.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Unit-test the classifier with synthetic timing traces (fast-stable, slow, unstable, high-latency, lossy). Test 'unknown' handling and flapping connectivity.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
MDN Network Information API and platform reachability docs: not fetched this session, unverified. web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07).
Last reviewed: 2026-11-07.
