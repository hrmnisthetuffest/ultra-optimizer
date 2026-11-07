<!-- format: 13-section -->
# Video and audio streaming

## 1. Purpose and applicability
Faster start, fewer rebuffers, stable quality without breaking sync.

## 2. Detection signals
Long startup, rebuffering, quality oscillation, A/V drift.

## 3. What to inspect
Adaptive bitrate logic, segment size, buffer targets, manifest fetch chain, CDN usage, error recovery, startup sequence, codec and container support.

## 4. Metrics
Startup delay, rebuffer ratio, bitrate switches, buffer health, segment fetch time, stream recovery time.

## 5. Common bottlenecks and anti-patterns
Long manifest chains, conservative startup bitrate with no ramp, thrash on throughput estimate noise, buffer too small or too large, no recovery on segment failure.

## 6. Candidate optimization techniques
Parallel manifest/init fetch, bounded startup ramp, smoothed throughput estimate with hysteresis, appropriate buffer targets, retry another representation or CDN on failure, preserve A/V sync.

## 7. Runtime tunables versus build-time changes
Runtime: buffer targets, switch thresholds. Build-time: segment duration, packaging.

## 8. Hardware-dependent decisions (RACE-style, measured conditions) versus universal changes (/optimize)
ABR is the canonical measured-condition adaptation; quality choice is the user's/ developer's product decision.

## 9. Compatibility and version considerations
Players and DRM constrain options.

## 10. Security, privacy and accessibility considerations
DRM and content protection must remain intact.

## 11. Validation and testing
Throttled-profile tests with step changes in bandwidth; measure rebuffer ratio and startup.

## 12. Rollback and failure handling
Behind a flag with safe default; restore previous configuration on failed validation.

## 13. Sources and last reviewed
No external source fetched for this file in this session; statements are general engineering knowledge and are unverified until checked against current official documentation for the project's actual stack.
Last reviewed: 2026-11-07.
