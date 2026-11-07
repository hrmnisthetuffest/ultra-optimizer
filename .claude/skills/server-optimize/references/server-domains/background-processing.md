<!-- format: 13-section -->
# Background jobs and scheduling

## 1. Purpose and applicability
Move slow work off the request path and run scheduled work safely.

## 2. Detection signals
Slow requests doing report/email/image work, cron overlap, job pile-ups.

## 3. What to inspect
Job definitions, scheduling, overlap protection, retries, idempotency, priorities, resource isolation from web workers.

## 4. Metrics
Job duration, queue wait, failure and retry rate, overlap count, resource use by jobs.

## 5. Common bottlenecks and anti-patterns
Jobs sharing the web worker pool, no overlap lock, non-idempotent retries, unbounded job fan-out.

## 6. Candidate optimization techniques
Queue slow work, add idempotency keys and leases, isolate job workers, rate-limit heavy jobs, schedule off-peak where allowed.

## 7. Runtime tunables versus build-time changes
Runtime: worker counts, schedules, timeouts.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: size job workers from verified spare capacity. /optimize lens: fix idempotency and overlap bugs. /ping-optimize lens: avoid bursts that saturate outbound links.

## 9. Compatibility and version considerations
Scheduler behavior varies by platform (cron, serverless scheduler, Kubernetes CronJob).

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Overlap test, retry test, crash-mid-job test.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
