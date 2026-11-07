---
name: race
description: Build, integrate, audit, benchmark, and improve RACE (Runtime Adaptive Configuration Engine), the hardware-aware application optimization engine. Use for application optimization that adapts application-internal behavior to detected hardware capabilities and real workloads, for example adaptive CPU/GPU path selection, thread and cache budgets, bounded benchmarking, and safe rollback inside an app. Not for changing device, OS, driver, BIOS or firmware settings, and not for generic hardware-independent cleanup (that is the separate /optimize command).
argument-hint: [build|audit|benchmark|status|improve|integrate|review]
---

# /race: Runtime Adaptive Configuration Engine

RACE makes an application adapt its OWN behavior (registered settings, algorithms, scheduling, caches, budgets, code paths) to the hardware it runs on and the workloads it really executes. It is built into the target application, inspected by evidence, and always reversible.

Requested mode: `$ARGUMENTS`
If the line above is empty, inspect the project and pick the most sensible mode, and say which mode you chose and why.

## Non-negotiable rules

1. **Never change the device.** No BIOS/UEFI, firmware, clocks, voltage, power or fan, OS power plan or scheduler, registry/kernel/services, driver or global graphics settings, system-wide environment or startup items, or other apps' settings. RACE only reads capabilities through supported, permissioned interfaces and changes the host app's own registered tunables. Reject requests to tune the device as out of scope. Details: [references/core/race-overview.md](references/core/race-overview.md).
2. **Preserve the application.** Zero known functional regressions; keep documented and observed contracts (features, APIs, file formats, security, privacy, accessibility, localization, offline, sync). Never remove, stub or degrade a feature or quality setting to win a benchmark. Never claim proven 100% equivalence.
3. **Evidence over assumption.** Measure. Label each claim as verified fact, benchmark, estimate, hypothesis or unknown. Never fabricate benchmark data. Hardware specs are hints, not performance results. Unknown stays `unknown`.
4. **Safe fallback always.** Every accelerated path needs a correct portable fallback. No detection means safe baseline.
5. **Privacy by default.** Local only, no telemetry unless the developer explicitly opts in with disclosure and retention controls.
6. **AI features are opt-in.** Add no model, hosted API, agent, or AI dependency unless the developer explicitly selects it. Optimizing a pre-existing AI pipeline is in scope; adding a new vendor, model or service is not.
7. **Stay separate from /optimize.** `/race` is for hardware-aware adaptation. Universal, device-independent cleanup belongs to the separate `/optimize` command; do not call or imitate it here, and tell the user to run it explicitly if that is what they need.
8. **No destructive or external actions** (reset, clean, force-push, publish, deploy, PR, telemetry upload) without explicit authorization. Inspect first; never discard the user's uncommitted work.

## Mode routing

| Mode | What to do |
|---|---|
| `audit` | Read-only fit assessment. No code changes. |
| `build` / `integrate` | Design and implement an initial RACE integration (workflow below). |
| `benchmark` | Run the app's existing defined benchmarks, or explain exactly what is missing. Never invent results. |
| `status` | Report integration state, active profile, recent observations, missing capabilities. Expose no sensitive data. |
| `improve` | Improve an existing RACE implementation while preserving its public contract. |
| `review` | Review a RACE patch/config for safety, correctness, performance. |
| (empty or free text) | Inspect, choose the mode, explain the detected state. |

## Default workflow (build / integrate)

1. Inspect repo state, uncommitted changes, docs, license, language/framework/build/test setup. See [project-detection](references/core/project-detection.md).
2. Classify app types, languages, frameworks, architecture, platforms (multiple allowed). Use [references/INDEX.md](references/INDEX.md) to select references.
3. Find existing profiling, settings, telemetry, logging, benchmark and feature-flag mechanisms.
4. Identify real workloads and bottlenecks. Never infer bottlenecks from hardware specs alone. See [workload-analysis](references/core/workload-analysis.md).
5. Load only relevant references (routing table below).
6. Produce a concise integration design and list decisions needing developer approval. See [developer-integration-decisions](references/core/developer-integration-decisions.md): optional manual "Benchmark & Optimize" button (recommended default: no), small temporary optimization notice (recommended default: yes), additional AI features (default: none), objectives that must never be traded away, supported platforms. Skip questions the project already answers.
7. Define a minimal tuning registry with safe defaults. See [tuning-registry](references/core/tuning-registry.md) and [schemas/](schemas/).
8. Implement capability detection with supported APIs for the stack. See the hardware references listed in [references/INDEX.md](references/INDEX.md).
9. Implement passive profiling and startup-aware scheduling. See [profiling-levels](references/core/profiling-levels.md), [scheduling-and-idle-detection](references/core/scheduling-and-idle-detection.md).
10. Implement the bounded benchmark coordinator only where the app has meaningful test workloads. See [benchmarking-methodology](references/core/benchmarking-methodology.md).
11. Implement adaptive selection, profile storage, user controls (pause/disable auto profiling, restore last-known-good) and rollback. See [adaptive-selection](references/core/adaptive-selection.md), [rollback-and-recovery](references/core/rollback-and-recovery.md).
12. Add tests: capability fallbacks, invalid config, cancellation, privacy defaults, workload transitions, rollback. Use [templates/](templates/) contracts.
13. Build and run the app; verify real workflows, not tests alone when runtime verification is possible.
14. Measure before and after; report actual results and uncertainty.
15. Document install, tunables, platforms, privacy behavior, limitations.

If the app lacks the APIs or tunable parameters for a safe runtime, report that and implement only what is genuinely supportable. Do not build a decorative "optimization engine".

## Timing rules (summary; full text in the profiling and scheduling references)

- Loading screen: only minimal capability detection and startup timings, within a strict budget. Never prolong loading.
- No loading screen: passive observation only; no heavy benchmark before 30 minutes of CUMULATIVE foreground use, and then only when idle and safe.
- Daily use: low-overhead metrics, no daily full benchmark. Re-calibrate only on major app update, runtime/driver/API capability change, persistent regression, changed workload profile, or explicit user request.
- Benchmark target roughly 5 to 10 minutes of active work, bounded, pausable, abortable.

## Reference routing (load only what applies)

| Need | Load |
|---|---|
| Overview, boundaries | references/core/race-overview.md |
| Which references apply | references/INDEX.md |
| CPU, ISA, dispatch | references/hardware/cpu-intelligence.md, instruction-sets-and-dispatch.md; vendor files only if relevant |
| GPU | references/hardware/gpu-intelligence.md plus the vendor file for the detected GPU |
| Memory, storage, platform, thermal, media, NPU | matching file in references/hardware/ |
| Workload class | one file in references/workloads/ |
| App category | one file in references/applications/ |
| Language / framework / architecture / build | matching file in references/languages, frameworks, architectures, compilers-and-build |
| Testing, budgets, data, compatibility | references/quality/ |
| Extend knowledge | references/core/knowledge-expansion.md |
| Contributing to someone else's project | references/core/open-source-contribution.md |

Schemas live in [schemas/](schemas/) (validate records with `scripts/validate_records.py`). Stack-neutral contracts and an executable reference model live in [templates/](templates/); they are contracts to adapt, not universal runtime code.

## Reporting

After work, report: files changed, tests run and results, measurements with workload and conditions, confidence labels, untested areas, risks, rollback method, and decisions still needing the developer. Do not say "complete" or "production-ready" unless evidence supports exactly that claim.
