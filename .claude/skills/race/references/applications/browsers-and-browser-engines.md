<!-- format: 13-section -->
# Browsers and browser engines

## 1. Purpose and applicability
Multi-process browsers and embedded engines. Most work is in open-source engine code; contribution rules apply.

## 2. Detection signals
Chromium/Gecko/WebKit-derived trees.

## 3. What to inspect
Process model, memory limits, tab discarding, GPU process, network stack, startup.

## 4. Metrics
Startup, page load, memory per tab, jank, power.

## 5. Common bottlenecks and anti-patterns
Unbounded tab memory; sync IPC; large cold-start work.

## 6. Candidate optimization techniques
Follow upstream guidelines and benchmarks; changes small and measured; see open-source-contribution reference.

## 7. Runtime tunables versus build-time changes
Runtime: via the project's existing preferences/flags.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
RACE: hardware-adaptive choices among registered paths. /optimize: universal code, build and data fixes. No-go changes: weakening security sandboxes, same-origin rules or privacy protections.

## 9. Compatibility and version considerations
Upstream benchmarks (e.g., project-standard suites) define regression gates.

## 10. Security, privacy, accessibility, data integrity
Security and privacy features are untouchable for speed.

## 11. Validation and benchmark methodology
Use the project's perf infrastructure; label results with versions.

## 12. Rollback considerations
Upstream revert procedures.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
