# Ultra Optimizer — Claude Code Build Specification

**Primary engine:** RACE — Runtime Adaptive Configuration Engine  
**Primary command:** `/race`  
**Secondary command:** `/optimize`  
**Document type:** Implementation brief and acceptance contract for Claude Code  
**Version:** 1.0  
**Date:** 7 November 2026  
**Status:** Approved product direction; implementation not yet performed

---

## Instructions to Claude Code: build the actual skill suite

Treat this document as the authoritative product and implementation specification for creating **Ultra Optimizer**. Do not merely summarize it, discuss it, or return another plan. Inspect the current workspace, create the complete Claude Code skill suite and its supporting reference library, validate the files, and leave the workspace in a usable state.

If the current workspace is empty, create the project there. If it already contains a project, inspect it first and place the Ultra Optimizer skill package in a clearly separated directory without overwriting unrelated files. Do not integrate RACE into the workspace's host application merely because you are building the skill suite. The purpose of this task is to build the reusable skill package; `/race` will later integrate RACE into whichever application repository the user invokes it from.

Work in phases, but complete as much as can safely be completed in this task. Keep a progress file and a test/evaluation file so work can continue across context windows. Do not claim a component is implemented until its files exist and its tests or validation checks have actually run. Where the specification describes a future runtime capability that cannot be implemented generically without knowing a target application's language, framework, platform or architecture, create a precise integration contract, reference material and adaptable templates—not fake universal runtime code.

Do not ask the user to repeat decisions already established in this specification. Resolve routine implementation details using conservative defaults. Ask only when a decision is genuinely blocking or would authorize a material, irreversible, privacy-sensitive or externally visible action.

## 1. Product definition and hierarchy

### 1.1 Product identity

**Ultra Optimizer** is a modular Claude Code skill suite whose primary purpose is to help developers build, integrate and improve applications that adapt their own internal execution and configuration to the hardware and workload on which they run.

Its central technology is:

**RACE — Runtime Adaptive Configuration Engine**

RACE is the primary engine. It is intended to be integrated into the target application and run inside that application. It detects relevant device capabilities, observes the application's own workloads, evaluates safe application-level configurations, benchmarks candidates and applies validated configurations within developer-defined bounds.

The suite also contains a secondary, separate universal optimization workflow. AI capabilities are optional and must be explicitly selected by the developer.

### 1.2 Strict priority order

1. **RACE and hardware-aware application optimization** — the primary purpose and default perspective for application-performance work.
2. **Supporting engineering intelligence** — language, framework, architecture, profiling, code quality, algorithms, security, reliability, testing, UX, maintainability and other disciplines that make RACE and its host application better.
3. **Universal `/optimize`** — a separate, hardware-independent workflow for broadly applicable code and engineering improvements.
4. **Developer-selected AI capabilities** — optional only; never add AI product features, model integrations, agents, external AI services or AI dependencies without explicit developer selection.

Do not present Ultra Optimizer as a generic refactoring skill with RACE as an optional extra. RACE is the organizing principle of the suite.

### 1.3 Commands and their separation

The package must expose two directly invocable Claude Code skills:

- `/race` — primary workflow. Build, integrate, audit, benchmark, report on, or improve RACE in the current application. When a user asks generally for application optimization and RACE is relevant, RACE-first reasoning is the default.
- `/optimize` — secondary workflow. Improve the project using universal, device-independent engineering changes only. It must not use live hardware specifications to choose implementation settings or hardware-specific tuning values.

Do not merge these commands. Do not let `/optimize` quietly invoke RACE. Do not let `/race` silently become a device-settings tweaker.

Recommended skill behavior:

- `/race` may be automatically selected by Claude when the user clearly asks for hardware-aware application performance optimization, because that is the primary purpose of Ultra Optimizer. Keep its description precise so it does not activate for unrelated tasks.
- `/optimize` is explicitly user-invoked and should set `disable-model-invocation: true`, so Claude does not unexpectedly perform a code-changing universal optimization workflow on its own.
- Both commands remain available in the `/` command menu.
- Check for command-name collisions during installation and validation. If `/race` or `/optimize` is already taken, report the conflict and provide a safe alternative rather than silently replacing an existing skill.

## 2. Claude Code skill packaging requirements

Use Claude Code's current **Skills** structure, not a legacy-only custom command implementation.

Create two skill directories so the user can invoke the exact desired command names:

```text
.claude/
└── skills/
    ├── race/
    │   ├── SKILL.md
    │   ├── references/
    │   ├── schemas/
    │   ├── templates/
    │   ├── scripts/
    │   └── evals/
    │
    └── optimize/
        ├── SKILL.md
        ├── references/
        ├── checklists/
        └── evals/
```

