<!-- format: 13-section -->
# Data integrity and migration

## 1. Purpose and applicability
Protect persisted data and formats during optimization.

## 2. Detection signals
Schemas, migrations, serializers, database files, caches.

## 3. What to inspect
Formats and versions, durability settings, migration scripts, backups.

## 4. Metrics
Round-trip equality, migration success, corruption detection.

## 5. Common bottlenecks and anti-patterns
Format changes without migration; weakened durability; cache poisoning.

## 6. Candidate optimization techniques
Avoid format changes unless approved; round-trip tests; backup before migration; read-compat with old versions.

## 7. Runtime tunables versus build-time changes
None at runtime unless a registered cache/format parameter.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Applies to both; hardware never changes data format.

## 9. Compatibility and version considerations
Older and newer app versions must read what is written.

## 10. Security, privacy, accessibility, data integrity
Encryption and integrity checks stay intact.

## 11. Validation and benchmark methodology
Property tests on serialization; crash-injection; migration dry runs.

## 12. Rollback considerations
Restore from backup; tested downgrade path.

## 13. Authoritative sources and last-reviewed
Generic method from the project spec; no external documents fetched for this file, so specific platform claims are **unverified**. Last reviewed: 2026-11-07.
