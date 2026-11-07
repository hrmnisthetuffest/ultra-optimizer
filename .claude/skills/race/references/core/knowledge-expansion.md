<!-- format: 13-section -->
# Knowledge expansion

## 1. Purpose and applicability
How to fill a knowledge gap (new language, framework, hardware architecture, workload) without guessing or silently changing shared material. Applies whenever the skill meets something its references do not cover.

## 2. Detection signals
The stack map names a technology with no reference file, or a reference is marked stale, `unverified` or `roadmap-only`; the user's hardware or framework is newer than the recorded versions.

## 3. What to inspect
`references/INDEX.md` (what exists), the last-reviewed date of the closest reference, the exact version in the project's manifests.

## 4. Metrics
Number of claims with a source; share of claims labelled fact versus hypothesis; age of sources.

## 5. Common bottlenecks and anti-patterns
Answering from memory as if verified; citing blogs before official docs; copying vendor marketing numbers as facts; mixing opinion with fact; rewriting shared references silently; sending project data to a search or AI service.

## 6. Candidate optimization techniques
Workflow: (1) state the exact gap and why it matters; (2) research official documentation first, then standards, source code, reputable publications, reproducible benchmarks; (3) record URL, publication/update date, software or hardware version, access date, conditions; (4) separate confirmed facts, hypotheses and opinions; (5) draft or update a reference in the 13-section format; (6) validate claims and check license/provenance (do not copy text or benchmark data whose terms are unknown); (7) leave it as a proposed local update and tell the user. Use the `hardware-benchmark` schema for evidence records with a confidence label.

## 7. Runtime tunables versus build-time changes
Not applicable. Knowledge is development-time only; the Runtime Engine does not fetch knowledge.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
New hardware knowledge feeds RACE; new language or framework knowledge is shared by both skills only by duplication, never by cross-links.

## 9. Compatibility and version considerations
Every reference carries a last-reviewed date; review stale ones before relying on version-specific advice. Official does not mean applicable to every project.

## 10. Security, privacy, accessibility, data integrity
Do not paste project secrets into queries. Do not send source or data externally. Respect site terms and licenses.

## 11. Validation and benchmark methodology
Cross-check a claim against a second independent source or a local measurement; if not possible, label it `unverified` or `estimated`.

## 12. Rollback considerations
Proposed updates live in a separate local file or branch; reverting is deleting that change.

## 13. Authoritative sources and last-reviewed
Project spec section 13. Last reviewed: 2026-11-07.
