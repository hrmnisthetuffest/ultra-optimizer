<!-- format: 13-section -->
# Cloud storage and sync

## 1. Purpose and applicability
Efficient incremental synchronization and transfer scheduling.

## 2. Detection signals
Whole-file reuploads, long initial sync, conflict storms, retry loops.

## 3. What to inspect
Change detection, delta or block-level transfer, chunking, manifest, conflict handling, scheduling, rate limiting.

## 4. Metrics
Bytes uploaded per change, sync latency, conflict rate, retries, battery/data cost.

## 5. Common bottlenecks and anti-patterns
Re-uploading unchanged data, sequential tiny uploads, no dedup, tight retry loops after errors.

## 6. Candidate optimization techniques
Block-level delta and content-addressed dedup, batched metadata calls, resumable chunked uploads, backoff with jitter, deferred background sync with user control.

## 7. Runtime tunables versus build-time changes
Runtime: chunk size, concurrency, schedule. Build-time: chunking scheme.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Scheduling by measured conditions is adaptive; delta/dedup is universal.

## 9. Compatibility and version considerations
Changing chunking breaks dedup compatibility; version it.

## 10. Security, privacy and accessibility considerations
Encryption at rest/in transit and sharing permissions must remain; dedup across users can leak existence of content, so scope dedup carefully.

## 11. Validation and testing
Fault-injection tests: interruption mid-chunk, conflicting edits, partial server failure; assert no data loss.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
