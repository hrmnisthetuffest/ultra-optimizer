<!-- format: 13-section -->
# Messaging and real-time communication

## 1. Purpose and applicability
Fast, reliable, deduplicated message delivery with robust reconnection and offline sync.

## 2. Detection signals
Delayed or duplicated messages, reconnect storms, battery or data drain from polling, attachment stalls.

## 3. What to inspect
Transport (WebSocket, long poll, push), heartbeat, reconnect logic, message ids and ordering, sync protocol, attachment upload path, offline queue.

## 4. Metrics
Delivery latency, reconnect time, duplicate rate, message loss, polling requests per hour.

## 5. Common bottlenecks and anti-patterns
Polling instead of push, no message ids, reconnect without jitter, retrying sends without idempotency keys, big attachments blocking small messages.

## 6. Candidate optimization techniques
Persistent connection with heartbeat sized to middlebox timeouts, exponential backoff with jitter on reconnect, client-generated message ids for dedup, resumable attachments on a separate path, delta sync from last cursor.

## 7. Runtime tunables versus build-time changes
Runtime: heartbeat, backoff bounds. Build-time: protocol ids and cursors.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
Universal: dedup ids, cursors. Adaptive: heartbeat and sync cadence by measured stability, bounded.

## 9. Compatibility and version considerations
Old clients must still sync.

## 10. Security, privacy and accessibility considerations
End-to-end encryption and privacy must be unchanged; never log message content.

## 11. Validation and testing
Interruption/reconnect tests assert exactly-once display and order.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
