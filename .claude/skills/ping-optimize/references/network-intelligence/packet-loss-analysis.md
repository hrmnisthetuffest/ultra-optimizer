<!-- format: 13-section -->
# Packet loss analysis

## 1. Purpose and applicability
Loss changes the right strategy. Reliable transports hide loss as delay; unreliable ones expose it as missing data.

## 2. Detection signals
Stalls on TCP flows, throughput collapse on lossy links, missing updates in UDP-based features, frequent retransmission counters.

## 3. What to inspect
Transport in use per feature; retransmission or loss counters exposed by the stack; app-level sequence gaps; retry logic layered on top of reliable transports (double recovery).

## 4. Metrics
Loss rate estimate, retransmission count, stall duration, sequence-gap rate, recovery time.

## 5. Common bottlenecks and anti-patterns
Aggressive application retransmission on top of TCP; no sequence numbers on UDP messages; retransmitting stale state; treating every timeout as loss.

## 6. Candidate optimization techniques
For UDP game or media paths: sequence numbers, selective reliability, forward error correction where justified, resend only still-relevant data. For TCP/HTTP: avoid app-level retry storms, prefer resumable transfers.

## 7. Runtime tunables versus build-time changes
Runtime: retransmit timeout bounds, redundancy level. Build-time: message framing with sequence numbers.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Loss-adaptive redundancy is a measured-condition decision; set hard upper bounds so adaptation cannot amplify congestion.

## 9. Compatibility and version considerations
Loss counters differ per OS; many are not available to unprivileged apps. Mark as unknown when unavailable.

## 10. Security, privacy and accessibility considerations
Measure with the least data possible: timings, sizes, status codes, protocol versions. Never record URLs with secrets, cookies, tokens, request or response bodies, or browsing history. Any stored metrics stay local unless the developer approves otherwise. Surfaces that show network status must be accessible (not color-only) and localized.

## 11. Validation and testing
Inject loss (0, 1, 5, 10 percent, bursty and uniform) in network_sim; assert eventual consistency, no duplicates, bounded retransmission volume.

## 12. Rollback and failure handling
Network measurement code is read-only; if a probe misbehaves, cancel it and remove it. Any adaptive rule derived from measurements must fall back to the static default configuration and keep a last-known-good setting.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
