---
name: server-optimize
description: Optimize the server and backend side of an application, and act as the shared server-intelligence library for the other Ultra Optimizer commands. Starts with ONE consolidated configuration intake (deployment mode, environments, hosting, runtime, datastores, priorities, workload, access level, scope, constraints), detects deployment targets from repository files, then audits request handling, concurrency, memory, databases, caching, queues, containers, Kubernetes, serverless, reliability, security and cost. Repository-only by default; live access and any production change need explicit authorization. Never changes server OS, firmware, drivers or infrastructure on its own.
argument-hint: [optional scope: e.g. api latency | database queries | docker image | kubernetes manifests | cold starts]
disable-model-invocation: true
---

# /server-optimize: server and backend optimization

This command orchestrates three lenses over server-side code and configuration, using one shared library of references, schemas and detection tooling in this skill:

1. **Universal lens** (what `/optimize` does): device-independent fixes to algorithms, queries, caching correctness, resource handling, concurrency safety.
2. **Hardware-aware lens** (what `/race` does): application-level choices from VERIFIED server capabilities, such as worker counts, memory budgets, cache sizes and database pool sizes, bounded by developer-approved limits.
3. **Network-aware lens** (what `/ping-optimize` does): attribute latency to server processing versus network, and improve connection behavior and payloads.

It applies these lenses itself. It may recommend running the sibling commands but never invokes them automatically. No AI features are introduced unless the developer explicitly selects them.

Requested scope: `$ARGUMENTS`
If empty, audit the whole backend. If a scope is named, restrict analysis to it (after the intake).

## Non-negotiable rules

1. **Intake first, once.** Before any analysis, run the consolidated intake (see below). Do not scatter ordinary configuration questions through the workflow. Ask again later only for a genuinely new critical unknown or an authorization that did not exist at intake time.
2. **Repository-only by default.** No live system is contacted until the developer grants a higher access level for a named environment. Levels, lowest to highest: repo-only, read-only infrastructure, read-only runtime metrics, staging profiling, authorized staging modifications, authorized production modifications.
3. **Never without explicit authorization:** restart production services, change production infrastructure, run database migrations, scale infrastructure, modify firewall rules, deploy code, change backup or retention configuration.
4. **Never modify** the server's operating system, kernel, BIOS, firmware, drivers or hardware settings, and never modify cloud or infrastructure settings automatically.
5. **Secrets.** Never ask for, accept, print, log or store secrets, tokens, keys, cookies or connection strings. Use only the developer's existing secret mechanism, with read-only identities where possible. Detection never opens `.env`, key, credential, tfstate or kubeconfig files.
6. **Detected is not verified.** Repository evidence says what is configured, not what runs. Never state a production region, instance size or running configuration as fact unless the developer provided it or a read-only live check verified it. Label every fact: detected-from-repository, developer-provided, verified-live or unknown.
7. **Preserve behavior.** Keep features, API contracts, authentication, authorization, data integrity, security guarantees and every supported deployment environment. Never weaken TLS or security for speed. Never blindly retry non-idempotent operations.
8. **Measure honestly.** Baseline first, repeated measurements, percentiles. Never invent numbers. Label results measured, estimated or unverified. Active load only against owned or explicitly authorized, non-production-by-default targets, bounded and cancellable.
9. **Reversible.** Small reviewable changes with a rollback point. If validation fails, automatically roll back changes this workflow made, when rollback is safe and inside the authorized scope; otherwise stop and report.
10. **No hidden machinery.** No background agents, new telemetry or runtime monitoring without explicit developer authorization and documented user controls.

## Workflow

### Step 0: Consolidated intake (mandatory, one batch)
1. Run `python3 scripts/detect_deployment.py PROJECT_ROOT --intake` from this skill's directory (use the real project root; quote paths with spaces). It is read-only and offline.
2. Present all ten items together with detected values prefilled and each marked with its source: (1) automatic detection, custom deployment or local-only; (2) environment(s): development, staging, production, multiple; (3) hosting provider and location; (4) runtime, language, architecture, infrastructure; (5) databases, caches, queues, external services; (6) priorities; (7) workload and traffic; (8) access level; (9) analysis scope: repository-only, read-only live, authorized implementation; (10) constraints: downtime, migrations, spending.
3. Prefer the native interactive question tool. It allows at most four questions per call, so send the choice-type items as back-to-back calls with nothing in between, and collect free-text items in one plain-text block. If interactive input is unavailable, print the whole intake as one text form with the prefilled values and wait for a single reply. Every item accepts "unknown" and "not applicable". Do not block on unknowns.
4. Record the answers as a deployment profile (`schemas/deployment-profile.schema.json`; examples in `schemas/examples/`). Validate it with `python3 scripts/validate_records.py schemas/deployment-profile.schema.json PROFILE.json`. In custom mode the developer's values replace detection; multiple environments and targets are supported.
5. Defaults when unanswered: mode automatic if anything was detected, otherwise local-only; access repo-only; scope repository-only.

### Step 1: Map the backend
Identify entry points, request paths, datastores, caches, queues, background jobs and external calls. Load only the shared references for components actually present (see the index).

### Step 2: Baseline
Use existing metrics, logs and traces first. Add bounded measurement only at the granted access level. Follow `references/deployment/workload-profiling.md`.

### Step 3: Diagnose
Attribute time per request stage and per component. Separate network time from server processing time. Separate warm from cold starts.

### Step 4: Discover and prioritize
List opportunities. Rank by expected impact, evidence confidence, effort, regression risk, security and compatibility, and the developer's stated priorities and constraints.

### Step 5: Implement (only when scope is authorized implementation)
Make focused changes. Universal fixes first, then hardware-aware changes through an explicit, bounded policy (`references/deployment/runtime-adaptation.md`), then network-aware changes. Environment changes beyond the repository need the matching access level for that environment.

### Step 6: Validate and roll back
Run behavior, contract, security and data-integrity tests, then representative load. Follow `references/deployment/validation-and-rollback.md`. Restore the previous state if validation fails.

### Step 7: Report
Deployment profile used (with sources of each fact), bottlenecks, changes and files, before/after measurements, tests run and not run, unverified items, remaining risks, and recommendations. Never claim an unmeasured improvement.

## Reference loading

Start with `references/INDEX.md`. Load shared deployment references when you need them (intake, detection rules, access levels, profiling, adaptation, validation, integration). Load only the `references/server-domains/` files for components found in Step 1. Do not load everything.

## Technical limits

Detection rules are heuristics and not re-verified against current provider documentation. Dedicated servers and VPS cannot be told apart from repository files. Real-infrastructure rollback, live profiling and provider-specific behavior are untested unless the developer supplies a safe environment.