The repository may have top-level `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `docs/`, `tests/`, `install/`, `progress.md`, and `CHANGELOG.md` as appropriate. Keep the Claude Code-loadable skill folders self-contained for project-local use. Do not make their runtime behavior depend on undocumented path assumptions or uninstalled external files.

### 2.1 SKILL.md requirements

Each skill must have valid YAML frontmatter at the very first line, followed by Markdown instructions.

Suggested starting frontmatter for `.claude/skills/race/SKILL.md`:

```yaml
---
name: race
description: Build, integrate, audit, benchmark, and improve RACE (Runtime Adaptive Configuration Engine), the hardware-aware application optimization engine. Use for application optimization that adapts application-internal behavior to detected hardware capabilities and real workloads.
argument-hint: [build|audit|benchmark|status|improve|integrate]
---
```

Suggested starting frontmatter for `.claude/skills/optimize/SKILL.md`:

```yaml
---
name: optimize
description: Perform universal, device-independent code and engineering optimization while preserving existing application behavior and functionality.
argument-hint: [audit|apply|review|report]
disable-model-invocation: true
---
```

Claude Code's skill command name is determined by the skill directory or frontmatter `name`. The exact commands must be tested in Claude Code rather than assumed from filenames alone. Do not use plugin packaging as the default if it would force the user's commands to be namespaced. A plugin distribution can be considered later as an optional distribution route, but the core deliverable must support `/race` and `/optimize` as ordinary personal or project skills.

Keep each `SKILL.md` concise and operational—preferably well below 500 lines. Put detailed guidance in supporting reference files and link to those files from `SKILL.md`. The skill entry point must explain the routing logic and tell Claude exactly which supporting references to load. Do not put the entire knowledge base into the always-loaded skill body.

Use only documented Claude Code frontmatter fields. Do not grant broad `allowed-tools` permissions by default. Preserve normal user permission prompts for shell commands, file operations, network calls, package installation and other meaningful side effects.

### 2.2 Installation and sharing

Provide safe installation instructions and scripts for:

- Project-local installation into `.claude/skills/`.
- Personal installation into `~/.claude/skills/` (with the appropriate home-directory behavior on Windows).
- Updating an existing Ultra Optimizer installation.
- Uninstalling only the files that the installer itself owns.

Installer behavior must:

- Detect the target OS and relevant Claude Code skills directory.
- Never overwrite unrelated skills.
- Detect an existing `race` or `optimize` directory and ask before replacing or offer a non-destructive backup/update path.
- Preserve user modifications or create a timestamped backup before a confirmed update.
- Print exactly what it installed, skipped or backed up.
- Avoid administrator privileges unless genuinely required; they should not be required for normal personal skill installation.
- Be idempotent where practical.

Document manual installation as a fallback. Test the installation scripts in the environments available in the build workspace. Do not claim Windows/macOS/Linux install support has been tested unless it has.

## 3. Global operating rules

These rules apply to the entire skill suite and are higher priority than optimization ideas in any reference file.

### 3.1 Preserve the application

The objective is to improve the application, not redefine it. Preserve all existing functionality and declared behavior, including:

- User-facing features and workflows.
- Public and internal API contracts unless a migration is explicitly authorized.
- File formats, import/export behavior and stored user data.
- Authentication, authorization, privacy and security properties.
- Integrations, extension/plugin compatibility and event semantics.
- Keyboard shortcuts, accessibility, localization and user preferences.
- Offline behavior and supported platform compatibility.
- Save, restore, backup, synchronization and recovery behavior.

Never remove, stub out, disable or silently degrade a feature to create a performance improvement. Never change output correctness, media quality, cryptographic guarantees, accessibility or user-selected quality settings merely to improve a benchmark score.

No engineer can prove identical behavior for every possible execution path of a nontrivial program. Therefore the enforceable standard is: **zero known functional regressions; preserve documented and observed behavioral contracts; run relevant automated and manual tests; test important edge cases; measure performance; disclose untested areas; and roll back failed or unsafe changes.** Never promise mathematically proven 100% equivalence when it has not been established.

### 3.2 Inspect before changing

Never speculate about files or behavior that have not been inspected. First identify the actual project root, repository state, uncommitted user changes, architecture, build/test commands and contribution rules. Do not overwrite user work. Do not reset, clean, delete, force-push, publish, deploy, submit a pull request or perform other destructive/external actions without explicit authorization.

### 3.3 Evidence over assumptions

- Measure the real application workload where feasible.
- Prefer official documentation for language, framework, platform, compiler, API and hardware capabilities.
- Distinguish verified facts, benchmark observations, estimates, hypotheses and unknowns.
- Record source, version, date and workload for hardware/database facts.
- Never assume a manufacturer, CPU family, instruction set or GPU vendor is universally superior.
- Never fabricate benchmark data or claim a performance improvement that was not measured.

### 3.4 Safe, reversible changes

Prefer small, independently testable changes. Record a baseline and a rollback point. Use a feature flag or bounded configuration switch for runtime experiments where appropriate. Apply only validated configurations. If a result is uncertain, keep the existing configuration and report the uncertainty.

Ask for approval before material architectural rewrites, new runtime dependencies, schema/data migrations, changes to security/privacy behavior, network telemetry, removal of compatibility support, public contributions, or destructive changes.

### 3.5 Privacy and data minimization

Do not inspect unrelated personal files or application content to infer hardware or performance. Collect only the minimum device and application metrics needed for optimization. Prefer local storage and local processing. Do not transmit telemetry by default. Do not collect serial numbers, account identifiers, browsing content, message content, document contents, passwords, tokens or unrelated personal data. Any external telemetry or cloud service requires explicit developer and user consent, clear disclosure, data minimization, retention controls and secure transport.

## 4. RACE: product and runtime specification

### 4.1 What RACE is

RACE is a developer-integrated, application-internal adaptive optimization engine. It has two halves:

1. **RACE Developer Intelligence:** Claude's development-time workflow that inspects the codebase, chooses relevant expertise, designs and implements tunable application pathways, generates integration code and tests it.
2. **RACE Runtime Engine:** Software integrated into the target application. It observes the host application's workloads, queries permitted hardware capability APIs, evaluates developer-approved application settings and applies validated configurations at runtime.

Claude builds the runtime integration; RACE does not become a general-purpose operating-system tuning utility.

### 4.2 Absolute device-settings prohibition

RACE must never modify the user's:

- BIOS or UEFI settings.
- Firmware.
- CPU/GPU clock, voltage, power limit or fan settings.
- Operating-system power plan or scheduler configuration.
- Registry, kernel settings or system services.
- Graphics driver configuration.
- Global graphics settings.
- Device drivers.
- System-wide environment variables or startup behavior.
- Other applications' settings.

RACE only reads relevant hardware capabilities through supported, permissioned interfaces and changes **the host application's own registered settings, algorithms, workload scheduling, rendering choices, caches, resource budgets or execution paths**.

If a requested tuning action would change a device or OS setting, reject that action and explain that it is outside RACE's scope.

### 4.3 Runtime component model

Design RACE as modular components with interfaces appropriate to the target stack. A conceptual architecture is:

1. **Capability Detector** — discovers CPU architecture, feature flags, core topology when available, GPU/API capabilities, memory availability, storage and runtime/platform features.
2. **Capability Knowledge Base** — versioned, evidence-backed hardware and API records.
3. **Application Workload Profiler** — observes application-owned metrics and task characteristics, not private user content.
4. **Workload Classifier** — classifies operations as CPU-bound, GPU-bound, memory-bound, storage-bound, network-bound, latency-sensitive, throughput-oriented, real-time, mixed or software-algorithm-bound.
5. **Tuning Registry** — an explicit allowlist of application-internal parameters that the developer has exposed for safe adaptation.
6. **Optimization Evaluator** — produces candidate configurations and scores their expected benefit, compatibility, risk and evidence confidence.
7. **Benchmark Coordinator** — runs bounded, relevant tests and compares candidates against a baseline.
8. **Scheduler** — defers invasive tests and configuration changes until safe times; respects foreground activity, application state, thermal conditions and user preference.
9. **Policy Manager** — enforces developer policy, user preference, compatibility, quality limits, safety limits and rollback.
10. **Runtime Adapter** — applies only registered, validated settings through the application's own code.
11. **Local State Store** — stores minimal versioned profiles, last-known-good configuration and benchmark metadata locally by default.
12. **Diagnostics and History** — explains changes, outcomes, confidence, measured impact and rollback events.

This is a conceptual component map, not a requirement to create unnecessary abstractions. Use a simpler architecture when the host application does not need every component.

### 4.4 Tuning registry contract

RACE must not change arbitrary variables, rewrite memory, patch executable code or manipulate undocumented internals at runtime. The developer must expose a controlled registry of tuneable application settings.

Each tunable parameter should describe, where applicable:

- Stable parameter ID and human-readable purpose.
- Type and allowed range or enumerated choices.
- Safe default and fallback.
- Whether it is runtime-adjustable or requires restart/rebuild.
- Workload category it affects.
- Supported platform, framework and capability requirements.
- Dependencies and mutually exclusive choices.
- Quality/correctness constraints.
- Validation function or test.
- Apply and rollback behavior.
- Risk level and whether user confirmation is required.

RACE may only apply settings registered by the developer. Reject out-of-range values, unsupported capabilities, invalid combinations and configurations that fail validation.

### 4.5 Two kinds of adaptation

**Runtime adaptation:** Select among prebuilt, prevalidated algorithms, APIs, rendering paths, model configurations already supported by the app, bounded cache sizes and registered parameters. Runtime adaptation must not rewrite source code or download and execute newly generated code.

**Developer-time adaptation:** Claude may modify source code to add a native architecture path, CPU feature dispatch, GPU backend, improved algorithm, optional acceleration integration or additional tuning parameter. Such changes must be built, tested, retain a portable fallback and pass behavior/performance validation before being considered complete.

### 4.6 Hardware intelligence database

Create a versioned, machine-readable schema for hardware capabilities. Markdown references explain concepts; structured records power capability queries.

Capture relevant fields where available and permitted:

**CPU:** vendor, exact model/family, architecture, generation, microarchitecture, x86-64/ARM64 or other ISA, physical/logical cores, heterogeneous core types, topology, cache hierarchy, supported instructions (such as SSE, AVX, AVX2, AVX-512 subsets, FMA, AES-NI, NEON, SVE/SVE2), vector/matrix capability, memory controller, NUMA features and hardware acceleration.

**GPU:** vendor, exact model, architecture, integrated/discrete status, available graphics/compute APIs, feature levels, shader/compute capabilities, CUDA compute capability where applicable, tensor/matrix and ray-tracing features, VRAM/shared/unified memory characteristics, video encode/decode engines and driver/API compatibility.

**Memory:** RAM type when detectable, capacity and available memory, channels/bandwidth where reliable, memory pressure, unified/shared memory characteristics, application working set and NUMA locality where relevant.

**Storage and I/O:** storage interface/type where detectable, measured sequential and random I/O where relevant, latency, throughput, available capacity, file system and device topology when safely discoverable.

**Platform/runtime:** OS and version, kernel/runtime, process architecture, native or emulated execution, compiler/runtime versions, graphics/compute APIs and driver capability.

**Display/media/AI accelerators:** resolution/refresh/HDR only when relevant; codec and hardware encode/decode capabilities; NPU presence and supported APIs/precision only where exposed.

Do not require every field to be available. Use `unknown` or `unsupported` rather than guessing. Treat advertised specifications as capability hints, not performance results.

### 4.7 Architecture and vendor intelligence

The database and references should cover:

- Intel CPU generations and hybrid P-core/E-core topologies.
- AMD Zen generations, chiplet/CCD topology, cache characteristics and 3D V-Cache where applicable.
- ARM64 implementations including Apple Silicon, Qualcomm and other vendors, with NEON/SVE support where available.
- x86/x86-64 and ARM differences, emulation and native execution.
- NVIDIA GPU architectures and CUDA/Tensor/RT/video capabilities where applicable.
- AMD RDNA and CDNA families, graphics/compute distinctions, ROCm and media capabilities where applicable.
- Intel Xe graphics and media/compute capabilities where applicable.
- Apple GPU/Metal/unified-memory behavior.
- Integrated versus discrete graphics and hybrid graphics routing.
- CPU/GPU combinations, PCIe generation/link width, Resizable BAR/SAM support and memory-transfer behavior.

Do not make simplistic claims such as “AMD CPU + AMD GPU is always better” or “Intel + NVIDIA is worse.” Store exact compatibility conditions and measured workload evidence. A platform feature being supported does not prove a universal performance benefit. Vendor pairing is a hypothesis to test, never an automatic score bonus.

### 4.8 Capability detection and CPU dispatch safety

Use supported OS, compiler, runtime and vendor APIs. Validate both CPU instruction support and OS-enabled execution state before using special instructions. Never infer instruction support from brand/model text alone. Use compiler-supported dispatch, established libraries or explicit feature checks. Every accelerated path must have a correct portable fallback. GPU paths require API/device/driver capability checks and resource-loss handling. If capability detection is unavailable, use the safe baseline implementation.

### 4.9 Hardware evidence records

Every curated hardware fact or performance record should include:

- Hardware model or architecture scope.
- Capability or tested behavior.
- Workload definition.
- Benchmark/tool and version.
- Software/driver/OS versions where relevant.
- Source URL and source type.
- Date obtained or tested.
- Methodology and test conditions.
- Result and units, if measured.
- Confidence label: official specification, independently measured, internally measured, estimated or unknown.
- Data license/provenance where applicable.

Do not fabricate an exhaustive SKU database. Start with a trustworthy extensible schema and a small set of verified representative records. Design update mechanisms for future hardware without hardcoding unsupported facts.

## 5. RACE profiling, benchmarking and scheduling

### 5.1 Three levels of observation

- **Level 1 — Passive observation:** very low-overhead startup timings, application-owned resource metrics and operation timings. No synthetic stress benchmark.
- **Level 2 — Lightweight profiling:** targeted sampling and workload classification with bounded overhead.
- **Level 3 — Active benchmarking:** controlled application-specific workloads and candidate configuration comparisons. This can temporarily affect performance and must be scheduled carefully.

Permission to observe does not imply permission to modify. Permission to profile does not imply permission to run a stress benchmark. Keep these actions separate.

### 5.2 Startup behavior when the application has a loading screen

During an existing loading/splash screen, RACE may perform minimal capability detection and low-cost startup measurements only within a strict time and resource budget. It must not prolong the loading screen to run a benchmark. Record startup timings that the app already knows, such as initialization phase duration and time-to-interactive.

After the application becomes usable, continue passive observation. Schedule deeper profiling and benchmark tests later in a suitable low-activity period. Do not block input, delay first usable screen or compete with a critical loading/streaming phase.

### 5.3 Startup behavior when there is no loading screen

At launch, do only the minimal capability detection that is necessary and inexpensive. Begin with passive observation. Do not run a heavy benchmark during the first 30 minutes of foreground use. Use **30 minutes of cumulative active/foreground application use** as the earliest point at which deeper profiling can be considered. This is a scheduling threshold, not a command to interrupt the user at minute 30. Run the deeper benchmark only when the app is idle or in a demonstrably safe low-activity state.

### 5.4 Daily use and repeat testing

The engine may collect low-overhead application metrics during normal daily use, subject to the app's privacy policy and user preference. Do not run a full 5–10-minute benchmark every day. Run initial calibration once per relevant installation/configuration, then repeat only when justified—for example, a major application update, a meaningful runtime/driver/API capability change, a persistent regression, a changed workload profile or an explicit user request.

### 5.5 Benchmark duration and methodology

Target a total active benchmark session of approximately 5–10 minutes when sufficient relevant tests exist. This is a target, not a mandatory duration. Apps without GPU work must not run GPU stress tests. Use smaller bounded tests that can pause, resume or abort.

Potential test categories:

- CPU single-thread and parallel throughput for actual app workloads.
- Thread contention and scheduling behavior.
- GPU rendering/compute and transfer overhead when used.
- Memory allocation, working set, bandwidth/latency where relevant.
- Storage I/O only when relevant and safe.
- Startup, time-to-interactive and common operation duration.
- Frame times, p95/p99 latency, throughput, error rate and resource footprint.

Methodology requirements:

- Capture a baseline first.
- Warm up JIT/runtime/cache paths where appropriate.
- Repeat tests enough to estimate noise.
- Avoid comparing dissimilar workloads.
- Track thermal and background-load conditions where accessible.
- Use robust statistics and confidence intervals when practical.
- Randomize candidate order or use a controlled crossover design when order effects are material.
- Stop/pause if user activity resumes, thermal conditions become unsafe, battery/energy constraints are reached, or the benchmark impacts the user's work.
- Never run unbounded stress tests.
- Do not claim a result is representative of every use case from a single synthetic test.

### 5.6 Idle detection and scheduling

Prefer app-owned signals such as no active user input, no foreground critical task, no active call/recording/render/export/gameplay/meeting, and safe workload queue state. Do not rely solely on OS “idle” because the app may be performing important background work. Let the developer define critical states. Respect battery-saving/low-power user modes as an app policy signal without changing device settings. Keep the scheduler platform-aware and cancellable.

### 5.7 Notifications and optional manual button

During integration, Claude must ask the developer two explicit decisions:

1. **Should the app expose a manual optimization/benchmark button?** Default recommendation: no; automatic behavior should be sufficient. If the developer chooses yes, integrate a button such as “Benchmark & Optimize” using the app's design system.
2. **Should the app display a small temporary optimization notice?** Default recommendation: yes when a noticeable profiling/benchmark/configuration operation is occurring. If the developer chooses no, honor that choice while preserving user controls through an existing preferences surface or approved app setting.

Example message, adapted to app tone and design:

> Optimizing your app for better performance. You may notice temporary slowdowns while we analyze and adjust its configuration.

Generate wording and presentation that fit the app's visual system, accessibility, localization and notification conventions. Do not show repeated disruptive notices. Passive low-overhead observation does not need a notice. Do not claim improved performance before a successful measurement.

The end user must have a meaningful way to pause or disable automatic profiling/optimization and restore the last-known-good configuration, whether via the manual button, existing app preferences or a developer-approved settings surface. Hiding the optional button must not remove user control.

### 5.8 Runtime optimization profiles

Support developer-defined and, where appropriate, user-selectable profiles such as:

- Balanced (recommended default).
- Maximum responsiveness.
- Maximum throughput.
- Minimum application resource consumption.
- Maximum reliability/stability.
- Minimum package/application size (primarily build-time).
- Custom developer-defined objectives.

Profiles express priorities and constraints; they are not guarantees. A profile must not violate correctness, security, user-selected quality or compatibility.

### 5.9 Optimization result and rollback

Store the original/default and last-known-good configuration. Apply candidate changes through a transaction or staged rollout where feasible. Validate after applying. Roll back automatically if correctness tests fail, errors increase beyond a developer-defined threshold, performance materially regresses or the runtime becomes unstable. Explain what was changed and measured. Keep an audit/history record that can be inspected and cleared according to the app's privacy policy.

## 6. Application-level optimization opportunities

The skill must learn to discover tunable parameters from the actual source code rather than blindly applying generic lists. The following are opportunity catalogs, not universal instructions to change every item.

### 6.1 CPU and processing

Thread-pool sizing; worker count; task chunk sizes; batching; parallelization thresholds; task scheduling; async I/O; work queues; backpressure; SIMD code paths; CPU feature dispatch; algorithm selection; computation caching; object pooling; allocation reduction; incremental computation; lazy evaluation; avoiding redundant work; data locality; serialization; parsing; compression; background task prioritization.

### 6.2 GPU and graphics

Rendering backend; compute backend; supported API path; GPU workload dispatch; rendering resolution and dynamic resolution where user quality policy permits; texture residency/streaming budgets; shader compilation and cache policy; render batching; draw-call reduction; resource reuse; asynchronous compute where supported; CPU/GPU work distribution; image/video filters; GPU memory budgets; device-loss recovery; integrated/discrete GPU choice only where the application and platform expose a legitimate supported choice.

### 6.3 Memory

Application-owned cache budgets; allocation strategies; object/buffer pooling; buffer reuse; virtualized lists; image/tile caching; resource eviction; memory-mapped files where appropriate; working-set reduction; incremental loading; avoiding retained object graphs; garbage-collection pressure reduction; data structure choice; memory locality; bounded caches; leak prevention.

### 6.4 Storage and data

I/O concurrency; read/write buffers; streaming; lazy loading; prefetching; file indexing; database batching; query plans and indexes; cache correctness; compression format/level where compatible; incremental persistence; autosave scheduling; asset unpacking; serialization; archive handling; temporary-file management; delta sync and resumable transfers.

### 6.5 UI and rendering

Avoid unnecessary component re-renders; DOM/layout complexity; virtualization; render scheduling; animation and event frequency; image decoding; canvas/WebGL/WebGPU/WebAssembly paths where supported; UI thread blocking; incremental rendering; lazy component loading; text layout; large-list handling; accessibility-preserving updates.

### 6.6 Networking

Request batching; connection pools; concurrency limits; cache semantics; payload encoding/compression; prefetching only when justified; retry/backoff; deduplication; polling interval; WebSocket message batching; response parsing; cancellation; prioritization; rate-limit compliance; graceful offline handling.

### 6.7 Startup and lifecycle

Lazy initialization; dependency loading; startup critical path; deferred work; resource preloading; cache warmup; background initialization; shutdown cleanup; session restoration; crash recovery; update/migration behavior; application health monitoring.

### 6.8 AI application profiles

If the developer explicitly opts into AI-related optimization or the app already includes an AI pipeline, RACE may profile that existing pipeline. Potential parameters include inference backend, model already supplied by the developer, precision/quantization already supported, batch size, concurrency, CPU/GPU/NPU placement, offloading, KV-cache budget, model-load timing and memory use. Do not add an AI model, vendor integration, agent, network API, new data collection or model dependency without explicit developer choice. Evaluate output quality and correctness alongside latency, throughput and resource use. A faster but materially worse output is not a valid optimization.

## 7. Application-type reference library

Build an indexed, expandable collection of focused references. Every reference should explain: what to inspect; relevant metrics; common bottlenecks; application-level tunable parameters; supported APIs/framework considerations; no-go changes; compatibility risks; tests/benchmarks; and authoritative sources.

At minimum, create references for the categories below. Do not generate hundreds of empty placeholder files. Create useful, substantive references for core categories and a clear index/roadmap for categories that cannot yet be covered in depth.

### 7.1 Desktop and native apps

- General desktop applications.
- Electron applications.
- Tauri applications.
- Native Windows applications (WinUI, WPF, .NET and applicable native APIs).
- Native macOS applications (Swift, SwiftUI, AppKit).
- Linux desktop applications (Qt, GTK and other relevant stacks).
- Cross-platform apps.
- Mobile apps: iOS, Android, Flutter and React Native.
- Progressive web apps and browser extensions.
- CLI/TUI/developer utilities.

### 7.2 Web and browser applications

- Whole websites and web applications.
- Individual pages.
- Landing pages, homepages, product/pricing/checkout/signup/login pages.
- Dashboards, admin panels, forms, search pages and settings pages.
- Blogs, documentation, portfolios, corporate sites, ecommerce, marketplaces and portals.
- Browser engines and browser-like applications.
- Technical SEO only when relevant to the user request; never confuse SEO with runtime performance.
- Core Web Vitals: LCP, INP and CLS, plus lab/field measurement distinctions, long tasks, resource loading, JavaScript, layout, paint and browser scheduling.

### 7.3 Everyday application profiles

- Browsers and browser extensions.
- Games and game launchers.
- Messaging, email, collaboration and video conferencing.
- Office/document editors, spreadsheets, presentations, notes and knowledge bases.
- Calendars, task/project management and booking/scheduling.
- Photo editors, video editors, media players/streaming, audio tools and music production.
- File managers, cloud storage, sync clients, archive tools and download managers.
- Password managers and security software.
- IDEs, code editors, terminals, debuggers, build systems and developer tools.
- Remote desktop, virtual machine and container tools.
- Screenshot, screen recording, clipboard, search and e-book tools.

### 7.4 Backend and infrastructure

Backend systems, APIs, databases, schemas, authentication, authorization, microservices, serverless, cloud infrastructure, DevOps, CI/CD, deployment, observability, caching, networking, real-time and distributed systems, storage, queues, messaging and job processing.

### 7.5 AI and automation profiles (developer-selected only)

AI applications, existing AI agents, LLM integration, prompt systems, RAG, model inference, AI evaluation, workflow orchestration, MCP integrations, Claude Skills, chatbots and AI cost optimization. These references may be consulted when the developer selects them or the project already uses the technology; they must not trigger adding new AI features by default.

### 7.6 Design and business profiles

UI/UX, visual design, typography, color systems, design systems, component libraries, responsive design, accessibility, animation, micro-interactions, ecommerce, shopping carts, payments, subscriptions, CRM/ERP, inventory, marketplaces, conversion, customer retention and business workflows. Use these only where relevant; business growth optimization is not a reason to change product behavior without approval.

### 7.7 Data, games and specialized engineering

Data pipelines, engineering, analytics, visualization, BI, dashboards, experiments, metrics, scientific software, algorithms, embedded systems, IoT, hardware integration, robotics, computer vision, audio/video processing, security engineering, testing and simulations.

## 8. Language, framework, compiler and architecture intelligence

This is a mandatory dimension of project classification. Detect the actual stack from manifests, source files, build configuration, lockfiles, compiler configuration and project documentation. Support mixed-language and monorepo projects; do not force a single-language classification.

### 8.1 Languages

Create practical references for JavaScript, TypeScript, Python, Rust, C, C++, C#, Java, Kotlin, Go, Swift, Objective-C, Dart, PHP, Ruby, Lua, R, Julia and SQL. Add other languages when encountered and relevant.

Each language reference should cover its actual runtime/memory/concurrency model, profiling tools, performance traps, idiomatic optimizations, compiler/build considerations, interoperability and tests. Examples:

- JavaScript/TypeScript: event loop, async I/O, V8/JIT, allocations/GC, module loading, bundle output, DOM/framework rendering.
- Python: profiling, algorithmic cost, allocations, vectorization, native extensions, GIL/free-threaded/runtime-version considerations, process/thread/async tradeoffs.
- Rust: ownership and borrowing, allocations, async runtimes, contention, SIMD, release profile, unsafe-code review and compiler optimizations.
- C/C++: memory layout, cache locality, undefined behavior, vectorization, concurrency, allocator behavior, sanitizers, compiler flags and ABI concerns.
- C#/Java/Kotlin: JIT/AOT, GC, allocation pressure, async/coroutines, object lifetimes, runtime diagnostics and platform-specific execution.
- Go: goroutines, GC, allocations, channels, profiling, scheduler and I/O.
- Swift/Objective-C: ARC, copy-on-write, value semantics, concurrency, UI main-thread behavior and compiler/runtime tools.
- Dart: isolates, async execution, AOT/JIT mode and Flutter rendering if relevant.
- PHP/Ruby: request lifecycle, runtime caches, allocations, concurrency/runtime model and database usage.
- Julia/R: compilation/type stability/vectorization and data/memory handling.
- SQL: query plans, indexing, joins, transactions, locking and execution behavior.

### 8.2 Frameworks and runtimes

At minimum cover React, Next.js, Vue, Angular, Svelte, Node.js, Electron, Tauri, Qt, .NET/WPF, SwiftUI/UIKit, Flutter, React Native, Unity, Unreal Engine, Django, FastAPI, Spring and ASP.NET Core. Add framework references when detected.

### 8.3 Compilers and build systems

Cover relevant toolchains such as Clang/LLVM, GCC, MSVC, Rust/Cargo, CMake, Meson, Bazel, Buck, MSBuild/dotnet, Gradle, Maven, Xcode, Vite, Webpack, Rollup, esbuild and other detected tools.

Investigate incremental builds, dependency graphs, cache correctness, parallelism, tree shaking, code splitting, minification, binary/package size, link-time optimization, profile-guided optimization, AOT and debug-symbol separation. Never blindly turn on aggressive flags. Verify behavior, ABI compatibility, reproducibility, package size and performance.

### 8.4 Architecture patterns

Cover monoliths, modular monoliths, microservices, event-driven systems, message queues, client-server systems, serverless, distributed systems, offline-first/local-first, plugin architectures, multi-tenant systems, real-time, streaming, batch, layered, microkernel, data-oriented, actor and reactive architectures.

Do not recommend a fashionable architecture without evidence. Prefer the simplest architecture that meets real functional, scaling, reliability and delivery requirements.

## 9. Universal `/optimize` specification

`/optimize` is secondary and strictly hardware-independent.

### 9.1 Permitted scope

It may inspect and improve source code, algorithms, data structures, architecture, build configuration, dependency use, database queries, rendering logic, request patterns, startup code, error handling, tests, documentation, accessibility, security, reliability, maintainability and workflow implementation where these are broadly applicable to the project's declared supported environments.

It may use the project's declared target platforms and language/framework versions. It must not use the current user's detected CPU/GPU/RAM/storage specifications to choose implementation tuning values or hardware-specific execution paths.

### 9.2 Prohibited scope

It must not:

- Perform live hardware detection for optimization choices.
- Select CPU/GPU architecture-specific settings based on the user's machine.
- Choose CUDA/ROCm/Metal/DirectML or a device-specific model/backend based on the current user's device.
- Set per-device thread counts or memory budgets.
- Tune graphics quality or hardware-specific rendering settings.
- Modify device, OS, firmware, driver, BIOS or system settings.
- Add AI functionality or integrations without explicit developer selection.
- Invoke RACE implicitly.

### 9.3 Broad-benefit eligibility filter

The user's ambition is to prioritize improvements expected to benefit nearly all users. Do not promise that any change benefits “99.99%” unless representative data establishes that. Use this eligibility test:

- Is the change independent of a specific end-user hardware model?
- Does it improve a general property such as correctness, avoidable work, maintainability, reliability or resource waste?
- Does it preserve declared platform support and behavior?
- Is the benefit supported by evidence or a well-understood invariant?
- Are there meaningful tradeoffs or regressions?
- Can it be tested and rolled back?

Do not optimize for a metric at the expense of another important objective without the developer's stated priority.

### 9.4 Execution behavior

By default, audit first, identify and prioritize opportunities, then implement safe, bounded improvements that are clearly within scope. Ask before high-risk rewrites, feature removals (which should generally be rejected), data migrations, new significant dependencies or irreversible actions. Do not return only recommendations when the user requested optimization and safe changes can be made. Always report what was changed, tests run, measurements obtained, unresolved risks and files touched.

## 10. Developer-selected AI capabilities

AI is not the default optimization solution. During initial RACE integration, ask whether the developer wants any additional AI feature or integration. If the answer is no or unspecified, add none.

Do not independently:

- Add a hosted model API.
- Add a local LLM or NPU model integration.
- Add an agent framework.
- Add AI chat or content-generation features.
- Upload source code, runtime telemetry or user data to AI providers.
- Add model downloads, API keys, cloud billing or new AI dependencies.

If the application already has AI functionality, RACE may optimize that existing pipeline within the developer-approved scope. Selecting a faster existing backend is not permission to introduce a new vendor, model or service. Ask for explicit selection of those capabilities.

## 11. Quality, regression and integrity engine

Create supporting references, checklists and test templates for:

- Baseline capture.
- Functional regression testing.
- Behavioral contract tests.
- API/format compatibility.
- Data integrity and migration checks.
- Security/privacy regression.
- Performance regression.
- Startup and lifecycle tests.
- Accessibility/localization regression.
- Load/stress testing with bounded resource use.
- Crash recovery and rollback.
- Cross-platform compatibility.
- Memory/resource leak checks.

### 11.1 Change impact analysis

Before modifying code, identify impacted modules, callers, APIs, dependencies, workflows and persisted data. After changes, run the most relevant tests and broaden coverage where impact is uncertain. Record test gaps rather than implying full validation.

### 11.2 Automatic rollback

For runtime RACE configuration, preserve a last-known-good profile and apply changes transactionally where feasible. For development-time code edits, use Git diffs and safe checkpoints; never reset or discard user work. Do not autonomously hard-reset a repository. Revert only the skill's own clearly identified changes and only when safe; ask when user work may overlap.

### 11.3 Performance budgets

Allow developers to define budgets such as startup-to-interactive time, p95 operation latency, frame-time targets, memory/VRAM budget, package size, CPU time, network request count and error rate. Budgets are application-specific and must include workload/environment context. They are guardrails, not reasons to break functionality.

### 11.4 Optimization scoring

Score opportunities using at least:

- Expected benefit (and its measurement basis).
- Evidence confidence.
- Scope of affected users/workloads.
- Implementation effort.
- Regression/security/privacy risk.
- Compatibility impact.
- Reversibility.
- Dependency/maintenance cost.

Do not reduce the score to a fabricated precision. Use transparent categories or ranges where evidence is weak.

### 11.5 Explainability and history

For every meaningful change, record: problem, evidence, affected files/parameters, chosen approach, alternatives considered, expected result, measured result, test evidence, confidence, tradeoffs and rollback method. Keep history local unless the developer and user approve external sharing.

## 12. Open-source contribution mode

Open-source support is an important secondary use case. RACE and `/optimize` should be able to improve an existing open-source repository while respecting its maintainers and contributors.

Before changing an external project:

- Read `CONTRIBUTING.md`, project instructions, code style and test guidance.
- Check the project license and contribution terms.
- Review relevant issues/discussions and existing implementation patterns.
- Identify whether the change fits project scope and maintainer priorities.
- Preserve project-specific conventions and compatibility guarantees.

For proposed contributions:

- Keep patches focused and reviewable.
- Avoid unnecessary rewrites or new dependencies.
- Include tests and benchmark evidence where appropriate.
- Explain the problem, fix, tradeoffs and measured impact.
- Disclose AI assistance if the project requires it.
- Do not push branches, publish releases, comment on issues or submit a PR without explicit user authorization.

Do not add RACE to an open-source project unless the project maintainer/developer has selected that integration. Do not assume an open-source license permits every form of reuse or redistribution of code, test data or benchmark data.

## 13. Self-expanding knowledge base

The skill should detect knowledge gaps when it encounters a new language, framework, hardware architecture, workload or application category.

Workflow:

1. Identify the exact gap and why it matters.
2. Research current official documentation first, then standards, source code, reputable technical publications and reproducible benchmarks.
3. Record source URL, publication/update date, software/hardware version, access date and relevant conditions.
4. Separate confirmed facts from hypotheses and opinions.
5. Draft or update a reference file using the standardized format.
6. Validate the claims and check licensing/provenance.
7. Keep the new material as a proposed local knowledge update or include it in the current package only when appropriate; never silently rewrite a published shared knowledge base or send data externally.

The knowledge base must be version-aware and periodically review stale references. A source being official does not mean every recommendation is applicable to every project.

## 14. Standard format for every reference file

Each substantive reference should use this structure:

1. Purpose and applicability.
2. Detection signals: files, manifests, APIs, architecture indicators.
3. What to inspect.
4. Relevant performance and correctness metrics.
5. Common bottlenecks and anti-patterns.
6. Candidate optimization techniques.
7. Runtime tunables versus build-time/code changes.
8. Hardware-dependent decisions (RACE only) versus universal changes (`/optimize`).
9. Compatibility and version considerations.
10. Security, privacy, accessibility and data-integrity constraints.
11. Validation and benchmark methodology.
12. Rollback considerations.
13. Authoritative sources and last-reviewed date.

Do not pad references with generic advice. Include concrete, stack-specific guidance and cite official documentation or reproducible evidence when available.

## 15. Recommended package structure

The exact structure may be adjusted if a simpler layout better fits the built skill, but preserve the separation and discoverability below:

```text
ultra-optimizer/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── progress.md
├── docs/
│   ├── PRODUCT_ARCHITECTURE.md
│   ├── RACE_RUNTIME_SPEC.md
│   ├── HARDWARE_DATA_SCHEMA.md
│   ├── PRIVACY_AND_SAFETY.md
│   ├── OPEN_SOURCE_CONTRIBUTIONS.md
│   └── BUILD_AND_RELEASE.md
├── .claude/
│   └── skills/
│       ├── race/
│       │   ├── SKILL.md
│       │   ├── references/
│       │   │   ├── core/
│       │   │   ├── hardware/
│       │   │   ├── workloads/
│       │   │   ├── applications/
│       │   │   ├── languages/
│       │   │   ├── frameworks/
│       │   │   ├── architectures/
│       │   │   ├── benchmarks/
│       │   │   └── quality/
│       │   ├── schemas/
│       │   ├── templates/
│       │   ├── scripts/
│       │   └── evals/
│       └── optimize/
│           ├── SKILL.md
│           ├── references/
│           ├── checklists/
│           └── evals/
├── install/
│   ├── install.sh
│   ├── install.ps1
│   ├── uninstall.sh
│   └── uninstall.ps1
└── tests/
    ├── validate_skill_structure.py
    ├── validate_schemas.py
    ├── test_installers/
    └── eval-cases/
