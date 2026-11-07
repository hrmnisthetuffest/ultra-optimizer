<!-- format: 13-section -->
# Developer integration decisions

## 1. Purpose and applicability
RACE integration requires a few decisions only the developer can make. Ask them once, at the start of a `build` or `integrate` run, skipping anything already answered in the conversation or project files. Use conservative defaults for the rest; do not ask the developer to repeat decisions.

## 2. Detection signals
Check first: existing settings UI, existing preferences storage, loading screen in startup code, existing AI features, existing telemetry, README statements of supported platforms.

## 3. What to inspect
Where a "Benchmark & Optimize" control would live; whether a notice component exists; localization and accessibility conventions of the UI; where persistent local state may be stored.

## 4. Metrics
Not applicable (decisions, not measurements). Record each decision with date and who made it.

## 5. Common bottlenecks and anti-patterns
Asking many questions that have safe defaults; adding a manual button when the developer did not choose one; showing repeated notices; proceeding on assumed answers for privacy-sensitive items.

## 6. Candidate optimization techniques
Not applicable.

## 7. Runtime tunables versus build-time changes
Decisions that become runtime settings: profile mode, auto-profiling on/off. Decisions that become build-time: target platforms, which tunables are registered.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
The questions below are RACE-only. `/optimize` asks none of them.

**Questions (with defaults):**
1. Manual "Benchmark & Optimize" button? Default **no**. If yes, ask where it lives.
2. Small temporary notice when noticeable optimization work occurs? Default **yes**. Example wording: "Optimizing your app for better performance. You may notice temporary slowdowns while we analyze and adjust its configuration." Adapt wording to the app's voice and localization. Show once per session at most; passive observation needs no notice; make no performance claim before measurement.
3. Additional AI features or integrations? Default **none**. If none or unspecified, add none.
4. Primary objective? Default **Balanced**. Others: max responsiveness, max throughput, min resource use, max reliability, min package size (build-time), custom.
5. Supported platforms and minimum versions? Default: those already in the manifests.
6. Is telemetry wanted? Default **no**; local-only history.
7. Any critical states where profiling must never run (calls, recording, export, gameplay, meetings)? Ask only if not discoverable.

**Always provide** the end user a way to pause/disable auto-profiling and restore last-known-good, even without the benchmark button (existing preferences or an approved settings surface).

## 9. Compatibility and version considerations
Notice and settings text must follow the app's localization system and accessibility patterns (screen-reader labels, no color-only signalling).

## 10. Security, privacy, accessibility, data integrity
Telemetry or any external sharing needs explicit consent, disclosure, retention controls and secure transport. Never default to on.

## 11. Validation and benchmark methodology
Verify the notice appears at most once, that pause/restore works, and that opting out leaves the app behaviorally unchanged.

## 12. Rollback considerations
Each decision is reversible by the user at runtime; store the choice in the profile (`auto_profiling`, `telemetry_consent`).

## 13. Authoritative sources and last-reviewed
Project spec sections 5.7, 5.8, 10 and Appendix C. Last reviewed: 2026-11-07.
