<!-- format: 13-section -->
# Privacy and consent

## 1. Purpose and applicability
Rules for any data RACE touches, stores or could transmit. Applies to every integration and to Claude's own handling of project data.

## 2. Detection signals
Existing telemetry or analytics SDKs; privacy policy files; consent UI; settings storage; regional compliance notes in the repo.

## 3. What to inspect
What the app already collects, where it is stored, who can read it; whether a consent flow exists; whether profiles or histories would land in synced or shared locations.

## 4. Metrics
Count of data fields collected (target: minimum); retention period; presence of identifiers (target: none).

## 5. Common bottlenecks and anti-patterns
Collecting serial numbers, account names, file paths, content, passwords or tokens; enabling telemetry by default; sending hardware fingerprints that uniquely identify a device; storing profiles in cloud-synced folders without notice; logging raw user input.

## 6. Candidate optimization techniques
Defaults: local only; no telemetry; coarse capability classes instead of unique fingerprints; aggregate timings; user-clearable history. If the developer wants external telemetry: explicit opt-in consent, disclosure of what is sent, retention controls, secure transport, and a way to withdraw consent. Claude must not send project code, runtime data or user data to any external service.

## 7. Runtime tunables versus build-time changes
Runtime: `telemetry_consent`, `auto_profiling` (enabled/paused/disabled), history clear. Build-time: whether any transport code exists at all (prefer none).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Hardware detection data is RACE-specific and must not be exported. Universal privacy fixes (removing needless logging) belong to security/privacy work under the separate `/optimize` command.

## 9. Compatibility and version considerations
Regional rules (GDPR, CCPA, etc.) may apply to the app; flag the question to the developer rather than giving legal advice.

## 10. Security, privacy, accessibility, data integrity
Consent prompts must be accessible and localized. Stored profile files must not contain secrets. Validate and sanitize loaded profile files (untrusted input).

## 11. Validation and benchmark methodology
Test: fresh install collects nothing external; opt-out stops all collection; clearing history removes it; profile file with out-of-range values is rejected.

## 12. Rollback considerations
Withdrawing consent must delete or stop using collected data per the stated retention policy.

## 13. Authoritative sources and last-reviewed
Project spec sections 3.5 and 4.6. Regulatory text is not summarized here and was not consulted. Last reviewed: 2026-11-07.