```

If a folder is not populated yet, do not leave dozens of empty folders. Create it when its first substantive content is ready. Keep hardware records in JSON/YAML with schema validation; use Markdown for explanations and procedures.

## 16. RACE integration workflow when `/race` is later used in a target application

The `/race` skill must support the following modes. If the user supplies an argument, follow it. If no argument is supplied, inspect the project and choose the most sensible behavior, explaining the detected state.

- `audit`: read-only assessment of whether and how RACE could fit the app; no code changes.
- `build` / `integrate`: design and implement an initial RACE integration.
- `benchmark`: run the existing app's defined benchmarks or explain what's missing; do not invent a benchmark result.
- `status`: report current RACE integration, active profile, recent observations and missing capabilities, without exposing sensitive data.
- `improve`: improve an existing RACE implementation while preserving its public contract.
- `review`: inspect a RACE patch/configuration for safety, correctness and performance.

Default `/race` workflow:

1. Inspect the repository, uncommitted changes, project docs, license, language/framework/build/test setup.
2. Classify app types, languages, frameworks, architecture and target platforms; support multiple classifications.
3. Identify existing profiling, settings, telemetry, logging, benchmark and feature-flag mechanisms.
4. Identify real application workloads and possible bottlenecks. Do not infer bottlenecks solely from hardware specifications.
5. Load only the relevant references.
6. Produce a concise integration design and identify developer decisions that require approval, including the optional manual button and optional notice.
7. Ask the developer whether any additional AI features are wanted; default to none.
8. Define a minimal tuning registry and safe fallback behavior.
9. Implement capability detection using supported APIs for the target stack.
10. Implement passive profiling and startup-aware scheduling.
11. Implement the bounded benchmark coordinator only where the app has meaningful test workloads.
12. Implement adaptive selection, profile storage, user controls and rollback.
13. Add tests for capability fallbacks, invalid configurations, cancellation, privacy defaults, workload transitions and rollback.
14. Build and run the app; validate behavior using real workflows, not tests alone when UI/runtime verification is available.
15. Measure before/after performance and report actual results and uncertainty.
16. Document installation, tuning parameters, supported platforms, privacy behavior and limitations.

If the project cannot support a safe RACE runtime because required APIs or tunable parameters do not exist, report the limitation and implement only the parts that are actually supportable. Do not create a fake or decorative “optimization engine.”

## 17. Universal `/optimize` workflow

1. Read project instructions and inspect current state.
2. Identify project purpose, target environments, language/framework, architecture and critical workflows.
3. Build a baseline of current tests, diagnostics and relevant performance data where available.
4. Scan for broadly applicable, device-independent opportunities.
5. Exclude hardware-specific, model/backend-selection and device-profile changes.
6. Score opportunities by impact, confidence, effort, risk and reversibility.
7. Reject changes that remove functionality or compromise important guarantees.
8. Implement safe high-value changes in small increments.
9. Run targeted tests after each meaningful change and broader regression tests at the end.
10. Compare performance only under comparable workloads and conditions.
11. Roll back a failed change safely; never discard unrelated user work.
12. Report changes, evidence, test results, performance outcomes, tradeoffs and remaining opportunities.

## 18. Evaluation and acceptance tests

Build an evaluation suite with realistic prompts and sample project fixtures. Evaluate both **trigger behavior** and **execution quality**.

### 18.1 Command-routing tests

Expected:

- “Optimize this desktop application for different hardware” routes to `/race` or RACE-first guidance.
- “Add adaptive GPU/CPU workload selection to this app” routes to `/race`.
- “Run a universal code cleanup with no device-specific tuning” routes to `/optimize` when explicitly invoked.
- `/optimize` never performs live hardware-based configuration selection.
- `/optimize` never silently invokes RACE.
- “Add an AI agent to the application” does not trigger automatic implementation; it requires developer selection and scope approval.

### 18.2 Project-classification fixtures

Test at least:

- Electron + React + TypeScript + SQLite desktop app.
- Browser-based React/Next.js application.
- Native Rust application.
- Python data/desktop tool.
- C++/Qt desktop application.
- Flutter mobile application.
- Unity game.
- Browser or browser-like application.
- Messaging/email client.
- Media editor.
- Multi-language monorepo.

Expected: multiple relevant references are selected; irrelevant profiles are not loaded; unknown stack elements are identified rather than guessed.

### 18.3 RACE runtime tests

Where a runtime prototype exists, test:

- Missing hardware API returns `unknown` and safe fallback is used.
- No GPU does not trigger GPU benchmark code.
- Unsupported CPU instruction path is never executed.
- GPU driver/API mismatch falls back safely.
- Invalid/out-of-range tuning values are rejected.
- Benchmark pauses when user activity resumes.
- Benchmark aborts on configured safety thresholds.
- No-loading-screen schedule waits until 30 minutes of cumulative foreground use before considering deeper profiling.
- Loading-screen path never delays time-to-interactive for heavy benchmarking.
- No full benchmark is forced daily.
- User pause/disable controls are honored.
- Last-known-good profile can be restored.
- No device/OS/firmware settings are modified.
- No telemetry leaves the device without explicit consent.

### 18.4 Behavior and quality tests

- Existing tests are preserved; do not delete or weaken tests to make a patch pass.
- Critical workflows remain functional.
- API and file-format compatibility is tested where relevant.
- Data migrations have backup/rollback tests.
- Security and privacy constraints remain intact.
- Performance gains are measured rather than assumed.
- A performance regression causes a fail, explanation or rollback according to policy.

### 18.5 Skill packaging tests

- Both `SKILL.md` files have valid YAML frontmatter.
- Directory and command names resolve as `/race` and `/optimize` in a Claude Code test session.
- Supporting references can be found from both skills.
- The RACE and optimize skill bodies stay concise and link to detailed resources.
- Installer scripts preserve unrelated skill directories.
- README installation steps are reproducible.
- Run current Claude Code skill validation commands if available; note the CLI version used.

### 18.6 Skill quality evaluations

Create realistic should-trigger and should-not-trigger cases. Use fresh sessions for evaluation so authoring context does not hide missing instructions. Compare skill-enabled behavior against a no-skill baseline when practical. Grade command selection, preservation of the RACE/optimize separation, evidence quality, implementation correctness, regression handling and privacy. Record results and version the evaluations.

## 19. Build plan and deliverables

Build in this order:

**Phase 1 — Foundation**
- Create project documentation and exact skill directories.
- Write concise, valid `/race` and `/optimize` `SKILL.md` entry points.
- Add command-routing and non-negotiable rules.
- Create the initial knowledge index.

**Phase 2 — RACE core specification**
- Write the runtime architecture reference.
- Define hardware capability schema and example records.
- Define workload schema and tuning registry schema.
- Define scheduler, profiling, benchmark, policy and rollback contracts.

**Phase 3 — Reference library**
- Add useful core references for CPU, GPU, memory, storage, workload classes, app profiles, languages, frameworks, architectures, compilers and quality engineering.
- Prioritize breadth of accurate coverage without shallow placeholder content.
- Record official sources and review dates.

**Phase 4 — Runtime templates and tools**
- Add stack-neutral contracts and only those starter templates/scripts that are genuinely reusable.
- Avoid pretending one implementation works for every language/framework.
- Add schema validators and reference-index validation.

**Phase 5 — Universal optimizer**
- Write the strict hardware-independent workflow and supporting checklists/references.
- Add routing guardrails preventing device-specific work from leaking into `/optimize`.

**Phase 6 — Install, evaluate and package**
- Build safe installers and manual installation documentation.
- Run all available structural/schema/evaluation tests.
- Report what is actually validated and what remains untested.

### Required final deliverables

At minimum:

- Working `/race` skill.
- Working `/optimize` skill.
- Indexed, modular reference library.
- RACE architecture/runtime specification.
- Versioned hardware and workload schemas.
- Application tuning registry contract.
- Benchmark/scheduler/rollback specifications.
- Developer decision checklist for optional button, notice and AI features.
- Privacy and safety policy.
- Open-source contribution guidance.
- Installation/update/uninstall instructions and scripts.
- Evaluation cases and validation scripts.
- README and progress report.

## 20. Completion report format

When finished, tell the user:

1. What was created and where.
2. How to invoke `/race` and `/optimize`.
3. How to install the skills personally or in a project.
4. Which reference categories are substantive and which remain on the roadmap.
5. Which checks/tests actually ran and their results.
6. Which platform installers/runtime examples were actually tested.
7. Important limitations and decisions still requiring a developer when RACE is integrated into a real app.

Do not say “complete,” “fully working,” “100% tested” or “production-ready” unless the evidence supports that exact claim.

---

## Appendix A — Suggested initial reference index

Start with these files, then expand using the standardized format in Section 14.

```text
.claude/skills/race/references/
├── core/
│   ├── race-overview.md
│   ├── project-detection.md
│   ├── workload-analysis.md
│   ├── tuning-registry.md
│   ├── profiling-levels.md
│   ├── scheduling-and-idle-detection.md
│   ├── benchmarking-methodology.md
│   ├── adaptive-selection.md
│   ├── privacy-and-consent.md
│   ├── rollback-and-recovery.md
│   └── developer-integration-decisions.md
├── hardware/
│   ├── cpu-intelligence.md
│   ├── intel-cpu-architectures.md
│   ├── amd-cpu-architectures.md
│   ├── arm64-and-apple-silicon.md
│   ├── instruction-sets-and-dispatch.md
│   ├── gpu-intelligence.md
│   ├── nvidia-gpu-architectures.md
│   ├── amd-gpu-architectures.md
│   ├── intel-and-apple-gpus.md
│   ├── cpu-gpu-pairing.md
│   ├── memory-intelligence.md
│   ├── storage-and-io.md
│   ├── platform-and-runtime.md
│   ├── thermal-and-sustained-performance.md
│   ├── display-and-media-capabilities.md
│   └── ai-accelerators.md
├── workloads/
│   ├── cpu-bound.md
│   ├── gpu-bound.md
│   ├── memory-bound.md
│   ├── storage-bound.md
│   ├── network-bound.md
│   ├── latency-sensitive.md
│   ├── throughput-oriented.md
│   ├── real-time.md
│   └── mixed-workloads.md
├── applications/
│   ├── desktop-apps.md
│   ├── electron-apps.md
│   ├── tauri-apps.md
│   ├── browsers-and-browser-engines.md
│   ├── websites-and-core-web-vitals.md
│   ├── games-and-game-launchers.md
│   ├── messaging-and-email.md
│   ├── office-and-productivity.md
│   ├── photo-video-and-audio.md
│   ├── file-and-cloud-sync-apps.md
│   ├── password-and-security-apps.md
│   ├── developer-tools-and-ides.md
│   ├── calendars-and-download-managers.md
│   ├── databases-and-data-tools.md
│   ├── ai-applications.md
│   └── engineering-and-scientific-apps.md
├── languages/
│   └── [one focused reference per detected/important language]
├── frameworks/
│   └── [one focused reference per detected/important framework]
├── architectures/
│   └── [one focused reference per relevant architecture]
├── compilers-and-build/
│   ├── compiler-optimization.md
│   ├── build-caching-and-incremental-builds.md
│   ├── link-time-and-profile-guided-optimization.md
│   └── binary-and-package-size.md
└── quality/
    ├── functionality-preservation.md
    ├── regression-testing.md
    ├── performance-budgets.md
    ├── change-impact-analysis.md
    ├── data-integrity.md
    ├── compatibility.md
    └── observability-and-explainability.md
