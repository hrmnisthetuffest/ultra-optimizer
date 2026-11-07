# RACE runtime specification (summary)

Authoritative source: the build specification. This document records how the repository implements it.

- **Prohibited**: any modification of BIOS/UEFI, firmware, CPU/GPU clocks, voltage, power, fans, OS power plan or scheduler, registry/kernel/services, driver or global graphics settings, other apps, system-wide environment.
- **Allowed**: reading capabilities through supported, permissioned interfaces; changing the host app's own registered parameters.
- **Tuning registry**: every tunable has ID, purpose, type/range, default and fallback, adjustability, workload categories, requirements, constraints, validation, apply/rollback, risk. Schema: `schemas/tunable-parameter.schema.json`.
- **Profiling levels**: L1 passive, L2 lightweight, L3 active benchmark. Loading-screen path: minimal detection only. No-loading-screen path: no heavy benchmark before 30 minutes of cumulative foreground use, and only when idle/safe.
- **Benchmark**: bounded (target 5-10 minutes active), pausable, abortable, never unbounded stress, no GPU stress for non-GPU apps.
- **Rollback**: original defaults and last-known-good stored; transactional apply; automatic rollback on correctness failure or regression.
- **Executable contract**: `race_reference_model.py` with `tests/test_race_reference_model.py` (11 tests) exercises registry validation, scheduler thresholds and LKG restore. It is a model, not production code.

See `.claude/skills/race/references/core/` for the full working references.
