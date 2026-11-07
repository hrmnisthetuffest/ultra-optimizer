<!-- format: 13-section -->
# Containers

## 1. Purpose and applicability
Build small, fast, correct images and run containers within sensible resource limits.

## 2. Detection signals
Large images, slow starts, OOM kills, CPU throttling, root user, secrets in layers.

## 3. What to inspect
Dockerfile layering, base image, multi-stage builds, resource limits/requests as seen by the runtime, health checks, signals and graceful shutdown, user and filesystem permissions.

## 4. Metrics
Image size, build time, start time, throttled CPU time, restarts, OOM count.

## 5. Common bottlenecks and anti-patterns
Single-stage builds with build tools, cache-busting layer order, ignoring cgroup limits, running as root, no graceful shutdown.

## 6. Candidate optimization techniques
Multi-stage builds, stable layer ordering, pinned slim bases, runtime reads cgroup limits, handle SIGTERM, drop privileges.

## 7. Runtime tunables versus build-time changes
Runtime: limits, health-check timings. Build-time: image structure.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: read effective CPU and memory limits at startup; never use host totals inside a container. /optimize lens: image hygiene and build correctness. /ping-optimize lens: startup time affects first-request latency.

## 9. Compatibility and version considerations
Behavior differs across container runtimes and cgroup versions.

## 10. Security, privacy and accessibility considerations
Never bake secrets into images; do not add privileged flags for performance. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Build reproducibility, image scan, start-time and memory measurement, graceful-shutdown test.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
