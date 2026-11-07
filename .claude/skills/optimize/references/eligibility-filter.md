<!-- format: 13-section -->
# Broad-benefit eligibility filter

## 1. Purpose and applicability
Decide whether a candidate change belongs in /optimize. Only broadly applicable, device-independent improvements qualify.

## 2. Detection signals
Candidate arises from code, build config, queries, dependencies or measured behavior on the declared supported environments.

## 3. What to inspect
Ask six questions: (1) Is it independent of a specific hardware model? (2) Does it improve a general property such as algorithmic cost, I/O, memory, startup or bundle size? (3) Does it preserve platform support and existing behavior? (4) Is there evidence or a provable invariant? (5) Are tradeoffs understood and acceptable? (6) Is it testable and reversible?

## 4. Metrics
Per-question answer, evidence reference, and whether the answer is yes, no or unknown.

## 5. Common bottlenecks and anti-patterns
Treating 'faster on my machine' as general; claiming a fixed percentage benefit without data; hiding a device-specific tweak as generic.

## 6. Candidate optimization techniques
Accept only when all answers are yes or acceptable-with-disclosure. Reject or defer anything depending on live hardware detection, CPU/GPU architecture settings, CUDA/ROCm/Metal/DirectML choices, per-device thread or memory budgets, graphics quality tuning, device/OS/driver/firmware settings, or newly added AI.

## 7. Runtime tunables versus build-time changes
Not applicable at runtime; this is an engineering gate.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Declared target platforms and versions may be used; live detection of the user's machine may not.

## 9. Compatibility and version considerations
Respect minimum supported versions and public contracts.

## 10. Security, privacy, accessibility, data integrity
Security and privacy improvements are eligible; security regressions are not.

## 11. Validation and benchmark methodology
Record the six answers in the report for each accepted change.

## 12. Rollback considerations
A change failing any question later is reverted or reworked.

## 13. Authoritative sources and last-reviewed
Project spec section 9 and general engineering practice; no external documents fetched for this file (specifics **unverified**). Last reviewed: 2026-11-07.
