<!-- format: 13-section -->
# Compression and payload size

## 1. Purpose and applicability
Smaller payloads transfer faster when bandwidth or loss is the limit. Compression costs CPU and can leak secrets in some attack settings.

## 2. Detection signals
Large text responses uncompressed; verbose JSON; images oversized; CPU-bound compression.

## 3. What to inspect
Content-Encoding in use; payload sizes by endpoint; serialization format; image and media formats; compression level.

## 4. Metrics
Bytes before/after, compression ratio, CPU time, transfer time.

## 5. Common bottlenecks and anti-patterns
Compressing already compressed data; high levels on hot paths; sending unused fields; no delta for repeated data.

## 6. Candidate optimization techniques
Enable standard content encodings the server and client both support; trim fields; use compact formats where compatible; deltas for repeated state; right-size images.

## 7. Runtime tunables versus build-time changes
Runtime: compression level, thresholds. Build-time: serialization format.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Compression level may depend on measured bandwidth versus CPU (adaptive, bounded). Field trimming is universal.

## 9. Compatibility and version considerations
Content negotiation required; keep old clients working.

## 10. Security, privacy and accessibility considerations
Compressing secrets alongside attacker-controlled data over TLS can leak information (BREACH-class issues); avoid compressing responses that mix secrets with reflected input. Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Round-trip integrity tests; measure CPU and latency, not only size.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
