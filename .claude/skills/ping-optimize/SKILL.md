---
name: ping-optimize
description: Diagnose and reduce application-perceived network latency and wasted network work in the app being developed. Use for round trips, request waterfalls, DNS/TCP/TLS overhead, connection reuse, HTTP/2 and HTTP/3, caching, retries and backoff, WebSocket and real-time traffic, game netcode, streaming, downloads and API chattiness, and for adapting the app's OWN networking to measured conditions. Changes only the application's networking implementation, never router, OS, driver, DNS, VPN or device settings.
argument-hint: [scope: e.g. browser navigation | game multiplayer latency | API response times | websocket connections | download performance | reduce unnecessary requests]
---

# /ping-optimize: network-performance diagnosis and optimization

This command makes the application communicate more efficiently, respond sooner, transfer data better and stay reliable on poor networks, so users wait less. It is not about making one ping number smaller. It is a network specialization that uses RACE-style, measured-condition adaptation, but it is a separate command from `/race` (hardware-aware optimization) and `/optimize` (universal, device-independent optimization). Do not run either of them from here; mention them if their scope is a better fit.

Requested scope: `$ARGUMENTS`
If the line above is empty, audit the whole project's networking. If a target, endpoint, workload or subsystem is named, scope everything to it. Users need not know networking jargon: translate findings into plain words.

## Non-negotiable rules

1. **Application only.** Never change router, modem, Wi-Fi, Ethernet adapter or driver, OS networking or TCP/IP settings, registry, device DNS, VPN, proxy, firewall, MTU, adapter power, BIOS/firmware or ISP settings. Never promise to remove ISP latency or shorten physical distance. Reject requests that need those changes and offer an application-level alternative.
2. **Attribute before optimizing.** Place each delay in one of nine buckets (application, local networking code, DNS, connection setup, transport, network path, remote server processing, data transfer, post-response client processing). Never confuse server processing time with network RTT. Never claim an app change reduced server ping without endpoint-specific measurements.
3. **Measure first, report honestly.** Establish a baseline, repeat measurements, compare before and after with percentiles. Never invent numbers. Label each claim as verified fact, measurement, estimate, hypothesis or unknown. One successful ping is not proof.
4. **Preserve behavior and security.** Keep features, API contracts, authentication, authorization, encryption, data integrity, offline behavior, error handling, rate limits and user preferences. Never disable TLS verification, weaken encryption or bypass restrictions. Never cache private or authenticated content incorrectly. Never blindly retry non-idempotent operations.
5. **Bounded, authorized testing.** Prefer passive observation and existing telemetry. Active probes only against endpoints the developer owns or explicitly authorizes: bounded, cancellable, no flooding, no scans, no excess parallel connections. Never collect browsing history, tokens, cookies, private bodies or unrelated personal data.
6. **No hidden machinery.** No background network agents, runtime network monitoring or telemetry without explicit developer authorization and documented user controls (pause, disable, last-known-good restore). No AI-based network optimization, agents or services unless the developer explicitly selects them.
7. **Adaptive changes need evidence and limits.** Bandwidth is not latency, and a faster link does not justify more concurrency. Every adaptive rule needs a measured trigger, hysteresis, safe bounds and a fallback.
8. **Safe and reversible.** Inspect repo state first; small reviewable changes; baseline and rollback point; no destructive or external actions (reset, force-push, deploy, publish, PR) without authorization; restore the previous known-good state if validation fails.

## Workflow (10 steps)

