# Test log (2026-11-07, Linux, Python 3.14.9, Claude Code 2.1.319)

| Check | Command | Result |
|---|---|---|
| Skill structure (frontmatter, links, 13-section refs, separation, no injection) | `python3 -I tests/validate_skill_structure.py --strict-refs` | 309 passed, 0 failed |
| Schemas and examples | `python3 -I tests/validate_schemas.py` | 24 checks, 0 failures |
| Reference runtime model (spec 18.3 subset) | `python3 -I tests/test_race_reference_model.py` | 11 passed |
| Classification fixtures (spec 18.2, 12 fixtures) | `python3 -I tests/test_fixtures.py` | 3 tests passed |
| Installers (bash, scratch HOME, spaces in paths) | `python3 -I tests/test_installers.py` | 10 passed; real `~/.claude/skills` untouched |
| Live skill discovery (headless `claude -p` in temp project, project-scope install) | manual, once | `race` visible to the model; `optimize` absent from the model's list, as expected for `disable-model-invocation: true`. The `/` menu itself and typed `/race`, `/optimize` were NOT verified. |

## Not run / not verified
- `install.ps1`, `uninstall.ps1`: never executed (no PowerShell); macOS and Windows untested.
- `evals/evals.json` routing/quality cases: authored, **not executed** in fresh sessions; no no-skill baseline comparison.
- Spec 18.3 items needing a real application runtime (GPU driver mismatch, real benchmark pause, telemetry egress) are covered only by the reference model's logic or by documentation.
- Hardware facts: only four NVIDIA compute capabilities are sourced; everything else is generic method marked unverified.
- Official Claude Code skill validation command: none exists in 2.1.319 docs; `claude --debug` not used.

## /ping-optimize (2026-11-07)
- `tests/validate_skill_structure.py --strict-refs`: 612 passed / 0 failed (includes ping-optimize isolation from race/optimize paths).
- `tests/test_ping_optimize_model.py`: 18 tests OK (backoff bounds, retry budget, non-idempotent no-retry, single-flight dedupe, adaptive concurrency limits, simulator loss/latency/outage/rate-limit scenarios).
- `tests/test_installers.py`: 10 OK with three skills (scratch HOME).
- Not verified: `evals/evals.json` prompts were not run in a live model; live `/ping-optimize` resolution not checked; RFC 9110 idempotency/Retry-After text not read; no real-network benchmarks run; `install.ps1` still untested.

## /server-optimize (2026-11-07)
- tests/validate_skill_structure.py --strict-refs: 883 checks, 0 failed.
- tests/test_server_optimize.py: 16 tests OK (six deployment fixtures, secret non-leak, intake items, schema valid/invalid, adaptation model, access rules).
- tests/test_installers.py updated for four skills.
- Not run / not verified: evals not executed on a live model; detection rules heuristic and unverified; no live infrastructure access, so live inspection, staging profiling and production rollback untested; install.ps1/uninstall.ps1 untested; domain references cite no fetched sources.
