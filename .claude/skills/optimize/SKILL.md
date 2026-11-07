---
name: optimize
description: Perform universal, device-independent code and engineering optimization while preserving existing application behavior and functionality.
argument-hint: [audit|apply|review|report]
disable-model-invocation: true
---

# /optimize: Universal, device-independent optimization

This command improves source, algorithms, data structures, architecture, build configuration, dependencies, queries, rendering logic, request patterns, startup code, error handling, tests, docs, accessibility, security, reliability and maintainability, for the application's DECLARED supported environments, without changing what the application does.

Requested mode: `$ARGUMENTS`
If the line above is empty, run `audit` first and propose what `apply` would change.

## Hard boundaries

1. **No live hardware-based decisions.** Do not detect the user's CPU/GPU/RAM/storage to choose settings. Do not pick CPU- or GPU-architecture-specific paths from the current machine, choose CUDA/ROCm/Metal/DirectML or any device-specific model/backend, set per-device thread counts or memory budgets, or tune graphics quality. Declared target platforms and versions (from the project's own support policy) are fine.
2. **Never change the device.** No device, OS, firmware, driver or BIOS settings.
3. **Do not invoke or imitate the hardware-aware engine.** If the user wants hardware-adaptive runtime behavior, tell them to run the separate `/race` command explicitly. Do not run it yourself.
4. **No unrequested AI.** Add no AI feature, model, agent, service or dependency without explicit developer selection. Optimizing a pre-existing AI pipeline's device-independent code is allowed.
5. **Preserve behavior.** Zero known functional regressions; keep documented and observed contracts (APIs, file formats, auth, privacy, security, integrations, accessibility, localization, offline, sync). Never remove or degrade a feature, quality setting or safeguard for speed. Never promise proven equivalence.
6. **Evidence over assumption.** Measure; never fabricate numbers; never promise a specific benefit percentage without data.
7. **Safe and reversible.** Small increments, a baseline, a rollback point. No destructive or external actions (reset, clean, force-push, publish, deploy, PR) without authorization. Never discard the user's unrelated work.

## Broad-benefit eligibility filter

Implement a change only if all six answers are acceptable. Full text: [references/eligibility-filter.md](references/eligibility-filter.md).

1. Is it independent of any specific hardware model?
2. Does it improve a general property (time, memory, size, reliability, clarity)?
3. Does it preserve platform support and behavior?
4. Is there evidence or an invariant supporting it?
5. Are the tradeoffs stated?
6. Can it be tested and rolled back?

If a good idea fails question 1, record it as "hardware-dependent, out of scope, see /race" and move on.

## Workflow

1. Read project instructions; inspect repo state and uncommitted changes. See [references/workflow.md](references/workflow.md).
2. Identify purpose, target environments, stack, architecture, critical workflows.
3. Baseline: existing tests, diagnostics, relevant performance data. Use [checklists/baseline-capture.md](checklists/baseline-capture.md).
4. Scan for broadly applicable opportunities using [references/opportunity-catalog.md](references/opportunity-catalog.md) and the stack notes in [references/stacks.md](references/stacks.md).
5. Exclude hardware-specific, model/backend-selection and device-profile changes.
6. Score by impact, confidence, effort, risk, reversibility. See [references/scoring.md](references/scoring.md).
7. Reject changes that remove functionality or weaken guarantees.
8. Implement safe, high-value changes in small increments (mode `apply` only).
9. Run targeted tests after each meaningful change, broader regression at the end. Use [checklists/regression-checklist.md](checklists/regression-checklist.md).
10. Compare performance only under comparable workloads and conditions. See [checklists/performance-comparison.md](checklists/performance-comparison.md).
11. Roll back a failed change safely, touching only your own changes. See [checklists/rollback.md](checklists/rollback.md).
12. Report changes, evidence, tests, performance, tradeoffs, remaining opportunities. See [references/reporting.md](references/reporting.md).

## Modes

| Mode | Behavior |
|---|---|
| `audit` | Read-only: baseline, ranked opportunities, rejected items with reasons. No edits. |
| `apply` | Implement approved or clearly safe items. Ask before high-risk rewrites, feature removals (generally rejected), data migrations, significant new dependencies, irreversible actions. |
| `review` | Review an existing diff or change set against these rules. |
| `report` | Summarize prior work: changes, evidence, test results, remaining items. |

When the user asked for `apply`, do the work with the checks above instead of only recommending.

## Checklists and references (load as needed)

- Checklists: [baseline-capture](checklists/baseline-capture.md), [regression-checklist](checklists/regression-checklist.md), [security-privacy-regression](checklists/security-privacy-regression.md), [performance-comparison](checklists/performance-comparison.md), [rollback](checklists/rollback.md), [compatibility-and-data](checklists/compatibility-and-data.md)
- References: [opportunity-catalog](references/opportunity-catalog.md), [stacks](references/stacks.md), [scoring](references/scoring.md), [reporting](references/reporting.md), [open-source-contribution](references/open-source-contribution.md)

## Reporting

Report: what changed and where, evidence, tests run and results, measurements with conditions, tradeoffs, risks, rollback method, files touched, untested areas, remaining opportunities. Do not say "complete" or "production-ready" unless evidence supports exactly that claim.
