<!-- format: 13-section -->
# Display and media capabilities

## 1. Purpose and applicability
Use display, codec and capture capabilities that the platform reports to choose rendering and media paths. Applies to games, video, image and UI-heavy apps.

## 2. Detection signals
Display resolution, scale factor, refresh rate, HDR/wide-gamut flags as exposed to apps; hardware encode/decode support per codec from the media API; camera/capture capabilities; audio device formats.

## 3. What to inspect
Render-resolution policy, frame pacing, vsync/frame limiting, decode/encode pipelines, color management, multi-monitor behavior.

## 4. Metrics
Frame-pacing consistency, dropped frames, decode/encode throughput, latency, CPU vs hardware codec load, quality metrics when changing encode settings.

## 5. Common bottlenecks and anti-patterns
Rendering above the display's refresh needs without reason; software codecs when hardware ones are available (or the reverse when hardware is buggy); ignoring high-DPI scaling; changing global display settings (forbidden).

## 6. Candidate optimization techniques
Match internal resolution and frame cap to the display within quality rules; select hardware codec paths only when reported and tested, with software fallback; adapt buffering to refresh rate.

## 7. Runtime tunables versus build-time changes
Runtime: render scale, frame cap, codec path, buffer count.

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Display- and codec-dependent choices are RACE. Asset compression and format changes for declared targets are universal.

## 9. Compatibility and version considerations
Hardware codec support differs by driver and OS; accessibility needs (reduced motion, high contrast) override performance choices.

## 10. Security, privacy, accessibility, data integrity
Never lower quality below declared product requirements; keep captions, contrast and motion settings intact. Do not log media content.

## 11. Validation and benchmark methodology
Visual/audio diff within tolerance; long-run stability; test with and without hardware acceleration.

## 12. Rollback considerations
Revert to the software/baseline path on decode errors or visual defects.

## 13. Authoritative sources and last-reviewed
Platform media API docs per project (not fetched; **unverified**). Last reviewed: 2026-11-07.
