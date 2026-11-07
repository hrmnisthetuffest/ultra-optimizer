<!-- format: 13-section -->
# CPU and GPU pairing and system balance

## 1. Purpose and applicability
Systems are combinations of components. Pairing effects exist but are easy to overstate. Applies when deciding CPU vs GPU placement and transfer strategy.

## 2. Detection signals
Integrated plus discrete GPU, hybrid-graphics routing, PCIe link speed/width where an API reports it, resizable-BAR/shared-memory indication where reported, unified-memory architectures, multi-GPU.

## 3. What to inspect
Data movement between CPU and GPU, transfer sizes, synchronization points, which adapter the app actually runs on, whether the app can choose the adapter.

## 4. Metrics
Transfer bandwidth and latency, CPU-side submit time, GPU idle time, end-to-end frame or batch time.

## 5. Common bottlenecks and anti-patterns
"Vendor X CPU with vendor X GPU is faster" stated as fact; scoring bonuses for matching brands; ignoring that the app may be on the integrated GPU; chatty small transfers across a slow link; assuming link width from the GPU name.

## 6. Candidate optimization techniques
Treat any pairing effect as a **hypothesis to test** on the actual system; batch and pipeline transfers; keep data resident on the device that uses it; choose the adapter by capability and measured throughput; allow a CPU path when transfer cost exceeds compute gain.

## 7. Runtime tunables versus build-time changes
Runtime: placement (CPU/GPU), batch size, transfer chunk size, adapter selector.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
All RACE. `/optimize` must not tune for a particular pairing.

## 9. Compatibility and version considerations
Hybrid-graphics behavior varies by OS and driver; test fallbacks.

## 10. Security, privacy, accessibility, data integrity
Do not export combination fingerprints. Results from different systems are not interchangeable.

## 11. Validation and benchmark methodology
Measure end-to-end, not kernel-only; run with both adapters if available; record versions.

## 12. Rollback considerations
Revert placement to the baseline on regression or errors.

## 13. Authoritative sources and last-reviewed
Project spec section 4.7 (no simplistic pairing claims). No vendor sources fetched; **unverified**. Last reviewed: 2026-11-07.
