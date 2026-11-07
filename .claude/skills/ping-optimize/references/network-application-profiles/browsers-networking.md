<!-- format: 13-section -->
# Browser and web-page networking

## 1. Purpose and applicability
Faster page and resource delivery for web apps, and understanding the network stack of browser-engine projects.

## 2. Detection signals
Slow LCP/TTFB, long waterfalls, many origins, cache misses, large images, service-worker issues.

## 3. What to inspect
Resource waterfall, critical path, origins, protocols (H2/H3), cache headers, images and fonts, service worker fetch handlers, preload/preconnect, third parties, Core Web Vitals (lab versus field).

## 4. Metrics
TTFB, LCP, INP, CLS (field p75), requests, bytes, cache hit rate, protocol share.

## 5. Common bottlenecks and anti-patterns
Render-blocking chains, uncached static assets, oversized images, too many origins, service worker adding latency, late discovery of critical resources.

## 6. Candidate optimization techniques
Fingerprinted long-lived static assets, validators, preconnect to critical origins, preload critical resources, modern image formats and sizing, fewer origins, H2/H3 where available, careful service-worker caching strategies, defer non-critical.

## 7. Runtime tunables versus build-time changes
Runtime: hints, priorities. Build-time: bundling, asset pipeline.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal: caching, waterfall fixes. Adaptive: data-saver aware media quality.

## 9. Compatibility and version considerations
For browser-engine projects (for example Firefox/Gecko and its Necko network library): read the project's own networking docs and contribution rules, understand architecture and process model before changing code, and follow open-source contribution rules; Necko specifics were not fetched here and are unverified.

## 10. Security, privacy and accessibility considerations
Do not cache personalized responses publicly; respect cookies/SameSite/CORS; no tracking added for measurement.

## 11. Validation and testing
Lighthouse-style lab runs plus field data where the developer has it; throttled network tests; cache correctness tests.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
web.dev TTFB, https://web.dev/articles/ttfb (fetched 2026-11-07); other web.dev/MDN pages not fetched.
Last reviewed: 2026-11-07.
