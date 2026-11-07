<!-- format: 13-section -->
# Online game networking

## 1. Purpose and applicability
Lower perceived lag and improve consistency without altering gameplay rules or fairness.

## 2. Detection signals
Rubber-banding, hit registration complaints, desync, bandwidth spikes, matchmaking delays.

## 3. What to inspect
Transport (UDP/QUIC/TCP/WebSocket), tick and send rates, replication scheme, snapshot and delta handling, interpolation, prediction and reconciliation, reliable/unreliable channels, matchmaking and endpoint selection.

## 4. Metrics
RTT p95, jitter, loss, snapshot age, correction frequency, bandwidth per client, packets per second.

## 5. Common bottlenecks and anti-patterns
Full-state snapshots, no delta compression, head-of-line blocking on reliable ordered channel for transient data, retransmitting stale state, sending too often, fixed interpolation buffer.

## 6. Candidate optimization techniques
Delta compression against acknowledged state, quantization, priority and relevancy filtering, unreliable channels for transient state with sequence numbers, interpolation buffer sized to measured jitter, prediction and reconciliation tuned without changing rules, matchmaking choosing among developer-provided regions by measured RTT.

## 7. Runtime tunables versus build-time changes
Runtime: send rate within server-approved bounds, interpolation delay. Build-time: serialization and protocol.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Region choice and interpolation delay are measured-condition (adaptive). Do not blindly raise tick rate; do not alter gameplay timing or fairness.

## 9. Compatibility and version considerations
Server authority and anti-cheat must remain intact; protocol changes need version negotiation.

## 10. Security, privacy and accessibility considerations
Never trust client-side prediction for authoritative state; do not expose extra state to clients for efficiency.

## 11. Validation and testing
Deterministic simulation with loss, jitter and reordering; assert state convergence and no fairness regression.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
