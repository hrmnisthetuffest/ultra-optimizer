# RACE reference index

Substantive references are listed with links. Items marked **roadmap-only** have no file yet; they are listed so gaps are explicit rather than hidden by stubs. To add one, follow `core/knowledge-expansion.md` and the 13-section format (see any existing reference).

## Core
- [adaptive-selection](core/adaptive-selection.md)
- [benchmarking-methodology](core/benchmarking-methodology.md)
- [developer-integration-decisions](core/developer-integration-decisions.md)
- [knowledge-expansion](core/knowledge-expansion.md)
- [open-source-contribution](core/open-source-contribution.md)
- [privacy-and-consent](core/privacy-and-consent.md)
- [profiling-levels](core/profiling-levels.md)
- [project-detection](core/project-detection.md)
- [race-overview](core/race-overview.md)
- [rollback-and-recovery](core/rollback-and-recovery.md)
- [scheduling-and-idle-detection](core/scheduling-and-idle-detection.md)
- [tuning-registry](core/tuning-registry.md)
- [workload-analysis](core/workload-analysis.md)

## hardware
- [ai-accelerators](hardware/ai-accelerators.md)
- [cpu-gpu-pairing](hardware/cpu-gpu-pairing.md)
- [cpu-intelligence](hardware/cpu-intelligence.md)
- [display-and-media-capabilities](hardware/display-and-media-capabilities.md)
- [gpu-intelligence](hardware/gpu-intelligence.md)
- [instruction-sets-and-dispatch](hardware/instruction-sets-and-dispatch.md)
- [memory-intelligence](hardware/memory-intelligence.md)
- [nvidia-gpu-architectures](hardware/nvidia-gpu-architectures.md)
- [platform-and-runtime](hardware/platform-and-runtime.md)
- [storage-and-io](hardware/storage-and-io.md)
- [thermal-and-sustained-performance](hardware/thermal-and-sustained-performance.md)

## workloads
- [cpu-bound](workloads/cpu-bound.md)
- [gpu-bound](workloads/gpu-bound.md)
- [latency-sensitive](workloads/latency-sensitive.md)
- [memory-bound](workloads/memory-bound.md)
- [mixed-workloads](workloads/mixed-workloads.md)
- [network-bound](workloads/network-bound.md)
- [real-time](workloads/real-time.md)
- [storage-bound](workloads/storage-bound.md)
- [throughput-oriented](workloads/throughput-oriented.md)

## applications
- [ai-applications](applications/ai-applications.md)
- [browsers-and-browser-engines](applications/browsers-and-browser-engines.md)
- [desktop-apps](applications/desktop-apps.md)
- [developer-tools-and-ides](applications/developer-tools-and-ides.md)
- [electron-apps](applications/electron-apps.md)
- [games-and-game-launchers](applications/games-and-game-launchers.md)
- [tauri-apps](applications/tauri-apps.md)
- [websites-and-core-web-vitals](applications/websites-and-core-web-vitals.md)

## languages
- [c-cpp](languages/c-cpp.md)
- [csharp-dotnet](languages/csharp-dotnet.md)
- [go](languages/go.md)
- [java-kotlin](languages/java-kotlin.md)
- [javascript-typescript](languages/javascript-typescript.md)
- [python](languages/python.md)
- [rust](languages/rust.md)
- [swift-objc](languages/swift-objc.md)

## frameworks
- [django-and-fastapi](frameworks/django-and-fastapi.md)
- [flutter-and-react-native](frameworks/flutter-and-react-native.md)
- [nodejs-backend](frameworks/nodejs-backend.md)
- [qt-gtk-and-native-ui](frameworks/qt-gtk-and-native-ui.md)
- [react-and-nextjs](frameworks/react-and-nextjs.md)
- [spring-and-aspnet-core](frameworks/spring-and-aspnet-core.md)

## architectures
- [client-server-and-offline-first](architectures/client-server-and-offline-first.md)
- [microservices-and-event-driven](architectures/microservices-and-event-driven.md)
- [monolith-and-modular-monolith](architectures/monolith-and-modular-monolith.md)
- [serverless-and-batch-streaming](architectures/serverless-and-batch-streaming.md)

## compilers-and-build
- [binary-and-package-size](compilers-and-build/binary-and-package-size.md)
- [build-caching-and-incremental-builds](compilers-and-build/build-caching-and-incremental-builds.md)
- [compiler-optimization](compilers-and-build/compiler-optimization.md)
- [link-time-and-profile-guided-optimization](compilers-and-build/link-time-and-profile-guided-optimization.md)

## quality
- [change-impact-analysis](quality/change-impact-analysis.md)
- [compatibility](quality/compatibility.md)
- [data-integrity](quality/data-integrity.md)
- [functionality-preservation](quality/functionality-preservation.md)
- [observability-and-explainability](quality/observability-and-explainability.md)
- [performance-budgets](quality/performance-budgets.md)
- [regression-testing](quality/regression-testing.md)

## Roadmap-only (no file yet; unverified until written)
- hardware: intel-cpu-architectures, amd-cpu-architectures, arm64-and-apple-silicon, amd-gpu-architectures, intel-and-apple-gpus
- applications: messaging-and-email, office-and-productivity, photo-video-and-audio, file-and-cloud-sync-apps, password-and-security-apps, calendars-and-download-managers, databases-and-data-tools, engineering-and-scientific-apps
- languages: Dart, PHP, Ruby, Lua, R, Julia, SQL
- frameworks: Vue, Angular, Svelte, Unity, Unreal, Electron-specific framework internals beyond `applications/electron-apps`
- architectures: plugin, multi-tenant, real-time/streaming specifics, actor, reactive, data-oriented, microkernel
- compilers: per-toolchain deep dives (Clang/LLVM, GCC, MSVC, Bazel, Buck, Gradle, Maven, Xcode, Vite, Webpack, Rollup, esbuild)
- benchmarks: curated hardware benchmark record sets (use `schemas/hardware-benchmark.schema.json`; none curated yet)
