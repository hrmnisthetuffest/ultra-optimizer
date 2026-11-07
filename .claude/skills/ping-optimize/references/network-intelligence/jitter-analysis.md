<!-- format: 13-section -->
# Jitter analysis

## 1. Purpose and applicability
Jitter is variation in delay. Real-time audio, video and games care about it more than about mean latency.

## 2. Detection signals
Choppy audio, rubber-banding, buffer underruns despite acceptable average RTT.

## 3. What to inspect
Packet or message inter-arrival times; jitter buffer or interpolation delay; clock sources used; whether timestamps come from the sender or receiver.

## 4. Metrics
Inter-arrival standard deviation or mean absolute deviation, p95-p50 spread, late-packet rate, jitter-buffer underrun and overrun counts.

## 5. Common bottlenecks and anti-patterns
Fixed tiny buffers; sending bursts instead of paced packets; main-thread stalls mistaken for network jitter; sampling on a busy event loop.

## 6. Candidate optimization techniques
Pace sends; adaptive jitter buffer within bounds; separate network jitter from local scheduling jitter by timestamping at the socket; reduce bursts.

## 7. Runtime tunables versus build-time changes
Runtime: buffer target, pacing interval. Build-time: protocol timestamps.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Buffer sizing from measured jitter is adaptive and must trade latency for smoothness explicitly. Do not hide this tradeoff.

## 9. Compatibility and version considerations
Real-time stacks (WebRTC) already include adaptive buffers; configure through their documented APIs rather than replacing them.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Use network_sim with variable-latency profiles; assert bounded buffer growth and no unbounded delay.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
