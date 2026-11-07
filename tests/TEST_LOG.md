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
