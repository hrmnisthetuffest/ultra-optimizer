# Product architecture

Ultra Optimizer is a pair of Claude Code skills with a strict separation of concerns.

| Layer | Skill | Role |
|---|---|---|
| 1 (primary) | `/race` | RACE: Runtime Adaptive Configuration Engine. Builds, integrates, audits, benchmarks and improves hardware-aware, application-internal optimization. |
| 2 | supporting references | Languages, frameworks, architectures, compilers, quality engine. Loaded on demand by `/race` (and mirrored where needed by `/optimize`). |
| 3 | `/optimize` | Universal, device-independent code and engineering optimization. Explicit invocation only (`disable-model-invocation: true`). |
| 4 | developer-selected AI | Optional, never added unless the developer selects it. |

## Separation rules
- `/optimize` never detects live hardware, never selects device-specific settings and never invokes `/race`.
- `/race` never changes device, OS, firmware or driver settings; it only adapts the host application's own registered parameters.
- Each skill folder is self-contained, so either can be installed alone. `/optimize` carries its own copies of the quality checklists.

## Two halves of RACE
1. **Developer Intelligence** (this repository): Claude-time analysis, integration and review.
2. **Runtime Engine** (inside the target app): capability detection, tuning registry, scheduler, evaluator, rollback. The repository provides contracts, schemas and an executable reference model (`.claude/skills/race/templates/race_reference_model.py`), not universal runtime code.

## Progressive disclosure
Each `SKILL.md` is a short router (under 500 lines). Detail lives in `references/`, loaded only when relevant. `scripts/detect_stack.py` selects references from manifests deterministically.
