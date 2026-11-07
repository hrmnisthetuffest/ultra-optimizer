<!-- format: 13-section -->
# Downloads and uploads

## 1. Purpose and applicability
Faster, resumable, verified transfers.

## 2. Detection signals
Slow large transfers, restart from zero after failure, corrupted files.

## 3. What to inspect
Range support, chunking, parallelism, checksums, retry logic, scheduling and priorities, temp-file handling.

## 4. Metrics
Goodput, resume success, verification failures, time to complete.

## 5. Common bottlenecks and anti-patterns
Single flow underusing link, whole-file restart, no verification, too many parallel parts triggering rate limits.

## 6. Candidate optimization techniques
Range requests with resumption, bounded parallel parts when single flow is demonstrably the limit, per-chunk or whole-file verification, backoff, pacing against interactive traffic.

## 7. Runtime tunables versus build-time changes
Runtime: parts, chunk size, rate cap. Build-time: manifest or checksum format.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Parts and chunk size from measured throughput (adaptive, bounded).

## 9. Compatibility and version considerations
Servers must support ranges; keep single-stream fallback.

## 10. Security, privacy and accessibility considerations
Verify integrity; do not follow redirects to untrusted hosts for sensitive data.

## 11. Validation and testing
Interrupt at random offsets; assert byte-exact result.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
