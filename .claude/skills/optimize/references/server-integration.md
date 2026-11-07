<!-- format: 13-section -->
# Server intelligence integration (optimize)

## 1. Purpose and applicability
Apply device-independent backend improvements: algorithms, queries, caching correctness, resource handling, concurrency safety. The shared Server & Backend Intelligence library ships with the skill named server-optimize. If that skill is installed, read its references/INDEX.md and load only the domain files relevant to the backend component found. If it is not installed, continue with this skill's own references and tell the developer that the shared library is unavailable; never invent server facts. Use only the universal domain guidance; ignore hardware- and network-specific tuning.

## 2. Detection signals
Backend code, ORM or SQL queries, caches, queues, background jobs, request handlers.

## 3. What to inspect
N+1 queries, missing indexes (as evidenced by query plans in code or tests), redundant work in the request path, unbounded memory, lock contention, caching key correctness, error handling.

## 4. Metrics
Algorithmic complexity, query counts per request, allocation counts, deterministic test timings.

## 5. Common bottlenecks and anti-patterns
Selecting an optimization because of a particular user's CPU, memory or network; caching without correct keys; removing validation for speed.

## 6. Candidate optimization techniques
Remove redundant work, batch queries, fix N+1, correct cache keys and invalidation, bound resources, make concurrency safe.

## 7. Runtime tunables versus build-time changes
Build-time and code-level changes only; no machine-specific constants.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/optimize lens: this file. /race lens: hardware-aware selection is out of scope here. /ping-optimize lens: network-condition adaptation is out of scope here.

## 9. Compatibility and version considerations
Changes must behave identically across supported environments.

## 10. Security, privacy and accessibility considerations
Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Existing tests plus new regression tests; results must not depend on the machine used.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