```

## Appendix B — Suggested schemas

Create JSON Schema files for at least:

- `hardware-capability.schema.json`
- `hardware-benchmark.schema.json`
- `workload-profile.schema.json`
- `tunable-parameter.schema.json`
- `application-optimization-profile.schema.json`
- `optimization-result.schema.json`

Keep schema fields explicit and versioned. Support unknown/unavailable values without inventing defaults. Validate example records in CI or with the supplied validation script.

## Appendix C — Developer integration questions

When RACE is integrated into an actual application, ask the developer:

1. Should the app expose an optional manual **Benchmark & Optimize** button? Recommended default: no.
2. Should the app show a small temporary notice during potentially noticeable optimization work? Recommended default: yes.
3. Does the developer want any additional AI features or integrations? Default: no AI additions.
4. Which user-facing performance/quality objectives matter most, and what must never be traded away?
5. Which platforms and versions are officially supported?

Do not ask all questions again if the project already documents the decisions. Ask only the missing questions needed for safe implementation. The application must still offer an appropriate way for users to pause/disable automatic profiling and restore a safe profile even if the optional button is not included.

## Appendix D — Current official references for Claude Code skill construction

Verify these pages again when implementing because Claude Code evolves:

- Claude Code Skills documentation: https://code.claude.com/docs/en/skills
- Skill frontmatter, names, supporting files and command invocation are documented in the Skills guide.
- Claude Code settings and permissions: https://code.claude.com/docs/en/settings
- Claude Code getting started: https://code.claude.com/docs/en/getting-started

Use current official documentation as the source of truth if a detail in this build specification conflicts with a newer Claude Code release. Preserve the product requirements and command names while adapting only the packaging mechanics.
