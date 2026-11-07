<!-- format: 13-section -->
# Network regression testing

## 1. Purpose and applicability
Keep network behavior from regressing after changes.

## 2. Detection signals
Any change touching networking.

## 3. What to inspect
Existing tests; network_sim scenarios; performance budgets (requests per operation, bytes, p95).

## 4. Metrics
Pass/fail per scenario, request counts, duplicate-transaction count, retry counts, latency budgets.

## 5. Common bottlenecks and anti-patterns
Flaky wall-clock tests; tests that need the real internet; no failure-path coverage.

## 6. Candidate optimization techniques
Deterministic simulated clock and network; scenarios: low/high/variable latency, jitter, loss, bandwidth cap, upload and download bottlenecks, interruption, DNS failure, slow server, 5xx, partial response, 429 rate limit, reconnect, offline. Assert: no duplicate transactions, no corruption, no infinite retries, no request storms, auth intact.

## 7. Runtime tunables versus build-time changes
Runtime: sample count, interval, size caps (all bounded). Build-time: whether probe endpoints or hooks exist.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Simulation validates logic, not real-world speed.

## 9. Compatibility and version considerations
Timing APIs and available counters differ by platform; record which were used.

## 10. Security, privacy and accessibility considerations
Run only against owned or explicitly authorized endpoints, with bounded traffic, cancellable, no flooding or scanning. Store timings and sizes only; no bodies, cookies, tokens or personal data.

## 11. Validation and testing
See tests/test_ping_optimize_model.py for a runnable example of these assertions.

## 12. Rollback and failure handling
Probes are removable; if a benchmark disturbs the application or the user, abort and discard the run.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
