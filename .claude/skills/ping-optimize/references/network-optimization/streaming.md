<!-- format: 13-section -->
# Streaming and chunked transfer

## 1. Purpose and applicability
Stream when partial data is useful early; chunk when resumption or memory limits matter.

## 2. Detection signals
Large payload buffered fully before use; long waits to first usable byte; memory spikes.

## 3. What to inspect
Response consumption model; buffer sizes; backpressure; framing and resumption points.

## 4. Metrics
Time to first usable data, memory peak, throughput, resume success rate.

## 5. Common bottlenecks and anti-patterns
Reading whole bodies into memory; no backpressure; chunks too small or too large; no integrity check per chunk.

## 6. Candidate optimization techniques
Incremental parsing, backpressure, range requests, sized chunks, per-chunk verification.

## 7. Runtime tunables versus build-time changes
Runtime: chunk size, buffer. Build-time: framing format.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Chunk size can adapt to measured throughput, bounded.

## 9. Compatibility and version considerations
Server must support ranges or streaming; keep non-streaming fallback.

## 10. Security, privacy and accessibility considerations
Collect only timings, sizes, counts and status codes. No bodies, cookies, tokens or URLs containing secrets. Local by default. User-visible controls must be accessible and localized.

## 11. Validation and testing
Interrupt mid-stream and assert resume without corruption or duplication.

## 12. Rollback and failure handling
Ship behind a flag or configuration value with a safe default; keep the previous behavior reachable; on failed validation or regression restore the last known-good configuration.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
