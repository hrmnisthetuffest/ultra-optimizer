<!-- format: 13-section -->
# Open-source contribution mode (RACE)

## 1. Purpose and applicability
Rules for improving an external open-source repository with RACE. Applies when the target is not the user's own project.

## 2. Detection signals
`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, `.github/` templates, a git remote that is not the user's, AI-disclosure policies.

## 3. What to inspect
Contribution guide, code style and test guidance, license and contribution terms, relevant open issues and discussions, existing performance-related patterns, whether maintainers asked for or rejected similar work.

## 4. Metrics
Patch size and focus; test coverage of the change; measured effect with conditions.

## 5. Common bottlenecks and anti-patterns
Adding RACE to a project whose maintainers did not choose it; large rewrites; new dependencies; unrelated formatting changes; assuming the license allows reuse of its test or benchmark data; opening a PR, comment or branch without authorization.

## 6. Candidate optimization techniques
Keep patches focused and reviewable; follow project conventions; include tests and benchmark evidence; explain problem, fix, trade-offs and measured impact; disclose AI assistance if the project requires it. Hardware-aware changes must fit the project's portability policy.

## 7. Runtime tunables versus build-time changes
Prefer changes the maintainers can accept without new runtime machinery; propose a RACE-style tunable only if they asked for one.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Contributing hardware-dependent code is acceptable only if the project already supports multiple targets with fallbacks. Otherwise suggest it in discussion form and do nothing else.

## 9. Compatibility and version considerations
Honor the project's supported platform and version matrix; do not drop support to gain speed.

## 10. Security, privacy, accessibility, data integrity
Do not include secrets or private benchmark data. Follow the project's security reporting policy for vulnerabilities found.

## 11. Validation and benchmark methodology
Run the project's own test suite and linters; reproduce benchmarks with documented commands so maintainers can repeat them.

## 12. Rollback considerations
Work on a local branch only. **Do not push, publish releases, comment on issues or open a PR without explicit user authorization.**

## 13. Authoritative sources and last-reviewed
Project spec section 12. Each project's own contribution guide governs. Last reviewed: 2026-11-07.
