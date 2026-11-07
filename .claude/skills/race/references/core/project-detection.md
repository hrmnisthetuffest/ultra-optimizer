<!-- format: 13-section -->
# Project and stack detection

## 1. Purpose and applicability
Identify the real stack, application type, supported platforms and existing performance surfaces before proposing anything. Applies at the start of every `build`, `audit`, `integrate` and `improve` run, including monorepos and mixed-language projects.

## 2. Detection signals
| Signal | Indicates |
|---|---|
| `package.json`, lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`) | Node/JS/TS; check deps for `electron`, `react`, `next`, `vue`, `@angular/core`, `svelte`, `@tauri-apps/api` |
| `Cargo.toml`, `Cargo.lock`, `tauri.conf.json` | Rust; Tauri if the config is present |
| `CMakeLists.txt`, `meson.build`, `BUILD.bazel`, `Makefile` | C/C++ build systems |
| `*.csproj`, `*.sln`, `Directory.Build.props` | .NET (WPF/WinUI/MAUI/ASP.NET Core by package refs) |
| `Package.swift`, `*.xcodeproj` | Swift/Xcode |
| `build.gradle(.kts)`, `pom.xml`, `AndroidManifest.xml` | JVM/Kotlin/Android |
| `pyproject.toml`, `requirements.txt`, `setup.cfg` | Python (Django/FastAPI by deps) |
| `go.mod`, `pubspec.yaml`, `composer.json`, `Gemfile` | Go, Dart/Flutter, PHP, Ruby |
| `ProjectSettings/`, `*.uproject` | Unity, Unreal |
Architecture hints: `docker-compose.yml`, `serverless.yml`, `k8s/`, message-queue clients, service directories.

## 3. What to inspect
Manifests and lockfiles first; build and CI config; entry points; existing config/preferences code; logging/metrics code; test directories and commands; README and contribution docs; `git status` for uncommitted work (do not touch it).

## 4. Metrics
Detection confidence per finding (confirmed from file / inferred / unknown); list of unknowns to ask the developer about.

## 5. Common bottlenecks and anti-patterns
Guessing the stack from a single file; ignoring secondary languages (native addon in a JS app); assuming the dev machine equals the target; treating a monorepo as one app.

## 6. Candidate optimization techniques
Not applicable (this is discovery). Output: a stack map naming each component, its runtime, its build tool, and which reference files to load.

## 7. Runtime tunables versus build-time changes
Record which existing settings are runtime-adjustable (config files, env read by the app) versus build-time (compiler flags, bundler config).

## 8. Hardware-dependent decisions (RACE) versus universal changes (/optimize)
Note which components can benefit from hardware-aware paths (native/compute/render) versus those where only universal changes apply.

## 9. Compatibility and version considerations
Record minimum supported OS/runtime versions from manifests; never raise them as part of optimization without approval.

## 10. Security, privacy, accessibility, data integrity
Do not read secrets files (`.env`, key files) for detection; mention their presence only. Do not upload any project content to external services.

## 11. Validation and benchmark methodology
Cross-check the stack map against the build: run the documented build/test commands (read-only where possible) before relying on the map.

## 12. Rollback considerations
Detection is read-only. If a build or test run creates artifacts, record them so they can be cleaned up without touching user files.

## 13. Authoritative sources and last-reviewed
Project spec section 8; file-name conventions are widely documented by each tool's official docs (not re-fetched this session). Last reviewed: 2026-11-07.
