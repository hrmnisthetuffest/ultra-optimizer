<!-- format: 13-section -->
# Websites and Core Web Vitals

## 1. Purpose and applicability
Web pages and sites; field data (real users) versus lab data; LCP, INP, CLS and long tasks.

## 2. Detection signals
HTML/JS/CSS projects, frameworks in package.json.

## 3. What to inspect
Critical rendering path, bundle sizes, images/fonts, third-party scripts, caching headers, hydration, long tasks.

## 4. Metrics
LCP, INP, CLS (lab proxies and field data when available), TTFB, JS execution time, transfer size.

## 5. Common bottlenecks and anti-patterns
Render-blocking resources; oversized images; layout shifts; heavy third-party scripts; hydration cost.

## 6. Candidate optimization techniques
Optimize images/fonts, preload critical resources, split code, defer non-critical JS, reserve layout space, cache. Browser-side adaptation to device capability only via supported web APIs and only with consent where privacy-sensitive (RACE).

## 7. Runtime tunables versus build-time changes
Runtime: image quality tier, prefetch policy. Build-time: bundling, compression.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: removing content or accessibility features, hiding third-party consent flows, cloaking for crawlers.

## 9. Compatibility and version considerations
Browser support lists; SEO changes only when relevant and without altering content semantics.

## 10. Security, privacy, accessibility, data integrity
Preserve a11y (semantics, focus, contrast); do not add tracking; respect consent.

## 11. Validation and benchmark methodology
Lighthouse/lab tests plus field data where available; label lab vs field results; repeat runs.

## 12. Rollback considerations
Revert via deploy tooling; keep old asset names reachable until caches expire.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
