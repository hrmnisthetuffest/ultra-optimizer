<!-- format: 13-section -->
# Consolidated configuration intake

## 1. Purpose and applicability
Define the mandatory first step of /server-optimize: one consolidated intake that gathers every material configuration answer before any analysis. Ordinary questions are not scattered through the workflow.

## 2. Detection signals
Every /server-optimize invocation. Also triggered later only by a genuinely new critical unknown or an authorization requirement that did not exist at intake time.

## 3. What to inspect
Run scripts/detect_deployment.py PROJECT_ROOT --intake. It returns the ten intake items with detected answers prefilled: (1) automatic, custom or local-only; (2) target environment(s); (3) hosting provider and location; (4) runtime, language, architecture, infrastructure; (5) databases, caches, queues, external services; (6) optimization priorities; (7) workload and traffic; (8) access level; (9) repository-only, read-only live, or authorized implementation; (10) operational constraints such as downtime, migrations and spending.

## 4. Metrics
Questions asked after intake (target: zero ordinary ones), unresolved items marked unknown, items prefilled and confirmed versus corrected.

## 5. Common bottlenecks and anti-patterns
Asking one question at a time across the workflow; asking for secrets, tokens or connection strings; silently assuming production; treating detected values as verified; asking about details that cannot change the plan.

## 6. Candidate optimization techniques
Present all items together with prefilled values and an unknown or not-applicable option for each. Prefer the native interactive question tool (AskUserQuestion). It accepts at most four questions per call and two to four options each, so send the choice-type items as back-to-back calls with no analysis between them, and collect free-text items (hosting details, services, workload, constraints) in one plain-text block that the developer edits. If interactive input is unavailable, print the whole intake as one text form and wait for one reply. Never block on unknown answers: record them as unknown and continue with repository-only analysis.

## 7. Runtime tunables versus build-time changes
Runtime: none. The answers become a deployment profile (schemas/deployment-profile.schema.json) that the rest of the workflow reads.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: needs verified CPU, memory, architecture and limits; unknowns become benchmarks or developer-approved assumptions. /optimize lens: ignores hosting answers when choosing code changes. /ping-optimize lens: needs endpoints, regions and authorization for active probes.

## 9. Compatibility and version considerations
Interactive question UI limits may change; the text fallback must always work.

## 10. Security, privacy and accessibility considerations
Never ask the developer to paste credentials, keys, tokens, connection strings or cookies. Ask for the name of the mechanism (environment variable name, secrets manager, cloud identity) only. Default access is repo-only; analysis scope defaults to repository-only. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
Test that the intake contains exactly the ten items, prefills detected values, marks each prefill source, never contains a secret field, and defaults to repository-only.

## 12. Rollback and failure handling
If the developer cancels or answers inconsistently (for example production-modify without naming production as authorized), fall back to repository-only and say so. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