1. **Inspect** the project: languages, frameworks, networking libraries, protocols, architecture, application category. Run `python3 scripts/detect_network_stack.py <project-root>` (relative to this skill's directory) for a first guess, then verify by reading code.
2. **Map** how data travels: client calls, endpoints, protocols, proxies and CDNs, auth flow, retry layers, caches.
3. **Baseline** with available telemetry or a bounded, authorized probe. See the benchmark references.
4. **Diagnose**: attribute latency to the nine buckets; find sequential dependencies, duplicates, polling, missing reuse, oversized payloads, bad retries.
5. **Research** official documentation and standards for the actual stack; record URL, version and access date; mark anything unfetched as unverified.
6. **Discover** opportunities from the real code.
7. **Prioritize** by expected impact, evidence confidence, effort, regression risk, security implications and compatibility.
8. **Implement** focused, reviewable changes that preserve behavior.
9. **Validate**: unit and integration tests, simulated network conditions (latency, jitter, loss, bandwidth cap, interruption, DNS failure, slow or erroring server, partial responses, rate limiting, reconnection, offline), regression checks. Verify no duplicate transactions, corruption, infinite retries, request storms, broken auth or lost functionality.
10. **Report**: bottlenecks, changes, files modified, before/after measurements, test results, untested areas, remaining issues, recommendations.

## Load references on demand (do not load everything)

Reference root: [references/INDEX.md](references/INDEX.md) lists every file with a one-line purpose. Load only what the scope needs.

| Situation | Load |
|---|---|
| Starting an audit | [network-detection](references/network-intelligence/network-detection.md), [latency-analysis](references/network-intelligence/latency-analysis.md), [application-network-profiling](references/network-benchmarks/application-network-profiling.md) |
| Slow first request / handshakes | [dns-intelligence](references/network-intelligence/dns-intelligence.md), [tcp-intelligence](references/network-intelligence/tcp-intelligence.md), [tls-intelligence](references/network-intelligence/tls-intelligence.md), [connection-management](references/network-intelligence/connection-management.md) |
| Protocol choice | [http-protocols](references/network-intelligence/http-protocols.md), [http2](references/network-intelligence/http2.md), [http3-and-quic](references/network-intelligence/http3-and-quic.md) |
| Ping, jitter, loss, congestion | [ping-analysis](references/network-intelligence/ping-analysis.md), [jitter-analysis](references/network-intelligence/jitter-analysis.md), [packet-loss-analysis](references/network-intelligence/packet-loss-analysis.md), [congestion-analysis](references/network-intelligence/congestion-analysis.md), [loaded-latency](references/network-benchmarks/loaded-latency.md) |
| Server vs network blame | [server-response-analysis](references/network-intelligence/server-response-analysis.md), [bandwidth-analysis](references/network-intelligence/bandwidth-analysis.md) |
| Fixing request patterns | [request-optimization](references/network-optimization/request-optimization.md), [latency-reduction](references/network-optimization/latency-reduction.md), [connection-pooling](references/network-optimization/connection-pooling.md), [concurrency](references/network-optimization/concurrency.md) |
| Caching, size, prefetch | [caching](references/network-optimization/caching.md), [compression](references/network-optimization/compression.md), [prefetching](references/network-optimization/prefetching.md), [streaming](references/network-optimization/streaming.md) |
| Failure behavior | [retry-and-recovery](references/network-optimization/retry-and-recovery.md), [adaptive-bandwidth](references/network-optimization/adaptive-bandwidth.md) |
| Measuring and testing | [latency-benchmarks](references/network-benchmarks/latency-benchmarks.md), [bandwidth-benchmarks](references/network-benchmarks/bandwidth-benchmarks.md), [jitter-and-packet-loss](references/network-benchmarks/jitter-and-packet-loss.md), [network-regression-testing](references/network-benchmarks/network-regression-testing.md) |
| Application category | one file from `references/network-application-profiles/`: [browsers](references/network-application-profiles/browsers-networking.md), [games](references/network-application-profiles/games-networking.md), [messaging](references/network-application-profiles/messaging-networking.md), [video](references/network-application-profiles/video-streaming.md), [downloads](references/network-application-profiles/downloads-and-uploads.md), [cloud sync](references/network-application-profiles/cloud-sync.md), [API/SaaS](references/network-application-profiles/api-and-saas-networking.md) |

Executable contracts (stdlib Python, illustrative templates, not universal runtime code): [templates/network_reference_model.py](templates/network_reference_model.py) (backoff with jitter, idempotency keys, retry budget, request dedup, adaptive concurrency with hysteresis) and [templates/network_sim.py](templates/network_sim.py) (deterministic simulated network for condition tests). Adapt them to the project's language; do not paste them blindly.

## Scope and limits

Findings that depend on a particular user's network or device belong in app-level adaptive logic that the developer approves, not in global defaults. Universal fixes (redundant requests, waterfalls, serialization, correct caching) are the kind of change `/optimize` also makes; this command may make them when network evidence motivates them. Document what could not be measured. Report format and timing rules: baseline before change, no performance claim before measurement.
